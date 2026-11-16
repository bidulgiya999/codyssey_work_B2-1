# CLI 계층: 명령어 해석 → 서비스 호출 → 결과 출력의 흐름을 담당합니다.
# 거래 CRUD: add=C, list/search=R, update=U, delete=D입니다.
"""argparse 기반 한국어 콘솔 인터페이스. update는 옵션 방식으로 고정."""
# 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다.
from __future__ import annotations

# 하위 명령·옵션·도움말·인자 오류를 표준 라이브러리로 처리합니다.
import argparse
# verbose 옵션에서 실행 결과와 소요 시간 로그를 표시합니다.
import logging
# 오류 출력 스트림과 프로세스 실행 관련 정보를 사용합니다.
import sys
# 터미널 제어 문자 검사와 한글 표시 폭 계산에 사용합니다.
import unicodedata
# 제너레이터를 전부 읽지 않고 limit개에서 중단합니다.
from itertools import islice
# 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다.
from pathlib import Path
# 목록 출력 함수가 리스트뿐 아니라 거래 제너레이터도 받도록 합니다.
from typing import Iterable

# 명령 함수를 감싸는 공통 오류·종료 코드·시간 측정 처리를 사용합니다.
from .decorators import command_boundary
# 거래 모델 및 금액·출력 건수 검증을 CLI에서 재사용합니다.
from .models import AppError, Transaction, positive
# CLI 또는 테스트가 서비스 업무 규칙과 검색 조건 객체를 사용합니다.
from .service import BudgetService, Filters
# 파일 경로와 초기화·명령 단위 잠금을 관리하는 저장소 객체를 연결합니다.
from .storage import DataStore


# argparse를 상속해 인자 오류도 원인+힌트 형식과 종료 코드 2로 통일합니다.
class Parser(argparse.ArgumentParser):
    # argparse가 잘못된 옵션·필수 인자 누락을 발견할 때 호출하는 오류 처리입니다.
    def error(self, message: str) -> None:
        # 잘못된 명령의 문법부터 보여주고 아래에서 원인과 힌트를 붙입니다.
        self.print_usage(sys.stderr)
        # 문법 오류는 argparse 관례대로 종료 코드 2로 끝냅니다.
        self.exit(2, f"[오류] {message}\n[힌트] 해당 명령의 --help를 확인하세요.\n")


