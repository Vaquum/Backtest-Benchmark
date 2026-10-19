# Performance analysis and interpretation

## Canonical observed result

The corrected campaign completed on 2026-10-19 from 18:32:11 to 18:50:08 UTC. All 14 cases, 70 independent timed processes, 700 full engine/component samples, and 100 separate Limen core samples passed admission. The strict independent validator checked 84 worker-runtime native-pool observations and all 800 post-call thread-control flags. Each case produced one identical checked result-array fingerprint across its preflight and measured repetitions. The [canonical report](../results/campaigns/2026-10-19-common-zero-single-thread/report.json) has SHA-256 `4ccf17702fa03d5abaacaa454a929ce49d71a88a84ca30bca3b20def364bc7cd`; [integrity and validation records](../results/campaigns/2026-10-19-common-zero-single-thread/) accompany it.

Limen had the smallest full-common median among the five admitted full-engine routes for both target paths. That finding applies to this contract and these observations. The decomposition matters: vectorbt's native run is much shorter than its required output materialization, while bt's native run is dramatically shorter than its transaction-helper materialization. Optional native ledger coverage also differs, as shown below.

All numbers in the following table are milliseconds. Each point is the median of five process medians of nine warm calls; ranges are the minimum and maximum of those five process medians. Independently computed component medians need not sum to the full-common median.

| Full-engine route | Strategy | Native run | Extraction + common | Full-common | Process-median range |
|---|---|---:|---:|---:|---:|
| Limen | Buy-and-hold | 2.243 | 0.306 | 2.589 | 2.280–2.759 |
| Backtrader | Buy-and-hold | 688.656 | 0.722 | 690.586 | 656.078–789.386 |
| vectorbt | Buy-and-hold | 9.865 | 50.017 | 61.284 | 49.776–77.908 |
| backtesting.py | Buy-and-hold | 42.566 | 0.770 | 43.401 | 40.662–45.325 |
| bt | Buy-and-hold | 95.619 | 5,221.771 | 5,308.303 | 4,866.027–5,571.319 |
| Limen | SMA 50/200 | 1.702 | 0.240 | 2.008 | 1.774–2.123 |
| Backtrader | SMA 50/200 | 660.305 | 0.785 | 661.027 | 646.042–683.217 |
| vectorbt | SMA 50/200 | 9.498 | 49.723 | 58.795 | 53.622–63.699 |
| backtesting.py | SMA 50/200 | 39.990 | 0.950 | 40.926 | 39.523–56.856 |
| bt | SMA 50/200 | 87.143 | 5,005.687 | 5,088.201 | 4,517.369–5,375.005 |

QSTrader and Qlib remain component-only observations, with no ratio against full engines:

| Native-component route | Strategy | Native run | Extraction + common | Full-common | Process-median range |
|---|---|---:|---:|---:|---:|
| QSTrader components | Buy-and-hold | 54.466 | 0.216 | 54.672 | 50.807–64.128 |
| Qlib components | Buy-and-hold | 60.608 | 0.187 | 60.783 | 56.490–75.141 |
| QSTrader components | SMA 50/200 | 52.008 | 0.227 | 52.235 | 50.480–61.036 |
| Qlib components | SMA 50/200 | 60.833 | 0.184 | 61.009 | 57.515–66.580 |

Limen's separately reported kernel-plus-common diagnostic had warm process-median aggregates of 0.855801 ms for Buy-and-hold, 0.779626 ms for SMA 50/200. These calls occur after all full calls, so their first phase is not process-cold. The canonical evidence retains [all 800 raw samples](../results/campaigns/2026-10-19-common-zero-single-thread/derived-raw-samples.csv), [each process median and startup/RSS observation](../results/campaigns/2026-10-19-common-zero-single-thread/derived-process-medians.csv), [native observation scopes](../results/campaigns/2026-10-19-common-zero-single-thread/derived-observation-scopes.csv), and [kernel decomposition](../results/campaigns/2026-10-19-common-zero-single-thread/derived-core-diagnostics.json).

The median first full-common calls were 2.781/2.529 ms for Limen and 17,313/18,182 ms for vectorbt in buy-and-hold/SMA respectively. Vectorbt's corresponding launch-to-first-valid medians were about 23.18/23.91 seconds; they include startup and cold JIT work under the fresh-cache protocol. First-call and warm observations should be read separately. No original-campaign samples are pooled into these corrected values.

