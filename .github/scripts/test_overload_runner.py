"""Protect the type assertion checks from masked or absent results."""

import importlib.util
from pathlib import (
    Path,
)
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    "run_overload_tests", Path(__file__).parents[2] / "scripts/run_overload_tests.py"
)
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class ConsumerTypeCheckTests(unittest.TestCase):
    def test_retains_failure_and_diagnostics(self):
        def run(command, **kwargs):
            config = runner.tomllib.loads(Path(command[-1]).read_text())["tool"]["mypy"]
            self.assertEqual(config["follow_imports"], "silent")
            self.assertEqual(config["files"], [str(Path("bad.py").resolve())])
            self.assertNotIn("disable_error_code", config)
            return subprocess.CompletedProcess(command, 1, "assertion failed\n")

        status, output = runner.check_file(
            Path("bad.py"), {"follow_imports": "silent"}, run
        )
        self.assertEqual(status, 1)
        self.assertIn("assertion failed", output)
        self.assertIn("[MYPY-TIME]", output)

    def test_empty_fixtures_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "pyproject.toml").write_text(
                '[tool.consumer-mypy]\nfiles = "tests/{impl}/{suite}/{length}"\n'
            )
            with self.assertRaisesRegex(ValueError, "No type assertion files"):
                runner.run_checks(root, "abi", "fixed", 1)

    def test_later_parallel_failure_is_not_lost(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "pyproject.toml").write_text(
                '[tool.consumer-mypy]\nfiles = "tests/{impl}/{suite}/{length}"\n'
                '[tool.consumer-mypy.workers]\n"3" = 2\n'
                '[tool.consumer-mypy.settings]\nfollow_imports = "silent"\n'
            )
            fixtures = root / "tests/abi/fixed/3"
            fixtures.mkdir(parents=True)
            (fixtures / "good.py").touch()
            (fixtures / "bad.py").touch()

            def run(command, **kwargs):
                content = Path(command[-1]).read_text()
                return subprocess.CompletedProcess(
                    command, int("bad.py" in content), "diagnostic\n"
                )

            self.assertEqual(runner.run_checks(root, "abi", "fixed", 3, run), 1)


if __name__ == "__main__":
    unittest.main()
