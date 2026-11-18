#### [faster_eth_abi.packed](https://github.com/SatoshiAndKin/faster-eth-abi/blob/master/faster_eth_abi/packed.py) - [view benchmarks](https://github.com/SatoshiAndKin/faster-eth-abi/blob/master/benchmarks/test_packed_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `encode_packed[address]` | 0.0006184553211589279 | 0.00014010080531923623 | 77.35% | 341.44% | 4.41x | ✅ |
| `encode_packed[bool]` | 0.0003414270970902706 | 4.6132269153251415e-05 | 86.49% | 640.10% | 7.40x | ✅ |
| `encode_packed[bytes]` | 0.00032298668340561426 | 3.84361817605176e-05 | 88.10% | 740.32% | 8.40x | ✅ |
| `encode_packed[string]` | 0.0003448945582802503 | 3.9982429115483935e-05 | 88.41% | 762.62% | 8.63x | ✅ |
| `encode_packed[tuple]` | 0.0008212154034755056 | 0.00014735036187560048 | 82.06% | 457.32% | 5.57x | ✅ |
| `encode_packed[uint256]` | 0.00043272129732541386 | 6.489603335708845e-05 | 85.00% | 566.79% | 6.67x | ✅ |
| `is_encodable_packed[address]` | 2.9541500761791456e-05 | 1.7355598827264287e-05 | 41.25% | 70.21% | 1.70x | ✅ |
| `is_encodable_packed[bool]` | 1.8801780713464456e-05 | 1.4315219753247303e-05 | 23.86% | 31.34% | 1.31x | ✅ |
| `is_encodable_packed[bytes]` | 1.8892265181115942e-05 | 1.6311139103633028e-05 | 13.66% | 15.82% | 1.16x | ✅ |
| `is_encodable_packed[string]` | 1.9072428681927354e-05 | 1.4382143427020945e-05 | 24.59% | 32.61% | 1.33x | ✅ |
| `is_encodable_packed[tuple]` | 0.00013181106258191254 | 3.496949566279503e-05 | 73.47% | 276.93% | 3.77x | ✅ |
| `is_encodable_packed[uint256]` | 5.556936862207173e-05 | 2.292298631452082e-05 | 58.75% | 142.42% | 2.42x | ✅ |