# 실행하지 않고 명령 문법만 구성합니다. 하위 명령과 옵션을 등록한 Parser를 반환합니다.
def parser() -> Parser:
    # 최상위 python -m budget_app 명령의 도움말과 문법을 구성합니다.
    root = Parser(description="데이터를 안전하게 저장하는 콘솔 가계부")
    # 전역 저장 위치 옵션입니다. add 등 하위 명령 앞에서 지정합니다.
    root.add_argument("--data-dir", default="./data", help="저장 폴더 (기본: ./data), 명령 앞에 지정")
    # 값을 받지 않는 스위치로, 실행 시간 로그 출력을 켭니다.
    root.add_argument("--verbose", action="store_true", help="명령 실행 시간/종료 코드 로그 출력")
    # 필수 하위 명령을 args.command로 받습니다. 하위 명령도 사용자 정의 Parser를 씁니다.
    commands = root.add_subparsers(dest="command", required=True, parser_class=Parser)
    # C(Create): add는 옵션 대신 실행 중 질문으로 값을 받습니다.
    commands.add_parser("add", help="대화형 거래 추가")
    # R(Read): list 전용 옵션을 붙일 하위 파서를 만듭니다.
    listing = commands.add_parser("list", help="날짜 최신순 목록")
    # list 기본 최대 출력은 20건이며 실제 양수 검증은 실행 시 합니다.
    listing.add_argument("--limit", default="20", help="최대 출력 건수 (기본: 20)")
    # R(Read): 검색 명령을 등록합니다.
    search = commands.add_parser("search", help="조건을 모두 만족하는 거래 검색")
    # 공통 검색 옵션 등록 함수를 재사용합니다.
    add_filters(search)
    # 검색은 limit 미지정 시 조건에 맞는 전체 결과를 표시합니다.
    search.add_argument("--limit", help="최대 출력 건수 (미지정 시 전체)")
    # 월 합계와 카테고리 지출 순위를 보여주는 집계 명령입니다.
    summary = commands.add_parser("summary", help="월별 요약과 지출 TOP N")
    # 요약 대상 월은 반드시 지정해야 합니다.
    summary.add_argument("--month", required=True, help="YYYY-MM")
    # 표시할 지출 카테고리 순위 개수의 기본값은 5입니다.
    summary.add_argument("--top", default="5", help="지출 카테고리 개수 (기본: 5)")
    # U(Update): 수정은 옵션 방식으로 고정합니다.
    update = commands.add_parser("update", help="옵션 방식으로 거래 수정")
    # 수정 대상의 고유 id는 필수입니다.
    update.add_argument("--id", required=True)
    # 동일한 방식으로 여섯 수정 가능 필드를 등록합니다.
    for field in ("date", "type", "category", "amount", "memo", "tags"):
        # 지정하지 않은 수정 필드는 None으로 받아 나중에 제외합니다.
        update.add_argument("--" + field, help=f"변경할 {field}")
    # D(Delete): 삭제 대상은 id 옵션으로 지정합니다.
    delete = commands.add_parser("delete", help="거래 삭제")
    # id 없는 삭제 요청은 문법 단계에서 차단합니다.
    delete.add_argument("--id", required=True)
    # 예산은 set/show의 2단계 명령입니다.
    budget = commands.add_parser("budget", help="월 예산 설정/조회")
    # budget 다음의 동작을 args.action으로 구분합니다.
    budgets = budget.add_subparsers(dest="action", required=True, parser_class=Parser)
    # 예산 신규 설정과 갱신을 담당하는 하위 명령입니다.
    setting = budgets.add_parser("set", help="월 예산 설정")
    # 예산이 적용될 월을 필수로 받습니다.
    setting.add_argument("--month", required=True)
    # 예산 양수 금액을 필수로 받습니다.
    setting.add_argument("--amount", required=True)
    # 저장된 예산을 조회하는 명령입니다.
    showing = budgets.add_parser("show", help="예산 조회")
    # 월을 생략하면 모든 월의 예산을 표시합니다.
    showing.add_argument("--month", help="미지정 시 전체 월")
    # 카테고리 추가·조회·삭제의 진입 명령입니다.
    category = commands.add_parser("category", help="카테고리 관리")
    # category의 동작도 args.action으로 구분합니다.
    categories = category.add_subparsers(dest="action", required=True, parser_class=Parser)
    # 세 카테고리 하위 명령을 같은 구조로 등록합니다.
    for name in ("add", "list", "remove"):
        # 추가와 삭제는 별도 이름 옵션 없이 실행 중 질문합니다.
        categories.add_parser(name, help={"add": "대화형 추가", "list": "목록", "remove": "대화형 삭제"}[name])
    # CSV 일괄 추가 명령을 등록합니다.
    importing = commands.add_parser("import", help="UTF-8 CSV 일괄 등록 (실패 시 전체 취소)")
    # --from은 Python 이름으로 쓰기 어려우므로 args.source에 매핑합니다.
    importing.add_argument("--from", dest="source", required=True, help="CSV 파일 경로")
    # 검색 조건에 맞는 거래를 CSV로 기록하는 명령입니다.
    exporting = commands.add_parser("export", help="기간 조건을 지정해 CSV 내보내기")
    # 출력 파일 경로는 필수입니다.
    exporting.add_argument("--out", required=True)
    # 내보내기는 일반 조건에 더해 월 조건도 등록합니다.
    add_filters(exporting, month=True)
    # 보너스 ZIP 백업 명령을 등록합니다.
    commands.add_parser("backup", help="타임스탬프 ZIP 백업 생성")
    # 구성된 파서를 반환합니다. 아직 거래 처리나 파일 저장은 실행하지 않습니다.
    return root


