# Canonical CPU campaign: configured and observed native pools

This is the completed corrective campaign, measured on 2026-10-19 from 18:32:11 to 18:50:08 UTC. Its report SHA-256 is `4ccf17702fa03d5abaacaa454a929ce49d71a88a84ca30bca3b20def364bc7cd`. All 14 cases and 70 independent measured processes passed numerical admission. The strict validator checked 84 verified worker-runtime native-pool observations and all 800 post-call control flags: 700 full engine/component samples plus 100 separately labeled Limen core samples. See [validation.json](validation.json) and [integrity.json](integrity.json).

The campaign was preregistered after correcting the separate Polars thread-pool control. Nine environment variables are fixed before worker startup, including `POLARS_MAX_THREADS=1`. Loaded BLAS and Polars pools are observed and gated before execution and after each full/core call, outside the timed interval. Missing observation capability or an observed non-one pool rejects admission. These are configured/observed native-pool controls, not a claim about total operating-system thread count or physical CPU isolation. The original campaign is retained separately as [superseded-control exploratory evidence](../2026-10-19-common-zero-original/); none of its samples are pooled here.

## Contract and repetitions

Seven adapters execute the same recorded year, two precomputed target paths, zero fees/slippage, a one-bar signal delay, and a common cash-affordable long/flat contract. There are 8,784 real source bars, 8,783 evaluated closes, penultimate-close liquidation, and a final actual settlement bar. The source-file SHA-256 is `a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72`. Prices are not fabricated. The separately acquired data manifest and source-byte hash establish the declared input; the hash alone does not establish venue provenance.

Each of the 14 cases has its own untimed fresh full-data preflight. Each case then runs in five independent measured processes, with one first and nine warm calls per process. Engine order rotates and is mirrored between strategies. The primary statistic is the median of the five within-process warm medians. Every first and warm value and every outlier is retained. Process-median min/max ranges are descriptive, not confidence intervals.

The native engine interval and the common-output materialization interval are recorded separately and add exactly within each sample. Independently aggregated component medians need not add to the full-common median. Preparation, imports, source verification, target computation, the independent oracle, explicit pre-call garbage collection, thread observations, and parity checks are outside the full-common interval. Startup observations retain launch-to-ready and launch-to-first-valid separately. Process lifetime peak RSS includes imports and validation and is not incremental engine memory.

## Interpretation

Limen, Backtrader, vectorbt, backtesting.py, and bt are the five admitted full-engine routes for this contract. QSTrader and Qlib are native-component routes with benchmark-owned replay drivers and have no full-engine ratio. Limen's internal kernel diagnostic occurs after all full calls in each process; its first phase is not process-cold. Native extras and optional ledger observations differ by adapter. Limen has native return/held arrays but no independent cash/units/quantity/fee ledger; its fills are inferred from held-segment boundaries.

The detailed [performance analysis](../../../reports/performance-analysis.md) explains why bt's native transaction materialization and vectorbt's lazy account outputs must remain visible beside their execution intervals. It includes the measured tables, native-field scope, cache/startup interpretation, and the original control diagnosis. The [repository overview](../../../README.md) links the generated views, whose headline tables are bound to this report's hash.

## Retained evidence

- `report.json`, per-worker/process JSON, `console.log`, and each `stdout.log` are copied unchanged from the completed run.
- `preregistration.json`, `timing-clear.json`, `benchmark-code.json`, and `benchmark-source/` establish the frozen runner and timing plan. The original raw installation/manifests and hash locks live in the repository's setup evidence and lock directories.
- `derived-raw-samples.csv` contains all 800 full/component/core observations, including native/extraction durations and post-call control flags.
- `derived-process-medians.csv` contains 80 process/layer rows: 70 full/component rows and 10 separate Limen core rows. It also retains raw startup/RSS observations.
- `derived-observation-scopes.csv` identifies the compared native fields and the adapter's exact declared scope/settings.
- `derived-core-diagnostics.json` separates kernel execution and kernel-plus-common output quantities. The latter is not a pure kernel duration.
- `derived-reproducibility.json` shows one checked result-array fingerprint and one installed candidate-code fingerprint per case across the preflight and repetitions. This is observed repeatability for these outputs, not a proof of all-workload or cross-host determinism.
- `omitted-runtime-artifacts.json` inventories every locally retained market/result array and compiled cache omitted from this public directory, with size and SHA-256. No dataset or JIT-cache copy is bundled.

Historical absolute paths in original logs and reports describe this run's workspace. Use the current repository bootstrap and benchmark commands to create a new run in a fresh output directory. The report validator checks admission metadata, code/source references, completeness, aggregate arithmetic, and recorded control fields; it does not rerun the numerical arrays or verify physical isolation.
