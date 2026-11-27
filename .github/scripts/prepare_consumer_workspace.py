"""Validate the installed native package without importing source from the checkout."""

import os
from pathlib import (
    Path,
)
import shutil
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parents[2]
    target = Path(os.environ["RUNNER_TEMP"]) / "abi-consumer"
    target.mkdir(parents=True, exist_ok=True)
    for relative in (
        "pyproject.toml",
        "scripts/generate_overload_tests.py",
        "scripts/run_overload_tests.py",
        "tests/typecheck/overload_boundaries.py",
        ".github/scripts/test_overload_generation.py",
    ):
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / relative, destination)
    subprocess.run(
        [
            sys.executable,
            "-c",
            "import importlib.machinery as m; import faster_eth_abi.abi as abi; "
            "assert any(abi.__file__.endswith(s) for s in m.EXTENSION_SUFFIXES), "
            "abi.__file__; print('Installed native ABI:', abi.__file__)",
        ],
        cwd=target,
        check=True,
    )


if __name__ == "__main__":
    main()
