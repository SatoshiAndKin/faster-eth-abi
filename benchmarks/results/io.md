#### [faster_eth_abi.io](https://github.com/SatoshiAndKin/faster-eth-abi/blob/master/faster_eth_abi/io.py) - [view benchmarks](https://github.com/SatoshiAndKin/faster-eth-abi/blob/master/benchmarks/test_io_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `contextframesbytesio_init[0]` | 0.00034561415762577084 | 0.00015453719883175017 | 55.29% | 123.64% | 2.24x | ✅ |
| `contextframesbytesio_init[1024]` | 0.0003445965268226389 | 0.0001541976201940553 | 55.25% | 123.48% | 2.23x | ✅ |
| `contextframesbytesio_init[32]` | 0.0003439972540667097 | 0.0001542136369132168 | 55.17% | 123.07% | 2.23x | ✅ |
| `contextframesbytesio_init[4096]` | 0.0003422734347374226 | 0.00015533096286262388 | 54.62% | 120.35% | 2.20x | ✅ |
| `contextframesbytesio_init[65536]` | 0.00034250325838143693 | 0.0001553552487204447 | 54.64% | 120.46% | 2.20x | ✅ |
| `contextframesbytesio_push_pop[10]` | 0.000462846368572986 | 0.0002273765383528759 | 50.87% | 103.56% | 2.04x | ✅ |
| `contextframesbytesio_push_pop[1]` | 6.058368781453431e-05 | 2.7664883245203523e-05 | 54.34% | 118.99% | 2.19x | ✅ |
| `contextframesbytesio_push_pop[50]` | 0.0023708060849063294 | 0.000976884827209875 | 58.80% | 142.69% | 2.43x | ✅ |
| `contextframesbytesio_push_pop[5]` | 0.0002365585156252501 | 9.982019972552562e-05 | 57.80% | 136.98% | 2.37x | ✅ |
| `contextframesbytesio_seek_in_frame[10]` | 0.0002062119073149596 | 0.00014654661852636324 | 28.93% | 40.71% | 1.41x | ✅ |
| `contextframesbytesio_seek_in_frame[1]` | 2.6593666816776818e-05 | 2.297490256977831e-05 | 13.61% | 15.75% | 1.16x | ✅ |
| `contextframesbytesio_seek_in_frame[50]` | 0.0009854329539083955 | 0.0006853652520324811 | 30.45% | 43.78% | 1.44x | ✅ |
| `contextframesbytesio_seek_in_frame[5]` | 9.77600294935368e-05 | 7.174507600874692e-05 | 26.61% | 36.26% | 1.36x | ✅ |
