import tempfile
import unittest
from pathlib import Path
from tools.check_mlog import check


class CheckMlogTest(unittest.TestCase):
    def evaluate(self, code):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.mlog"
            path.write_text(code, encoding="utf-8")
            return check(path)

    def test_line_zero_and_last_line_are_valid(self):
        errors, _, total = self.evaluate("set a 1\njump 0 always 0 0\njump 2 always 0 0\n")
        self.assertEqual((errors, total), ([], 3))

    def test_jump_past_end_fails(self):
        errors, _, _ = self.evaluate("set a 1\njump 2 always 0 0\n")
        self.assertTrue(any("fora das linhas" in error for error in errors))

    def test_pseudocode_labels_fail(self):
        errors, _, _ = self.evaluate("loop:\nunit bind @mono\n")
        self.assertEqual(len(errors), 2)

    def test_dynamic_jump_is_warning(self):
        errors, warnings, _ = self.evaluate("set next 0\njump next always 0 0\n")
        self.assertEqual(errors, [])
        self.assertTrue(any("dinâmico" in warning for warning in warnings))


if __name__ == "__main__":
    unittest.main()
