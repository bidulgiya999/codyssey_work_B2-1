# 서비스 계층: 거래 CRUD와 검색·집계·카테고리·예산의 업무 규칙을 담당합니다.
# CLI와 저장소 사이에서 정책을 적용하며, 화면에 출력할 자료를 반환합니다.
"""거래, 카테고리, 예산 및 CSV 입출력의 업무 규칙."""
# 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다.
from __future__ import annotations

# 쉼표·인용·개행을 직접 나누지 않고 표준 CSV 규칙으로 처리합니다.
import csv
# 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다.
import os
# 가져오기를 원본이 아닌 사본에서 처리하도록 파일을 복사합니다.
import shutil
# 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다.
import tempfile
# 세 저장 파일의 ZIP 백업을 만들거나 테스트에서 검사합니다.
import zipfile
# 처음 보는 지출 카테고리의 누적 합계를 0에서 시작합니다.
from collections import defaultdict
# 검색 조건 모델과 불변 거래의 일부 필드만 바꾼 사본을 만듭니다.
from dataclasses import dataclass, replace
# 백업 파일 이름에 실행 시각을 넣습니다.
from datetime import datetime
# 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다.
from pathlib import Path
# 서비스 결과와 한 건씩 전달하는 거래 스트림의 타입입니다.
from typing import Any, Iterator
# 외부 카운터 파일 없이 충돌 가능성이 매우 낮은 무작위 거래 id를 만듭니다.
from uuid import uuid4

# 서비스가 모델 생성과 공통 입력 검증 함수를 재사용합니다.
from .models import AppError, Transaction, parse_tags, positive, valid_date, valid_month, valid_name
# 서비스가 직접 저수준 I/O를 중복 구현하지 않고 공통 저장 기능에 위임합니다.
from .storage import DataStore, TransactionRepository, atomic_text, read_jsonl, write_jsonl

# 내보내기 열 순서이며 앞의 네 열은 가져오기에 필수입니다.
CSV_FIELDS = ("date", "type", "category", "amount", "memo", "tags")


@dataclass(frozen=True)
# 검색 조건을 담는 불변 dataclass입니다. None은 해당 조건을 지정하지 않았다는 뜻입니다.
class Filters:
    # 포함할 시작 날짜입니다. None이면 하한이 없습니다.
    start: str | None = None
    # 포함할 종료 날짜입니다. None이면 상한이 없습니다.
    end: str | None = None
    # YYYY-MM 월 조건입니다. 날짜 범위와 동시에 지정하지 않습니다.
    month: str | None = None
    # 정확히 일치해야 하는 등록 카테고리입니다.
    category: str | None = None
    # 수입 또는 지출만 선택하는 조건입니다.
    type: str | None = None
    # 메모에서 찾을 부분 문자열입니다.
    q: str | None = None
    # 태그 목록에 완전히 일치하는 값이 있는지 검사합니다.
    tag: str | None = None

    # 검색 실행 전에 날짜·월·기간 순서와 조건의 충돌을 검증합니다.
    def __post_init__(self) -> None:
        # 시작 날짜가 지정된 경우에만 형식을 검증합니다.
        if self.start:
            valid_date(self.start)
        # 종료 날짜도 별도로 검증합니다.
        if self.end:
            valid_date(self.end)
        # 월 조건은 YYYY-MM이 유효한지 확인합니다.
        if self.month:
            valid_month(self.month)
        # 두 경계의 형식 검증 후 사전식 비교로 날짜 순서를 검사합니다.
        if self.start and self.end and self.start > self.end:
            raise AppError("시작 날짜가 종료 날짜보다 늦습니다.")
        # 서로 다른 기간 표현의 충돌을 막아 사용자 의도를 명확하게 합니다.
        if self.month and (self.start or self.end):
            raise AppError("--month와 --from/--to는 함께 사용할 수 없습니다.")
        # Filters를 CLI 밖에서 직접 생성해도 타입 제한을 적용합니다.
        if self.type is not None and self.type not in ("income", "expense"):
            raise AppError("type은 income 또는 expense여야 합니다.")

    # 거래 한 건이 모든 조건(AND)을 만족하면 True, 아니면 False를 반환합니다.
    def matches(self, t: Transaction) -> bool:
        # 미지정 조건은 통과합니다. 기간 경계 포함·카테고리/타입 일치·메모 casefold·태그 포함을 AND로 결합합니다.
        return (not self.start or t.date >= self.start) and (not self.end or t.date <= self.end) and (
            not self.month or t.date[:7] == self.month) and (
            self.category is None or t.category == self.category) and (
            self.type is None or t.type == self.type) and (
            self.q is None or self.q.casefold() in t.memo.casefold()) and (
            self.tag is None or self.tag in t.tags)


