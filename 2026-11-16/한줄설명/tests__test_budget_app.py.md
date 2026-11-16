# tests/test_budget_app.py 한 줄씩 설명

대상: [주석 코드](../주석코드/tests/test_budget_app.py). 총 486줄입니다. 줄 번호는 이 사본과 일치합니다. 설명은 읽기 자료이며 실행할 명령이 아닙니다.

| 줄 | 실제 코드 | 설명 |
| ---: | --- | --- |
| [1](../주석코드/tests/test_budget_app.py#L1) | <code># 회귀 테스트: 기능과 실패 시 데이터 보존을 함께 확인합니다.</code> | 설명 주석입니다. 회귀 테스트: 기능과 실패 시 데이터 보존을 함께 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [2](../주석코드/tests/test_budget_app.py#L2) | <code># 모든 저장 작업은 TemporaryDirectory 안에서 하므로 실제 data에는 영향을 주지 않습니다.</code> | 설명 주석입니다. 모든 저장 작업은 TemporaryDirectory 안에서 하므로 실제 data에는 영향을 주지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [3](../주석코드/tests/test_budget_app.py#L3) | <code># assertEqual은 값 일치, assertRaises는 예상 오류 발생을 검사합니다.</code> | 설명 주석입니다. assertEqual은 값 일치, assertRaises는 예상 오류 발생을 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [4](../주석코드/tests/test_budget_app.py#L4) | <code># 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다.</code> | 설명 주석입니다. 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [5](../주석코드/tests/test_budget_app.py#L5) | <code>from __future__ import annotations</code> | 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다. / __future__에서 필요한 이름을 가져옵니다. |
| [6](../주석코드/tests/test_budget_app.py#L6) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [7](../주석코드/tests/test_budget_app.py#L7) | <code># 쉼표·인용·개행을 직접 나누지 않고 표준 CSV 규칙으로 처리합니다.</code> | 설명 주석입니다. 쉼표·인용·개행을 직접 나누지 않고 표준 CSV 규칙으로 처리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [8](../주석코드/tests/test_budget_app.py#L8) | <code>import csv</code> | 쉼표·인용·개행을 직접 나누지 않고 표준 CSV 규칙으로 처리합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [9](../주석코드/tests/test_budget_app.py#L9) | <code># 테스트에서 화면 출력을 파일 대신 메모리 문자열에 수집합니다.</code> | 설명 주석입니다. 테스트에서 화면 출력을 파일 대신 메모리 문자열에 수집합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [10](../주석코드/tests/test_budget_app.py#L10) | <code>import io</code> | 테스트에서 화면 출력을 파일 대신 메모리 문자열에 수집합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [11](../주석코드/tests/test_budget_app.py#L11) | <code># JSONL의 한 줄을 dict로 읽거나 JSON 문자열로 저장합니다.</code> | 설명 주석입니다. JSONL의 한 줄을 dict로 읽거나 JSON 문자열로 저장합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [12](../주석코드/tests/test_budget_app.py#L12) | <code>import json</code> | JSONL의 한 줄을 dict로 읽거나 JSON 문자열로 저장합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [13](../주석코드/tests/test_budget_app.py#L13) | <code># 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다.</code> | 설명 주석입니다. 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [14](../주석코드/tests/test_budget_app.py#L14) | <code>import os</code> | 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [15](../주석코드/tests/test_budget_app.py#L15) | <code># 실제 별도 Python 프로세스로 진입점과 종료 코드를 테스트합니다.</code> | 설명 주석입니다. 실제 별도 Python 프로세스로 진입점과 종료 코드를 테스트합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [16](../주석코드/tests/test_budget_app.py#L16) | <code>import subprocess</code> | 실제 별도 Python 프로세스로 진입점과 종료 코드를 테스트합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [17](../주석코드/tests/test_budget_app.py#L17) | <code># 오류 출력 스트림과 프로세스 실행 관련 정보를 사용합니다.</code> | 설명 주석입니다. 오류 출력 스트림과 프로세스 실행 관련 정보를 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [18](../주석코드/tests/test_budget_app.py#L18) | <code>import sys</code> | 오류 출력 스트림과 프로세스 실행 관련 정보를 사용합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [19](../주석코드/tests/test_budget_app.py#L19) | <code># 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다.</code> | 설명 주석입니다. 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [20](../주석코드/tests/test_budget_app.py#L20) | <code>import tempfile</code> | 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [21](../주석코드/tests/test_budget_app.py#L21) | <code># 표준 라이브러리 테스트 실행기와 검증 메서드를 사용합니다.</code> | 설명 주석입니다. 표준 라이브러리 테스트 실행기와 검증 메서드를 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [22](../주석코드/tests/test_budget_app.py#L22) | <code>import unittest</code> | 표준 라이브러리 테스트 실행기와 검증 메서드를 사용합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [23](../주석코드/tests/test_budget_app.py#L23) | <code># 세 저장 파일의 ZIP 백업을 만들거나 테스트에서 검사합니다.</code> | 설명 주석입니다. 세 저장 파일의 ZIP 백업을 만들거나 테스트에서 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [24](../주석코드/tests/test_budget_app.py#L24) | <code>import zipfile</code> | 세 저장 파일의 ZIP 백업을 만들거나 테스트에서 검사합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [25](../주석코드/tests/test_budget_app.py#L25) | <code># 테스트 중 정상 출력과 오류 출력을 각각 수집합니다.</code> | 설명 주석입니다. 테스트 중 정상 출력과 오류 출력을 각각 수집합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [26](../주석코드/tests/test_budget_app.py#L26) | <code>from contextlib import redirect_stderr, redirect_stdout</code> | 테스트 중 정상 출력과 오류 출력을 각각 수집합니다. / contextlib에서 필요한 이름을 가져옵니다. |
| [27](../주석코드/tests/test_budget_app.py#L27) | <code># 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다.</code> | 설명 주석입니다. 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [28](../주석코드/tests/test_budget_app.py#L28) | <code>from pathlib import Path</code> | 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다. / pathlib에서 필요한 이름을 가져옵니다. |
| [29](../주석코드/tests/test_budget_app.py#L29) | <code># 사용자 입력이나 파일 교체 실패를 테스트에서 통제합니다.</code> | 설명 주석입니다. 사용자 입력이나 파일 교체 실패를 테스트에서 통제합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [30](../주석코드/tests/test_budget_app.py#L30) | <code>from unittest.mock import patch</code> | 사용자 입력이나 파일 교체 실패를 테스트에서 통제합니다. / unittest.mock에서 필요한 이름을 가져옵니다. |
| [31](../주석코드/tests/test_budget_app.py#L31) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [32](../주석코드/tests/test_budget_app.py#L32) | <code># CLI의 main 함수를 모듈 실행 진입점에 연결합니다.</code> | 설명 주석입니다. CLI의 main 함수를 모듈 실행 진입점에 연결합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [33](../주석코드/tests/test_budget_app.py#L33) | <code>from budget_app.cli import main</code> | CLI의 main 함수를 모듈 실행 진입점에 연결합니다. / budget_app.cli에서 필요한 이름을 가져옵니다. |
| [34](../주석코드/tests/test_budget_app.py#L34) | <code># 테스트에서 모델 검증 함수와 예상 오류를 직접 확인합니다.</code> | 설명 주석입니다. 테스트에서 모델 검증 함수와 예상 오류를 직접 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [35](../주석코드/tests/test_budget_app.py#L35) | <code>from budget_app.models import AppError, Transaction, positive, valid_date</code> | 테스트에서 모델 검증 함수와 예상 오류를 직접 확인합니다. / budget_app.models에서 필요한 이름을 가져옵니다. |
| [36](../주석코드/tests/test_budget_app.py#L36) | <code># CLI 또는 테스트가 서비스 업무 규칙과 검색 조건 객체를 사용합니다.</code> | 설명 주석입니다. CLI 또는 테스트가 서비스 업무 규칙과 검색 조건 객체를 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [37](../주석코드/tests/test_budget_app.py#L37) | <code>from budget_app.service import BudgetService, Filters</code> | CLI 또는 테스트가 서비스 업무 규칙과 검색 조건 객체를 사용합니다. / budget_app.service에서 필요한 이름을 가져옵니다. |
| [38](../주석코드/tests/test_budget_app.py#L38) | <code># 테스트 데이터 초기화와 손상 시나리오를 구성하는 저장 도우미입니다.</code> | 설명 주석입니다. 테스트 데이터 초기화와 손상 시나리오를 구성하는 저장 도우미입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [39](../주석코드/tests/test_budget_app.py#L39) | <code>from budget_app.storage import DataStore, read_jsonl, write_jsonl</code> | 테스트 데이터 초기화와 손상 시나리오를 구성하는 저장 도우미입니다. / budget_app.storage에서 필요한 이름을 가져옵니다. |
| [40](../주석코드/tests/test_budget_app.py#L40) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [41](../주석코드/tests/test_budget_app.py#L41) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [42](../주석코드/tests/test_budget_app.py#L42) | <code># unittest가 test_로 시작하는 30개 메서드를 찾아 각각 독립된 데이터로 검증합니다.</code> | 설명 주석입니다. unittest가 test_로 시작하는 30개 메서드를 찾아 각각 독립된 데이터로 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [43](../주석코드/tests/test_budget_app.py#L43) | <code>class BudgetTests(unittest.TestCase):</code> | unittest가 test_로 시작하는 30개 메서드를 찾아 각각 독립된 데이터로 검증합니다. / BudgetTests 클래스의 정의를 시작합니다. 들여쓴 메서드와 속성이 이 클래스에 속합니다. |
| [44](../주석코드/tests/test_budget_app.py#L44) | <code>    # 각 테스트 전에 임시 데이터 폴더를 만들고 초기 파일 및 서비스를 준비합니다.</code> | 설명 주석입니다. 각 테스트 전에 임시 데이터 폴더를 만들고 초기 파일 및 서비스를 준비합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [45](../주석코드/tests/test_budget_app.py#L45) | <code>    def setUp(self) -&gt; None:</code> | 각 테스트 전에 임시 데이터 폴더를 만들고 초기 파일 및 서비스를 준비합니다. / setUp 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [46](../주석코드/tests/test_budget_app.py#L46) | <code>        self.temporary = tempfile.TemporaryDirectory()</code> | 오른쪽 계산/호출 결과를 self.temporary에 저장합니다. |
| [47](../주석코드/tests/test_budget_app.py#L47) | <code>        self.addCleanup(self.temporary.cleanup)</code> | self.addCleanup 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [48](../주석코드/tests/test_budget_app.py#L48) | <code>        self.root = Path(self.temporary.name)</code> | 오른쪽 계산/호출 결과를 self.root에 저장합니다. |
| [49](../주석코드/tests/test_budget_app.py#L49) | <code>        self.store = DataStore(self.root / &quot;data&quot;)</code> | 오른쪽 계산/호출 결과를 self.store에 저장합니다. |
| [50](../주석코드/tests/test_budget_app.py#L50) | <code>        with self.store.session():</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [51](../주석코드/tests/test_budget_app.py#L51) | <code>            pass</code> | 이 블록에서는 별도 동작을 하지 않습니다. 제너레이터 검증 순회나 초기화용 with 진입만 필요할 때 사용합니다. |
| [52](../주석코드/tests/test_budget_app.py#L52) | <code>        self.service = BudgetService(self.store)</code> | 오른쪽 계산/호출 결과를 self.service에 저장합니다. |
| [53](../주석코드/tests/test_budget_app.py#L53) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [54](../주석코드/tests/test_budget_app.py#L54) | <code>    # 테스트에 필요한 유효한 거래를 만드는 공통 도우미입니다.</code> | 설명 주석입니다. 테스트에 필요한 유효한 거래를 만드는 공통 도우미입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [55](../주석코드/tests/test_budget_app.py#L55) | <code>    def transaction(self, day: str = &quot;2024-01-15&quot;, amount: int = 15000,</code> | 테스트에 필요한 유효한 거래를 만드는 공통 도우미입니다. / transaction 함수를 정의합니다. 인자: self, day, amount, category, type. 반환 타입: Transaction. def 자체는 본문을 실행하지 않습니다. |
| [56](../주석코드/tests/test_budget_app.py#L56) | <code>                    category: str = &quot;food&quot;, type: str = &quot;expense&quot;, **kwargs: str) -&gt; Transaction:</code> | 55행에서 시작한 FunctionDef 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [57](../주석코드/tests/test_budget_app.py#L57) | <code>        return Transaction.create(date=day, amount=amount, category=category, type=type, **kwargs)</code> | 호출자에게 Transaction.create(date=day, amount=amount, category=category, type=type, **kwargs)을 반환하고 현재 함수 실행을 끝냅니다. |
| [58](../주석코드/tests/test_budget_app.py#L58) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [59](../주석코드/tests/test_budget_app.py#L59) | <code>    # 실제 키보드 대신 입력 목록을 제공하고 종료 코드·표준 출력·오류 출력을 수집합니다.</code> | 설명 주석입니다. 실제 키보드 대신 입력 목록을 제공하고 종료 코드·표준 출력·오류 출력을 수집합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [60](../주석코드/tests/test_budget_app.py#L60) | <code>    def run_cli(self, *args: str, inputs: list[str] &#124; None = None) -&gt; tuple[int, str, str]:</code> | 실제 키보드 대신 입력 목록을 제공하고 종료 코드·표준 출력·오류 출력을 수집합니다. / run_cli 함수를 정의합니다. 인자: self, inputs. 반환 타입: tuple[int, str, str]. def 자체는 본문을 실행하지 않습니다. |
| [61](../주석코드/tests/test_budget_app.py#L61) | <code>        out, err = io.StringIO(), io.StringIO()</code> | 오른쪽 계산/호출 결과를 (out, err)에 저장합니다. |
| [62](../주석코드/tests/test_budget_app.py#L62) | <code>        with redirect_stdout(out), redirect_stderr(err), patch(&quot;builtins.input&quot;, side_effect=inputs or []):</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [63](../주석코드/tests/test_budget_app.py#L63) | <code>            code = main([&quot;--data-dir&quot;, str(self.store.directory), *args])</code> | 오른쪽 계산/호출 결과를 code에 저장합니다. |
| [64](../주석코드/tests/test_budget_app.py#L64) | <code>        return code, out.getvalue(), err.getvalue()</code> | 호출자에게 (code, out.getvalue(), err.getvalue())을 반환하고 현재 함수 실행을 끝냅니다. |
| [65](../주석코드/tests/test_budget_app.py#L65) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [66](../주석코드/tests/test_budget_app.py#L66) | <code>    # 검증할 CSV를 임시 폴더에 만들어 경로를 반환하는 도우미입니다.</code> | 설명 주석입니다. 검증할 CSV를 임시 폴더에 만들어 경로를 반환하는 도우미입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [67](../주석코드/tests/test_budget_app.py#L67) | <code>    def csv_file(self, rows: list[list[str]], header: tuple[str, ...] = (&quot;date&quot;, &quot;type&quot;, &quot;category&quot;, &quot;amount&quot;, &quot;memo&quot;, &quot;tags&quot;)) -&gt; Path:</code> | 검증할 CSV를 임시 폴더에 만들어 경로를 반환하는 도우미입니다. / csv_file 함수를 정의합니다. 인자: self, rows, header. 반환 타입: Path. def 자체는 본문을 실행하지 않습니다. |
| [68](../주석코드/tests/test_budget_app.py#L68) | <code>        path = self.root / &quot;input.csv&quot;</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [69](../주석코드/tests/test_budget_app.py#L69) | <code>        with path.open(&quot;w&quot;, encoding=&quot;utf-8&quot;, newline=&quot;&quot;) as stream:</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [70](../주석코드/tests/test_budget_app.py#L70) | <code>            writer = csv.writer(stream)</code> | 오른쪽 계산/호출 결과를 writer에 저장합니다. |
| [71](../주석코드/tests/test_budget_app.py#L71) | <code>            writer.writerow(header)</code> | writer.writerow 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [72](../주석코드/tests/test_budget_app.py#L72) | <code>            writer.writerows(rows)</code> | writer.writerows 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [73](../주석코드/tests/test_budget_app.py#L73) | <code>        return path</code> | 호출자에게 path을 반환하고 현재 함수 실행을 끝냅니다. |
| [74](../주석코드/tests/test_budget_app.py#L74) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [75](../주석코드/tests/test_budget_app.py#L75) | <code>    # 초기화가 세 저장 파일과 기본 카테고리를 만드는지 검증합니다.</code> | 설명 주석입니다. 초기화가 세 저장 파일과 기본 카테고리를 만드는지 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [76](../주석코드/tests/test_budget_app.py#L76) | <code>    def test_initialization_creates_three_files_and_defaults(self) -&gt; None:</code> | 초기화가 세 저장 파일과 기본 카테고리를 만드는지 검증합니다. / test_initialization_creates_three_files_and_defaults 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [77](../주석코드/tests/test_budget_app.py#L77) | <code>        for name in self.store.FILES:</code> | self.store.FILES에서 값을 하나씩 받아 name에 넣고 블록을 반복합니다. |
| [78](../주석코드/tests/test_budget_app.py#L78) | <code>            # 필요한 저장 파일이 실제로 생성되었는지 확인합니다.</code> | 설명 주석입니다. 필요한 저장 파일이 실제로 생성되었는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [79](../주석코드/tests/test_budget_app.py#L79) | <code>            self.assertTrue((self.store.directory / name).exists())</code> | 필요한 저장 파일이 실제로 생성되었는지 확인합니다. / 테스트 검증 메서드 self.assertTrue를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [80](../주석코드/tests/test_budget_app.py#L80) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [81](../주석코드/tests/test_budget_app.py#L81) | <code>        self.assertIn(&quot;food&quot;, self.service.categories())</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [82](../주석코드/tests/test_budget_app.py#L82) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [83](../주석코드/tests/test_budget_app.py#L83) | <code>    # 0바이트 카테고리 파일에 기본 이름이 재생성되는 정책을 확인합니다.</code> | 설명 주석입니다. 0바이트 카테고리 파일에 기본 이름이 재생성되는 정책을 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [84](../주석코드/tests/test_budget_app.py#L84) | <code>    def test_empty_categories_reinitialized(self) -&gt; None:</code> | 0바이트 카테고리 파일에 기본 이름이 재생성되는 정책을 확인합니다. / test_empty_categories_reinitialized 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [85](../주석코드/tests/test_budget_app.py#L85) | <code>        self.store.path(&quot;categories&quot;).write_text(&quot;&quot;, encoding=&quot;utf-8&quot;)</code> | self.store.path(&#x27;categories&#x27;).write_text 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [86](../주석코드/tests/test_budget_app.py#L86) | <code>        with self.store.session():</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [87](../주석코드/tests/test_budget_app.py#L87) | <code>            # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [88](../주석코드/tests/test_budget_app.py#L88) | <code>            self.assertIn(&quot;salary&quot;, self.service.categories())</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [89](../주석코드/tests/test_budget_app.py#L89) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [90](../주석코드/tests/test_budget_app.py#L90) | <code>    # 잘못된 날짜·윤년·금액 범위·bool·과도한 길이 입력을 검증합니다.</code> | 설명 주석입니다. 잘못된 날짜·윤년·금액 범위·bool·과도한 길이 입력을 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [91](../주석코드/tests/test_budget_app.py#L91) | <code>    def test_invalid_dates_and_amounts(self) -&gt; None:</code> | 잘못된 날짜·윤년·금액 범위·bool·과도한 길이 입력을 검증합니다. / test_invalid_dates_and_amounts 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [92](../주석코드/tests/test_budget_app.py#L92) | <code>        for value in (&quot;2024-02-30&quot;, &quot;2024-1-01&quot;, &quot;0000-01-01&quot;, &quot;2024-13-01&quot;):</code> | (&#x27;2024-02-30&#x27;, &#x27;2024-1-01&#x27;, &#x27;0000-01-01&#x27;, &#x27;2024-13-01&#x27;)에서 값을 하나씩 받아 value에 넣고 블록을 반복합니다. |
| [93](../주석코드/tests/test_budget_app.py#L93) | <code>            with self.subTest(value=value), self.assertRaises(AppError):</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [94](../주석코드/tests/test_budget_app.py#L94) | <code>                valid_date(value)</code> | valid_date 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [95](../주석코드/tests/test_budget_app.py#L95) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [96](../주석코드/tests/test_budget_app.py#L96) | <code>        self.assertEqual(valid_date(&quot;2024-02-29&quot;), &quot;2024-02-29&quot;)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [97](../주석코드/tests/test_budget_app.py#L97) | <code>        for value in (0, -1, True, &quot;1.5&quot;, &quot;x&quot;, &quot;9&quot; * 5000, 9223372036854775808):</code> | (0, -1, True, &#x27;1.5&#x27;, &#x27;x&#x27;, &#x27;9&#x27; * 5000, 9223372036854775808)에서 값을 하나씩 받아 value에 넣고 블록을 반복합니다. |
| [98](../주석코드/tests/test_budget_app.py#L98) | <code>            with self.subTest(value=str(value)[:20]), self.assertRaises(AppError):</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [99](../주석코드/tests/test_budget_app.py#L99) | <code>                positive(value)</code> | positive 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [100](../주석코드/tests/test_budget_app.py#L100) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [101](../주석코드/tests/test_budget_app.py#L101) | <code>    # C/R: 추가 후 고유 id, 제너레이터 및 최신순 영구 저장을 확인합니다.</code> | 설명 주석입니다. C/R: 추가 후 고유 id, 제너레이터 및 최신순 영구 저장을 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [102](../주석코드/tests/test_budget_app.py#L102) | <code>    def test_add_persists_and_streams_in_date_order(self) -&gt; None:</code> | C/R: 추가 후 고유 id, 제너레이터 및 최신순 영구 저장을 확인합니다. / test_add_persists_and_streams_in_date_order 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [103](../주석코드/tests/test_budget_app.py#L103) | <code>        for day in (&quot;2024-01-15&quot;, &quot;2024-02-01&quot;, &quot;2024-01-01&quot;, &quot;2024-01-15&quot;):</code> | (&#x27;2024-01-15&#x27;, &#x27;2024-02-01&#x27;, &#x27;2024-01-01&#x27;, &#x27;2024-01-15&#x27;)에서 값을 하나씩 받아 day에 넣고 블록을 반복합니다. |
| [104](../주석코드/tests/test_budget_app.py#L104) | <code>            self.service.add(self.transaction(day))</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [105](../주석코드/tests/test_budget_app.py#L105) | <code>        iterator = self.service.transactions.iter_all()</code> | 오른쪽 계산/호출 결과를 iterator에 저장합니다. |
| [106](../주석코드/tests/test_budget_app.py#L106) | <code>        # 같은 이터레이터 객체인지 비교해 반복자가 그대로 사용되는지 검사합니다.</code> | 설명 주석입니다. 같은 이터레이터 객체인지 비교해 반복자가 그대로 사용되는지 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [107](../주석코드/tests/test_budget_app.py#L107) | <code>        self.assertIs(iter(iterator), iterator)</code> | 같은 이터레이터 객체인지 비교해 반복자가 그대로 사용되는지 검사합니다. / 테스트 검증 메서드 self.assertIs를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [108](../주석코드/tests/test_budget_app.py#L108) | <code>        keys = [t.key for t in iterator]</code> | 오른쪽 계산/호출 결과를 keys에 저장합니다. |
| [109](../주석코드/tests/test_budget_app.py#L109) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [110](../주석코드/tests/test_budget_app.py#L110) | <code>        self.assertEqual(keys, sorted(keys, reverse=True))</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [111](../주석코드/tests/test_budget_app.py#L111) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [112](../주석코드/tests/test_budget_app.py#L112) | <code>        self.assertEqual(len({t.id for t in BudgetService(self.store).transactions.iter_all()}), 4)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [113](../주석코드/tests/test_budget_app.py#L113) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [114](../주석코드/tests/test_budget_app.py#L114) | <code>    # 유효하지 않은 카테고리·타입이 원본 파일을 바꾸지 않는지 확인합니다.</code> | 설명 주석입니다. 유효하지 않은 카테고리·타입이 원본 파일을 바꾸지 않는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [115](../주석코드/tests/test_budget_app.py#L115) | <code>    def test_invalid_category_and_type_do_not_write(self) -&gt; None:</code> | 유효하지 않은 카테고리·타입이 원본 파일을 바꾸지 않는지 확인합니다. / test_invalid_category_and_type_do_not_write 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [116](../주석코드/tests/test_budget_app.py#L116) | <code>        # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.</code> | 설명 주석입니다. 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [117](../주석코드/tests/test_budget_app.py#L117) | <code>        before = self.store.path(&quot;transactions&quot;).read_bytes()</code> | 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. / 오른쪽 계산/호출 결과를 before에 저장합니다. |
| [118](../주석코드/tests/test_budget_app.py#L118) | <code>        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [119](../주석코드/tests/test_budget_app.py#L119) | <code>        with self.assertRaises(AppError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [120](../주석코드/tests/test_budget_app.py#L120) | <code>            self.service.add(self.transaction(category=&quot;unknown&quot;))</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [121](../주석코드/tests/test_budget_app.py#L121) | <code>        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [122](../주석코드/tests/test_budget_app.py#L122) | <code>        with self.assertRaises(AppError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [123](../주석코드/tests/test_budget_app.py#L123) | <code>            self.transaction(type=&quot;other&quot;)</code> | self.transaction 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [124](../주석코드/tests/test_budget_app.py#L124) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [125](../주석코드/tests/test_budget_app.py#L125) | <code>        self.assertEqual(before, self.store.path(&quot;transactions&quot;).read_bytes())</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [126](../주석코드/tests/test_budget_app.py#L126) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [127](../주석코드/tests/test_budget_app.py#L127) | <code>    # U: 날짜 변경 시 순서 재배치와 메모·태그 비우기를 확인합니다.</code> | 설명 주석입니다. U: 날짜 변경 시 순서 재배치와 메모·태그 비우기를 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [128](../주석코드/tests/test_budget_app.py#L128) | <code>    def test_update_reorders_and_clears_optional_fields(self) -&gt; None:</code> | U: 날짜 변경 시 순서 재배치와 메모·태그 비우기를 확인합니다. / test_update_reorders_and_clears_optional_fields 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [129](../주석코드/tests/test_budget_app.py#L129) | <code>        transaction = self.transaction(memo=&quot;old&quot;, tags=&quot;a,b&quot;)</code> | 오른쪽 계산/호출 결과를 transaction에 저장합니다. |
| [130](../주석코드/tests/test_budget_app.py#L130) | <code>        self.service.add(transaction)</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [131](../주석코드/tests/test_budget_app.py#L131) | <code>        self.service.add(self.transaction(&quot;2024-02-01&quot;))</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [132](../주석코드/tests/test_budget_app.py#L132) | <code>        self.service.update(transaction.id, {&quot;date&quot;: &quot;2024-03-01&quot;, &quot;amount&quot;: &quot;12&quot;, &quot;memo&quot;: &quot;&quot;, &quot;tags&quot;: &quot;&quot;})</code> | self.service.update 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [133](../주석코드/tests/test_budget_app.py#L133) | <code>        first = next(self.service.transactions.iter_all())</code> | 오른쪽 계산/호출 결과를 first에 저장합니다. |
| [134](../주석코드/tests/test_budget_app.py#L134) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [135](../주석코드/tests/test_budget_app.py#L135) | <code>        self.assertEqual((first.id, first.amount, first.memo, first.tags), (transaction.id, 12, &quot;&quot;, ()))</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [136](../주석코드/tests/test_budget_app.py#L136) | <code>        self.service.update(transaction.id, {&quot;date&quot;: &quot;2023-01-01&quot;})</code> | self.service.update 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [137](../주석코드/tests/test_budget_app.py#L137) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [138](../주석코드/tests/test_budget_app.py#L138) | <code>        self.assertEqual(list(self.service.transactions.iter_all())[-1].id, transaction.id)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [139](../주석코드/tests/test_budget_app.py#L139) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [140](../주석코드/tests/test_budget_app.py#L140) | <code>    # D: 삭제 성공 및 없는 id의 삭제·수정 거부를 검증합니다.</code> | 설명 주석입니다. D: 삭제 성공 및 없는 id의 삭제·수정 거부를 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [141](../주석코드/tests/test_budget_app.py#L141) | <code>    def test_delete_and_missing_id(self) -&gt; None:</code> | D: 삭제 성공 및 없는 id의 삭제·수정 거부를 검증합니다. / test_delete_and_missing_id 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [142](../주석코드/tests/test_budget_app.py#L142) | <code>        transaction = self.transaction()</code> | 오른쪽 계산/호출 결과를 transaction에 저장합니다. |
| [143](../주석코드/tests/test_budget_app.py#L143) | <code>        self.service.add(transaction)</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [144](../주석코드/tests/test_budget_app.py#L144) | <code>        self.service.delete(transaction.id)</code> | self.service.delete 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [145](../주석코드/tests/test_budget_app.py#L145) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [146](../주석코드/tests/test_budget_app.py#L146) | <code>        self.assertEqual(list(self.service.transactions.iter_all()), [])</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [147](../주석코드/tests/test_budget_app.py#L147) | <code>        for method in (lambda: self.service.delete(&quot;missing&quot;), lambda: self.service.update(&quot;missing&quot;, {&quot;memo&quot;: &quot;x&quot;})):</code> | (lambda: self.service.delete(&#x27;missing&#x27;), lambda: self.service.update(&#x27;missing&#x27;, {&#x27;memo&#x27;: &#x27;x&#x27;}))에서 값을 하나씩 받아 method에 넣고 블록을 반복합니다. |
| [148](../주석코드/tests/test_budget_app.py#L148) | <code>            # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [149](../주석코드/tests/test_budget_app.py#L149) | <code>            with self.assertRaisesRegex(AppError, &quot;없는 데이터&quot;):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [150](../주석코드/tests/test_budget_app.py#L150) | <code>                method()</code> | method 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [151](../주석코드/tests/test_budget_app.py#L151) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [152](../주석코드/tests/test_budget_app.py#L152) | <code>    # 잘못된 수정 요청 전후 파일 바이트를 비교해 원본 보존을 확인합니다.</code> | 설명 주석입니다. 잘못된 수정 요청 전후 파일 바이트를 비교해 원본 보존을 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [153](../주석코드/tests/test_budget_app.py#L153) | <code>    def test_failed_update_preserves_bytes(self) -&gt; None:</code> | 잘못된 수정 요청 전후 파일 바이트를 비교해 원본 보존을 확인합니다. / test_failed_update_preserves_bytes 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [154](../주석코드/tests/test_budget_app.py#L154) | <code>        transaction = self.transaction()</code> | 오른쪽 계산/호출 결과를 transaction에 저장합니다. |
| [155](../주석코드/tests/test_budget_app.py#L155) | <code>        self.service.add(transaction)</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [156](../주석코드/tests/test_budget_app.py#L156) | <code>        # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.</code> | 설명 주석입니다. 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [157](../주석코드/tests/test_budget_app.py#L157) | <code>        before = self.store.path(&quot;transactions&quot;).read_bytes()</code> | 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. / 오른쪽 계산/호출 결과를 before에 저장합니다. |
| [158](../주석코드/tests/test_budget_app.py#L158) | <code>        for changes in ({&quot;amount&quot;: &quot;0&quot;}, {&quot;date&quot;: &quot;wrong&quot;}, {&quot;category&quot;: &quot;missing&quot;}, {}):</code> | ({&#x27;amount&#x27;: &#x27;0&#x27;}, {&#x27;date&#x27;: &#x27;wrong&#x27;}, {&#x27;category&#x27;: &#x27;missing&#x27;}, {})에서 값을 하나씩 받아 changes에 넣고 블록을 반복합니다. |
| [159](../주석코드/tests/test_budget_app.py#L159) | <code>            with self.subTest(changes=changes), self.assertRaises(AppError):</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [160](../주석코드/tests/test_budget_app.py#L160) | <code>                self.service.update(transaction.id, changes)</code> | self.service.update 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [161](../주석코드/tests/test_budget_app.py#L161) | <code>            # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [162](../주석코드/tests/test_budget_app.py#L162) | <code>            self.assertEqual(before, self.store.path(&quot;transactions&quot;).read_bytes())</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [163](../주석코드/tests/test_budget_app.py#L163) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [164](../주석코드/tests/test_budget_app.py#L164) | <code>    # 날짜 경계 포함, AND 검색, 태그 중복 제거와 완전 일치를 확인합니다.</code> | 설명 주석입니다. 날짜 경계 포함, AND 검색, 태그 중복 제거와 완전 일치를 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [165](../주석코드/tests/test_budget_app.py#L165) | <code>    def test_search_combines_all_conditions_inclusively(self) -&gt; None:</code> | 날짜 경계 포함, AND 검색, 태그 중복 제거와 완전 일치를 확인합니다. / test_search_combines_all_conditions_inclusively 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [166](../주석코드/tests/test_budget_app.py#L166) | <code>        selected = self.transaction(memo=&quot;Lunch MEAL&quot;, tags=&quot;work,meal,work&quot;)</code> | 오른쪽 계산/호출 결과를 selected에 저장합니다. |
| [167](../주석코드/tests/test_budget_app.py#L167) | <code>        self.service.add(selected)</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [168](../주석코드/tests/test_budget_app.py#L168) | <code>        self.service.add(self.transaction(&quot;2024-01-16&quot;, memo=&quot;meal&quot;, tags=&quot;meal&quot;))</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [169](../주석코드/tests/test_budget_app.py#L169) | <code>        filters = Filters(start=&quot;2024-01-15&quot;, end=&quot;2024-01-15&quot;, type=&quot;expense&quot;, category=&quot;food&quot;, q=&quot;meal&quot;, tag=&quot;work&quot;)</code> | 오른쪽 계산/호출 결과를 filters에 저장합니다. |
| [170](../주석코드/tests/test_budget_app.py#L170) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [171](../주석코드/tests/test_budget_app.py#L171) | <code>        self.assertEqual(list(self.service.search(filters)), [selected])</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [172](../주석코드/tests/test_budget_app.py#L172) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [173](../주석코드/tests/test_budget_app.py#L173) | <code>        self.assertEqual(selected.tags, (&quot;work&quot;, &quot;meal&quot;))</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [174](../주석코드/tests/test_budget_app.py#L174) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [175](../주석코드/tests/test_budget_app.py#L175) | <code>        self.assertEqual(list(self.service.search(Filters(tag=&quot;wor&quot;))), [])</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [176](../주석코드/tests/test_budget_app.py#L176) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [177](../주석코드/tests/test_budget_app.py#L177) | <code>    # 역전된 기간·없는 월·월과 범위의 충돌을 거부하는지 확인합니다.</code> | 설명 주석입니다. 역전된 기간·없는 월·월과 범위의 충돌을 거부하는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [178](../주석코드/tests/test_budget_app.py#L178) | <code>    def test_invalid_filters(self) -&gt; None:</code> | 역전된 기간·없는 월·월과 범위의 충돌을 거부하는지 확인합니다. / test_invalid_filters 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [179](../주석코드/tests/test_budget_app.py#L179) | <code>        for args in ({&quot;start&quot;: &quot;2024-03-01&quot;, &quot;end&quot;: &quot;2024-01-01&quot;}, {&quot;month&quot;: &quot;2024-13&quot;},</code> | ({&#x27;start&#x27;: &#x27;2024-03-01&#x27;, &#x27;end&#x27;: &#x27;2024-01-01&#x27;}, {&#x27;month&#x27;: &#x27;2024-13&#x27;}, {&#x27;month&#x27;: &#x27;2024-01&#x27;, &#x27;start&#x27;: &#x27;2024-01-01&#x27;})에서 값을 하나씩 받아 args에 넣고 블록을 반복합니다. |
| [180](../주석코드/tests/test_budget_app.py#L180) | <code>                     {&quot;month&quot;: &quot;2024-01&quot;, &quot;start&quot;: &quot;2024-01-01&quot;}):</code> | 179행에서 시작한 For 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [181](../주석코드/tests/test_budget_app.py#L181) | <code>            with self.subTest(args=args), self.assertRaises(AppError):</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [182](../주석코드/tests/test_budget_app.py#L182) | <code>                Filters(**args)</code> | Filters 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [183](../주석코드/tests/test_budget_app.py#L183) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [184](../주석코드/tests/test_budget_app.py#L184) | <code>    # 해당 월만 합산하고 TOP 제한·예산 사용률·초과 경고가 맞는지 검증합니다.</code> | 설명 주석입니다. 해당 월만 합산하고 TOP 제한·예산 사용률·초과 경고가 맞는지 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [185](../주석코드/tests/test_budget_app.py#L185) | <code>    def test_summary_budget_and_warning(self) -&gt; None:</code> | 해당 월만 합산하고 TOP 제한·예산 사용률·초과 경고가 맞는지 검증합니다. / test_summary_budget_and_warning 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [186](../주석코드/tests/test_budget_app.py#L186) | <code>        for transaction in (self.transaction(amount=100), self.transaction(amount=200, category=&quot;rent&quot;),</code> | (self.transaction(amount=100), self.transaction(amount=200, category=&#x27;rent&#x27;), self.transaction(amount=1000, category=&#x27;salary&#x27;, type=&#x27;income&#x27;), self.transaction(&#x27;2024-02-01&#x27;))에서 값을 하나씩 받아 transaction에 넣고 블록을 반복합니다. |
| [187](../주석코드/tests/test_budget_app.py#L187) | <code>                            self.transaction(amount=1000, category=&quot;salary&quot;, type=&quot;income&quot;), self.transaction(&quot;2024-02-01&quot;)):</code> | 186행에서 시작한 For 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [188](../주석코드/tests/test_budget_app.py#L188) | <code>            self.service.add(transaction)</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [189](../주석코드/tests/test_budget_app.py#L189) | <code>        self.service.set_budget(&quot;2024-01&quot;, &quot;250&quot;)</code> | self.service.set_budget 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [190](../주석코드/tests/test_budget_app.py#L190) | <code>        result = self.service.summary(&quot;2024-01&quot;)</code> | 오른쪽 계산/호출 결과를 result에 저장합니다. |
| [191](../주석코드/tests/test_budget_app.py#L191) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [192](../주석코드/tests/test_budget_app.py#L192) | <code>        self.assertEqual((result[&quot;income&quot;], result[&quot;expense&quot;], result[&quot;budget&quot;]), (1000, 300, 250))</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [193](../주석코드/tests/test_budget_app.py#L193) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [194](../주석코드/tests/test_budget_app.py#L194) | <code>        self.assertEqual(result[&quot;categories&quot;], [(&quot;rent&quot;, 200), (&quot;food&quot;, 100)])</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [195](../주석코드/tests/test_budget_app.py#L195) | <code>        code, out, _ = self.run_cli(&quot;summary&quot;, &quot;--month&quot;, &quot;2024-01&quot;, &quot;--top&quot;, &quot;1&quot;)</code> | 오른쪽 계산/호출 결과를 (code, out, _)에 저장합니다. |
| [196](../주석코드/tests/test_budget_app.py#L196) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [197](../주석코드/tests/test_budget_app.py#L197) | <code>        self.assertEqual(code, 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [198](../주석코드/tests/test_budget_app.py#L198) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [199](../주석코드/tests/test_budget_app.py#L199) | <code>        self.assertIn(&quot;120.0%&quot;, out)</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [200](../주석코드/tests/test_budget_app.py#L200) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [201](../주석코드/tests/test_budget_app.py#L201) | <code>        self.assertIn(&quot;예산 초과&quot;, out)</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [202](../주석코드/tests/test_budget_app.py#L202) | <code>        # 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다.</code> | 설명 주석입니다. 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [203](../주석코드/tests/test_budget_app.py#L203) | <code>        self.assertNotIn(&quot;2) food&quot;, out)</code> | 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다. / 테스트 검증 메서드 self.assertNotIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [204](../주석코드/tests/test_budget_app.py#L204) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [205](../주석코드/tests/test_budget_app.py#L205) | <code>    # 거래 없는 월도 데이터 없음과 설정 예산 0%를 출력하는지 확인합니다.</code> | 설명 주석입니다. 거래 없는 월도 데이터 없음과 설정 예산 0%를 출력하는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [206](../주석코드/tests/test_budget_app.py#L206) | <code>    def test_empty_summary_still_shows_budget(self) -&gt; None:</code> | 거래 없는 월도 데이터 없음과 설정 예산 0%를 출력하는지 확인합니다. / test_empty_summary_still_shows_budget 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [207](../주석코드/tests/test_budget_app.py#L207) | <code>        self.service.set_budget(&quot;2024-02&quot;, 10)</code> | self.service.set_budget 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [208](../주석코드/tests/test_budget_app.py#L208) | <code>        code, out, _ = self.run_cli(&quot;summary&quot;, &quot;--month&quot;, &quot;2024-02&quot;)</code> | 오른쪽 계산/호출 결과를 (code, out, _)에 저장합니다. |
| [209](../주석코드/tests/test_budget_app.py#L209) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [210](../주석코드/tests/test_budget_app.py#L210) | <code>        self.assertEqual(code, 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [211](../주석코드/tests/test_budget_app.py#L211) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [212](../주석코드/tests/test_budget_app.py#L212) | <code>        self.assertIn(&quot;데이터 없음&quot;, out)</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [213](../주석코드/tests/test_budget_app.py#L213) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [214](../주석코드/tests/test_budget_app.py#L214) | <code>        self.assertIn(&quot;0.0%&quot;, out)</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [215](../주석코드/tests/test_budget_app.py#L215) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [216](../주석코드/tests/test_budget_app.py#L216) | <code>    # 중복 추가 거부와 사용 중 카테고리 삭제 보호를 확인합니다.</code> | 설명 주석입니다. 중복 추가 거부와 사용 중 카테고리 삭제 보호를 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [217](../주석코드/tests/test_budget_app.py#L217) | <code>    def test_category_usage_and_duplicate_guard(self) -&gt; None:</code> | 중복 추가 거부와 사용 중 카테고리 삭제 보호를 확인합니다. / test_category_usage_and_duplicate_guard 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [218](../주석코드/tests/test_budget_app.py#L218) | <code>        self.service.category_add(&quot;leisure&quot;)</code> | self.service.category_add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [219](../주석코드/tests/test_budget_app.py#L219) | <code>        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [220](../주석코드/tests/test_budget_app.py#L220) | <code>        with self.assertRaises(AppError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [221](../주석코드/tests/test_budget_app.py#L221) | <code>            self.service.category_add(&quot;leisure&quot;)</code> | self.service.category_add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [222](../주석코드/tests/test_budget_app.py#L222) | <code>        self.service.category_remove(&quot;leisure&quot;)</code> | self.service.category_remove 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [223](../주석코드/tests/test_budget_app.py#L223) | <code>        self.service.add(self.transaction())</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [224](../주석코드/tests/test_budget_app.py#L224) | <code>        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [225](../주석코드/tests/test_budget_app.py#L225) | <code>        with self.assertRaisesRegex(AppError, &quot;사용 중&quot;):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [226](../주석코드/tests/test_budget_app.py#L226) | <code>            self.service.category_remove(&quot;food&quot;)</code> | self.service.category_remove 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [227](../주석코드/tests/test_budget_app.py#L227) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [228](../주석코드/tests/test_budget_app.py#L228) | <code>    # CSV 가져오기→내보내기→재가져오기에서 한글·인용·개행·태그 보존을 확인합니다.</code> | 설명 주석입니다. CSV 가져오기→내보내기→재가져오기에서 한글·인용·개행·태그 보존을 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [229](../주석코드/tests/test_budget_app.py#L229) | <code>    def test_import_and_export_roundtrip_unicode_quotes_and_tags(self) -&gt; None:</code> | CSV 가져오기→내보내기→재가져오기에서 한글·인용·개행·태그 보존을 확인합니다. / test_import_and_export_roundtrip_unicode_quotes_and_tags 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [230](../주석코드/tests/test_budget_app.py#L230) | <code>        path = self.csv_file([[&quot;2024-01-01&quot;, &quot;expense&quot;, &quot;food&quot;, &quot;1200&quot;, &#x27;한글, &quot;메모&quot;\n두 줄&#x27;, &quot;a,b&quot;],</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [231](../주석코드/tests/test_budget_app.py#L231) | <code>                              [&quot;2024-01-31&quot;, &quot;income&quot;, &quot;salary&quot;, &quot;3000&quot;, &quot;월급&quot;, &quot;&quot;]])</code> | 230행에서 시작한 Assign 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [232](../주석코드/tests/test_budget_app.py#L232) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [233](../주석코드/tests/test_budget_app.py#L233) | <code>        self.assertEqual(self.service.import_csv(path), 2)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [234](../주석코드/tests/test_budget_app.py#L234) | <code>        exported = self.root / &quot;export.csv&quot;</code> | 오른쪽 계산/호출 결과를 exported에 저장합니다. |
| [235](../주석코드/tests/test_budget_app.py#L235) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [236](../주석코드/tests/test_budget_app.py#L236) | <code>        self.assertEqual(self.service.export_csv(exported, Filters(month=&quot;2024-01&quot;)), 2)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [237](../주석코드/tests/test_budget_app.py#L237) | <code>        with exported.open(encoding=&quot;utf-8&quot;, newline=&quot;&quot;) as stream:</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [238](../주석코드/tests/test_budget_app.py#L238) | <code>            rows = list(csv.DictReader(stream))</code> | 오른쪽 계산/호출 결과를 rows에 저장합니다. |
| [239](../주석코드/tests/test_budget_app.py#L239) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [240](../주석코드/tests/test_budget_app.py#L240) | <code>        self.assertEqual(rows[1][&quot;memo&quot;], &#x27;한글, &quot;메모&quot;\n두 줄&#x27;)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [241](../주석코드/tests/test_budget_app.py#L241) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [242](../주석코드/tests/test_budget_app.py#L242) | <code>        self.assertEqual(rows[1][&quot;tags&quot;], &quot;a,b&quot;)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [243](../주석코드/tests/test_budget_app.py#L243) | <code>        second = DataStore(self.root / &quot;second&quot;)</code> | 오른쪽 계산/호출 결과를 second에 저장합니다. |
| [244](../주석코드/tests/test_budget_app.py#L244) | <code>        with second.session():</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [245](../주석코드/tests/test_budget_app.py#L245) | <code>            # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [246](../주석코드/tests/test_budget_app.py#L246) | <code>            self.assertEqual(BudgetService(second).import_csv(exported), 2)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [247](../주석코드/tests/test_budget_app.py#L247) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [248](../주석코드/tests/test_budget_app.py#L248) | <code>    # 두 번째 행 실패 시 첫 번째 행도 반영되지 않는 전체 취소를 검증합니다.</code> | 설명 주석입니다. 두 번째 행 실패 시 첫 번째 행도 반영되지 않는 전체 취소를 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [249](../주석코드/tests/test_budget_app.py#L249) | <code>    def test_import_invalid_later_row_rolls_back_everything(self) -&gt; None:</code> | 두 번째 행 실패 시 첫 번째 행도 반영되지 않는 전체 취소를 검증합니다. / test_import_invalid_later_row_rolls_back_everything 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [250](../주석코드/tests/test_budget_app.py#L250) | <code>        self.service.add(self.transaction())</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [251](../주석코드/tests/test_budget_app.py#L251) | <code>        # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.</code> | 설명 주석입니다. 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [252](../주석코드/tests/test_budget_app.py#L252) | <code>        before = self.store.path(&quot;transactions&quot;).read_bytes()</code> | 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. / 오른쪽 계산/호출 결과를 before에 저장합니다. |
| [253](../주석코드/tests/test_budget_app.py#L253) | <code>        path = self.csv_file([[&quot;2024-01-01&quot;, &quot;expense&quot;, &quot;food&quot;, &quot;10&quot;, &quot;valid&quot;, &quot;&quot;],</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [254](../주석코드/tests/test_budget_app.py#L254) | <code>                              [&quot;2024-01-02&quot;, &quot;expense&quot;, &quot;food&quot;, &quot;0&quot;, &quot;invalid&quot;, &quot;&quot;]])</code> | 253행에서 시작한 Assign 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [255](../주석코드/tests/test_budget_app.py#L255) | <code>        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [256](../주석코드/tests/test_budget_app.py#L256) | <code>        with self.assertRaisesRegex(AppError, &quot;CSV 3행&quot;):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [257](../주석코드/tests/test_budget_app.py#L257) | <code>            self.service.import_csv(path)</code> | self.service.import_csv 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [258](../주석코드/tests/test_budget_app.py#L258) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [259](../주석코드/tests/test_budget_app.py#L259) | <code>        self.assertEqual(before, self.store.path(&quot;transactions&quot;).read_bytes())</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [260](../주석코드/tests/test_budget_app.py#L260) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [261](../주석코드/tests/test_budget_app.py#L261) | <code>        self.assertEqual(list(self.store.directory.glob(&quot;.import-*&quot;)), [])</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [262](../주석코드/tests/test_budget_app.py#L262) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [263](../주석코드/tests/test_budget_app.py#L263) | <code>    # 중복 헤더·미등록 카테고리·깨진 인코딩을 안전하게 거부하는지 확인합니다.</code> | 설명 주석입니다. 중복 헤더·미등록 카테고리·깨진 인코딩을 안전하게 거부하는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [264](../주석코드/tests/test_budget_app.py#L264) | <code>    def test_import_bad_headers_unknown_category_and_bad_encoding(self) -&gt; None:</code> | 중복 헤더·미등록 카테고리·깨진 인코딩을 안전하게 거부하는지 확인합니다. / test_import_bad_headers_unknown_category_and_bad_encoding 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [265](../주석코드/tests/test_budget_app.py#L265) | <code>        path = self.csv_file([], header=(&quot;date&quot;, &quot;type&quot;, &quot;category&quot;, &quot;amount&quot;, &quot;amount&quot;))</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [266](../주석코드/tests/test_budget_app.py#L266) | <code>        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [267](../주석코드/tests/test_budget_app.py#L267) | <code>        with self.assertRaises(AppError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [268](../주석코드/tests/test_budget_app.py#L268) | <code>            self.service.import_csv(path)</code> | self.service.import_csv 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [269](../주석코드/tests/test_budget_app.py#L269) | <code>        path = self.csv_file([[&quot;2024-01-01&quot;, &quot;expense&quot;, &quot;missing&quot;, &quot;10&quot;, &quot;&quot;, &quot;&quot;]])</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [270](../주석코드/tests/test_budget_app.py#L270) | <code>        # 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다.</code> | 설명 주석입니다. 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [271](../주석코드/tests/test_budget_app.py#L271) | <code>        self.assertNotEqual(self.run_cli(&quot;import&quot;, &quot;--from&quot;, str(path))[0], 0)</code> | 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다. / 테스트 검증 메서드 self.assertNotEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [272](../주석코드/tests/test_budget_app.py#L272) | <code>        path.write_bytes(b&quot;\xff\xff&quot;)</code> | path.write_bytes 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [273](../주석코드/tests/test_budget_app.py#L273) | <code>        code, _, err = self.run_cli(&quot;import&quot;, &quot;--from&quot;, str(path))</code> | 오른쪽 계산/호출 결과를 (code, _, err)에 저장합니다. |
| [274](../주석코드/tests/test_budget_app.py#L274) | <code>        # 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다.</code> | 설명 주석입니다. 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [275](../주석코드/tests/test_budget_app.py#L275) | <code>        self.assertNotEqual(code, 0)</code> | 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다. / 테스트 검증 메서드 self.assertNotEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [276](../주석코드/tests/test_budget_app.py#L276) | <code>        # 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다.</code> | 설명 주석입니다. 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [277](../주석코드/tests/test_budget_app.py#L277) | <code>        self.assertNotIn(&quot;Traceback&quot;, err)</code> | 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다. / 테스트 검증 메서드 self.assertNotIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [278](../주석코드/tests/test_budget_app.py#L278) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [279](../주석코드/tests/test_budget_app.py#L279) | <code>    # 선택 열이 없거나 UTF-8 BOM이 있는 정상 CSV를 허용하는지 확인합니다.</code> | 설명 주석입니다. 선택 열이 없거나 UTF-8 BOM이 있는 정상 CSV를 허용하는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [280](../주석코드/tests/test_budget_app.py#L280) | <code>    def test_optional_csv_columns_and_bom(self) -&gt; None:</code> | 선택 열이 없거나 UTF-8 BOM이 있는 정상 CSV를 허용하는지 확인합니다. / test_optional_csv_columns_and_bom 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [281](../주석코드/tests/test_budget_app.py#L281) | <code>        path = self.csv_file([[&quot;2024-01-01&quot;, &quot;expense&quot;, &quot;food&quot;, &quot;1&quot;]], header=(&quot;date&quot;, &quot;type&quot;, &quot;category&quot;, &quot;amount&quot;))</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [282](../주석코드/tests/test_budget_app.py#L282) | <code>        path.write_bytes(b&quot;\xef\xbb\xbf&quot; + path.read_bytes())</code> | path.write_bytes 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [283](../주석코드/tests/test_budget_app.py#L283) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [284](../주석코드/tests/test_budget_app.py#L284) | <code>        self.assertEqual(self.service.import_csv(path), 1)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [285](../주석코드/tests/test_budget_app.py#L285) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [286](../주석코드/tests/test_budget_app.py#L286) | <code>    # 기간 없는 내보내기와 실제 저장 파일 덮어쓰기를 막는지 검증합니다.</code> | 설명 주석입니다. 기간 없는 내보내기와 실제 저장 파일 덮어쓰기를 막는지 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [287](../주석코드/tests/test_budget_app.py#L287) | <code>    def test_export_requires_period_and_protects_data(self) -&gt; None:</code> | 기간 없는 내보내기와 실제 저장 파일 덮어쓰기를 막는지 검증합니다. / test_export_requires_period_and_protects_data 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [288](../주석코드/tests/test_budget_app.py#L288) | <code>        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [289](../주석코드/tests/test_budget_app.py#L289) | <code>        with self.assertRaises(AppError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [290](../주석코드/tests/test_budget_app.py#L290) | <code>            self.service.export_csv(self.root / &quot;out.csv&quot;, Filters())</code> | self.service.export_csv 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [291](../주석코드/tests/test_budget_app.py#L291) | <code>        for name in self.store.FILES:</code> | self.store.FILES에서 값을 하나씩 받아 name에 넣고 블록을 반복합니다. |
| [292](../주석코드/tests/test_budget_app.py#L292) | <code>            path = self.store.directory / name</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [293](../주석코드/tests/test_budget_app.py#L293) | <code>            # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.</code> | 설명 주석입니다. 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [294](../주석코드/tests/test_budget_app.py#L294) | <code>            before = path.read_bytes()</code> | 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. / 오른쪽 계산/호출 결과를 before에 저장합니다. |
| [295](../주석코드/tests/test_budget_app.py#L295) | <code>            # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [296](../주석코드/tests/test_budget_app.py#L296) | <code>            with self.assertRaises(AppError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [297](../주석코드/tests/test_budget_app.py#L297) | <code>                self.service.export_csv(path, Filters(month=&quot;2024-01&quot;))</code> | self.service.export_csv 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [298](../주석코드/tests/test_budget_app.py#L298) | <code>            # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [299](../주석코드/tests/test_budget_app.py#L299) | <code>            self.assertEqual(before, path.read_bytes())</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [300](../주석코드/tests/test_budget_app.py#L300) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [301](../주석코드/tests/test_budget_app.py#L301) | <code>    # 기간 경계를 포함하며 결과 0건이어도 CSV 헤더는 만드는지 확인합니다.</code> | 설명 주석입니다. 기간 경계를 포함하며 결과 0건이어도 CSV 헤더는 만드는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [302](../주석코드/tests/test_budget_app.py#L302) | <code>    def test_export_range_and_empty_header(self) -&gt; None:</code> | 기간 경계를 포함하며 결과 0건이어도 CSV 헤더는 만드는지 확인합니다. / test_export_range_and_empty_header 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [303](../주석코드/tests/test_budget_app.py#L303) | <code>        self.service.add(self.transaction())</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [304](../주석코드/tests/test_budget_app.py#L304) | <code>        path = self.root / &quot;out.csv&quot;</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [305](../주석코드/tests/test_budget_app.py#L305) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [306](../주석코드/tests/test_budget_app.py#L306) | <code>        self.assertEqual(self.service.export_csv(path, Filters(start=&quot;2024-01-15&quot;, end=&quot;2024-01-15&quot;)), 1)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [307](../주석코드/tests/test_budget_app.py#L307) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [308](../주석코드/tests/test_budget_app.py#L308) | <code>        self.assertEqual(self.service.export_csv(path, Filters(month=&quot;2023-01&quot;)), 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [309](../주석코드/tests/test_budget_app.py#L309) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [310](../주석코드/tests/test_budget_app.py#L310) | <code>        self.assertEqual(len(path.read_text(encoding=&quot;utf-8&quot;).splitlines()), 1)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [311](../주석코드/tests/test_budget_app.py#L311) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [312](../주석코드/tests/test_budget_app.py#L312) | <code>    # 쓰기 도중 오류와 os.replace 실패를 주입해 원본·임시 파일 정리를 검증합니다.</code> | 설명 주석입니다. 쓰기 도중 오류와 os.replace 실패를 주입해 원본·임시 파일 정리를 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [313](../주석코드/tests/test_budget_app.py#L313) | <code>    def test_atomic_write_failure_does_not_truncate_original(self) -&gt; None:</code> | 쓰기 도중 오류와 os.replace 실패를 주입해 원본·임시 파일 정리를 검증합니다. / test_atomic_write_failure_does_not_truncate_original 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [314](../주석코드/tests/test_budget_app.py#L314) | <code>        self.service.add(self.transaction())</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [315](../주석코드/tests/test_budget_app.py#L315) | <code>        path = self.store.path(&quot;transactions&quot;)</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [316](../주석코드/tests/test_budget_app.py#L316) | <code>        # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.</code> | 설명 주석입니다. 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [317](../주석코드/tests/test_budget_app.py#L317) | <code>        before = path.read_bytes()</code> | 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. / 오른쪽 계산/호출 결과를 before에 저장합니다. |
| [318](../주석코드/tests/test_budget_app.py#L318) | <code>        # 일부 기록 뒤 고의 오류를 내는 제너레이터로 저장 실패를 재현합니다.</code> | 설명 주석입니다. 일부 기록 뒤 고의 오류를 내는 제너레이터로 저장 실패를 재현합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [319](../주석코드/tests/test_budget_app.py#L319) | <code>        def records():</code> | 일부 기록 뒤 고의 오류를 내는 제너레이터로 저장 실패를 재현합니다. / records 함수를 정의합니다. 인자: 없음. 반환 타입: 반환 타입 미지정. def 자체는 본문을 실행하지 않습니다. |
| [320](../주석코드/tests/test_budget_app.py#L320) | <code>            yield {&quot;partial&quot;: True}</code> | 호출자에게 {&#x27;partial&#x27;: True}을 전달하고 잠시 멈춥니다. 다음 요청/컨텍스트 종료 시 이 지점 뒤에서 이어집니다. |
| [321](../주석코드/tests/test_budget_app.py#L321) | <code>            raise OSError(&quot;simulated disk failure&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [322](../주석코드/tests/test_budget_app.py#L322) | <code>        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [323](../주석코드/tests/test_budget_app.py#L323) | <code>        with self.assertRaises(OSError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [324](../주석코드/tests/test_budget_app.py#L324) | <code>            write_jsonl(path, records())</code> | write_jsonl 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [325](../주석코드/tests/test_budget_app.py#L325) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [326](../주석코드/tests/test_budget_app.py#L326) | <code>        self.assertEqual(path.read_bytes(), before)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [327](../주석코드/tests/test_budget_app.py#L327) | <code>        # 실제 사용자 입력/운영체제 기능을 대신하는 조건을 주입해 실패 경로를 재현합니다.</code> | 설명 주석입니다. 실제 사용자 입력/운영체제 기능을 대신하는 조건을 주입해 실패 경로를 재현합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [328](../주석코드/tests/test_budget_app.py#L328) | <code>        with patch(&quot;budget_app.storage.os.replace&quot;, side_effect=PermissionError(&quot;simulated replace failure&quot;)):</code> | 실제 사용자 입력/운영체제 기능을 대신하는 조건을 주입해 실패 경로를 재현합니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [329](../주석코드/tests/test_budget_app.py#L329) | <code>            # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [330](../주석코드/tests/test_budget_app.py#L330) | <code>            with self.assertRaises(PermissionError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [331](../주석코드/tests/test_budget_app.py#L331) | <code>                self.service.add(self.transaction())</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [332](../주석코드/tests/test_budget_app.py#L332) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [333](../주석코드/tests/test_budget_app.py#L333) | <code>        self.assertEqual(path.read_bytes(), before)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [334](../주석코드/tests/test_budget_app.py#L334) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [335](../주석코드/tests/test_budget_app.py#L335) | <code>        self.assertEqual(list(self.store.directory.glob(&quot;.budget-*.tmp&quot;)), [])</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [336](../주석코드/tests/test_budget_app.py#L336) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [337](../주석코드/tests/test_budget_app.py#L337) | <code>    # 파일 뒤쪽 손상을 만났을 때 새 저장으로 손상 원본을 덮어쓰지 않는지 확인합니다.</code> | 설명 주석입니다. 파일 뒤쪽 손상을 만났을 때 새 저장으로 손상 원본을 덮어쓰지 않는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [338](../주석코드/tests/test_budget_app.py#L338) | <code>    def test_corruption_during_rewrite_preserves_original(self) -&gt; None:</code> | 파일 뒤쪽 손상을 만났을 때 새 저장으로 손상 원본을 덮어쓰지 않는지 확인합니다. / test_corruption_during_rewrite_preserves_original 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [339](../주석코드/tests/test_budget_app.py#L339) | <code>        self.service.add(self.transaction())</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [340](../주석코드/tests/test_budget_app.py#L340) | <code>        path = self.store.path(&quot;transactions&quot;)</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [341](../주석코드/tests/test_budget_app.py#L341) | <code>        with path.open(&quot;a&quot;, encoding=&quot;utf-8&quot;) as stream:</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [342](../주석코드/tests/test_budget_app.py#L342) | <code>            stream.write(&quot;{broken\n&quot;)</code> | stream.write 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [343](../주석코드/tests/test_budget_app.py#L343) | <code>        # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.</code> | 설명 주석입니다. 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [344](../주석코드/tests/test_budget_app.py#L344) | <code>        before = path.read_bytes()</code> | 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다. / 오른쪽 계산/호출 결과를 before에 저장합니다. |
| [345](../주석코드/tests/test_budget_app.py#L345) | <code>        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [346](../주석코드/tests/test_budget_app.py#L346) | <code>        with self.assertRaises(AppError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [347](../주석코드/tests/test_budget_app.py#L347) | <code>            self.service.add(self.transaction())</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [348](../주석코드/tests/test_budget_app.py#L348) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [349](../주석코드/tests/test_budget_app.py#L349) | <code>        self.assertEqual(before, path.read_bytes())</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [350](../주석코드/tests/test_budget_app.py#L350) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [351](../주석코드/tests/test_budget_app.py#L351) | <code>    # 필드 누락과 정렬 손상이 거래 읽기에서 보고되는지 확인합니다.</code> | 설명 주석입니다. 필드 누락과 정렬 손상이 거래 읽기에서 보고되는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [352](../주석코드/tests/test_budget_app.py#L352) | <code>    def test_invalid_schema_and_sort_order_are_reported(self) -&gt; None:</code> | 필드 누락과 정렬 손상이 거래 읽기에서 보고되는지 확인합니다. / test_invalid_schema_and_sort_order_are_reported 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [353](../주석코드/tests/test_budget_app.py#L353) | <code>        path = self.store.path(&quot;transactions&quot;)</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [354](../주석코드/tests/test_budget_app.py#L354) | <code>        for rows in ([{&quot;id&quot;: &quot;bad&quot;}], [self.transaction(&quot;2024-01-01&quot;).record(), self.transaction(&quot;2024-02-01&quot;).record()]):</code> | ([{&#x27;id&#x27;: &#x27;bad&#x27;}], [self.transaction(&#x27;2024-01-01&#x27;).record(), self.transaction(&#x27;2024-02-01&#x27;).record()])에서 값을 하나씩 받아 rows에 넣고 블록을 반복합니다. |
| [355](../주석코드/tests/test_budget_app.py#L355) | <code>            write_jsonl(path, rows)</code> | write_jsonl 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [356](../주석코드/tests/test_budget_app.py#L356) | <code>            # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [357](../주석코드/tests/test_budget_app.py#L357) | <code>            with self.assertRaises(AppError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [358](../주석코드/tests/test_budget_app.py#L358) | <code>                list(self.service.transactions.iter_all())</code> | list 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [359](../주석코드/tests/test_budget_app.py#L359) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [360](../주석코드/tests/test_budget_app.py#L360) | <code>    # 두 번째 세션을 막고 정상·예외 종료에서 잠금을 정리하는지 검증합니다.</code> | 설명 주석입니다. 두 번째 세션을 막고 정상·예외 종료에서 잠금을 정리하는지 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [361](../주석코드/tests/test_budget_app.py#L361) | <code>    def test_lock_blocks_second_command_and_cleans_up(self) -&gt; None:</code> | 두 번째 세션을 막고 정상·예외 종료에서 잠금을 정리하는지 검증합니다. / test_lock_blocks_second_command_and_cleans_up 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [362](../주석코드/tests/test_budget_app.py#L362) | <code>        with self.store.session():</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [363](../주석코드/tests/test_budget_app.py#L363) | <code>            # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [364](../주석코드/tests/test_budget_app.py#L364) | <code>            with self.assertRaises(AppError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [365](../주석코드/tests/test_budget_app.py#L365) | <code>                with DataStore(self.store.directory).session():</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [366](../주석코드/tests/test_budget_app.py#L366) | <code>                    self.fail(&quot;lock bypass&quot;)</code> | self.fail 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [367](../주석코드/tests/test_budget_app.py#L367) | <code>        # 정리 후 잠금 파일 등이 남아 있지 않아야 합니다.</code> | 설명 주석입니다. 정리 후 잠금 파일 등이 남아 있지 않아야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [368](../주석코드/tests/test_budget_app.py#L368) | <code>        self.assertFalse((self.store.directory / &quot;.budget.lock&quot;).exists())</code> | 정리 후 잠금 파일 등이 남아 있지 않아야 합니다. / 테스트 검증 메서드 self.assertFalse를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [369](../주석코드/tests/test_budget_app.py#L369) | <code>        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.</code> | 설명 주석입니다. 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [370](../주석코드/tests/test_budget_app.py#L370) | <code>        with self.assertRaises(RuntimeError):</code> | 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [371](../주석코드/tests/test_budget_app.py#L371) | <code>            with self.store.session():</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [372](../주석코드/tests/test_budget_app.py#L372) | <code>                raise RuntimeError(&quot;test&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [373](../주석코드/tests/test_budget_app.py#L373) | <code>        # 정리 후 잠금 파일 등이 남아 있지 않아야 합니다.</code> | 설명 주석입니다. 정리 후 잠금 파일 등이 남아 있지 않아야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [374](../주석코드/tests/test_budget_app.py#L374) | <code>        self.assertFalse((self.store.directory / &quot;.budget.lock&quot;).exists())</code> | 정리 후 잠금 파일 등이 남아 있지 않아야 합니다. / 테스트 검증 메서드 self.assertFalse를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [375](../주석코드/tests/test_budget_app.py#L375) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [376](../주석코드/tests/test_budget_app.py#L376) | <code>    # 백업 이름 구별 및 ZIP 안의 세 파일 이름·바이트 일치를 확인합니다.</code> | 설명 주석입니다. 백업 이름 구별 및 ZIP 안의 세 파일 이름·바이트 일치를 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [377](../주석코드/tests/test_budget_app.py#L377) | <code>    def test_backup_contains_all_persistent_files(self) -&gt; None:</code> | 백업 이름 구별 및 ZIP 안의 세 파일 이름·바이트 일치를 확인합니다. / test_backup_contains_all_persistent_files 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [378](../주석코드/tests/test_budget_app.py#L378) | <code>        self.service.add(self.transaction())</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [379](../주석코드/tests/test_budget_app.py#L379) | <code>        path = self.service.backup()</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [380](../주석코드/tests/test_budget_app.py#L380) | <code>        # 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다.</code> | 설명 주석입니다. 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [381](../주석코드/tests/test_budget_app.py#L381) | <code>        self.assertNotEqual(path, self.service.backup())</code> | 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다. / 테스트 검증 메서드 self.assertNotEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [382](../주석코드/tests/test_budget_app.py#L382) | <code>        with zipfile.ZipFile(path) as archive:</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [383](../주석코드/tests/test_budget_app.py#L383) | <code>            # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [384](../주석코드/tests/test_budget_app.py#L384) | <code>            self.assertEqual(set(archive.namelist()), set(self.store.FILES))</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [385](../주석코드/tests/test_budget_app.py#L385) | <code>            for name in self.store.FILES:</code> | self.store.FILES에서 값을 하나씩 받아 name에 넣고 블록을 반복합니다. |
| [386](../주석코드/tests/test_budget_app.py#L386) | <code>                # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [387](../주석코드/tests/test_budget_app.py#L387) | <code>                self.assertEqual(archive.read(name), (self.store.directory / name).read_bytes())</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [388](../주석코드/tests/test_budget_app.py#L388) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [389](../주석코드/tests/test_budget_app.py#L389) | <code>    # 대화형 입력 저장과 --limit 1이 한 건만 출력하는지 확인합니다.</code> | 설명 주석입니다. 대화형 입력 저장과 --limit 1이 한 건만 출력하는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [390](../주석코드/tests/test_budget_app.py#L390) | <code>    def test_interactive_add_and_list_limit(self) -&gt; None:</code> | 대화형 입력 저장과 --limit 1이 한 건만 출력하는지 확인합니다. / test_interactive_add_and_list_limit 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [391](../주석코드/tests/test_budget_app.py#L391) | <code>        inputs = [&quot;2024-01-15&quot;, &quot;expense&quot;, &quot;food&quot;, &quot;15000&quot;, &quot;점심&quot;, &quot;meal&quot;]</code> | 오른쪽 계산/호출 결과를 inputs에 저장합니다. |
| [392](../주석코드/tests/test_budget_app.py#L392) | <code>        code, out, _ = self.run_cli(&quot;add&quot;, inputs=inputs)</code> | 오른쪽 계산/호출 결과를 (code, out, _)에 저장합니다. |
| [393](../주석코드/tests/test_budget_app.py#L393) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [394](../주석코드/tests/test_budget_app.py#L394) | <code>        self.assertEqual(code, 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [395](../주석코드/tests/test_budget_app.py#L395) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [396](../주석코드/tests/test_budget_app.py#L396) | <code>        self.assertIn(&quot;id=TX-&quot;, out)</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [397](../주석코드/tests/test_budget_app.py#L397) | <code>        self.service.add(self.transaction())</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [398](../주석코드/tests/test_budget_app.py#L398) | <code>        code, out, _ = self.run_cli(&quot;list&quot;, &quot;--limit&quot;, &quot;1&quot;)</code> | 오른쪽 계산/호출 결과를 (code, out, _)에 저장합니다. |
| [399](../주석코드/tests/test_budget_app.py#L399) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [400](../주석코드/tests/test_budget_app.py#L400) | <code>        self.assertEqual(code, 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [401](../주석코드/tests/test_budget_app.py#L401) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [402](../주석코드/tests/test_budget_app.py#L402) | <code>        self.assertEqual(out.count(&quot;TX-&quot;), 1)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [403](../주석코드/tests/test_budget_app.py#L403) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [404](../주석코드/tests/test_budget_app.py#L404) | <code>    # 없는 id와 EOF 취소에서 힌트·종료 코드·스택트레이스 생략을 확인합니다.</code> | 설명 주석입니다. 없는 id와 EOF 취소에서 힌트·종료 코드·스택트레이스 생략을 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [405](../주석코드/tests/test_budget_app.py#L405) | <code>    def test_cli_error_and_cancel_have_no_traceback(self) -&gt; None:</code> | 없는 id와 EOF 취소에서 힌트·종료 코드·스택트레이스 생략을 확인합니다. / test_cli_error_and_cancel_have_no_traceback 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [406](../주석코드/tests/test_budget_app.py#L406) | <code>        code, _, err = self.run_cli(&quot;delete&quot;, &quot;--id&quot;, &quot;unknown&quot;)</code> | 오른쪽 계산/호출 결과를 (code, _, err)에 저장합니다. |
| [407](../주석코드/tests/test_budget_app.py#L407) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [408](../주석코드/tests/test_budget_app.py#L408) | <code>        self.assertEqual(code, 1)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [409](../주석코드/tests/test_budget_app.py#L409) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [410](../주석코드/tests/test_budget_app.py#L410) | <code>        self.assertIn(&quot;[힌트]&quot;, err)</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [411](../주석코드/tests/test_budget_app.py#L411) | <code>        # 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다.</code> | 설명 주석입니다. 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [412](../주석코드/tests/test_budget_app.py#L412) | <code>        self.assertNotIn(&quot;Traceback&quot;, err)</code> | 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다. / 테스트 검증 메서드 self.assertNotIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [413](../주석코드/tests/test_budget_app.py#L413) | <code>        # 실제 사용자 입력/운영체제 기능을 대신하는 조건을 주입해 실패 경로를 재현합니다.</code> | 설명 주석입니다. 실제 사용자 입력/운영체제 기능을 대신하는 조건을 주입해 실패 경로를 재현합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [414](../주석코드/tests/test_budget_app.py#L414) | <code>        with patch(&quot;builtins.input&quot;, side_effect=EOFError), redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()):</code> | 실제 사용자 입력/운영체제 기능을 대신하는 조건을 주입해 실패 경로를 재현합니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [415](../주석코드/tests/test_budget_app.py#L415) | <code>            # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [416](../주석코드/tests/test_budget_app.py#L416) | <code>            self.assertEqual(main([&quot;--data-dir&quot;, str(self.store.directory), &quot;add&quot;]), 130)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [417](../주석코드/tests/test_budget_app.py#L417) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [418](../주석코드/tests/test_budget_app.py#L418) | <code>    # 카테고리·예산·검색 명령을 CLI 경로로 검증합니다.</code> | 설명 주석입니다. 카테고리·예산·검색 명령을 CLI 경로로 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [419](../주석코드/tests/test_budget_app.py#L419) | <code>    def test_cli_budget_category_and_search(self) -&gt; None:</code> | 카테고리·예산·검색 명령을 CLI 경로로 검증합니다. / test_cli_budget_category_and_search 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [420](../주석코드/tests/test_budget_app.py#L420) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [421](../주석코드/tests/test_budget_app.py#L421) | <code>        self.assertEqual(self.run_cli(&quot;category&quot;, &quot;add&quot;, inputs=[&quot;취미&quot;])[0], 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [422](../주석코드/tests/test_budget_app.py#L422) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [423](../주석코드/tests/test_budget_app.py#L423) | <code>        self.assertIn(&quot;취미&quot;, self.run_cli(&quot;category&quot;, &quot;list&quot;)[1])</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [424](../주석코드/tests/test_budget_app.py#L424) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [425](../주석코드/tests/test_budget_app.py#L425) | <code>        self.assertEqual(self.run_cli(&quot;category&quot;, &quot;remove&quot;, inputs=[&quot;취미&quot;])[0], 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [426](../주석코드/tests/test_budget_app.py#L426) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [427](../주석코드/tests/test_budget_app.py#L427) | <code>        self.assertEqual(self.run_cli(&quot;budget&quot;, &quot;set&quot;, &quot;--month&quot;, &quot;2024-01&quot;, &quot;--amount&quot;, &quot;100&quot;)[0], 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [428](../주석코드/tests/test_budget_app.py#L428) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [429](../주석코드/tests/test_budget_app.py#L429) | <code>        self.assertIn(&quot;100원&quot;, self.run_cli(&quot;budget&quot;, &quot;show&quot;, &quot;--month&quot;, &quot;2024-01&quot;)[1])</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [430](../주석코드/tests/test_budget_app.py#L430) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [431](../주석코드/tests/test_budget_app.py#L431) | <code>        self.assertIn(&quot;데이터 없음&quot;, self.run_cli(&quot;search&quot;, &quot;--q&quot;, &quot;none&quot;)[1])</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [432](../주석코드/tests/test_budget_app.py#L432) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [433](../주석코드/tests/test_budget_app.py#L433) | <code>    # 여러 CLI 명령을 이어 실행해 거래 변경과 입출력 연결을 검증합니다.</code> | 설명 주석입니다. 여러 CLI 명령을 이어 실행해 거래 변경과 입출력 연결을 검증합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [434](../주석코드/tests/test_budget_app.py#L434) | <code>    def test_cli_update_delete_export_import_and_backup(self) -&gt; None:</code> | 여러 CLI 명령을 이어 실행해 거래 변경과 입출력 연결을 검증합니다. / test_cli_update_delete_export_import_and_backup 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [435](../주석코드/tests/test_budget_app.py#L435) | <code>        t = self.transaction()</code> | 오른쪽 계산/호출 결과를 t에 저장합니다. |
| [436](../주석코드/tests/test_budget_app.py#L436) | <code>        self.service.add(t)</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [437](../주석코드/tests/test_budget_app.py#L437) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [438](../주석코드/tests/test_budget_app.py#L438) | <code>        self.assertEqual(self.run_cli(&quot;update&quot;, &quot;--id&quot;, t.id, &quot;--memo&quot;, &quot;new&quot;)[0], 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [439](../주석코드/tests/test_budget_app.py#L439) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [440](../주석코드/tests/test_budget_app.py#L440) | <code>        self.assertEqual(self.service.transactions.find(t.id).memo, &quot;new&quot;)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [441](../주석코드/tests/test_budget_app.py#L441) | <code>        out = str(self.root / &quot;out.csv&quot;)</code> | 오른쪽 계산/호출 결과를 out에 저장합니다. |
| [442](../주석코드/tests/test_budget_app.py#L442) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [443](../주석코드/tests/test_budget_app.py#L443) | <code>        self.assertEqual(self.run_cli(&quot;export&quot;, &quot;--out&quot;, out, &quot;--month&quot;, &quot;2024-01&quot;)[0], 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [444](../주석코드/tests/test_budget_app.py#L444) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [445](../주석코드/tests/test_budget_app.py#L445) | <code>        self.assertEqual(self.run_cli(&quot;delete&quot;, &quot;--id&quot;, t.id)[0], 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [446](../주석코드/tests/test_budget_app.py#L446) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [447](../주석코드/tests/test_budget_app.py#L447) | <code>        self.assertIn(&quot;imported=1&quot;, self.run_cli(&quot;import&quot;, &quot;--from&quot;, out)[1])</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [448](../주석코드/tests/test_budget_app.py#L448) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [449](../주석코드/tests/test_budget_app.py#L449) | <code>        self.assertEqual(self.run_cli(&quot;backup&quot;)[0], 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [450](../주석코드/tests/test_budget_app.py#L450) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [451](../주석코드/tests/test_budget_app.py#L451) | <code>    # 실제 별도 Python 프로세스로 모든 --help와 인자 오류 코드 2를 확인합니다.</code> | 설명 주석입니다. 실제 별도 Python 프로세스로 모든 --help와 인자 오류 코드 2를 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [452](../주석코드/tests/test_budget_app.py#L452) | <code>    def test_subprocess_entrypoint_exit_codes_and_all_help(self) -&gt; None:</code> | 실제 별도 Python 프로세스로 모든 --help와 인자 오류 코드 2를 확인합니다. / test_subprocess_entrypoint_exit_codes_and_all_help 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [453](../주석코드/tests/test_budget_app.py#L453) | <code>        commands = [[], [&quot;add&quot;], [&quot;list&quot;], [&quot;search&quot;], [&quot;summary&quot;], [&quot;update&quot;], [&quot;delete&quot;],</code> | 오른쪽 계산/호출 결과를 commands에 저장합니다. |
| [454](../주석코드/tests/test_budget_app.py#L454) | <code>                    [&quot;import&quot;], [&quot;export&quot;], [&quot;backup&quot;], [&quot;budget&quot;], [&quot;budget&quot;, &quot;set&quot;], [&quot;budget&quot;, &quot;show&quot;],</code> | 453행에서 시작한 Assign 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [455](../주석코드/tests/test_budget_app.py#L455) | <code>                    [&quot;category&quot;], [&quot;category&quot;, &quot;add&quot;], [&quot;category&quot;, &quot;list&quot;], [&quot;category&quot;, &quot;remove&quot;]]</code> | 453행에서 시작한 Assign 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [456](../주석코드/tests/test_budget_app.py#L456) | <code>        env = {**os.environ, &quot;PYTHONIOENCODING&quot;: &quot;utf-8&quot;}</code> | 오른쪽 계산/호출 결과를 env에 저장합니다. |
| [457](../주석코드/tests/test_budget_app.py#L457) | <code>        for command in commands:</code> | commands에서 값을 하나씩 받아 command에 넣고 블록을 반복합니다. |
| [458](../주석코드/tests/test_budget_app.py#L458) | <code>            result = subprocess.run([sys.executable, &quot;-m&quot;, &quot;budget_app&quot;, *command, &quot;--help&quot;],</code> | 오른쪽 계산/호출 결과를 result에 저장합니다. |
| [459](../주석코드/tests/test_budget_app.py#L459) | <code>                                    capture_output=True, encoding=&quot;utf-8&quot;, env=env)</code> | 458행에서 시작한 Assign 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [460](../주석코드/tests/test_budget_app.py#L460) | <code>            # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [461](../주석코드/tests/test_budget_app.py#L461) | <code>            self.assertEqual(result.returncode, 0, result.stderr)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [462](../주석코드/tests/test_budget_app.py#L462) | <code>        result = subprocess.run([sys.executable, &quot;-m&quot;, &quot;budget_app&quot;, &quot;delete&quot;], capture_output=True, encoding=&quot;utf-8&quot;, env=env)</code> | 오른쪽 계산/호출 결과를 result에 저장합니다. |
| [463](../주석코드/tests/test_budget_app.py#L463) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [464](../주석코드/tests/test_budget_app.py#L464) | <code>        self.assertEqual(result.returncode, 2)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [465](../주석코드/tests/test_budget_app.py#L465) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [466](../주석코드/tests/test_budget_app.py#L466) | <code>        self.assertIn(&quot;[힌트]&quot;, result.stderr)</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [467](../주석코드/tests/test_budget_app.py#L467) | <code>        # 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다.</code> | 설명 주석입니다. 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [468](../주석코드/tests/test_budget_app.py#L468) | <code>        self.assertNotIn(&quot;Traceback&quot;, result.stderr)</code> | 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다. / 테스트 검증 메서드 self.assertNotIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [469](../주석코드/tests/test_budget_app.py#L469) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [470](../주석코드/tests/test_budget_app.py#L470) | <code>    # 첫 줄 이후 깨진 행을 둬 --limit 1이 불필요한 읽기를 하지 않는지 확인합니다.</code> | 설명 주석입니다. 첫 줄 이후 깨진 행을 둬 --limit 1이 불필요한 읽기를 하지 않는지 확인합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [471](../주석코드/tests/test_budget_app.py#L471) | <code>    def test_limit_does_not_read_entire_transaction_file(self) -&gt; None:</code> | 첫 줄 이후 깨진 행을 둬 --limit 1이 불필요한 읽기를 하지 않는지 확인합니다. / test_limit_does_not_read_entire_transaction_file 함수를 정의합니다. 인자: self. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [472](../주석코드/tests/test_budget_app.py#L472) | <code>        self.service.add(self.transaction())</code> | self.service.add 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [473](../주석코드/tests/test_budget_app.py#L473) | <code>        with self.store.path(&quot;transactions&quot;).open(&quot;a&quot;, encoding=&quot;utf-8&quot;) as stream:</code> | with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [474](../주석코드/tests/test_budget_app.py#L474) | <code>            stream.write(&quot;{bad trailing row\n&quot;)</code> | stream.write 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [475](../주석코드/tests/test_budget_app.py#L475) | <code>        # --limit 1은 두 번째 줄을 파싱하지 않아야 한다.</code> | 설명 주석입니다. --limit 1은 두 번째 줄을 파싱하지 않아야 한다. (Python 실행에는 영향을 주지 않습니다.) |
| [476](../주석코드/tests/test_budget_app.py#L476) | <code>        code, out, _ = self.run_cli(&quot;list&quot;, &quot;--limit&quot;, &quot;1&quot;)</code> | --limit 1은 두 번째 줄을 파싱하지 않아야 한다. / 오른쪽 계산/호출 결과를 (code, out, _)에 저장합니다. |
| [477](../주석코드/tests/test_budget_app.py#L477) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [478](../주석코드/tests/test_budget_app.py#L478) | <code>        self.assertEqual(code, 0)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [479](../주석코드/tests/test_budget_app.py#L479) | <code>        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.</code> | 설명 주석입니다. 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [480](../주석코드/tests/test_budget_app.py#L480) | <code>        self.assertIn(&quot;1건&quot;, out)</code> | 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다. / 테스트 검증 메서드 self.assertIn를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [481](../주석코드/tests/test_budget_app.py#L481) | <code>        # 실제 값과 기대값이 같아야 통과합니다.</code> | 설명 주석입니다. 실제 값과 기대값이 같아야 통과합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [482](../주석코드/tests/test_budget_app.py#L482) | <code>        self.assertEqual(self.run_cli(&quot;list&quot;, &quot;--limit&quot;, &quot;2&quot;)[0], 1)</code> | 실제 값과 기대값이 같아야 통과합니다. / 테스트 검증 메서드 self.assertEqual를 호출합니다. 기대와 다르면 테스트를 실패 처리합니다. |
| [483](../주석코드/tests/test_budget_app.py#L483) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [484](../주석코드/tests/test_budget_app.py#L484) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [485](../주석코드/tests/test_budget_app.py#L485) | <code>if __name__ == &quot;__main__&quot;:</code> | 조건 __name__ == &#x27;__main__&#x27;가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [486](../주석코드/tests/test_budget_app.py#L486) | <code>    unittest.main()</code> | unittest.main 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