## What this comparison measures

The executable comparison measures a narrowly defined historical execution task: apply identical, precomputed long/flat targets to one recorded hourly price series, with a one-bar signal delay, continuous affordable units, and a common cash/quantity accounting contract. It separates native execution, the work needed to materialize comparable outputs, startup, and a Limen kernel diagnostic. It does not establish a universal speed ordering of the candidate products.

The source fixture contains 8,784 real bars. The benchmark evaluates 8,783 close observations and reserves the final real bar for settling engines whose close fills are reflected during the next event. Liquidation occurs at the penultimate source close. The original source bytes are identified by SHA-256 `a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72`. Source prices are unchanged in preparation. The native fractional-trading wrapper in backtesting.py transforms units internally, using a `1e-12` unit quantum in this adapter; its reported prices and quantities are converted back to the original economic units. Continuous units describe the common oracle contract, with the native approximation admitted under the recorded numerical tolerances. Data byte identity does not by itself prove exchange provenance or data completeness. See the executable [data admission](../bench/data.py), [contract/oracle](../bench/contract.py), and recorded data catalog.

Buy-and-hold and 50/200 SMA decisions are computed in common preparation, outside timed adapter calls. A decision available after close `t` may fill at close `t+1`. A transition into long buys the quantity affordable from current cash, then holds that quantity until a transition to flat sells it. Entry and exit fees, when a separate costed contract is admitted, are charged on actual fill notional; slippage changes the executed price. The canonical CPU campaign uses zero fees and zero slippage. It excludes partial fills, impact, borrowing, funding, corporate actions, exchange-calendar rules, and intrabar order sequencing. Those features require different contracts and evidence.

This task gives useful evidence about execution/accounting overhead on the recorded path. It does not time native SMA implementations, strategy discovery, a complete Limen search/selection workflow, portfolio construction across many assets, distributed execution, or a live trading system. The source audit covers those capabilities where there is evidence; the latency table does not stand in for that audit.

## Admission before speed

Each adapter is checked against an independent loop that updates cash and units explicitly. The oracle does not import candidate engines. It compares every evaluated equity value, timestamp, incoming held state, fill bar, fill side, and fill price. Native cash, units, fill quantities, and fees are compared additionally when the adapter observes them. Missing optional account fields are retained as missing; the oracle never supplies a candidate's absent ledger. See [the parity implementation](../bench/contract.py) and [worker admission](../bench/worker.py).

There is an important observation asymmetry:

| Adapter | Optional native observations checked in this route | What limits the claim |
|---|---|---|
| Limen | None of cash, units, fill quantities, or fill fees | Native returns and held segments produce the equity path; fill boundaries are inferred from those segments. This is weaker than agreement with an independent native order ledger. |
| Backtrader | Fill quantities and commissions | Equity is observed from the broker at strategy callbacks. Separate cash and units paths are not exported by this adapter. |
| backtesting.py | Trade quantities | Native equity and completed trades are observed, but separate cash, units, and fill-fee paths are not exported here. |
| vectorbt | Cash, units, quantities, fees | All four optional fields are checked through the native portfolio/order outputs. |
| bt | Cash, units, quantities, fees | Transactions come from its native helper, which itself derives transactions from recorded position differences and security prices. |
| QSTrader components | Cash, units, quantities, fees | Native broker/portfolio/transaction components run through a benchmark-owned hourly replay driver. |
| Qlib components | Cash, units, quantities, fees | Native Exchange/Position accounting runs through a benchmark-owned replay driver and recorded-quote extension. |

The adapters and their `output_observation` fields are the executable source for these distinctions: [Limen](../bench/adapters/limen.py), [Backtrader](../bench/adapters/backtrader.py), [backtesting.py](../bench/adapters/backtesting_py.py), [vectorbt](../bench/adapters/vectorbt.py), [bt](../bench/adapters/bt.py), [QSTrader](../bench/adapters/qstrader.py), and [Qlib](../bench/adapters/qlib.py). Numerical admission establishes agreement for the checked contract and fields; it does not make their internal models or available observations identical.

