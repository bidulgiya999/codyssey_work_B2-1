"""줄 단위 JSONL 스트리밍, 잠금, 원자적 파일 교체."""
from __future__ import annotations

import json
import os
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterable, Iterator, TextIO

from .models import AppError, Transaction


@contextmanager
def atomic_text(path: Path, *, newline: str | None = None) -> Iterator[TextIO]:
    """대상과 같은 폴더에 쓰고 flush/fsync 후 교체. 실패 시 원본 유지."""
    fd, temporary = tempfile.mkstemp(prefix=".budget-", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline=newline) as stream:
            yield stream
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def read_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    with path.open(encoding="utf-8") as stream:
        for number, line in enumerate(stream, 1):
            try:
                row = json.loads(line)
                if not isinstance(row, dict):
                    raise ValueError("JSON 객체가 아닙니다")
            except (ValueError, TypeError) as exc:
                raise AppError(f"{path.name}:{number} 저장 데이터 오류: {exc}",
                               "원본을 백업한 뒤 해당 줄을 복구하세요. 파일을 자동 초기화하지 않습니다.") from None
            yield row


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    with atomic_text(path) as stream:
        for row in records:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")


class DataStore:
    FILES = ("transactions.jsonl", "categories.jsonl", "budgets.jsonl")
    DEFAULT_CATEGORIES = ("food", "transport", "rent", "salary", "etc")

    def __init__(self, directory: Path) -> None:
        self.directory = directory.resolve()

    @contextmanager
    def session(self) -> Iterator[None]:
        """모든 CLI 명령의 일관된 스냅샷 및 동시 쓰기 유실 방지."""
        self.directory.mkdir(parents=True, exist_ok=True)
        lock = self.directory / ".budget.lock"
        try:
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            raise AppError("다른 가계부 명령이 실행 중이거나 잠금 파일이 남아 있습니다.",
                           f"다른 프로세스 종료를 확인하세요. 비정상 종료였다면 {lock}을 삭제하세요.") from None
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as stream:
                stream.write(str(os.getpid()))
            for name in self.FILES:
                path = self.directory / name
                if not path.exists():
                    write_jsonl(path, ())
            if self.path("categories").stat().st_size == 0:
                write_jsonl(self.path("categories"), ({"name": n} for n in self.DEFAULT_CATEGORIES))
            yield
        finally:
            lock.unlink(missing_ok=True)

    def path(self, name: str) -> Path:
        return self.directory / (name + ".jsonl")

    def protect_output(self, path: Path) -> None:
        resolved = path.resolve()
        protected = [self.directory / n for n in (*self.FILES, ".budget.lock")]
        if any(resolved == p or (resolved.exists() and p.exists() and os.path.samefile(resolved, p))
               for p in protected):
            raise AppError("가계부 저장 파일을 내보내기 대상으로 지정할 수 없습니다.", "별도의 CSV 경로를 지정하세요.")


class TransactionRepository:
    def __init__(self, path: Path) -> None:
        self.path = path

    def iter_all(self) -> Iterator[Transaction]:
        """파일은 (date, id) 내림차순. 한 번에 거래 한 건만 읽는다."""
        previous: tuple[str, str] | None = None
        for number, row in enumerate(read_jsonl(self.path), 1):
            try:
                transaction = Transaction.from_record(row)
            except (AppError, TypeError, ValueError, AttributeError) as exc:
                raise AppError(f"{self.path.name}:{number} 거래 데이터 오류: {exc}",
                               "파일을 백업하고 해당 레코드를 복구하세요.") from None
            if previous is not None and transaction.key >= previous:
                raise AppError("거래 파일의 최신순 정렬 또는 고유 키가 손상되었습니다.",
                               "백업 파일에서 복구하세요. 저장 파일을 직접 편집하지 마세요.")
            previous = transaction.key
            yield transaction

    def find(self, identifier: str) -> Transaction:
        for transaction in self.iter_all():
            if transaction.id == identifier:
                return transaction
        raise AppError(f"없는 데이터: {identifier}", "list 또는 search로 거래 id를 확인하세요.")

    def replace(self, identifier: str | None = None,
                replacement: Transaction | None = None) -> None:
        """새 거래를 병합하며 스트리밍 재작성. 수정/삭제 대상은 건너뛴다."""
        def records() -> Iterator[dict[str, Any]]:
            pending = replacement
            for old in self.iter_all():
                if old.id == identifier:
                    continue
                if pending is not None and pending.key > old.key:
                    yield pending.record()
                    pending = None
                yield old.record()
            if pending is not None:
                yield pending.record()
        write_jsonl(self.path, records())
