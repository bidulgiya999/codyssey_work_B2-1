"""거래, 카테고리, 예산 및 CSV 입출력의 업무 규칙."""
from __future__ import annotations

import csv
import os
import shutil
import tempfile
import zipfile
from collections import defaultdict
from dataclasses import dataclass, replace
from datetime import datetime
from pathlib import Path
from typing import Any, Iterator
from uuid import uuid4

from .models import AppError, Transaction, parse_tags, positive, valid_date, valid_month, valid_name
from .storage import DataStore, TransactionRepository, atomic_text, read_jsonl, write_jsonl

CSV_FIELDS = ("date", "type", "category", "amount", "memo", "tags")


@dataclass(frozen=True)
class Filters:
    start: str | None = None
    end: str | None = None
    month: str | None = None
    category: str | None = None
    type: str | None = None
    q: str | None = None
    tag: str | None = None

    def __post_init__(self) -> None:
        if self.start:
            valid_date(self.start)
        if self.end:
            valid_date(self.end)
        if self.month:
            valid_month(self.month)
        if self.start and self.end and self.start > self.end:
            raise AppError("시작 날짜가 종료 날짜보다 늦습니다.")
        if self.month and (self.start or self.end):
            raise AppError("--month와 --from/--to는 함께 사용할 수 없습니다.")
        if self.type is not None and self.type not in ("income", "expense"):
            raise AppError("type은 income 또는 expense여야 합니다.")

    def matches(self, t: Transaction) -> bool:
        return (not self.start or t.date >= self.start) and (not self.end or t.date <= self.end) and (
            not self.month or t.date[:7] == self.month) and (
            self.category is None or t.category == self.category) and (
            self.type is None or t.type == self.type) and (
            self.q is None or self.q.casefold() in t.memo.casefold()) and (
            self.tag is None or self.tag in t.tags)


