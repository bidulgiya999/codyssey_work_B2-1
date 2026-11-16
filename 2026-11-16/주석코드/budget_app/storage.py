# 저장소 계층: JSONL 읽기·쓰기, 초기화, 잠금, 원자적 교체를 담당합니다.
# 거래 전체를 배열로 올리지 않고 제너레이터로 순서대로 처리합니다.
"""줄 단위 JSONL 스트리밍, 잠금, 원자적 파일 교체."""
# 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다.
from __future__ import annotations

# JSONL의 한 줄을 dict로 읽거나 JSON 문자열로 저장합니다.
import json
# 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다.
import os
# 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다.
import tempfile
# yield가 있는 함수를 with로 쓰는 컨텍스트 관리자로 바꿉니다.
from contextlib import contextmanager
# 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다.
from pathlib import Path
# 레코드 값·순회 입력·제너레이터 반환·텍스트 스트림의 타입 계약입니다.
from typing import Any, Iterable, Iterator, TextIO

# 거래 모델 검증과 사용자 오류 정보를 저장소에서도 같은 계약으로 사용합니다.
from .models import AppError, Transaction


@contextmanager
# with 문에 쓰기 스트림을 제공하고 정상 완료할 때만 임시 파일을 원본과 교체합니다.
def atomic_text(path: Path, *, newline: str | None = None) -> Iterator[TextIO]:
    """대상과 같은 폴더에 쓰고 flush/fsync 후 교체. 실패 시 원본 유지."""
    # 같은 파일시스템에서 교체하도록 원본의 부모 폴더에 고유 임시 파일을 만듭니다.
    fd, temporary = tempfile.mkstemp(prefix=".budget-", suffix=".tmp", dir=path.parent)
    try:
        # mkstemp가 준 파일 디스크립터를 UTF-8 텍스트 스트림으로 엽니다.
        with os.fdopen(fd, "w", encoding="utf-8", newline=newline) as stream:
            # 호출자의 with 블록으로 스트림을 빌려줍니다. 블록에서 오류가 나면 아래 교체는 건너뜁니다.
            yield stream
            # Python 버퍼의 내용을 운영체제로 보냅니다.
            stream.flush()
            # 운영체제에 해당 파일의 기록을 저장장치로 동기화하도록 요청합니다.
            os.fsync(stream.fileno())
        # 쓰기와 닫기가 모두 끝난 뒤에만 이름을 교체합니다. 원본을 먼저 지우지 않습니다.
        os.replace(temporary, path)
    finally:
        # 성공이면 이미 옮겨져 없고, 실패면 남은 임시 파일을 정리합니다.
        Path(temporary).unlink(missing_ok=True)


# R(Read)의 기반: 줄 단위로 JSON 객체를 해석해 yield하는 제너레이터입니다.
def read_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    # with를 벗어나면 읽기 파일을 닫습니다.
    with path.open(encoding="utf-8") as stream:
        # 파일 객체 반복은 줄 단위 읽기입니다. 1부터 센 줄 번호로 손상 위치를 안내합니다.
        for number, line in enumerate(stream, 1):
            try:
                # JSONL의 한 줄을 Python 값으로 해석합니다.
                row = json.loads(line)
                # 숫자·배열 같은 JSON도 유효한 문법이지만 저장 레코드 스키마로는 거부합니다.
                if not isinstance(row, dict):
                    raise ValueError("JSON 객체가 아닙니다")
            except (ValueError, TypeError) as exc:
                raise AppError(f"{path.name}:{number} 저장 데이터 오류: {exc}",
                               "원본을 백업한 뒤 해당 줄을 복구하세요. 파일을 자동 초기화하지 않습니다.") from None
            # 한 건만 전달하고 다음 요청까지 멈춥니다. 전체 레코드 리스트를 만들지 않습니다.
            yield row


# 객체들을 JSON 한 줄씩 써서 저장합니다. 입력 Iterable을 전체 리스트로 만들지 않습니다.
def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    # 한 줄이라도 직렬화/쓰기 실패 시 기존 파일을 유지하는 공통 저장 경로입니다.
    with atomic_text(path) as stream:
        # 호출자가 넘긴 리스트 또는 제너레이터를 한 건씩 소비합니다.
        for row in records:
            # 한글을 그대로 기록하고 각 JSON 객체 끝에 개행을 붙입니다.
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")


