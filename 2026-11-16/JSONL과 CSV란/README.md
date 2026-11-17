# JSONL과 CSV란?

파일 이름의 올바른 표기는 **CSV**입니다. JSONL과 CSV는 데이터를 텍스트로 저장하는 구조이며 Python 코드나 별도의 프로그램 이름은 아닙니다. 둘 다 표준 라이브러리로 읽고 쓸 수 있습니다.

이 가계부는 **내부 영구 저장에 JSONL**, **다른 프로그램과 주고받는 교환 파일에 CSV**를 사용합니다. [실행 명령 모음](../명령어_모음집.md)과 함께 보세요.

## 1. JSONL: JSON 객체를 한 줄에 하나씩

JSONL은 JSON Lines라는 뜻입니다. 이 프로그램에서는 한 줄이 한 레코드이며, 각 레코드는 필드 이름과 값을 가진 JSON 객체입니다. 확장자는 `.jsonl`입니다.

```jsonl
{"id":"TX-ffffffffffffffffffffffffffffffff","type":"income","date":"2026-11-16","amount":3000000,"category":"salary","memo":"이번달 월급","tags":["기타"]}
{"id":"TX-eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee","type":"expense","date":"2026-11-16","amount":12000,"category":"food","memo":"저녁","tags":["meal","work"]}
```

위 데이터는 구조를 설명하기 위해 만든 **예시**이며 현재 실제 거래 파일의 사본이 아닙니다. id는 예시 고정값이고 실제 add는 UUID로 새 id를 만듭니다. 두 예시 거래는 같은 날짜이므로 id 내림차순으로 배치했습니다.

| 기호/값 | 뜻 |
| --- | --- |
| `{ ... }` | 필드 이름과 값으로 구성된 JSON 객체 |
| `"amount": 12000` | amount 값은 따옴표 없는 JSON 숫자 |
| `"category": "food"` | 문자열 값은 큰따옴표로 감쌈 |
| `"tags": ["meal", "work"]` | 태그는 여러 문자열의 배열 |
| 한 줄 뒤의 개행 | 다음 레코드와 구분 |

일반 JSON의 큰 배열처럼 파일 전체를 `[`와 `]`로 감싸거나 거래 사이에 구분 쉼표를 붙이지 않습니다. 각 줄을 독립된 JSON으로 해석합니다. 메모에 줄바꿈이 있으면 저장 시 `\n`으로 이스케이프되어 레코드의 물리 줄은 하나로 유지됩니다.

### 거래 필드

| 필드 | Python 모델 | 의미 |
| --- | --- | --- |
| id | str | 고유 식별자, 수정·삭제에 사용 |
| type | str | income / expense |
| date | str | 실제 날짜 YYYY-MM-DD |
| amount | int | 양수 원 단위 금액 |
| category | str | 등록된 카테고리 |
| memo | str | 선택 메모, 기본 빈 문자열 |
| tags | tuple[str, ...] | 모델에서는 tuple, JSON에서는 배열 |

JSON 문법이 맞는 것과 거래로 유효한 것은 다릅니다. 예를 들어 `amount: 0`은 문법만 보면 JSON 숫자지만 가계부 정책에서 거부합니다. 타입 힌트와 별도로 실제 입력·저장 데이터를 검증합니다.

## 2. 이 저장소의 JSONL 세 파일

기본 위치는 **calculator 루트의 data 폴더**입니다. GitHub에는 프로그램이 있고 실제 실행 시 파일을 생성·저장합니다. 문서의 예시는 [예시 폴더](./예시)에 따로 있습니다.

### transactions.jsonl — 거래

위처럼 각 줄에 거래 하나를 저장하며 `(date, id)` 내림차순을 유지합니다. 검색과 목록은 한 줄씩 읽습니다. 실제 날짜순 정렬은 JSONL 자체 기능이 아니라 이 프로그램의 저장 정책입니다.

### categories.jsonl — 등록 카테고리

```jsonl
{"name":"food"}
{"name":"salary"}
```

한 줄이 이름 하나입니다. 실제 기본 목록에는 food, transport, rent, salary, etc가 있습니다. 초기 생성 순서와 추가 후 정렬 순서는 다를 수 있습니다. 거래에 사용 중인 이름의 삭제는 서비스에서 차단합니다.

### budgets.jsonl — 월 예산

```jsonl
{"month":"2026-11","amount":10000}
```