# search와 export가 공유하는 조건 옵션을 한곳에서 등록합니다.
def add_filters(command: argparse.ArgumentParser, month: bool = False) -> None:
    # 외부 옵션 이름은 --from, 내부 필드 이름은 start입니다.
    command.add_argument("--from", dest="start", help="시작일 YYYY-MM-DD (포함)")
    # 종료 날짜는 end로 받으며 해당 날짜도 검색에 포함합니다.
    command.add_argument("--to", dest="end", help="종료일 YYYY-MM-DD (포함)")
    # 호출자가 허용한 경우에만 --month를 문법에 추가합니다.
    if month:
        # 실제 월/범위 충돌 검사는 Filters에서 수행합니다.
        command.add_argument("--month", help="YYYY-MM, 날짜 범위와 동시 사용 불가")
    # 카테고리 완전 일치 조건입니다.
    command.add_argument("--category")
    # 타입 오타는 argparse choices가 문법 오류로 거부합니다.
    command.add_argument("--type", choices=("income", "expense"))
    # 메모의 부분 문자열 검색 옵션입니다.
    command.add_argument("--q", help="메모 키워드 (대소문자 무시)")
    # 태그 목록 안의 한 값과 완전히 일치해야 합니다.
    command.add_argument("--tag", help="태그 완전 일치")


# argparse.Namespace에서 검색 관련 값만 골라 Filters 객체로 변환합니다.
def filters_from(args: argparse.Namespace) -> Filters:
    # 각 옵션 값을 꺼내 데이터 객체로 넘겨 검색 조건 계약을 통일합니다.
    return Filters(**{key: getattr(args, key, None)
                      for key in ("start", "end", "month", "category", "type", "q", "tag")})


# 사용자 데이터의 제어 문자를 화면에서 보이는 이스케이프로 바꿔 터미널 표시를 보호합니다.
def display(value: object) -> str:
    """개행/탭/터미널 제어 문자를 화면에서 이스케이프한다."""
    # 제어 문자만 \uXXXX 표기로 바꾸며 일반 한글은 그대로 둡니다.
    return "".join(f"\\u{ord(c):04x}" if unicodedata.category(c).startswith("C") else c for c in str(value))


# 한글 등 넓은 문자의 화면 폭을 고려해 표 열의 오른쪽을 공백으로 채웁니다.
def pad(value: str, width: int) -> str:
    # 동아시아 전각/넓은 문자는 화면 두 칸으로 계산합니다.
    cells = sum(2 if unicodedata.east_asian_width(c) in ("W", "F") else 1 for c in value)
    # 목표 폭보다 짧을 때만 공백을 붙이고 긴 내용은 자르지 않습니다.
    return value + " " * max(0, width - cells)


# 거래 Iterable을 한 건씩 출력하고 실제 출력 건수 또는 데이터 없음을 표시합니다.
def print_transactions(transactions: Iterable[Transaction]) -> None:
    count = 0
    # 거래가 없어도 표의 각 열 의미를 먼저 보여줍니다.
    print("ID | 날짜 | 타입 | 카테고리 | 금액 | 메모 | 태그")
    # Iterable을 순회하므로 제너레이터를 그대로 소비할 수 있습니다.
    for t in transactions:
        # 금액은 천 단위 구분자를 넣고 타입/카테고리 열을 정렬해 표시합니다.
        print(f"{t.id} | {t.date} | {t.type:7} | {pad(display(t.category), 12)} | "
              f"{t.amount:>10,} | {display(t.memo)} | {display(','.join(t.tags))}")
        # 실제 출력한 건수만 셉니다.
        count += 1
    # 결과가 0건이면 데이터 없음을 명확히 표시합니다.
    print(f"[조회] {count}건" if count else "데이터 없음")