An untimed fresh full-data preflight precedes the measurement campaign. Every first and warm timed result is checked again outside the timed interval. A failed or missing requested measurement invalidates that entire case's aggregate and ratio; previously observed raw samples remain retained. Unsupported contracts have explicit dispositions. For example, the current Limen adapter does not map its native fee-return convention onto this cash-affordable fill-time fee contract. Backtrader and backtesting.py costed observation routes are not yet admitted. The 999-observation costed preflight admits vectorbt and Qlib at five basis points each of fee and slippage; it is a correctness observation, not a costed performance campaign. See the retained [preflight evidence](../results/evidence/core-harness/preflight/).

## Timing boundaries

The worker exposes three different timing quantities per full call:

| Quantity | Included work |
|---|---|
| `engine_ms` | Adapter-declared native construction and execution. The exact native extras vary by engine and are recorded with every case. |
| `extraction_common_ms` | Materializing the required native account/equity/fill outputs, normalizing them into common arrays, and calculating the small common result summary. |
| `full_common_ms` | The preceding two intervals together. Each individual sample equals their sum. |

Input loading, target generation, adapter preparation, imports, source verification, the independent oracle, explicit pre-call garbage collection, thread-pool observation, and numerical parity checks are outside the full-common interval. Allocations and any collections triggered within the timed call remain included. Separately reported launch-to-ready and launch-to-first-valid times show startup costs rather than folding them into warm native execution.

The displayed engine and extraction medians are calculated independently. They need not add to the displayed full-common median, although their durations add exactly within every raw call. This follows from taking medians of different distributions; the raw sample tables make the identity directly inspectable.

Five adapters qualify for this full-engine comparison: Limen, Backtrader, vectorbt, backtesting.py, and bt. Their public/native paths still perform different amounts of extra work. Limen computes its native snapshot metrics. Backtrader constructs its engine, ingests Pandas bars, and preloads them, with standard chart observers disabled. Backtesting.py and bt compute native performance statistics during their public run calls. Vectorbt's account outputs are materialized lazily. These are useful end-to-end routes to the required observations, but their durations are not measurements of a uniform internal kernel.

QSTrader and Qlib have separate native-component rows. Their benchmark-owned replay drivers do not execute the full higher-level products. The full QSTrader session selects a daily business-day event engine in [its pinned implementation](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L206-L215), which is a different workload from this recorded hourly contract. Neither component adapter receives a full-engine ratio.

Limen's direct return kernel is an internal diagnostic. It executes after all full-engine calls in each process. Its phase called `first` means the first direct invocation at that point; the process, imports, data, and preceding full snapshot path are already warm. It must not be described as a process-cold kernel measurement or ranked against complete engines.

## Why extraction matters: bt and vectorbt

The original campaign exposed an especially large separation in bt: native execution was about 97 ms in both strategies, while common extraction took several seconds. A separate post-campaign `cProfile` run attributed 13.375 of 13.391 profiled seconds to two Pandas `unstack()` calls; its [original profile text](../results/campaigns/2026-10-19-common-zero-original/diagnostics/bt-extraction/result/profile.txt) and [structured profile](../results/campaigns/2026-10-19-common-zero-original/diagnostics/bt-extraction/result/profile.json) are retained. Instrumentation changes absolute durations, so those profile values are attribution evidence only and are excluded from the comparative sample tables.

The adapter invokes native `get_transactions()` once. The pinned helper independently unstacks its security-price table and its nonzero position differences, then combines them into transactions: [bt core.py, lines 1209–1241](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L1209-L1241). In the installed Pandas 2.3.3 environment, the observed call chain enters `stack_v3` and makes many per-index selections. The profile's roughly 17,570 repeated index-selection calls support that attribution. It does not measure asymptotic scaling, and this campaign does not establish how the cost changes with data length or another dependency version. The native output route was preserved in the corrective campaign; neither candidate code nor observations were replaced to improve its number.

Vectorbt also requires care when reading the columns. Its measured `Portfolio.from_signals` call is separate from materializing assets, cash, account value, and order records in common extraction. The pinned implementation exposes cached account computations, including [assets](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L4332-L4347), [cash](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L4446-L4485), and [value](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L4546-L4580). The adapter explicitly selects its Numba route. The first call can compile both simulation and output-materialization functions; warm calls benefit from already compiled functions. Reporting only its simulation interval would leave required output work outside the comparison. Reporting only full-common would conceal where that work occurs. Both quantities are retained.