한 월에 한 레코드를 저장하고 같은 월에 budget set을 실행하면 금액을 갱신합니다. 월은 문자열, 금액은 숫자입니다.

## 3. CSV: 행과 열로 이루어진 표

CSV는 **Comma-Separated Values**, 즉 쉼표로 구분하는 값입니다. 확장자는 `.csv`입니다. 이 프로그램의 첫 행은 열 이름(헤더)이고 이후 각 레코드가 거래입니다.

```csv
date,type,category,amount,memo,tags
2026-11-16,income,salary,3000000,이번달 월급,기타
2026-11-16,expense,food,12000,저녁,"meal,work"
```

`"meal,work"`를 감싼 큰따옴표는 **쉼표가 포함된 한 개의 셀**이라는 뜻입니다. 큰따옴표가 없으면 두 열로 나뉠 수 있습니다. 셀 안의 큰따옴표는 표준 CSV 규칙에서 두 번 적으며, 셀 안 개행도 인용해서 표현할 수 있습니다. 따라서 CSV는 무조건 문자열을 split(',')로 나누거나 물리 줄마다 거래라고 가정하면 안 됩니다. 프로그램은 csv 모듈로 처리합니다.

### 이 과제에서 고정한 CSV 스키마

| 컬럼 | 필수 | 입력 규칙 |
| --- | --- | --- |
| date | Y | YYYY-MM-DD 실제 날짜 |
| type | Y | income 또는 expense |
| category | Y | 이미 등록된 이름 |
| amount | Y | 양수 정수, 소수·쉼표 천 단위 구분자 없음 |
| memo | N | 문자열, 생략/빈 값 가능 |
| tags | N | 쉼표로 나눈 태그 문자열, 생략/빈 값 가능 |

이 프로그램의 교환 규칙은 **UTF-8, 헤더 포함**입니다. 입력은 BOM이 있는 UTF-8도 허용하며, 내보내기는 위 여섯 열을 순서대로 기록합니다. CSV 형식 자체가 모든 파일에 UTF-8이나 헤더를 강제하는 것은 아니고, 여기서 정한 스키마입니다.

CSV 값은 기본적으로 문자열로 읽히므로 amount를 int로 검증·변환합니다. id는 교환 스키마에 없습니다. import할 때 각 행마다 새 id가 생성됩니다. 같은 CSV를 재가져오면 기존 id를 찾아 수정하는 것이 아니라 중복 거래가 추가됩니다.

## 4. 같은 거래가 어떻게 달라지나요?

| 항목 | 내부 JSONL | 교환 CSV |
| --- | --- | --- |
| 필드 이름 | 각 객체마다 기록 | 맨 위 헤더에 기록 |
| 거래 id | 저장함 | 이 과제의 CSV에는 없음 |
| 금액 | JSON 숫자 | 읽을 때 문자열, 정수로 변환 필요 |
| 태그 | 배열 `["meal","work"]` | 한 셀의 쉼표 문자열 `"meal,work"` |
| 구조 | 한 줄 한 객체 | 표의 열과 레코드 |
| 개행 처리 | 문자열 안 개행은 `\n`로 이스케이프 | 셀 내부 개행은 인용된 필드로 여러 물리 줄 사용 가능 |

두 파일의 바이트나 표기가 같지는 않아도 변환 후의 거래 정보가 일치하도록 합니다. 다만 CSV에는 id가 없어 내보내기→가져오기 후 새 id가 생성되는 차이는 의도된 정책입니다.

## 5. 장단점과 언제 쓰는가?

| 형식 | 장점 | 단점 | 주로 쓰기 좋은 상황 |
| --- | --- | --- | --- |
| JSONL | 한 줄씩 처리, 숫자·배열 표현, 각 줄의 필드 이름이 명확 | 키 이름 반복으로 커질 수 있음, 스프레드시트에서 직접 보기 불편, 잘못된 스키마는 여전히 검증 필요 | 앱의 레코드 저장, 로그·이벤트 스트림, 줄 단위 데이터 처리 |
| CSV | 간단한 표, 여러 도구와 교환하기 쉬움, 고정 열이면 구조가 간결 | 타입 변환 필요, 배열 표현 규칙 필요, 쉼표·인용·개행 주의 | 표 자료 전달, 스프레드시트 분석, 일괄 가져오기/내보내기 |

