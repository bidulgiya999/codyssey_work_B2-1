# budget_app/cli.py 한 줄씩 설명

대상: [주석 코드](../주석코드/budget_app/cli.py). 총 314줄입니다. 줄 번호는 이 사본과 일치합니다. 설명은 읽기 자료이며 실행할 명령이 아닙니다.

| 줄 | 실제 코드 | 설명 |
| ---: | --- | --- |
| [1](../주석코드/budget_app/cli.py#L1) | <code># CLI 계층: 명령어 해석 → 서비스 호출 → 결과 출력의 흐름을 담당합니다.</code> | 설명 주석입니다. CLI 계층: 명령어 해석 → 서비스 호출 → 결과 출력의 흐름을 담당합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [2](../주석코드/budget_app/cli.py#L2) | <code># 거래 CRUD: add=C, list/search=R, update=U, delete=D입니다.</code> | 설명 주석입니다. 거래 CRUD: add=C, list/search=R, update=U, delete=D입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [3](../주석코드/budget_app/cli.py#L3) | <code>&quot;&quot;&quot;argparse 기반 한국어 콘솔 인터페이스. update는 옵션 방식으로 고정.&quot;&quot;&quot;</code> | 거래 CRUD: add=C, list/search=R, update=U, delete=D입니다. / 파일/클래스/함수의 목적을 적은 문서 문자열(docstring)입니다. |
| [4](../주석코드/budget_app/cli.py#L4) | <code># 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다.</code> | 설명 주석입니다. 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [5](../주석코드/budget_app/cli.py#L5) | <code>from __future__ import annotations</code> | 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다. / __future__에서 필요한 이름을 가져옵니다. |
| [6](../주석코드/budget_app/cli.py#L6) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [7](../주석코드/budget_app/cli.py#L7) | <code># 하위 명령·옵션·도움말·인자 오류를 표준 라이브러리로 처리합니다.</code> | 설명 주석입니다. 하위 명령·옵션·도움말·인자 오류를 표준 라이브러리로 처리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [8](../주석코드/budget_app/cli.py#L8) | <code>import argparse</code> | 하위 명령·옵션·도움말·인자 오류를 표준 라이브러리로 처리합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [9](../주석코드/budget_app/cli.py#L9) | <code># verbose 옵션에서 실행 결과와 소요 시간 로그를 표시합니다.</code> | 설명 주석입니다. verbose 옵션에서 실행 결과와 소요 시간 로그를 표시합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [10](../주석코드/budget_app/cli.py#L10) | <code>import logging</code> | verbose 옵션에서 실행 결과와 소요 시간 로그를 표시합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [11](../주석코드/budget_app/cli.py#L11) | <code># 오류 출력 스트림과 프로세스 실행 관련 정보를 사용합니다.</code> | 설명 주석입니다. 오류 출력 스트림과 프로세스 실행 관련 정보를 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [12](../주석코드/budget_app/cli.py#L12) | <code>import sys</code> | 오류 출력 스트림과 프로세스 실행 관련 정보를 사용합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [13](../주석코드/budget_app/cli.py#L13) | <code># 터미널 제어 문자 검사와 한글 표시 폭 계산에 사용합니다.</code> | 설명 주석입니다. 터미널 제어 문자 검사와 한글 표시 폭 계산에 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [14](../주석코드/budget_app/cli.py#L14) | <code>import unicodedata</code> | 터미널 제어 문자 검사와 한글 표시 폭 계산에 사용합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [15](../주석코드/budget_app/cli.py#L15) | <code># 제너레이터를 전부 읽지 않고 limit개에서 중단합니다.</code> | 설명 주석입니다. 제너레이터를 전부 읽지 않고 limit개에서 중단합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [16](../주석코드/budget_app/cli.py#L16) | <code>from itertools import islice</code> | 제너레이터를 전부 읽지 않고 limit개에서 중단합니다. / itertools에서 필요한 이름을 가져옵니다. |
| [17](../주석코드/budget_app/cli.py#L17) | <code># 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다.</code> | 설명 주석입니다. 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [18](../주석코드/budget_app/cli.py#L18) | <code>from pathlib import Path</code> | 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다. / pathlib에서 필요한 이름을 가져옵니다. |
| [19](../주석코드/budget_app/cli.py#L19) | <code># 목록 출력 함수가 리스트뿐 아니라 거래 제너레이터도 받도록 합니다.</code> | 설명 주석입니다. 목록 출력 함수가 리스트뿐 아니라 거래 제너레이터도 받도록 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [20](../주석코드/budget_app/cli.py#L20) | <code>from typing import Iterable</code> | 목록 출력 함수가 리스트뿐 아니라 거래 제너레이터도 받도록 합니다. / typing에서 필요한 이름을 가져옵니다. |
| [21](../주석코드/budget_app/cli.py#L21) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [22](../주석코드/budget_app/cli.py#L22) | <code># 명령 함수를 감싸는 공통 오류·종료 코드·시간 측정 처리를 사용합니다.</code> | 설명 주석입니다. 명령 함수를 감싸는 공통 오류·종료 코드·시간 측정 처리를 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [23](../주석코드/budget_app/cli.py#L23) | <code>from .decorators import command_boundary</code> | 명령 함수를 감싸는 공통 오류·종료 코드·시간 측정 처리를 사용합니다. / decorators에서 필요한 이름을 가져옵니다. |
| [24](../주석코드/budget_app/cli.py#L24) | <code># 거래 모델 및 금액·출력 건수 검증을 CLI에서 재사용합니다.</code> | 설명 주석입니다. 거래 모델 및 금액·출력 건수 검증을 CLI에서 재사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [25](../주석코드/budget_app/cli.py#L25) | <code>from .models import AppError, Transaction, positive</code> | 거래 모델 및 금액·출력 건수 검증을 CLI에서 재사용합니다. / models에서 필요한 이름을 가져옵니다. |
| [26](../주석코드/budget_app/cli.py#L26) | <code># CLI 또는 테스트가 서비스 업무 규칙과 검색 조건 객체를 사용합니다.</code> | 설명 주석입니다. CLI 또는 테스트가 서비스 업무 규칙과 검색 조건 객체를 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [27](../주석코드/budget_app/cli.py#L27) | <code>from .service import BudgetService, Filters</code> | CLI 또는 테스트가 서비스 업무 규칙과 검색 조건 객체를 사용합니다. / service에서 필요한 이름을 가져옵니다. |
| [28](../주석코드/budget_app/cli.py#L28) | <code># 파일 경로와 초기화·명령 단위 잠금을 관리하는 저장소 객체를 연결합니다.</code> | 설명 주석입니다. 파일 경로와 초기화·명령 단위 잠금을 관리하는 저장소 객체를 연결합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [29](../주석코드/budget_app/cli.py#L29) | <code>from .storage import DataStore</code> | 파일 경로와 초기화·명령 단위 잠금을 관리하는 저장소 객체를 연결합니다. / storage에서 필요한 이름을 가져옵니다. |
| [30](../주석코드/budget_app/cli.py#L30) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [31](../주석코드/budget_app/cli.py#L31) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [32](../주석코드/budget_app/cli.py#L32) | <code># argparse를 상속해 인자 오류도 원인+힌트 형식과 종료 코드 2로 통일합니다.</code> | 설명 주석입니다. argparse를 상속해 인자 오류도 원인+힌트 형식과 종료 코드 2로 통일합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [33](../주석코드/budget_app/cli.py#L33) | <code>class Parser(argparse.ArgumentParser):</code> | argparse를 상속해 인자 오류도 원인+힌트 형식과 종료 코드 2로 통일합니다. / Parser 클래스의 정의를 시작합니다. 들여쓴 메서드와 속성이 이 클래스에 속합니다. |
| [34](../주석코드/budget_app/cli.py#L34) | <code>    # argparse가 잘못된 옵션·필수 인자 누락을 발견할 때 호출하는 오류 처리입니다.</code> | 설명 주석입니다. argparse가 잘못된 옵션·필수 인자 누락을 발견할 때 호출하는 오류 처리입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [35](../주석코드/budget_app/cli.py#L35) | <code>    def error(self, message: str) -&gt; None:</code> | argparse가 잘못된 옵션·필수 인자 누락을 발견할 때 호출하는 오류 처리입니다. / error 함수를 정의합니다. 인자: self, message. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [36](../주석코드/budget_app/cli.py#L36) | <code>        # 잘못된 명령의 문법부터 보여주고 아래에서 원인과 힌트를 붙입니다.</code> | 설명 주석입니다. 잘못된 명령의 문법부터 보여주고 아래에서 원인과 힌트를 붙입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [37](../주석코드/budget_app/cli.py#L37) | <code>        self.print_usage(sys.stderr)</code> | 잘못된 명령의 문법부터 보여주고 아래에서 원인과 힌트를 붙입니다. / self.print_usage 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [38](../주석코드/budget_app/cli.py#L38) | <code>        # 문법 오류는 argparse 관례대로 종료 코드 2로 끝냅니다.</code> | 설명 주석입니다. 문법 오류는 argparse 관례대로 종료 코드 2로 끝냅니다. (Python 실행에는 영향을 주지 않습니다.) |
| [39](../주석코드/budget_app/cli.py#L39) | <code>        self.exit(2, f&quot;[오류] {message}\n[힌트] 해당 명령의 --help를 확인하세요.\n&quot;)</code> | 문법 오류는 argparse 관례대로 종료 코드 2로 끝냅니다. / self.exit 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [40](../주석코드/budget_app/cli.py#L40) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [41](../주석코드/budget_app/cli.py#L41) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [42](../주석코드/budget_app/cli.py#L42) | <code># 실행하지 않고 명령 문법만 구성합니다. 하위 명령과 옵션을 등록한 Parser를 반환합니다.</code> | 설명 주석입니다. 실행하지 않고 명령 문법만 구성합니다. 하위 명령과 옵션을 등록한 Parser를 반환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [43](../주석코드/budget_app/cli.py#L43) | <code>def parser() -&gt; Parser:</code> | 실행하지 않고 명령 문법만 구성합니다. 하위 명령과 옵션을 등록한 Parser를 반환합니다. / parser 함수를 정의합니다. 인자: 없음. 반환 타입: Parser. def 자체는 본문을 실행하지 않습니다. |
| [44](../주석코드/budget_app/cli.py#L44) | <code>    # 최상위 python -m budget_app 명령의 도움말과 문법을 구성합니다.</code> | 설명 주석입니다. 최상위 python -m budget_app 명령의 도움말과 문법을 구성합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [45](../주석코드/budget_app/cli.py#L45) | <code>    root = Parser(description=&quot;데이터를 안전하게 저장하는 콘솔 가계부&quot;)</code> | 최상위 python -m budget_app 명령의 도움말과 문법을 구성합니다. / 오른쪽 계산/호출 결과를 root에 저장합니다. |
| [46](../주석코드/budget_app/cli.py#L46) | <code>    # 전역 저장 위치 옵션입니다. add 등 하위 명령 앞에서 지정합니다.</code> | 설명 주석입니다. 전역 저장 위치 옵션입니다. add 등 하위 명령 앞에서 지정합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [47](../주석코드/budget_app/cli.py#L47) | <code>    root.add_argument(&quot;--data-dir&quot;, default=&quot;./data&quot;, help=&quot;저장 폴더 (기본: ./data), 명령 앞에 지정&quot;)</code> | 전역 저장 위치 옵션입니다. add 등 하위 명령 앞에서 지정합니다. / root.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [48](../주석코드/budget_app/cli.py#L48) | <code>    # 값을 받지 않는 스위치로, 실행 시간 로그 출력을 켭니다.</code> | 설명 주석입니다. 값을 받지 않는 스위치로, 실행 시간 로그 출력을 켭니다. (Python 실행에는 영향을 주지 않습니다.) |
| [49](../주석코드/budget_app/cli.py#L49) | <code>    root.add_argument(&quot;--verbose&quot;, action=&quot;store_true&quot;, help=&quot;명령 실행 시간/종료 코드 로그 출력&quot;)</code> | 값을 받지 않는 스위치로, 실행 시간 로그 출력을 켭니다. / root.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [50](../주석코드/budget_app/cli.py#L50) | <code>    # 필수 하위 명령을 args.command로 받습니다. 하위 명령도 사용자 정의 Parser를 씁니다.</code> | 설명 주석입니다. 필수 하위 명령을 args.command로 받습니다. 하위 명령도 사용자 정의 Parser를 씁니다. (Python 실행에는 영향을 주지 않습니다.) |
| [51](../주석코드/budget_app/cli.py#L51) | <code>    commands = root.add_subparsers(dest=&quot;command&quot;, required=True, parser_class=Parser)</code> | 필수 하위 명령을 args.command로 받습니다. 하위 명령도 사용자 정의 Parser를 씁니다. / 오른쪽 계산/호출 결과를 commands에 저장합니다. |
| [52](../주석코드/budget_app/cli.py#L52) | <code>    # C(Create): add는 옵션 대신 실행 중 질문으로 값을 받습니다.</code> | 설명 주석입니다. C(Create): add는 옵션 대신 실행 중 질문으로 값을 받습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [53](../주석코드/budget_app/cli.py#L53) | <code>    commands.add_parser(&quot;add&quot;, help=&quot;대화형 거래 추가&quot;)</code> | C(Create): add는 옵션 대신 실행 중 질문으로 값을 받습니다. / commands.add_parser 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [54](../주석코드/budget_app/cli.py#L54) | <code>    # R(Read): list 전용 옵션을 붙일 하위 파서를 만듭니다.</code> | 설명 주석입니다. R(Read): list 전용 옵션을 붙일 하위 파서를 만듭니다. (Python 실행에는 영향을 주지 않습니다.) |
| [55](../주석코드/budget_app/cli.py#L55) | <code>    listing = commands.add_parser(&quot;list&quot;, help=&quot;날짜 최신순 목록&quot;)</code> | R(Read): list 전용 옵션을 붙일 하위 파서를 만듭니다. / 오른쪽 계산/호출 결과를 listing에 저장합니다. |
| [56](../주석코드/budget_app/cli.py#L56) | <code>    # list 기본 최대 출력은 20건이며 실제 양수 검증은 실행 시 합니다.</code> | 설명 주석입니다. list 기본 최대 출력은 20건이며 실제 양수 검증은 실행 시 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [57](../주석코드/budget_app/cli.py#L57) | <code>    listing.add_argument(&quot;--limit&quot;, default=&quot;20&quot;, help=&quot;최대 출력 건수 (기본: 20)&quot;)</code> | list 기본 최대 출력은 20건이며 실제 양수 검증은 실행 시 합니다. / listing.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [58](../주석코드/budget_app/cli.py#L58) | <code>    # R(Read): 검색 명령을 등록합니다.</code> | 설명 주석입니다. R(Read): 검색 명령을 등록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [59](../주석코드/budget_app/cli.py#L59) | <code>    search = commands.add_parser(&quot;search&quot;, help=&quot;조건을 모두 만족하는 거래 검색&quot;)</code> | R(Read): 검색 명령을 등록합니다. / 오른쪽 계산/호출 결과를 search에 저장합니다. |
| [60](../주석코드/budget_app/cli.py#L60) | <code>    # 공통 검색 옵션 등록 함수를 재사용합니다.</code> | 설명 주석입니다. 공통 검색 옵션 등록 함수를 재사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [61](../주석코드/budget_app/cli.py#L61) | <code>    add_filters(search)</code> | 공통 검색 옵션 등록 함수를 재사용합니다. / add_filters 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [62](../주석코드/budget_app/cli.py#L62) | <code>    # 검색은 limit 미지정 시 조건에 맞는 전체 결과를 표시합니다.</code> | 설명 주석입니다. 검색은 limit 미지정 시 조건에 맞는 전체 결과를 표시합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [63](../주석코드/budget_app/cli.py#L63) | <code>    search.add_argument(&quot;--limit&quot;, help=&quot;최대 출력 건수 (미지정 시 전체)&quot;)</code> | 검색은 limit 미지정 시 조건에 맞는 전체 결과를 표시합니다. / search.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [64](../주석코드/budget_app/cli.py#L64) | <code>    # 월 합계와 카테고리 지출 순위를 보여주는 집계 명령입니다.</code> | 설명 주석입니다. 월 합계와 카테고리 지출 순위를 보여주는 집계 명령입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [65](../주석코드/budget_app/cli.py#L65) | <code>    summary = commands.add_parser(&quot;summary&quot;, help=&quot;월별 요약과 지출 TOP N&quot;)</code> | 월 합계와 카테고리 지출 순위를 보여주는 집계 명령입니다. / 오른쪽 계산/호출 결과를 summary에 저장합니다. |
| [66](../주석코드/budget_app/cli.py#L66) | <code>    # 요약 대상 월은 반드시 지정해야 합니다.</code> | 설명 주석입니다. 요약 대상 월은 반드시 지정해야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [67](../주석코드/budget_app/cli.py#L67) | <code>    summary.add_argument(&quot;--month&quot;, required=True, help=&quot;YYYY-MM&quot;)</code> | 요약 대상 월은 반드시 지정해야 합니다. / summary.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [68](../주석코드/budget_app/cli.py#L68) | <code>    # 표시할 지출 카테고리 순위 개수의 기본값은 5입니다.</code> | 설명 주석입니다. 표시할 지출 카테고리 순위 개수의 기본값은 5입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [69](../주석코드/budget_app/cli.py#L69) | <code>    summary.add_argument(&quot;--top&quot;, default=&quot;5&quot;, help=&quot;지출 카테고리 개수 (기본: 5)&quot;)</code> | 표시할 지출 카테고리 순위 개수의 기본값은 5입니다. / summary.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [70](../주석코드/budget_app/cli.py#L70) | <code>    # U(Update): 수정은 옵션 방식으로 고정합니다.</code> | 설명 주석입니다. U(Update): 수정은 옵션 방식으로 고정합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [71](../주석코드/budget_app/cli.py#L71) | <code>    update = commands.add_parser(&quot;update&quot;, help=&quot;옵션 방식으로 거래 수정&quot;)</code> | U(Update): 수정은 옵션 방식으로 고정합니다. / 오른쪽 계산/호출 결과를 update에 저장합니다. |
| [72](../주석코드/budget_app/cli.py#L72) | <code>    # 수정 대상의 고유 id는 필수입니다.</code> | 설명 주석입니다. 수정 대상의 고유 id는 필수입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [73](../주석코드/budget_app/cli.py#L73) | <code>    update.add_argument(&quot;--id&quot;, required=True)</code> | 수정 대상의 고유 id는 필수입니다. / update.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [74](../주석코드/budget_app/cli.py#L74) | <code>    # 동일한 방식으로 여섯 수정 가능 필드를 등록합니다.</code> | 설명 주석입니다. 동일한 방식으로 여섯 수정 가능 필드를 등록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [75](../주석코드/budget_app/cli.py#L75) | <code>    for field in (&quot;date&quot;, &quot;type&quot;, &quot;category&quot;, &quot;amount&quot;, &quot;memo&quot;, &quot;tags&quot;):</code> | 동일한 방식으로 여섯 수정 가능 필드를 등록합니다. / (&#x27;date&#x27;, &#x27;type&#x27;, &#x27;category&#x27;, &#x27;amount&#x27;, &#x27;memo&#x27;, &#x27;tags&#x27;)에서 값을 하나씩 받아 field에 넣고 블록을 반복합니다. |
| [76](../주석코드/budget_app/cli.py#L76) | <code>        # 지정하지 않은 수정 필드는 None으로 받아 나중에 제외합니다.</code> | 설명 주석입니다. 지정하지 않은 수정 필드는 None으로 받아 나중에 제외합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [77](../주석코드/budget_app/cli.py#L77) | <code>        update.add_argument(&quot;--&quot; + field, help=f&quot;변경할 {field}&quot;)</code> | 지정하지 않은 수정 필드는 None으로 받아 나중에 제외합니다. / update.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [78](../주석코드/budget_app/cli.py#L78) | <code>    # D(Delete): 삭제 대상은 id 옵션으로 지정합니다.</code> | 설명 주석입니다. D(Delete): 삭제 대상은 id 옵션으로 지정합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [79](../주석코드/budget_app/cli.py#L79) | <code>    delete = commands.add_parser(&quot;delete&quot;, help=&quot;거래 삭제&quot;)</code> | D(Delete): 삭제 대상은 id 옵션으로 지정합니다. / 오른쪽 계산/호출 결과를 delete에 저장합니다. |
| [80](../주석코드/budget_app/cli.py#L80) | <code>    # id 없는 삭제 요청은 문법 단계에서 차단합니다.</code> | 설명 주석입니다. id 없는 삭제 요청은 문법 단계에서 차단합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [81](../주석코드/budget_app/cli.py#L81) | <code>    delete.add_argument(&quot;--id&quot;, required=True)</code> | id 없는 삭제 요청은 문법 단계에서 차단합니다. / delete.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [82](../주석코드/budget_app/cli.py#L82) | <code>    # 예산은 set/show의 2단계 명령입니다.</code> | 설명 주석입니다. 예산은 set/show의 2단계 명령입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [83](../주석코드/budget_app/cli.py#L83) | <code>    budget = commands.add_parser(&quot;budget&quot;, help=&quot;월 예산 설정/조회&quot;)</code> | 예산은 set/show의 2단계 명령입니다. / 오른쪽 계산/호출 결과를 budget에 저장합니다. |
| [84](../주석코드/budget_app/cli.py#L84) | <code>    # budget 다음의 동작을 args.action으로 구분합니다.</code> | 설명 주석입니다. budget 다음의 동작을 args.action으로 구분합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [85](../주석코드/budget_app/cli.py#L85) | <code>    budgets = budget.add_subparsers(dest=&quot;action&quot;, required=True, parser_class=Parser)</code> | budget 다음의 동작을 args.action으로 구분합니다. / 오른쪽 계산/호출 결과를 budgets에 저장합니다. |
| [86](../주석코드/budget_app/cli.py#L86) | <code>    # 예산 신규 설정과 갱신을 담당하는 하위 명령입니다.</code> | 설명 주석입니다. 예산 신규 설정과 갱신을 담당하는 하위 명령입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [87](../주석코드/budget_app/cli.py#L87) | <code>    setting = budgets.add_parser(&quot;set&quot;, help=&quot;월 예산 설정&quot;)</code> | 예산 신규 설정과 갱신을 담당하는 하위 명령입니다. / 오른쪽 계산/호출 결과를 setting에 저장합니다. |
| [88](../주석코드/budget_app/cli.py#L88) | <code>    # 예산이 적용될 월을 필수로 받습니다.</code> | 설명 주석입니다. 예산이 적용될 월을 필수로 받습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [89](../주석코드/budget_app/cli.py#L89) | <code>    setting.add_argument(&quot;--month&quot;, required=True)</code> | 예산이 적용될 월을 필수로 받습니다. / setting.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [90](../주석코드/budget_app/cli.py#L90) | <code>    # 예산 양수 금액을 필수로 받습니다.</code> | 설명 주석입니다. 예산 양수 금액을 필수로 받습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [91](../주석코드/budget_app/cli.py#L91) | <code>    setting.add_argument(&quot;--amount&quot;, required=True)</code> | 예산 양수 금액을 필수로 받습니다. / setting.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [92](../주석코드/budget_app/cli.py#L92) | <code>    # 저장된 예산을 조회하는 명령입니다.</code> | 설명 주석입니다. 저장된 예산을 조회하는 명령입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [93](../주석코드/budget_app/cli.py#L93) | <code>    showing = budgets.add_parser(&quot;show&quot;, help=&quot;예산 조회&quot;)</code> | 저장된 예산을 조회하는 명령입니다. / 오른쪽 계산/호출 결과를 showing에 저장합니다. |
| [94](../주석코드/budget_app/cli.py#L94) | <code>    # 월을 생략하면 모든 월의 예산을 표시합니다.</code> | 설명 주석입니다. 월을 생략하면 모든 월의 예산을 표시합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [95](../주석코드/budget_app/cli.py#L95) | <code>    showing.add_argument(&quot;--month&quot;, help=&quot;미지정 시 전체 월&quot;)</code> | 월을 생략하면 모든 월의 예산을 표시합니다. / showing.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [96](../주석코드/budget_app/cli.py#L96) | <code>    # 카테고리 추가·조회·삭제의 진입 명령입니다.</code> | 설명 주석입니다. 카테고리 추가·조회·삭제의 진입 명령입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [97](../주석코드/budget_app/cli.py#L97) | <code>    category = commands.add_parser(&quot;category&quot;, help=&quot;카테고리 관리&quot;)</code> | 카테고리 추가·조회·삭제의 진입 명령입니다. / 오른쪽 계산/호출 결과를 category에 저장합니다. |
| [98](../주석코드/budget_app/cli.py#L98) | <code>    # category의 동작도 args.action으로 구분합니다.</code> | 설명 주석입니다. category의 동작도 args.action으로 구분합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [99](../주석코드/budget_app/cli.py#L99) | <code>    categories = category.add_subparsers(dest=&quot;action&quot;, required=True, parser_class=Parser)</code> | category의 동작도 args.action으로 구분합니다. / 오른쪽 계산/호출 결과를 categories에 저장합니다. |
| [100](../주석코드/budget_app/cli.py#L100) | <code>    # 세 카테고리 하위 명령을 같은 구조로 등록합니다.</code> | 설명 주석입니다. 세 카테고리 하위 명령을 같은 구조로 등록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [101](../주석코드/budget_app/cli.py#L101) | <code>    for name in (&quot;add&quot;, &quot;list&quot;, &quot;remove&quot;):</code> | 세 카테고리 하위 명령을 같은 구조로 등록합니다. / (&#x27;add&#x27;, &#x27;list&#x27;, &#x27;remove&#x27;)에서 값을 하나씩 받아 name에 넣고 블록을 반복합니다. |
| [102](../주석코드/budget_app/cli.py#L102) | <code>        # 추가와 삭제는 별도 이름 옵션 없이 실행 중 질문합니다.</code> | 설명 주석입니다. 추가와 삭제는 별도 이름 옵션 없이 실행 중 질문합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [103](../주석코드/budget_app/cli.py#L103) | <code>        categories.add_parser(name, help={&quot;add&quot;: &quot;대화형 추가&quot;, &quot;list&quot;: &quot;목록&quot;, &quot;remove&quot;: &quot;대화형 삭제&quot;}[name])</code> | 추가와 삭제는 별도 이름 옵션 없이 실행 중 질문합니다. / categories.add_parser 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [104](../주석코드/budget_app/cli.py#L104) | <code>    # CSV 일괄 추가 명령을 등록합니다.</code> | 설명 주석입니다. CSV 일괄 추가 명령을 등록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [105](../주석코드/budget_app/cli.py#L105) | <code>    importing = commands.add_parser(&quot;import&quot;, help=&quot;UTF-8 CSV 일괄 등록 (실패 시 전체 취소)&quot;)</code> | CSV 일괄 추가 명령을 등록합니다. / 오른쪽 계산/호출 결과를 importing에 저장합니다. |
| [106](../주석코드/budget_app/cli.py#L106) | <code>    # --from은 Python 이름으로 쓰기 어려우므로 args.source에 매핑합니다.</code> | 설명 주석입니다. --from은 Python 이름으로 쓰기 어려우므로 args.source에 매핑합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [107](../주석코드/budget_app/cli.py#L107) | <code>    importing.add_argument(&quot;--from&quot;, dest=&quot;source&quot;, required=True, help=&quot;CSV 파일 경로&quot;)</code> | --from은 Python 이름으로 쓰기 어려우므로 args.source에 매핑합니다. / importing.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [108](../주석코드/budget_app/cli.py#L108) | <code>    # 검색 조건에 맞는 거래를 CSV로 기록하는 명령입니다.</code> | 설명 주석입니다. 검색 조건에 맞는 거래를 CSV로 기록하는 명령입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [109](../주석코드/budget_app/cli.py#L109) | <code>    exporting = commands.add_parser(&quot;export&quot;, help=&quot;기간 조건을 지정해 CSV 내보내기&quot;)</code> | 검색 조건에 맞는 거래를 CSV로 기록하는 명령입니다. / 오른쪽 계산/호출 결과를 exporting에 저장합니다. |
| [110](../주석코드/budget_app/cli.py#L110) | <code>    # 출력 파일 경로는 필수입니다.</code> | 설명 주석입니다. 출력 파일 경로는 필수입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [111](../주석코드/budget_app/cli.py#L111) | <code>    exporting.add_argument(&quot;--out&quot;, required=True)</code> | 출력 파일 경로는 필수입니다. / exporting.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [112](../주석코드/budget_app/cli.py#L112) | <code>    # 내보내기는 일반 조건에 더해 월 조건도 등록합니다.</code> | 설명 주석입니다. 내보내기는 일반 조건에 더해 월 조건도 등록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [113](../주석코드/budget_app/cli.py#L113) | <code>    add_filters(exporting, month=True)</code> | 내보내기는 일반 조건에 더해 월 조건도 등록합니다. / add_filters 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [114](../주석코드/budget_app/cli.py#L114) | <code>    # 보너스 ZIP 백업 명령을 등록합니다.</code> | 설명 주석입니다. 보너스 ZIP 백업 명령을 등록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [115](../주석코드/budget_app/cli.py#L115) | <code>    commands.add_parser(&quot;backup&quot;, help=&quot;타임스탬프 ZIP 백업 생성&quot;)</code> | 보너스 ZIP 백업 명령을 등록합니다. / commands.add_parser 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [116](../주석코드/budget_app/cli.py#L116) | <code>    # 구성된 파서를 반환합니다. 아직 거래 처리나 파일 저장은 실행하지 않습니다.</code> | 설명 주석입니다. 구성된 파서를 반환합니다. 아직 거래 처리나 파일 저장은 실행하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [117](../주석코드/budget_app/cli.py#L117) | <code>    return root</code> | 구성된 파서를 반환합니다. 아직 거래 처리나 파일 저장은 실행하지 않습니다. / 호출자에게 root을 반환하고 현재 함수 실행을 끝냅니다. |
| [118](../주석코드/budget_app/cli.py#L118) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [119](../주석코드/budget_app/cli.py#L119) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [120](../주석코드/budget_app/cli.py#L120) | <code># search와 export가 공유하는 조건 옵션을 한곳에서 등록합니다.</code> | 설명 주석입니다. search와 export가 공유하는 조건 옵션을 한곳에서 등록합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [121](../주석코드/budget_app/cli.py#L121) | <code>def add_filters(command: argparse.ArgumentParser, month: bool = False) -&gt; None:</code> | search와 export가 공유하는 조건 옵션을 한곳에서 등록합니다. / add_filters 함수를 정의합니다. 인자: command, month. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [122](../주석코드/budget_app/cli.py#L122) | <code>    # 외부 옵션 이름은 --from, 내부 필드 이름은 start입니다.</code> | 설명 주석입니다. 외부 옵션 이름은 --from, 내부 필드 이름은 start입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [123](../주석코드/budget_app/cli.py#L123) | <code>    command.add_argument(&quot;--from&quot;, dest=&quot;start&quot;, help=&quot;시작일 YYYY-MM-DD (포함)&quot;)</code> | 외부 옵션 이름은 --from, 내부 필드 이름은 start입니다. / command.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [124](../주석코드/budget_app/cli.py#L124) | <code>    # 종료 날짜는 end로 받으며 해당 날짜도 검색에 포함합니다.</code> | 설명 주석입니다. 종료 날짜는 end로 받으며 해당 날짜도 검색에 포함합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [125](../주석코드/budget_app/cli.py#L125) | <code>    command.add_argument(&quot;--to&quot;, dest=&quot;end&quot;, help=&quot;종료일 YYYY-MM-DD (포함)&quot;)</code> | 종료 날짜는 end로 받으며 해당 날짜도 검색에 포함합니다. / command.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [126](../주석코드/budget_app/cli.py#L126) | <code>    # 호출자가 허용한 경우에만 --month를 문법에 추가합니다.</code> | 설명 주석입니다. 호출자가 허용한 경우에만 --month를 문법에 추가합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [127](../주석코드/budget_app/cli.py#L127) | <code>    if month:</code> | 호출자가 허용한 경우에만 --month를 문법에 추가합니다. / 조건 month가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [128](../주석코드/budget_app/cli.py#L128) | <code>        # 실제 월/범위 충돌 검사는 Filters에서 수행합니다.</code> | 설명 주석입니다. 실제 월/범위 충돌 검사는 Filters에서 수행합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [129](../주석코드/budget_app/cli.py#L129) | <code>        command.add_argument(&quot;--month&quot;, help=&quot;YYYY-MM, 날짜 범위와 동시 사용 불가&quot;)</code> | 실제 월/범위 충돌 검사는 Filters에서 수행합니다. / command.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [130](../주석코드/budget_app/cli.py#L130) | <code>    # 카테고리 완전 일치 조건입니다.</code> | 설명 주석입니다. 카테고리 완전 일치 조건입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [131](../주석코드/budget_app/cli.py#L131) | <code>    command.add_argument(&quot;--category&quot;)</code> | 카테고리 완전 일치 조건입니다. / command.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [132](../주석코드/budget_app/cli.py#L132) | <code>    # 타입 오타는 argparse choices가 문법 오류로 거부합니다.</code> | 설명 주석입니다. 타입 오타는 argparse choices가 문법 오류로 거부합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [133](../주석코드/budget_app/cli.py#L133) | <code>    command.add_argument(&quot;--type&quot;, choices=(&quot;income&quot;, &quot;expense&quot;))</code> | 타입 오타는 argparse choices가 문법 오류로 거부합니다. / command.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [134](../주석코드/budget_app/cli.py#L134) | <code>    # 메모의 부분 문자열 검색 옵션입니다.</code> | 설명 주석입니다. 메모의 부분 문자열 검색 옵션입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [135](../주석코드/budget_app/cli.py#L135) | <code>    command.add_argument(&quot;--q&quot;, help=&quot;메모 키워드 (대소문자 무시)&quot;)</code> | 메모의 부분 문자열 검색 옵션입니다. / command.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [136](../주석코드/budget_app/cli.py#L136) | <code>    # 태그 목록 안의 한 값과 완전히 일치해야 합니다.</code> | 설명 주석입니다. 태그 목록 안의 한 값과 완전히 일치해야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [137](../주석코드/budget_app/cli.py#L137) | <code>    command.add_argument(&quot;--tag&quot;, help=&quot;태그 완전 일치&quot;)</code> | 태그 목록 안의 한 값과 완전히 일치해야 합니다. / command.add_argument 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [138](../주석코드/budget_app/cli.py#L138) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [139](../주석코드/budget_app/cli.py#L139) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [140](../주석코드/budget_app/cli.py#L140) | <code># argparse.Namespace에서 검색 관련 값만 골라 Filters 객체로 변환합니다.</code> | 설명 주석입니다. argparse.Namespace에서 검색 관련 값만 골라 Filters 객체로 변환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [141](../주석코드/budget_app/cli.py#L141) | <code>def filters_from(args: argparse.Namespace) -&gt; Filters:</code> | argparse.Namespace에서 검색 관련 값만 골라 Filters 객체로 변환합니다. / filters_from 함수를 정의합니다. 인자: args. 반환 타입: Filters. def 자체는 본문을 실행하지 않습니다. |
| [142](../주석코드/budget_app/cli.py#L142) | <code>    # 각 옵션 값을 꺼내 데이터 객체로 넘겨 검색 조건 계약을 통일합니다.</code> | 설명 주석입니다. 각 옵션 값을 꺼내 데이터 객체로 넘겨 검색 조건 계약을 통일합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [143](../주석코드/budget_app/cli.py#L143) | <code>    return Filters(**{key: getattr(args, key, None)</code> | 각 옵션 값을 꺼내 데이터 객체로 넘겨 검색 조건 계약을 통일합니다. / 호출자에게 Filters(**{key: getattr(args, key, None) for key in (&#x27;start&#x27;, &#x27;end&#x27;, &#x27;month&#x27;, &#x27;category&#x27;, &#x27;type&#x27;, &#x27;q&#x27;, &#x27;tag&#x27;)})을 반환하고 현재 함수 실행을 끝냅니다. |
| [144](../주석코드/budget_app/cli.py#L144) | <code>                      for key in (&quot;start&quot;, &quot;end&quot;, &quot;month&quot;, &quot;category&quot;, &quot;type&quot;, &quot;q&quot;, &quot;tag&quot;)})</code> | 143행에서 시작한 Return 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [145](../주석코드/budget_app/cli.py#L145) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [146](../주석코드/budget_app/cli.py#L146) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [147](../주석코드/budget_app/cli.py#L147) | <code># 사용자 데이터의 제어 문자를 화면에서 보이는 이스케이프로 바꿔 터미널 표시를 보호합니다.</code> | 설명 주석입니다. 사용자 데이터의 제어 문자를 화면에서 보이는 이스케이프로 바꿔 터미널 표시를 보호합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [148](../주석코드/budget_app/cli.py#L148) | <code>def display(value: object) -&gt; str:</code> | 사용자 데이터의 제어 문자를 화면에서 보이는 이스케이프로 바꿔 터미널 표시를 보호합니다. / display 함수를 정의합니다. 인자: value. 반환 타입: str. def 자체는 본문을 실행하지 않습니다. |
| [149](../주석코드/budget_app/cli.py#L149) | <code>    &quot;&quot;&quot;개행/탭/터미널 제어 문자를 화면에서 이스케이프한다.&quot;&quot;&quot;</code> | 파일/클래스/함수의 목적을 적은 문서 문자열(docstring)입니다. |
| [150](../주석코드/budget_app/cli.py#L150) | <code>    # 제어 문자만 \uXXXX 표기로 바꾸며 일반 한글은 그대로 둡니다.</code> | 설명 주석입니다. 제어 문자만 \uXXXX 표기로 바꾸며 일반 한글은 그대로 둡니다. (Python 실행에는 영향을 주지 않습니다.) |
| [151](../주석코드/budget_app/cli.py#L151) | <code>    return &quot;&quot;.join(f&quot;\\u{ord(c):04x}&quot; if unicodedata.category(c).startswith(&quot;C&quot;) else c for c in str(value))</code> | 제어 문자만 \uXXXX 표기로 바꾸며 일반 한글은 그대로 둡니다. / 호출자에게 &#x27;&#x27;.join((f&#x27;\\u{ord(c):04x}&#x27; if unicodedata.category(c).startswith(&#x27;C&#x27;) else c for c in str(value)))을 반환하고 현재 함수 실행을 끝냅니다. |
| [152](../주석코드/budget_app/cli.py#L152) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [153](../주석코드/budget_app/cli.py#L153) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [154](../주석코드/budget_app/cli.py#L154) | <code># 한글 등 넓은 문자의 화면 폭을 고려해 표 열의 오른쪽을 공백으로 채웁니다.</code> | 설명 주석입니다. 한글 등 넓은 문자의 화면 폭을 고려해 표 열의 오른쪽을 공백으로 채웁니다. (Python 실행에는 영향을 주지 않습니다.) |
| [155](../주석코드/budget_app/cli.py#L155) | <code>def pad(value: str, width: int) -&gt; str:</code> | 한글 등 넓은 문자의 화면 폭을 고려해 표 열의 오른쪽을 공백으로 채웁니다. / pad 함수를 정의합니다. 인자: value, width. 반환 타입: str. def 자체는 본문을 실행하지 않습니다. |
| [156](../주석코드/budget_app/cli.py#L156) | <code>    # 동아시아 전각/넓은 문자는 화면 두 칸으로 계산합니다.</code> | 설명 주석입니다. 동아시아 전각/넓은 문자는 화면 두 칸으로 계산합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [157](../주석코드/budget_app/cli.py#L157) | <code>    cells = sum(2 if unicodedata.east_asian_width(c) in (&quot;W&quot;, &quot;F&quot;) else 1 for c in value)</code> | 동아시아 전각/넓은 문자는 화면 두 칸으로 계산합니다. / 오른쪽 계산/호출 결과를 cells에 저장합니다. |
| [158](../주석코드/budget_app/cli.py#L158) | <code>    # 목표 폭보다 짧을 때만 공백을 붙이고 긴 내용은 자르지 않습니다.</code> | 설명 주석입니다. 목표 폭보다 짧을 때만 공백을 붙이고 긴 내용은 자르지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [159](../주석코드/budget_app/cli.py#L159) | <code>    return value + &quot; &quot; * max(0, width - cells)</code> | 목표 폭보다 짧을 때만 공백을 붙이고 긴 내용은 자르지 않습니다. / 호출자에게 value + &#x27; &#x27; * max(0, width - cells)을 반환하고 현재 함수 실행을 끝냅니다. |
| [160](../주석코드/budget_app/cli.py#L160) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [161](../주석코드/budget_app/cli.py#L161) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [162](../주석코드/budget_app/cli.py#L162) | <code># 거래 Iterable을 한 건씩 출력하고 실제 출력 건수 또는 데이터 없음을 표시합니다.</code> | 설명 주석입니다. 거래 Iterable을 한 건씩 출력하고 실제 출력 건수 또는 데이터 없음을 표시합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [163](../주석코드/budget_app/cli.py#L163) | <code>def print_transactions(transactions: Iterable[Transaction]) -&gt; None:</code> | 거래 Iterable을 한 건씩 출력하고 실제 출력 건수 또는 데이터 없음을 표시합니다. / print_transactions 함수를 정의합니다. 인자: transactions. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [164](../주석코드/budget_app/cli.py#L164) | <code>    count = 0</code> | 오른쪽 계산/호출 결과를 count에 저장합니다. |
| [165](../주석코드/budget_app/cli.py#L165) | <code>    # 거래가 없어도 표의 각 열 의미를 먼저 보여줍니다.</code> | 설명 주석입니다. 거래가 없어도 표의 각 열 의미를 먼저 보여줍니다. (Python 실행에는 영향을 주지 않습니다.) |
| [166](../주석코드/budget_app/cli.py#L166) | <code>    print(&quot;ID &#124; 날짜 &#124; 타입 &#124; 카테고리 &#124; 금액 &#124; 메모 &#124; 태그&quot;)</code> | 거래가 없어도 표의 각 열 의미를 먼저 보여줍니다. / print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [167](../주석코드/budget_app/cli.py#L167) | <code>    # Iterable을 순회하므로 제너레이터를 그대로 소비할 수 있습니다.</code> | 설명 주석입니다. Iterable을 순회하므로 제너레이터를 그대로 소비할 수 있습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [168](../주석코드/budget_app/cli.py#L168) | <code>    for t in transactions:</code> | Iterable을 순회하므로 제너레이터를 그대로 소비할 수 있습니다. / transactions에서 값을 하나씩 받아 t에 넣고 블록을 반복합니다. |
| [169](../주석코드/budget_app/cli.py#L169) | <code>        # 금액은 천 단위 구분자를 넣고 타입/카테고리 열을 정렬해 표시합니다.</code> | 설명 주석입니다. 금액은 천 단위 구분자를 넣고 타입/카테고리 열을 정렬해 표시합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [170](../주석코드/budget_app/cli.py#L170) | <code>        print(f&quot;{t.id} &#124; {t.date} &#124; {t.type:7} &#124; {pad(display(t.category), 12)} &#124; &quot;</code> | 금액은 천 단위 구분자를 넣고 타입/카테고리 열을 정렬해 표시합니다. / print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [171](../주석코드/budget_app/cli.py#L171) | <code>              f&quot;{t.amount:&gt;10,} &#124; {display(t.memo)} &#124; {display(&#x27;,&#x27;.join(t.tags))}&quot;)</code> | 170행에서 시작한 Expr 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [172](../주석코드/budget_app/cli.py#L172) | <code>        # 실제 출력한 건수만 셉니다.</code> | 설명 주석입니다. 실제 출력한 건수만 셉니다. (Python 실행에는 영향을 주지 않습니다.) |
| [173](../주석코드/budget_app/cli.py#L173) | <code>        count += 1</code> | 실제 출력한 건수만 셉니다. / 기존 count 값에 계산 결과를 반영해 누적·갱신합니다. |
| [174](../주석코드/budget_app/cli.py#L174) | <code>    # 결과가 0건이면 데이터 없음을 명확히 표시합니다.</code> | 설명 주석입니다. 결과가 0건이면 데이터 없음을 명확히 표시합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [175](../주석코드/budget_app/cli.py#L175) | <code>    print(f&quot;[조회] {count}건&quot; if count else &quot;데이터 없음&quot;)</code> | 결과가 0건이면 데이터 없음을 명확히 표시합니다. / print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [176](../주석코드/budget_app/cli.py#L176) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [177](../주석코드/budget_app/cli.py#L177) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [178](../주석코드/budget_app/cli.py#L178) | <code># 이 함수의 실행을 공통 오류·종료 코드·시간 측정 처리로 감쌉니다.</code> | 설명 주석입니다. 이 함수의 실행을 공통 오류·종료 코드·시간 측정 처리로 감쌉니다. (Python 실행에는 영향을 주지 않습니다.) |
| [179](../주석코드/budget_app/cli.py#L179) | <code>@command_boundary</code> | 바로 아래 함수/클래스에 command_boundary 데코레이터를 적용합니다. 중간 설명 주석은 적용 대상을 바꾸지 않습니다. |
| [180](../주석코드/budget_app/cli.py#L180) | <code># 파싱된 명령을 서비스에 연결합니다. CRUD 정책과 파일 기록은 각 계층에 위임합니다.</code> | 설명 주석입니다. 파싱된 명령을 서비스에 연결합니다. CRUD 정책과 파일 기록은 각 계층에 위임합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [181](../주석코드/budget_app/cli.py#L181) | <code>def execute(args: argparse.Namespace) -&gt; None:</code> | 파싱된 명령을 서비스에 연결합니다. CRUD 정책과 파일 기록은 각 계층에 위임합니다. / execute 함수를 정의합니다. 인자: args. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [182](../주석코드/budget_app/cli.py#L182) | <code>    # 사용자가 정한 폴더에 연결합니다. 실제 초기화는 session 안에서 합니다.</code> | 설명 주석입니다. 사용자가 정한 폴더에 연결합니다. 실제 초기화는 session 안에서 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [183](../주석코드/budget_app/cli.py#L183) | <code>    store = DataStore(Path(args.data_dir))</code> | 사용자가 정한 폴더에 연결합니다. 실제 초기화는 session 안에서 합니다. / 오른쪽 계산/호출 결과를 store에 저장합니다. |
| [184](../주석코드/budget_app/cli.py#L184) | <code>    # 입력부터 저장/조회 종료까지 같은 잠금을 유지해 동시 변경을 막습니다.</code> | 설명 주석입니다. 입력부터 저장/조회 종료까지 같은 잠금을 유지해 동시 변경을 막습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [185](../주석코드/budget_app/cli.py#L185) | <code>    with store.session():</code> | 입력부터 저장/조회 종료까지 같은 잠금을 유지해 동시 변경을 막습니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [186](../주석코드/budget_app/cli.py#L186) | <code>        # 저장 폴더에 연결된 업무 서비스 객체를 만듭니다.</code> | 설명 주석입니다. 저장 폴더에 연결된 업무 서비스 객체를 만듭니다. (Python 실행에는 영향을 주지 않습니다.) |
| [187](../주석코드/budget_app/cli.py#L187) | <code>        service = BudgetService(store)</code> | 저장 폴더에 연결된 업무 서비스 객체를 만듭니다. / 오른쪽 계산/호출 결과를 service에 저장합니다. |
| [188](../주석코드/budget_app/cli.py#L188) | <code>        # 하위 명령 이름으로 아래 실행 경로를 선택합니다.</code> | 설명 주석입니다. 하위 명령 이름으로 아래 실행 경로를 선택합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [189](../주석코드/budget_app/cli.py#L189) | <code>        command = args.command</code> | 하위 명령 이름으로 아래 실행 경로를 선택합니다. / 오른쪽 계산/호출 결과를 command에 저장합니다. |
| [190](../주석코드/budget_app/cli.py#L190) | <code>        # C(Create): 질문 입력 → 모델 검증 → 카테고리 확인 → 안전 저장.</code> | 설명 주석입니다. C(Create): 질문 입력 → 모델 검증 → 카테고리 확인 → 안전 저장. (Python 실행에는 영향을 주지 않습니다.) |
| [191](../주석코드/budget_app/cli.py#L191) | <code>        if command == &quot;add&quot;:</code> | C(Create): 질문 입력 → 모델 검증 → 카테고리 확인 → 안전 저장. / 조건 command == &#x27;add&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [192](../주석코드/budget_app/cli.py#L192) | <code>            # 사용자가 입력 가능한 카테고리 목록을 먼저 안내합니다.</code> | 설명 주석입니다. 사용자가 입력 가능한 카테고리 목록을 먼저 안내합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [193](../주석코드/budget_app/cli.py#L193) | <code>            print(&quot;등록된 카테고리: &quot; + &quot;, &quot;.join(service.categories()))</code> | 사용자가 입력 가능한 카테고리 목록을 먼저 안내합니다. / print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [194](../주석코드/budget_app/cli.py#L194) | <code>            # input 값으로 모델을 만듭니다. 이 호출이 성공해야 서비스 저장으로 넘어갑니다.</code> | 설명 주석입니다. input 값으로 모델을 만듭니다. 이 호출이 성공해야 서비스 저장으로 넘어갑니다. (Python 실행에는 영향을 주지 않습니다.) |
| [195](../주석코드/budget_app/cli.py#L195) | <code>            transaction = Transaction.create(</code> | input 값으로 모델을 만듭니다. 이 호출이 성공해야 서비스 저장으로 넘어갑니다. / 오른쪽 계산/호출 결과를 transaction에 저장합니다. |
| [196](../주석코드/budget_app/cli.py#L196) | <code>                # 날짜는 문자열로 입력받고 앞뒤 공백을 제거합니다.</code> | 설명 주석입니다. 날짜는 문자열로 입력받고 앞뒤 공백을 제거합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [197](../주석코드/budget_app/cli.py#L197) | <code>                date=input(&quot;날짜(YYYY-MM-DD): &quot;).strip(),</code> | 날짜는 문자열로 입력받고 앞뒤 공백을 제거합니다. / 195행에서 시작한 Assign 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [198](../주석코드/budget_app/cli.py#L198) | <code>                # income 또는 expense를 받습니다. 실제 제한은 모델에서 검증합니다.</code> | 설명 주석입니다. income 또는 expense를 받습니다. 실제 제한은 모델에서 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [199](../주석코드/budget_app/cli.py#L199) | <code>                type=input(&quot;타입(income/expense): &quot;).strip(),</code> | income 또는 expense를 받습니다. 실제 제한은 모델에서 검증합니다. / 195행에서 시작한 Assign 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [200](../주석코드/budget_app/cli.py#L200) | <code>                # 등록된 이름인지 서비스에서 검사할 값입니다.</code> | 설명 주석입니다. 등록된 이름인지 서비스에서 검사할 값입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [201](../주석코드/budget_app/cli.py#L201) | <code>                category=input(&quot;카테고리: &quot;).strip(),</code> | 등록된 이름인지 서비스에서 검사할 값입니다. / 195행에서 시작한 Assign 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [202](../주석코드/budget_app/cli.py#L202) | <code>                # 문자열 입력을 모델의 positive가 정수로 검증·변환합니다.</code> | 설명 주석입니다. 문자열 입력을 모델의 positive가 정수로 검증·변환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [203](../주석코드/budget_app/cli.py#L203) | <code>                amount=input(&quot;금액(양수 정수): &quot;).strip(),</code> | 문자열 입력을 모델의 positive가 정수로 검증·변환합니다. / 195행에서 시작한 Assign 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [204](../주석코드/budget_app/cli.py#L204) | <code>                # 메모는 공백도 내용일 수 있어 그대로 받고, 태그는 모델에서 쉼표 분리합니다.</code> | 설명 주석입니다. 메모는 공백도 내용일 수 있어 그대로 받고, 태그는 모델에서 쉼표 분리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [205](../주석코드/budget_app/cli.py#L205) | <code>                memo=input(&quot;메모(선택): &quot;), tags=input(&quot;태그(쉼표 구분, 선택): &quot;))</code> | 메모는 공백도 내용일 수 있어 그대로 받고, 태그는 모델에서 쉼표 분리합니다. / 195행에서 시작한 Assign 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [206](../주석코드/budget_app/cli.py#L206) | <code>            # C: 입력이 모두 유효하면 서비스에 영구 저장을 요청합니다.</code> | 설명 주석입니다. C: 입력이 모두 유효하면 서비스에 영구 저장을 요청합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [207](../주석코드/budget_app/cli.py#L207) | <code>            service.add(transaction)</code> | C: 입력이 모두 유효하면 서비스에 영구 저장을 요청합니다. / service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [208](../주석코드/budget_app/cli.py#L208) | <code>            # 저장이 실제 성공한 뒤에만 새 id를 안내합니다.</code> | 설명 주석입니다. 저장이 실제 성공한 뒤에만 새 id를 안내합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [209](../주석코드/budget_app/cli.py#L209) | <code>            print(f&quot;[저장 완료] id={transaction.id}&quot;)</code> | 저장이 실제 성공한 뒤에만 새 id를 안내합니다. / print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [210](../주석코드/budget_app/cli.py#L210) | <code>        # R(Read): list와 search는 같은 스트리밍 조회·출력 경로를 공유합니다.</code> | 설명 주석입니다. R(Read): list와 search는 같은 스트리밍 조회·출력 경로를 공유합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [211](../주석코드/budget_app/cli.py#L211) | <code>        elif command in (&quot;list&quot;, &quot;search&quot;):</code> | R(Read): list와 search는 같은 스트리밍 조회·출력 경로를 공유합니다. / 조건 command in (&#x27;list&#x27;, &#x27;search&#x27;)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [212](../주석코드/budget_app/cli.py#L212) | <code>            # 제한 건수도 양수로 검증합니다. None이면 검색 결과 전체를 허용합니다.</code> | 설명 주석입니다. 제한 건수도 양수로 검증합니다. None이면 검색 결과 전체를 허용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [213](../주석코드/budget_app/cli.py#L213) | <code>            limit = positive(args.limit) if args.limit is not None else None</code> | 제한 건수도 양수로 검증합니다. None이면 검색 결과 전체를 허용합니다. / 오른쪽 계산/호출 결과를 limit에 저장합니다. |
| [214](../주석코드/budget_app/cli.py#L214) | <code>            # list는 조건 없는 Filters, search는 사용자가 선택한 조건을 사용합니다.</code> | 설명 주석입니다. list는 조건 없는 Filters, search는 사용자가 선택한 조건을 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [215](../주석코드/budget_app/cli.py#L215) | <code>            transactions = service.search(Filters() if command == &quot;list&quot; else filters_from(args))</code> | list는 조건 없는 Filters, search는 사용자가 선택한 조건을 사용합니다. / 오른쪽 계산/호출 결과를 transactions에 저장합니다. |
| [216](../주석코드/budget_app/cli.py#L216) | <code>            # limit까지만 제너레이터를 소비하므로 뒤쪽 파일을 불필요하게 읽지 않습니다.</code> | 설명 주석입니다. limit까지만 제너레이터를 소비하므로 뒤쪽 파일을 불필요하게 읽지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [217](../주석코드/budget_app/cli.py#L217) | <code>            print_transactions(islice(transactions, limit))</code> | limit까지만 제너레이터를 소비하므로 뒤쪽 파일을 불필요하게 읽지 않습니다. / print_transactions 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [218](../주석코드/budget_app/cli.py#L218) | <code>        # U(Update): 사용자가 실제로 지정한 옵션만 수정 요청으로 보냅니다.</code> | 설명 주석입니다. U(Update): 사용자가 실제로 지정한 옵션만 수정 요청으로 보냅니다. (Python 실행에는 영향을 주지 않습니다.) |
| [219](../주석코드/budget_app/cli.py#L219) | <code>        elif command == &quot;update&quot;:</code> | U(Update): 사용자가 실제로 지정한 옵션만 수정 요청으로 보냅니다. / 조건 command == &#x27;update&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [220](../주석코드/budget_app/cli.py#L220) | <code>            # None은 미지정이므로 제외합니다. 빈 문자열은 유지해 메모/태그를 지울 수 있게 합니다.</code> | 설명 주석입니다. None은 미지정이므로 제외합니다. 빈 문자열은 유지해 메모/태그를 지울 수 있게 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [221](../주석코드/budget_app/cli.py#L221) | <code>            changes = {key: getattr(args, key) for key in (&quot;date&quot;, &quot;type&quot;, &quot;category&quot;, &quot;amount&quot;, &quot;memo&quot;, &quot;tags&quot;)</code> | None은 미지정이므로 제외합니다. 빈 문자열은 유지해 메모/태그를 지울 수 있게 합니다. / 오른쪽 계산/호출 결과를 changes에 저장합니다. |
| [222](../주석코드/budget_app/cli.py#L222) | <code>                       if getattr(args, key) is not None}</code> | 221행에서 시작한 Assign 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [223](../주석코드/budget_app/cli.py#L223) | <code>            # 대상 id 조회와 새 값 검증·저장을 서비스에 위임합니다.</code> | 설명 주석입니다. 대상 id 조회와 새 값 검증·저장을 서비스에 위임합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [224](../주석코드/budget_app/cli.py#L224) | <code>            service.update(args.id, changes)</code> | 대상 id 조회와 새 값 검증·저장을 서비스에 위임합니다. / service.update 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [225](../주석코드/budget_app/cli.py#L225) | <code>            print(f&quot;[수정 완료] id={args.id}&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [226](../주석코드/budget_app/cli.py#L226) | <code>        # D(Delete): 서비스가 존재 여부 확인 후 대상만 제외해 파일을 재작성합니다.</code> | 설명 주석입니다. D(Delete): 서비스가 존재 여부 확인 후 대상만 제외해 파일을 재작성합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [227](../주석코드/budget_app/cli.py#L227) | <code>        elif command == &quot;delete&quot;:</code> | D(Delete): 서비스가 존재 여부 확인 후 대상만 제외해 파일을 재작성합니다. / 조건 command == &#x27;delete&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [228](../주석코드/budget_app/cli.py#L228) | <code>            # 없는 id이면 이 호출에서 오류가 발생하고 아래 성공 메시지는 실행되지 않습니다.</code> | 설명 주석입니다. 없는 id이면 이 호출에서 오류가 발생하고 아래 성공 메시지는 실행되지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [229](../주석코드/budget_app/cli.py#L229) | <code>            service.delete(args.id)</code> | 없는 id이면 이 호출에서 오류가 발생하고 아래 성공 메시지는 실행되지 않습니다. / service.delete 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [230](../주석코드/budget_app/cli.py#L230) | <code>            print(f&quot;[삭제 완료] id={args.id}&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [231](../주석코드/budget_app/cli.py#L231) | <code>        # 카테고리 관리 분기입니다. 거래 CRUD와 별도의 메타데이터를 수정합니다.</code> | 설명 주석입니다. 카테고리 관리 분기입니다. 거래 CRUD와 별도의 메타데이터를 수정합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [232](../주석코드/budget_app/cli.py#L232) | <code>        elif command == &quot;category&quot;:</code> | 카테고리 관리 분기입니다. 거래 CRUD와 별도의 메타데이터를 수정합니다. / 조건 command == &#x27;category&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [233](../주석코드/budget_app/cli.py#L233) | <code>            if args.action == &quot;list&quot;:</code> | 조건 args.action == &#x27;list&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [234](../주석코드/budget_app/cli.py#L234) | <code>                # 검증된 카테고리 목록을 한 줄씩 화면에 표시합니다.</code> | 설명 주석입니다. 검증된 카테고리 목록을 한 줄씩 화면에 표시합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [235](../주석코드/budget_app/cli.py#L235) | <code>                for name in service.categories():</code> | 검증된 카테고리 목록을 한 줄씩 화면에 표시합니다. / service.categories()에서 값을 하나씩 받아 name에 넣고 블록을 반복합니다. |
| [236](../주석코드/budget_app/cli.py#L236) | <code>                    print(&quot;- &quot; + display(name))</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [237](../주석코드/budget_app/cli.py#L237) | <code>            elif args.action == &quot;add&quot;:</code> | 조건 args.action == &#x27;add&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [238](../주석코드/budget_app/cli.py#L238) | <code>                # 이름 입력과 화면 출력은 CLI, 중복 검증과 저장은 서비스가 담당합니다.</code> | 설명 주석입니다. 이름 입력과 화면 출력은 CLI, 중복 검증과 저장은 서비스가 담당합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [239](../주석코드/budget_app/cli.py#L239) | <code>                name = service.category_add(input(&quot;카테고리명: &quot;))</code> | 이름 입력과 화면 출력은 CLI, 중복 검증과 저장은 서비스가 담당합니다. / 오른쪽 계산/호출 결과를 name에 저장합니다. |
| [240](../주석코드/budget_app/cli.py#L240) | <code>                print(f&quot;[저장 완료] category={name}&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [241](../주석코드/budget_app/cli.py#L241) | <code>            else:</code> | 바로 앞 조건에 해당하지 않는 경우의 대체 처리 블록입니다. |
| [242](../주석코드/budget_app/cli.py#L242) | <code>                # 삭제할 카테고리 이름만 받고 실제 사용 여부 검사는 서비스에 맡깁니다.</code> | 설명 주석입니다. 삭제할 카테고리 이름만 받고 실제 사용 여부 검사는 서비스에 맡깁니다. (Python 실행에는 영향을 주지 않습니다.) |
| [243](../주석코드/budget_app/cli.py#L243) | <code>                name = input(&quot;삭제할 카테고리명: &quot;).strip()</code> | 삭제할 카테고리 이름만 받고 실제 사용 여부 검사는 서비스에 맡깁니다. / 오른쪽 계산/호출 결과를 name에 저장합니다. |
| [244](../주석코드/budget_app/cli.py#L244) | <code>                # 사용 중인 이름은 AppError가 발생하므로 삭제 완료를 출력하지 않습니다.</code> | 설명 주석입니다. 사용 중인 이름은 AppError가 발생하므로 삭제 완료를 출력하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [245](../주석코드/budget_app/cli.py#L245) | <code>                service.category_remove(name)</code> | 사용 중인 이름은 AppError가 발생하므로 삭제 완료를 출력하지 않습니다. / service.category_remove 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [246](../주석코드/budget_app/cli.py#L246) | <code>                print(f&quot;[삭제 완료] category={name}&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [247](../주석코드/budget_app/cli.py#L247) | <code>        # 예산 set은 저장, show는 조회로 분리합니다.</code> | 설명 주석입니다. 예산 set은 저장, show는 조회로 분리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [248](../주석코드/budget_app/cli.py#L248) | <code>        elif command == &quot;budget&quot;:</code> | 예산 set은 저장, show는 조회로 분리합니다. / 조건 command == &#x27;budget&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [249](../주석코드/budget_app/cli.py#L249) | <code>            if args.action == &quot;set&quot;:</code> | 조건 args.action == &#x27;set&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [250](../주석코드/budget_app/cli.py#L250) | <code>                # 월과 금액을 검증하고 예산 파일을 영구 저장합니다.</code> | 설명 주석입니다. 월과 금액을 검증하고 예산 파일을 영구 저장합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [251](../주석코드/budget_app/cli.py#L251) | <code>                service.set_budget(args.month, args.amount)</code> | 월과 금액을 검증하고 예산 파일을 영구 저장합니다. / service.set_budget 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [252](../주석코드/budget_app/cli.py#L252) | <code>                print(f&quot;[저장 완료] {args.month} 예산 {int(args.amount):,}원&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [253](../주석코드/budget_app/cli.py#L253) | <code>            else:</code> | 바로 앞 조건에 해당하지 않는 경우의 대체 처리 블록입니다. |
| [254](../주석코드/budget_app/cli.py#L254) | <code>                # 다른 계층의 모델·검증·저장 처리를 가져와 같은 로직을 재사용합니다.</code> | 설명 주석입니다. 다른 계층의 모델·검증·저장 처리를 가져와 같은 로직을 재사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [255](../주석코드/budget_app/cli.py#L255) | <code>                from .models import valid_month</code> | 다른 계층의 모델·검증·저장 처리를 가져와 같은 로직을 재사용합니다. / models에서 필요한 이름을 가져옵니다. |
| [256](../주석코드/budget_app/cli.py#L256) | <code>                # 조회에도 잘못된 월 표기를 허용하지 않습니다.</code> | 설명 주석입니다. 조회에도 잘못된 월 표기를 허용하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [257](../주석코드/budget_app/cli.py#L257) | <code>                if args.month is not None:</code> | 조회에도 잘못된 월 표기를 허용하지 않습니다. / 조건 args.month is not None가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [258](../주석코드/budget_app/cli.py#L258) | <code>                    valid_month(args.month)</code> | valid_month 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [259](../주석코드/budget_app/cli.py#L259) | <code>                budgets = service.budgets()</code> | 오른쪽 계산/호출 결과를 budgets에 저장합니다. |
| [260](../주석코드/budget_app/cli.py#L260) | <code>                # 월 미지정이면 전체, 지정이면 해당 월만 선택합니다.</code> | 설명 주석입니다. 월 미지정이면 전체, 지정이면 해당 월만 선택합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [261](../주석코드/budget_app/cli.py#L261) | <code>                selected = {m: a for m, a in sorted(budgets.items()) if args.month is None or m == args.month}</code> | 월 미지정이면 전체, 지정이면 해당 월만 선택합니다. / 오른쪽 계산/호출 결과를 selected에 저장합니다. |
| [262](../주석코드/budget_app/cli.py#L262) | <code>                for month, amount in selected.items():</code> | selected.items()에서 값을 하나씩 받아 (month, amount)에 넣고 블록을 반복합니다. |
| [263](../주석코드/budget_app/cli.py#L263) | <code>                    print(f&quot;{month}: {amount:,}원&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [264](../주석코드/budget_app/cli.py#L264) | <code>                # 설정되지 않은 예산을 0원 예산과 혼동하지 않도록 별도 문구를 표시합니다.</code> | 설명 주석입니다. 설정되지 않은 예산을 0원 예산과 혼동하지 않도록 별도 문구를 표시합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [265](../주석코드/budget_app/cli.py#L265) | <code>                if not selected:</code> | 설정되지 않은 예산을 0원 예산과 혼동하지 않도록 별도 문구를 표시합니다. / 조건 not selected가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [266](../주석코드/budget_app/cli.py#L266) | <code>                    print(&quot;설정된 예산 없음&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [267](../주석코드/budget_app/cli.py#L267) | <code>        # 집계는 Read에 해당합니다. 거래를 추가하거나 수정하지 않습니다.</code> | 설명 주석입니다. 집계는 Read에 해당합니다. 거래를 추가하거나 수정하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [268](../주석코드/budget_app/cli.py#L268) | <code>        elif command == &quot;summary&quot;:</code> | 집계는 Read에 해당합니다. 거래를 추가하거나 수정하지 않습니다. / 조건 command == &#x27;summary&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [269](../주석코드/budget_app/cli.py#L269) | <code>            # 표시할 순위 개수도 양수여야 합니다.</code> | 설명 주석입니다. 표시할 순위 개수도 양수여야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [270](../주석코드/budget_app/cli.py#L270) | <code>            top = positive(args.top)</code> | 표시할 순위 개수도 양수여야 합니다. / 오른쪽 계산/호출 결과를 top에 저장합니다. |
| [271](../주석코드/budget_app/cli.py#L271) | <code>            # 서비스는 합계 자료만 반환하며 아래 CLI 코드가 문구를 구성합니다.</code> | 설명 주석입니다. 서비스는 합계 자료만 반환하며 아래 CLI 코드가 문구를 구성합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [272](../주석코드/budget_app/cli.py#L272) | <code>            result = service.summary(args.month)</code> | 서비스는 합계 자료만 반환하며 아래 CLI 코드가 문구를 구성합니다. / 오른쪽 계산/호출 결과를 result에 저장합니다. |
| [273](../주석코드/budget_app/cli.py#L273) | <code>            # 잔액 계산에 쓸 두 합계를 꺼냅니다.</code> | 설명 주석입니다. 잔액 계산에 쓸 두 합계를 꺼냅니다. (Python 실행에는 영향을 주지 않습니다.) |
| [274](../주석코드/budget_app/cli.py#L274) | <code>            income, expense = result[&quot;income&quot;], result[&quot;expense&quot;]</code> | 잔액 계산에 쓸 두 합계를 꺼냅니다. / 오른쪽 계산/호출 결과를 (income, expense)에 저장합니다. |
| [275](../주석코드/budget_app/cli.py#L275) | <code>            # 거래가 없는 월도 명확히 안내한 뒤 0원 합계를 출력합니다.</code> | 설명 주석입니다. 거래가 없는 월도 명확히 안내한 뒤 0원 합계를 출력합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [276](../주석코드/budget_app/cli.py#L276) | <code>            if not result[&quot;count&quot;]:</code> | 거래가 없는 월도 명확히 안내한 뒤 0원 합계를 출력합니다. / 조건 not result[&#x27;count&#x27;]가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [277](../주석코드/budget_app/cli.py#L277) | <code>                print(&quot;데이터 없음&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [278](../주석코드/budget_app/cli.py#L278) | <code>            print(f&quot;총 수입: {income:,}원\n총 지출: {expense:,}원\n잔액: {income - expense:,}원&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [279](../주석코드/budget_app/cli.py#L279) | <code>            # 예산 None은 미설정입니다. 설정된 예산은 양수이므로 나눗셈이 가능합니다.</code> | 설명 주석입니다. 예산 None은 미설정입니다. 설정된 예산은 양수이므로 나눗셈이 가능합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [280](../주석코드/budget_app/cli.py#L280) | <code>            budget = result[&quot;budget&quot;]</code> | 예산 None은 미설정입니다. 설정된 예산은 양수이므로 나눗셈이 가능합니다. / 오른쪽 계산/호출 결과를 budget에 저장합니다. |
| [281](../주석코드/budget_app/cli.py#L281) | <code>            # 예산이 있을 때만 사용률을 출력합니다.</code> | 설명 주석입니다. 예산이 있을 때만 사용률을 출력합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [282](../주석코드/budget_app/cli.py#L282) | <code>            if budget is not None:</code> | 예산이 있을 때만 사용률을 출력합니다. / 조건 budget is not None가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [283](../주석코드/budget_app/cli.py#L283) | <code>                print(f&quot;예산: {budget:,}원 (사용률 {expense * 100 / budget:.1f}%)&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [284](../주석코드/budget_app/cli.py#L284) | <code>                # 예산과 같은 금액은 초과가 아닙니다. 큰 경우에만 경고합니다.</code> | 설명 주석입니다. 예산과 같은 금액은 초과가 아닙니다. 큰 경우에만 경고합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [285](../주석코드/budget_app/cli.py#L285) | <code>                if expense &gt; budget:</code> | 예산과 같은 금액은 초과가 아닙니다. 큰 경우에만 경고합니다. / 조건 expense &gt; budget가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [286](../주석코드/budget_app/cli.py#L286) | <code>                    print(f&quot;[경고] 예산 초과: {expense - budget:,}원&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [287](../주석코드/budget_app/cli.py#L287) | <code>            print(f&quot;지출 TOP {top}&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [288](../주석코드/budget_app/cli.py#L288) | <code>            # 정렬된 집계 결과 중 top개만 1부터 번호를 붙여 출력합니다.</code> | 설명 주석입니다. 정렬된 집계 결과 중 top개만 1부터 번호를 붙여 출력합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [289](../주석코드/budget_app/cli.py#L289) | <code>            for rank, (category, amount) in enumerate(result[&quot;categories&quot;][:top], 1):</code> | 정렬된 집계 결과 중 top개만 1부터 번호를 붙여 출력합니다. / enumerate(result[&#x27;categories&#x27;][:top], 1)에서 값을 하나씩 받아 (rank, (category, amount))에 넣고 블록을 반복합니다. |
| [290](../주석코드/budget_app/cli.py#L290) | <code>                print(f&quot;{rank}) {display(category)} {amount:,}원&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [291](../주석코드/budget_app/cli.py#L291) | <code>        # 일괄 Create: CSV 검증과 전체 반영/취소는 서비스가 담당합니다.</code> | 설명 주석입니다. 일괄 Create: CSV 검증과 전체 반영/취소는 서비스가 담당합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [292](../주석코드/budget_app/cli.py#L292) | <code>        elif command == &quot;import&quot;:</code> | 일괄 Create: CSV 검증과 전체 반영/취소는 서비스가 담당합니다. / 조건 command == &#x27;import&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [293](../주석코드/budget_app/cli.py#L293) | <code>            # 성공한 뒤에만 처리 건수를 받습니다. 오류가 나면 완료 문구를 출력하지 않습니다.</code> | 설명 주석입니다. 성공한 뒤에만 처리 건수를 받습니다. 오류가 나면 완료 문구를 출력하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [294](../주석코드/budget_app/cli.py#L294) | <code>            count = service.import_csv(Path(args.source))</code> | 성공한 뒤에만 처리 건수를 받습니다. 오류가 나면 완료 문구를 출력하지 않습니다. / 오른쪽 계산/호출 결과를 count에 저장합니다. |
| [295](../주석코드/budget_app/cli.py#L295) | <code>            print(f&quot;[완료] imported={count}, skipped=0&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [296](../주석코드/budget_app/cli.py#L296) | <code>        # 거래는 Read, 교환 파일은 쓰기 작업입니다. 저장 거래 자체는 바꾸지 않습니다.</code> | 설명 주석입니다. 거래는 Read, 교환 파일은 쓰기 작업입니다. 저장 거래 자체는 바꾸지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [297](../주석코드/budget_app/cli.py#L297) | <code>        elif command == &quot;export&quot;:</code> | 거래는 Read, 교환 파일은 쓰기 작업입니다. 저장 거래 자체는 바꾸지 않습니다. / 조건 command == &#x27;export&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [298](../주석코드/budget_app/cli.py#L298) | <code>            # 조건 검증과 출력 보호를 거친 CSV 내보내기를 요청합니다.</code> | 설명 주석입니다. 조건 검증과 출력 보호를 거친 CSV 내보내기를 요청합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [299](../주석코드/budget_app/cli.py#L299) | <code>            count = service.export_csv(Path(args.out), filters_from(args))</code> | 조건 검증과 출력 보호를 거친 CSV 내보내기를 요청합니다. / 오른쪽 계산/호출 결과를 count에 저장합니다. |
| [300](../주석코드/budget_app/cli.py#L300) | <code>            print(f&quot;[완료] {args.out} ({count} records)&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [301](../주석코드/budget_app/cli.py#L301) | <code>        # 백업 경로를 반환받아 사용자에게 보여줍니다.</code> | 설명 주석입니다. 백업 경로를 반환받아 사용자에게 보여줍니다. (Python 실행에는 영향을 주지 않습니다.) |
| [302](../주석코드/budget_app/cli.py#L302) | <code>        elif command == &quot;backup&quot;:</code> | 백업 경로를 반환받아 사용자에게 보여줍니다. / 조건 command == &#x27;backup&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [303](../주석코드/budget_app/cli.py#L303) | <code>            print(f&quot;[백업 완료] {service.backup()}&quot;)</code> | print 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [304](../주석코드/budget_app/cli.py#L304) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [305](../주석코드/budget_app/cli.py#L305) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [306](../주석코드/budget_app/cli.py#L306) | <code># 외부에서 호출하는 시작 함수입니다. 문법 해석과 로그 설정 후 종료 코드를 반환합니다.</code> | 설명 주석입니다. 외부에서 호출하는 시작 함수입니다. 문법 해석과 로그 설정 후 종료 코드를 반환합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [307](../주석코드/budget_app/cli.py#L307) | <code>def main(argv: list[str] &#124; None = None) -&gt; int:</code> | 외부에서 호출하는 시작 함수입니다. 문법 해석과 로그 설정 후 종료 코드를 반환합니다. / main 함수를 정의합니다. 인자: argv. 반환 타입: int. def 자체는 본문을 실행하지 않습니다. |
| [308](../주석코드/budget_app/cli.py#L308) | <code>    # argv=None이면 실제 터미널 인자를, 리스트이면 테스트에서 준 인자를 해석합니다.</code> | 설명 주석입니다. argv=None이면 실제 터미널 인자를, 리스트이면 테스트에서 준 인자를 해석합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [309](../주석코드/budget_app/cli.py#L309) | <code>    args = parser().parse_args(argv)</code> | argv=None이면 실제 터미널 인자를, 리스트이면 테스트에서 준 인자를 해석합니다. / 오른쪽 계산/호출 결과를 args에 저장합니다. |
| [310](../주석코드/budget_app/cli.py#L310) | <code>    # 사용자가 요청했을 때만 INFO 로그를 표시합니다.</code> | 설명 주석입니다. 사용자가 요청했을 때만 INFO 로그를 표시합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [311](../주석코드/budget_app/cli.py#L311) | <code>    if args.verbose:</code> | 사용자가 요청했을 때만 INFO 로그를 표시합니다. / 조건 args.verbose가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [312](../주석코드/budget_app/cli.py#L312) | <code>        logging.basicConfig(level=logging.INFO, format=&quot;[로그] %(message)s&quot;)</code> | logging.basicConfig 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [313](../주석코드/budget_app/cli.py#L313) | <code>    # 데코레이터가 반환한 종료 코드(int)를 __main__으로 전달합니다.</code> | 설명 주석입니다. 데코레이터가 반환한 종료 코드(int)를 __main__으로 전달합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [314](../주석코드/budget_app/cli.py#L314) | <code>    return execute(args)</code> | 데코레이터가 반환한 종료 코드(int)를 __main__으로 전달합니다. / 호출자에게 execute(args)을 반환하고 현재 함수 실행을 끝냅니다. |
