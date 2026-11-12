from __future__ import annotations

import csv
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

from budget_app.cli import main
from budget_app.models import AppError, Transaction, positive, valid_date
from budget_app.service import BudgetService, Filters
from budget_app.storage import DataStore, read_jsonl, write_jsonl


class BudgetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.store = DataStore(self.root / "data")
        with self.store.session():
            pass
        self.service = BudgetService(self.store)

    def transaction(self, day: str = "2024-01-15", amount: int = 15000,
                    category: str = "food", type: str = "expense", **kwargs: str) -> Transaction:
        return Transaction.create(date=day, amount=amount, category=category, type=type, **kwargs)

    def run_cli(self, *args: str, inputs: list[str] | None = None) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err), patch("builtins.input", side_effect=inputs or []):
            code = main(["--data-dir", str(self.store.directory), *args])
        return code, out.getvalue(), err.getvalue()

    def csv_file(self, rows: list[list[str]], header: tuple[str, ...] = ("date", "type", "category", "amount", "memo", "tags")) -> Path:
        path = self.root / "input.csv"
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(header)
            writer.writerows(rows)
        return path

    def test_initialization_creates_three_files_and_defaults(self) -> None:
        for name in self.store.FILES:
            self.assertTrue((self.store.directory / name).exists())
        self.assertIn("food", self.service.categories())

    def test_empty_categories_reinitialized(self) -> None:
        self.store.path("categories").write_text("", encoding="utf-8")
        with self.store.session():
            self.assertIn("salary", self.service.categories())

    def test_invalid_dates_and_amounts(self) -> None:
        for value in ("2024-02-30", "2024-1-01", "0000-01-01", "2024-13-01"):
            with self.subTest(value=value), self.assertRaises(AppError):
                valid_date(value)
        self.assertEqual(valid_date("2024-02-29"), "2024-02-29")
        for value in (0, -1, True, "1.5", "x", "9" * 5000, 9223372036854775808):
            with self.subTest(value=str(value)[:20]), self.assertRaises(AppError):
                positive(value)

    def test_add_persists_and_streams_in_date_order(self) -> None:
        for day in ("2024-01-15", "2024-02-01", "2024-01-01", "2024-01-15"):
            self.service.add(self.transaction(day))
        iterator = self.service.transactions.iter_all()
        self.assertIs(iter(iterator), iterator)
        keys = [t.key for t in iterator]
        self.assertEqual(keys, sorted(keys, reverse=True))
        self.assertEqual(len({t.id for t in BudgetService(self.store).transactions.iter_all()}), 4)

    def test_invalid_category_and_type_do_not_write(self) -> None:
        before = self.store.path("transactions").read_bytes()
        with self.assertRaises(AppError):
            self.service.add(self.transaction(category="unknown"))
        with self.assertRaises(AppError):
            self.transaction(type="other")
        self.assertEqual(before, self.store.path("transactions").read_bytes())

    def test_update_reorders_and_clears_optional_fields(self) -> None:
        transaction = self.transaction(memo="old", tags="a,b")
        self.service.add(transaction)
        self.service.add(self.transaction("2024-02-01"))
        self.service.update(transaction.id, {"date": "2024-03-01", "amount": "12", "memo": "", "tags": ""})
        first = next(self.service.transactions.iter_all())
        self.assertEqual((first.id, first.amount, first.memo, first.tags), (transaction.id, 12, "", ()))
        self.service.update(transaction.id, {"date": "2023-01-01"})
        self.assertEqual(list(self.service.transactions.iter_all())[-1].id, transaction.id)

    def test_delete_and_missing_id(self) -> None:
        transaction = self.transaction()
        self.service.add(transaction)
        self.service.delete(transaction.id)
        self.assertEqual(list(self.service.transactions.iter_all()), [])
        for method in (lambda: self.service.delete("missing"), lambda: self.service.update("missing", {"memo": "x"})):
            with self.assertRaisesRegex(AppError, "없는 데이터"):
                method()

    def test_failed_update_preserves_bytes(self) -> None:
        transaction = self.transaction()
        self.service.add(transaction)
        before = self.store.path("transactions").read_bytes()
        for changes in ({"amount": "0"}, {"date": "wrong"}, {"category": "missing"}, {}):
            with self.subTest(changes=changes), self.assertRaises(AppError):
                self.service.update(transaction.id, changes)
            self.assertEqual(before, self.store.path("transactions").read_bytes())

    def test_search_combines_all_conditions_inclusively(self) -> None:
        selected = self.transaction(memo="Lunch MEAL", tags="work,meal,work")
        self.service.add(selected)
        self.service.add(self.transaction("2024-01-16", memo="meal", tags="meal"))
        filters = Filters(start="2024-01-15", end="2024-01-15", type="expense", category="food", q="meal", tag="work")
        self.assertEqual(list(self.service.search(filters)), [selected])
        self.assertEqual(selected.tags, ("work", "meal"))
        self.assertEqual(list(self.service.search(Filters(tag="wor"))), [])

    def test_invalid_filters(self) -> None:
        for args in ({"start": "2024-03-01", "end": "2024-01-01"}, {"month": "2024-13"},
                     {"month": "2024-01", "start": "2024-01-01"}):
            with self.subTest(args=args), self.assertRaises(AppError):
                Filters(**args)

    def test_summary_budget_and_warning(self) -> None:
        for transaction in (self.transaction(amount=100), self.transaction(amount=200, category="rent"),
                            self.transaction(amount=1000, category="salary", type="income"), self.transaction("2024-02-01")):
            self.service.add(transaction)
        self.service.set_budget("2024-01", "250")
        result = self.service.summary("2024-01")
        self.assertEqual((result["income"], result["expense"], result["budget"]), (1000, 300, 250))
        self.assertEqual(result["categories"], [("rent", 200), ("food", 100)])
        code, out, _ = self.run_cli("summary", "--month", "2024-01", "--top", "1")
        self.assertEqual(code, 0)
        self.assertIn("120.0%", out)
        self.assertIn("예산 초과", out)
        self.assertNotIn("2) food", out)

    def test_empty_summary_still_shows_budget(self) -> None:
        self.service.set_budget("2024-02", 10)
        code, out, _ = self.run_cli("summary", "--month", "2024-02")
        self.assertEqual(code, 0)
        self.assertIn("데이터 없음", out)
        self.assertIn("0.0%", out)

    def test_category_usage_and_duplicate_guard(self) -> None:
        self.service.category_add("leisure")
        with self.assertRaises(AppError):
            self.service.category_add("leisure")
        self.service.category_remove("leisure")
        self.service.add(self.transaction())
        with self.assertRaisesRegex(AppError, "사용 중"):
            self.service.category_remove("food")

    def test_import_and_export_roundtrip_unicode_quotes_and_tags(self) -> None:
        path = self.csv_file([["2024-01-01", "expense", "food", "1200", '한글, "메모"\n두 줄', "a,b"],
                              ["2024-01-31", "income", "salary", "3000", "월급", ""]])
        self.assertEqual(self.service.import_csv(path), 2)
        exported = self.root / "export.csv"
        self.assertEqual(self.service.export_csv(exported, Filters(month="2024-01")), 2)
        with exported.open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(rows[1]["memo"], '한글, "메모"\n두 줄')
        self.assertEqual(rows[1]["tags"], "a,b")
        second = DataStore(self.root / "second")
        with second.session():
            self.assertEqual(BudgetService(second).import_csv(exported), 2)

    def test_import_invalid_later_row_rolls_back_everything(self) -> None:
        self.service.add(self.transaction())
        before = self.store.path("transactions").read_bytes()
        path = self.csv_file([["2024-01-01", "expense", "food", "10", "valid", ""],
                              ["2024-01-02", "expense", "food", "0", "invalid", ""]])
        with self.assertRaisesRegex(AppError, "CSV 3행"):
            self.service.import_csv(path)
        self.assertEqual(before, self.store.path("transactions").read_bytes())
        self.assertEqual(list(self.store.directory.glob(".import-*")), [])

    def test_import_bad_headers_unknown_category_and_bad_encoding(self) -> None:
        path = self.csv_file([], header=("date", "type", "category", "amount", "amount"))
        with self.assertRaises(AppError):
            self.service.import_csv(path)
        path = self.csv_file([["2024-01-01", "expense", "missing", "10", "", ""]])
        self.assertNotEqual(self.run_cli("import", "--from", str(path))[0], 0)
        path.write_bytes(b"\xff\xff")
        code, _, err = self.run_cli("import", "--from", str(path))
        self.assertNotEqual(code, 0)
        self.assertNotIn("Traceback", err)

    def test_optional_csv_columns_and_bom(self) -> None:
        path = self.csv_file([["2024-01-01", "expense", "food", "1"]], header=("date", "type", "category", "amount"))
        path.write_bytes(b"\xef\xbb\xbf" + path.read_bytes())
        self.assertEqual(self.service.import_csv(path), 1)

    def test_export_requires_period_and_protects_data(self) -> None:
        with self.assertRaises(AppError):
            self.service.export_csv(self.root / "out.csv", Filters())
        for name in self.store.FILES:
            path = self.store.directory / name
            before = path.read_bytes()
            with self.assertRaises(AppError):
                self.service.export_csv(path, Filters(month="2024-01"))
            self.assertEqual(before, path.read_bytes())

    def test_export_range_and_empty_header(self) -> None:
        self.service.add(self.transaction())
        path = self.root / "out.csv"
        self.assertEqual(self.service.export_csv(path, Filters(start="2024-01-15", end="2024-01-15")), 1)
        self.assertEqual(self.service.export_csv(path, Filters(month="2023-01")), 0)
        self.assertEqual(len(path.read_text(encoding="utf-8").splitlines()), 1)

    def test_atomic_write_failure_does_not_truncate_original(self) -> None:
        self.service.add(self.transaction())
        path = self.store.path("transactions")
        before = path.read_bytes()
        def records():
            yield {"partial": True}
            raise OSError("simulated disk failure")
        with self.assertRaises(OSError):
            write_jsonl(path, records())
        self.assertEqual(path.read_bytes(), before)
        with patch("budget_app.storage.os.replace", side_effect=PermissionError("simulated replace failure")):
            with self.assertRaises(PermissionError):
                self.service.add(self.transaction())
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(list(self.store.directory.glob(".budget-*.tmp")), [])

    def test_corruption_during_rewrite_preserves_original(self) -> None:
        self.service.add(self.transaction())
        path = self.store.path("transactions")
        with path.open("a", encoding="utf-8") as stream:
            stream.write("{broken\n")
        before = path.read_bytes()
        with self.assertRaises(AppError):
            self.service.add(self.transaction())
        self.assertEqual(before, path.read_bytes())

    def test_invalid_schema_and_sort_order_are_reported(self) -> None:
        path = self.store.path("transactions")
        for rows in ([{"id": "bad"}], [self.transaction("2024-01-01").record(), self.transaction("2024-02-01").record()]):
            write_jsonl(path, rows)
            with self.assertRaises(AppError):
                list(self.service.transactions.iter_all())

    def test_lock_blocks_second_command_and_cleans_up(self) -> None:
        with self.store.session():
            with self.assertRaises(AppError):
                with DataStore(self.store.directory).session():
                    self.fail("lock bypass")
        self.assertFalse((self.store.directory / ".budget.lock").exists())
        with self.assertRaises(RuntimeError):
            with self.store.session():
                raise RuntimeError("test")
        self.assertFalse((self.store.directory / ".budget.lock").exists())

    def test_backup_contains_all_persistent_files(self) -> None:
        self.service.add(self.transaction())
        path = self.service.backup()
        self.assertNotEqual(path, self.service.backup())
        with zipfile.ZipFile(path) as archive:
            self.assertEqual(set(archive.namelist()), set(self.store.FILES))
            for name in self.store.FILES:
                self.assertEqual(archive.read(name), (self.store.directory / name).read_bytes())

    def test_interactive_add_and_list_limit(self) -> None:
        inputs = ["2024-01-15", "expense", "food", "15000", "점심", "meal"]
        code, out, _ = self.run_cli("add", inputs=inputs)
        self.assertEqual(code, 0)
        self.assertIn("id=TX-", out)
        self.service.add(self.transaction())
        code, out, _ = self.run_cli("list", "--limit", "1")
        self.assertEqual(code, 0)
        self.assertEqual(out.count("TX-"), 1)

    def test_cli_error_and_cancel_have_no_traceback(self) -> None:
        code, _, err = self.run_cli("delete", "--id", "unknown")
        self.assertEqual(code, 1)
        self.assertIn("[힌트]", err)
        self.assertNotIn("Traceback", err)
        with patch("builtins.input", side_effect=EOFError), redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()):
            self.assertEqual(main(["--data-dir", str(self.store.directory), "add"]), 130)

    def test_cli_budget_category_and_search(self) -> None:
        self.assertEqual(self.run_cli("category", "add", inputs=["취미"])[0], 0)
        self.assertIn("취미", self.run_cli("category", "list")[1])
        self.assertEqual(self.run_cli("category", "remove", inputs=["취미"])[0], 0)
        self.assertEqual(self.run_cli("budget", "set", "--month", "2024-01", "--amount", "100")[0], 0)
        self.assertIn("100원", self.run_cli("budget", "show", "--month", "2024-01")[1])
        self.assertIn("데이터 없음", self.run_cli("search", "--q", "none")[1])

    def test_cli_update_delete_export_import_and_backup(self) -> None:
        t = self.transaction()
        self.service.add(t)
        self.assertEqual(self.run_cli("update", "--id", t.id, "--memo", "new")[0], 0)
        self.assertEqual(self.service.transactions.find(t.id).memo, "new")
        out = str(self.root / "out.csv")
        self.assertEqual(self.run_cli("export", "--out", out, "--month", "2024-01")[0], 0)
        self.assertEqual(self.run_cli("delete", "--id", t.id)[0], 0)
        self.assertIn("imported=1", self.run_cli("import", "--from", out)[1])
        self.assertEqual(self.run_cli("backup")[0], 0)

    def test_subprocess_entrypoint_exit_codes_and_all_help(self) -> None:
        commands = [[], ["add"], ["list"], ["search"], ["summary"], ["update"], ["delete"],
                    ["import"], ["export"], ["backup"], ["budget"], ["budget", "set"], ["budget", "show"],
                    ["category"], ["category", "add"], ["category", "list"], ["category", "remove"]]
        env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
        for command in commands:
            result = subprocess.run([sys.executable, "-m", "budget_app", *command, "--help"],
                                    capture_output=True, encoding="utf-8", env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([sys.executable, "-m", "budget_app", "delete"], capture_output=True, encoding="utf-8", env=env)
        self.assertEqual(result.returncode, 2)
        self.assertIn("[힌트]", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_limit_does_not_read_entire_transaction_file(self) -> None:
        self.service.add(self.transaction())
        with self.store.path("transactions").open("a", encoding="utf-8") as stream:
            stream.write("{bad trailing row\n")
        # --limit 1은 두 번째 줄을 파싱하지 않아야 한다.
        code, out, _ = self.run_cli("list", "--limit", "1")
        self.assertEqual(code, 0)
        self.assertIn("1건", out)
        self.assertEqual(self.run_cli("list", "--limit", "2")[0], 1)


if __name__ == "__main__":
    unittest.main()