class BudgetService:
    def __init__(self, store: DataStore) -> None:
        self.store = store
        self.transactions = TransactionRepository(store.path("transactions"))

    def categories(self) -> list[str]:
        names = []
        for row in read_jsonl(self.store.path("categories")):
            if set(row) != {"name"} or not isinstance(row["name"], str):
                raise AppError("카테고리 파일 스키마 오류", "categories.jsonl을 백업 후 복구하세요.")
            name = valid_name(row["name"])
            if name != row["name"] or name in names:
                raise AppError("카테고리 파일에 공백 또는 중복 이름이 있습니다.")
            names.append(name)
        return names

    def require_category(self, name: str) -> None:
        if name not in self.categories():
            raise AppError(f"등록되지 않은 카테고리: {name}", "category list로 확인하거나 category add로 등록하세요.")

    def category_add(self, name: str) -> str:
        name = valid_name(name)
        names = self.categories()
        if name in names:
            raise AppError(f"이미 등록된 카테고리: {name}")
        write_jsonl(self.store.path("categories"), ({"name": n} for n in sorted([*names, name])))
        return name

    def category_remove(self, name: str) -> None:
        self.require_category(name)
        if any(t.category == name for t in self.transactions.iter_all()):
            raise AppError("사용 중인 카테고리는 삭제할 수 없습니다.", "해당 거래를 수정하거나 삭제한 뒤 다시 시도하세요.")
        names = self.categories()
        if len(names) == 1:
            raise AppError("마지막 카테고리는 삭제할 수 없습니다.", "새 카테고리를 먼저 추가하세요.")
        write_jsonl(self.store.path("categories"), ({"name": n} for n in names if n != name))

    def add(self, transaction: Transaction) -> None:
        self.require_category(transaction.category)
        self.transactions.replace(replacement=transaction)

    def update(self, identifier: str, changes: dict[str, Any]) -> None:
        if not changes:
            raise AppError("수정할 필드를 하나 이상 지정하세요.")
        old = self.transactions.find(identifier)
        if "amount" in changes:
            changes["amount"] = positive(changes["amount"])
        if "tags" in changes:
            changes["tags"] = parse_tags(changes["tags"])
        updated = replace(old, **changes)
        self.require_category(updated.category)
        self.transactions.replace(identifier, updated)

    def delete(self, identifier: str) -> None:
        self.transactions.find(identifier)
        self.transactions.replace(identifier)

    def search(self, filters: Filters) -> Iterator[Transaction]:
        if filters.category is not None:
            self.require_category(filters.category)
        for transaction in self.transactions.iter_all():
            if filters.matches(transaction):
                yield transaction

    def budgets(self) -> dict[str, int]:
        result: dict[str, int] = {}
        for row in read_jsonl(self.store.path("budgets")):
            if set(row) != {"month", "amount"} or not isinstance(row["month"], str) or type(row["amount"]) is not int:
                raise AppError("예산 파일 스키마 오류", "budgets.jsonl을 백업 후 복구하세요.")
            month = valid_month(row["month"])
            if month in result:
                raise AppError("예산 파일에 중복 월이 있습니다.")
            result[month] = positive(row["amount"])
        return result

    def set_budget(self, month: str, amount: str | int) -> None:
        valid_month(month)
        amount = positive(amount)
        budgets = self.budgets()
        budgets[month] = amount
        write_jsonl(self.store.path("budgets"), ({"month": m, "amount": a} for m, a in sorted(budgets.items())))

    def summary(self, month: str) -> dict[str, Any]:
        income = expense = count = 0
        categories: dict[str, int] = defaultdict(int)
        for t in self.search(Filters(month=month)):
            count += 1
            if t.type == "income":
                income += t.amount
            else:
                expense += t.amount
                categories[t.category] += t.amount
        return {"income": income, "expense": expense, "count": count,
                "categories": sorted(categories.items(), key=lambda x: (-x[1], x[0])),
                "budget": self.budgets().get(month)}

    def import_csv(self, path: Path) -> int:
        """한 행이라도 잘못되면 전체 취소. 디스크 스테이징으로 메모리 상수 유지."""
        categories = set(self.categories())
        # 원본 전체 검증: 손상된 파일을 덮어쓰거나 무시하지 않는다.
        for _ in self.transactions.iter_all():
            pass
        with tempfile.TemporaryDirectory(prefix=".import-", dir=self.store.directory) as temporary:
            staged = Path(temporary) / "transactions.jsonl"
            shutil.copyfile(self.transactions.path, staged)
            repository = TransactionRepository(staged)
            count = 0
            with path.open(encoding="utf-8-sig", newline="") as stream:
                reader = csv.DictReader(stream, strict=True)
                headers = reader.fieldnames
                if (not headers or len(headers) != len(set(headers)) or
                        not set(CSV_FIELDS[:4]).issubset(headers) or set(headers) - set(CSV_FIELDS)):
                    raise AppError("CSV 헤더 오류", "date,type,category,amount,memo,tags 스키마를 사용하세요.")
                for row in reader:
                    try:
                        if None in row or any(v is None for v in row.values()):
                            raise AppError("헤더와 열 개수가 다릅니다.")
                        transaction = Transaction.create(**row)
                        if transaction.category not in categories:
                            raise AppError(f"등록되지 않은 카테고리: {transaction.category}")
                    except AppError as exc:
                        raise AppError(f"CSV {reader.line_num}행: {exc}", "CSV를 수정하세요. 이번 가져오기는 전부 취소되었습니다.") from None
                    repository.replace(replacement=transaction)
                    count += 1
            # 같은 파일시스템 내 원자적 교체. staging의 마지막 쓰기에서 fsync 완료.
            if count:
                os.replace(staged, self.transactions.path)
            return count

    def export_csv(self, path: Path, filters: Filters) -> int:
        if not (filters.month or filters.start or filters.end):
            raise AppError("내보내기에는 --month 또는 --from/--to 조건이 필요합니다.")
        self.store.protect_output(path)
        count = 0
        with atomic_text(path, newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=CSV_FIELDS)
            writer.writeheader()
            for t in self.search(filters):
                row = {key: getattr(t, key) for key in CSV_FIELDS}
                row["tags"] = ",".join(t.tags)
                writer.writerow(row)
                count += 1
        return count

    def backup(self) -> Path:
        folder = self.store.directory / "backups"
        folder.mkdir(exist_ok=True)
        path = folder / f"backup-{datetime.now():%Y%m%d-%H%M%S-%f}-{uuid4().hex[:8]}.zip"
        try:
            with zipfile.ZipFile(path, "x", zipfile.ZIP_DEFLATED) as archive:
                for filename in self.store.FILES:
                    archive.write(self.store.directory / filename, arcname=filename)
        except BaseException:
            path.unlink(missing_ok=True)
            raise
        return path
