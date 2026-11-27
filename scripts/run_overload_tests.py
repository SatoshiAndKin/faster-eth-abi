"""Run consumer assertions with the settings stored in pyproject.toml."""

import argparse
from concurrent.futures import (
    ThreadPoolExecutor,
)
import json
from pathlib import (
    Path,
)
import subprocess
import sys
import tempfile
import time

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


def check_file(path, settings, run=subprocess.run):
    """Keep the actual type check exit status and its full diagnostic output."""
    config = dict(settings)
    config["files"] = [str(path.resolve())]
    content = "[tool.mypy]\n" + "\n".join(
        f"{key} = {json.dumps(value)}" for key, value in config.items()
    )
    start = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="abi-overload-") as directory:
        target = Path(directory) / "pyproject.toml"
        target.write_text(content + "\n")
        result = run(
            [sys.executable, "-m", "mypy", "--config-file", str(target)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
    return result.returncode, (
        result.stdout + f"[MYPY-TIME] {path} took {time.monotonic() - start:.3f}s\n"
    )


def run_checks(root, impl, suite, length, run=subprocess.run):
    """Reject empty fixture sets and retain the existing per-length parallelism."""
    data = tomllib.loads((root / "pyproject.toml").read_text())
    profile = data["tool"]["consumer-mypy"]
    directory = root / profile["files"].format(impl=impl, suite=suite, length=length)
    files = sorted(directory.glob("*.py"))
    if not files:
        raise ValueError(f"No type assertion files found in {directory}")
    if length == 1:
        files.extend(root / name for name in profile.get("boundary_files", []))
    workers = profile["workers"][str(length)]
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = pool.map(
            lambda path: check_file(path, profile["settings"], run), files
        )
        failed = False
        for status, output in results:
            print(output, end="", flush=True)
            failed = failed or status != 0
    return int(failed)


def main():
    """Select only the fixture identity; keep type checker settings in TOML."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--impl", choices=("abi", "codec"), required=True)
    parser.add_argument("--suite", choices=("fixed", "variable"), required=True)
    parser.add_argument("--length", choices=range(1, 5), type=int, required=True)
    args = parser.parse_args()
    try:
        return run_checks(Path.cwd(), args.impl, args.suite, args.length)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
