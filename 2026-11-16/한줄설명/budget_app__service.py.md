# budget_app/service.py 한 줄씩 설명

대상: [주석 코드](../주석코드/budget_app/service.py). 총 334줄입니다. 줄 번호는 이 사본과 일치합니다. 설명은 읽기 자료이며 실행할 명령이 아닙니다.

| 줄 | 실제 코드 | 설명 |
| ---: | --- | --- |
| [1](../주석코드/budget_app/service.py#L1) | <code># 서비스 계층: 거래 CRUD와 검색·집계·카테고리·예산의 업무 규칙을 담당합니다.</code> | 설명 주석입니다. 서비스 계층: 거래 CRUD와 검색·집계·카테고리·예산의 업무 규칙을 담당합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [2](../주석코드/budget_app/service.py#L2) | <code># CLI와 저장소 사이에서 정책을 적용하며, 화면에 출력할 자료를 반환합니다.</code> | 설명 주석입니다. CLI와 저장소 사이에서 정책을 적용하며, 화면에 출력할 자료를 반환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [3](../주석코드/budget_app/service.py#L3) | <code>&quot;&quot;&quot;거래, 카테고리, 예산 및 CSV 입출력의 업무 규칙.&quot;&quot;&quot;</code> | CLI와 저장소 사이에서 정책을 적용하며, 화면에 출력할 자료를 반환합니다. / 파일/클래스/함수의 목적을 적은 문서 문자열(docstring)입니다. |
| [4](../주석코드/budget_app/service.py#L4) | <code># 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다.</code> | 설명 주석입니다. 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [5](../주석코드/budget_app/service.py#L5) | <code>from __future__ import annotations</code> | 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다. / __future__에서 필요한 이름을 가져옵니다. |
| [6](../주석코드/budget_app/service.py#L6) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [7](../주석코드/budget_app/service.py#L7) | <code># 쉼표·인용·개행을 직접 나누지 않고 표준 CSV 규칙으로 처리합니다.</code> | 설명 주석입니다. 쉼표·인용·개행을 직접 나누지 않고 표준 CSV 규칙으로 처리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [8](../주석코드/budget_app/service.py#L8) | <code>import csv</code> | 쉼표·인용·개행을 직접 나누지 않고 표준 CSV 규칙으로 처리합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [9](../주석코드/budget_app/service.py#L9) | <code># 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다.</code> | 설명 주석입니다. 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [10](../주석코드/budget_app/service.py#L10) | <code>import os</code> | 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [11](../주석코드/budget_app/service.py#L11) | <code># 가져오기를 원본이 아닌 사본에서 처리하도록 파일을 복사합니다.</code> | 설명 주석입니다. 가져오기를 원본이 아닌 사본에서 처리하도록 파일을 복사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [12](../주석코드/budget_app/service.py#L12) | <code>import shutil</code> | 가져오기를 원본이 아닌 사본에서 처리하도록 파일을 복사합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [13](../주석코드/budget_app/service.py#L13) | <code># 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다.</code> | 설명 주석입니다. 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [14](../주석코드/budget_app/service.py#L14) | <code>import tempfile</code> | 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [15](../주석코드/budget_app/service.py#L15) | <code># 세 저장 파일의 ZIP 백업을 만들거나 테스트에서 검사합니다.</code> | 설명 주석입니다. 세 저장 파일의 ZIP 백업을 만들거나 테스트에서 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [16](../주석코드/budget_app/service.py#L16) | <code>import zipfile</code> | 세 저장 파일의 ZIP 백업을 만들거나 테스트에서 검사합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [17](../주석코드/budget_app/service.py#L17) | <code># 처음 보는 지출 카테고리의 누적 합계를 0에서 시작합니다.</code> | 설명 주석입니다. 처음 보는 지출 카테고리의 누적 합계를 0에서 시작합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [18](../주석코드/budget_app/service.py#L18) | <code>from collections import defaultdict</code> | 처음 보는 지출 카테고리의 누적 합계를 0에서 시작합니다. / collections에서 필요한 이름을 가져옵니다. |
| [19](../주석코드/budget_app/service.py#L19) | <code># 검색 조건 모델과 불변 거래의 일부 필드만 바꾼 사본을 만듭니다.</code> | 설명 주석입니다. 검색 조건 모델과 불변 거래의 일부 필드만 바꾼 사본을 만듭니다. (Python 실행에는 영향을 주지 않습니다.) |
| [20](../주석코드/budget_app/service.py#L20) | <code>from dataclasses import dataclass, replace</code> | 검색 조건 모델과 불변 거래의 일부 필드만 바꾼 사본을 만듭니다. / dataclasses에서 필요한 이름을 가져옵니다. |
| [21](../주석코드/budget_app/service.py#L21) | <code># 백업 파일 이름에 실행 시각을 넣습니다.</code> | 설명 주석입니다. 백업 파일 이름에 실행 시각을 넣습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [22](../주석코드/budget_app/service.py#L22) | <code>from datetime import datetime</code> | 백업 파일 이름에 실행 시각을 넣습니다. / datetime에서 필요한 이름을 가져옵니다. |
| [23](../주석코드/budget_app/service.py#L23) | <code># 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다.</code> | 설명 주석입니다. 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [24](../주석코드/budget_app/service.py#L24) | <code>from pathlib import Path</code> | 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다. / pathlib에서 필요한 이름을 가져옵니다. |
| [25](../주석코드/budget_app/service.py#L25) | <code># 서비스 결과와 한 건씩 전달하는 거래 스트림의 타입입니다.</code> | 설명 주석입니다. 서비스 결과와 한 건씩 전달하는 거래 스트림의 타입입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [26](../주석코드/budget_app/service.py#L26) | <code>from typing import Any, Iterator</code> | 서비스 결과와 한 건씩 전달하는 거래 스트림의 타입입니다. / typing에서 필요한 이름을 가져옵니다. |
| [27](../주석코드/budget_app/service.py#L27) | <code># 외부 카운터 파일 없이 충돌 가능성이 매우 낮은 무작위 거래 id를 만듭니다.</code> | 설명 주석입니다. 외부 카운터 파일 없이 충돌 가능성이 매우 낮은 무작위 거래 id를 만듭니다. (Python 실행에는 영향을 주지 않습니다.) |
| [28](../주석코드/budget_app/service.py#L28) | <code>from uuid import uuid4</code> | 외부 카운터 파일 없이 충돌 가능성이 매우 낮은 무작위 거래 id를 만듭니다. / uuid에서 필요한 이름을 가져옵니다. |
| [29](../주석코드/budget_app/service.py#L29) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [30](../주석코드/budget_app/service.py#L30) | <code># 서비스가 모델 생성과 공통 입력 검증 함수를 재사용합니다.</code> | 설명 주석입니다. 서비스가 모델 생성과 공통 입력 검증 함수를 재사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [31](../주석코드/budget_app/service.py#L31) | <code>from .models import AppError, Transaction, parse_tags, positive, valid_date, valid_month, valid_name</code> | 서비스가 모델 생성과 공통 입력 검증 함수를 재사용합니다. / models에서 필요한 이름을 가져옵니다. |
| [32](../주석코드/budget_app/service.py#L32) | <code># 서비스가 직접 저수준 I/O를 중복 구현하지 않고 공통 저장 기능에 위임합니다.</code> | 설명 주석입니다. 서비스가 직접 저수준 I/O를 중복 구현하지 않고 공통 저장 기능에 위임합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [33](../주석코드/budget_app/service.py#L33) | <code>from .storage import DataStore, TransactionRepository, atomic_text, read_jsonl, write_jsonl</code> | 서비스가 직접 저수준 I/O를 중복 구현하지 않고 공통 저장 기능에 위임합니다. / storage에서 필요한 이름을 가져옵니다. |
| [34](../주석코드/budget_app/service.py#L34) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [35](../주석코드/budget_app/service.py#L35) | <code># 내보내기 열 순서이며 앞의 네 열은 가져오기에 필수입니다.</code> | 설명 주석입니다. 내보내기 열 순서이며 앞의 네 열은 가져오기에 필수입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [36](../주석코드/budget_app/service.py#L36) | <code>CSV_FIELDS = (&quot;date&quot;, &quot;type&quot;, &quot;category&quot;, &quot;amount&quot;, &quot;memo&quot;, &quot;tags&quot;)</code> | 내보내기 열 순서이며 앞의 네 열은 가져오기에 필수입니다. / 오른쪽 계산/호출 결과를 CSV_FIELDS에 저장합니다. |
| [37](../주석코드/budget_app/service.py#L37) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [38](../주석코드/budget_app/service.py#L38) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [39](../주석코드/budget_app/service.py#L39) | <code>@dataclass(frozen=True)</code> | 바로 아래 함수/클래스에 dataclass(frozen=True) 데코레이터를 적용합니다. 중간 설명 주석은 적용 대상을 바꾸지 않습니다. |
| [40](../주석코드/budget_app/service.py#L40) | <code># 검색 조건을 담는 불변 dataclass입니다. None은 해당 조건을 지정하지 않았다는 뜻입니다.</code> | 설명 주석입니다. 검색 조건을 담는 불변 dataclass입니다. None은 해당 조건을 지정하지 않았다는 뜻입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [41](../주석코드/budget_app/service.py#L41) | <code>class Filters:</code> | 검색 조건을 담는 불변 dataclass입니다. None은 해당 조건을 지정하지 않았다는 뜻입니다. / Filters 클래스의 정의를 시작합니다. 들여쓴 메서드와 속성이 이 클래스에 속합니다. |
| [42](../주석코드/budget_app/service.py#L42) | <code>    # 포함할 시작 날짜입니다. None이면 하한이 없습니다.</code> | 설명 주석입니다. 포함할 시작 날짜입니다. None이면 하한이 없습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [43](../주석코드/budget_app/service.py#L43) | <code>    start: str &#124; None = None</code> | 포함할 시작 날짜입니다. None이면 하한이 없습니다. / start의 타입을 str &#124; None로 명시하고 기본값을 설정합니다. |
| [44](../주석코드/budget_app/service.py#L44) | <code>    # 포함할 종료 날짜입니다. None이면 상한이 없습니다.</code> | 설명 주석입니다. 포함할 종료 날짜입니다. None이면 상한이 없습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [45](../주석코드/budget_app/service.py#L45) | <code>    end: str &#124; None = None</code> | 포함할 종료 날짜입니다. None이면 상한이 없습니다. / end의 타입을 str &#124; None로 명시하고 기본값을 설정합니다. |
| [46](../주석코드/budget_app/service.py#L46) | <code>    # YYYY-MM 월 조건입니다. 날짜 범위와 동시에 지정하지 않습니다.</code> | 설명 주석입니다. YYYY-MM 월 조건입니다. 날짜 범위와 동시에 지정하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [47](../주석코드/budget_app/service.py#L47) | <code>    month: str &#124; None = None</code> | YYYY-MM 월 조건입니다. 날짜 범위와 동시에 지정하지 않습니다. / month의 타입을 str &#124; None로 명시하고 기본값을 설정합니다. |
| [48](../주석코드/budget_app/service.py#L48) | <code>    # 정확히 일치해야 하는 등록 카테고리입니다.</code> | 설명 주석입니다. 정확히 일치해야 하는 등록 카테고리입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [49](../주석코드/budget_app/service.py#L49) | <code>    category: str &#124; None = None</code> | 정확히 일치해야 하는 등록 카테고리입니다. / category의 타입을 str &#124; None로 명시하고 기본값을 설정합니다. |
| [50](../주석코드/budget_app/service.py#L50) | <code>    # 수입 또는 지출만 선택하는 조건입니다.</code> | 설명 주석입니다. 수입 또는 지출만 선택하는 조건입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [51](../주석코드/budget_app/service.py#L51) | <code>    type: str &#124; None = None</code> | 수입 또는 지출만 선택하는 조건입니다. / type의 타입을 str &#124; None로 명시하고 기본값을 설정합니다. |
| [52](../주석코드/budget_app/service.py#L52) | <code>    # 메모에서 찾을 부분 문자열입니다.</code> | 설명 주석입니다. 메모에서 찾을 부분 문자열입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [53](../주석코드/budget_app/service.py#L53) | <code>    q: str &#124; None = None</code> | 메모에서 찾을 부분 문자열입니다. / q의 타입을 str &#124; None로 명시하고 기본값을 설정합니다. |
| [54](../주석코드/budget_app/service.py#L54) | <code>    # 태그 목록에 완전히 일치하는 값이 있는지 검사합니다.</code> | 설명 주석입니다. 태그 목록에 완전히 일치하는 값이 있는지 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [55](../주석코드/budget_app/service.py#L55) | <code>    tag: str &#124; None = None</code> | 태그 목록에 완전히 일치하는 값이 있는지 검사합니다. / tag의 타입을 str &#124; None로 명시하고 기본값을 설정합니다. |
| [56](../주석코드/budget_app/service.py#L56) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [57](../주석코드/budget_app/service.py#L57) | <code>    # 검색 실행 전에 날짜·월·기간 순서와 조건의 충돌을 검증합니다.</code> | 설명 주석입니다. 검색 실행 전에 날짜·월·기간 순서와 조건의 충돌을 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [58](../주석코드/budget_app/service.py#L58) | <code>    def __post_init__(self) -&gt; None:</code> | 검색 실행 전에 날짜·월·기간 순서와 조건의 충돌을 검증합니다. / __post_init__ 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [59](../주석코드/budget_app/service.py#L59) | <code>        # 시작 날짜가 지정된 경우에만 형식을 검증합니다.</code> | 설명 주석입니다. 시작 날짜가 지정된 경우에만 형식을 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [60](../주석코드/budget_app/service.py#L60) | <code>        if self.start:</code> | 시작 날짜가 지정된 경우에만 형식을 검증합니다. / 조건 self.start가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [61](../주석코드/budget_app/service.py#L61) | <code>            valid_date(self.start)</code> | valid_date 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [62](../주석코드/budget_app/service.py#L62) | <code>        # 종료 날짜도 별도로 검증합니다.</code> | 설명 주석입니다. 종료 날짜도 별도로 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [63](../주석코드/budget_app/service.py#L63) | <code>        if self.end:</code> | 종료 날짜도 별도로 검증합니다. / 조건 self.end가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [64](../주석코드/budget_app/service.py#L64) | <code>            valid_date(self.end)</code> | valid_date 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [65](../주석코드/budget_app/service.py#L65) | <code>        # 월 조건은 YYYY-MM이 유효한지 확인합니다.</code> | 설명 주석입니다. 월 조건은 YYYY-MM이 유효한지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [66](../주석코드/budget_app/service.py#L66) | <code>        if self.month:</code> | 월 조건은 YYYY-MM이 유효한지 확인합니다. / 조건 self.month가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [67](../주석코드/budget_app/service.py#L67) | <code>            valid_month(self.month)</code> | valid_month 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [68](../주석코드/budget_app/service.py#L68) | <code>        # 두 경계의 형식 검증 후 사전식 비교로 날짜 순서를 검사합니다.</code> | 설명 주석입니다. 두 경계의 형식 검증 후 사전식 비교로 날짜 순서를 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [69](../주석코드/budget_app/service.py#L69) | <code>        if self.start and self.end and self.start &gt; self.end:</code> | 두 경계의 형식 검증 후 사전식 비교로 날짜 순서를 검사합니다. / 조건 self.start and self.end and (self.start &gt; self.end)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [70](../주석코드/budget_app/service.py#L70) | <code>            raise AppError(&quot;시작 날짜가 종료 날짜보다 늦습니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [71](../주석코드/budget_app/service.py#L71) | <code>        # 서로 다른 기간 표현의 충돌을 막아 사용자 의도를 명확하게 합니다.</code> | 설명 주석입니다. 서로 다른 기간 표현의 충돌을 막아 사용자 의도를 명확하게 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [72](../주석코드/budget_app/service.py#L72) | <code>        if self.month and (self.start or self.end):</code> | 서로 다른 기간 표현의 충돌을 막아 사용자 의도를 명확하게 합니다. / 조건 self.month and (self.start or self.end)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [73](../주석코드/budget_app/service.py#L73) | <code>            raise AppError(&quot;--month와 --from/--to는 함께 사용할 수 없습니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [74](../주석코드/budget_app/service.py#L74) | <code>        # Filters를 CLI 밖에서 직접 생성해도 타입 제한을 적용합니다.</code> | 설명 주석입니다. Filters를 CLI 밖에서 직접 생성해도 타입 제한을 적용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [75](../주석코드/budget_app/service.py#L75) | <code>        if self.type is not None and self.type not in (&quot;income&quot;, &quot;expense&quot;):</code> | Filters를 CLI 밖에서 직접 생성해도 타입 제한을 적용합니다. / 조건 self.type is not None and self.type not in (&#x27;income&#x27;, &#x27;expense&#x27;)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [76](../주석코드/budget_app/service.py#L76) | <code>            raise AppError(&quot;type은 income 또는 expense여야 합니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [77](../주석코드/budget_app/service.py#L77) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [78](../주석코드/budget_app/service.py#L78) | <code>    # 거래 한 건이 모든 조건(AND)을 만족하면 True, 아니면 False를 반환합니다.</code> | 설명 주석입니다. 거래 한 건이 모든 조건(AND)을 만족하면 True, 아니면 False를 반환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [79](../주석코드/budget_app/service.py#L79) | <code>    def matches(self, t: Transaction) -&gt; bool:</code> | 거래 한 건이 모든 조건(AND)을 만족하면 True, 아니면 False를 반환합니다. / matches 함수를 정의합니다. 인자: self, t. 반환 타입: bool. def 자체는 본문을 실행하지 않습니다. |
| [80](../주석코드/budget_app/service.py#L80) | <code>        # 미지정 조건은 통과합니다. 기간 경계 포함·카테고리/타입 일치·메모 casefold·태그 포함을 AND로 결합합니다.</code> | 설명 주석입니다. 미지정 조건은 통과합니다. 기간 경계 포함·카테고리/타입 일치·메모 casefold·태그 포함을 AND로 결합합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [81](../주석코드/budget_app/service.py#L81) | <code>        return (not self.start or t.date &gt;= self.start) and (not self.end or t.date &lt;= self.end) and (</code> | 미지정 조건은 통과합니다. 기간 경계 포함·카테고리/타입 일치·메모 casefold·태그 포함을 AND로 결합합니다. / 호출자에게 (not self.start or t.date &gt;= self.start) and (not self.end or t.date &lt;= self.end) and (not self.month or t.date[:7] == self.month) and (self.category is None or t.category == self.category) and (self.type is None or t.type == self.type) and (self.q is None or self.q.casefold() in t.memo.casefold()) and (self.tag is None or self.tag in t.tags)을 반환하고 현재 함수 실행을 끝냅니다. |
| [82](../주석코드/budget_app/service.py#L82) | <code>            not self.month or t.date[:7] == self.month) and (</code> | 81행에서 시작한 Return 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [83](../주석코드/budget_app/service.py#L83) | <code>            self.category is None or t.category == self.category) and (</code> | 81행에서 시작한 Return 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [84](../주석코드/budget_app/service.py#L84) | <code>            self.type is None or t.type == self.type) and (</code> | 81행에서 시작한 Return 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [85](../주석코드/budget_app/service.py#L85) | <code>            self.q is None or self.q.casefold() in t.memo.casefold()) and (</code> | 81행에서 시작한 Return 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [86](../주석코드/budget_app/service.py#L86) | <code>            self.tag is None or self.tag in t.tags)</code> | 81행에서 시작한 Return 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [87](../주석코드/budget_app/service.py#L87) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [88](../주석코드/budget_app/service.py#L88) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [89](../주석코드/budget_app/service.py#L89) | <code># 업무 규칙 담당 클래스입니다. 직접 입력받거나 출력하지 않고 저장소를 조합합니다.</code> | 설명 주석입니다. 업무 규칙 담당 클래스입니다. 직접 입력받거나 출력하지 않고 저장소를 조합합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [90](../주석코드/budget_app/service.py#L90) | <code>class BudgetService:</code> | 업무 규칙 담당 클래스입니다. 직접 입력받거나 출력하지 않고 저장소를 조합합니다. / BudgetService 클래스의 정의를 시작합니다. 들여쓴 메서드와 속성이 이 클래스에 속합니다. |
| [91](../주석코드/budget_app/service.py#L91) | <code>    # 데이터 경로 관리자와 거래 저장소를 연결합니다. 서비스 호출은 CLI 잠금 안에서 이루어집니다.</code> | 설명 주석입니다. 데이터 경로 관리자와 거래 저장소를 연결합니다. 서비스 호출은 CLI 잠금 안에서 이루어집니다. (Python 실행에는 영향을 주지 않습니다.) |
| [92](../주석코드/budget_app/service.py#L92) | <code>    def __init__(self, store: DataStore) -&gt; None:</code> | 데이터 경로 관리자와 거래 저장소를 연결합니다. 서비스 호출은 CLI 잠금 안에서 이루어집니다. / __init__ 함수를 정의합니다. 인자: self, store. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [93](../주석코드/budget_app/service.py#L93) | <code>        # 세 파일과 경로·보호 정책은 전달받은 DataStore에 위임합니다.</code> | 설명 주석입니다. 세 파일과 경로·보호 정책은 전달받은 DataStore에 위임합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [94](../주석코드/budget_app/service.py#L94) | <code>        self.store = store</code> | 세 파일과 경로·보호 정책은 전달받은 DataStore에 위임합니다. / 오른쪽 계산/호출 결과를 self.store에 저장합니다. |
| [95](../주석코드/budget_app/service.py#L95) | <code>        # 거래 읽기와 병합 재작성을 TransactionRepository에 위임합니다.</code> | 설명 주석입니다. 거래 읽기와 병합 재작성을 TransactionRepository에 위임합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [96](../주석코드/budget_app/service.py#L96) | <code>        self.transactions = TransactionRepository(store.path(&quot;transactions&quot;))</code> | 거래 읽기와 병합 재작성을 TransactionRepository에 위임합니다. / 오른쪽 계산/호출 결과를 self.transactions에 저장합니다. |
| [97](../주석코드/budget_app/service.py#L97) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [98](../주석코드/budget_app/service.py#L98) | <code>    # 카테고리 파일의 스키마와 중복을 검증하고 이름 목록을 반환합니다.</code> | 설명 주석입니다. 카테고리 파일의 스키마와 중복을 검증하고 이름 목록을 반환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [99](../주석코드/budget_app/service.py#L99) | <code>    def categories(self) -&gt; list[str]:</code> | 카테고리 파일의 스키마와 중복을 검증하고 이름 목록을 반환합니다. / categories 함수를 정의합니다. 인자: self. 반환 타입: list[str]. def 자체는 본문을 실행하지 않습니다. |
| [100](../주석코드/budget_app/service.py#L100) | <code>        # 거래와 달리 작은 메타데이터 목록은 메모리에 모읍니다.</code> | 설명 주석입니다. 거래와 달리 작은 메타데이터 목록은 메모리에 모읍니다. (Python 실행에는 영향을 주지 않습니다.) |
| [101](../주석코드/budget_app/service.py#L101) | <code>        names = []</code> | 거래와 달리 작은 메타데이터 목록은 메모리에 모읍니다. / 오른쪽 계산/호출 결과를 names에 저장합니다. |
| [102](../주석코드/budget_app/service.py#L102) | <code>        # 카테고리는 각 줄에 name 하나만 있는 JSON 객체로 저장합니다.</code> | 설명 주석입니다. 카테고리는 각 줄에 name 하나만 있는 JSON 객체로 저장합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [103](../주석코드/budget_app/service.py#L103) | <code>        for row in read_jsonl(self.store.path(&quot;categories&quot;)):</code> | 카테고리는 각 줄에 name 하나만 있는 JSON 객체로 저장합니다. / read_jsonl(self.store.path(&#x27;categories&#x27;))에서 값을 하나씩 받아 row에 넣고 블록을 반복합니다. |
| [104](../주석코드/budget_app/service.py#L104) | <code>            # 열 누락·추가와 문자열 아닌 이름을 저장 손상으로 보고합니다.</code> | 설명 주석입니다. 열 누락·추가와 문자열 아닌 이름을 저장 손상으로 보고합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [105](../주석코드/budget_app/service.py#L105) | <code>            if set(row) != {&quot;name&quot;} or not isinstance(row[&quot;name&quot;], str):</code> | 열 누락·추가와 문자열 아닌 이름을 저장 손상으로 보고합니다. / 조건 set(row) != {&#x27;name&#x27;} or not isinstance(row[&#x27;name&#x27;], str)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [106](../주석코드/budget_app/service.py#L106) | <code>                raise AppError(&quot;카테고리 파일 스키마 오류&quot;, &quot;categories.jsonl을 백업 후 복구하세요.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [107](../주석코드/budget_app/service.py#L107) | <code>            # 이름 형식을 검증하고 정리한 값을 얻습니다.</code> | 설명 주석입니다. 이름 형식을 검증하고 정리한 값을 얻습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [108](../주석코드/budget_app/service.py#L108) | <code>            name = valid_name(row[&quot;name&quot;])</code> | 이름 형식을 검증하고 정리한 값을 얻습니다. / 오른쪽 계산/호출 결과를 name에 저장합니다. |
| [109](../주석코드/budget_app/service.py#L109) | <code>            # 저장 파일에는 앞뒤 공백이나 중복 이름이 남아 있으면 안 됩니다.</code> | 설명 주석입니다. 저장 파일에는 앞뒤 공백이나 중복 이름이 남아 있으면 안 됩니다. (Python 실행에는 영향을 주지 않습니다.) |
| [110](../주석코드/budget_app/service.py#L110) | <code>            if name != row[&quot;name&quot;] or name in names:</code> | 저장 파일에는 앞뒤 공백이나 중복 이름이 남아 있으면 안 됩니다. / 조건 name != row[&#x27;name&#x27;] or name in names가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [111](../주석코드/budget_app/service.py#L111) | <code>                raise AppError(&quot;카테고리 파일에 공백 또는 중복 이름이 있습니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [112](../주석코드/budget_app/service.py#L112) | <code>            # 검증을 통과한 이름만 결과 목록에 포함합니다.</code> | 설명 주석입니다. 검증을 통과한 이름만 결과 목록에 포함합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [113](../주석코드/budget_app/service.py#L113) | <code>            names.append(name)</code> | 검증을 통과한 이름만 결과 목록에 포함합니다. / names.append 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [114](../주석코드/budget_app/service.py#L114) | <code>        return names</code> | 호출자에게 names을 반환하고 현재 함수 실행을 끝냅니다. |
| [115](../주석코드/budget_app/service.py#L115) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [116](../주석코드/budget_app/service.py#L116) | <code>    # 여러 기능에서 공통으로 쓰는 등록 여부 검사입니다. 미등록 카테고리는 저장 전에 거부합니다.</code> | 설명 주석입니다. 여러 기능에서 공통으로 쓰는 등록 여부 검사입니다. 미등록 카테고리는 저장 전에 거부합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [117](../주석코드/budget_app/service.py#L117) | <code>    def require_category(self, name: str) -&gt; None:</code> | 여러 기능에서 공통으로 쓰는 등록 여부 검사입니다. 미등록 카테고리는 저장 전에 거부합니다. / require_category 함수를 정의합니다. 인자: self, name. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [118](../주석코드/budget_app/service.py#L118) | <code>        # 거래가 참조할 수 있는 카테고리인지 검사합니다.</code> | 설명 주석입니다. 거래가 참조할 수 있는 카테고리인지 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [119](../주석코드/budget_app/service.py#L119) | <code>        if name not in self.categories():</code> | 거래가 참조할 수 있는 카테고리인지 검사합니다. / 조건 name not in self.categories()가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [120](../주석코드/budget_app/service.py#L120) | <code>            raise AppError(f&quot;등록되지 않은 카테고리: {name}&quot;, &quot;category list로 확인하거나 category add로 등록하세요.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [121](../주석코드/budget_app/service.py#L121) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [122](../주석코드/budget_app/service.py#L122) | <code>    # 카테고리 C: 이름 정리 후 중복을 거부하고 추가된 목록을 안전하게 저장합니다.</code> | 설명 주석입니다. 카테고리 C: 이름 정리 후 중복을 거부하고 추가된 목록을 안전하게 저장합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [123](../주석코드/budget_app/service.py#L123) | <code>    def category_add(self, name: str) -&gt; str:</code> | 카테고리 C: 이름 정리 후 중복을 거부하고 추가된 목록을 안전하게 저장합니다. / category_add 함수를 정의합니다. 인자: self, name. 반환 타입: str. def 자체는 본문을 실행하지 않습니다. |
| [124](../주석코드/budget_app/service.py#L124) | <code>        # 대화형 입력의 앞뒤 공백을 정리한 뒤 중복 여부를 판단합니다.</code> | 설명 주석입니다. 대화형 입력의 앞뒤 공백을 정리한 뒤 중복 여부를 판단합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [125](../주석코드/budget_app/service.py#L125) | <code>        name = valid_name(name)</code> | 대화형 입력의 앞뒤 공백을 정리한 뒤 중복 여부를 판단합니다. / 오른쪽 계산/호출 결과를 name에 저장합니다. |
| [126](../주석코드/budget_app/service.py#L126) | <code>        # 저장된 이름을 읽어 변경 전 목록을 확보합니다.</code> | 설명 주석입니다. 저장된 이름을 읽어 변경 전 목록을 확보합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [127](../주석코드/budget_app/service.py#L127) | <code>        names = self.categories()</code> | 저장된 이름을 읽어 변경 전 목록을 확보합니다. / 오른쪽 계산/호출 결과를 names에 저장합니다. |
| [128](../주석코드/budget_app/service.py#L128) | <code>        # 같은 이름을 두 번 추가하지 않습니다.</code> | 설명 주석입니다. 같은 이름을 두 번 추가하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [129](../주석코드/budget_app/service.py#L129) | <code>        if name in names:</code> | 같은 이름을 두 번 추가하지 않습니다. / 조건 name in names가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [130](../주석코드/budget_app/service.py#L130) | <code>            raise AppError(f&quot;이미 등록된 카테고리: {name}&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [131](../주석코드/budget_app/service.py#L131) | <code>        # 기존 이름과 새 이름을 정렬해 원자적으로 저장합니다.</code> | 설명 주석입니다. 기존 이름과 새 이름을 정렬해 원자적으로 저장합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [132](../주석코드/budget_app/service.py#L132) | <code>        write_jsonl(self.store.path(&quot;categories&quot;), ({&quot;name&quot;: n} for n in sorted([*names, name])))</code> | 기존 이름과 새 이름을 정렬해 원자적으로 저장합니다. / write_jsonl 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [133](../주석코드/budget_app/service.py#L133) | <code>        return name</code> | 호출자에게 name을 반환하고 현재 함수 실행을 끝냅니다. |
| [134](../주석코드/budget_app/service.py#L134) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [135](../주석코드/budget_app/service.py#L135) | <code>    # 카테고리 D: 사용 중이거나 마지막 남은 이름은 보호하고 나머지 이름만 저장합니다.</code> | 설명 주석입니다. 카테고리 D: 사용 중이거나 마지막 남은 이름은 보호하고 나머지 이름만 저장합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [136](../주석코드/budget_app/service.py#L136) | <code>    def category_remove(self, name: str) -&gt; None:</code> | 카테고리 D: 사용 중이거나 마지막 남은 이름은 보호하고 나머지 이름만 저장합니다. / category_remove 함수를 정의합니다. 인자: self, name. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [137](../주석코드/budget_app/service.py#L137) | <code>        self.require_category(name)</code> | self.require_category 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [138](../주석코드/budget_app/service.py#L138) | <code>        # 거래를 스트리밍 검사하다 첫 사용 사례를 발견하면 삭제를 차단합니다.</code> | 설명 주석입니다. 거래를 스트리밍 검사하다 첫 사용 사례를 발견하면 삭제를 차단합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [139](../주석코드/budget_app/service.py#L139) | <code>        if any(t.category == name for t in self.transactions.iter_all()):</code> | 거래를 스트리밍 검사하다 첫 사용 사례를 발견하면 삭제를 차단합니다. / 조건 any((t.category == name for t in self.transactions.iter_all()))가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [140](../주석코드/budget_app/service.py#L140) | <code>            raise AppError(&quot;사용 중인 카테고리는 삭제할 수 없습니다.&quot;, &quot;해당 거래를 수정하거나 삭제한 뒤 다시 시도하세요.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [141](../주석코드/budget_app/service.py#L141) | <code>        # 저장된 이름을 읽어 변경 전 목록을 확보합니다.</code> | 설명 주석입니다. 저장된 이름을 읽어 변경 전 목록을 확보합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [142](../주석코드/budget_app/service.py#L142) | <code>        names = self.categories()</code> | 저장된 이름을 읽어 변경 전 목록을 확보합니다. / 오른쪽 계산/호출 결과를 names에 저장합니다. |
| [143](../주석코드/budget_app/service.py#L143) | <code>        # 빈 카테고리 파일의 기본값 재생성과 혼동되지 않도록 마지막 이름은 보호합니다.</code> | 설명 주석입니다. 빈 카테고리 파일의 기본값 재생성과 혼동되지 않도록 마지막 이름은 보호합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [144](../주석코드/budget_app/service.py#L144) | <code>        if len(names) == 1:</code> | 빈 카테고리 파일의 기본값 재생성과 혼동되지 않도록 마지막 이름은 보호합니다. / 조건 len(names) == 1가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [145](../주석코드/budget_app/service.py#L145) | <code>            raise AppError(&quot;마지막 카테고리는 삭제할 수 없습니다.&quot;, &quot;새 카테고리를 먼저 추가하세요.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [146](../주석코드/budget_app/service.py#L146) | <code>        # 삭제 대상 이름만 제외하고 나머지 카테고리를 보존합니다.</code> | 설명 주석입니다. 삭제 대상 이름만 제외하고 나머지 카테고리를 보존합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [147](../주석코드/budget_app/service.py#L147) | <code>        write_jsonl(self.store.path(&quot;categories&quot;), ({&quot;name&quot;: n} for n in names if n != name))</code> | 삭제 대상 이름만 제외하고 나머지 카테고리를 보존합니다. / write_jsonl 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [148](../주석코드/budget_app/service.py#L148) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [149](../주석코드/budget_app/service.py#L149) | <code>    # 거래 C(Create): 등록된 카테고리인지 확인한 후 새 거래를 정렬 병합 저장합니다.</code> | 설명 주석입니다. 거래 C(Create): 등록된 카테고리인지 확인한 후 새 거래를 정렬 병합 저장합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [150](../주석코드/budget_app/service.py#L150) | <code>    def add(self, transaction: Transaction) -&gt; None:</code> | 거래 C(Create): 등록된 카테고리인지 확인한 후 새 거래를 정렬 병합 저장합니다. / add 함수를 정의합니다. 인자: self, transaction. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [151](../주석코드/budget_app/service.py#L151) | <code>        # C: 모델 형식 검증과 별개로 등록 카테고리 정책을 확인합니다.</code> | 설명 주석입니다. C: 모델 형식 검증과 별개로 등록 카테고리 정책을 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [152](../주석코드/budget_app/service.py#L152) | <code>        self.require_category(transaction.category)</code> | C: 모델 형식 검증과 별개로 등록 카테고리 정책을 확인합니다. / self.require_category 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [153](../주석코드/budget_app/service.py#L153) | <code>        # C: 제외할 id 없이 새 거래만 정렬 순서에 삽입합니다.</code> | 설명 주석입니다. C: 제외할 id 없이 새 거래만 정렬 순서에 삽입합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [154](../주석코드/budget_app/service.py#L154) | <code>        self.transactions.replace(replacement=transaction)</code> | C: 제외할 id 없이 새 거래만 정렬 순서에 삽입합니다. / self.transactions.replace 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [155](../주석코드/budget_app/service.py#L155) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [156](../주석코드/budget_app/service.py#L156) | <code>    # 거래 U(Update): 기존 id를 찾고 지정된 필드만 검증·변경한 새 객체로 교체합니다.</code> | 설명 주석입니다. 거래 U(Update): 기존 id를 찾고 지정된 필드만 검증·변경한 새 객체로 교체합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [157](../주석코드/budget_app/service.py#L157) | <code>    def update(self, identifier: str, changes: dict[str, Any]) -&gt; None:</code> | 거래 U(Update): 기존 id를 찾고 지정된 필드만 검증·변경한 새 객체로 교체합니다. / update 함수를 정의합니다. 인자: self, identifier, changes. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [158](../주석코드/budget_app/service.py#L158) | <code>        # U: 아무 필드도 지정하지 않은 요청은 실수일 수 있으므로 거부합니다.</code> | 설명 주석입니다. U: 아무 필드도 지정하지 않은 요청은 실수일 수 있으므로 거부합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [159](../주석코드/budget_app/service.py#L159) | <code>        if not changes:</code> | U: 아무 필드도 지정하지 않은 요청은 실수일 수 있으므로 거부합니다. / 조건 not changes가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [160](../주석코드/budget_app/service.py#L160) | <code>            raise AppError(&quot;수정할 필드를 하나 이상 지정하세요.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [161](../주석코드/budget_app/service.py#L161) | <code>        # U: 대상 존재를 먼저 확인합니다. 없는 id면 이 단계에서 실패합니다.</code> | 설명 주석입니다. U: 대상 존재를 먼저 확인합니다. 없는 id면 이 단계에서 실패합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [162](../주석코드/budget_app/service.py#L162) | <code>        old = self.transactions.find(identifier)</code> | U: 대상 존재를 먼저 확인합니다. 없는 id면 이 단계에서 실패합니다. / 오른쪽 계산/호출 결과를 old에 저장합니다. |
| [163](../주석코드/budget_app/service.py#L163) | <code>        # CLI 옵션은 문자열이므로 수정 금액도 int로 검증·변환합니다.</code> | 설명 주석입니다. CLI 옵션은 문자열이므로 수정 금액도 int로 검증·변환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [164](../주석코드/budget_app/service.py#L164) | <code>        if &quot;amount&quot; in changes:</code> | CLI 옵션은 문자열이므로 수정 금액도 int로 검증·변환합니다. / 조건 &#x27;amount&#x27; in changes가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [165](../주석코드/budget_app/service.py#L165) | <code>            changes[&quot;amount&quot;] = positive(changes[&quot;amount&quot;])</code> | 오른쪽 계산/호출 결과를 changes[&#x27;amount&#x27;]에 저장합니다. |
| [166](../주석코드/budget_app/service.py#L166) | <code>        # 태그 문자열을 모델이 요구하는 tuple로 변환합니다. 빈 문자열이면 태그를 비웁니다.</code> | 설명 주석입니다. 태그 문자열을 모델이 요구하는 tuple로 변환합니다. 빈 문자열이면 태그를 비웁니다. (Python 실행에는 영향을 주지 않습니다.) |
| [167](../주석코드/budget_app/service.py#L167) | <code>        if &quot;tags&quot; in changes:</code> | 태그 문자열을 모델이 요구하는 tuple로 변환합니다. 빈 문자열이면 태그를 비웁니다. / 조건 &#x27;tags&#x27; in changes가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [168](../주석코드/budget_app/service.py#L168) | <code>            changes[&quot;tags&quot;] = parse_tags(changes[&quot;tags&quot;])</code> | 오른쪽 계산/호출 결과를 changes[&#x27;tags&#x27;]에 저장합니다. |
| [169](../주석코드/budget_app/service.py#L169) | <code>        # frozen 객체를 직접 수정하지 않고 선택 필드만 바꾼 새 dataclass를 만듭니다.</code> | 설명 주석입니다. frozen 객체를 직접 수정하지 않고 선택 필드만 바꾼 새 dataclass를 만듭니다. (Python 실행에는 영향을 주지 않습니다.) |
| [170](../주석코드/budget_app/service.py#L170) | <code>        updated = replace(old, **changes)</code> | frozen 객체를 직접 수정하지 않고 선택 필드만 바꾼 새 dataclass를 만듭니다. / 오른쪽 계산/호출 결과를 updated에 저장합니다. |
| [171](../주석코드/budget_app/service.py#L171) | <code>        # 수정 후에도 등록되지 않은 카테고리를 참조할 수 없습니다.</code> | 설명 주석입니다. 수정 후에도 등록되지 않은 카테고리를 참조할 수 없습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [172](../주석코드/budget_app/service.py#L172) | <code>        self.require_category(updated.category)</code> | 수정 후에도 등록되지 않은 카테고리를 참조할 수 없습니다. / self.require_category 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [173](../주석코드/budget_app/service.py#L173) | <code>        # U: 기존 id 거래를 제외하고 같은 id의 새 객체를 날짜 정렬에 맞춰 삽입합니다.</code> | 설명 주석입니다. U: 기존 id 거래를 제외하고 같은 id의 새 객체를 날짜 정렬에 맞춰 삽입합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [174](../주석코드/budget_app/service.py#L174) | <code>        self.transactions.replace(identifier, updated)</code> | U: 기존 id 거래를 제외하고 같은 id의 새 객체를 날짜 정렬에 맞춰 삽입합니다. / self.transactions.replace 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [175](../주석코드/budget_app/service.py#L175) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [176](../주석코드/budget_app/service.py#L176) | <code>    # 거래 D(Delete): id 존재를 먼저 확인하고 해당 거래를 제외한 파일로 교체합니다.</code> | 설명 주석입니다. 거래 D(Delete): id 존재를 먼저 확인하고 해당 거래를 제외한 파일로 교체합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [177](../주석코드/budget_app/service.py#L177) | <code>    def delete(self, identifier: str) -&gt; None:</code> | 거래 D(Delete): id 존재를 먼저 확인하고 해당 거래를 제외한 파일로 교체합니다. / delete 함수를 정의합니다. 인자: self, identifier. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [178](../주석코드/budget_app/service.py#L178) | <code>        # D: 파일을 쓰기 전에 존재 여부를 검사해 없는 id를 명확히 안내합니다.</code> | 설명 주석입니다. D: 파일을 쓰기 전에 존재 여부를 검사해 없는 id를 명확히 안내합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [179](../주석코드/budget_app/service.py#L179) | <code>        self.transactions.find(identifier)</code> | D: 파일을 쓰기 전에 존재 여부를 검사해 없는 id를 명확히 안내합니다. / self.transactions.find 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [180](../주석코드/budget_app/service.py#L180) | <code>        # D: 대체 거래를 주지 않아 해당 id만 빼고 저장합니다.</code> | 설명 주석입니다. D: 대체 거래를 주지 않아 해당 id만 빼고 저장합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [181](../주석코드/budget_app/service.py#L181) | <code>        self.transactions.replace(identifier)</code> | D: 대체 거래를 주지 않아 해당 id만 빼고 저장합니다. / self.transactions.replace 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [182](../주석코드/budget_app/service.py#L182) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [183](../주석코드/budget_app/service.py#L183) | <code>    # 거래 R(Read): 거래 스트림에서 조건을 통과한 것만 yield하여 CLI로 전달합니다.</code> | 설명 주석입니다. 거래 R(Read): 거래 스트림에서 조건을 통과한 것만 yield하여 CLI로 전달합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [184](../주석코드/budget_app/service.py#L184) | <code>    def search(self, filters: Filters) -&gt; Iterator[Transaction]:</code> | 거래 R(Read): 거래 스트림에서 조건을 통과한 것만 yield하여 CLI로 전달합니다. / search 함수를 정의합니다. 인자: self, filters. 반환 타입: Iterator[Transaction]. def 자체는 본문을 실행하지 않습니다. |
| [185](../주석코드/budget_app/service.py#L185) | <code>        # R: 카테고리 이름의 오타를 결과 없음으로 숨기지 않고 명확히 안내합니다.</code> | 설명 주석입니다. R: 카테고리 이름의 오타를 결과 없음으로 숨기지 않고 명확히 안내합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [186](../주석코드/budget_app/service.py#L186) | <code>        if filters.category is not None:</code> | R: 카테고리 이름의 오타를 결과 없음으로 숨기지 않고 명확히 안내합니다. / 조건 filters.category is not None가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [187](../주석코드/budget_app/service.py#L187) | <code>            self.require_category(filters.category)</code> | self.require_category 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [188](../주석코드/budget_app/service.py#L188) | <code>        # R: 거래를 한 건씩 받습니다. list도 비어 있는 Filters로 이 경로를 재사용합니다.</code> | 설명 주석입니다. R: 거래를 한 건씩 받습니다. list도 비어 있는 Filters로 이 경로를 재사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [189](../주석코드/budget_app/service.py#L189) | <code>        for transaction in self.transactions.iter_all():</code> | R: 거래를 한 건씩 받습니다. list도 비어 있는 Filters로 이 경로를 재사용합니다. / self.transactions.iter_all()에서 값을 하나씩 받아 transaction에 넣고 블록을 반복합니다. |
| [190](../주석코드/budget_app/service.py#L190) | <code>            # R: 모든 검색 조건을 통과한 거래만 다음 단계로 보냅니다.</code> | 설명 주석입니다. R: 모든 검색 조건을 통과한 거래만 다음 단계로 보냅니다. (Python 실행에는 영향을 주지 않습니다.) |
| [191](../주석코드/budget_app/service.py#L191) | <code>            if filters.matches(transaction):</code> | R: 모든 검색 조건을 통과한 거래만 다음 단계로 보냅니다. / 조건 filters.matches(transaction)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [192](../주석코드/budget_app/service.py#L192) | <code>                # R: 전체 결과 리스트 대신 필요한 시점에 한 거래씩 전달합니다.</code> | 설명 주석입니다. R: 전체 결과 리스트 대신 필요한 시점에 한 거래씩 전달합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [193](../주석코드/budget_app/service.py#L193) | <code>                yield transaction</code> | R: 전체 결과 리스트 대신 필요한 시점에 한 거래씩 전달합니다. / 호출자에게 transaction을 전달하고 잠시 멈춥니다. 다음 요청/컨텍스트 종료 시 이 지점 뒤에서 이어집니다. |
| [194](../주석코드/budget_app/service.py#L194) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [195](../주석코드/budget_app/service.py#L195) | <code>    # 예산을 월→금액 dict로 읽습니다. 중복 월·잘못된 스키마는 손상으로 취급합니다.</code> | 설명 주석입니다. 예산을 월→금액 dict로 읽습니다. 중복 월·잘못된 스키마는 손상으로 취급합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [196](../주석코드/budget_app/service.py#L196) | <code>    def budgets(self) -&gt; dict[str, int]:</code> | 예산을 월→금액 dict로 읽습니다. 중복 월·잘못된 스키마는 손상으로 취급합니다. / budgets 함수를 정의합니다. 인자: self. 반환 타입: dict[str, int]. def 자체는 본문을 실행하지 않습니다. |
| [197](../주석코드/budget_app/service.py#L197) | <code>        # 월 문자열을 키로, 예산 금액 int를 값으로 쓰는 계약입니다.</code> | 설명 주석입니다. 월 문자열을 키로, 예산 금액 int를 값으로 쓰는 계약입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [198](../주석코드/budget_app/service.py#L198) | <code>        result: dict[str, int] = {}</code> | 월 문자열을 키로, 예산 금액 int를 값으로 쓰는 계약입니다. / result의 타입을 dict[str, int]로 명시하고 기본값을 설정합니다. |
| [199](../주석코드/budget_app/service.py#L199) | <code>        # 예산도 JSONL의 레코드 단위로 읽습니다.</code> | 설명 주석입니다. 예산도 JSONL의 레코드 단위로 읽습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [200](../주석코드/budget_app/service.py#L200) | <code>        for row in read_jsonl(self.store.path(&quot;budgets&quot;)):</code> | 예산도 JSONL의 레코드 단위로 읽습니다. / read_jsonl(self.store.path(&#x27;budgets&#x27;))에서 값을 하나씩 받아 row에 넣고 블록을 반복합니다. |
| [201](../주석코드/budget_app/service.py#L201) | <code>            # 예산 스키마와 실제 자료형을 함께 검사합니다.</code> | 설명 주석입니다. 예산 스키마와 실제 자료형을 함께 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [202](../주석코드/budget_app/service.py#L202) | <code>            if set(row) != {&quot;month&quot;, &quot;amount&quot;} or not isinstance(row[&quot;month&quot;], str) or type(row[&quot;amount&quot;]) is not int:</code> | 예산 스키마와 실제 자료형을 함께 검사합니다. / 조건 set(row) != {&#x27;month&#x27;, &#x27;amount&#x27;} or not isinstance(row[&#x27;month&#x27;], str) or type(row[&#x27;amount&#x27;]) is not int가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [203](../주석코드/budget_app/service.py#L203) | <code>                raise AppError(&quot;예산 파일 스키마 오류&quot;, &quot;budgets.jsonl을 백업 후 복구하세요.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [204](../주석코드/budget_app/service.py#L204) | <code>            month = valid_month(row[&quot;month&quot;])</code> | 오른쪽 계산/호출 결과를 month에 저장합니다. |
| [205](../주석코드/budget_app/service.py#L205) | <code>            # 한 달에 여러 예산 레코드가 있으면 임의 선택하지 않고 오류로 안내합니다.</code> | 설명 주석입니다. 한 달에 여러 예산 레코드가 있으면 임의 선택하지 않고 오류로 안내합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [206](../주석코드/budget_app/service.py#L206) | <code>            if month in result:</code> | 한 달에 여러 예산 레코드가 있으면 임의 선택하지 않고 오류로 안내합니다. / 조건 month in result가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [207](../주석코드/budget_app/service.py#L207) | <code>                raise AppError(&quot;예산 파일에 중복 월이 있습니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [208](../주석코드/budget_app/service.py#L208) | <code>            result[month] = positive(row[&quot;amount&quot;])</code> | 오른쪽 계산/호출 결과를 result[month]에 저장합니다. |
| [209](../주석코드/budget_app/service.py#L209) | <code>        return result</code> | 호출자에게 result을 반환하고 현재 함수 실행을 끝냅니다. |
| [210](../주석코드/budget_app/service.py#L210) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [211](../주석코드/budget_app/service.py#L211) | <code>    # 예산 C/U: 처음인 월은 추가하고 이미 있는 월은 금액을 갱신한 뒤 저장합니다.</code> | 설명 주석입니다. 예산 C/U: 처음인 월은 추가하고 이미 있는 월은 금액을 갱신한 뒤 저장합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [212](../주석코드/budget_app/service.py#L212) | <code>    def set_budget(self, month: str, amount: str &#124; int) -&gt; None:</code> | 예산 C/U: 처음인 월은 추가하고 이미 있는 월은 금액을 갱신한 뒤 저장합니다. / set_budget 함수를 정의합니다. 인자: self, month, amount. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [213](../주석코드/budget_app/service.py#L213) | <code>        valid_month(month)</code> | valid_month 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [214](../주석코드/budget_app/service.py#L214) | <code>        amount = positive(amount)</code> | 오른쪽 계산/호출 결과를 amount에 저장합니다. |
| [215](../주석코드/budget_app/service.py#L215) | <code>        budgets = self.budgets()</code> | 오른쪽 계산/호출 결과를 budgets에 저장합니다. |
| [216](../주석코드/budget_app/service.py#L216) | <code>        # dict 대입으로 없는 월 추가(C)와 기존 월 갱신(U)을 같은 코드로 처리합니다.</code> | 설명 주석입니다. dict 대입으로 없는 월 추가(C)와 기존 월 갱신(U)을 같은 코드로 처리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [217](../주석코드/budget_app/service.py#L217) | <code>        budgets[month] = amount</code> | dict 대입으로 없는 월 추가(C)와 기존 월 갱신(U)을 같은 코드로 처리합니다. / 오른쪽 계산/호출 결과를 budgets[month]에 저장합니다. |
| [218](../주석코드/budget_app/service.py#L218) | <code>        # 월별 설정 전체를 작은 메타데이터 파일에 안전하게 교체 저장합니다.</code> | 설명 주석입니다. 월별 설정 전체를 작은 메타데이터 파일에 안전하게 교체 저장합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [219](../주석코드/budget_app/service.py#L219) | <code>        write_jsonl(self.store.path(&quot;budgets&quot;), ({&quot;month&quot;: m, &quot;amount&quot;: a} for m, a in sorted(budgets.items())))</code> | 월별 설정 전체를 작은 메타데이터 파일에 안전하게 교체 저장합니다. / write_jsonl 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [220](../주석코드/budget_app/service.py#L220) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [221](../주석코드/budget_app/service.py#L221) | <code>    # 월 거래를 한 번 순회하며 수입·지출·건수·카테고리 지출을 누적한 결과를 반환합니다.</code> | 설명 주석입니다. 월 거래를 한 번 순회하며 수입·지출·건수·카테고리 지출을 누적한 결과를 반환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [222](../주석코드/budget_app/service.py#L222) | <code>    def summary(self, month: str) -&gt; dict[str, Any]:</code> | 월 거래를 한 번 순회하며 수입·지출·건수·카테고리 지출을 누적한 결과를 반환합니다. / summary 함수를 정의합니다. 인자: self, month. 반환 타입: dict[str, Any]. def 자체는 본문을 실행하지 않습니다. |
| [223](../주석코드/budget_app/service.py#L223) | <code>        # 거래 전체 대신 합계와 개수만 유지합니다.</code> | 설명 주석입니다. 거래 전체 대신 합계와 개수만 유지합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [224](../주석코드/budget_app/service.py#L224) | <code>        income = expense = count = 0</code> | 거래 전체 대신 합계와 개수만 유지합니다. / 오른쪽 계산/호출 결과를 income, expense, count에 저장합니다. |
| [225](../주석코드/budget_app/service.py#L225) | <code>        # defaultdict(int)는 처음 보는 카테고리의 합계를 0에서 시작하게 합니다.</code> | 설명 주석입니다. defaultdict(int)는 처음 보는 카테고리의 합계를 0에서 시작하게 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [226](../주석코드/budget_app/service.py#L226) | <code>        categories: dict[str, int] = defaultdict(int)</code> | defaultdict(int)는 처음 보는 카테고리의 합계를 0에서 시작하게 합니다. / categories의 타입을 dict[str, int]로 명시하고 기본값을 설정합니다. |
| [227](../주석코드/budget_app/service.py#L227) | <code>        # 선택 월에 속한 거래 스트림만 집계합니다.</code> | 설명 주석입니다. 선택 월에 속한 거래 스트림만 집계합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [228](../주석코드/budget_app/service.py#L228) | <code>        for t in self.search(Filters(month=month)):</code> | 선택 월에 속한 거래 스트림만 집계합니다. / self.search(Filters(month=month))에서 값을 하나씩 받아 t에 넣고 블록을 반복합니다. |
| [229](../주석코드/budget_app/service.py#L229) | <code>            count += 1</code> | 기존 count 값에 계산 결과를 반영해 누적·갱신합니다. |
| [230](../주석코드/budget_app/service.py#L230) | <code>            # type을 기준으로 수입 합계와 지출 합계를 분리합니다.</code> | 설명 주석입니다. type을 기준으로 수입 합계와 지출 합계를 분리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [231](../주석코드/budget_app/service.py#L231) | <code>            if t.type == &quot;income&quot;:</code> | type을 기준으로 수입 합계와 지출 합계를 분리합니다. / 조건 t.type == &#x27;income&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [232](../주석코드/budget_app/service.py#L232) | <code>                income += t.amount</code> | 기존 income 값에 계산 결과를 반영해 누적·갱신합니다. |
| [233](../주석코드/budget_app/service.py#L233) | <code>            else:</code> | 바로 앞 조건에 해당하지 않는 경우의 대체 처리 블록입니다. |
| [234](../주석코드/budget_app/service.py#L234) | <code>                expense += t.amount</code> | 기존 expense 값에 계산 결과를 반영해 누적·갱신합니다. |
| [235](../주석코드/budget_app/service.py#L235) | <code>                # 수입은 순위에 넣지 않고 지출만 카테고리별로 누적합니다.</code> | 설명 주석입니다. 수입은 순위에 넣지 않고 지출만 카테고리별로 누적합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [236](../주석코드/budget_app/service.py#L236) | <code>                categories[t.category] += t.amount</code> | 수입은 순위에 넣지 않고 지출만 카테고리별로 누적합니다. / 기존 categories[t.category] 값에 계산 결과를 반영해 누적·갱신합니다. |
| [237](../주석코드/budget_app/service.py#L237) | <code>        # 합계와 예산을 반환합니다. 카테고리는 금액 내림차순·이름 오름차순 정렬입니다.</code> | 설명 주석입니다. 합계와 예산을 반환합니다. 카테고리는 금액 내림차순·이름 오름차순 정렬입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [238](../주석코드/budget_app/service.py#L238) | <code>        return {&quot;income&quot;: income, &quot;expense&quot;: expense, &quot;count&quot;: count,</code> | 합계와 예산을 반환합니다. 카테고리는 금액 내림차순·이름 오름차순 정렬입니다. / 호출자에게 {&#x27;income&#x27;: income, &#x27;expense&#x27;: expense, &#x27;count&#x27;: count, &#x27;categories&#x27;: sorted(categories.items(), key=lambda x: (-x[1], x[0])), &#x27;budget&#x27;: self.budgets().get(month)}을 반환하고 현재 함수 실행을 끝냅니다. |
| [239](../주석코드/budget_app/service.py#L239) | <code>                &quot;categories&quot;: sorted(categories.items(), key=lambda x: (-x[1], x[0])),</code> | 238행에서 시작한 Return 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [240](../주석코드/budget_app/service.py#L240) | <code>                &quot;budget&quot;: self.budgets().get(month)}</code> | 238행에서 시작한 Return 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [241](../주석코드/budget_app/service.py#L241) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [242](../주석코드/budget_app/service.py#L242) | <code>    # CSV 일괄 C: 원본이 아닌 스테이징 사본에 병합하고 모든 행이 성공해야 최종 반영합니다.</code> | 설명 주석입니다. CSV 일괄 C: 원본이 아닌 스테이징 사본에 병합하고 모든 행이 성공해야 최종 반영합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [243](../주석코드/budget_app/service.py#L243) | <code>    def import_csv(self, path: Path) -&gt; int:</code> | CSV 일괄 C: 원본이 아닌 스테이징 사본에 병합하고 모든 행이 성공해야 최종 반영합니다. / import_csv 함수를 정의합니다. 인자: self, path. 반환 타입: int. def 자체는 본문을 실행하지 않습니다. |
| [244](../주석코드/budget_app/service.py#L244) | <code>        &quot;&quot;&quot;한 행이라도 잘못되면 전체 취소. 디스크 스테이징으로 메모리 상수 유지.&quot;&quot;&quot;</code> | 파일/클래스/함수의 목적을 적은 문서 문자열(docstring)입니다. |
| [245](../주석코드/budget_app/service.py#L245) | <code>        # 가져오는 행마다 파일을 다시 읽지 않도록 카테고리 이름을 집합으로 준비합니다.</code> | 설명 주석입니다. 가져오는 행마다 파일을 다시 읽지 않도록 카테고리 이름을 집합으로 준비합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [246](../주석코드/budget_app/service.py#L246) | <code>        categories = set(self.categories())</code> | 가져오는 행마다 파일을 다시 읽지 않도록 카테고리 이름을 집합으로 준비합니다. / 오른쪽 계산/호출 결과를 categories에 저장합니다. |
| [247](../주석코드/budget_app/service.py#L247) | <code>        # 원본 전체 검증: 손상된 파일을 덮어쓰거나 무시하지 않는다.</code> | 설명 주석입니다. 원본 전체 검증: 손상된 파일을 덮어쓰거나 무시하지 않는다. (Python 실행에는 영향을 주지 않습니다.) |
| [248](../주석코드/budget_app/service.py#L248) | <code>        for _ in self.transactions.iter_all():</code> | 원본 전체 검증: 손상된 파일을 덮어쓰거나 무시하지 않는다. / self.transactions.iter_all()에서 값을 하나씩 받아 _에 넣고 블록을 반복합니다. |
| [249](../주석코드/budget_app/service.py#L249) | <code>            pass</code> | 이 블록에서는 별도 동작을 하지 않습니다. 제너레이터 검증 순회나 초기화용 with 진입만 필요할 때 사용합니다. |
| [250](../주석코드/budget_app/service.py#L250) | <code>        # 원본 폴더 안에 스테이징 공간을 만들고 종료 시 자동 정리합니다.</code> | 설명 주석입니다. 원본 폴더 안에 스테이징 공간을 만들고 종료 시 자동 정리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [251](../주석코드/budget_app/service.py#L251) | <code>        with tempfile.TemporaryDirectory(prefix=&quot;.import-&quot;, dir=self.store.directory) as temporary:</code> | 원본 폴더 안에 스테이징 공간을 만들고 종료 시 자동 정리합니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [252](../주석코드/budget_app/service.py#L252) | <code>            # 실패해도 원본 거래 파일에는 영향이 없도록 별도 파일을 사용합니다.</code> | 설명 주석입니다. 실패해도 원본 거래 파일에는 영향이 없도록 별도 파일을 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [253](../주석코드/budget_app/service.py#L253) | <code>            staged = Path(temporary) / &quot;transactions.jsonl&quot;</code> | 실패해도 원본 거래 파일에는 영향이 없도록 별도 파일을 사용합니다. / 오른쪽 계산/호출 결과를 staged에 저장합니다. |
| [254](../주석코드/budget_app/service.py#L254) | <code>            # 현재 거래를 사본으로 보존해 새 CSV 행을 기존 거래와 합칠 수 있게 합니다.</code> | 설명 주석입니다. 현재 거래를 사본으로 보존해 새 CSV 행을 기존 거래와 합칠 수 있게 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [255](../주석코드/budget_app/service.py#L255) | <code>            shutil.copyfile(self.transactions.path, staged)</code> | 현재 거래를 사본으로 보존해 새 CSV 행을 기존 거래와 합칠 수 있게 합니다. / shutil.copyfile 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [256](../주석코드/budget_app/service.py#L256) | <code>            # 같은 저장소 구현을 임시 경로에 적용해 병합 로직을 재사용합니다.</code> | 설명 주석입니다. 같은 저장소 구현을 임시 경로에 적용해 병합 로직을 재사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [257](../주석코드/budget_app/service.py#L257) | <code>            repository = TransactionRepository(staged)</code> | 같은 저장소 구현을 임시 경로에 적용해 병합 로직을 재사용합니다. / 오른쪽 계산/호출 결과를 repository에 저장합니다. |
| [258](../주석코드/budget_app/service.py#L258) | <code>            count = 0</code> | 오른쪽 계산/호출 결과를 count에 저장합니다. |
| [259](../주석코드/budget_app/service.py#L259) | <code>            # UTF-8과 UTF-8 BOM을 모두 읽습니다. newline=&quot;&quot;은 csv 모듈이 개행을 처리하게 합니다.</code> | 설명 주석입니다. UTF-8과 UTF-8 BOM을 모두 읽습니다. newline=&quot;&quot;은 csv 모듈이 개행을 처리하게 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [260](../주석코드/budget_app/service.py#L260) | <code>            with path.open(encoding=&quot;utf-8-sig&quot;, newline=&quot;&quot;) as stream:</code> | UTF-8과 UTF-8 BOM을 모두 읽습니다. newline=&quot;&quot;은 csv 모듈이 개행을 처리하게 합니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [261](../주석코드/budget_app/service.py#L261) | <code>                # 헤더를 키로 각 행을 dict로 읽고 잘못된 CSV 인용 문법도 검사합니다.</code> | 설명 주석입니다. 헤더를 키로 각 행을 dict로 읽고 잘못된 CSV 인용 문법도 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [262](../주석코드/budget_app/service.py#L262) | <code>                reader = csv.DictReader(stream, strict=True)</code> | 헤더를 키로 각 행을 dict로 읽고 잘못된 CSV 인용 문법도 검사합니다. / 오른쪽 계산/호출 결과를 reader에 저장합니다. |
| [263](../주석코드/budget_app/service.py#L263) | <code>                # 첫 행에서 선언한 열 이름을 검증합니다.</code> | 설명 주석입니다. 첫 행에서 선언한 열 이름을 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [264](../주석코드/budget_app/service.py#L264) | <code>                headers = reader.fieldnames</code> | 첫 행에서 선언한 열 이름을 검증합니다. / 오른쪽 계산/호출 결과를 headers에 저장합니다. |
| [265](../주석코드/budget_app/service.py#L265) | <code>                # 헤더 없음·중복·필수 열 누락·알 수 없는 열을 거부합니다. 선택 열 두 개는 없어도 됩니다.</code> | 설명 주석입니다. 헤더 없음·중복·필수 열 누락·알 수 없는 열을 거부합니다. 선택 열 두 개는 없어도 됩니다. (Python 실행에는 영향을 주지 않습니다.) |
| [266](../주석코드/budget_app/service.py#L266) | <code>                if (not headers or len(headers) != len(set(headers)) or</code> | 헤더 없음·중복·필수 열 누락·알 수 없는 열을 거부합니다. 선택 열 두 개는 없어도 됩니다. / 조건 not headers or len(headers) != len(set(headers)) or (not set(CSV_FIELDS[:4]).issubset(headers)) or set(headers) - set(CSV_FIELDS)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [267](../주석코드/budget_app/service.py#L267) | <code>                        not set(CSV_FIELDS[:4]).issubset(headers) or set(headers) - set(CSV_FIELDS)):</code> | 266행에서 시작한 If 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [268](../주석코드/budget_app/service.py#L268) | <code>                    raise AppError(&quot;CSV 헤더 오류&quot;, &quot;date,type,category,amount,memo,tags 스키마를 사용하세요.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [269](../주석코드/budget_app/service.py#L269) | <code>                # CSV도 한 행씩 소비해 입력 전체를 배열로 만들지 않습니다.</code> | 설명 주석입니다. CSV도 한 행씩 소비해 입력 전체를 배열로 만들지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [270](../주석코드/budget_app/service.py#L270) | <code>                for row in reader:</code> | CSV도 한 행씩 소비해 입력 전체를 배열로 만들지 않습니다. / reader에서 값을 하나씩 받아 row에 넣고 블록을 반복합니다. |
| [271](../주석코드/budget_app/service.py#L271) | <code>                    try:</code> | 오류가 발생할 수 있는 처리를 시작합니다. 해당 except/finally에서 오류 안내와 정리를 처리합니다. |
| [272](../주석코드/budget_app/service.py#L272) | <code>                        # 헤더보다 많거나 적은 필드가 있는 행은 암묵적으로 보정하지 않습니다.</code> | 설명 주석입니다. 헤더보다 많거나 적은 필드가 있는 행은 암묵적으로 보정하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [273](../주석코드/budget_app/service.py#L273) | <code>                        if None in row or any(v is None for v in row.values()):</code> | 헤더보다 많거나 적은 필드가 있는 행은 암묵적으로 보정하지 않습니다. / 조건 None in row or any((v is None for v in row.values()))가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [274](../주석코드/budget_app/service.py#L274) | <code>                            raise AppError(&quot;헤더와 열 개수가 다릅니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [275](../주석코드/budget_app/service.py#L275) | <code>                        # 각 행은 새 id를 발급받습니다. 같은 CSV 재가져오기는 새 거래로 추가됩니다.</code> | 설명 주석입니다. 각 행은 새 id를 발급받습니다. 같은 CSV 재가져오기는 새 거래로 추가됩니다. (Python 실행에는 영향을 주지 않습니다.) |
| [276](../주석코드/budget_app/service.py#L276) | <code>                        transaction = Transaction.create(**row)</code> | 각 행은 새 id를 발급받습니다. 같은 CSV 재가져오기는 새 거래로 추가됩니다. / 오른쪽 계산/호출 결과를 transaction에 저장합니다. |
| [277](../주석코드/budget_app/service.py#L277) | <code>                        if transaction.category not in categories:</code> | 조건 transaction.category not in categories가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [278](../주석코드/budget_app/service.py#L278) | <code>                            raise AppError(f&quot;등록되지 않은 카테고리: {transaction.category}&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [279](../주석코드/budget_app/service.py#L279) | <code>                    # 문제가 난 CSV 줄 번호를 붙이고 전체 취소 사실을 안내합니다.</code> | 설명 주석입니다. 문제가 난 CSV 줄 번호를 붙이고 전체 취소 사실을 안내합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [280](../주석코드/budget_app/service.py#L280) | <code>                    except AppError as exc:</code> | 앞선 try에서 해당 종류의 예외가 발생했을 때 처리할 분기입니다. as 이름이 있으면 예외 객체를 그 이름으로 받습니다. |
| [281](../주석코드/budget_app/service.py#L281) | <code>                        raise AppError(f&quot;CSV {reader.line_num}행: {exc}&quot;, &quot;CSV를 수정하세요. 이번 가져오기는 전부 취소되었습니다.&quot;) from None</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [282](../주석코드/budget_app/service.py#L282) | <code>                    # 원본이 아닌 스테이징 파일에 이 행을 정렬 병합합니다.</code> | 설명 주석입니다. 원본이 아닌 스테이징 파일에 이 행을 정렬 병합합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [283](../주석코드/budget_app/service.py#L283) | <code>                    repository.replace(replacement=transaction)</code> | 원본이 아닌 스테이징 파일에 이 행을 정렬 병합합니다. / repository.replace 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [284](../주석코드/budget_app/service.py#L284) | <code>                    count += 1</code> | 기존 count 값에 계산 결과를 반영해 누적·갱신합니다. |
| [285](../주석코드/budget_app/service.py#L285) | <code>            # 같은 파일시스템 내 원자적 교체. staging의 마지막 쓰기에서 fsync 완료.</code> | 설명 주석입니다. 같은 파일시스템 내 원자적 교체. staging의 마지막 쓰기에서 fsync 완료. (Python 실행에는 영향을 주지 않습니다.) |
| [286](../주석코드/budget_app/service.py#L286) | <code>            # 빈 CSV는 원본을 교체할 필요가 없습니다.</code> | 설명 주석입니다. 빈 CSV는 원본을 교체할 필요가 없습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [287](../주석코드/budget_app/service.py#L287) | <code>            if count:</code> | 빈 CSV는 원본을 교체할 필요가 없습니다. / 조건 count가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [288](../주석코드/budget_app/service.py#L288) | <code>                # 모든 행을 통과했을 때만 최종 반영합니다. 이전 오류는 원본에 전혀 반영되지 않습니다.</code> | 설명 주석입니다. 모든 행을 통과했을 때만 최종 반영합니다. 이전 오류는 원본에 전혀 반영되지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [289](../주석코드/budget_app/service.py#L289) | <code>                os.replace(staged, self.transactions.path)</code> | 모든 행을 통과했을 때만 최종 반영합니다. 이전 오류는 원본에 전혀 반영되지 않습니다. / os.replace 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [290](../주석코드/budget_app/service.py#L290) | <code>            return count</code> | 호출자에게 count을 반환하고 현재 함수 실행을 끝냅니다. |
| [291](../주석코드/budget_app/service.py#L291) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [292](../주석코드/budget_app/service.py#L292) | <code>    # CSV R/출력: 기간 조건에 맞는 거래를 표준 CSV 스키마로 기록하고 건수를 반환합니다.</code> | 설명 주석입니다. CSV R/출력: 기간 조건에 맞는 거래를 표준 CSV 스키마로 기록하고 건수를 반환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [293](../주석코드/budget_app/service.py#L293) | <code>    def export_csv(self, path: Path, filters: Filters) -&gt; int:</code> | CSV R/출력: 기간 조건에 맞는 거래를 표준 CSV 스키마로 기록하고 건수를 반환합니다. / export_csv 함수를 정의합니다. 인자: self, path, filters. 반환 타입: int. def 자체는 본문을 실행하지 않습니다. |
| [294](../주석코드/budget_app/service.py#L294) | <code>        # 내보내기 범위를 의도적으로 선택하도록 최소 하나의 기간 조건을 요구합니다.</code> | 설명 주석입니다. 내보내기 범위를 의도적으로 선택하도록 최소 하나의 기간 조건을 요구합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [295](../주석코드/budget_app/service.py#L295) | <code>        if not (filters.month or filters.start or filters.end):</code> | 내보내기 범위를 의도적으로 선택하도록 최소 하나의 기간 조건을 요구합니다. / 조건 not (filters.month or filters.start or filters.end)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [296](../주석코드/budget_app/service.py#L296) | <code>            raise AppError(&quot;내보내기에는 --month 또는 --from/--to 조건이 필요합니다.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [297](../주석코드/budget_app/service.py#L297) | <code>        # 사용자 출력 경로가 실제 저장 파일을 가리키면 작업을 거부합니다.</code> | 설명 주석입니다. 사용자 출력 경로가 실제 저장 파일을 가리키면 작업을 거부합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [298](../주석코드/budget_app/service.py#L298) | <code>        self.store.protect_output(path)</code> | 사용자 출력 경로가 실제 저장 파일을 가리키면 작업을 거부합니다. / self.store.protect_output 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [299](../주석코드/budget_app/service.py#L299) | <code>        count = 0</code> | 오른쪽 계산/호출 결과를 count에 저장합니다. |
| [300](../주석코드/budget_app/service.py#L300) | <code>        # 내보내기 실패도 기존 CSV를 훼손하지 않도록 같은 안전 쓰기를 사용합니다.</code> | 설명 주석입니다. 내보내기 실패도 기존 CSV를 훼손하지 않도록 같은 안전 쓰기를 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [301](../주석코드/budget_app/service.py#L301) | <code>        with atomic_text(path, newline=&quot;&quot;) as stream:</code> | 내보내기 실패도 기존 CSV를 훼손하지 않도록 같은 안전 쓰기를 사용합니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [302](../주석코드/budget_app/service.py#L302) | <code>            # 고정된 CSV 필드 순서에 맞춰 dict를 기록합니다.</code> | 설명 주석입니다. 고정된 CSV 필드 순서에 맞춰 dict를 기록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [303](../주석코드/budget_app/service.py#L303) | <code>            writer = csv.DictWriter(stream, fieldnames=CSV_FIELDS)</code> | 고정된 CSV 필드 순서에 맞춰 dict를 기록합니다. / 오른쪽 계산/호출 결과를 writer에 저장합니다. |
| [304](../주석코드/budget_app/service.py#L304) | <code>            # 조회 결과가 0건이어도 스키마를 알 수 있게 헤더는 기록합니다.</code> | 설명 주석입니다. 조회 결과가 0건이어도 스키마를 알 수 있게 헤더는 기록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [305](../주석코드/budget_app/service.py#L305) | <code>            writer.writeheader()</code> | 조회 결과가 0건이어도 스키마를 알 수 있게 헤더는 기록합니다. / writer.writeheader 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [306](../주석코드/budget_app/service.py#L306) | <code>            # R: 조건을 통과한 거래를 순서대로 기록합니다.</code> | 설명 주석입니다. R: 조건을 통과한 거래를 순서대로 기록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [307](../주석코드/budget_app/service.py#L307) | <code>            for t in self.search(filters):</code> | R: 조건을 통과한 거래를 순서대로 기록합니다. / self.search(filters)에서 값을 하나씩 받아 t에 넣고 블록을 반복합니다. |
| [308](../주석코드/budget_app/service.py#L308) | <code>                # 모델에서 교환용 여섯 필드만 골라 id를 제외합니다.</code> | 설명 주석입니다. 모델에서 교환용 여섯 필드만 골라 id를 제외합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [309](../주석코드/budget_app/service.py#L309) | <code>                row = {key: getattr(t, key) for key in CSV_FIELDS}</code> | 모델에서 교환용 여섯 필드만 골라 id를 제외합니다. / 오른쪽 계산/호출 결과를 row에 저장합니다. |
| [310](../주석코드/budget_app/service.py#L310) | <code>                # tuple 태그를 쉼표 문자열로 바꿉니다. 쉼표 인용은 csv 모듈이 처리합니다.</code> | 설명 주석입니다. tuple 태그를 쉼표 문자열로 바꿉니다. 쉼표 인용은 csv 모듈이 처리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [311](../주석코드/budget_app/service.py#L311) | <code>                row[&quot;tags&quot;] = &quot;,&quot;.join(t.tags)</code> | tuple 태그를 쉼표 문자열로 바꿉니다. 쉼표 인용은 csv 모듈이 처리합니다. / 오른쪽 계산/호출 결과를 row[&#x27;tags&#x27;]에 저장합니다. |
| [312](../주석코드/budget_app/service.py#L312) | <code>                # 한글·쉼표·큰따옴표·개행을 표준 CSV 규칙으로 기록합니다.</code> | 설명 주석입니다. 한글·쉼표·큰따옴표·개행을 표준 CSV 규칙으로 기록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [313](../주석코드/budget_app/service.py#L313) | <code>                writer.writerow(row)</code> | 한글·쉼표·큰따옴표·개행을 표준 CSV 규칙으로 기록합니다. / writer.writerow 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [314](../주석코드/budget_app/service.py#L314) | <code>                count += 1</code> | 기존 count 값에 계산 결과를 반영해 누적·갱신합니다. |
| [315](../주석코드/budget_app/service.py#L315) | <code>        return count</code> | 호출자에게 count을 반환하고 현재 함수 실행을 끝냅니다. |
| [316](../주석코드/budget_app/service.py#L316) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [317](../주석코드/budget_app/service.py#L317) | <code>    # 보너스 기능: 잠금 안에서 세 JSONL 파일을 ZIP으로 복사하고 생성 경로를 반환합니다.</code> | 설명 주석입니다. 보너스 기능: 잠금 안에서 세 JSONL 파일을 ZIP으로 복사하고 생성 경로를 반환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [318](../주석코드/budget_app/service.py#L318) | <code>    def backup(self) -&gt; Path:</code> | 보너스 기능: 잠금 안에서 세 JSONL 파일을 ZIP으로 복사하고 생성 경로를 반환합니다. / backup 함수를 정의합니다. 인자: self. 반환 타입: Path. def 자체는 본문을 실행하지 않습니다. |
| [319](../주석코드/budget_app/service.py#L319) | <code>        # 사용자가 선택한 데이터 폴더 안에 backups 하위 폴더를 사용합니다.</code> | 설명 주석입니다. 사용자가 선택한 데이터 폴더 안에 backups 하위 폴더를 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [320](../주석코드/budget_app/service.py#L320) | <code>        folder = self.store.directory / &quot;backups&quot;</code> | 사용자가 선택한 데이터 폴더 안에 backups 하위 폴더를 사용합니다. / 오른쪽 계산/호출 결과를 folder에 저장합니다. |
| [321](../주석코드/budget_app/service.py#L321) | <code>        folder.mkdir(exist_ok=True)</code> | folder.mkdir 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [322](../주석코드/budget_app/service.py#L322) | <code>        # 시각의 마이크로초와 UUID 일부를 붙여 백업 이름 충돌을 줄입니다.</code> | 설명 주석입니다. 시각의 마이크로초와 UUID 일부를 붙여 백업 이름 충돌을 줄입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [323](../주석코드/budget_app/service.py#L323) | <code>        path = folder / f&quot;backup-{datetime.now():%Y%m%d-%H%M%S-%f}-{uuid4().hex[:8]}.zip&quot;</code> | 시각의 마이크로초와 UUID 일부를 붙여 백업 이름 충돌을 줄입니다. / 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [324](../주석코드/budget_app/service.py#L324) | <code>        try:</code> | 오류가 발생할 수 있는 처리를 시작합니다. 해당 except/finally에서 오류 안내와 정리를 처리합니다. |
| [325](../주석코드/budget_app/service.py#L325) | <code>            # x 모드는 같은 이름 파일이 있으면 덮어쓰지 않고 실패합니다.</code> | 설명 주석입니다. x 모드는 같은 이름 파일이 있으면 덮어쓰지 않고 실패합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [326](../주석코드/budget_app/service.py#L326) | <code>            with zipfile.ZipFile(path, &quot;x&quot;, zipfile.ZIP_DEFLATED) as archive:</code> | x 모드는 같은 이름 파일이 있으면 덮어쓰지 않고 실패합니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [327](../주석코드/budget_app/service.py#L327) | <code>                for filename in self.store.FILES:</code> | self.store.FILES에서 값을 하나씩 받아 filename에 넣고 블록을 반복합니다. |
| [328](../주석코드/budget_app/service.py#L328) | <code>                    # 압축 내부에는 절대 경로 대신 파일 이름만 기록합니다.</code> | 설명 주석입니다. 압축 내부에는 절대 경로 대신 파일 이름만 기록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [329](../주석코드/budget_app/service.py#L329) | <code>                    archive.write(self.store.directory / filename, arcname=filename)</code> | 압축 내부에는 절대 경로 대신 파일 이름만 기록합니다. / archive.write 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [330](../주석코드/budget_app/service.py#L330) | <code>        # 중단까지 포함해 생성 실패한 불완전 ZIP을 남기지 않도록 정리한 후 다시 오류를 전달합니다.</code> | 설명 주석입니다. 중단까지 포함해 생성 실패한 불완전 ZIP을 남기지 않도록 정리한 후 다시 오류를 전달합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [331](../주석코드/budget_app/service.py#L331) | <code>        except BaseException:</code> | 앞선 try에서 해당 종류의 예외가 발생했을 때 처리할 분기입니다. as 이름이 있으면 예외 객체를 그 이름으로 받습니다. |
| [332](../주석코드/budget_app/service.py#L332) | <code>            path.unlink(missing_ok=True)</code> | path.unlink 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [333](../주석코드/budget_app/service.py#L333) | <code>            raise</code> | 잡은 예외를 다시 발생시켜 상위 호출자에게 전달합니다. |
| [334](../주석코드/budget_app/service.py#L334) | <code>        return path</code> | 호출자에게 path을 반환하고 현재 함수 실행을 끝냅니다. |