# 데이터 폴더, 세 저장 파일, 초기 카테고리와 명령 단위 잠금을 관리합니다.
class DataStore:
    # 과제의 세 영구 저장 파일입니다. 백업도 이 목록을 그대로 사용합니다.
    FILES = ("transactions.jsonl", "categories.jsonl", "budgets.jsonl")
    # 카테고리 파일이 없거나 0바이트일 때 사용할 초기 목록입니다.
    DEFAULT_CATEGORIES = ("food", "transport", "rent", "salary", "etc")

    # 상대 경로를 절대 경로로 정규화합니다. 이 단계에서는 파일을 만들지 않습니다.
    def __init__(self, directory: Path) -> None:
        # 이후 경로 비교와 파일 접근에서 동일한 절대 경로 기준을 사용합니다.
        self.directory = directory.resolve()

    @contextmanager
    # 명령 실행 동안 잠금을 보유합니다. 초기화 후 제어를 넘기고 마지막에 잠금을 해제합니다.
    def session(self) -> Iterator[None]:
        """모든 CLI 명령의 일관된 스냅샷 및 동시 쓰기 유실 방지."""
        # 최초 실행이라도 부모 폴더까지 만들고, 이미 있으면 그대로 사용합니다.
        self.directory.mkdir(parents=True, exist_ok=True)
        # 거래뿐 아니라 메타데이터도 같은 명령 단위 잠금으로 보호합니다.
        lock = self.directory / ".budget.lock"
        try:
            # O_EXCL로 이미 잠금이 있으면 실패시켜 두 명령의 동시 진입을 막습니다.
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        # 충돌이나 비정상 종료 후 남은 잠금은 자동 삭제하지 않고 사용자에게 안내합니다.
        except FileExistsError:
            raise AppError("다른 가계부 명령이 실행 중이거나 잠금 파일이 남아 있습니다.",
                           f"다른 프로세스 종료를 확인하세요. 비정상 종료였다면 {lock}을 삭제하세요.") from None
        try:
            # 잠금을 잡은 프로세스 id를 기록해 운영 중 확인에 도움을 줍니다.
            with os.fdopen(fd, "w", encoding="utf-8") as stream:
                # 이 값은 진단용입니다. 잠금의 핵심은 O_EXCL로 생성한 파일의 존재입니다.
                stream.write(str(os.getpid()))
            # 초기화는 세 파일 각각에 대해 수행합니다.
            for name in self.FILES:
                path = self.directory / name
                # 기존 파일을 빈 파일로 덮어쓰지 않고, 없는 파일만 생성합니다.
                if not path.exists():
                    # 빈 Iterable을 저장해 빈 JSONL 파일을 만듭니다.
                    write_jsonl(path, ())
            # 0바이트일 때만 기본 카테고리를 생성합니다. 깨진 JSON은 자동 초기화하지 않습니다.
            if self.path("categories").stat().st_size == 0:
                write_jsonl(self.path("categories"), ({"name": n} for n in self.DEFAULT_CATEGORIES))
            # 호출자의 명령 실행 구간으로 제어를 넘깁니다. 그동안 잠금은 유지됩니다.
            yield
        finally:
            # 정상 종료와 예상 예외 모두 finally를 거치며 잠금 파일을 해제합니다.
            lock.unlink(missing_ok=True)

    # 논리 이름 transactions/categories/budgets를 실제 JSONL 파일 경로로 바꿉니다.
    def path(self, name: str) -> Path:
        # Path의 / 연산으로 운영체제 경로 구분자를 안전하게 조합합니다.
        return self.directory / (name + ".jsonl")

    # CSV 내보내기가 실제 저장 파일이나 잠금 파일을 덮어쓰지 못하게 막습니다.
    def protect_output(self, path: Path) -> None:
        # 상대 경로나 심볼릭 링크를 정규화해 덮어쓰기 검사 우회를 줄입니다.
        resolved = path.resolve()
        # 거래·카테고리·예산 파일과 현재 명령의 잠금을 출력 경로에서 제외합니다.
        protected = [self.directory / n for n in (*self.FILES, ".budget.lock")]
        # 경로 문자열뿐 아니라 이미 존재하는 하드 링크의 같은 파일 여부도 검사합니다.
        if any(resolved == p or (resolved.exists() and p.exists() and os.path.samefile(resolved, p))
               for p in protected):
            raise AppError("가계부 저장 파일을 내보내기 대상으로 지정할 수 없습니다.", "별도의 CSV 경로를 지정하세요.")


