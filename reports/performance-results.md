# Recorded execution performance

Values describe the frozen source builds, exact real input and declared public API/component workload. They are not universal engine speed, native indicator throughput, a trained research campaign, or live-trading capacity.

Warm latency is the median of the within-process medians; process and repetition counts belong to each campaign's raw report. First full-API calls use fresh processes/JIT caches. Full-common latency includes common-output extraction; native extra work differs. The process-median range is descriptive, not a confidence interval. Separate campaigns must not be pooled or compared without reconciling source, data, contract, machine and timing scope. See the [full protocol](../protocol/README.md).

## Campaign 2026-10-19-common-zero-single-thread

[Raw report](../results/campaigns/2026-10-19-common-zero-single-thread/report.json) · SHA-256 `4ccf17702fa03d5abaacaa454a929ce49d71a88a84ca30bca3b20def364bc7cd`

Input SHA-256 `a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72`. Started 2026-10-19T18:32:11.683574+00:00; finished 2026-10-19T18:50:08.087747+00:00.

### Full native public API results

| Engine | Strategy | Status / processes | Warm full-common ms | Process-median range ms | First full-common ms | Candidate/Limen duration | Peak process RSS MiB |
|---|---|---|---:|---:|---:|---:|---:|
| [limen](candidates/limen.md#p07) | buy_and_hold | verified / 5 | 2.589 | 2.280–2.759 | 2.781 | 1.00× | 125.3 |
| [backtrader](candidates/backtrader.md#p07) | buy_and_hold | verified / 5 | 690.586 | 656.078–789.386 | 740.090 | 266.76× | 125.9 |
| [vectorbt](candidates/vectorbt.md#p07) | buy_and_hold | verified / 5 | 61.284 | 49.776–77.908 | 17,313.421 | 23.67× | 498.2 |
| [backtesting_py](candidates/backtesting_py.md#p07) | buy_and_hold | verified / 5 | 43.401 | 40.662–45.325 | 51.170 | 16.76× | 130.6 |
| [bt](candidates/bt.md#p07) | buy_and_hold | verified / 5 | 5,308.303 | 4,866.027–5,571.319 | 5,082.935 | 2,050.48× | 240.7 |
| [limen](candidates/limen.md#p07) | sma_cross | verified / 5 | 2.008 | 1.774–2.123 | 2.529 | 1.00× | 126.4 |
| [backtrader](candidates/backtrader.md#p07) | sma_cross | verified / 5 | 661.027 | 646.042–683.217 | 692.080 | 329.20× | 125.9 |
| [vectorbt](candidates/vectorbt.md#p07) | sma_cross | verified / 5 | 58.795 | 53.622–63.699 | 18,181.647 | 29.28× | 498.1 |
| [backtesting_py](candidates/backtesting_py.md#p07) | sma_cross | verified / 5 | 40.926 | 39.523–56.856 | 44.241 | 20.38× | 130.5 |
| [bt](candidates/bt.md#p07) | sma_cross | verified / 5 | 5,088.201 | 4,517.369–5,375.005 | 4,978.946 | 2,533.98× | 240.8 |

### Native components — no full-engine ratios

| Engine | Strategy | Status / processes | Warm full-common ms | Process-median range ms | First full-common ms | Candidate/Limen duration | Peak process RSS MiB |
|---|---|---|---:|---:|---:|---:|---:|
| [qstrader](candidates/qstrader.md#p07) | buy_and_hold | verified / 5 | 54.672 | 50.807–64.128 | 52.038 | Not eligible | 125.0 |
| [qlib](candidates/qlib.md#p07) | buy_and_hold | verified / 5 | 60.783 | 56.490–75.141 | 61.753 | Not eligible | 219.4 |
| [qstrader](candidates/qstrader.md#p07) | sma_cross | verified / 5 | 52.235 | 50.480–61.036 | 54.850 | Not eligible | 127.0 |
| [qlib](candidates/qlib.md#p07) | sma_cross | verified / 5 | 61.009 | 57.515–66.580 | 61.872 | Not eligible | 203.7 |

### Cold process and timing decomposition

Launch-to-first-valid includes source verification, imports, input loading, oracle and successful parity. It is a reproducible harness journey, not pure native startup. RSS is a process high-water mark, not incremental engine allocation.

| Engine | Strategy | Native warm ms | Extraction warm ms | Warm CPU ms | Launch to first valid ms | Evaluated bars/s |
|---|---|---:|---:|---:|---:|---:|
| limen | buy_and_hold | 2.243 | 0.306 | 2.594 | 474.254 | 3,392,672 |
| backtrader | buy_and_hold | 688.656 | 0.722 | 690.536 | 2,453.576 | 12,718 |
| vectorbt | buy_and_hold | 9.865 | 50.017 | 61.289 | 23,180.636 | 143,317 |
| backtesting_py | buy_and_hold | 42.566 | 0.770 | 43.402 | 897.882 | 202,370 |
| bt | buy_and_hold | 95.619 | 5,221.771 | 5,307.880 | 6,710.300 | 1,655 |
| qstrader | buy_and_hold | 54.466 | 0.216 | 54.673 | 1,333.364 | 160,650 |
| qlib | buy_and_hold | 60.608 | 0.187 | 60.786 | 1,413.847 | 144,497 |
| limen | sma_cross | 1.702 | 0.240 | 2.012 | 411.347 | 4,374,026 |
| backtrader | sma_cross | 660.305 | 0.785 | 661.003 | 2,230.691 | 13,287 |
| vectorbt | sma_cross | 9.498 | 49.723 | 58.801 | 23,914.300 | 149,384 |
| backtesting_py | sma_cross | 39.990 | 0.950 | 40.929 | 876.757 | 214,609 |
| bt | sma_cross | 87.143 | 5,005.687 | 5,087.735 | 6,409.785 | 1,726 |
| qstrader | sma_cross | 52.008 | 0.227 | 52.238 | 1,309.992 | 168,143 |
| qlib | sma_cross | 60.833 | 0.184 | 61.011 | 1,520.438 | 143,963 |

## Interpretation and retained attempts

Machine-level raw results include scope/settings, native output observability, every timing call, process medians, source/build identity, code hashes, parity checks and process logs. Prepared market arrays and compiler caches are omitted from published evidence with digests; rerunning from the hashed source fixture regenerates them.

The separately retained [original campaign](../results/campaigns/2026-10-19-common-zero-original/) did not limit Polars' separate pool and is excluded from these registered headline tables. The corrective campaign adds explicit Polars limits and observed loaded-pool admission. See [performance interpretation](performance-analysis.md) for native execution versus lazy output materialization, the original control deviation and the separately labelled Limen internal-core diagnostics. A core diagnostic's phase named first runs after the full snapshot calls and is not process-cold.

## Unmeasured comparison scopes

LEAN, Zipline-reloaded, Freqtrade and Jesse are fully included in the code grid but lack an admitted matched replay adapter in this campaign. Nautilus's native source test compilation hit two explicit time limits; no execution or test-success result is inferred. hftbacktest is a recorded-depth specialist; its 22 passing native library tests are not an OHLC performance measurement. Full QSTrader/Qlib workflows, parameter/search scaling, native indicator kernels, parallel/GPU throughput, market-impact fidelity and restart costs remain unmeasured.

Only vectorbt and Qlib passed the separate 5-bps fee plus 5-bps slippage component/public-API preflight; it is not a comparative costed-speed campaign. Limen's common snapshot adapter rejects that accounting convention, so a costed Limen ratio is absent by design.

