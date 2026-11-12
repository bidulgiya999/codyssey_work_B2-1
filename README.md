# 파일 기반 콘솔 가계부

Python 3.10 이상과 **표준 라이브러리만** 사용하는 콘솔 가계부입니다. 별도의 `pip install`이 필요하지 않습니다. 거래 CRUD, 검색, 월별 요약, 예산, 카테고리 관리, CSV 가져오기/내보내기와 ZIP 백업을 제공합니다.

## 실행

저장소를 내려받아 README가 있는 폴더에서 실행합니다.

```bash
git clone https://github.com/bidulgiya999/codyssey_work_B2-1.git
cd codyssey_work_B2-1
python --version
python -m budget_app --help
python -m budget_app category list
python -m budget_app add
```

Windows에서 Python 명령이 `py`인 환경은 `python` 대신 `py -3`을 사용해도 됩니다. 모든 명령과 하위 명령은 `--help`를 지원합니다. 옵션은 `--` 표기로 통일했습니다.

전역 옵션은 **명령 앞**에 지정합니다. 기본 저장 위치는 실행한 작업 폴더의 `./data`이며, 다음처럼 바꿀 수 있습니다.

```bash
python -m budget_app --data-dir ./my-ledger category list
python -m budget_app --data-dir ./my-ledger --verbose list --limit 3
```

`--verbose`는 실행 시간과 종료 코드를 표준 오류로 기록합니다. 개인정보인 메모나 입력 내용은 로그에 남기지 않습니다.

## 주요 명령

### 거래 추가: 대화형

```text
$ python -m budget_app add
등록된 카테고리: food, transport, rent, salary, etc
날짜(YYYY-MM-DD): 2024-01-15
타입(income/expense): expense
카테고리: food
금액(양수 정수): 15000
메모(선택): 점심
태그(쉼표 구분, 선택): meal,work
[저장 완료] id=TX-...
```

날짜는 실제 달력 날짜여야 하며, 금액은 `1~9223372036854775807` 범위의 정수입니다. 금액 단위는 원입니다. 0·음수·소수·미등록 카테고리·잘못된 타입은 오류 메시지와 힌트를 출력하고 저장하지 않습니다. 오류가 나면 명령을 다시 실행합니다. 메모/태그는 엔터로 생략할 수 있습니다. 태그는 앞뒤 공백 및 중복을 제거합니다.

### 목록과 검색

```bash
python -m budget_app list
python -m budget_app list --limit 3
python -m budget_app search --from 2024-01-01 --to 2024-01-31
python -m budget_app search --category food --type expense --q 점심 --tag meal
python -m budget_app search --from 2024-01-01 --limit 10
```

목록 기본 출력은 20건이며 검색은 기본 전체 출력입니다. `--limit`은 양수입니다. 여러 검색 조건은 AND로 결합합니다. 시작/종료 날짜를 포함하며, 한쪽 경계만 지정해도 됩니다. 메모는 대소문자를 무시한 부분 일치, 태그는 대소문자를 구분하는 완전 일치입니다. 결과는 **거래 날짜 내림차순**이며 같은 날짜는 id 내림차순입니다. 같은 날짜의 순서는 입력 시각을 뜻하지 않습니다. 거래 id는 UUID 기반 `TX-<32자리 16진수>`입니다.

### 수정과 삭제

**수정은 옵션 방식으로 고정**했습니다. `list`에서 확인한 실제 id로 `TX-...`를 바꿉니다.

```bash
python -m budget_app update --id TX-... --amount 12000 --memo 저녁 --tags meal,home
python -m budget_app update --id TX-... --date 2024-02-01 --category etc
python -m budget_app update --id TX-... --memo "" --tags ""
python -m budget_app delete --id TX-...
```

수정 가능한 필드는 `--date`, `--type`, `--category`, `--amount`, `--memo`, `--tags`입니다. 지정하지 않은 값은 유지합니다. 메모/태그는 빈 문자열로 지울 수 있습니다. 없는 id나 수정 필드가 없는 요청은 오류로 처리합니다. 날짜를 바꾸면 정렬 위치도 함께 바뀝니다.

### 월별 요약과 예산

```bash
python -m budget_app budget set --month 2024-01 --amount 500000
python -m budget_app budget show --month 2024-01
python -m budget_app budget show
python -m budget_app summary --month 2024-01 --top 3
```

예산 설정은 같은 월의 기존 값을 교체합니다. `summary`는 총수입, 총지출, 잔액과 카테고리별 지출 TOP N을 출력합니다. `--top` 기본값은 5입니다. 합계 동률은 카테고리명 순입니다. 월 예산이 있으면 지출/예산 사용률을 표시하고, 지출이 예산보다 크면 초과액과 경고를 출력합니다. 거래가 없는 달은 `데이터 없음`과 0원 합계를 표시하며 예산도 확인할 수 있습니다.

### 카테고리: 추가/삭제는 대화형

