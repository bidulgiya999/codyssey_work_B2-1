"""입력 계약과 영구 저장 모델."""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from datetime import date
from typing import Any
from uuid import uuid4


class AppError(Exception):
    def __init__(self, message: str, hint: str = "--help에서 사용 방법을 확인하세요.") -> None:
        super().__init__(message)
        self.hint = hint


def valid_date(value: str) -> str:
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        raise AppError("날짜 형식 오류", "YYYY-MM-DD 형식으로 입력하세요. 예: 2024-01-15")
    try:
        date.fromisoformat(value)
    except ValueError:
        raise AppError("존재하지 않는 날짜", "달력에 있는 날짜를 입력하세요.") from None
    return value


def valid_month(value: str) -> str:
    valid_date(value + "-01")
    return value


def positive(value: Any) -> int:
    text = str(value)
    if (isinstance(value, bool) or len(text) > 19 or not re.fullmatch(r"[0-9]+", text)
            or not 0 < int(text) <= 9223372036854775807):
        raise AppError("금액/개수는 양수 정수여야 합니다.", "1~9223372036854775807 범위의 정수를 입력하세요.")
    return int(value)


def valid_name(value: str) -> str:
    value = value.strip()
    if not value or any(ord(c) < 32 for c in value):
        raise AppError("카테고리명은 비어 있거나 제어 문자를 포함할 수 없습니다.")
    return value


def parse_tags(value: str) -> tuple[str, ...]:
    return tuple(dict.fromkeys(tag.strip() for tag in value.split(",") if tag.strip()))


@dataclass(frozen=True)
class Transaction:
    id: str
    type: str
    date: str
    amount: int
    category: str
    memo: str = ""
    tags: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.id, str) or not self.id.strip():
            raise AppError("거래 id가 비어 있습니다.")
        if self.type not in ("income", "expense"):
            raise AppError("type은 income 또는 expense여야 합니다.")
        valid_date(self.date)
        if type(self.amount) is not int:
            raise AppError("저장된 금액은 정수여야 합니다.")
        positive(self.amount)
        if valid_name(self.category) != self.category:
            raise AppError("카테고리 앞뒤 공백을 제거하세요.")
        if not isinstance(self.memo, str) or not isinstance(self.tags, tuple):
            raise AppError("메모/태그 자료형이 올바르지 않습니다.")
        if any(not isinstance(t, str) or not t.strip() or "," in t for t in self.tags):
            raise AppError("태그는 쉼표가 없는 비어 있지 않은 문자열이어야 합니다.")

    @property
    def key(self) -> tuple[str, str]:
        return self.date, self.id

    def record(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_record(cls, row: dict[str, Any]) -> Transaction:
        try:
            fields = dict(row)
            tags = fields.get("tags", [])
            if not isinstance(tags, list):
                raise AppError("저장된 tags는 배열이어야 합니다.")
            fields["tags"] = tuple(tags)
            return cls(**fields)
        except (TypeError, ValueError, AttributeError) as exc:
            raise AppError(f"거래 스키마 오류: {exc}") from None

    @classmethod
    def create(cls, *, date: str, type: str, category: str, amount: Any,
               memo: str = "", tags: str = "") -> Transaction:
        return cls("TX-" + uuid4().hex, type, date, positive(amount),
                   valid_name(category), memo, parse_tags(tags))
