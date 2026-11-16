# 회귀 테스트: 기능과 실패 시 데이터 보존을 함께 확인합니다.
# 모든 저장 작업은 TemporaryDirectory 안에서 하므로 실제 data에는 영향을 주지 않습니다.
# assertEqual은 값 일치, assertRaises는 예상 오류 발생을 검사합니다.
# 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다.
from __future__ import annotations

# 쉼표·인용·개행을 직접 나누지 않고 표준 CSV 규칙으로 처리합니다.
import csv
# 테스트에서 화면 출력을 파일 대신 메모리 문자열에 수집합니다.
import io
# JSONL의 한 줄을 dict로 읽거나 JSON 문자열로 저장합니다.
import json
# 파일 디스크립터·잠금 플래그·fsync·원자적 파일 교체 같은 운영체제 기능입니다.
import os
# 실제 별도 Python 프로세스로 진입점과 종료 코드를 테스트합니다.
import subprocess
# 오류 출력 스트림과 프로세스 실행 관련 정보를 사용합니다.
import sys
# 임시 파일/폴더를 고유 이름으로 만들고 안전하게 정리합니다.
import tempfile
# 표준 라이브러리 테스트 실행기와 검증 메서드를 사용합니다.
import unittest
# 세 저장 파일의 ZIP 백업을 만들거나 테스트에서 검사합니다.
import zipfile
# 테스트 중 정상 출력과 오류 출력을 각각 수집합니다.
from contextlib import redirect_stderr, redirect_stdout
# 문자열 연결 대신 경로·파일 처리를 담당하는 표준 객체입니다.
from pathlib import Path
# 사용자 입력이나 파일 교체 실패를 테스트에서 통제합니다.
from unittest.mock import patch

# CLI의 main 함수를 모듈 실행 진입점에 연결합니다.
from budget_app.cli import main
# 테스트에서 모델 검증 함수와 예상 오류를 직접 확인합니다.
from budget_app.models import AppError, Transaction, positive, valid_date
# CLI 또는 테스트가 서비스 업무 규칙과 검색 조건 객체를 사용합니다.
from budget_app.service import BudgetService, Filters
# 테스트 데이터 초기화와 손상 시나리오를 구성하는 저장 도우미입니다.
from budget_app.storage import DataStore, read_jsonl, write_jsonl


