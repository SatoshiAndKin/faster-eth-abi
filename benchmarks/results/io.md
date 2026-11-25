#### [faster_eth_abi.io](https://github.com/SatoshiAndKin/faster-eth-abi/blob/master/faster_eth_abi/io.py) - [view benchmarks](https://github.com/SatoshiAndKin/faster-eth-abi/blob/master/benchmarks/test_io_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `contextframesbytesio_init[0]` | 0.0005728676540921655 | 0.00023158883542378407 | 59.57% | 147.36% | 2.47x | ✅ |
| `contextframesbytesio_init[1024]` | 0.0005738877470025782 | 0.00023191899594987193 | 59.59% | 147.45% | 2.47x | ✅ |
| `contextframesbytesio_init[32]` | 0.0005736646572580888 | 0.0002320208150636927 | 59.55% | 147.25% | 2.47x | ✅ |
| `contextframesbytesio_init[4096]` | 0.0005747576931749718 | 0.00023263163799955986 | 59.53% | 147.07% | 2.47x | ✅ |
| `contextframesbytesio_init[65536]` | 0.0005804648667444249 | 0.00023235557788630959 | 59.97% | 149.82% | 2.50x | ✅ |
| `contextframesbytesio_push_pop[10]` | 0.0006728565484562162 | 0.00028197231179414526 | 58.09% | 138.63% | 2.39x | ✅ |
| `contextframesbytesio_push_pop[1]` | 8.573684682315741e-05 | 3.891353008245994e-05 | 54.61% | 120.33% | 2.20x | ✅ |
| `contextframesbytesio_push_pop[50]` | 0.0034988076173291965 | 0.0014965521274657048 | 57.23% | 133.79% | 2.34x | ✅ |
| `contextframesbytesio_push_pop[5]` | 0.00033365360684107977 | 0.00013947063205445412 | 58.20% | 139.23% | 2.39x | ✅ |
| `contextframesbytesio_seek_in_frame[10]` | 0.00030133383729370115 | 0.00022681938734381301 | 24.73% | 32.85% | 1.33x | ✅ |
| `contextframesbytesio_seek_in_frame[1]` | 3.82185987406187e-05 | 3.218395791523446e-05 | 15.79% | 18.75% | 1.19x | ✅ |
| `contextframesbytesio_seek_in_frame[50]` | 0.0014530729999991177 | 0.0011258750818779624 | 22.52% | 29.06% | 1.29x | ✅ |
| `contextframesbytesio_seek_in_frame[5]` | 0.00014008905830333122 | 0.0001063243428319067 | 24.10% | 31.76% | 1.32x | ✅ |