Fresh Numba cache directories are used for each independent worker. This makes first-process compilation costs visible; it is not the same deployment scenario as launching repeatedly against a persistent populated JIT cache. No Rust vectorbt backend or GPU path is measured here. The pinned vectorbt source carries the Commons Clause in addition to its Apache 2 terms, so it is cataloged as source available rather than assumed to have the same license terms as this benchmark repository.

## Replication, environment, and the thread-control correction

The preregistered design uses seven adapters, two strategies, five independent measured processes per case, and one first plus nine warm calls per process. It yields 70 measured processes and 700 full engine/component call observations. The Limen diagnostic adds 100 separately labeled calls. The summary uses the median of five within-process warm medians. It retains all five medians, their min/max, every first call, every warm call, and all outliers. Ranges describe the observed process variation; they are not confidence intervals. Five process blocks do not support a general claim about performance across hosts.

Engine order rotates by block and is mirrored across the two strategies. The strategy executed first alternates by block. Across the mirrored pair, each engine has the same mean execution position in every block; within one strategy, five blocks cover only five of the seven possible engine positions. The process is serial, and other known build/test workloads are paused. Ordinary operating-system or container scheduling noise remains possible.

The original completed campaign is retained under [common-zero-original](../results/campaigns/2026-10-19-common-zero-original/). Its numerical checks passed, but a subsequent control audit found that setting `RAYON_NUM_THREADS=1` did not limit Polars' separate pool. A fresh process with the same eight declared variables and the same installed Limen environment reported a nine-thread Polars pool with `POLARS_MAX_THREADS` unset. The original workers did not record this pool themselves. That is a control gap, and the original campaign is superseded for controlled rankings. Its raw records, timing values, original source snapshot, diagnosis, and corrections remain unchanged and inspectable.

The corrective protocol adds `POLARS_MAX_THREADS=1` to the fixed environment controls. It verifies the requested settings and observed BLAS/Polars pools before execution and after every full/core call, outside the timed interval. It records an explicit absent/loaded state for Polars and rejects a missing observer or an observed pool whose size differs from one. Admission is visible in each corrected timing sample. The independent validator has a `--require-native-thread-policy` option, so omitting the entire corrective policy cannot silently satisfy the canonical reporting gate. See [thread provenance and admission](../bench/provenance.py), [worker enforcement](../bench/worker.py), and [report validation](../scripts/validate_assessment.py).

The seven measured candidate runtimes use isolated Python 3.12.14 virtual environments, built frozen source revisions, hash-locked dependencies, recorded installed-code fingerprints, and checked actual import locations. These are source/build identity controls; they do not claim bit-identical builds on every compiler or platform. Each engine uses its own dependency lock. Vectorbt's frozen source requires different NumPy/Pandas versions from the other core candidates, so results include those dependency choices. Workers record visible CPU affinity and operating-system information, but the observed host did not expose a CPU model or container quota values. Peak RSS is a process lifetime high-water value that includes imports, oracle construction, validation, and repeated calls. It is not incremental engine memory or a measured memory-scaling curve.

## Reading and extending the grid

Use measured values only when the candidate implements the same contract, passes whole-path admission, exposes the same declared comparison layer, and completes every preregistered process. If one of those conditions is absent, record an explicit unmeasured, unsupported, or component-only disposition. A failed dependency build, unavailable adapter, or bounded native compilation attempt is not a backtest latency result.

The wider 42-criterion grid separates computational capabilities from their measured performance. Source-backed caching, factorized preparation, serial/parallel scheduling, allocation behavior, and resource bounds are relevant evidence, but they do not become quantitative speedups without a controlled experiment. This campaign does not measure input-size scaling, multi-asset scaling, parameter-search throughput, parallel efficiency, cache capacity, fault recovery, or GPU execution. A future comparison should add distinct preregistered scenarios for those questions rather than extrapolating from this single recorded year.

To add another engine, pin and inspect its executable implementation, build that exact source against a recorded dependency set, and implement the smallest adapter whose observed semantics match the common contract. Declare each native extra and any reconstructed or unavailable field. Run recorded-data buy-and-hold, crossover, flat, and relevant costed checks before timing. Preserve rejection histories and output hashes. Then reuse the same process-level design and loaded-pool gates, publishing a new campaign with its own code hashes and evidence. The report renderer keeps campaigns separate and verifies the registered report hash; it does not pool historical or corrective samples.
