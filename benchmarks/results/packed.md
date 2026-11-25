#### [faster_eth_abi.packed](https://github.com/SatoshiAndKin/faster-eth-abi/blob/master/faster_eth_abi/packed.py) - [view benchmarks](https://github.com/SatoshiAndKin/faster-eth-abi/blob/master/benchmarks/test_packed_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `encode_packed[address]` | 0.0009031427524432848 | 0.00019184281449278502 | 78.76% | 370.77% | 4.71x | ✅ |
| `encode_packed[bool]` | 0.0004994405055913536 | 6.609617288474788e-05 | 86.77% | 655.63% | 7.56x | ✅ |
| `encode_packed[bytes]` | 0.00047826642384099375 | 5.867925985659609e-05 | 87.73% | 715.05% | 8.15x | ✅ |
| `encode_packed[string]` | 0.0005123649374300825 | 6.0574858938472966e-05 | 88.18% | 745.84% | 8.46x | ✅ |
| `encode_packed[tuple]` | 0.0012552888505436251 | 0.00020137139237720583 | 83.96% | 523.37% | 6.23x | ✅ |
| `encode_packed[uint256]` | 0.0006420021051420036 | 9.464279662282114e-05 | 85.26% | 578.34% | 6.78x | ✅ |
| `is_encodable_packed[address]` | 4.470916191680667e-05 | 2.6468588347704175e-05 | 40.80% | 68.91% | 1.69x | ✅ |
| `is_encodable_packed[bool]` | 2.861024509145595e-05 | 2.2421112358974864e-05 | 21.63% | 27.60% | 1.28x | ✅ |
| `is_encodable_packed[bytes]` | 2.891377217540757e-05 | 2.5318861309221137e-05 | 12.43% | 14.20% | 1.14x | ✅ |
| `is_encodable_packed[string]` | 2.988636756150434e-05 | 2.2521177237320374e-05 | 24.64% | 32.70% | 1.33x | ✅ |
| `is_encodable_packed[tuple]` | 0.0001972370172566976 | 5.250124899110413e-05 | 73.38% | 275.68% | 3.76x | ✅ |
| `is_encodable_packed[uint256]` | 7.95607375029869e-05 | 3.3219195761620376e-05 | 58.25% | 139.50% | 2.40x | ✅ |
