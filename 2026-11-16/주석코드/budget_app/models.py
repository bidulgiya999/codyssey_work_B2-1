# 모델 계층: 거래의 형태와 입력 값의 유효성을 정의합니다.
# 파일 저장과 화면 출력은 하지 않고, 잘못된 값은 AppError로 알립니다.
"""입력 계약과 영구 저장 모델."""
# 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다.
from __future__ import annotations

# 정규식으로 날짜와 양수 숫자 문자열의 형식을 검사합니다.
import re
# dataclass 생성자·비교 기능과 저장용 dict 변환을 사용합니다.
from dataclasses import asdict, dataclass
# 실제 달력 날짜와 윤년을 검증합니다.
from datetime import date
# 검증 전 입력처럼 여러 자료형을 받을 수 있는 값을 표시합니다.
from typing import Any
# 외부 카운터 파일 없이 충돌 가능성이 매우 낮은 무작위 거래 id를 만듭니다.
from uuid import uuid4


# 사용자에게 보여줄 원인(message)과 해결 방법(hint)을 함께 보관하는 예외입니다.
class AppError(Exception):
    # Exception에 원인을 저장하고 별도 hint 속성으로 해결 안내를 전달합니다.
    def __init__(self, message: str, hint: str = "--help에서 사용 방법을 확인하세요.") -> None:
        # 예외의 기본 문자열은 원인 메시지입니다. 데코레이터가 str(exc)로 출력합니다.
        super().__init__(message)
        # 원인과 해결 방법을 분리해 CLI에서 각각 안내할 수 있게 합니다.
        self.hint = hint


# 문자열 모양과 실제 달력 날짜를 모두 검증하고 원래 날짜 문자열을 반환합니다.
def valid_date(value: str) -> str:
    # 정규식 전체 일치로 YYYY-MM-DD의 자리 수와 하이픈 위치를 강제합니다.
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        raise AppError("날짜 형식 오류", "YYYY-MM-DD 형식으로 입력하세요. 예: 2024-01-15")
    try:
        # 문자 모양뿐 아니라 2월 30일처럼 달력에 없는 날짜까지 거부합니다.
        date.fromisoformat(value)
    except ValueError:
        # from None은 원래 예외 연결 표시를 생략합니다. 최종 화면 안내는 데코레이터가 담당합니다.
        raise AppError("존재하지 않는 날짜", "달력에 있는 날짜를 입력하세요.") from None
    return value


# YYYY-MM에 -01을 붙여 날짜 검증을 재사용하고 유효한 월 문자열을 반환합니다.
def valid_month(value: str) -> str:
    # 매월 1일을 붙이면 월 검증에 날짜 검증 로직을 재사용할 수 있습니다.
    valid_date(value + "-01")
    return value


# 입력 문자열/정수를 허용 범위의 양수 int로 바꿉니다. 금액·limit·top에 재사용합니다.
def positive(value: Any) -> int:
    # 문자열로 통일해 입력 길이·숫자 형식을 먼저 검사합니다.
    text = str(value)
    # bool은 int의 하위 타입이므로 별도로 거부합니다. 길이 제한은 거대한 정수 변환도 막습니다.
    if (isinstance(value, bool) or len(text) > 19 or not re.fullmatch(r"[0-9]+", text)
            or not 0 < int(text) <= 9223372036854775807):
        raise AppError("금액/개수는 양수 정수여야 합니다.", "1~9223372036854775807 범위의 정수를 입력하세요.")
    # 모든 검사를 통과한 값만 정수로 바꿔 호출자에게 전달합니다.
    return int(value)


# 앞뒤 공백을 정리하고 빈 이름·제어 문자가 없는 카테고리명을 반환합니다.
def valid_name(value: str) -> str:
    # 카테고리 입력 앞뒤의 불필요한 공백을 제거합니다.
    value = value.strip()
    # 빈 이름과 줄바꿈·탭 등 제어 문자는 카테고리로 저장하지 않습니다.
    if not value or any(ord(c) < 32 for c in value):
        raise AppError("카테고리명은 비어 있거나 제어 문자를 포함할 수 없습니다.")
    return value


# 쉼표 분리 → 공백 정리 → 빈 태그 제외 → 순서를 유지한 중복 제거 → tuple 반환.
def parse_tags(value: str) -> tuple[str, ...]:
    # dict의 삽입 순서를 이용해 원래 순서를 유지하면서 태그 중복을 제거합니다.
    return tuple(dict.fromkeys(tag.strip() for tag in value.split(",") if tag.strip()))