두 형식 모두 순차 처리할 수 있습니다. 제너레이터가 JSONL에서만 가능한 것은 아닙니다. JSONL이라는 이유만으로 id 인덱스나 빠른 수정·삭제가 생기지도 않습니다. 현재 프로그램은 거래 변경 시 파일을 재작성합니다.

**이 과제의 선택 이유:** 내부는 태그 배열과 숫자를 표현하기 좋은 JSONL, 외부 전달은 표에 익숙한 사용자를 위한 CSV로 나눴습니다. 거래·카테고리·예산의 영구 저장 형식은 JSONL 하나로 통일하고 CSV는 교환용으로만 씁니다.

## 6. 명령과 코드의 연결

| 동작 | 내부 흐름 |
| --- | --- |
| add | 입력 검증 → 새 Transaction → transactions.jsonl에 정렬 병합 |
| list/search | read_jsonl → Transaction.from_record → 조건 검사 → 표 출력 |
| export | 내부 거래 조회 → 태그 배열을 쉼표 문자열로 변환 → CSV 헤더/행 기록 |
| import | CSV 읽기 → 금액·날짜·카테고리 검증 → 새 id → 스테이징 JSONL → 전체 성공 시 반영 |

관련 코드는 [storage.py](../../budget_app/storage.py)의 `read_jsonl`, `write_jsonl`, [models.py](../../budget_app/models.py)의 `record`, `from_record`, [service.py](../../budget_app/service.py)의 `CSV_FIELDS`, `import_csv`, `export_csv`입니다.

## 7. 예시 파일 보기와 안전한 사용

[예시 폴더](./예시)의 세 JSONL과 CSV는 구조 학습용입니다. 현재 data 파일에 덮어쓰지 마세요. 파일을 클릭해서 구조를 비교하면 됩니다. 예시 JSONL의 id는 설명용 고정값입니다.

CSV 가져오기를 직접 연습하려면 기존 평가 데이터 대신 별도 폴더를 사용합니다. 아래 명령은 calculator 루트의 VS Code PowerShell 터미널에서 실행합니다.

```powershell
& $ledgerPython -m budget_app --data-dir ./format-practice import --from "2026-11-16/JSONL과 CSV란/예시/transactions.csv"
& $ledgerPython -m budget_app --data-dir ./format-practice list --limit 5
```

첫 실행에 기본 카테고리를 생성하므로 예시 food/salary를 사용할 수 있습니다. 같은 명령을 반복하면 별도 폴더에도 중복 등록되므로 한 번만 가져옵니다. CSV의 각 행에 새 id를 만들기 때문에 JSONL 예시 id와는 달라집니다.

실제 기존 저장 파일을 보기만 할 때:

```powershell
Get-Content -Encoding UTF8 .\data\categories.jsonl
Get-Content -Encoding UTF8 .\data\budgets.jsonl
Get-Content -Encoding UTF8 .\data\transactions.jsonl -TotalCount 5
```

Get-Content는 보기 명령입니다. 큰 JSONL 파일은 TotalCount로 일부만 볼 수 있습니다. 실제 파일을 직접 편집하면 최신순 정렬이나 스키마를 깨뜨릴 수 있으므로 거래 변경은 앱 명령을 사용합니다.

## 8. 깨진 행이 있으면?

JSONL을 읽다가 문법·모델 오류를 발견하면 파일/줄 위치와 해결 안내를 표시하며 자동 초기화하지 않습니다. CSV 가져오기는 일부 성공으로 넘어가지 않고, **첫 오류를 보고 이번 전체 작업을 취소**합니다. 원본이 아닌 임시 사본에 작업하므로 정상 행을 먼저 처리했어도 원본에는 반영하지 않습니다.

실제 시연에서 내보내기 2건·가져오기 3건을 확인했고 자동 테스트는 한글·쉼표·인용·개행 왕복 및 잘못된 가져오기 전체 취소를 검증합니다. [당시 실행 기록](../README.md)은 현재 파일의 최신 합계와는 다를 수 있습니다.

**평가 멘트:** “내부 저장은 숫자와 태그 배열을 표현하고 한 줄씩 읽기 좋은 JSONL을 선택했습니다. 사용자와의 교환은 표 형태의 CSV로 제공합니다. CSV의 필드와 인코딩을 고정하고, 가져올 때 검증과 전체 취소 정책으로 데이터를 보호합니다.”
