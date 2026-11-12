"""argparse 기반 한국어 콘솔 인터페이스. update는 옵션 방식으로 고정."""
from __future__ import annotations

import argparse
import logging
import sys
import unicodedata
from itertools import islice
from pathlib import Path
from typing import Iterable

from .decorators import command_boundary
from .models import AppError, Transaction, positive
from .service import BudgetService, Filters
from .storage import DataStore


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        self.print_usage(sys.stderr)
        self.exit(2, f"[오류] {message}\n[힌트] 해당 명령의 --help를 확인하세요.\n")


def parser() -> Parser:
    root = Parser(description="데이터를 안전하게 저장하는 콘솔 가계부")
    root.add_argument("--data-dir", default="./data", help="저장 폴더 (기본: ./data), 명령 앞에 지정")
    root.add_argument("--verbose", action="store_true", help="명령 실행 시간/종료 코드 로그 출력")
    commands = root.add_subparsers(dest="command", required=True, parser_class=Parser)
    commands.add_parser("add", help="대화형 거래 추가")
    listing = commands.add_parser("list", help="날짜 최신순 목록")
    listing.add_argument("--limit", default="20", help="최대 출력 건수 (기본: 20)")
    search = commands.add_parser("search", help="조건을 모두 만족하는 거래 검색")
    add_filters(search)
    search.add_argument("--limit", help="최대 출력 건수 (미지정 시 전체)")
    summary = commands.add_parser("summary", help="월별 요약과 지출 TOP N")
    summary.add_argument("--month", required=True, help="YYYY-MM")
    summary.add_argument("--top", default="5", help="지출 카테고리 개수 (기본: 5)")
    update = commands.add_parser("update", help="옵션 방식으로 거래 수정")
    update.add_argument("--id", required=True)
    for field in ("date", "type", "category", "amount", "memo", "tags"):
        update.add_argument("--" + field, help=f"변경할 {field}")
    delete = commands.add_parser("delete", help="거래 삭제")
    delete.add_argument("--id", required=True)
    budget = commands.add_parser("budget", help="월 예산 설정/조회")
    budgets = budget.add_subparsers(dest="action", required=True, parser_class=Parser)
    setting = budgets.add_parser("set", help="월 예산 설정")
    setting.add_argument("--month", required=True)
    setting.add_argument("--amount", required=True)
    showing = budgets.add_parser("show", help="예산 조회")
    showing.add_argument("--month", help="미지정 시 전체 월")
    category = commands.add_parser("category", help="카테고리 관리")
    categories = category.add_subparsers(dest="action", required=True, parser_class=Parser)
    for name in ("add", "list", "remove"):
        categories.add_parser(name, help={"add": "대화형 추가", "list": "목록", "remove": "대화형 삭제"}[name])
    importing = commands.add_parser("import", help="UTF-8 CSV 일괄 등록 (실패 시 전체 취소)")
    importing.add_argument("--from", dest="source", required=True, help="CSV 파일 경로")
    exporting = commands.add_parser("export", help="기간 조건을 지정해 CSV 내보내기")
    exporting.add_argument("--out", required=True)
    add_filters(exporting, month=True)
    commands.add_parser("backup", help="타임스탬프 ZIP 백업 생성")
    return root


def add_filters(command: argparse.ArgumentParser, month: bool = False) -> None:
    command.add_argument("--from", dest="start", help="시작일 YYYY-MM-DD (포함)")
    command.add_argument("--to", dest="end", help="종료일 YYYY-MM-DD (포함)")
    if month:
        command.add_argument("--month", help="YYYY-MM, 날짜 범위와 동시 사용 불가")
    command.add_argument("--category")
    command.add_argument("--type", choices=("income", "expense"))
    command.add_argument("--q", help="메모 키워드 (대소문자 무시)")
    command.add_argument("--tag", help="태그 완전 일치")


def filters_from(args: argparse.Namespace) -> Filters:
    return Filters(**{key: getattr(args, key, None)
                      for key in ("start", "end", "month", "category", "type", "q", "tag")})


