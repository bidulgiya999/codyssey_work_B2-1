# budget_app/models.py 한 줄씩 설명

대상: [주석 코드](../주석코드/budget_app/models.py). 총 157줄입니다. 줄 번호는 이 사본과 일치합니다. 설명은 읽기 자료이며 실행할 명령이 아닙니다.

| 줄 | 실제 코드 | 설명 |
| ---: | --- | --- |
| [1](../주석코드/budget_app/models.py#L1) | <code># 모델 계층: 거래의 형태와 입력 값의 유효성을 정의합니다.</code> | 설명 주석입니다. 모델 계층: 거래의 형태와 입력 값의 유효성을 정의합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [2](../주석코드/budget_app/models.py#L2) | <code># 파일 저장과 화면 출력은 하지 않고, 잘못된 값은 AppError로 알립니다.</code> | 설명 주석입니다. 파일 저장과 화면 출력은 하지 않고, 잘못된 값은 AppError로 알립니다. (Python 실행에는 영향을 주지 않습니다.) |
| [3](../주석코드/budget_app/models.py#L3) | <code>&quot;&quot;&quot;입력 계약과 영구 저장 모델.&quot;&quot;&quot;</code> | 파일 저장과 화면 출력은 하지 않고, 잘못된 값은 AppError로 알립니다. / 파일/클래스/함수의 목적을 적은 문서 문자열(docstring)입니다. |
| [4](../주석코드/budget_app/models.py#L4) | <code># 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다.</code> | 설명 주석입니다. 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [5](../주석코드/budget_app/models.py#L5) | <code>from __future__ import annotations</code> | 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다. / __future__에서 필요한 이름을 가져옵니다. |
| [6](../주석코드/budget_app/models.py#L6) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [7](../주석코드/budget_app/models.py#L7) | <code># 정규식으로 날짜와 양수 숫자 문자열의 형식을 검사합니다.</code> | 설명 주석입니다. 정규식으로 날짜와 양수 숫자 문자열의 형식을 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [8](../주석코드/budget_app/models.py#L8) | <code>import re</code> | 정규식으로 날짜와 양수 숫자 문자열의 형식을 검사합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [9](../주석코드/budget_app/models.py#L9) | <code># dataclass 생성자·비교 기능과 저장용 dict 변환을 사용합니다.</code> | 설명 주석입니다. dataclass 생성자·비교 기능과 저장용 dict 변환을 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [10](../주석코드/budget_app/models.py#L10) | <code>from dataclasses import asdict, dataclass</code> | dataclass 생성자·비교 기능과 저장용 dict 변환을 사용합니다. / dataclasses에서 필요한 이름을 가져옵니다. |
| [11](../주석코드/budget_app/models.py#L11) | <code># 실제 달력 날짜와 윤년을 검증합니다.</code> | 설명 주석입니다. 실제 달력 날짜와 윤년을 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [12](../주석코드/budget_app/models.py#L12) | <code>from datetime import date</code> | 실제 달력 날짜와 윤년을 검증합니다. / datetime에서 필요한 이름을 가져옵니다. |
| [13](../주석코드/budget_app/models.py#L13) | <code># 검증 전 입력처럼 여러 자료형을 받을 수 있는 값을 표시합니다.</code> | 설명 주석입니다. 검증 전 입력처럼 여러 자료형을 받을 수 있는 값을 표시합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [14](../주석코드/budget_app/models.py#L14) | <code>from typing import Any</code> | 검증 전 입력처럼 여러 자료형을 받을 수 있는 값을 표시합니다. / typing에서 필요한 이름을 가져옵니다. |
| [15](../주석코드/budget_app/models.py#L15) | <code># 외부 카운터 파일 없이 충돌 가능성이 매우 낮은 무작위 거래 id를 만듭니다.</code> | 설명 주석입니다. 외부 카운터 파일 없이 충돌 가능성이 매우 낮은 무작위 거래 id를 만듭니다. (Python 실행에는 영향을 주지 않습니다.) |
| [16](../주석코드/budget_app/models.py#L16) | <code>from uuid import uuid4</code> | 외부 카운터 파일 없이 충돌 가능성이 매우 낮은 무작위 거래 id를 만듭니다. / uuid에서 필요한 이름을 가져옵니다. |
| [17](../주석코드/budget_app/models.py#L17) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [18](../주석코드/budget_app/models.py#L18) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [19](../주석코드/budget_app/models.py#L19) | <code># 사용자에게 보여줄 원인(message)과 해결 방법(hint)을 함께 보관하는 예외입니다.</code> | 설명 주석입니다. 사용자에게 보여줄 원인(message)과 해결 방법(hint)을 함께 보관하는 예외입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [20](../주석코드/budget_app/models.py#L20) | <code>class AppError(Exception):</code> | 사용자에게 보여줄 원인(message)과 해결 방법(hint)을 함께 보관하는 예외입니다. / AppError 클래스의 정의를 시작합니다. 들여쓴 메서드와 속성이 이 클래스에 속합니다. |
| [21](../주석코드/budget_app/models.py#L21) | <code>    # Exception에 원인을 저장하고 별도 hint 속성으로 해결 안내를 전달합니다.</code> | 설명 주석입니다. Exception에 원인을 저장하고 별도 hint 속성으로 해결 안내를 전달합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [22](../주석코드/budget_app/models.py#L22) | <code>    def __init__(self, message: str, hint: str = &quot;--help에서 사용 방법을 확인하세요.&quot;) -&gt; None:</code> | Exception에 원인을 저장하고 별도 hint 속성으로 해결 안내를 전달합니다. / __init__ 함수를 정의합니다. 인자: self, message, hint. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [23](../주석코드/budget_app/models.py#L23) | <code>        # 예외의 기본 문자열은 원인 메시지입니다. 데코레이터가 str(exc)로 출력합니다.</code> | 설명 주석입니다. 예외의 기본 문자열은 원인 메시지입니다. 데코레이터가 str(exc)로 출력합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [24](../주석코드/budget_app/models.py#L24) | <code>        super().__init__(message)</code> | 예외의 기본 문자열은 원인 메시지입니다. 데코레이터가 str(exc)로 출력합니다. / super().__init__ 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [25](../주석코드/budget_app/models.py#L25) | <code>        # 원인과 해결 방법을 분리해 CLI에서 각각 안내할 수 있게 합니다.</code> | 설명 주석입니다. 원인과 해결 방법을 분리해 CLI에서 각각 안내할 수 있게 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [26](../주석코드/budget_app/models.py#L26) | <code>        self.hint = hint</code> | 원인과 해결 방법을 분리해 CLI에서 각각 안내할 수 있게 합니다. / 오른쪽 계산/호출 결과를 self.hint에 저장합니다. |
| [27](../주석코드/budget_app/models.py#L27) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [28](../주석코드/budget_app/models.py#L28) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [29](../주석코드/budget_app/models.py#L29) | <code># 문자열 모양과 실제 달력 날짜를 모두 검증하고 원래 날짜 문자열을 반환합니다.</code> | 설명 주석입니다. 문자열 모양과 실제 달력 날짜를 모두 검증하고 원래 날짜 문자열을 반환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [30](../주석코드/budget_app/models.py#L30) | <code>def valid_date(value: str) -&gt; str:</code> | 문자열 모양과 실제 달력 날짜를 모두 검증하고 원래 날짜 문자열을 반환합니다. / valid_date 함수를 정의합니다. 인자: value. 반환 타입: str. def 자체는 본문을 실행하지 않습니다. |
| [31](../주석코드/budget_app/models.py#L31) | <code>    # 정규식 전체 일치로 YYYY-MM-DD의 자리 수와 하이픈 위치를 강제합니다.</code> | 설명 주석입니다. 정규식 전체 일치로 YYYY-MM-DD의 자리 수와 하이픈 위치를 강제합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [32](../주석코드/budget_app/models.py#L32) | <code>    if not re.fullmatch(r&quot;[0-9]{4}-[0-9]{2}-[0-9]{2}&quot;, value):</code> | 정규식 전체 일치로 YYYY-MM-DD의 자리 수와 하이픈 위치를 강제합니다. / 조건 not re.fullmatch(&#x27;[0-9]{4}-[0-9]{2}-[0-9]{2}&#x27;, value)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [33](../주석코드/budget_app/models.py#L33) | <code>        raise AppError(&quot;날짜 형식 오류&quot;, &quot;YYYY-MM-DD 형식으로 입력하세요. 예: 2024-01-15&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [34](../주석코드/budget_app/models.py#L34) | <code>    try:</code> | 오류가 발생할 수 있는 처리를 시작합니다. 해당 except/finally에서 오류 안내와 정리를 처리합니다. |
| [35](../주석코드/budget_app/models.py#L35) | <code>        # 문자 모양뿐 아니라 2월 30일처럼 달력에 없는 날짜까지 거부합니다.</code> | 설명 주석입니다. 문자 모양뿐 아니라 2월 30일처럼 달력에 없는 날짜까지 거부합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [36](../주석코드/budget_app/models.py#L36) | <code>        date.fromisoformat(value)</code> | 문자 모양뿐 아니라 2월 30일처럼 달력에 없는 날짜까지 거부합니다. / date.fromisoformat 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [37](../주석코드/budget_app/models.py#L37) | <code>    except ValueError:</code> | 앞선 try에서 해당 종류의 예외가 발생했을 때 처리할 분기입니다. as 이름이 있으면 예외 객체를 그 이름으로 받습니다. |
| [38](../주석코드/budget_app/models.py#L38) | <code>        # from None은 원래 예외 연결 표시를 생략합니다. 최종 화면 안내는 데코레이터가 담당합니다.</code> | 설명 주석입니다. from None은 원래 예외 연결 표시를 생략합니다. 최종 화면 안내는 데코레이터가 담당합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [39](../주석코드/budget_app/models.py#L39) | <code>        raise AppError(&quot;존재하지 않는 날짜&quot;, &quot;달력에 있는 날짜를 입력하세요.&quot;) from None</code> | from None은 원래 예외 연결 표시를 생략합니다. 최종 화면 안내는 데코레이터가 담당합니다. / 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [40](../주석코드/budget_app/models.py#L40) | <code>    return value</code> | 호출자에게 value을 반환하고 현재 함수 실행을 끝냅니다. |
| [41](../주석코드/budget_app/models.py#L41) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [42](../주석코드/budget_app/models.py#L42) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [43](../주석코드/budget_app/models.py#L43) | <code># YYYY-MM에 -01을 붙여 날짜 검증을 재사용하고 유효한 월 문자열을 반환합니다.</code> | 설명 주석입니다. YYYY-MM에 -01을 붙여 날짜 검증을 재사용하고 유효한 월 문자열을 반환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [44](../주석코드/budget_app/models.py#L44) | <code>def valid_month(value: str) -&gt; str:</code> | YYYY-MM에 -01을 붙여 날짜 검증을 재사용하고 유효한 월 문자열을 반환합니다. / valid_month 함수를 정의합니다. 인자: value. 반환 타입: str. def 자체는 본문을 실행하지 않습니다. |
| [45](../주석코드/budget_app/models.py#L45) | <code>    # 매월 1일을 붙이면 월 검증에 날짜 검증 로직을 재사용할 수 있습니다.</code> | 설명 주석입니다. 매월 1일을 붙이면 월 검증에 날짜 검증 로직을 재사용할 수 있습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [46](../주석코드/budget_app/models.py#L46) | <code>    valid_date(value + &quot;-01&quot;)</code> | 매월 1일을 붙이면 월 검증에 날짜 검증 로직을 재사용할 수 있습니다. / valid_date 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [47](../주석코드/budget_app/models.py#L47) | <code>    return value</code> | 호출자에게 value을 반환하고 현재 함수 실행을 끝냅니다. |
| [48](../주석코드/budget_app/models.py#L48) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [49](../주석코드/budget_app/models.py#L49) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [50](../주석코드/budget_app/models.py#L50) | <code># 입력 문자열/정수를 허용 범위의 양수 int로 바꿉니다. 금액·limit·top에 재사용합니다.</code> | 설명 주석입니다. 입력 문자열/정수를 허용 범위의 양수 int로 바꿉니다. 금액·limit·top에 재사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [51](../주석코드/budget_app/models.py#L51) | <code>def positive(value: Any) -&gt; int:</code> | 입력 문자열/정수를 허용 범위의 양수 int로 바꿉니다. 금액·limit·top에 재사용합니다. / positive 함수를 정의합니다. 인자: value. 반환 타입: int. def 자체는 본문을 실행하지 않습니다. |
| [52](../주석코드/budget_app/models.py#L52) | <code>    # 문자열로 통일해 입력 길이·숫자 형식을 먼저 검사합니다.</code> | 설명 주석입니다. 문자열로 통일해 입력 길이·숫자 형식을 먼저 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [53](../주석코드/budget_app/models.py#L53) | <code>    text = str(value)</code> | 문자열로 통일해 입력 길이·숫자 형식을 먼저 검사합니다. / 오른쪽 계산/호출 결과를 text에 저장합니다. |
| [54](../주석코드/budget_app/models.py#L54) | <code>    # bool은 int의 하위 타입이므로 별도로 거부합니다. 길이 제한은 거대한 정수 변환도 막습니다.</code> | 설명 주석입니다. bool은 int의 하위 타입이므로 별도로 거부합니다. 길이 제한은 거대한 정수 변환도 막습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [55](../주석코드/budget_app/models.py#L55) | <code>    if (isinstance(value, bool) or len(text) &gt; 19 or not re.fullmatch(r&quot;[0-9]+&quot;, text)</code> | bool은 int의 하위 타입이므로 별도로 거부합니다. 길이 제한은 거대한 정수 변환도 막습니다. / 조건 isinstance(value, bool) or len(text) &gt; 19 or (not re.fullmatch(&#x27;[0-9]+&#x27;, text)) or (not 0 &lt; int(text) &lt;= 9223372036854775807)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [56](../주석코드/budget_app/models.py#L56) | <code>            or not 0 &lt; int(text) &lt;= 9223372036854775807):</code> | 55행에서 시작한 If 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [57](../주석코드/budget_app/models.py#L57) | <code>        raise AppError(&quot;금액/개수는 양수 정수여야 합니다.&quot;, &quot;1~9223372036854775807 범위의 정수를 입력하세요.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [58](../주석코드/budget_app/models.py#L58) | <code>    # 모든 검사를 통과한 값만 정수로 바꿔 호출자에게 전달합니다.</code> | 설명 주석입니다. 모든 검사를 통과한 값만 정수로 바꿔 호출자에게 전달합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [59](../주석코드/budget_app/models.py#L59) | <code>    return int(value)</code> | 모든 검사를 통과한 값만 정수로 바꿔 호출자에게 전달합니다. / 호출자에게 int(value)을 반환하고 현재 함수 실행을 끝냅니다. |
| [60](../주석코드/budget_app/models.py#L60) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [61](../주석코드/budget_app/models.py#L61) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [62](../주석코드/budget_app/models.py#L62) | <code># 앞뒤 공백을 정리하고 빈 이름·제어 문자가 없는 카테고리명을 반환합니다.</code> | 설명 주석입니다. 앞뒤 공백을 정리하고 빈 이름·제어 문자가 없는 카테고리명을 반환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [63](../주석코드/budget_app/models.py#L63) | <code>def valid_name(value: str) -&gt; str:</code> | 앞뒤 공백을 정리하고 빈 이름·제어 문자가 없는 카테고리명을 반환합니다. / valid_name 함수를 정의합니다. 인자: value. 반환 타입: str. def 자체는 본문을 실행하지 않습니다. |
| [64](../주석코드/budget_app/models.py#L64) | <code>    # 카테고리 입력 앞뒤의 불필요한 공백을 제거합니다.</code> | 설명 주석입니다. 카테고리 입력 앞뒤의 불필요한 공백을 제거합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [65](../주석코드/budget_app/models.py#L65) | <code>    value = value.strip()</code> | 카테고리 입력 앞뒤의 불필요한 공백을 제거합니다. / 오른쪽 계산/호출 결과를 value에 저장합니다. |
| [66](../주석코드/budget_app/models.py#L66) | <code>    # 빈 이름과 줄바꿈·탭 등 제어 문자는 카테고리로 저장하지 않습니다.</code> | 설명 주석입니다. 빈 이름과 줄바꿈·탭 등 제어 문자는 카테고리로 저장하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [67](../주석코드/budget_app/models.py#L67) | <code>    if not value or any(ord(c) &lt; 32 for c in value):</code> | 빈 이름과 줄바꿈·탭 등 제어 문자는 카테고리로 저장하지 않습니다. / 조건 not value or any((ord(c) &lt; 32 for c in value))가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [68](../주석코드/budget_app/models.py#L68) | <code>        raise AppError(&quot;카테고리명은 비어 있거나 제어 문자를 포함할 수 없습니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [69](../주석코드/budget_app/models.py#L69) | <code>    return value</code> | 호출자에게 value을 반환하고 현재 함수 실행을 끝냅니다. |
| [70](../주석코드/budget_app/models.py#L70) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [71](../주석코드/budget_app/models.py#L71) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [72](../주석코드/budget_app/models.py#L72) | <code># 쉼표 분리 → 공백 정리 → 빈 태그 제외 → 순서를 유지한 중복 제거 → tuple 반환.</code> | 설명 주석입니다. 쉼표 분리 → 공백 정리 → 빈 태그 제외 → 순서를 유지한 중복 제거 → tuple 반환. (Python 실행에는 영향을 주지 않습니다.) |
| [73](../주석코드/budget_app/models.py#L73) | <code>def parse_tags(value: str) -&gt; tuple[str, ...]:</code> | 쉼표 분리 → 공백 정리 → 빈 태그 제외 → 순서를 유지한 중복 제거 → tuple 반환. / parse_tags 함수를 정의합니다. 인자: value. 반환 타입: tuple[str, ...]. def 자체는 본문을 실행하지 않습니다. |
| [74](../주석코드/budget_app/models.py#L74) | <code>    # dict의 삽입 순서를 이용해 원래 순서를 유지하면서 태그 중복을 제거합니다.</code> | 설명 주석입니다. dict의 삽입 순서를 이용해 원래 순서를 유지하면서 태그 중복을 제거합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [75](../주석코드/budget_app/models.py#L75) | <code>    return tuple(dict.fromkeys(tag.strip() for tag in value.split(&quot;,&quot;) if tag.strip()))</code> | dict의 삽입 순서를 이용해 원래 순서를 유지하면서 태그 중복을 제거합니다. / 호출자에게 tuple(dict.fromkeys((tag.strip() for tag in value.split(&#x27;,&#x27;) if tag.strip())))을 반환하고 현재 함수 실행을 끝냅니다. |
| [76](../주석코드/budget_app/models.py#L76) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [77](../주석코드/budget_app/models.py#L77) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [78](../주석코드/budget_app/models.py#L78) | <code>@dataclass(frozen=True)</code> | 바로 아래 함수/클래스에 dataclass(frozen=True) 데코레이터를 적용합니다. 중간 설명 주석은 적용 대상을 바꾸지 않습니다. |
| [79](../주석코드/budget_app/models.py#L79) | <code># 한 거래의 계약입니다. dataclass가 생성자를 만들고 frozen=True가 직접 변경을 막습니다.</code> | 설명 주석입니다. 한 거래의 계약입니다. dataclass가 생성자를 만들고 frozen=True가 직접 변경을 막습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [80](../주석코드/budget_app/models.py#L80) | <code>class Transaction:</code> | 한 거래의 계약입니다. dataclass가 생성자를 만들고 frozen=True가 직접 변경을 막습니다. / Transaction 클래스의 정의를 시작합니다. 들여쓴 메서드와 속성이 이 클래스에 속합니다. |
| [81](../주석코드/budget_app/models.py#L81) | <code>    # 고유 거래 식별자입니다. 수정·삭제에서 이 값을 사용합니다.</code> | 설명 주석입니다. 고유 거래 식별자입니다. 수정·삭제에서 이 값을 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [82](../주석코드/budget_app/models.py#L82) | <code>    id: str</code> | 고유 거래 식별자입니다. 수정·삭제에서 이 값을 사용합니다. / id의 타입을 str로 명시합니다. dataclass에서는 거래/조건 필드 선언에 사용합니다. |
| [83](../주석코드/budget_app/models.py#L83) | <code>    # 거래 종류: income(수입) 또는 expense(지출).</code> | 설명 주석입니다. 거래 종류: income(수입) 또는 expense(지출). (Python 실행에는 영향을 주지 않습니다.) |
| [84](../주석코드/budget_app/models.py#L84) | <code>    type: str</code> | 거래 종류: income(수입) 또는 expense(지출). / type의 타입을 str로 명시합니다. dataclass에서는 거래/조건 필드 선언에 사용합니다. |
| [85](../주석코드/budget_app/models.py#L85) | <code>    # 검증된 YYYY-MM-DD 문자열은 날짜 순서와 사전식 비교 순서가 같습니다.</code> | 설명 주석입니다. 검증된 YYYY-MM-DD 문자열은 날짜 순서와 사전식 비교 순서가 같습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [86](../주석코드/budget_app/models.py#L86) | <code>    date: str</code> | 검증된 YYYY-MM-DD 문자열은 날짜 순서와 사전식 비교 순서가 같습니다. / date의 타입을 str로 명시합니다. dataclass에서는 거래/조건 필드 선언에 사용합니다. |
| [87](../주석코드/budget_app/models.py#L87) | <code>    # 양수 원 단위 금액입니다. 지출 여부는 부호 대신 type으로 구분합니다.</code> | 설명 주석입니다. 양수 원 단위 금액입니다. 지출 여부는 부호 대신 type으로 구분합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [88](../주석코드/budget_app/models.py#L88) | <code>    amount: int</code> | 양수 원 단위 금액입니다. 지출 여부는 부호 대신 type으로 구분합니다. / amount의 타입을 int로 명시합니다. dataclass에서는 거래/조건 필드 선언에 사용합니다. |
| [89](../주석코드/budget_app/models.py#L89) | <code>    # 카테고리명 자체의 형식은 모델에서, 등록 여부는 서비스에서 검사합니다.</code> | 설명 주석입니다. 카테고리명 자체의 형식은 모델에서, 등록 여부는 서비스에서 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [90](../주석코드/budget_app/models.py#L90) | <code>    category: str</code> | 카테고리명 자체의 형식은 모델에서, 등록 여부는 서비스에서 검사합니다. / category의 타입을 str로 명시합니다. dataclass에서는 거래/조건 필드 선언에 사용합니다. |
| [91](../주석코드/budget_app/models.py#L91) | <code>    # 선택 메모의 기본값은 빈 문자열입니다.</code> | 설명 주석입니다. 선택 메모의 기본값은 빈 문자열입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [92](../주석코드/budget_app/models.py#L92) | <code>    memo: str = &quot;&quot;</code> | 선택 메모의 기본값은 빈 문자열입니다. / memo의 타입을 str로 명시하고 기본값을 설정합니다. |
| [93](../주석코드/budget_app/models.py#L93) | <code>    # 불변 tuple을 사용해 frozen 거래 안의 태그도 임의 변경을 피합니다.</code> | 설명 주석입니다. 불변 tuple을 사용해 frozen 거래 안의 태그도 임의 변경을 피합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [94](../주석코드/budget_app/models.py#L94) | <code>    tags: tuple[str, ...] = ()</code> | 불변 tuple을 사용해 frozen 거래 안의 태그도 임의 변경을 피합니다. / tags의 타입을 tuple[str, ...]로 명시하고 기본값을 설정합니다. |
| [95](../주석코드/budget_app/models.py#L95) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [96](../주석코드/budget_app/models.py#L96) | <code>    # 생성자 실행 직후 호출되어 객체 자체가 유효한 거래인지 검증합니다.</code> | 설명 주석입니다. 생성자 실행 직후 호출되어 객체 자체가 유효한 거래인지 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [97](../주석코드/budget_app/models.py#L97) | <code>    def __post_init__(self) -&gt; None:</code> | 생성자 실행 직후 호출되어 객체 자체가 유효한 거래인지 검증합니다. / __post_init__ 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [98](../주석코드/budget_app/models.py#L98) | <code>        # 저장 파일을 복원할 때도 id가 유효한 문자열이어야 합니다.</code> | 설명 주석입니다. 저장 파일을 복원할 때도 id가 유효한 문자열이어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [99](../주석코드/budget_app/models.py#L99) | <code>        if not isinstance(self.id, str) or not self.id.strip():</code> | 저장 파일을 복원할 때도 id가 유효한 문자열이어야 합니다. / 조건 not isinstance(self.id, str) or not self.id.strip()가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [100](../주석코드/budget_app/models.py#L100) | <code>            raise AppError(&quot;거래 id가 비어 있습니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [101](../주석코드/budget_app/models.py#L101) | <code>        # 정해진 두 종류만 받아 수입·지출 집계의 기준을 고정합니다.</code> | 설명 주석입니다. 정해진 두 종류만 받아 수입·지출 집계의 기준을 고정합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [102](../주석코드/budget_app/models.py#L102) | <code>        if self.type not in (&quot;income&quot;, &quot;expense&quot;):</code> | 정해진 두 종류만 받아 수입·지출 집계의 기준을 고정합니다. / 조건 self.type not in (&#x27;income&#x27;, &#x27;expense&#x27;)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [103](../주석코드/budget_app/models.py#L103) | <code>            raise AppError(&quot;type은 income 또는 expense여야 합니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [104](../주석코드/budget_app/models.py#L104) | <code>        # 객체를 직접 만들 때도 날짜 검증을 건너뛸 수 없습니다.</code> | 설명 주석입니다. 객체를 직접 만들 때도 날짜 검증을 건너뛸 수 없습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [105](../주석코드/budget_app/models.py#L105) | <code>        valid_date(self.date)</code> | 객체를 직접 만들 때도 날짜 검증을 건너뛸 수 없습니다. / valid_date 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [106](../주석코드/budget_app/models.py#L106) | <code>        # 저장 모델에서는 문자열 숫자와 bool을 허용하지 않고 정확한 int만 허용합니다.</code> | 설명 주석입니다. 저장 모델에서는 문자열 숫자와 bool을 허용하지 않고 정확한 int만 허용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [107](../주석코드/budget_app/models.py#L107) | <code>        if type(self.amount) is not int:</code> | 저장 모델에서는 문자열 숫자와 bool을 허용하지 않고 정확한 int만 허용합니다. / 조건 type(self.amount) is not int가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [108](../주석코드/budget_app/models.py#L108) | <code>            raise AppError(&quot;저장된 금액은 정수여야 합니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [109](../주석코드/budget_app/models.py#L109) | <code>        # 정수여도 0이나 음수면 거래로 사용할 수 없습니다.</code> | 설명 주석입니다. 정수여도 0이나 음수면 거래로 사용할 수 없습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [110](../주석코드/budget_app/models.py#L110) | <code>        positive(self.amount)</code> | 정수여도 0이나 음수면 거래로 사용할 수 없습니다. / positive 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [111](../주석코드/budget_app/models.py#L111) | <code>        # 정리되지 않은 공백이 파일에 남아 이름 비교를 방해하는 것을 막습니다.</code> | 설명 주석입니다. 정리되지 않은 공백이 파일에 남아 이름 비교를 방해하는 것을 막습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [112](../주석코드/budget_app/models.py#L112) | <code>        if valid_name(self.category) != self.category:</code> | 정리되지 않은 공백이 파일에 남아 이름 비교를 방해하는 것을 막습니다. / 조건 valid_name(self.category) != self.category가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [113](../주석코드/budget_app/models.py#L113) | <code>            raise AppError(&quot;카테고리 앞뒤 공백을 제거하세요.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [114](../주석코드/budget_app/models.py#L114) | <code>        # 메모·태그의 실제 자료형도 검사합니다. 타입 힌트만으로 실행 중 검증되지는 않습니다.</code> | 설명 주석입니다. 메모·태그의 실제 자료형도 검사합니다. 타입 힌트만으로 실행 중 검증되지는 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [115](../주석코드/budget_app/models.py#L115) | <code>        if not isinstance(self.memo, str) or not isinstance(self.tags, tuple):</code> | 메모·태그의 실제 자료형도 검사합니다. 타입 힌트만으로 실행 중 검증되지는 않습니다. / 조건 not isinstance(self.memo, str) or not isinstance(self.tags, tuple)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [116](../주석코드/budget_app/models.py#L116) | <code>            raise AppError(&quot;메모/태그 자료형이 올바르지 않습니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [117](../주석코드/budget_app/models.py#L117) | <code>        # 태그 하나마다 문자열·빈 값·쉼표 포함 여부를 확인합니다.</code> | 설명 주석입니다. 태그 하나마다 문자열·빈 값·쉼표 포함 여부를 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [118](../주석코드/budget_app/models.py#L118) | <code>        if any(not isinstance(t, str) or not t.strip() or &quot;,&quot; in t for t in self.tags):</code> | 태그 하나마다 문자열·빈 값·쉼표 포함 여부를 확인합니다. / 조건 any((not isinstance(t, str) or not t.strip() or &#x27;,&#x27; in t for t in self.tags))가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [119](../주석코드/budget_app/models.py#L119) | <code>            raise AppError(&quot;태그는 쉼표가 없는 비어 있지 않은 문자열이어야 합니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [120](../주석코드/budget_app/models.py#L120) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [121](../주석코드/budget_app/models.py#L121) | <code>    @property</code> | 바로 아래 함수/클래스에 property 데코레이터를 적용합니다. 중간 설명 주석은 적용 대상을 바꾸지 않습니다. |
| [122](../주석코드/budget_app/models.py#L122) | <code>    # 정렬 기준을 (날짜, id) 튜플로 반환합니다. 같은 날짜는 id로 순서를 정합니다.</code> | 설명 주석입니다. 정렬 기준을 (날짜, id) 튜플로 반환합니다. 같은 날짜는 id로 순서를 정합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [123](../주석코드/budget_app/models.py#L123) | <code>    def key(self) -&gt; tuple[str, str]:</code> | 정렬 기준을 (날짜, id) 튜플로 반환합니다. 같은 날짜는 id로 순서를 정합니다. / key 함수를 정의합니다. 인자: self. 반환 타입: tuple[str, str]. def 자체는 본문을 실행하지 않습니다. |
| [124](../주석코드/budget_app/models.py#L124) | <code>        # 날짜가 같으면 id를 비교하는 튜플 정렬 기준입니다.</code> | 설명 주석입니다. 날짜가 같으면 id를 비교하는 튜플 정렬 기준입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [125](../주석코드/budget_app/models.py#L125) | <code>        return self.date, self.id</code> | 날짜가 같으면 id를 비교하는 튜플 정렬 기준입니다. / 호출자에게 (self.date, self.id)을 반환하고 현재 함수 실행을 끝냅니다. |
| [126](../주석코드/budget_app/models.py#L126) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [127](../주석코드/budget_app/models.py#L127) | <code>    # 저장을 위해 dataclass를 dict로 바꿉니다. tuple 태그는 JSON 직렬화 시 배열이 됩니다.</code> | 설명 주석입니다. 저장을 위해 dataclass를 dict로 바꿉니다. tuple 태그는 JSON 직렬화 시 배열이 됩니다. (Python 실행에는 영향을 주지 않습니다.) |
| [128](../주석코드/budget_app/models.py#L128) | <code>    def record(self) -&gt; dict[str, Any]:</code> | 저장을 위해 dataclass를 dict로 바꿉니다. tuple 태그는 JSON 직렬화 시 배열이 됩니다. / record 함수를 정의합니다. 인자: self. 반환 타입: dict[str, Any]. def 자체는 본문을 실행하지 않습니다. |
| [129](../주석코드/budget_app/models.py#L129) | <code>        # dataclass의 필드 이름과 값을 저장 가능한 사전으로 복사합니다.</code> | 설명 주석입니다. dataclass의 필드 이름과 값을 저장 가능한 사전으로 복사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [130](../주석코드/budget_app/models.py#L130) | <code>        return asdict(self)</code> | dataclass의 필드 이름과 값을 저장 가능한 사전으로 복사합니다. / 호출자에게 asdict(self)을 반환하고 현재 함수 실행을 끝냅니다. |
| [131](../주석코드/budget_app/models.py#L131) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [132](../주석코드/budget_app/models.py#L132) | <code>    @classmethod</code> | 바로 아래 함수/클래스에 classmethod 데코레이터를 적용합니다. 중간 설명 주석은 적용 대상을 바꾸지 않습니다. |
| [133](../주석코드/budget_app/models.py#L133) | <code>    # 파일에서 읽은 dict를 거래 객체로 복원합니다. 저장 태그 배열은 tuple로 변환합니다.</code> | 설명 주석입니다. 파일에서 읽은 dict를 거래 객체로 복원합니다. 저장 태그 배열은 tuple로 변환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [134](../주석코드/budget_app/models.py#L134) | <code>    def from_record(cls, row: dict[str, Any]) -&gt; Transaction:</code> | 파일에서 읽은 dict를 거래 객체로 복원합니다. 저장 태그 배열은 tuple로 변환합니다. / from_record 함수를 정의합니다. 인자: cls, row. 반환 타입: Transaction. def 자체는 본문을 실행하지 않습니다. |
| [135](../주석코드/budget_app/models.py#L135) | <code>        try:</code> | 오류가 발생할 수 있는 처리를 시작합니다. 해당 except/finally에서 오류 안내와 정리를 처리합니다. |
| [136](../주석코드/budget_app/models.py#L136) | <code>            # 원본 dict를 바꾸지 않도록 필드 사본을 만듭니다.</code> | 설명 주석입니다. 원본 dict를 바꾸지 않도록 필드 사본을 만듭니다. (Python 실행에는 영향을 주지 않습니다.) |
| [137](../주석코드/budget_app/models.py#L137) | <code>            fields = dict(row)</code> | 원본 dict를 바꾸지 않도록 필드 사본을 만듭니다. / 오른쪽 계산/호출 결과를 fields에 저장합니다. |
| [138](../주석코드/budget_app/models.py#L138) | <code>            # 저장 파일의 선택 필드 tags가 생략되면 빈 배열로 처리합니다.</code> | 설명 주석입니다. 저장 파일의 선택 필드 tags가 생략되면 빈 배열로 처리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [139](../주석코드/budget_app/models.py#L139) | <code>            tags = fields.get(&quot;tags&quot;, [])</code> | 저장 파일의 선택 필드 tags가 생략되면 빈 배열로 처리합니다. / 오른쪽 계산/호출 결과를 tags에 저장합니다. |
| [140](../주석코드/budget_app/models.py#L140) | <code>            # JSON 스키마에서 tags는 문자열 하나가 아니라 배열이어야 합니다.</code> | 설명 주석입니다. JSON 스키마에서 tags는 문자열 하나가 아니라 배열이어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [141](../주석코드/budget_app/models.py#L141) | <code>            if not isinstance(tags, list):</code> | JSON 스키마에서 tags는 문자열 하나가 아니라 배열이어야 합니다. / 조건 not isinstance(tags, list)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [142](../주석코드/budget_app/models.py#L142) | <code>                raise AppError(&quot;저장된 tags는 배열이어야 합니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [143](../주석코드/budget_app/models.py#L143) | <code>            # JSON 배열(list)을 거래 모델이 요구하는 tuple로 복원합니다.</code> | 설명 주석입니다. JSON 배열(list)을 거래 모델이 요구하는 tuple로 복원합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [144](../주석코드/budget_app/models.py#L144) | <code>            fields[&quot;tags&quot;] = tuple(tags)</code> | JSON 배열(list)을 거래 모델이 요구하는 tuple로 복원합니다. / 오른쪽 계산/호출 결과를 fields[&#x27;tags&#x27;]에 저장합니다. |
| [145](../주석코드/budget_app/models.py#L145) | <code>            # **로 사전의 필드들을 생성자 인자로 펼칩니다. 누락·알 수 없는 필드는 오류가 됩니다.</code> | 설명 주석입니다. **로 사전의 필드들을 생성자 인자로 펼칩니다. 누락·알 수 없는 필드는 오류가 됩니다. (Python 실행에는 영향을 주지 않습니다.) |
| [146](../주석코드/budget_app/models.py#L146) | <code>            return cls(**fields)</code> | **로 사전의 필드들을 생성자 인자로 펼칩니다. 누락·알 수 없는 필드는 오류가 됩니다. / 호출자에게 cls(**fields)을 반환하고 현재 함수 실행을 끝냅니다. |
| [147](../주석코드/budget_app/models.py#L147) | <code>        except (TypeError, ValueError, AttributeError) as exc:</code> | 앞선 try에서 해당 종류의 예외가 발생했을 때 처리할 분기입니다. as 이름이 있으면 예외 객체를 그 이름으로 받습니다. |
| [148](../주석코드/budget_app/models.py#L148) | <code>            raise AppError(f&quot;거래 스키마 오류: {exc}&quot;) from None</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [149](../주석코드/budget_app/models.py#L149) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [150](../주석코드/budget_app/models.py#L150) | <code>    @classmethod</code> | 바로 아래 함수/클래스에 classmethod 데코레이터를 적용합니다. 중간 설명 주석은 적용 대상을 바꾸지 않습니다. |
| [151](../주석코드/budget_app/models.py#L151) | <code>    # C(Create)의 모델 생성 단계입니다. 새 UUID id와 정리·검증된 필드로 거래를 만듭니다.</code> | 설명 주석입니다. C(Create)의 모델 생성 단계입니다. 새 UUID id와 정리·검증된 필드로 거래를 만듭니다. (Python 실행에는 영향을 주지 않습니다.) |
| [152](../주석코드/budget_app/models.py#L152) | <code>    def create(cls, *, date: str, type: str, category: str, amount: Any,</code> | C(Create)의 모델 생성 단계입니다. 새 UUID id와 정리·검증된 필드로 거래를 만듭니다. / create 함수를 정의합니다. 인자: cls, date, type, category, amount, memo, tags. 반환 타입: Transaction. def 자체는 본문을 실행하지 않습니다. |
| [153](../주석코드/budget_app/models.py#L153) | <code>               # 선택 메모의 기본값은 빈 문자열입니다.</code> | 설명 주석입니다. 선택 메모의 기본값은 빈 문자열입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [154](../주석코드/budget_app/models.py#L154) | <code>               memo: str = &quot;&quot;, tags: str = &quot;&quot;) -&gt; Transaction:</code> | 선택 메모의 기본값은 빈 문자열입니다. / 152행에서 시작한 FunctionDef 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [155](../주석코드/budget_app/models.py#L155) | <code>        # uuid4로 새 id를 만들고 금액·카테고리·태그를 정리한 뒤 최종 모델 검증을 거칩니다.</code> | 설명 주석입니다. uuid4로 새 id를 만들고 금액·카테고리·태그를 정리한 뒤 최종 모델 검증을 거칩니다. (Python 실행에는 영향을 주지 않습니다.) |
| [156](../주석코드/budget_app/models.py#L156) | <code>        return cls(&quot;TX-&quot; + uuid4().hex, type, date, positive(amount),</code> | uuid4로 새 id를 만들고 금액·카테고리·태그를 정리한 뒤 최종 모델 검증을 거칩니다. / 호출자에게 cls(&#x27;TX-&#x27; + uuid4().hex, type, date, positive(amount), valid_name(category), memo, parse_tags(tags))을 반환하고 현재 함수 실행을 끝냅니다. |
| [157](../주석코드/budget_app/models.py#L157) | <code>                   valid_name(category), memo, parse_tags(tags))</code> | 156행에서 시작한 Return 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
