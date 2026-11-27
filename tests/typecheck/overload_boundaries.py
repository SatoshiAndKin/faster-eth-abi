"""Check the positional overload boundary against the installed public API."""

from typing import (
    Any,
    Tuple,
    Union,
)

from typing_extensions import (
    assert_type,
)

from faster_eth_abi import (
    abi,
)
from faster_eth_abi.codec import (
    ABIDecoder,
)
from faster_eth_abi.registry import (
    ABIRegistry,
)


def check_overload_boundaries() -> None:
    data = b""
    decoder = ABIDecoder(ABIRegistry())
    assert_type(
        abi.decode(("uint256", "bytes", "string"), data), Tuple[int, bytes, str]
    )
    assert_type(
        decoder.decode(("uint256", "bytes", "string"), data), Tuple[int, bytes, str]
    )
    assert_type(
        abi.decode(("uint256", "uint256", "uint256", "uint256"), data), Tuple[int, ...]
    )
    assert_type(
        decoder.decode(("uint256", "uint256", "uint256", "uint256"), data),
        Tuple[int, ...],
    )
    assert_type(
        abi.decode(("uint256", "bytes", "uint256", "bytes"), data),
        Tuple[Union[int, bytes], ...],
    )
    assert_type(
        decoder.decode(("uint256", "bytes", "uint256", "bytes"), data),
        Tuple[Union[int, bytes], ...],
    )
    assert_type(abi.decode(("?", "uint256", "bytes", "string"), data), Tuple[Any, ...])
    assert_type(
        decoder.decode(("?", "uint256", "bytes", "string"), data), Tuple[Any, ...]
    )