```bash
python -m budget_app category list
python -m budget_app category add
python -m budget_app category remove
```

`add`와 `remove` 실행 후 카테고리명을 입력합니다. 이름은 대소문자를 구분합니다. 중복 이름, 사용 중인 카테고리, 마지막 남은 카테고리는 추가/삭제 정책에 따라 거부합니다. 사용 중인 카테고리를 지우려면 관련 거래를 먼저 수정하거나 삭제하세요.

### CSV 가져오기/내보내기

```bash
python -m budget_app import --from examples/import.csv
python -m budget_app export --out january.csv --month 2024-01
python -m budget_app export --out food.csv --from 2024-01-01 --to 2024-01-31 --category food
```

내보내기는 `--month` 또는 `--from`/`--to` 중 하나 이상의 기간 조건이 필수입니다. 월과 날짜 범위는 함께 지정할 수 없습니다. 검색과 동일한 `--category`, `--type`, `--q`, `--tag` 필터도 지원합니다. 결과가 없어도 헤더를 포함한 CSV를 생성합니다. 대상 CSV가 이미 있으면 성공 시 교체하며, 오류 시 기존 파일을 유지합니다. 대상 폴더는 미리 만들어 두세요. 가계부 저장 파일을 내보내기 대상으로 지정하는 것은 차단합니다.

CSV 스키마는 다음과 같습니다. **UTF-8, 헤더 포함**, 구분자는 쉼표입니다. 입력은 UTF-8 BOM도 허용합니다.

| 열 | 필수 | 설명 |
| --- | --- | --- |
| date | Y | 실제 날짜, `YYYY-MM-DD` |
| type | Y | `income` 또는 `expense` |
| category | Y | 이미 등록된 카테고리 |
| amount | Y | 양수 정수, 단위 원 |
| memo | N | 문자열, 생략/빈 값 가능 |
| tags | N | 쉼표로 구분하는 문자열, 생략/빈 값 가능 |

```csv
date,type,category,amount,memo,tags
2024-01-15,expense,food,15000,점심,"meal,work"
2024-01-01,income,salary,3000000,월급,salary
```

쉼표·큰따옴표·개행이 들어간 값은 표준 CSV 인용 규칙을 따릅니다. `memo`, `tags` 열 자체는 생략 가능하지만, 헤더 중복/알 수 없는 열/행의 열 개수 불일치는 거부합니다. 등록되지 않은 카테고리는 `category add`로 먼저 추가하세요.

가져오기는 한 행이라도 잘못되면 **전체 취소**합니다. 성공 시 `imported=N, skipped=0`을 출력합니다. CSV에는 id가 없으므로 각 행에 새 id를 발급합니다. 같은 CSV를 다시 가져오면 별도 거래로 중복 등록됩니다. 내보내기는 날짜 최신순이며 여섯 열을 모두 기록합니다.

### 백업 (보너스)

```bash
python -m budget_app backup
```

`data/backups/backup-날짜-시각-고유값.zip`에 세 저장 파일의 동일 시점 사본을 담습니다. 복구는 프로그램을 모두 종료하고 현재 파일을 별도로 보관한 뒤, ZIP의 세 파일을 데이터 폴더에 함께 덮어씁니다. 백업은 명시적으로 명령을 실행할 때 생성됩니다.

## 저장 구조와 안전성

영구 저장 형식은 **JSONL**이며 각 줄이 JSON 객체 하나입니다. CSV는 교환용입니다. 첫 실행 시 저장 폴더와 아래 세 파일을 자동 생성합니다.

| 파일 | 한 줄의 데이터 예 |
| --- | --- |
| `data/transactions.jsonl` | `{"id":"TX-...","type":"expense","date":"2024-01-15","amount":15000,"category":"food","memo":"점심","tags":["meal"]}` |
| `data/categories.jsonl` | `{"name":"food"}` |
| `data/budgets.jsonl` | `{"month":"2024-01","amount":500000}` |

카테고리 파일이 0바이트면 `food, transport, rent, salary, etc`를 자동 생성합니다. 깨진 JSON이나 잘못된 스키마를 빈 데이터로 간주하지 않습니다. 거래 파일은 직접 편집하지 마세요. 읽는 중 발견한 손상이나 정렬 오류는 원인과 복구 힌트를 표시합니다. `list --limit`은 필요한 범위까지만 검증하므로 뒤쪽 손상은 전체 조회나 변경 시 발견될 수 있습니다.

모든 CLI 명령은 데이터 폴더의 `.budget.lock`을 배타적으로 생성합니다. 동시에 실행한 다른 명령은 안내 후 실패하므로 두 쓰기가 서로 덮어쓰지 않습니다. 정상/예외 종료 시 잠금을 해제합니다. 강제 종료로 잠금이 남았다면 **다른 프로세스가 실행 중이지 않은지 확인한 뒤** 잠금 파일만 지우고 재실행하세요.

