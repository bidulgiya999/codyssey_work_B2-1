# 파일별 역할과 CRUD 코드 안내

## CRUD란?

CRUD는 데이터를 다루는 네 기본 동작 **Create(생성), Read(조회), Update(수정), Delete(삭제)**의 머리글자입니다. 데이터베이스에서만 쓰는 말이 아니라 이 가계부처럼 파일에 저장하는 프로그램에도 적용됩니다.

| 동작 | 가계부 명령 | 서비스 | 저장소 처리 |
| --- | --- | --- | --- |
| C 생성 | `add` | `BudgetService.add()` | `replace(replacement=transaction)`으로 새 거래 삽입 |
| R 조회 | `list`, `search` | `BudgetService.search()` | `iter_all()`에서 한 건씩 읽기 |
| U 수정 | `update --id ...` | `BudgetService.update()` | 대상 옛 버전을 제외하고 수정본 삽입 |
| D 삭제 | `delete --id ...` | `BudgetService.delete()` | 대상 id만 제외하고 재작성 |

`summary`는 읽은 거래를 집계하는 Read입니다. `export`는 거래를 읽어 외부 CSV를 쓰며 거래 자체를 변경하지 않습니다. `import`는 여러 거래를 생성하는 일괄 Create입니다. `budget set`은 해당 월이 없으면 Create, 있으면 Update이고, 카테고리 add/list/remove는 별도 메타데이터의 C/R/D입니다.

## Python 파일 전체 지도

| 파일 | 책임 | 먼저 볼 코드 |
| --- | --- | --- |
| [budget_app/__init__.py](../budget_app/__init__.py) | 패키지 표시, import 시 작업 실행 안 함 | 파일 설명 주석 |
| [budget_app/__main__.py](../budget_app/__main__.py) | `python -m budget_app` 진입점·종료 코드 | `SystemExit(main())` |
| [budget_app/models.py](../budget_app/models.py) | 거래 모델·검증·오류 정보 | `Transaction`, `positive()`, `valid_date()` |
| [budget_app/storage.py](../budget_app/storage.py) | JSONL 읽기·안전 쓰기·잠금·거래 저장소 | `atomic_text()`, `read_jsonl()`, `TransactionRepository` |
| [budget_app/service.py](../budget_app/service.py) | 정책·CRUD·검색·요약·CSV·백업 | `BudgetService`, `Filters` |
| [budget_app/cli.py](../budget_app/cli.py) | 인자 해석·질문·출력 | `parser()`, `execute()`, `main()` |
| [budget_app/decorators.py](../budget_app/decorators.py) | 공통 오류 안내·종료 코드·시간 로그 | `command_boundary()` |
| [tests/__init__.py](../tests/__init__.py) | 테스트 패키지 표시 | 파일 설명 주석 |
| [tests/test_budget_app.py](../tests/test_budget_app.py) | 30개 테스트 및 임시 데이터 도우미 | `BudgetTests`, 각 `test_...` 메서드 |

각 파일 상단에 역할을, 각 클래스·함수 앞에 책임을, 주요 문장 앞에 처리 순서와 이유를 한국어 주석으로 달았습니다. 조건문·변환·예외·반환·yield·파일 교체 및 테스트의 검증 목적을 함께 읽을 수 있습니다. 여러 줄로 이어지는 한 문장은 묶어서 설명합니다.

## models.py 읽는 순서

- `AppError`: 원인 메시지와 해결 hint를 보관합니다.
- `valid_date` / `valid_month`: 모양뿐 아니라 달력 날짜도 검사합니다.
- `positive`: 금액·limit·top을 양수 정수로 검증합니다.
- `valid_name` / `parse_tags`: 카테고리와 태그를 정리합니다.
- `Transaction`: 일곱 필드의 거래 dataclass입니다. `__post_init__`은 모델 계약, `key`는 날짜/id 정렬, `record`는 저장 dict, `from_record`는 파일 복원, `create`는 새 id와 입력 정리를 담당합니다.

## storage.py 읽는 순서