# unittest가 test_로 시작하는 30개 메서드를 찾아 각각 독립된 데이터로 검증합니다.
class BudgetTests(unittest.TestCase):
    # 각 테스트 전에 임시 데이터 폴더를 만들고 초기 파일 및 서비스를 준비합니다.
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.store = DataStore(self.root / "data")
        with self.store.session():
            pass
        self.service = BudgetService(self.store)

    # 테스트에 필요한 유효한 거래를 만드는 공통 도우미입니다.
    def transaction(self, day: str = "2024-01-15", amount: int = 15000,
                    category: str = "food", type: str = "expense", **kwargs: str) -> Transaction:
        return Transaction.create(date=day, amount=amount, category=category, type=type, **kwargs)

    # 실제 키보드 대신 입력 목록을 제공하고 종료 코드·표준 출력·오류 출력을 수집합니다.
    def run_cli(self, *args: str, inputs: list[str] | None = None) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err), patch("builtins.input", side_effect=inputs or []):
            code = main(["--data-dir", str(self.store.directory), *args])
        return code, out.getvalue(), err.getvalue()

    # 검증할 CSV를 임시 폴더에 만들어 경로를 반환하는 도우미입니다.
    def csv_file(self, rows: list[list[str]], header: tuple[str, ...] = ("date", "type", "category", "amount", "memo", "tags")) -> Path:
        path = self.root / "input.csv"
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(header)
            writer.writerows(rows)
        return path

    # 초기화가 세 저장 파일과 기본 카테고리를 만드는지 검증합니다.
    def test_initialization_creates_three_files_and_defaults(self) -> None:
        for name in self.store.FILES:
            # 필요한 저장 파일이 실제로 생성되었는지 확인합니다.
            self.assertTrue((self.store.directory / name).exists())
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("food", self.service.categories())

    # 0바이트 카테고리 파일에 기본 이름이 재생성되는 정책을 확인합니다.
    def test_empty_categories_reinitialized(self) -> None:
        self.store.path("categories").write_text("", encoding="utf-8")
        with self.store.session():
            # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
            self.assertIn("salary", self.service.categories())

    # 잘못된 날짜·윤년·금액 범위·bool·과도한 길이 입력을 검증합니다.
    def test_invalid_dates_and_amounts(self) -> None:
        for value in ("2024-02-30", "2024-1-01", "0000-01-01", "2024-13-01"):
            with self.subTest(value=value), self.assertRaises(AppError):
                valid_date(value)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(valid_date("2024-02-29"), "2024-02-29")
        for value in (0, -1, True, "1.5", "x", "9" * 5000, 9223372036854775808):
            with self.subTest(value=str(value)[:20]), self.assertRaises(AppError):
                positive(value)

    # C/R: 추가 후 고유 id, 제너레이터 및 최신순 영구 저장을 확인합니다.
    def test_add_persists_and_streams_in_date_order(self) -> None:
        for day in ("2024-01-15", "2024-02-01", "2024-01-01", "2024-01-15"):
            self.service.add(self.transaction(day))
        iterator = self.service.transactions.iter_all()
        # 같은 이터레이터 객체인지 비교해 반복자가 그대로 사용되는지 검사합니다.
        self.assertIs(iter(iterator), iterator)
        keys = [t.key for t in iterator]
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(keys, sorted(keys, reverse=True))
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(len({t.id for t in BudgetService(self.store).transactions.iter_all()}), 4)

    # 유효하지 않은 카테고리·타입이 원본 파일을 바꾸지 않는지 확인합니다.
    def test_invalid_category_and_type_do_not_write(self) -> None:
        # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.
        before = self.store.path("transactions").read_bytes()
        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
        with self.assertRaises(AppError):
            self.service.add(self.transaction(category="unknown"))
        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
        with self.assertRaises(AppError):
            self.transaction(type="other")
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(before, self.store.path("transactions").read_bytes())

    # U: 날짜 변경 시 순서 재배치와 메모·태그 비우기를 확인합니다.
    def test_update_reorders_and_clears_optional_fields(self) -> None:
        transaction = self.transaction(memo="old", tags="a,b")
        self.service.add(transaction)
        self.service.add(self.transaction("2024-02-01"))
        self.service.update(transaction.id, {"date": "2024-03-01", "amount": "12", "memo": "", "tags": ""})
        first = next(self.service.transactions.iter_all())
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual((first.id, first.amount, first.memo, first.tags), (transaction.id, 12, "", ()))
        self.service.update(transaction.id, {"date": "2023-01-01"})
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(list(self.service.transactions.iter_all())[-1].id, transaction.id)

    # D: 삭제 성공 및 없는 id의 삭제·수정 거부를 검증합니다.
    def test_delete_and_missing_id(self) -> None:
        transaction = self.transaction()
        self.service.add(transaction)
        self.service.delete(transaction.id)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(list(self.service.transactions.iter_all()), [])
        for method in (lambda: self.service.delete("missing"), lambda: self.service.update("missing", {"memo": "x"})):
            # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
            with self.assertRaisesRegex(AppError, "없는 데이터"):
                method()

    # 잘못된 수정 요청 전후 파일 바이트를 비교해 원본 보존을 확인합니다.
    def test_failed_update_preserves_bytes(self) -> None:
        transaction = self.transaction()
        self.service.add(transaction)
        # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.
        before = self.store.path("transactions").read_bytes()
        for changes in ({"amount": "0"}, {"date": "wrong"}, {"category": "missing"}, {}):
            with self.subTest(changes=changes), self.assertRaises(AppError):
                self.service.update(transaction.id, changes)
            # 실제 값과 기대값이 같아야 통과합니다.
            self.assertEqual(before, self.store.path("transactions").read_bytes())

    # 날짜 경계 포함, AND 검색, 태그 중복 제거와 완전 일치를 확인합니다.
    def test_search_combines_all_conditions_inclusively(self) -> None:
        selected = self.transaction(memo="Lunch MEAL", tags="work,meal,work")
        self.service.add(selected)
        self.service.add(self.transaction("2024-01-16", memo="meal", tags="meal"))
        filters = Filters(start="2024-01-15", end="2024-01-15", type="expense", category="food", q="meal", tag="work")
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(list(self.service.search(filters)), [selected])
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(selected.tags, ("work", "meal"))
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(list(self.service.search(Filters(tag="wor"))), [])

    # 역전된 기간·없는 월·월과 범위의 충돌을 거부하는지 확인합니다.
    def test_invalid_filters(self) -> None:
        for args in ({"start": "2024-03-01", "end": "2024-01-01"}, {"month": "2024-13"},
                     {"month": "2024-01", "start": "2024-01-01"}):
            with self.subTest(args=args), self.assertRaises(AppError):
                Filters(**args)

    # 해당 월만 합산하고 TOP 제한·예산 사용률·초과 경고가 맞는지 검증합니다.
    def test_summary_budget_and_warning(self) -> None:
        for transaction in (self.transaction(amount=100), self.transaction(amount=200, category="rent"),
                            self.transaction(amount=1000, category="salary", type="income"), self.transaction("2024-02-01")):
            self.service.add(transaction)
        self.service.set_budget("2024-01", "250")
        result = self.service.summary("2024-01")
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual((result["income"], result["expense"], result["budget"]), (1000, 300, 250))
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(result["categories"], [("rent", 200), ("food", 100)])
        code, out, _ = self.run_cli("summary", "--month", "2024-01", "--top", "1")
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(code, 0)
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("120.0%", out)
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("예산 초과", out)
        # 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다.
        self.assertNotIn("2) food", out)

    # 거래 없는 월도 데이터 없음과 설정 예산 0%를 출력하는지 확인합니다.
    def test_empty_summary_still_shows_budget(self) -> None:
        self.service.set_budget("2024-02", 10)
        code, out, _ = self.run_cli("summary", "--month", "2024-02")
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(code, 0)
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("데이터 없음", out)
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("0.0%", out)

    # 중복 추가 거부와 사용 중 카테고리 삭제 보호를 확인합니다.
    def test_category_usage_and_duplicate_guard(self) -> None:
        self.service.category_add("leisure")
        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
        with self.assertRaises(AppError):
            self.service.category_add("leisure")
        self.service.category_remove("leisure")
        self.service.add(self.transaction())
        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
        with self.assertRaisesRegex(AppError, "사용 중"):
            self.service.category_remove("food")

    # CSV 가져오기→내보내기→재가져오기에서 한글·인용·개행·태그 보존을 확인합니다.
    def test_import_and_export_roundtrip_unicode_quotes_and_tags(self) -> None:
        path = self.csv_file([["2024-01-01", "expense", "food", "1200", '한글, "메모"\n두 줄', "a,b"],
                              ["2024-01-31", "income", "salary", "3000", "월급", ""]])
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.service.import_csv(path), 2)
        exported = self.root / "export.csv"
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.service.export_csv(exported, Filters(month="2024-01")), 2)
        with exported.open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(rows[1]["memo"], '한글, "메모"\n두 줄')
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(rows[1]["tags"], "a,b")
        second = DataStore(self.root / "second")
        with second.session():
            # 실제 값과 기대값이 같아야 통과합니다.
            self.assertEqual(BudgetService(second).import_csv(exported), 2)

    # 두 번째 행 실패 시 첫 번째 행도 반영되지 않는 전체 취소를 검증합니다.
    def test_import_invalid_later_row_rolls_back_everything(self) -> None:
        self.service.add(self.transaction())
        # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.
        before = self.store.path("transactions").read_bytes()
        path = self.csv_file([["2024-01-01", "expense", "food", "10", "valid", ""],
                              ["2024-01-02", "expense", "food", "0", "invalid", ""]])
        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
        with self.assertRaisesRegex(AppError, "CSV 3행"):
            self.service.import_csv(path)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(before, self.store.path("transactions").read_bytes())
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(list(self.store.directory.glob(".import-*")), [])

    # 중복 헤더·미등록 카테고리·깨진 인코딩을 안전하게 거부하는지 확인합니다.
    def test_import_bad_headers_unknown_category_and_bad_encoding(self) -> None:
        path = self.csv_file([], header=("date", "type", "category", "amount", "amount"))
        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
        with self.assertRaises(AppError):
            self.service.import_csv(path)
        path = self.csv_file([["2024-01-01", "expense", "missing", "10", "", ""]])
        # 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다.
        self.assertNotEqual(self.run_cli("import", "--from", str(path))[0], 0)
        path.write_bytes(b"\xff\xff")
        code, _, err = self.run_cli("import", "--from", str(path))
        # 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다.
        self.assertNotEqual(code, 0)
        # 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다.
        self.assertNotIn("Traceback", err)

    # 선택 열이 없거나 UTF-8 BOM이 있는 정상 CSV를 허용하는지 확인합니다.
    def test_optional_csv_columns_and_bom(self) -> None:
        path = self.csv_file([["2024-01-01", "expense", "food", "1"]], header=("date", "type", "category", "amount"))
        path.write_bytes(b"\xef\xbb\xbf" + path.read_bytes())
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.service.import_csv(path), 1)

    # 기간 없는 내보내기와 실제 저장 파일 덮어쓰기를 막는지 검증합니다.
    def test_export_requires_period_and_protects_data(self) -> None:
        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
        with self.assertRaises(AppError):
            self.service.export_csv(self.root / "out.csv", Filters())
        for name in self.store.FILES:
            path = self.store.directory / name
            # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.
            before = path.read_bytes()
            # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
            with self.assertRaises(AppError):
                self.service.export_csv(path, Filters(month="2024-01"))
            # 실제 값과 기대값이 같아야 통과합니다.
            self.assertEqual(before, path.read_bytes())

    # 기간 경계를 포함하며 결과 0건이어도 CSV 헤더는 만드는지 확인합니다.
    def test_export_range_and_empty_header(self) -> None:
        self.service.add(self.transaction())
        path = self.root / "out.csv"
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.service.export_csv(path, Filters(start="2024-01-15", end="2024-01-15")), 1)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.service.export_csv(path, Filters(month="2023-01")), 0)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(len(path.read_text(encoding="utf-8").splitlines()), 1)

    # 쓰기 도중 오류와 os.replace 실패를 주입해 원본·임시 파일 정리를 검증합니다.
    def test_atomic_write_failure_does_not_truncate_original(self) -> None:
        self.service.add(self.transaction())
        path = self.store.path("transactions")
        # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.
        before = path.read_bytes()
        # 일부 기록 뒤 고의 오류를 내는 제너레이터로 저장 실패를 재현합니다.
        def records():
            yield {"partial": True}
            raise OSError("simulated disk failure")
        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
        with self.assertRaises(OSError):
            write_jsonl(path, records())
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(path.read_bytes(), before)
        # 실제 사용자 입력/운영체제 기능을 대신하는 조건을 주입해 실패 경로를 재현합니다.
        with patch("budget_app.storage.os.replace", side_effect=PermissionError("simulated replace failure")):
            # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
            with self.assertRaises(PermissionError):
                self.service.add(self.transaction())
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(path.read_bytes(), before)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(list(self.store.directory.glob(".budget-*.tmp")), [])

    # 파일 뒤쪽 손상을 만났을 때 새 저장으로 손상 원본을 덮어쓰지 않는지 확인합니다.
    def test_corruption_during_rewrite_preserves_original(self) -> None:
        self.service.add(self.transaction())
        path = self.store.path("transactions")
        with path.open("a", encoding="utf-8") as stream:
            stream.write("{broken\n")
        # 실패 전 원본 바이트를 보관해 나중에 단 한 바이트도 바뀌지 않았는지 비교합니다.
        before = path.read_bytes()
        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
        with self.assertRaises(AppError):
            self.service.add(self.transaction())
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(before, path.read_bytes())

    # 필드 누락과 정렬 손상이 거래 읽기에서 보고되는지 확인합니다.
    def test_invalid_schema_and_sort_order_are_reported(self) -> None:
        path = self.store.path("transactions")
        for rows in ([{"id": "bad"}], [self.transaction("2024-01-01").record(), self.transaction("2024-02-01").record()]):
            write_jsonl(path, rows)
            # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
            with self.assertRaises(AppError):
                list(self.service.transactions.iter_all())

    # 두 번째 세션을 막고 정상·예외 종료에서 잠금을 정리하는지 검증합니다.
    def test_lock_blocks_second_command_and_cleans_up(self) -> None:
        with self.store.session():
            # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
            with self.assertRaises(AppError):
                with DataStore(self.store.directory).session():
                    self.fail("lock bypass")
        # 정리 후 잠금 파일 등이 남아 있지 않아야 합니다.
        self.assertFalse((self.store.directory / ".budget.lock").exists())
        # 오류가 발생해야 통과하는 검증입니다. 오류가 없으면 테스트 실패입니다.
        with self.assertRaises(RuntimeError):
            with self.store.session():
                raise RuntimeError("test")
        # 정리 후 잠금 파일 등이 남아 있지 않아야 합니다.
        self.assertFalse((self.store.directory / ".budget.lock").exists())

    # 백업 이름 구별 및 ZIP 안의 세 파일 이름·바이트 일치를 확인합니다.
    def test_backup_contains_all_persistent_files(self) -> None:
        self.service.add(self.transaction())
        path = self.service.backup()
        # 두 값이 달라야 통과합니다. 오류 코드 검사에서는 0과 다름을 확인합니다.
        self.assertNotEqual(path, self.service.backup())
        with zipfile.ZipFile(path) as archive:
            # 실제 값과 기대값이 같아야 통과합니다.
            self.assertEqual(set(archive.namelist()), set(self.store.FILES))
            for name in self.store.FILES:
                # 실제 값과 기대값이 같아야 통과합니다.
                self.assertEqual(archive.read(name), (self.store.directory / name).read_bytes())

    # 대화형 입력 저장과 --limit 1이 한 건만 출력하는지 확인합니다.
    def test_interactive_add_and_list_limit(self) -> None:
        inputs = ["2024-01-15", "expense", "food", "15000", "점심", "meal"]
        code, out, _ = self.run_cli("add", inputs=inputs)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(code, 0)
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("id=TX-", out)
        self.service.add(self.transaction())
        code, out, _ = self.run_cli("list", "--limit", "1")
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(code, 0)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(out.count("TX-"), 1)

    # 없는 id와 EOF 취소에서 힌트·종료 코드·스택트레이스 생략을 확인합니다.
    def test_cli_error_and_cancel_have_no_traceback(self) -> None:
        code, _, err = self.run_cli("delete", "--id", "unknown")
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(code, 1)
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("[힌트]", err)
        # 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다.
        self.assertNotIn("Traceback", err)
        # 실제 사용자 입력/운영체제 기능을 대신하는 조건을 주입해 실패 경로를 재현합니다.
        with patch("builtins.input", side_effect=EOFError), redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()):
            # 실제 값과 기대값이 같아야 통과합니다.
            self.assertEqual(main(["--data-dir", str(self.store.directory), "add"]), 130)

    # 카테고리·예산·검색 명령을 CLI 경로로 검증합니다.
    def test_cli_budget_category_and_search(self) -> None:
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.run_cli("category", "add", inputs=["취미"])[0], 0)
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("취미", self.run_cli("category", "list")[1])
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.run_cli("category", "remove", inputs=["취미"])[0], 0)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.run_cli("budget", "set", "--month", "2024-01", "--amount", "100")[0], 0)
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("100원", self.run_cli("budget", "show", "--month", "2024-01")[1])
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("데이터 없음", self.run_cli("search", "--q", "none")[1])

    # 여러 CLI 명령을 이어 실행해 거래 변경과 입출력 연결을 검증합니다.
    def test_cli_update_delete_export_import_and_backup(self) -> None:
        t = self.transaction()
        self.service.add(t)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.run_cli("update", "--id", t.id, "--memo", "new")[0], 0)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.service.transactions.find(t.id).memo, "new")
        out = str(self.root / "out.csv")
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.run_cli("export", "--out", out, "--month", "2024-01")[0], 0)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.run_cli("delete", "--id", t.id)[0], 0)
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("imported=1", self.run_cli("import", "--from", out)[1])
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.run_cli("backup")[0], 0)

    # 실제 별도 Python 프로세스로 모든 --help와 인자 오류 코드 2를 확인합니다.
    def test_subprocess_entrypoint_exit_codes_and_all_help(self) -> None:
        commands = [[], ["add"], ["list"], ["search"], ["summary"], ["update"], ["delete"],
                    ["import"], ["export"], ["backup"], ["budget"], ["budget", "set"], ["budget", "show"],
                    ["category"], ["category", "add"], ["category", "list"], ["category", "remove"]]
        env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
        for command in commands:
            result = subprocess.run([sys.executable, "-m", "budget_app", *command, "--help"],
                                    capture_output=True, encoding="utf-8", env=env)
            # 실제 값과 기대값이 같아야 통과합니다.
            self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([sys.executable, "-m", "budget_app", "delete"], capture_output=True, encoding="utf-8", env=env)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(result.returncode, 2)
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("[힌트]", result.stderr)
        # 출력하면 안 되는 값이나 Traceback이 결과에 없는지 확인합니다.
        self.assertNotIn("Traceback", result.stderr)

    # 첫 줄 이후 깨진 행을 둬 --limit 1이 불필요한 읽기를 하지 않는지 확인합니다.
    def test_limit_does_not_read_entire_transaction_file(self) -> None:
        self.service.add(self.transaction())
        with self.store.path("transactions").open("a", encoding="utf-8") as stream:
            stream.write("{bad trailing row\n")
        # --limit 1은 두 번째 줄을 파싱하지 않아야 한다.
        code, out, _ = self.run_cli("list", "--limit", "1")
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(code, 0)
        # 기대한 이름·메시지·필드가 결과 안에 포함되어야 합니다.
        self.assertIn("1건", out)
        # 실제 값과 기대값이 같아야 통과합니다.
        self.assertEqual(self.run_cli("list", "--limit", "2")[0], 1)


if __name__ == "__main__":
    unittest.main()