변경은 같은 파일시스템의 임시 파일에 끝까지 기록하고 `flush`와 `fsync` 후 `os.replace`로 교체합니다. 직렬화·검증·쓰기·교체 실패 시 기존 파일을 유지하고 임시 파일을 정리합니다. CSV 가져오기는 별도 스테이징 사본에서 검증/병합한 후 최종 교체합니다. 이 보장은 단일 파일 교체 단위이며, 파일시스템/저장장치 장애까지 포괄하는 데이터베이스 트랜잭션은 아닙니다. 정기적인 백업을 권장합니다.

## 설계와 학습 포인트

```text
budget_app/
  __main__.py     python -m 진입점
  cli.py          인자 해석, 대화형 입력, 표 출력
  models.py       Transaction dataclass, 유효성 검증, AppError
  storage.py      JSONL 제너레이터, 저장소, 잠금, 원자적 쓰기
  service.py      CRUD, 검색, 집계, 카테고리/예산 정책, CSV, 백업
  decorators.py   공통 예외 처리, 종료 코드, 실행 시간 로그
tests/
  test_budget_app.py
examples/
  import.csv
```

- **제너레이터:** `read_jsonl()` → `TransactionRepository.iter_all()` → `BudgetService.search()`가 `yield`로 연결됩니다. `read()`/`readlines()`로 거래 전체를 메모리에 올리지 않습니다. 파일을 날짜 내림차순으로 유지하므로 조회 시 전체 정렬도 필요하지 않습니다. 목록 제한은 `islice`로 조기에 중단합니다.
- **변경의 비용:** 거래 한 건 삽입/수정/삭제는 스트리밍 병합 재작성으로 시간 O(n), 거래 버퍼 O(1)입니다. 검색은 O(n), 요약은 카테고리 수에 비례하는 메모리만 사용합니다. 카테고리/예산 설정은 작은 메타데이터이므로 메모리에 읽습니다.
- **가져오기의 선택:** 거래 배열을 메모리에 쌓지 않고 스테이징 파일에 한 행씩 정렬 병합합니다. 거래 버퍼는 O(1)이지만 m건 가져오기에 O(mn + m²) 시간과 원본 크기에 비례하는 임시 디스크 공간을 사용합니다. 대규모 가져오기 성능보다 표준 라이브러리 기반의 단순한 검증·전체 취소를 우선한 구현입니다.
- **데코레이터:** `@command_boundary`를 CLI 실행 함수에 적용해 오류 메시지/힌트, 종료 코드, 시간 측정을 업무 코드와 분리했습니다. `functools.wraps`로 함수 정보를 유지합니다.
- **타입 힌트:** `Iterator[Transaction]`, `dict[str, int]`, `Transaction | None` 등으로 계층 사이의 입출력 계약을 명시합니다. 예를 들어 저장소는 거래를 하나씩 반환하고 서비스의 `search()`는 거래 제너레이터를 그대로 CLI로 전달합니다. 타입 힌트와 별도로 실제 입력도 검증합니다.
- **최소 클래스 수:** `Transaction`, `DataStore`, `TransactionRepository`, `BudgetService`, `Filters`, `AppError`로 책임을 나눴습니다.

## 오류와 종료 코드

정상 완료/도움말은 `0`, 입력·데이터·파일 오류는 `1`, 명령 인자 오류는 `2`, EOF/Ctrl+C 입력 취소는 `130`입니다. 예상 가능한 오류는 스택트레이스 대신 `[오류]`와 `[힌트]`를 표준 오류에 출력합니다.

## 테스트

```bash
python -m unittest discover -s tests -v
```

30개 테스트에서 기능/입력 검증, 최신순 정렬, 제너레이터 조기 중단, 모든 명령의 도움말, subprocess 종료 코드, 한글·쉼표·개행 CSV 왕복, 잘못된 가져오기의 전체 취소, 손상 데이터, 교체/쓰기 실패 시 원본 보존, 동시 접근 잠금과 백업을 검증합니다. 테스트는 임시 폴더를 사용해 실제 `./data`에 영향을 주지 않습니다. GitHub Actions는 Windows/Linux에서 Python 3.10, 3.12, 3.14 조합을 실행하도록 구성했습니다.

### 예제 데이터로 빠르게 확인

```bash
python -m budget_app --data-dir ./demo-data import --from examples/import.csv
python -m budget_app --data-dir ./demo-data list --limit 3
python -m budget_app --data-dir ./demo-data budget set --month 2024-01 --amount 30000
python -m budget_app --data-dir ./demo-data summary --month 2024-01 --top 3
python -m budget_app --data-dir ./demo-data export --out demo-export.csv --month 2024-01
python -m budget_app --data-dir ./demo-data backup
```

예제 요약은 수입 3,000,000원, 지출 35,000원, 잔액 2,965,000원, 예산 사용률 116.7%, 초과액 5,000원입니다.