# 이 함수의 실행을 공통 오류·종료 코드·시간 측정 처리로 감쌉니다.
@command_boundary
# 파싱된 명령을 서비스에 연결합니다. CRUD 정책과 파일 기록은 각 계층에 위임합니다.
def execute(args: argparse.Namespace) -> None:
    # 사용자가 정한 폴더에 연결합니다. 실제 초기화는 session 안에서 합니다.
    store = DataStore(Path(args.data_dir))
    # 입력부터 저장/조회 종료까지 같은 잠금을 유지해 동시 변경을 막습니다.
    with store.session():
        # 저장 폴더에 연결된 업무 서비스 객체를 만듭니다.
        service = BudgetService(store)
        # 하위 명령 이름으로 아래 실행 경로를 선택합니다.
        command = args.command
        # C(Create): 질문 입력 → 모델 검증 → 카테고리 확인 → 안전 저장.
        if command == "add":
            # 사용자가 입력 가능한 카테고리 목록을 먼저 안내합니다.
            print("등록된 카테고리: " + ", ".join(service.categories()))
            # input 값으로 모델을 만듭니다. 이 호출이 성공해야 서비스 저장으로 넘어갑니다.
            transaction = Transaction.create(
                # 날짜는 문자열로 입력받고 앞뒤 공백을 제거합니다.
                date=input("날짜(YYYY-MM-DD): ").strip(),
                # income 또는 expense를 받습니다. 실제 제한은 모델에서 검증합니다.
                type=input("타입(income/expense): ").strip(),
                # 등록된 이름인지 서비스에서 검사할 값입니다.
                category=input("카테고리: ").strip(),
                # 문자열 입력을 모델의 positive가 정수로 검증·변환합니다.
                amount=input("금액(양수 정수): ").strip(),
                # 메모는 공백도 내용일 수 있어 그대로 받고, 태그는 모델에서 쉼표 분리합니다.
                memo=input("메모(선택): "), tags=input("태그(쉼표 구분, 선택): "))
            # C: 입력이 모두 유효하면 서비스에 영구 저장을 요청합니다.
            service.add(transaction)
            # 저장이 실제 성공한 뒤에만 새 id를 안내합니다.
            print(f"[저장 완료] id={transaction.id}")
        # R(Read): list와 search는 같은 스트리밍 조회·출력 경로를 공유합니다.
        elif command in ("list", "search"):
            # 제한 건수도 양수로 검증합니다. None이면 검색 결과 전체를 허용합니다.
            limit = positive(args.limit) if args.limit is not None else None
            # list는 조건 없는 Filters, search는 사용자가 선택한 조건을 사용합니다.
            transactions = service.search(Filters() if command == "list" else filters_from(args))
            # limit까지만 제너레이터를 소비하므로 뒤쪽 파일을 불필요하게 읽지 않습니다.
            print_transactions(islice(transactions, limit))
        # U(Update): 사용자가 실제로 지정한 옵션만 수정 요청으로 보냅니다.
        elif command == "update":
            # None은 미지정이므로 제외합니다. 빈 문자열은 유지해 메모/태그를 지울 수 있게 합니다.
            changes = {key: getattr(args, key) for key in ("date", "type", "category", "amount", "memo", "tags")
                       if getattr(args, key) is not None}
            # 대상 id 조회와 새 값 검증·저장을 서비스에 위임합니다.
            service.update(args.id, changes)
            print(f"[수정 완료] id={args.id}")
        # D(Delete): 서비스가 존재 여부 확인 후 대상만 제외해 파일을 재작성합니다.
        elif command == "delete":
            # 없는 id이면 이 호출에서 오류가 발생하고 아래 성공 메시지는 실행되지 않습니다.
            service.delete(args.id)
            print(f"[삭제 완료] id={args.id}")
        # 카테고리 관리 분기입니다. 거래 CRUD와 별도의 메타데이터를 수정합니다.
        elif command == "category":
            if args.action == "list":
                # 검증된 카테고리 목록을 한 줄씩 화면에 표시합니다.
                for name in service.categories():
                    print("- " + display(name))
            elif args.action == "add":
                # 이름 입력과 화면 출력은 CLI, 중복 검증과 저장은 서비스가 담당합니다.
                name = service.category_add(input("카테고리명: "))
                print(f"[저장 완료] category={name}")
            else:
                # 삭제할 카테고리 이름만 받고 실제 사용 여부 검사는 서비스에 맡깁니다.
                name = input("삭제할 카테고리명: ").strip()
                # 사용 중인 이름은 AppError가 발생하므로 삭제 완료를 출력하지 않습니다.
                service.category_remove(name)
                print(f"[삭제 완료] category={name}")
        # 예산 set은 저장, show는 조회로 분리합니다.
        elif command == "budget":
            if args.action == "set":
                # 월과 금액을 검증하고 예산 파일을 영구 저장합니다.
                service.set_budget(args.month, args.amount)
                print(f"[저장 완료] {args.month} 예산 {int(args.amount):,}원")
            else:
                # 다른 계층의 모델·검증·저장 처리를 가져와 같은 로직을 재사용합니다.
                from .models import valid_month
                # 조회에도 잘못된 월 표기를 허용하지 않습니다.
                if args.month is not None:
                    valid_month(args.month)
                budgets = service.budgets()
                # 월 미지정이면 전체, 지정이면 해당 월만 선택합니다.
                selected = {m: a for m, a in sorted(budgets.items()) if args.month is None or m == args.month}
                for month, amount in selected.items():
                    print(f"{month}: {amount:,}원")
                # 설정되지 않은 예산을 0원 예산과 혼동하지 않도록 별도 문구를 표시합니다.
                if not selected:
                    print("설정된 예산 없음")
        # 집계는 Read에 해당합니다. 거래를 추가하거나 수정하지 않습니다.
        elif command == "summary":
            # 표시할 순위 개수도 양수여야 합니다.
            top = positive(args.top)
            # 서비스는 합계 자료만 반환하며 아래 CLI 코드가 문구를 구성합니다.
            result = service.summary(args.month)
            # 잔액 계산에 쓸 두 합계를 꺼냅니다.
            income, expense = result["income"], result["expense"]
            # 거래가 없는 월도 명확히 안내한 뒤 0원 합계를 출력합니다.
            if not result["count"]:
                print("데이터 없음")
            print(f"총 수입: {income:,}원\n총 지출: {expense:,}원\n잔액: {income - expense:,}원")
            # 예산 None은 미설정입니다. 설정된 예산은 양수이므로 나눗셈이 가능합니다.
            budget = result["budget"]
            # 예산이 있을 때만 사용률을 출력합니다.
            if budget is not None:
                print(f"예산: {budget:,}원 (사용률 {expense * 100 / budget:.1f}%)")
                # 예산과 같은 금액은 초과가 아닙니다. 큰 경우에만 경고합니다.
                if expense > budget:
                    print(f"[경고] 예산 초과: {expense - budget:,}원")
            print(f"지출 TOP {top}")
            # 정렬된 집계 결과 중 top개만 1부터 번호를 붙여 출력합니다.
            for rank, (category, amount) in enumerate(result["categories"][:top], 1):
                print(f"{rank}) {display(category)} {amount:,}원")
        # 일괄 Create: CSV 검증과 전체 반영/취소는 서비스가 담당합니다.
        elif command == "import":
            # 성공한 뒤에만 처리 건수를 받습니다. 오류가 나면 완료 문구를 출력하지 않습니다.
            count = service.import_csv(Path(args.source))
            print(f"[완료] imported={count}, skipped=0")
        # 거래는 Read, 교환 파일은 쓰기 작업입니다. 저장 거래 자체는 바꾸지 않습니다.
        elif command == "export":
            # 조건 검증과 출력 보호를 거친 CSV 내보내기를 요청합니다.
            count = service.export_csv(Path(args.out), filters_from(args))
            print(f"[완료] {args.out} ({count} records)")
        # 백업 경로를 반환받아 사용자에게 보여줍니다.
        elif command == "backup":
            print(f"[백업 완료] {service.backup()}")


# 외부에서 호출하는 시작 함수입니다. 문법 해석과 로그 설정 후 종료 코드를 반환합니다.
def main(argv: list[str] | None = None) -> int:
    # argv=None이면 실제 터미널 인자를, 리스트이면 테스트에서 준 인자를 해석합니다.
    args = parser().parse_args(argv)
    # 사용자가 요청했을 때만 INFO 로그를 표시합니다.
    if args.verbose:
        logging.basicConfig(level=logging.INFO, format="[로그] %(message)s")
    # 데코레이터가 반환한 종료 코드(int)를 __main__으로 전달합니다.
    return execute(args)