# 거래 파일의 정렬·조회·병합 재작성을 전담합니다. 카테고리 정책은 서비스 책임입니다.
class TransactionRepository:
    # 처리할 거래 파일 경로를 보관합니다. 가져오기에서는 스테이징 경로도 사용할 수 있습니다.
    def __init__(self, path: Path) -> None:
        # 저장소는 거래 파일 하나의 경로만 알면 동작합니다.
        self.path = path

    # 거래 한 건씩 복원하며 (date, id) 내림차순인지 검사합니다. 거래 전체를 정렬하지 않습니다.
    def iter_all(self) -> Iterator[Transaction]:
        """파일은 (date, id) 내림차순. 한 번에 거래 한 건만 읽는다."""
        # 직전 거래 키 하나만 기억해 정렬을 검사하므로 거래 건수만큼 메모리가 늘지 않습니다.
        previous: tuple[str, str] | None = None
        for number, row in enumerate(read_jsonl(self.path), 1):
            try:
                # 파일의 dict도 모델 검증을 통과해야 거래로 전달합니다.
                transaction = Transaction.from_record(row)
            except (AppError, TypeError, ValueError, AttributeError) as exc:
                raise AppError(f"{self.path.name}:{number} 거래 데이터 오류: {exc}",
                               "파일을 백업하고 해당 레코드를 복구하세요.") from None
            # 이전 값보다 작아야 내림차순입니다. 같은 정렬 키도 손상으로 거부합니다.
            if previous is not None and transaction.key >= previous:
                raise AppError("거래 파일의 최신순 정렬 또는 고유 키가 손상되었습니다.",
                               "백업 파일에서 복구하세요. 저장 파일을 직접 편집하지 마세요.")
            # 다음 거래와 비교할 기준만 갱신합니다.
            previous = transaction.key
            # R(Read) 스트림을 서비스로 한 건씩 전달합니다.
            yield transaction

    # R(Read): id가 같은 거래를 찾으면 반환하고, 끝까지 없으면 AppError를 발생시킵니다.
    def find(self, identifier: str) -> Transaction:
        # id 조회는 인덱스가 없으므로 앞에서부터 최대 n건을 검사합니다.
        for transaction in self.iter_all():
            # 다른 필드가 같아도 id가 같아야 같은 거래입니다.
            if transaction.id == identifier:
                # 첫 일치 거래를 반환합니다. 이후 레코드는 이 조회에서 필요하지 않습니다.
                return transaction
        raise AppError(f"없는 데이터: {identifier}", "list 또는 search로 거래 id를 확인하세요.")

    # C/U/D가 공유하는 저장 연산입니다. 기존 거래를 순회하며 대상 제외 및 새 거래 삽입을 처리합니다.
    def replace(self, identifier: str | None = None,
                replacement: Transaction | None = None) -> None:
        """새 거래를 병합하며 스트리밍 재작성. 수정/삭제 대상은 건너뛴다."""
        # 실제 교체 파일에 들어갈 dict들을 하나씩 생성하는 내부 제너레이터입니다.
        def records() -> Iterator[dict[str, Any]]:
            # 아직 삽입하지 않은 새 거래입니다. 삭제 요청은 None이므로 삽입하지 않습니다.
            pending = replacement
            # 기존 최신순을 유지하며 입력을 한 건씩 읽습니다.
            for old in self.iter_all():
                # U/D에서는 대상의 옛 버전을 제외합니다. C에서는 identifier=None이라 제외하지 않습니다.
                if old.id == identifier:
                    # 대상 거래만 건너뛰며 나머지 레코드는 보존합니다.
                    continue
                # 새 거래가 현재 거래보다 최신이면 이 위치가 삽입 지점입니다.
                if pending is not None and pending.key > old.key:
                    # 새 거래를 한 번만 출력 파일 쪽으로 전달합니다.
                    yield pending.record()
                    # 이미 삽입한 거래를 뒤에서 다시 쓰지 않게 표시합니다.
                    pending = None
                # 대상이 아닌 기존 거래는 필드를 바꾸지 않고 새 파일에 보존합니다.
                yield old.record()
            # 반복이 끝날 때까지 삽입하지 못했다면 가장 오래된 거래이므로 마지막에 추가합니다.
            if pending is not None:
                # 새 거래를 한 번만 출력 파일 쪽으로 전달합니다.
                yield pending.record()
        # 내부 제너레이터가 끝까지 성공한 경우에만 거래 파일을 교체합니다.
        write_jsonl(self.path, records())
