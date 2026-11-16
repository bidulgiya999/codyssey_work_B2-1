# budget_app/storage.py 한 줄씩 설명

대상: [주석 코드](../주석코드/budget_app/storage.py). 총 205줄입니다. 줄 번호는 이 사본과 일치합니다. 설명은 읽기 자료이며 실행할 명령이 아닙니다.

| 줄 | 실제 코드 | 설명 |
| ---: | --- | --- |
| [1](../주석코드/budget_app/storage.py#L1) | <code># 저장소 계층: JSONL 읽기·쓰기, 초기화, 잠금, 원자적 교체를 담당합니다.</code> | 설명 주석입니다. 저장소 계층: JSONL 읽기·쓰기, 초기화, 잠금, 원자적 교체를 담당합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [2](../주석코드/budget_app/storage.py#L2) | <code># 거래 전체를 배열로 올리지 않고 제너레이터로 순서대로 처리합니다.</code> | 설명 주석입니다. 거래 전체를 배열로 올리지 않고 제너레이터로 순서대로 처리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [3](../주석코드/budget_app/storage.py#L3) | <code>&quot;&quot;&quot;줄 단위 JSONL 스트리밍, 잠금, 원자적 파일 교체.&quot;&quot;&quot;</code> | 거래 전체를 배열로 올리지 않고 제너레이터로 순서대로 처리합니다. / 파일/클래스/함수의 목적을 적은 문서 문자열(docstring)입니다. |
| [4](../주석코드/budget_app/storage.py#L4) | <code># 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다.</code> | 설명 주석입니다. 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [5](../주석코드/budget_app/storage.py#L5) | <code>from __future__ import annotations</code> | 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다. / __future__에서 필요한 이름을 가져옵니다. |
| [6](../주석코드/budget_app/storage.py#L6) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [7](../주석코드/budget_app/storage.py#L7) | <code># JSONL의 한 줄을 dict로 읽거나 JSON 문자열로 저장합니다.</code> | 설명 주석입니다. JSONL의 한 줄을 dict로 읽거나 JSON 문자열로 저장합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [8](../주석코드/budget_app/storage.py#L8) | <code>import json</code> | JSONL의 한 줄을 dict로 읽거나 JSON 문자열로 저장합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [9](../주석코드/budget_app/storage.py#L9) | <code># 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다.</code> | 설명 주석입니다. 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [10](../주석코드/budget_app/storage.py#L10) | <code>import os</code> | 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [11](../주석코드/budget_app/storage.py#L11) | <code># 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다.</code> | 설명 주석입니다. 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [12](../주석코드/budget_app/storage.py#L12) | <code>import tempfile</code> | 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다. / 표준 라이브러리 모듈을 가져와 이후 코드에서 사용합니다. |
| [13](../주석코드/budget_app/storage.py#L13) | <code># yield가 있는 함수를 with로 쓰는 컨텍스트 관리자로 바꿉니다.</code> | 설명 주석입니다. yield가 있는 함수를 with로 쓰는 컨텍스트 관리자로 바꿉니다. (Python 실행에는 영향을 주지 않습니다.) |
| [14](../주석코드/budget_app/storage.py#L14) | <code>from contextlib import contextmanager</code> | yield가 있는 함수를 with로 쓰는 컨텍스트 관리자로 바꿉니다. / contextlib에서 필요한 이름을 가져옵니다. |
| [15](../주석코드/budget_app/storage.py#L15) | <code># 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다.</code> | 설명 주석입니다. 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [16](../주석코드/budget_app/storage.py#L16) | <code>from pathlib import Path</code> | 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다. / pathlib에서 필요한 이름을 가져옵니다. |
| [17](../주석코드/budget_app/storage.py#L17) | <code># 레코드 값·순회 입력·제너레이터 반환·텍스트 스트림의 타입 계약입니다.</code> | 설명 주석입니다. 레코드 값·순회 입력·제너레이터 반환·텍스트 스트림의 타입 계약입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [18](../주석코드/budget_app/storage.py#L18) | <code>from typing import Any, Iterable, Iterator, TextIO</code> | 레코드 값·순회 입력·제너레이터 반환·텍스트 스트림의 타입 계약입니다. / typing에서 필요한 이름을 가져옵니다. |
| [19](../주석코드/budget_app/storage.py#L19) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [20](../주석코드/budget_app/storage.py#L20) | <code># 거래 모델 검증과 사용자 오류 정보를 저장소에서도 같은 계약으로 사용합니다.</code> | 설명 주석입니다. 거래 모델 검증과 사용자 오류 정보를 저장소에서도 같은 계약으로 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [21](../주석코드/budget_app/storage.py#L21) | <code>from .models import AppError, Transaction</code> | 거래 모델 검증과 사용자 오류 정보를 저장소에서도 같은 계약으로 사용합니다. / models에서 필요한 이름을 가져옵니다. |
| [22](../주석코드/budget_app/storage.py#L22) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [23](../주석코드/budget_app/storage.py#L23) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [24](../주석코드/budget_app/storage.py#L24) | <code>@contextmanager</code> | 바로 아래 함수/클래스에 contextmanager 데코레이터를 적용합니다. 중간 설명 주석은 적용 대상을 바꾸지 않습니다. |
| [25](../주석코드/budget_app/storage.py#L25) | <code># with 문에 쓰기 스트림을 제공하고 정상 완료할 때만 임시 파일을 원본과 교체합니다.</code> | 설명 주석입니다. with 문에 쓰기 스트림을 제공하고 정상 완료할 때만 임시 파일을 원본과 교체합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [26](../주석코드/budget_app/storage.py#L26) | <code>def atomic_text(path: Path, *, newline: str &#124; None = None) -&gt; Iterator[TextIO]:</code> | with 문에 쓰기 스트림을 제공하고 정상 완료할 때만 임시 파일을 원본과 교체합니다. / atomic_text 함수를 정의합니다. 인자: path, newline. 반환 타입: Iterator[TextIO]. def 자체는 본문을 실행하지 않습니다. |
| [27](../주석코드/budget_app/storage.py#L27) | <code>    &quot;&quot;&quot;대상과 같은 폴더에 쓰고 flush/fsync 후 교체. 실패 시 원본 유지.&quot;&quot;&quot;</code> | 파일/클래스/함수의 목적을 적은 문서 문자열(docstring)입니다. |
| [28](../주석코드/budget_app/storage.py#L28) | <code>    # 같은 파일시스템에서 교체하도록 원본의 부모 폴더에 고유 임시 파일을 만듭니다.</code> | 설명 주석입니다. 같은 파일시스템에서 교체하도록 원본의 부모 폴더에 고유 임시 파일을 만듭니다. (Python 실행에는 영향을 주지 않습니다.) |
| [29](../주석코드/budget_app/storage.py#L29) | <code>    fd, temporary = tempfile.mkstemp(prefix=&quot;.budget-&quot;, suffix=&quot;.tmp&quot;, dir=path.parent)</code> | 같은 파일시스템에서 교체하도록 원본의 부모 폴더에 고유 임시 파일을 만듭니다. / 오른쪽 계산/호출 결과를 (fd, temporary)에 저장합니다. |
| [30](../주석코드/budget_app/storage.py#L30) | <code>    try:</code> | 오류가 발생할 수 있는 처리를 시작합니다. 해당 except/finally에서 오류 안내와 정리를 처리합니다. |
| [31](../주석코드/budget_app/storage.py#L31) | <code>        # mkstemp가 준 파일 디스크립터를 UTF-8 텍스트 스트림으로 엽니다.</code> | 설명 주석입니다. mkstemp가 준 파일 디스크립터를 UTF-8 텍스트 스트림으로 엽니다. (Python 실행에는 영향을 주지 않습니다.) |
| [32](../주석코드/budget_app/storage.py#L32) | <code>        with os.fdopen(fd, &quot;w&quot;, encoding=&quot;utf-8&quot;, newline=newline) as stream:</code> | mkstemp가 준 파일 디스크립터를 UTF-8 텍스트 스트림으로 엽니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [33](../주석코드/budget_app/storage.py#L33) | <code>            # 호출자의 with 블록으로 스트림을 빌려줍니다. 블록에서 오류가 나면 아래 교체는 건너뜁니다.</code> | 설명 주석입니다. 호출자의 with 블록으로 스트림을 빌려줍니다. 블록에서 오류가 나면 아래 교체는 건너뜁니다. (Python 실행에는 영향을 주지 않습니다.) |
| [34](../주석코드/budget_app/storage.py#L34) | <code>            yield stream</code> | 호출자의 with 블록으로 스트림을 빌려줍니다. 블록에서 오류가 나면 아래 교체는 건너뜁니다. / 호출자에게 stream을 전달하고 잠시 멈춥니다. 다음 요청/컨텍스트 종료 시 이 지점 뒤에서 이어집니다. |
| [35](../주석코드/budget_app/storage.py#L35) | <code>            # Python 버퍼의 내용을 운영체제로 보냅니다.</code> | 설명 주석입니다. Python 버퍼의 내용을 운영체제로 보냅니다. (Python 실행에는 영향을 주지 않습니다.) |
| [36](../주석코드/budget_app/storage.py#L36) | <code>            stream.flush()</code> | Python 버퍼의 내용을 운영체제로 보냅니다. / stream.flush 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [37](../주석코드/budget_app/storage.py#L37) | <code>            # 운영체제에 해당 파일의 기록을 저장장치로 동기화하도록 요청합니다.</code> | 설명 주석입니다. 운영체제에 해당 파일의 기록을 저장장치로 동기화하도록 요청합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [38](../주석코드/budget_app/storage.py#L38) | <code>            os.fsync(stream.fileno())</code> | 운영체제에 해당 파일의 기록을 저장장치로 동기화하도록 요청합니다. / os.fsync 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [39](../주석코드/budget_app/storage.py#L39) | <code>        # 쓰기와 닫기가 모두 끝난 뒤에만 이름을 교체합니다. 원본을 먼저 지우지 않습니다.</code> | 설명 주석입니다. 쓰기와 닫기가 모두 끝난 뒤에만 이름을 교체합니다. 원본을 먼저 지우지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [40](../주석코드/budget_app/storage.py#L40) | <code>        os.replace(temporary, path)</code> | 쓰기와 닫기가 모두 끝난 뒤에만 이름을 교체합니다. 원본을 먼저 지우지 않습니다. / os.replace 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [41](../주석코드/budget_app/storage.py#L41) | <code>    finally:</code> | try 처리의 성공 여부와 관계없이 실행할 정리/로그 구간입니다. 프로세스 강제 종료까지 보장하는 것은 아닙니다. |
| [42](../주석코드/budget_app/storage.py#L42) | <code>        # 성공이면 이미 옮겨져 없고, 실패면 남은 임시 파일을 정리합니다.</code> | 설명 주석입니다. 성공이면 이미 옮겨져 없고, 실패면 남은 임시 파일을 정리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [43](../주석코드/budget_app/storage.py#L43) | <code>        Path(temporary).unlink(missing_ok=True)</code> | 성공이면 이미 옮겨져 없고, 실패면 남은 임시 파일을 정리합니다. / Path(temporary).unlink 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [44](../주석코드/budget_app/storage.py#L44) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [45](../주석코드/budget_app/storage.py#L45) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [46](../주석코드/budget_app/storage.py#L46) | <code># R(Read)의 기반: 줄 단위로 JSON 객체를 해석해 yield하는 제너레이터입니다.</code> | 설명 주석입니다. R(Read)의 기반: 줄 단위로 JSON 객체를 해석해 yield하는 제너레이터입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [47](../주석코드/budget_app/storage.py#L47) | <code>def read_jsonl(path: Path) -&gt; Iterator[dict[str, Any]]:</code> | R(Read)의 기반: 줄 단위로 JSON 객체를 해석해 yield하는 제너레이터입니다. / read_jsonl 함수를 정의합니다. 인자: path. 반환 타입: Iterator[dict[str, Any]]. def 자체는 본문을 실행하지 않습니다. |
| [48](../주석코드/budget_app/storage.py#L48) | <code>    # with를 벗어나면 읽기 파일을 닫습니다.</code> | 설명 주석입니다. with를 벗어나면 읽기 파일을 닫습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [49](../주석코드/budget_app/storage.py#L49) | <code>    with path.open(encoding=&quot;utf-8&quot;) as stream:</code> | with를 벗어나면 읽기 파일을 닫습니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [50](../주석코드/budget_app/storage.py#L50) | <code>        # 파일 객체 반복은 줄 단위 읽기입니다. 1부터 센 줄 번호로 손상 위치를 안내합니다.</code> | 설명 주석입니다. 파일 객체 반복은 줄 단위 읽기입니다. 1부터 센 줄 번호로 손상 위치를 안내합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [51](../주석코드/budget_app/storage.py#L51) | <code>        for number, line in enumerate(stream, 1):</code> | 파일 객체 반복은 줄 단위 읽기입니다. 1부터 센 줄 번호로 손상 위치를 안내합니다. / enumerate(stream, 1)에서 값을 하나씩 받아 (number, line)에 넣고 블록을 반복합니다. |
| [52](../주석코드/budget_app/storage.py#L52) | <code>            try:</code> | 오류가 발생할 수 있는 처리를 시작합니다. 해당 except/finally에서 오류 안내와 정리를 처리합니다. |
| [53](../주석코드/budget_app/storage.py#L53) | <code>                # JSONL의 한 줄을 Python 값으로 해석합니다.</code> | 설명 주석입니다. JSONL의 한 줄을 Python 값으로 해석합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [54](../주석코드/budget_app/storage.py#L54) | <code>                row = json.loads(line)</code> | JSONL의 한 줄을 Python 값으로 해석합니다. / 오른쪽 계산/호출 결과를 row에 저장합니다. |
| [55](../주석코드/budget_app/storage.py#L55) | <code>                # 숫자·배열 같은 JSON도 유효한 문법이지만 저장 레코드 스키마로는 거부합니다.</code> | 설명 주석입니다. 숫자·배열 같은 JSON도 유효한 문법이지만 저장 레코드 스키마로는 거부합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [56](../주석코드/budget_app/storage.py#L56) | <code>                if not isinstance(row, dict):</code> | 숫자·배열 같은 JSON도 유효한 문법이지만 저장 레코드 스키마로는 거부합니다. / 조건 not isinstance(row, dict)가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [57](../주석코드/budget_app/storage.py#L57) | <code>                    raise ValueError(&quot;JSON 객체가 아닙니다&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [58](../주석코드/budget_app/storage.py#L58) | <code>            except (ValueError, TypeError) as exc:</code> | 앞선 try에서 해당 종류의 예외가 발생했을 때 처리할 분기입니다. as 이름이 있으면 예외 객체를 그 이름으로 받습니다. |
| [59](../주석코드/budget_app/storage.py#L59) | <code>                raise AppError(f&quot;{path.name}:{number} 저장 데이터 오류: {exc}&quot;,</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [60](../주석코드/budget_app/storage.py#L60) | <code>                               &quot;원본을 백업한 뒤 해당 줄을 복구하세요. 파일을 자동 초기화하지 않습니다.&quot;) from None</code> | 59행에서 시작한 Raise 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [61](../주석코드/budget_app/storage.py#L61) | <code>            # 한 건만 전달하고 다음 요청까지 멈춥니다. 전체 레코드 리스트를 만들지 않습니다.</code> | 설명 주석입니다. 한 건만 전달하고 다음 요청까지 멈춥니다. 전체 레코드 리스트를 만들지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [62](../주석코드/budget_app/storage.py#L62) | <code>            yield row</code> | 한 건만 전달하고 다음 요청까지 멈춥니다. 전체 레코드 리스트를 만들지 않습니다. / 호출자에게 row을 전달하고 잠시 멈춥니다. 다음 요청/컨텍스트 종료 시 이 지점 뒤에서 이어집니다. |
| [63](../주석코드/budget_app/storage.py#L63) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [64](../주석코드/budget_app/storage.py#L64) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [65](../주석코드/budget_app/storage.py#L65) | <code># 객체들을 JSON 한 줄씩 써서 저장합니다. 입력 Iterable을 전체 리스트로 만들지 않습니다.</code> | 설명 주석입니다. 객체들을 JSON 한 줄씩 써서 저장합니다. 입력 Iterable을 전체 리스트로 만들지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [66](../주석코드/budget_app/storage.py#L66) | <code>def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -&gt; None:</code> | 객체들을 JSON 한 줄씩 써서 저장합니다. 입력 Iterable을 전체 리스트로 만들지 않습니다. / write_jsonl 함수를 정의합니다. 인자: path, records. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [67](../주석코드/budget_app/storage.py#L67) | <code>    # 한 줄이라도 직렬화/쓰기 실패 시 기존 파일을 유지하는 공통 저장 경로입니다.</code> | 설명 주석입니다. 한 줄이라도 직렬화/쓰기 실패 시 기존 파일을 유지하는 공통 저장 경로입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [68](../주석코드/budget_app/storage.py#L68) | <code>    with atomic_text(path) as stream:</code> | 한 줄이라도 직렬화/쓰기 실패 시 기존 파일을 유지하는 공통 저장 경로입니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [69](../주석코드/budget_app/storage.py#L69) | <code>        # 호출자가 넘긴 리스트 또는 제너레이터를 한 건씩 소비합니다.</code> | 설명 주석입니다. 호출자가 넘긴 리스트 또는 제너레이터를 한 건씩 소비합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [70](../주석코드/budget_app/storage.py#L70) | <code>        for row in records:</code> | 호출자가 넘긴 리스트 또는 제너레이터를 한 건씩 소비합니다. / records에서 값을 하나씩 받아 row에 넣고 블록을 반복합니다. |
| [71](../주석코드/budget_app/storage.py#L71) | <code>            # 한글을 그대로 기록하고 각 JSON 객체 끝에 개행을 붙입니다.</code> | 설명 주석입니다. 한글을 그대로 기록하고 각 JSON 객체 끝에 개행을 붙입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [72](../주석코드/budget_app/storage.py#L72) | <code>            stream.write(json.dumps(row, ensure_ascii=False) + &quot;\n&quot;)</code> | 한글을 그대로 기록하고 각 JSON 객체 끝에 개행을 붙입니다. / stream.write 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [73](../주석코드/budget_app/storage.py#L73) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [74](../주석코드/budget_app/storage.py#L74) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [75](../주석코드/budget_app/storage.py#L75) | <code># 데이터 폴더, 세 저장 파일, 초기 카테고리와 명령 단위 잠금을 관리합니다.</code> | 설명 주석입니다. 데이터 폴더, 세 저장 파일, 초기 카테고리와 명령 단위 잠금을 관리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [76](../주석코드/budget_app/storage.py#L76) | <code>class DataStore:</code> | 데이터 폴더, 세 저장 파일, 초기 카테고리와 명령 단위 잠금을 관리합니다. / DataStore 클래스의 정의를 시작합니다. 들여쓴 메서드와 속성이 이 클래스에 속합니다. |
| [77](../주석코드/budget_app/storage.py#L77) | <code>    # 과제의 세 영구 저장 파일입니다. 백업도 이 목록을 그대로 사용합니다.</code> | 설명 주석입니다. 과제의 세 영구 저장 파일입니다. 백업도 이 목록을 그대로 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [78](../주석코드/budget_app/storage.py#L78) | <code>    FILES = (&quot;transactions.jsonl&quot;, &quot;categories.jsonl&quot;, &quot;budgets.jsonl&quot;)</code> | 과제의 세 영구 저장 파일입니다. 백업도 이 목록을 그대로 사용합니다. / 오른쪽 계산/호출 결과를 FILES에 저장합니다. |
| [79](../주석코드/budget_app/storage.py#L79) | <code>    # 카테고리 파일이 없거나 0바이트일 때 사용할 초기 목록입니다.</code> | 설명 주석입니다. 카테고리 파일이 없거나 0바이트일 때 사용할 초기 목록입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [80](../주석코드/budget_app/storage.py#L80) | <code>    DEFAULT_CATEGORIES = (&quot;food&quot;, &quot;transport&quot;, &quot;rent&quot;, &quot;salary&quot;, &quot;etc&quot;)</code> | 카테고리 파일이 없거나 0바이트일 때 사용할 초기 목록입니다. / 오른쪽 계산/호출 결과를 DEFAULT_CATEGORIES에 저장합니다. |
| [81](../주석코드/budget_app/storage.py#L81) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [82](../주석코드/budget_app/storage.py#L82) | <code>    # 상대 경로를 절대 경로로 정규화합니다. 이 단계에서는 파일을 만들지 않습니다.</code> | 설명 주석입니다. 상대 경로를 절대 경로로 정규화합니다. 이 단계에서는 파일을 만들지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [83](../주석코드/budget_app/storage.py#L83) | <code>    def __init__(self, directory: Path) -&gt; None:</code> | 상대 경로를 절대 경로로 정규화합니다. 이 단계에서는 파일을 만들지 않습니다. / __init__ 함수를 정의합니다. 인자: self, directory. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [84](../주석코드/budget_app/storage.py#L84) | <code>        # 이후 경로 비교와 파일 접근에서 동일한 절대 경로 기준을 사용합니다.</code> | 설명 주석입니다. 이후 경로 비교와 파일 접근에서 동일한 절대 경로 기준을 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [85](../주석코드/budget_app/storage.py#L85) | <code>        self.directory = directory.resolve()</code> | 이후 경로 비교와 파일 접근에서 동일한 절대 경로 기준을 사용합니다. / 오른쪽 계산/호출 결과를 self.directory에 저장합니다. |
| [86](../주석코드/budget_app/storage.py#L86) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [87](../주석코드/budget_app/storage.py#L87) | <code>    @contextmanager</code> | 바로 아래 함수/클래스에 contextmanager 데코레이터를 적용합니다. 중간 설명 주석은 적용 대상을 바꾸지 않습니다. |
| [88](../주석코드/budget_app/storage.py#L88) | <code>    # 명령 실행 동안 잠금을 보유합니다. 초기화 후 제어를 넘기고 마지막에 잠금을 해제합니다.</code> | 설명 주석입니다. 명령 실행 동안 잠금을 보유합니다. 초기화 후 제어를 넘기고 마지막에 잠금을 해제합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [89](../주석코드/budget_app/storage.py#L89) | <code>    def session(self) -&gt; Iterator[None]:</code> | 명령 실행 동안 잠금을 보유합니다. 초기화 후 제어를 넘기고 마지막에 잠금을 해제합니다. / session 함수를 정의합니다. 인자: self. 반환 타입: Iterator[None]. def 자체는 본문을 실행하지 않습니다. |
| [90](../주석코드/budget_app/storage.py#L90) | <code>        &quot;&quot;&quot;모든 CLI 명령의 일관된 스냅샷 및 동시 쓰기 유실 방지.&quot;&quot;&quot;</code> | 파일/클래스/함수의 목적을 적은 문서 문자열(docstring)입니다. |
| [91](../주석코드/budget_app/storage.py#L91) | <code>        # 최초 실행이라도 부모 폴더까지 만들고, 이미 있으면 그대로 사용합니다.</code> | 설명 주석입니다. 최초 실행이라도 부모 폴더까지 만들고, 이미 있으면 그대로 사용합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [92](../주석코드/budget_app/storage.py#L92) | <code>        self.directory.mkdir(parents=True, exist_ok=True)</code> | 최초 실행이라도 부모 폴더까지 만들고, 이미 있으면 그대로 사용합니다. / self.directory.mkdir 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [93](../주석코드/budget_app/storage.py#L93) | <code>        # 거래뿐 아니라 메타데이터도 같은 명령 단위 잠금으로 보호합니다.</code> | 설명 주석입니다. 거래뿐 아니라 메타데이터도 같은 명령 단위 잠금으로 보호합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [94](../주석코드/budget_app/storage.py#L94) | <code>        lock = self.directory / &quot;.budget.lock&quot;</code> | 거래뿐 아니라 메타데이터도 같은 명령 단위 잠금으로 보호합니다. / 오른쪽 계산/호출 결과를 lock에 저장합니다. |
| [95](../주석코드/budget_app/storage.py#L95) | <code>        try:</code> | 오류가 발생할 수 있는 처리를 시작합니다. 해당 except/finally에서 오류 안내와 정리를 처리합니다. |
| [96](../주석코드/budget_app/storage.py#L96) | <code>            # O_EXCL로 이미 잠금이 있으면 실패시켜 두 명령의 동시 진입을 막습니다.</code> | 설명 주석입니다. O_EXCL로 이미 잠금이 있으면 실패시켜 두 명령의 동시 진입을 막습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [97](../주석코드/budget_app/storage.py#L97) | <code>            fd = os.open(lock, os.O_CREAT &#124; os.O_EXCL &#124; os.O_WRONLY, 0o600)</code> | O_EXCL로 이미 잠금이 있으면 실패시켜 두 명령의 동시 진입을 막습니다. / 오른쪽 계산/호출 결과를 fd에 저장합니다. |
| [98](../주석코드/budget_app/storage.py#L98) | <code>        # 충돌이나 비정상 종료 후 남은 잠금은 자동 삭제하지 않고 사용자에게 안내합니다.</code> | 설명 주석입니다. 충돌이나 비정상 종료 후 남은 잠금은 자동 삭제하지 않고 사용자에게 안내합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [99](../주석코드/budget_app/storage.py#L99) | <code>        except FileExistsError:</code> | 앞선 try에서 해당 종류의 예외가 발생했을 때 처리할 분기입니다. as 이름이 있으면 예외 객체를 그 이름으로 받습니다. |
| [100](../주석코드/budget_app/storage.py#L100) | <code>            raise AppError(&quot;다른 가계부 명령이 실행 중이거나 잠금 파일이 남아 있습니다.&quot;,</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [101](../주석코드/budget_app/storage.py#L101) | <code>                           f&quot;다른 프로세스 종료를 확인하세요. 비정상 종료였다면 {lock}을 삭제하세요.&quot;) from None</code> | 100행에서 시작한 Raise 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [102](../주석코드/budget_app/storage.py#L102) | <code>        try:</code> | 오류가 발생할 수 있는 처리를 시작합니다. 해당 except/finally에서 오류 안내와 정리를 처리합니다. |
| [103](../주석코드/budget_app/storage.py#L103) | <code>            # 잠금을 잡은 프로세스 id를 기록해 운영 중 확인에 도움을 줍니다.</code> | 설명 주석입니다. 잠금을 잡은 프로세스 id를 기록해 운영 중 확인에 도움을 줍니다. (Python 실행에는 영향을 주지 않습니다.) |
| [104](../주석코드/budget_app/storage.py#L104) | <code>            with os.fdopen(fd, &quot;w&quot;, encoding=&quot;utf-8&quot;) as stream:</code> | 잠금을 잡은 프로세스 id를 기록해 운영 중 확인에 도움을 줍니다. / with로 자원을 사용하며 정상/예외 종료 시 정리 작업이 실행되도록 합니다. 컨텍스트 관리자가 진입·종료를 담당합니다. |
| [105](../주석코드/budget_app/storage.py#L105) | <code>                # 이 값은 진단용입니다. 잠금의 핵심은 O_EXCL로 생성한 파일의 존재입니다.</code> | 설명 주석입니다. 이 값은 진단용입니다. 잠금의 핵심은 O_EXCL로 생성한 파일의 존재입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [106](../주석코드/budget_app/storage.py#L106) | <code>                stream.write(str(os.getpid()))</code> | 이 값은 진단용입니다. 잠금의 핵심은 O_EXCL로 생성한 파일의 존재입니다. / stream.write 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [107](../주석코드/budget_app/storage.py#L107) | <code>            # 초기화는 세 파일 각각에 대해 수행합니다.</code> | 설명 주석입니다. 초기화는 세 파일 각각에 대해 수행합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [108](../주석코드/budget_app/storage.py#L108) | <code>            for name in self.FILES:</code> | 초기화는 세 파일 각각에 대해 수행합니다. / self.FILES에서 값을 하나씩 받아 name에 넣고 블록을 반복합니다. |
| [109](../주석코드/budget_app/storage.py#L109) | <code>                path = self.directory / name</code> | 오른쪽 계산/호출 결과를 path에 저장합니다. |
| [110](../주석코드/budget_app/storage.py#L110) | <code>                # 기존 파일을 빈 파일로 덮어쓰지 않고, 없는 파일만 생성합니다.</code> | 설명 주석입니다. 기존 파일을 빈 파일로 덮어쓰지 않고, 없는 파일만 생성합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [111](../주석코드/budget_app/storage.py#L111) | <code>                if not path.exists():</code> | 기존 파일을 빈 파일로 덮어쓰지 않고, 없는 파일만 생성합니다. / 조건 not path.exists()가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [112](../주석코드/budget_app/storage.py#L112) | <code>                    # 빈 Iterable을 저장해 빈 JSONL 파일을 만듭니다.</code> | 설명 주석입니다. 빈 Iterable을 저장해 빈 JSONL 파일을 만듭니다. (Python 실행에는 영향을 주지 않습니다.) |
| [113](../주석코드/budget_app/storage.py#L113) | <code>                    write_jsonl(path, ())</code> | 빈 Iterable을 저장해 빈 JSONL 파일을 만듭니다. / write_jsonl 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [114](../주석코드/budget_app/storage.py#L114) | <code>            # 0바이트일 때만 기본 카테고리를 생성합니다. 깨진 JSON은 자동 초기화하지 않습니다.</code> | 설명 주석입니다. 0바이트일 때만 기본 카테고리를 생성합니다. 깨진 JSON은 자동 초기화하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [115](../주석코드/budget_app/storage.py#L115) | <code>            if self.path(&quot;categories&quot;).stat().st_size == 0:</code> | 0바이트일 때만 기본 카테고리를 생성합니다. 깨진 JSON은 자동 초기화하지 않습니다. / 조건 self.path(&#x27;categories&#x27;).stat().st_size == 0가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [116](../주석코드/budget_app/storage.py#L116) | <code>                write_jsonl(self.path(&quot;categories&quot;), ({&quot;name&quot;: n} for n in self.DEFAULT_CATEGORIES))</code> | write_jsonl 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [117](../주석코드/budget_app/storage.py#L117) | <code>            # 호출자의 명령 실행 구간으로 제어를 넘깁니다. 그동안 잠금은 유지됩니다.</code> | 설명 주석입니다. 호출자의 명령 실행 구간으로 제어를 넘깁니다. 그동안 잠금은 유지됩니다. (Python 실행에는 영향을 주지 않습니다.) |
| [118](../주석코드/budget_app/storage.py#L118) | <code>            yield</code> | 호출자의 명령 실행 구간으로 제어를 넘깁니다. 그동안 잠금은 유지됩니다. / 호출자에게 제어권을 전달하고 잠시 멈춥니다. 다음 요청/컨텍스트 종료 시 이 지점 뒤에서 이어집니다. |
| [119](../주석코드/budget_app/storage.py#L119) | <code>        finally:</code> | try 처리의 성공 여부와 관계없이 실행할 정리/로그 구간입니다. 프로세스 강제 종료까지 보장하는 것은 아닙니다. |
| [120](../주석코드/budget_app/storage.py#L120) | <code>            # 정상 종료와 예상 예외 모두 finally를 거치며 잠금 파일을 해제합니다.</code> | 설명 주석입니다. 정상 종료와 예상 예외 모두 finally를 거치며 잠금 파일을 해제합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [121](../주석코드/budget_app/storage.py#L121) | <code>            lock.unlink(missing_ok=True)</code> | 정상 종료와 예상 예외 모두 finally를 거치며 잠금 파일을 해제합니다. / lock.unlink 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
| [122](../주석코드/budget_app/storage.py#L122) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [123](../주석코드/budget_app/storage.py#L123) | <code>    # 논리 이름 transactions/categories/budgets를 실제 JSONL 파일 경로로 바꿉니다.</code> | 설명 주석입니다. 논리 이름 transactions/categories/budgets를 실제 JSONL 파일 경로로 바꿉니다. (Python 실행에는 영향을 주지 않습니다.) |
| [124](../주석코드/budget_app/storage.py#L124) | <code>    def path(self, name: str) -&gt; Path:</code> | 논리 이름 transactions/categories/budgets를 실제 JSONL 파일 경로로 바꿉니다. / path 함수를 정의합니다. 인자: self, name. 반환 타입: Path. def 자체는 본문을 실행하지 않습니다. |
| [125](../주석코드/budget_app/storage.py#L125) | <code>        # Path의 / 연산으로 운영체제 경로 구분자를 안전하게 조합합니다.</code> | 설명 주석입니다. Path의 / 연산으로 운영체제 경로 구분자를 안전하게 조합합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [126](../주석코드/budget_app/storage.py#L126) | <code>        return self.directory / (name + &quot;.jsonl&quot;)</code> | Path의 / 연산으로 운영체제 경로 구분자를 안전하게 조합합니다. / 호출자에게 self.directory / (name + &#x27;.jsonl&#x27;)을 반환하고 현재 함수 실행을 끝냅니다. |
| [127](../주석코드/budget_app/storage.py#L127) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [128](../주석코드/budget_app/storage.py#L128) | <code>    # CSV 내보내기가 실제 저장 파일이나 잠금 파일을 덮어쓰지 못하게 막습니다.</code> | 설명 주석입니다. CSV 내보내기가 실제 저장 파일이나 잠금 파일을 덮어쓰지 못하게 막습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [129](../주석코드/budget_app/storage.py#L129) | <code>    def protect_output(self, path: Path) -&gt; None:</code> | CSV 내보내기가 실제 저장 파일이나 잠금 파일을 덮어쓰지 못하게 막습니다. / protect_output 함수를 정의합니다. 인자: self, path. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [130](../주석코드/budget_app/storage.py#L130) | <code>        # 상대 경로나 심볼릭 링크를 정규화해 덮어쓰기 검사 우회를 줄입니다.</code> | 설명 주석입니다. 상대 경로나 심볼릭 링크를 정규화해 덮어쓰기 검사 우회를 줄입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [131](../주석코드/budget_app/storage.py#L131) | <code>        resolved = path.resolve()</code> | 상대 경로나 심볼릭 링크를 정규화해 덮어쓰기 검사 우회를 줄입니다. / 오른쪽 계산/호출 결과를 resolved에 저장합니다. |
| [132](../주석코드/budget_app/storage.py#L132) | <code>        # 거래·카테고리·예산 파일과 현재 명령의 잠금을 출력 경로에서 제외합니다.</code> | 설명 주석입니다. 거래·카테고리·예산 파일과 현재 명령의 잠금을 출력 경로에서 제외합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [133](../주석코드/budget_app/storage.py#L133) | <code>        protected = [self.directory / n for n in (*self.FILES, &quot;.budget.lock&quot;)]</code> | 거래·카테고리·예산 파일과 현재 명령의 잠금을 출력 경로에서 제외합니다. / 오른쪽 계산/호출 결과를 protected에 저장합니다. |
| [134](../주석코드/budget_app/storage.py#L134) | <code>        # 경로 문자열뿐 아니라 이미 존재하는 하드 링크의 같은 파일 여부도 검사합니다.</code> | 설명 주석입니다. 경로 문자열뿐 아니라 이미 존재하는 하드 링크의 같은 파일 여부도 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [135](../주석코드/budget_app/storage.py#L135) | <code>        if any(resolved == p or (resolved.exists() and p.exists() and os.path.samefile(resolved, p))</code> | 경로 문자열뿐 아니라 이미 존재하는 하드 링크의 같은 파일 여부도 검사합니다. / 조건 any((resolved == p or (resolved.exists() and p.exists() and os.path.samefile(resolved, p)) for p in protected))가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [136](../주석코드/budget_app/storage.py#L136) | <code>               for p in protected):</code> | 135행에서 시작한 If 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [137](../주석코드/budget_app/storage.py#L137) | <code>            raise AppError(&quot;가계부 저장 파일을 내보내기 대상으로 지정할 수 없습니다.&quot;, &quot;별도의 CSV 경로를 지정하세요.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [138](../주석코드/budget_app/storage.py#L138) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [139](../주석코드/budget_app/storage.py#L139) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [140](../주석코드/budget_app/storage.py#L140) | <code># 거래 파일의 정렬·조회·병합 재작성을 전담합니다. 카테고리 정책은 서비스 책임입니다.</code> | 설명 주석입니다. 거래 파일의 정렬·조회·병합 재작성을 전담합니다. 카테고리 정책은 서비스 책임입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [141](../주석코드/budget_app/storage.py#L141) | <code>class TransactionRepository:</code> | 거래 파일의 정렬·조회·병합 재작성을 전담합니다. 카테고리 정책은 서비스 책임입니다. / TransactionRepository 클래스의 정의를 시작합니다. 들여쓴 메서드와 속성이 이 클래스에 속합니다. |
| [142](../주석코드/budget_app/storage.py#L142) | <code>    # 처리할 거래 파일 경로를 보관합니다. 가져오기에서는 스테이징 경로도 사용할 수 있습니다.</code> | 설명 주석입니다. 처리할 거래 파일 경로를 보관합니다. 가져오기에서는 스테이징 경로도 사용할 수 있습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [143](../주석코드/budget_app/storage.py#L143) | <code>    def __init__(self, path: Path) -&gt; None:</code> | 처리할 거래 파일 경로를 보관합니다. 가져오기에서는 스테이징 경로도 사용할 수 있습니다. / __init__ 함수를 정의합니다. 인자: self, path. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [144](../주석코드/budget_app/storage.py#L144) | <code>        # 저장소는 거래 파일 하나의 경로만 알면 동작합니다.</code> | 설명 주석입니다. 저장소는 거래 파일 하나의 경로만 알면 동작합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [145](../주석코드/budget_app/storage.py#L145) | <code>        self.path = path</code> | 저장소는 거래 파일 하나의 경로만 알면 동작합니다. / 오른쪽 계산/호출 결과를 self.path에 저장합니다. |
| [146](../주석코드/budget_app/storage.py#L146) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [147](../주석코드/budget_app/storage.py#L147) | <code>    # 거래 한 건씩 복원하며 (date, id) 내림차순인지 검사합니다. 거래 전체를 정렬하지 않습니다.</code> | 설명 주석입니다. 거래 한 건씩 복원하며 (date, id) 내림차순인지 검사합니다. 거래 전체를 정렬하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [148](../주석코드/budget_app/storage.py#L148) | <code>    def iter_all(self) -&gt; Iterator[Transaction]:</code> | 거래 한 건씩 복원하며 (date, id) 내림차순인지 검사합니다. 거래 전체를 정렬하지 않습니다. / iter_all 함수를 정의합니다. 인자: self. 반환 타입: Iterator[Transaction]. def 자체는 본문을 실행하지 않습니다. |
| [149](../주석코드/budget_app/storage.py#L149) | <code>        &quot;&quot;&quot;파일은 (date, id) 내림차순. 한 번에 거래 한 건만 읽는다.&quot;&quot;&quot;</code> | 파일/클래스/함수의 목적을 적은 문서 문자열(docstring)입니다. |
| [150](../주석코드/budget_app/storage.py#L150) | <code>        # 직전 거래 키 하나만 기억해 정렬을 검사하므로 거래 건수만큼 메모리가 늘지 않습니다.</code> | 설명 주석입니다. 직전 거래 키 하나만 기억해 정렬을 검사하므로 거래 건수만큼 메모리가 늘지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [151](../주석코드/budget_app/storage.py#L151) | <code>        previous: tuple[str, str] &#124; None = None</code> | 직전 거래 키 하나만 기억해 정렬을 검사하므로 거래 건수만큼 메모리가 늘지 않습니다. / previous의 타입을 tuple[str, str] &#124; None로 명시하고 기본값을 설정합니다. |
| [152](../주석코드/budget_app/storage.py#L152) | <code>        for number, row in enumerate(read_jsonl(self.path), 1):</code> | enumerate(read_jsonl(self.path), 1)에서 값을 하나씩 받아 (number, row)에 넣고 블록을 반복합니다. |
| [153](../주석코드/budget_app/storage.py#L153) | <code>            try:</code> | 오류가 발생할 수 있는 처리를 시작합니다. 해당 except/finally에서 오류 안내와 정리를 처리합니다. |
| [154](../주석코드/budget_app/storage.py#L154) | <code>                # 파일의 dict도 모델 검증을 통과해야 거래로 전달합니다.</code> | 설명 주석입니다. 파일의 dict도 모델 검증을 통과해야 거래로 전달합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [155](../주석코드/budget_app/storage.py#L155) | <code>                transaction = Transaction.from_record(row)</code> | 파일의 dict도 모델 검증을 통과해야 거래로 전달합니다. / 오른쪽 계산/호출 결과를 transaction에 저장합니다. |
| [156](../주석코드/budget_app/storage.py#L156) | <code>            except (AppError, TypeError, ValueError, AttributeError) as exc:</code> | 앞선 try에서 해당 종류의 예외가 발생했을 때 처리할 분기입니다. as 이름이 있으면 예외 객체를 그 이름으로 받습니다. |
| [157](../주석코드/budget_app/storage.py#L157) | <code>                raise AppError(f&quot;{self.path.name}:{number} 거래 데이터 오류: {exc}&quot;,</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [158](../주석코드/budget_app/storage.py#L158) | <code>                               &quot;파일을 백업하고 해당 레코드를 복구하세요.&quot;) from None</code> | 157행에서 시작한 Raise 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [159](../주석코드/budget_app/storage.py#L159) | <code>            # 이전 값보다 작아야 내림차순입니다. 같은 정렬 키도 손상으로 거부합니다.</code> | 설명 주석입니다. 이전 값보다 작아야 내림차순입니다. 같은 정렬 키도 손상으로 거부합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [160](../주석코드/budget_app/storage.py#L160) | <code>            if previous is not None and transaction.key &gt;= previous:</code> | 이전 값보다 작아야 내림차순입니다. 같은 정렬 키도 손상으로 거부합니다. / 조건 previous is not None and transaction.key &gt;= previous가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [161](../주석코드/budget_app/storage.py#L161) | <code>                raise AppError(&quot;거래 파일의 최신순 정렬 또는 고유 키가 손상되었습니다.&quot;,</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [162](../주석코드/budget_app/storage.py#L162) | <code>                               &quot;백업 파일에서 복구하세요. 저장 파일을 직접 편집하지 마세요.&quot;)</code> | 161행에서 시작한 Raise 문장의 이어지는 줄입니다. 이 줄까지의 인자·식·괄호를 앞줄과 함께 해석합니다. 독립된 명령으로 실행하는 줄이 아닙니다. |
| [163](../주석코드/budget_app/storage.py#L163) | <code>            # 다음 거래와 비교할 기준만 갱신합니다.</code> | 설명 주석입니다. 다음 거래와 비교할 기준만 갱신합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [164](../주석코드/budget_app/storage.py#L164) | <code>            previous = transaction.key</code> | 다음 거래와 비교할 기준만 갱신합니다. / 오른쪽 계산/호출 결과를 previous에 저장합니다. |
| [165](../주석코드/budget_app/storage.py#L165) | <code>            # R(Read) 스트림을 서비스로 한 건씩 전달합니다.</code> | 설명 주석입니다. R(Read) 스트림을 서비스로 한 건씩 전달합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [166](../주석코드/budget_app/storage.py#L166) | <code>            yield transaction</code> | R(Read) 스트림을 서비스로 한 건씩 전달합니다. / 호출자에게 transaction을 전달하고 잠시 멈춥니다. 다음 요청/컨텍스트 종료 시 이 지점 뒤에서 이어집니다. |
| [167](../주석코드/budget_app/storage.py#L167) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [168](../주석코드/budget_app/storage.py#L168) | <code>    # R(Read): id가 같은 거래를 찾으면 반환하고, 끝까지 없으면 AppError를 발생시킵니다.</code> | 설명 주석입니다. R(Read): id가 같은 거래를 찾으면 반환하고, 끝까지 없으면 AppError를 발생시킵니다. (Python 실행에는 영향을 주지 않습니다.) |
| [169](../주석코드/budget_app/storage.py#L169) | <code>    def find(self, identifier: str) -&gt; Transaction:</code> | R(Read): id가 같은 거래를 찾으면 반환하고, 끝까지 없으면 AppError를 발생시킵니다. / find 함수를 정의합니다. 인자: self, identifier. 반환 타입: Transaction. def 자체는 본문을 실행하지 않습니다. |
| [170](../주석코드/budget_app/storage.py#L170) | <code>        # id 조회는 인덱스가 없으므로 앞에서부터 최대 n건을 검사합니다.</code> | 설명 주석입니다. id 조회는 인덱스가 없으므로 앞에서부터 최대 n건을 검사합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [171](../주석코드/budget_app/storage.py#L171) | <code>        for transaction in self.iter_all():</code> | id 조회는 인덱스가 없으므로 앞에서부터 최대 n건을 검사합니다. / self.iter_all()에서 값을 하나씩 받아 transaction에 넣고 블록을 반복합니다. |
| [172](../주석코드/budget_app/storage.py#L172) | <code>            # 다른 필드가 같아도 id가 같아야 같은 거래입니다.</code> | 설명 주석입니다. 다른 필드가 같아도 id가 같아야 같은 거래입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [173](../주석코드/budget_app/storage.py#L173) | <code>            if transaction.id == identifier:</code> | 다른 필드가 같아도 id가 같아야 같은 거래입니다. / 조건 transaction.id == identifier가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [174](../주석코드/budget_app/storage.py#L174) | <code>                # 첫 일치 거래를 반환합니다. 이후 레코드는 이 조회에서 필요하지 않습니다.</code> | 설명 주석입니다. 첫 일치 거래를 반환합니다. 이후 레코드는 이 조회에서 필요하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [175](../주석코드/budget_app/storage.py#L175) | <code>                return transaction</code> | 첫 일치 거래를 반환합니다. 이후 레코드는 이 조회에서 필요하지 않습니다. / 호출자에게 transaction을 반환하고 현재 함수 실행을 끝냅니다. |
| [176](../주석코드/budget_app/storage.py#L176) | <code>        raise AppError(f&quot;없는 데이터: {identifier}&quot;, &quot;list 또는 search로 거래 id를 확인하세요.&quot;)</code> | 예외를 발생시켜 정상 경로를 중단합니다. 상위 예외 처리 코드로 전달합니다. |
| [177](../주석코드/budget_app/storage.py#L177) | <code>(빈 줄)</code> | 빈 줄입니다. 실행 동작 없이 서로 다른 처리 단위를 구분합니다. |
| [178](../주석코드/budget_app/storage.py#L178) | <code>    # C/U/D가 공유하는 저장 연산입니다. 기존 거래를 순회하며 대상 제외 및 새 거래 삽입을 처리합니다.</code> | 설명 주석입니다. C/U/D가 공유하는 저장 연산입니다. 기존 거래를 순회하며 대상 제외 및 새 거래 삽입을 처리합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [179](../주석코드/budget_app/storage.py#L179) | <code>    def replace(self, identifier: str &#124; None = None,</code> | C/U/D가 공유하는 저장 연산입니다. 기존 거래를 순회하며 대상 제외 및 새 거래 삽입을 처리합니다. / replace 함수를 정의합니다. 인자: self, identifier, replacement. 반환 타입: None. def 자체는 본문을 실행하지 않습니다. |
| [180](../주석코드/budget_app/storage.py#L180) | <code>                replacement: Transaction &#124; None = None) -&gt; None:</code> | 179행에서 시작한 FunctionDef 문장의 이어지는 줄입니다. 인자·필드·조건식을 이어 적으며, 전체 문장이 완성되어야 하나의 처리로 해석됩니다. |
| [181](../주석코드/budget_app/storage.py#L181) | <code>        &quot;&quot;&quot;새 거래를 병합하며 스트리밍 재작성. 수정/삭제 대상은 건너뛴다.&quot;&quot;&quot;</code> | 파일/클래스/함수의 목적을 적은 문서 문자열(docstring)입니다. |
| [182](../주석코드/budget_app/storage.py#L182) | <code>        # 실제 교체 파일에 들어갈 dict들을 하나씩 생성하는 내부 제너레이터입니다.</code> | 설명 주석입니다. 실제 교체 파일에 들어갈 dict들을 하나씩 생성하는 내부 제너레이터입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [183](../주석코드/budget_app/storage.py#L183) | <code>        def records() -&gt; Iterator[dict[str, Any]]:</code> | 실제 교체 파일에 들어갈 dict들을 하나씩 생성하는 내부 제너레이터입니다. / records 함수를 정의합니다. 인자: 없음. 반환 타입: Iterator[dict[str, Any]]. def 자체는 본문을 실행하지 않습니다. |
| [184](../주석코드/budget_app/storage.py#L184) | <code>            # 아직 삽입하지 않은 새 거래입니다. 삭제 요청은 None이므로 삽입하지 않습니다.</code> | 설명 주석입니다. 아직 삽입하지 않은 새 거래입니다. 삭제 요청은 None이므로 삽입하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [185](../주석코드/budget_app/storage.py#L185) | <code>            pending = replacement</code> | 아직 삽입하지 않은 새 거래입니다. 삭제 요청은 None이므로 삽입하지 않습니다. / 오른쪽 계산/호출 결과를 pending에 저장합니다. |
| [186](../주석코드/budget_app/storage.py#L186) | <code>            # 기존 최신순을 유지하며 입력을 한 건씩 읽습니다.</code> | 설명 주석입니다. 기존 최신순을 유지하며 입력을 한 건씩 읽습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [187](../주석코드/budget_app/storage.py#L187) | <code>            for old in self.iter_all():</code> | 기존 최신순을 유지하며 입력을 한 건씩 읽습니다. / self.iter_all()에서 값을 하나씩 받아 old에 넣고 블록을 반복합니다. |
| [188](../주석코드/budget_app/storage.py#L188) | <code>                # U/D에서는 대상의 옛 버전을 제외합니다. C에서는 identifier=None이라 제외하지 않습니다.</code> | 설명 주석입니다. U/D에서는 대상의 옛 버전을 제외합니다. C에서는 identifier=None이라 제외하지 않습니다. (Python 실행에는 영향을 주지 않습니다.) |
| [189](../주석코드/budget_app/storage.py#L189) | <code>                if old.id == identifier:</code> | U/D에서는 대상의 옛 버전을 제외합니다. C에서는 identifier=None이라 제외하지 않습니다. / 조건 old.id == identifier가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [190](../주석코드/budget_app/storage.py#L190) | <code>                    # 대상 거래만 건너뛰며 나머지 레코드는 보존합니다.</code> | 설명 주석입니다. 대상 거래만 건너뛰며 나머지 레코드는 보존합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [191](../주석코드/budget_app/storage.py#L191) | <code>                    continue</code> | 대상 거래만 건너뛰며 나머지 레코드는 보존합니다. / 현재 반복의 남은 부분을 건너뛰고 다음 항목으로 이동합니다. |
| [192](../주석코드/budget_app/storage.py#L192) | <code>                # 새 거래가 현재 거래보다 최신이면 이 위치가 삽입 지점입니다.</code> | 설명 주석입니다. 새 거래가 현재 거래보다 최신이면 이 위치가 삽입 지점입니다. (Python 실행에는 영향을 주지 않습니다.) |
| [193](../주석코드/budget_app/storage.py#L193) | <code>                if pending is not None and pending.key &gt; old.key:</code> | 새 거래가 현재 거래보다 최신이면 이 위치가 삽입 지점입니다. / 조건 pending is not None and pending.key &gt; old.key가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [194](../주석코드/budget_app/storage.py#L194) | <code>                    # 새 거래를 한 번만 출력 파일 쪽으로 전달합니다.</code> | 설명 주석입니다. 새 거래를 한 번만 출력 파일 쪽으로 전달합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [195](../주석코드/budget_app/storage.py#L195) | <code>                    yield pending.record()</code> | 새 거래를 한 번만 출력 파일 쪽으로 전달합니다. / 호출자에게 pending.record()을 전달하고 잠시 멈춥니다. 다음 요청/컨텍스트 종료 시 이 지점 뒤에서 이어집니다. |
| [196](../주석코드/budget_app/storage.py#L196) | <code>                    # 이미 삽입한 거래를 뒤에서 다시 쓰지 않게 표시합니다.</code> | 설명 주석입니다. 이미 삽입한 거래를 뒤에서 다시 쓰지 않게 표시합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [197](../주석코드/budget_app/storage.py#L197) | <code>                    pending = None</code> | 이미 삽입한 거래를 뒤에서 다시 쓰지 않게 표시합니다. / 오른쪽 계산/호출 결과를 pending에 저장합니다. |
| [198](../주석코드/budget_app/storage.py#L198) | <code>                # 대상이 아닌 기존 거래는 필드를 바꾸지 않고 새 파일에 보존합니다.</code> | 설명 주석입니다. 대상이 아닌 기존 거래는 필드를 바꾸지 않고 새 파일에 보존합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [199](../주석코드/budget_app/storage.py#L199) | <code>                yield old.record()</code> | 대상이 아닌 기존 거래는 필드를 바꾸지 않고 새 파일에 보존합니다. / 호출자에게 old.record()을 전달하고 잠시 멈춥니다. 다음 요청/컨텍스트 종료 시 이 지점 뒤에서 이어집니다. |
| [200](../주석코드/budget_app/storage.py#L200) | <code>            # 반복이 끝날 때까지 삽입하지 못했다면 가장 오래된 거래이므로 마지막에 추가합니다.</code> | 설명 주석입니다. 반복이 끝날 때까지 삽입하지 못했다면 가장 오래된 거래이므로 마지막에 추가합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [201](../주석코드/budget_app/storage.py#L201) | <code>            if pending is not None:</code> | 반복이 끝날 때까지 삽입하지 못했다면 가장 오래된 거래이므로 마지막에 추가합니다. / 조건 pending is not None가 참일 때 바로 아래 들여쓴 블록을 실행합니다. |
| [202](../주석코드/budget_app/storage.py#L202) | <code>                # 새 거래를 한 번만 출력 파일 쪽으로 전달합니다.</code> | 설명 주석입니다. 새 거래를 한 번만 출력 파일 쪽으로 전달합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [203](../주석코드/budget_app/storage.py#L203) | <code>                yield pending.record()</code> | 새 거래를 한 번만 출력 파일 쪽으로 전달합니다. / 호출자에게 pending.record()을 전달하고 잠시 멈춥니다. 다음 요청/컨텍스트 종료 시 이 지점 뒤에서 이어집니다. |
| [204](../주석코드/budget_app/storage.py#L204) | <code>        # 내부 제너레이터가 끝까지 성공한 경우에만 거래 파일을 교체합니다.</code> | 설명 주석입니다. 내부 제너레이터가 끝까지 성공한 경우에만 거래 파일을 교체합니다. (Python 실행에는 영향을 주지 않습니다.) |
| [205](../주석코드/budget_app/storage.py#L205) | <code>        write_jsonl(self.path, records())</code> | 내부 제너레이터가 끝까지 성공한 경우에만 거래 파일을 교체합니다. / write_jsonl 함수를 호출합니다. 반환값을 변수에 대입하지 않고 호출의 처리 효과를 사용합니다. |
