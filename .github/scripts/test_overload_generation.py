"""Keep sampled CI assertions identical to their complete product intervals."""

from contextlib import (
    contextmanager,
)
import importlib.util
import itertools
import os
from pathlib import (
    Path,
)
import random
import tempfile
import unittest
from unittest.mock import (
    patch,
)

SPEC = importlib.util.spec_from_file_location(
    "generate_overload_tests",
    Path(__file__).parents[2] / "scripts/generate_overload_tests.py",
)
generator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generator)


@contextmanager
def workspace():
    before = Path.cwd()
    with tempfile.TemporaryDirectory() as directory:
        os.chdir(directory)
        try:
            yield Path(directory)
        finally:
            os.chdir(before)


class SampledAssertionsTests(unittest.TestCase):
    def setUp(self):
        self.patches = patch.multiple(
            generator, ALL_LITERALS=["?", "bytes", "int"], NUM_LITERALS=3, CHUNK_SIZE=5
        )
        self.patches.start()
        self.addCleanup(self.patches.stop)

    def test_each_chunk_matches_the_complete_product_including_partial_tail(self):
        for length in range(1, 5):
            complete = list(itertools.product(generator.ALL_LITERALS, repeat=length))
            chunks = []
            for index in range(1, generator.compute_total_chunks(length) + 1):
                chunk = list(generator.iter_case_chunk(length, index))
                self.assertEqual(chunk, complete[(index - 1) * 5 : index * 5])
                chunks.extend(chunk)
            self.assertEqual(chunks, complete)

    def test_sampled_files_equal_complete_files_with_original_seed_and_case_ids(self):
        for impl, mode in itertools.product(("abi", "codec"), ("fixed", "variable")):
            with self.subTest(impl=impl, mode=mode), workspace() as root:
                total = generator.stream_cases_and_write_files(
                    mode, impl, lengths=[1, 2, 3, 4]
                )
                complete = {
                    f.relative_to(root): f.read_bytes() for f in root.rglob("*.py")
                }
                for path in complete:
                    (root / path).unlink()
                sampled_total = generator.stream_cases_and_write_files(
                    mode, impl, sample_1_of_x=3, seed=42, lengths=[1, 2, 3, 4]
                )
                self.assertEqual(total, sampled_total)
                expected = set()
                for length in range(1, 5):
                    count = generator.compute_total_chunks(length)
                    selected = random.Random(42).sample(
                        range(1, count + 1), max(1, count // 3)
                    )
                    expected.update(
                        Path(
                            f"tests/typecheck/{impl}/decode/{mode}/len_{length}/"
                            f"overload_test_data_{index:05d}.py"
                        )
                        for index in selected
                    )
                actual = {
                    f.relative_to(root): f.read_bytes() for f in root.rglob("*.py")
                }
                self.assertEqual(set(actual), expected)
                for path, content in actual.items():
                    self.assertEqual(content, complete[path])


if __name__ == "__main__":
    unittest.main()