# 업무 규칙 담당 클래스입니다. 직접 입력받거나 출력하지 않고 저장소를 조합합니다.
class BudgetService:
    # 데이터 경로 관리자와 거래 저장소를 연결합니다. 서비스 호출은 CLI 잠금 안에서 이루어집니다.
    def __init__(self, store: DataStore) -> None:
        # 세 파일과 경로·보호 정책은 전달받은 DataStore에 위임합니다.
        self.store = store
        # 거래 읽기와 병합 재작성을 TransactionRepository에 위임합니다.
        self.transactions = TransactionRepository(store.path("transactions"))

    # 카테고리 파일의 스키마와 중복을 검증하고 이름 목록을 반환합니다.
    def categories(self) -> list[str]:
        # 거래와 달리 작은 메타데이터 목록은 메모리에 모읍니다.
        names = []
        # 카테고리는 각 줄에 name 하나만 있는 JSON 객체로 저장합니다.
        for row in read_jsonl(self.store.path("categories")):
            # 열 누락·추가와 문자열 아닌 이름을 저장 손상으로 보고합니다.
            if set(row) != {"name"} or not isinstance(row["name"], str):
                raise AppError("카테고리 파일 스키마 오류", "categories.jsonl을 백업 후 복구하세요.")
            # 이름 형식을 검증하고 정리한 값을 얻습니다.
            name = valid_name(row["name"])
            # 저장 파일에는 앞뒤 공백이나 중복 이름이 남아 있으면 안 됩니다.
            if name != row["name"] or name in names:
                raise AppError("카테고리 파일에 공백 또는 중복 이름이 있습니다.")
            # 검증을 통과한 이름만 결과 목록에 포함합니다.
            names.append(name)
        return names

    # 여러 기능에서 공통으로 쓰는 등록 여부 검사입니다. 미등록 카테고리는 저장 전에 거부합니다.
    def require_category(self, name: str) -> None:
        # 거래가 참조할 수 있는 카테고리인지 검사합니다.
        if name not in self.categories():
            raise AppError(f"등록되지 않은 카테고리: {name}", "category list로 확인하거나 category add로 등록하세요.")

    # 카테고리 C: 이름 정리 후 중복을 거부하고 추가된 목록을 안전하게 저장합니다.
    def category_add(self, name: str) -> str:
        # 대화형 입력의 앞뒤 공백을 정리한 뒤 중복 여부를 판단합니다.
        name = valid_name(name)
        # 저장된 이름을 읽어 변경 전 목록을 확보합니다.
        names = self.categories()
        # 같은 이름을 두 번 추가하지 않습니다.
        if name in names:
            raise AppError(f"이미 등록된 카테고리: {name}")
        # 기존 이름과 새 이름을 정렬해 원자적으로 저장합니다.
        write_jsonl(self.store.path("categories"), ({"name": n} for n in sorted([*names, name])))
        return name

    # 카테고리 D: 사용 중이거나 마지막 남은 이름은 보호하고 나머지 이름만 저장합니다.
    def category_remove(self, name: str) -> None:
        self.require_category(name)
        # 거래를 스트리밍 검사하다 첫 사용 사례를 발견하면 삭제를 차단합니다.
        if any(t.category == name for t in self.transactions.iter_all()):
            raise AppError("사용 중인 카테고리는 삭제할 수 없습니다.", "해당 거래를 수정하거나 삭제한 뒤 다시 시도하세요.")
        # 저장된 이름을 읽어 변경 전 목록을 확보합니다.
        names = self.categories()
        # 빈 카테고리 파일의 기본값 재생성과 혼동되지 않도록 마지막 이름은 보호합니다.
        if len(names) == 1:
            raise AppError("마지막 카테고리는 삭제할 수 없습니다.", "새 카테고리를 먼저 추가하세요.")
        # 삭제 대상 이름만 제외하고 나머지 카테고리를 보존합니다.
        write_jsonl(self.store.path("categories"), ({"name": n} for n in names if n != name))

    # 거래 C(Create): 등록된 카테고리인지 확인한 후 새 거래를 정렬 병합 저장합니다.
    def add(self, transaction: Transaction) -> None:
        # C: 모델 형식 검증과 별개로 등록 카테고리 정책을 확인합니다.
        self.require_category(transaction.category)
        # C: 제외할 id 없이 새 거래만 정렬 순서에 삽입합니다.
        self.transactions.replace(replacement=transaction)

    # 거래 U(Update): 기존 id를 찾고 지정된 필드만 검증·변경한 새 객체로 교체합니다.
    def update(self, identifier: str, changes: dict[str, Any]) -> None:
        # U: 아무 필드도 지정하지 않은 요청은 실수일 수 있으므로 거부합니다.
        if not changes:
            raise AppError("수정할 필드를 하나 이상 지정하세요.")
        # U: 대상 존재를 먼저 확인합니다. 없는 id면 이 단계에서 실패합니다.
        old = self.transactions.find(identifier)
        # CLI 옵션은 문자열이므로 수정 금액도 int로 검증·변환합니다.
        if "amount" in changes:
            changes["amount"] = positive(changes["amount"])
        # 태그 문자열을 모델이 요구하는 tuple로 변환합니다. 빈 문자열이면 태그를 비웁니다.
        if "tags" in changes:
            changes["tags"] = parse_tags(changes["tags"])
        # frozen 객체를 직접 수정하지 않고 선택 필드만 바꾼 새 dataclass를 만듭니다.
        updated = replace(old, **changes)
        # 수정 후에도 등록되지 않은 카테고리를 참조할 수 없습니다.
        self.require_category(updated.category)
        # U: 기존 id 거래를 제외하고 같은 id의 새 객체를 날짜 정렬에 맞춰 삽입합니다.
        self.transactions.replace(identifier, updated)

    # 거래 D(Delete): id 존재를 먼저 확인하고 해당 거래를 제외한 파일로 교체합니다.
    def delete(self, identifier: str) -> None:
        # D: 파일을 쓰기 전에 존재 여부를 검사해 없는 id를 명확히 안내합니다.
        self.transactions.find(identifier)
        # D: 대체 거래를 주지 않아 해당 id만 빼고 저장합니다.
        self.transactions.replace(identifier)

    # 거래 R(Read): 거래 스트림에서 조건을 통과한 것만 yield하여 CLI로 전달합니다.
    def search(self, filters: Filters) -> Iterator[Transaction]:
        # R: 카테고리 이름의 오타를 결과 없음으로 숨기지 않고 명확히 안내합니다.
        if filters.category is not None:
            self.require_category(filters.category)
        # R: 거래를 한 건씩 받습니다. list도 비어 있는 Filters로 이 경로를 재사용합니다.
        for transaction in self.transactions.iter_all():
            # R: 모든 검색 조건을 통과한 거래만 다음 단계로 보냅니다.
            if filters.matches(transaction):
                # R: 전체 결과 리스트 대신 필요한 시점에 한 거래씩 전달합니다.
                yield transaction

    # 예산을 월→금액 dict로 읽습니다. 중복 월·잘못된 스키마는 손상으로 취급합니다.
    def budgets(self) -> dict[str, int]:
        # 월 문자열을 키로, 예산 금액 int를 값으로 쓰는 계약입니다.
        result: dict[str, int] = {}
        # 예산도 JSONL의 레코드 단위로 읽습니다.
        for row in read_jsonl(self.store.path("budgets")):
            # 예산 스키마와 실제 자료형을 함께 검사합니다.
            if set(row) != {"month", "amount"} or not isinstance(row["month"], str) or type(row["amount"]) is not int:
                raise AppError("예산 파일 스키마 오류", "budgets.jsonl을 백업 후 복구하세요.")
            month = valid_month(row["month"])
            # 한 달에 여러 예산 레코드가 있으면 임의 선택하지 않고 오류로 안내합니다.
            if month in result:
                raise AppError("예산 파일에 중복 월이 있습니다.")
            result[month] = positive(row["amount"])
        return result

    # 예산 C/U: 처음인 월은 추가하고 이미 있는 월은 금액을 갱신한 뒤 저장합니다.
    def set_budget(self, month: str, amount: str | int) -> None:
        valid_month(month)
        amount = positive(amount)
        budgets = self.budgets()
        # dict 대입으로 없는 월 추가(C)와 기존 월 갱신(U)을 같은 코드로 처리합니다.
        budgets[month] = amount
        # 월별 설정 전체를 작은 메타데이터 파일에 안전하게 교체 저장합니다.
        write_jsonl(self.store.path("budgets"), ({"month": m, "amount": a} for m, a in sorted(budgets.items())))

    # 월 거래를 한 번 순회하며 수입·지출·건수·카테고리 지출을 누적한 결과를 반환합니다.
    def summary(self, month: str) -> dict[str, Any]:
        # 거래 전체 대신 합계와 개수만 유지합니다.
        income = expense = count = 0
        # defaultdict(int)는 처음 보는 카테고리의 합계를 0에서 시작하게 합니다.
        categories: dict[str, int] = defaultdict(int)
        # 선택 월에 속한 거래 스트림만 집계합니다.
        for t in self.search(Filters(month=month)):
            count += 1
            # type을 기준으로 수입 합계와 지출 합계를 분리합니다.
            if t.type == "income":
                income += t.amount
            else:
                expense += t.amount
                # 수입은 순위에 넣지 않고 지출만 카테고리별로 누적합니다.
                categories[t.category] += t.amount
        # 합계와 예산을 반환합니다. 카테고리는 금액 내림차순·이름 오름차순 정렬입니다.
        return {"income": income, "expense": expense, "count": count,
                "categories": sorted(categories.items(), key=lambda x: (-x[1], x[0])),
                "budget": self.budgets().get(month)}

    # CSV 일괄 C: 원본이 아닌 스테이징 사본에 병합하고 모든 행이 성공해야 최종 반영합니다.
    def import_csv(self, path: Path) -> int:
        """한 행이라도 잘못되면 전체 취소. 디스크 스테이징으로 메모리 상수 유지."""
        # 가져오는 행마다 파일을 다시 읽지 않도록 카테고리 이름을 집합으로 준비합니다.
        categories = set(self.categories())
        # 원본 전체 검증: 손상된 파일을 덮어쓰거나 무시하지 않는다.
        for _ in self.transactions.iter_all():
            pass
        # 원본 폴더 안에 스테이징 공간을 만들고 종료 시 자동 정리합니다.
        with tempfile.TemporaryDirectory(prefix=".import-", dir=self.store.directory) as temporary:
            # 실패해도 원본 거래 파일에는 영향이 없도록 별도 파일을 사용합니다.
            staged = Path(temporary) / "transactions.jsonl"
            # 현재 거래를 사본으로 보존해 새 CSV 행을 기존 거래와 합칠 수 있게 합니다.
            shutil.copyfile(self.transactions.path, staged)
            # 같은 저장소 구현을 임시 경로에 적용해 병합 로직을 재사용합니다.
            repository = TransactionRepository(staged)
            count = 0
            # UTF-8과 UTF-8 BOM을 모두 읽습니다. newline=""은 csv 모듈이 개행을 처리하게 합니다.
            with path.open(encoding="utf-8-sig", newline="") as stream:
                # 헤더를 키로 각 행을 dict로 읽고 잘못된 CSV 인용 문법도 검사합니다.
                reader = csv.DictReader(stream, strict=True)
                # 첫 행에서 선언한 열 이름을 검증합니다.
                headers = reader.fieldnames
                # 헤더 없음·중복·필수 열 누락·알 수 없는 열을 거부합니다. 선택 열 두 개는 없어도 됩니다.
                if (not headers or len(headers) != len(set(headers)) or
                        not set(CSV_FIELDS[:4]).issubset(headers) or set(headers) - set(CSV_FIELDS)):
                    raise AppError("CSV 헤더 오류", "date,type,category,amount,memo,tags 스키마를 사용하세요.")
                # CSV도 한 행씩 소비해 입력 전체를 배열로 만들지 않습니다.
                for row in reader:
                    try:
                        # 헤더보다 많거나 적은 필드가 있는 행은 암묵적으로 보정하지 않습니다.
                        if None in row or any(v is None for v in row.values()):
                            raise AppError("헤더와 열 개수가 다릅니다.")
                        # 각 행은 새 id를 발급받습니다. 같은 CSV 재가져오기는 새 거래로 추가됩니다.
                        transaction = Transaction.create(**row)
                        if transaction.category not in categories:
                            raise AppError(f"등록되지 않은 카테고리: {transaction.category}")
                    # 문제가 난 CSV 줄 번호를 붙이고 전체 취소 사실을 안내합니다.
                    except AppError as exc:
                        raise AppError(f"CSV {reader.line_num}행: {exc}", "CSV를 수정하세요. 이번 가져오기는 전부 취소되었습니다.") from None
                    # 원본이 아닌 스테이징 파일에 이 행을 정렬 병합합니다.
                    repository.replace(replacement=transaction)
                    count += 1
            # 같은 파일시스템 내 원자적 교체. staging의 마지막 쓰기에서 fsync 완료.
            # 빈 CSV는 원본을 교체할 필요가 없습니다.
            if count:
                # 모든 행을 통과했을 때만 최종 반영합니다. 이전 오류는 원본에 전혀 반영되지 않습니다.
                os.replace(staged, self.transactions.path)
            return count

    # CSV R/출력: 기간 조건에 맞는 거래를 표준 CSV 스키마로 기록하고 건수를 반환합니다.
    def export_csv(self, path: Path, filters: Filters) -> int:
        # 내보내기 범위를 의도적으로 선택하도록 최소 하나의 기간 조건을 요구합니다.
        if not (filters.month or filters.start or filters.end):
            raise AppError("내보내기에는 --month 또는 --from/--to 조건이 필요합니다.")
        # 사용자 출력 경로가 실제 저장 파일을 가리키면 작업을 거부합니다.
        self.store.protect_output(path)
        count = 0
        # 내보내기 실패도 기존 CSV를 훼손하지 않도록 같은 안전 쓰기를 사용합니다.
        with atomic_text(path, newline="") as stream:
            # 고정된 CSV 필드 순서에 맞춰 dict를 기록합니다.
            writer = csv.DictWriter(stream, fieldnames=CSV_FIELDS)
            # 조회 결과가 0건이어도 스키마를 알 수 있게 헤더는 기록합니다.
            writer.writeheader()
            # R: 조건을 통과한 거래를 순서대로 기록합니다.
            for t in self.search(filters):
                # 모델에서 교환용 여섯 필드만 골라 id를 제외합니다.
                row = {key: getattr(t, key) for key in CSV_FIELDS}
                # tuple 태그를 쉼표 문자열로 바꿉니다. 쉼표 인용은 csv 모듈이 처리합니다.
                row["tags"] = ",".join(t.tags)
                # 한글·쉼표·큰따옴표·개행을 표준 CSV 규칙으로 기록합니다.
                writer.writerow(row)
                count += 1
        return count

    # 보너스 기능: 잠금 안에서 세 JSONL 파일을 ZIP으로 복사하고 생성 경로를 반환합니다.
    def backup(self) -> Path:
        # 사용자가 선택한 데이터 폴더 안에 backups 하위 폴더를 사용합니다.
        folder = self.store.directory / "backups"
        folder.mkdir(exist_ok=True)
        # 시각의 마이크로초와 UUID 일부를 붙여 백업 이름 충돌을 줄입니다.
        path = folder / f"backup-{datetime.now():%Y%m%d-%H%M%S-%f}-{uuid4().hex[:8]}.zip"
        try:
            # x 모드는 같은 이름 파일이 있으면 덮어쓰지 않고 실패합니다.
            with zipfile.ZipFile(path, "x", zipfile.ZIP_DEFLATED) as archive:
                for filename in self.store.FILES:
                    # 압축 내부에는 절대 경로 대신 파일 이름만 기록합니다.
                    archive.write(self.store.directory / filename, arcname=filename)
        # 중단까지 포함해 생성 실패한 불완전 ZIP을 남기지 않도록 정리한 후 다시 오류를 전달합니다.
        except BaseException:
            path.unlink(missing_ok=True)
            raise
        return path
