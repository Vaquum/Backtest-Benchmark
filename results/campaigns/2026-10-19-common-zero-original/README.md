# Original campaign: superseded thread control

This is the unchanged first comparative campaign. Its numeric admission completed successfully: 14 cases, 70 independent timed processes, 700 full engine/component calls, and 100 separate Limen core diagnostic calls. Every required equity, held-state, timestamp, and fill sample passed the common contract; available optional account fields were checked. The original report, worker records, logs, every timing sample and outlier, and a byte-identical benchmark source snapshot are retained.

**This campaign is exploratory and superseded for controlled rankings.** Its protocol declared one native thread but omitted Polars' separate `POLARS_MAX_THREADS` control and did not observe that pool. A fresh post-campaign process using the same eight declared controls in the same installed Limen environment reported nine Polars threads. That diagnosis establishes a control gap; the original processes did not record their actual Polars pool sizes. The corrective campaign uses explicit Polars control and a gate before and after every call. Read `disposition.json` and `diagnostics/native-thread-pool-check.json` before using this original report. Ratios inside its unmodified records remain historical arithmetic, not the canonical corrected ranking.

## Scope and timing boundaries

The recorded fixture has 8,784 actual source bars, with 8,783 close observations evaluated and the final actual bar used for settlement. Its SHA-256 is `a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72`. Buy-and-hold and 50/200 SMA target arrays are prepared once outside timed adapter calls. Each native engine executes the same delayed long/flat targets with continuous affordable units, zero fees/slippage, and penultimate-close liquidation. This measures execution and accounting of precomputed targets. It does not measure native indicator generation or a full research pipeline.

Each case has five independent measured processes, each with one first and nine warm calls. The primary statistic is the median of five within-process warm medians. Min/max ranges are descriptive, not confidence intervals. Engine order rotates and is mirrored between the two strategies; no raw observation is removed.

`engine_ms` is native engine construction/run for the declared adapter. `extraction_common_ms` includes materializing its required output arrays and common summary. Their sum is `full_common_ms`. Preparation, imports, source verification, the independent oracle, explicit pre-call garbage collection, and numerical admission are outside that interval. Launch-to-first-valid includes these startup tasks and the first admitted call. Fresh process and fresh Numba cache directories do not imply a cold operating-system file cache.

Native extras differ: bt and backtesting.py compute native performance statistics; Backtrader standard chart observers are disabled; vectorbt account arrays are materialized lazily during extraction. A single post-campaign profile attributes bt extraction primarily to two Pandas `unstack()` calls inside native `get_transactions()`. The adapter calls that native helper once; no redundant second adapter call was found. Its roughly 97 ms native simulation and multi-second common extraction must be read separately. Profiler durations in `diagnostics/bt-extraction/` include instrumentation overhead and are excluded from campaign samples.

QSTrader and Qlib use native components with benchmark-owned replay drivers; they receive no full-engine ratio. Limen's direct kernel calls run after all full calls in the same process. A core phase named `first` is the first direct invocation, not a process-cold kernel result.

## Observability and environment

Limen provides native returns and held segments; fills are inferred from their boundaries. Its adapter has no independent native cash, units, fill quantity, or fee ledger. Backtrader observes fill quantities and fees but does not separately emit cash/units here. Backtesting.py observes native trade quantities but not separate cash/units/fees. Vectorbt, bt, QSTrader, and Qlib emit all four optional fields in this route. `derived-observation-scopes.csv` retains the exact scopes, and original parity objects identify checked and unobserved fields.

Workers used built catalog-pinned sources, isolated Python 3.12.14 virtual environments, hash-locked dependencies, installed-code fingerprints, and actual import-location checks. Each engine has its own recorded dependency set; vectorbt's frozen source requires different NumPy/Pandas versions from the other core engines. Linux reports nine visible logical CPUs and affinity entries, but the CPU model and container quota fields were unavailable in the recorded environment. Peak RSS is a process lifetime high-water observation, including imports and validation, not incremental memory attributable solely to the engine.

## Files

- `report.json`, worker/process JSON, `console.log`, and per-worker `stdout.log` are original observed records copied unchanged.
- `benchmark-source/` contains the original benchmark Python files matching `benchmark-code.json` and the preregistration hashes. It exists to preserve the superseded implementation; the repository's current `bench/` is the corrected runner.
- `derived-raw-samples.csv` contains every full/component/core sample. `derived-process-medians.csv`, `derived-observation-scopes.csv`, and `derived-core-diagnostics.json` are derived views of the original report.
- `validation.json` records the independent schema, source-reference, admission-metadata, completeness, and aggregate-arithmetic checks. It does not replay market arrays or retroactively validate the missing original Polars control.
- `omitted-runtime-artifacts.json` records every omitted market/result array and compiled cache with its byte size and hash. These artifacts remain in local evidence and can be regenerated from the separately acquired hash-pinned recorded fixture. No market prices are fabricated or bundled here.

Absolute paths inside historical raw records describe the observed workspace. They are not portable setup commands. Use the repository's current reproduction instructions and write new evidence to a fresh output directory.