def display(value: object) -> str:
    """개행/탭/터미널 제어 문자를 화면에서 이스케이프한다."""
    return "".join(f"\\u{ord(c):04x}" if unicodedata.category(c).startswith("C") else c for c in str(value))


def pad(value: str, width: int) -> str:
    cells = sum(2 if unicodedata.east_asian_width(c) in ("W", "F") else 1 for c in value)
    return value + " " * max(0, width - cells)


def print_transactions(transactions: Iterable[Transaction]) -> None:
    count = 0
    print("ID | 날짜 | 타입 | 카테고리 | 금액 | 메모 | 태그")
    for t in transactions:
        print(f"{t.id} | {t.date} | {t.type:7} | {pad(display(t.category), 12)} | "
              f"{t.amount:>10,} | {display(t.memo)} | {display(','.join(t.tags))}")
        count += 1
    print(f"[조회] {count}건" if count else "데이터 없음")


@command_boundary
def execute(args: argparse.Namespace) -> None:
    store = DataStore(Path(args.data_dir))
    with store.session():
        service = BudgetService(store)
        command = args.command
        if command == "add":
            print("등록된 카테고리: " + ", ".join(service.categories()))
            transaction = Transaction.create(
                date=input("날짜(YYYY-MM-DD): ").strip(),
                type=input("타입(income/expense): ").strip(),
                category=input("카테고리: ").strip(),
                amount=input("금액(양수 정수): ").strip(),
                memo=input("메모(선택): "), tags=input("태그(쉼표 구분, 선택): "))
            service.add(transaction)
            print(f"[저장 완료] id={transaction.id}")
        elif command in ("list", "search"):
            limit = positive(args.limit) if args.limit is not None else None
            transactions = service.search(Filters() if command == "list" else filters_from(args))
            print_transactions(islice(transactions, limit))
        elif command == "update":
            changes = {key: getattr(args, key) for key in ("date", "type", "category", "amount", "memo", "tags")
                       if getattr(args, key) is not None}
            service.update(args.id, changes)
            print(f"[수정 완료] id={args.id}")
        elif command == "delete":
            service.delete(args.id)
            print(f"[삭제 완료] id={args.id}")
        elif command == "category":
            if args.action == "list":
                for name in service.categories():
                    print("- " + display(name))
            elif args.action == "add":
                name = service.category_add(input("카테고리명: "))
                print(f"[저장 완료] category={name}")
            else:
                name = input("삭제할 카테고리명: ").strip()
                service.category_remove(name)
                print(f"[삭제 완료] category={name}")
        elif command == "budget":
            if args.action == "set":
                service.set_budget(args.month, args.amount)
                print(f"[저장 완료] {args.month} 예산 {int(args.amount):,}원")
            else:
                from .models import valid_month
                if args.month is not None:
                    valid_month(args.month)
                budgets = service.budgets()
                selected = {m: a for m, a in sorted(budgets.items()) if args.month is None or m == args.month}
                for month, amount in selected.items():
                    print(f"{month}: {amount:,}원")
                if not selected:
                    print("설정된 예산 없음")
        elif command == "summary":
            top = positive(args.top)
            result = service.summary(args.month)
            income, expense = result["income"], result["expense"]
            if not result["count"]:
                print("데이터 없음")
            print(f"총 수입: {income:,}원\n총 지출: {expense:,}원\n잔액: {income - expense:,}원")
            budget = result["budget"]
            if budget is not None:
                print(f"예산: {budget:,}원 (사용률 {expense * 100 / budget:.1f}%)")
                if expense > budget:
                    print(f"[경고] 예산 초과: {expense - budget:,}원")
            print(f"지출 TOP {top}")
            for rank, (category, amount) in enumerate(result["categories"][:top], 1):
                print(f"{rank}) {display(category)} {amount:,}원")
        elif command == "import":
            count = service.import_csv(Path(args.source))
            print(f"[완료] imported={count}, skipped=0")
        elif command == "export":
            count = service.export_csv(Path(args.out), filters_from(args))
            print(f"[완료] {args.out} ({count} records)")
        elif command == "backup":
            print(f"[백업 완료] {service.backup()}")


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.verbose:
        logging.basicConfig(level=logging.INFO, format="[로그] %(message)s")
    return execute(args)