- `atomic_text`: 임시 스트림 제공 → 정상 기록 완료 → flush/fsync → 닫기 → os.replace → 남은 임시 파일 정리.
- `read_jsonl`: 한 줄 파싱과 손상 위치 안내 후 dict를 yield합니다.
- `write_jsonl`: Iterable을 한 건씩 JSONL로 쓰고 atomic_text에 교체를 맡깁니다.
- `DataStore.session`: 데이터 폴더와 세 파일 초기화·잠금·종료 정리입니다.
- `protect_output`: CSV 출력으로 저장 파일이 덮어써지는 것을 막습니다.
- `TransactionRepository.iter_all` / `find`: 거래 스트림과 id 조회입니다.
- `replace`: C/U/D가 공유하는 스트리밍 재작성입니다. 이름의 replace는 파일 저장 연산이며, `dataclasses.replace`가 객체 사본을 만드는 것과 구분합니다.

## service.py 읽는 순서

- `Filters.__post_init__` / `matches`: 검색 조건 검증과 한 거래의 AND 일치 판단입니다.
- `categories` / `require_category`: 저장된 이름 확인과 등록 여부 검사입니다.
- `category_add` / `category_remove`: 중복·사용 중·마지막 카테고리 보호입니다.
- `add` / `search` / `update` / `delete`: 거래 CRUD의 중심입니다.
- `budgets` / `set_budget`: 월별 설정 조회와 C/U 저장입니다.
- `summary`: 월별 합계와 지출 순위를 만들고 예산도 반환합니다.
- `import_csv`: 사본 스테이징에서 모든 행을 처리한 뒤 한 번에 최종 반영합니다.
- `export_csv`: 기간·출력 경로 보호 후 여섯 열 CSV를 씁니다.
- `backup`: 세 파일의 ZIP과 생성 경로를 반환합니다.

## cli.py와 decorators.py 읽는 순서

- `Parser.error`: 잘못된 명령 문법을 종료 코드 2와 힌트로 안내합니다.
- `parser` / `add_filters`: 명령·옵션·도움말 문법을 등록합니다.
- `filters_from`: 옵션을 Filters 객체로 바꿉니다.
- `display` / `pad` / `print_transactions`: 제어 문자 표시·한글 폭·거래 표 출력입니다.
- `execute`: 명령별로 입력과 서비스 호출을 연결합니다. 이 함수에 `@command_boundary`를 적용합니다.
- `main`: 인자 해석과 verbose 로그를 설정한 후 실행 결과를 반환합니다.
- `command_boundary`: 함수 실행을 감싸 예상 예외·취소를 처리하고 finally에서 시간을 기록합니다.

## 실제 CRUD 데이터 흐름

### C: add

`__main__` → `main` → `execute` 질문 → `Transaction.create` 검증 → `BudgetService.add` 카테고리 검사 → `TransactionRepository.replace` 정렬 삽입 → `write_jsonl` / `atomic_text` → 성공 id 출력.

### R: list/search

`execute` 조건 생성 → `BudgetService.search` → `iter_all` → `read_jsonl` 순차 읽기 → 모델 복원 → 조건 일치 거래 yield → `islice` 제한 → 표 출력. 읽기 흐름은 요청이 올 때 진행하는 지연 처리입니다.

### U: update

옵션 중 지정한 값만 `changes`로 구성 → 기존 id `find` → 금액·태그 변환 → `dataclasses.replace`로 새 객체 생성·검증 → 카테고리 확인 → 저장소가 옛 거래를 제외하고 수정본을 정렬 삽입.

### D: delete

id `find`로 존재 확인 → `replace(identifier)` 호출(대체 거래 없음) → 그 id만 건너뛴 새 파일 작성 → 원자적 교체. 재삭제는 id 조회에서 실패합니다.

## 평가 때 보여줄 순서

1. 위 CRUD 표로 명령과 역할을 설명합니다.
2. cli의 `execute`에서 각 명령 분기를 보여줍니다.
3. service의 CRUD 메서드에서 검증과 정책을 설명합니다.
4. storage의 `replace`, `read_jsonl`, `atomic_text`에서 실제 파일 처리를 보여줍니다.
5. tests에서 정상 동작뿐 아니라 실패 시 원본 보존 테스트도 보여줍니다.

사용자에게 입력받는 책임, 업무 판단, 실제 파일 기록이 서로 다른 위치에 있음을 설명하는 것이 핵심입니다. [평가 질문별 답변](./답변.md)에는 성능·저장 포맷·오류 정책까지 정리했습니다.
