"""Protect the shipped stub package identity and complete module set."""

from pathlib import (
    Path,
)
import tempfile
import unittest
import zipfile

from verify_stub_wheel import (
    verify,
)


class StubWheelTests(unittest.TestCase):
    def wheel(self, directory, name="eth-abi-stubs", omit="", runtime=False):
        path = Path(directory) / "stubs.whl"
        with zipfile.ZipFile(path, "w") as wheel:
            wheel.writestr("stubs.dist-info/METADATA", f"Name: {name}\nVersion: 1\n")
            for package in ("eth_abi", "faster_eth_abi"):
                for module in (
                    "__init__",
                    "abi",
                    "codec",
                    "utils/numeric",
                    "tools/_strategies",
                ):
                    member = f"{package}/{module}.pyi"
                    if member != omit:
                        wheel.writestr(member, "")
            if runtime:
                wheel.writestr("eth_abi/abi.py", "")
        return path

    def test_complete_stub_distribution(self):
        with tempfile.TemporaryDirectory() as directory:
            verify(self.wheel(directory))

    def test_rejects_wrong_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "identity"):
                verify(self.wheel(directory, name="types-eth-utils"))

    def test_rejects_missing_nested_module(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "Missing typed module"):
                verify(self.wheel(directory, omit="eth_abi/utils/numeric.pyi"))

    def test_rejects_runtime_source(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "runtime modules"):
                verify(self.wheel(directory, runtime=True))


if __name__ == "__main__":
    unittest.main()
