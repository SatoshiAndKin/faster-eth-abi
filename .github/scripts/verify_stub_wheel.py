"""Validate the identity and typed subpackages of the shipped stub wheel."""

from email.parser import (
    Parser,
)
from pathlib import (
    Path,
)
import zipfile


def verify(path):
    """Reject another project's identity, missing stubs, and runtime sources."""
    with zipfile.ZipFile(path) as wheel:
        names = set(wheel.namelist())
        metadata = [name for name in names if name.endswith(".dist-info/METADATA")]
        if len(metadata) != 1:
            raise ValueError("Expected exactly one wheel metadata file")
        info = Parser().parsestr(wheel.read(metadata[0]).decode())
        if info["Name"] != "eth-abi-stubs":
            raise ValueError("Wheel identity must be eth-abi-stubs")
        for package in ("eth_abi", "faster_eth_abi"):
            for file in (
                "__init__.pyi",
                "abi.pyi",
                "codec.pyi",
                "utils/numeric.pyi",
                "tools/_strategies.pyi",
            ):
                if f"{package}/{file}" not in names:
                    raise ValueError(f"Missing typed module: {package}/{file}")
        if any(name.endswith((".py", ".so", ".pyd")) for name in names):
            raise ValueError("A stub-only wheel must not contain runtime modules")
    print(f"Validated {path.name}: eth-abi-stubs and both typed package trees")


if __name__ == "__main__":
    wheels = list(Path("dist-stubs").glob("*.whl"))
    if len(wheels) != 1:
        raise ValueError("Expected exactly one generated stub wheel")
    verify(wheels[0])