@dataclass(frozen=True)
# 한 거래의 계약입니다. dataclass가 생성자를 만들고 frozen=True가 직접 변경을 막습니다.
class Transaction:
    # 고유 거래 식별자입니다. 수정·삭제에서 이 값을 사용합니다.
    id: str
    # 거래 종류: income(수입) 또는 expense(지출).
    type: str
    # 검증된 YYYY-MM-DD 문자열은 날짜 순서와 사전식 비교 순서가 같습니다.
    date: str
    # 양수 원 단위 금액입니다. 지출 여부는 부호 대신 type으로 구분합니다.
    amount: int
    # 카테고리명 자체의 형식은 모델에서, 등록 여부는 서비스에서 검사합니다.
    category: str
    # 선택 메모의 기본값은 빈 문자열입니다.
    memo: str = ""
    # 불변 tuple을 사용해 frozen 거래 안의 태그도 임의 변경을 피합니다.
    tags: tuple[str, ...] = ()

    # 생성자 실행 직후 호출되어 객체 자체가 유효한 거래인지 검증합니다.
    def __post_init__(self) -> None:
        # 저장 파일을 복원할 때도 id가 유효한 문자열이어야 합니다.
        if not isinstance(self.id, str) or not self.id.strip():
            raise AppError("거래 id가 비어 있습니다.")
        # 정해진 두 종류만 받아 수입·지출 집계의 기준을 고정합니다.
        if self.type not in ("income", "expense"):
            raise AppError("type은 income 또는 expense여야 합니다.")
        # 객체를 직접 만들 때도 날짜 검증을 건너뛸 수 없습니다.
        valid_date(self.date)
        # 저장 모델에서는 문자열 숫자와 bool을 허용하지 않고 정확한 int만 허용합니다.
        if type(self.amount) is not int:
            raise AppError("저장된 금액은 정수여야 합니다.")
        # 정수여도 0이나 음수면 거래로 사용할 수 없습니다.
        positive(self.amount)
        # 정리되지 않은 공백이 파일에 남아 이름 비교를 방해하는 것을 막습니다.
        if valid_name(self.category) != self.category:
            raise AppError("카테고리 앞뒤 공백을 제거하세요.")
        # 메모·태그의 실제 자료형도 검사합니다. 타입 힌트만으로 실행 중 검증되지는 않습니다.
        if not isinstance(self.memo, str) or not isinstance(self.tags, tuple):
            raise AppError("메모/태그 자료형이 올바르지 않습니다.")
        # 태그 하나마다 문자열·빈 값·쉼표 포함 여부를 확인합니다.
        if any(not isinstance(t, str) or not t.strip() or "," in t for t in self.tags):
            raise AppError("태그는 쉼표가 없는 비어 있지 않은 문자열이어야 합니다.")

    @property
    # 정렬 기준을 (날짜, id) 튜플로 반환합니다. 같은 날짜는 id로 순서를 정합니다.
    def key(self) -> tuple[str, str]:
        # 날짜가 같으면 id를 비교하는 튜플 정렬 기준입니다.
        return self.date, self.id

    # 저장을 위해 dataclass를 dict로 바꿉니다. tuple 태그는 JSON 직렬화 시 배열이 됩니다.
    def record(self) -> dict[str, Any]:
        # dataclass의 필드 이름과 값을 저장 가능한 사전으로 복사합니다.
        return asdict(self)

    @classmethod
    # 파일에서 읽은 dict를 거래 객체로 복원합니다. 저장 태그 배열은 tuple로 변환합니다.
    def from_record(cls, row: dict[str, Any]) -> Transaction:
        try:
            # 원본 dict를 바꾸지 않도록 필드 사본을 만듭니다.
            fields = dict(row)
            # 저장 파일의 선택 필드 tags가 생략되면 빈 배열로 처리합니다.
            tags = fields.get("tags", [])
            # JSON 스키마에서 tags는 문자열 하나가 아니라 배열이어야 합니다.
            if not isinstance(tags, list):
                raise AppError("저장된 tags는 배열이어야 합니다.")
            # JSON 배열(list)을 거래 모델이 요구하는 tuple로 복원합니다.
            fields["tags"] = tuple(tags)
            # **로 사전의 필드들을 생성자 인자로 펼칩니다. 누락·알 수 없는 필드는 오류가 됩니다.
            return cls(**fields)
        except (TypeError, ValueError, AttributeError) as exc:
            raise AppError(f"거래 스키마 오류: {exc}") from None

    @classmethod
    # C(Create)의 모델 생성 단계입니다. 새 UUID id와 정리·검증된 필드로 거래를 만듭니다.
    def create(cls, *, date: str, type: str, category: str, amount: Any,
               # 선택 메모의 기본값은 빈 문자열입니다.
               memo: str = "", tags: str = "") -> Transaction:
        # uuid4로 새 id를 만들고 금액·카테고리·태그를 정리한 뒤 최종 모델 검증을 거칩니다.
        return cls("TX-" + uuid4().hex, type, date, positive(amount),
                   valid_name(category), memo, parse_tags(tags))
