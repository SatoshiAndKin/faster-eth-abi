"""
parse_benchmark_output.py

Extracts per-function benchmark timings from pytest-benchmark's benchmark.json output.
Write test timings as JSON grouped by Python submodule and function.

Usage:
    python parse_benchmark_output.py <benchmark.json> [output.json]
        [--additional <part.json> ...]
"""

import argparse
import json
from pathlib import (
    Path,
)
import re
from typing import (
    Any,
)


def get_submodule(bench: dict[str, Any]) -> str:
    # Extract the submodule from the test file in the full pytest node ID.
    fullname = bench.get("fullname", "")
    m = re.search(r"benchmarks/test_([a-zA-Z0-9_]+)_benchmarks\.py", fullname)
    if m:
        return f"faster_eth_abi.{m.group(1)}"
    return "unknown"


def get_group_name(test_name: str) -> str:
    # Extract group from test name, e.g., test_foo, test_faster_foo -> group: foo
    m = re.match(r"test_faster_(.+)", test_name)
    if m:
        return m.group(1)
    m = re.match(r"test_(.+)", test_name)
    if m:
        return m.group(1)
    return test_name


def parse_pytest_benchmark_json(
    data: dict[str, Any],
) -> dict[str, dict[str, dict[str, Any]]]:
    """
    Parses pytest-benchmark's benchmark.json and extracts per-function timings,
    grouped by submodule and group name.
    Returns a dict: {submodule: {group: {function_name: {...}}}}
    """
    results: dict[str, dict[str, dict[str, Any]]] = {}
    for bench in data.get("benchmarks", []):
        name = bench["name"]
        submodule = get_submodule(bench)
        group = get_group_name(name)
        stats = bench["stats"]
        submodule_results = results.setdefault(submodule, {})
        group_results = submodule_results.setdefault(group, {})
        group_results[name] = {
            "mean": stats.get("mean"),
            "stddev": stats.get("stddev", None),
            "iqr": stats.get("iqr", None),
            "min": stats.get("min", None),
            "max": stats.get("max", None),
            "rounds": stats.get("rounds", None),
        }
    return results


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract and combine pytest benchmark results"
    )
    parser.add_argument("benchmark", type=Path)
    parser.add_argument(
        "output", type=Path, nargs="?", default=Path("benchmark_results.json")
    )
    parser.add_argument("--additional", type=Path, nargs="+", default=[])
    args = parser.parse_args()

    results: dict[str, dict[str, dict[str, Any]]] = {}
    for infile in [args.benchmark, *args.additional]:
        with infile.open() as f:
            partition = parse_pytest_benchmark_json(json.load(f))
        for submodule, groups in partition.items():
            merged_groups = results.setdefault(submodule, {})
            overlap = merged_groups.keys() & groups.keys()
            if overlap:
                raise ValueError(
                    f"Benchmark groups occur in multiple partitions: "
                    f"{submodule}: {sorted(overlap)}"
                )
            merged_groups.update(groups)

    with args.output.open("w") as f:
        json.dump(results, f, indent=2)
    print(f"Parsed results written to {args.output}")


if __name__ == "__main__":
    main()
