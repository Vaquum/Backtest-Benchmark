# backtesting.py

**Frozen source:** [kernc/backtesting.py @ ca2e2611621e472542ba90f7243a1fa06a7d7108](https://github.com/kernc/backtesting.py/tree/ca2e2611621e472542ba90f7243a1fa06a7d7108)

**Observed license label:** AGPL-3.0  
**Layer:** Bar broker/strategy execution and parameter optimizer

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Full FractionalBacktest replay is admitted; mandatory native statistics and representation conversion remain in its timed work.

**Academic:** The core slices registered data/indicators; the percentage trailing helper changes all 153 mature stop distances under a real-prefix extension probe.

**Safety:** Native affordability/cost controls are present; optional helper chronology and trusted strategy execution remain separate boundaries.

## P01

### Parameter-space construction and retained memory

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native grid optimizer construction

The grid optimizer materializes a param_combos list after scanning the Cartesian product and applying constraints/random acceptance.

**Limit:** A small max_tries does not avoid scanning the product on this path. No measured construction-memory sweep.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtesting/backtesting.py:1505–1537](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1505-L1537)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Grid and SAMBO optimizer candidate paths

Grid builds admissible sampled configurations; SAMBO uses a memoized objective and its own bounded max_tries configuration.

**Limit:** Grid random acceptance and SAMBO search are distinct scientific work; compare only a fixed common accepted stream for speed.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtesting/backtesting.py:1513–1526](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1513-L1526); [backtesting/backtesting.py:1574–1605](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1574-L1605)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Fresh FractionalBacktest public run including native statistics

Backtest constructs data/broker/strategy and returns native statistics; the native fractional wrapper performs representation scaling.

**Limit:** First-call figures belong to the declared public API/component scope. Process-launch-to-first-valid includes identity, imports, data, oracle and validation, not just engine startup. No full trained research campaign or fleet-level latency guarantee.

**Measurement state:** Measured for the linked finite single-host replay campaign; broader criterion scopes remain unmeasured

**Recorded measurements:**

```json
[
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "buy_and_hold",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "first_full_common_ms_median": 51.169885,
    "first_full_common_ms_min": 43.439578,
    "first_full_common_ms_max": 61.351603,
    "launch_to_ready_ms_median": 28.618002,
    "launch_to_first_valid_ms_median": 897.881798
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "first_full_common_ms_median": 44.241377,
    "first_full_common_ms_min": 42.938463,
    "first_full_common_ms_max": 61.256882,
    "launch_to_ready_ms_median": 31.948724,
    "launch_to_first_valid_ms_median": 876.757227
  }
]
```

**Executable sources:** [backtesting/backtesting.py:1321–1354](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1354); [backtesting/backtesting.py:1373–1383](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1373-L1383); [backtesting/lib.py:536–557](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/lib.py#L536-L557)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Single Backtest.run versus fitted research campaign

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtesting/backtesting.py:1321–1354](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1354); [backtesting/backtesting.py:1373–1383](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1373-L1383)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** User Strategy.init indicators versus trained preprocessing reuse

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtesting/backtesting.py:1321–1354](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1354); [backtesting/backtesting.py:1373–1383](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1373-L1383)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Strategy.I registration and public helper indicators

The run path slices registered indicators to each current bar, but user indicator functions determine kernel complexity. Native ATR and trailing helpers are separate optional paths.

**Limit:** Shared benchmark SMA values are external; this does not benchmark user indicator kernels or resolve optional helper causality findings.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtesting/backtesting.py:1321–1354](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1354); [backtesting/lib.py:461–506](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/lib.py#L461-L506)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** FractionalBacktest.run with delayed trade_on_close and predeclared liquidation

Native bar loop, broker bookkeeping, fractional conversion and mandatory statistics are included before extracting common outputs.

**Limit:** One recorded single-instrument zero-cost contract and two fixed signals. Native APIs perform different extra work. Components and internal kernels cannot receive full-engine ratios; costs, data-size scaling, native indicators and other markets require separate campaigns.

**Measurement state:** Measured for the linked finite single-host replay campaign; broader criterion scopes remain unmeasured

**Recorded measurements:**

```json
[
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "buy_and_hold",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "warm_full_common_ms_median": 43.400759,
    "warm_engine_ms_median": 42.56645,
    "warm_extraction_common_ms_median": 0.770283,
    "warm_full_common_cpu_ms_median": 43.402356,
    "warm_process_medians_ms": [
      44.716898,
      43.400759,
      45.325396,
      42.675326,
      40.662238
    ],
    "warm_process_median_ms_min": 40.662238,
    "warm_process_median_ms_max": 45.325396,
    "warm_evaluation_bars_per_second": 202369.7327505263,
    "relative_to_limen_warm_full_common": 16.764720151884163
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "warm_full_common_ms_median": 40.925612,
    "warm_engine_ms_median": 39.99003,
    "warm_extraction_common_ms_median": 0.949704,
    "warm_full_common_cpu_ms_median": 40.929158,
    "warm_process_medians_ms": [
      40.925612,
      39.523005,
      56.856129,
      39.769402,
      51.526707
    ],
    "warm_process_median_ms_min": 39.523005,
    "warm_process_median_ms_max": 56.856129,
    "warm_evaluation_bars_per_second": 214608.88599540063,
    "relative_to_limen_warm_full_common": 20.38138237740228
  }
]
```

**Executable sources:** [backtesting/backtesting.py:1321–1354](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1354); [backtesting/backtesting.py:1373–1383](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1373-L1383); [backtesting/lib.py:536–557](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/lib.py#L536-L557)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Per-bar broker/strategy loop

The engine processes bar-based orders and strategy callbacks, with an optional finalize_trades branch.

**Limit:** Queue/depth/tick-latency and forward-label workloads require different contracts; bar-loop timing cannot stand in for them.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtesting/backtesting.py:1339–1370](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1339-L1370)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Input copies, indicator arrays, trade history and grid shared memory

Each run wraps a shallow DataFrame copy; grid optimization builds heatmaps and uses shared memory for data batches.

**Limit:** Process high-water RSS includes imported dependencies, compilation and earlier calls; it is not incremental engine memory, process-tree PSS or a hard resource bound. Multi-asset/grid/parallel memory scaling remains unmeasured.

**Measurement state:** Measured for the linked finite single-host replay campaign; broader criterion scopes remain unmeasured

**Recorded measurements:**

```json
[
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "buy_and_hold",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "peak_rss_bytes_median": 136982528
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "peak_rss_bytes_median": 136839168
  }
]
```

**Executable sources:** [backtesting/backtesting.py:1321–1334](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1334); [backtesting/backtesting.py:1529–1553](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1529-L1553)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native optimization Pool and shared memory

Grid optimization dispatches batches through Pool.imap with shared-memory conversion and collects heatmap scores.

**Limit:** No parallel scaling or optimization work is present in the single-run timing.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtesting/backtesting.py:1538–1553](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1538-L1553); [backtesting/backtesting.py:1642–1656](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1642-L1656)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** SAMBO memoized objective

The SAMBO branch wraps repeated parameter evaluations with lru_cache.

**Limit:** This caches objectives for that optimizer invocation; it is not evidence of generic fold-fitted reuse or a measured cache hit-rate improvement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtesting/backtesting.py:1597–1605](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1597-L1605)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Returned Backtest statistics versus durable search checkpoint/resume

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtesting/backtesting.py:1321–1354](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1354); [backtesting/backtesting.py:1373–1383](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1373-L1383)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Fails** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Native TrailingStrategy percentage helper used from init

The core run loop slices visible data/registered indicators through the current row. However, the shipped trailing helper backfills early ATR and fits the percentage-to-ATR multiplier on the full init sample. A recorded-fixture 192-versus-384-row probe changed the multiplier from 12.534609847694947 to 11.750024076167358 and changed all 153 fully observable historical stop distances; the fixed-six-ATR control changed zero.

**Limit:** Scope is TrailingStrategy.set_trailing_pct called in init with ATR40 and pct0.10, not every Backtest strategy. The probe reads native helper state through public Backtest.run; no orders or realized P&L were measured. Mature-row comparison excludes the 39 warmup rows; native ATR arrays themselves were equal across the common prefix.

**Executable sources:** [backtesting/backtesting.py:1321–1354](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1354); [backtesting/lib.py:471–474](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/lib.py#L471-L474); [backtesting/lib.py:492–506](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/lib.py#L492-L506); [backtesting/test/_test.py:1023–1028](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/test/_test.py#L1023-L1028)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Managed model train/evaluation isolation

Backtest constructs a strategy for one supplied data frame; optimize repeatedly evaluates parameter combinations on that frame.

**Limit:** No managed estimator train/evaluation pipeline was located in the inspected API. Add an ML adapter with explicit fit ownership for platform comparison; one-frame strategy execution is outside that training contract.

**Executable sources:** [backtesting/backtesting.py:1321–1329](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1329); [backtesting/backtesting.py:1541–1560](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1541-L1560)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Forward ML target availability

The run loop schedules strategy callbacks and processes supplied OHLC/trades without a native target-construction stage in the inspected core.

**Limit:** Label horizon, censoring and point-in-time supervision belong to a model adapter. The causal trailing-helper defect is separately captured under A01, not reclassified as label leakage.

**Executable sources:** [backtesting/backtesting.py:1339–1354](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1339-L1354)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Managed temporal validation geometry

Native optimize shares the same supplied frame among candidate evaluations.

**Limit:** A purge/embargo/nested walk-forward coordinator was not located in the inspected run/optimize API. External slicing and an adapter can provide it; repeated optimization of one frame is not such a protocol.

**Executable sources:** [backtesting/backtesting.py:1537–1563](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1537-L1563)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Fold-fitted preprocessing and stacking

Strategy.init owns indicator preparation before the core exposes per-step prefixes.

**Limit:** There is no managed estimator transform/OOF-stack fit contract in this inspected path. Registered-indicator slicing does not retrospectively make full-sample fitted transformations causal.

**Executable sources:** [backtesting/backtesting.py:1321–1345](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1345)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native strategy parameter objective

Optimize supports a named or callable objective and returns the best candidate on the evaluated data.

**Limit:** Probability calibration is outside this API. If a parameter represents a decision threshold, the reported best score is optimized in-sample performance; a separate nested validation/calibration adapter is required.

**Executable sources:** [backtesting/backtesting.py:1458–1472](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1458-L1472); [backtesting/backtesting.py:1554–1564](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1554-L1564)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native headline statistics

Returns are resampled by inferred frequency; code chooses 252/365 or weekly/monthly/yearly annualization. Native Sharpe divides geometric annualized return by a compounded-volatility expression; buy-and-hold begins after the strategy indicator warmup.

**Limit:** Native Sharpe is not the arithmetic-mean/std convention used by several peers. Warmup-dependent benchmark start, final-trade policy and frequency inference can change comparison semantics; use common raw equity/trades for shared metrics.

**Executable sources:** [backtesting/_stats.py:115–155](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/_stats.py#L115-L155); [backtesting/backtesting.py:1355–1379](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1355-L1379)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Inspected numeric regressions plus focused causal counterexample

Tests assert a complete fixed historical strategy/statistics vector, trade ledger columns and boundary behavior. This assessment executed one focused recorded-data helper prefix counterexample with a mature-row control.

**Limit:** The inspected test suite was not executed by this academic audit; the focused probe establishes one local defect, not a global numeric failure rate. Regression snapshots are weaker than an independent execution/accounting oracle.

**Executable sources:** [backtesting/test/_test.py:328–391](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/test/_test.py#L328-L391); [backtesting/lib.py:471–506](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/lib.py#L471-L506)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Statistical model convergence

Grid/SAMBO search evaluates backtest objectives; the core does not manage estimator likelihood convergence or fit-conditioning diagnostics.

**Limit:** Search-budget completion is not model convergence. Apply this criterion to an added fitted-model adapter, not to the execution loop.

**Executable sources:** [backtesting/backtesting.py:1514–1525](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1514-L1525); [backtesting/backtesting.py:1597–1621](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1597-L1621)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native parameter search result history

Grid optimization creates a parameter-indexed objective heatmap; SAMBO can return evaluated points/objectives and its raw result.

**Limit:** History return is optional, contains the selected objective rather than every full trial artifact, and does not include external or previous discarded searches. No complete failure/selection family ledger is established by the native return.

**Executable sources:** [backtesting/backtesting.py:1531–1564](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1531-L1564); [backtesting/backtesting.py:1626–1631](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1626-L1631)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Unknown** · Inspected · applicability `native` · capability `not_located`

**Scope:** Selection-adjusted inference for optimize

The inspected optimize path selects the maximum objective over its evaluated grid/SAMBO points.

**Limit:** No DSR, PBO, dependence-aware uncertainty or familywise adjustment was located in this run/optimization/statistics surface. This is a bounded capability finding, not a claim that user strategies cannot supply such analysis.

**Executable sources:** [backtesting/backtesting.py:1554–1564](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1554-L1564); [backtesting/_stats.py:139–155](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/_stats.py#L139-L155)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Per-run performance and search outputs

Run returns full equity/trade artifacts with dates; parameter heatmaps retain candidate coordinates.

**Limit:** No canonical input-byte/code/environment equality gate was located here. Indicator-dependent warmup changes the effective evaluation/benchmark start even when nominal input dates match, so common contracts must freeze burn-in and finalization.

**Executable sources:** [backtesting/backtesting.py:1331–1339](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1331-L1339); [backtesting/_stats.py:115–117](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/_stats.py#L115-L117); [backtesting/test/_test.py:376–391](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/test/_test.py#L376-L391); [backtesting/backtesting.py:1531–1535](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1531-L1535)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Protected final holdout protocol

Native optimize reuses the supplied frame and reruns its best parameter set.

**Limit:** No separate reserved final-data access/freeze protocol was located in that API. A testing adapter must own final holdout admission and distinguish repeated validation from a first final evaluation.

**Executable sources:** [backtesting/backtesting.py:1537–1564](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1537-L1564)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Economic external validity and baseline quality

The statistics include a long-only buy-and-hold benchmark and the repository contains executable historical strategy regressions.

**Limit:** The buy-and-hold comparator is price-only and warmup-dependent; it is not automatically a cost/exposure-matched economic null. No matched independent study here establishes live fill realism or predictive edge.

**Executable sources:** [backtesting/_stats.py:115–117](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/_stats.py#L115-L117); [backtesting/test/_test.py:328–363](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/test/_test.py#L328-L363)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Parameter sweeps and random OHLC sensitivity

Random-state-controlled grid sampling and a random_ohlc_data generator provide sensitivity primitives.

**Limit:** The generator calls DataFrame.sample with the same supplied random_state on every yield; a fixed integer replays that sample instead of advancing a local seeded stream. Its row/gap resampling also does not preserve general serial dependence. No mandatory ablation/independent-regime protocol is present in these helpers.

**Executable sources:** [backtesting/backtesting.py:1514–1523](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1514-L1523); [backtesting/lib.py:338–372](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/lib.py#L338-L372)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native Python Strategy and optional commission callback; full managed research workflow is a separate layer.

The public core accepts a Strategy subclass and calls its Python init/run callbacks. No constrained declarative callable resolver participates in this route.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtesting/backtesting.py:1195–1223](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1195-L1223); [backtesting/backtesting.py:1321–1329](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1329)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Backtest constructor and native broker admission.

The constructor checks DataFrame type, nonempty OHLC columns and missing OHLC values; sorts unsorted indices. Broker cash/margin and fee-range checks use Python assertions, while order bracket ordering uses explicit errors.

**Limit:** Assertions can be disabled with Python -O. The inspected constructor does not establish finite-positive OHLC, unique timestamps or OHLC cross-consistency. Negative relative fees inside the accepted range are explicit rebates.

**Executable sources:** [backtesting/backtesting.py:1195–1269](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1195-L1269); [backtesting/backtesting.py:728–759](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L728-L759); [backtesting/backtesting.py:765–814](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L765-L814)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Finite data iteration and native parameter optimization.

The backtest iterates a finite input length. Optimization enumerates admissible parameter combinations and uses max_tries as a sampling fraction/target; shared-memory context cleanup is implemented.

**Limit:** No hard time/RAM quota for arbitrary Strategy callbacks or the full parameter product is established. max_tries sampling is not an exact resource deadline or a strict accepted-combination cap.

**Executable sources:** [backtesting/backtesting.py:1341–1379](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1341-L1379); [backtesting/backtesting.py:1505–1559](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1505-L1559); [backtesting/_util.py:278–343](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/_util.py#L278-L343)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native in-memory DataFrame backtest; full managed research workflow is a separate layer.

Core Backtest accepts an already-loaded DataFrame; a network downloader or archive extraction boundary is outside this selected route.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtesting/backtesting.py:1195–1269](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1195-L1269)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native in-memory backtest result; full managed research workflow is a separate layer.

The selected run constructs in-memory broker/strategy state and a result series; it does not implement a content-addressed research-round log or durable restart frontier.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtesting/backtesting.py:1321–1379](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1379)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native in-memory backtest result; full managed research workflow is a separate layer.

The selected run constructs in-memory broker/strategy state and a result series; it does not implement a content-addressed research-round log or durable restart frontier.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtesting/backtesting.py:1321–1379](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1379)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native in-memory backtest result; full managed research workflow is a separate layer.

The selected run constructs in-memory broker/strategy state and a result series; it does not implement a content-addressed research-round log or durable restart frontier.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtesting/backtesting.py:1321–1379](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1379)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native Backtest.optimize multiprocessing and shared arrays.

Pool and SharedMemoryManager are context-managed; optimization consumes imap results, and shared-memory blocks are closed/unlinked on context exit.

**Limit:** No worker task deadline, committed-prefix persistence or recovery of completed work after worker death was established. Strategy exceptions and hard process kills were not injected in this review.

**Executable sources:** [backtesting/backtesting.py:1540–1559](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1540-L1559); [backtesting/_util.py:278–343](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/_util.py#L278-L343)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native Strategy callback execution; full managed research workflow is a separate layer.

The engine has indicator warmup and order validation, but a probability-valued inference object with an explicit unavailable contract is outside the fixed Strategy route.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtesting/backtesting.py:1331–1360](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1331-L1360)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Partial** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Core row loop and the native trailing-stop helper.

Core run slices data and registered indicator arrays through the current row and processes broker orders before the next Strategy callback. Strategy.init can see the full batch. TrailingStrategy.set_trailing_pct computes a whole-batch average used by historical stops.

**Limit:** Core chronology is conditional on causal user calculations and helper selection. The separately reproduced percentage-trailing helper changes historical stop distances under prefix extension; it does not establish changed executed orders or PnL for every strategy.

**Executable sources:** [backtesting/backtesting.py:1321–1355](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1321-L1355); [backtesting/lib.py:471–506](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/lib.py#L471-L506)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native broker affordability with finite valid inputs and configured margin/commission.

Order sizing includes spread/commission; insufficient post-cost buying power cancels an opening order. Nonpositive account equity closes trades, clamps subsequent equity to zero and stops simulation.

**Limit:** Margin explicitly permits leverage; this is the configured simulator accounting rule, not a universal cash-only constraint or live liquidation guarantee. Custom commission callbacks remain trusted code.

**Executable sources:** [backtesting/backtesting.py:956–980](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L956-L980); [backtesting/backtesting.py:1007–1014](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1007-L1014); [backtesting/backtesting.py:855–873](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L855-L873)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** OHLC stop/limit and terminal-position semantics.

Contingent stops are prioritized; opening gaps and stop/limit ordering have explicit price logic. Some same-bar contingent ambiguities defer execution with a warning. Terminal liquidation is controlled by finalize_trades.

**Limit:** Bar-level assumptions do not reconstruct an order book or guaranteed queue fill; open terminal positions and forced close are different experiments.

**Executable sources:** [backtesting/backtesting.py:887–919](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L887-L919); [backtesting/backtesting.py:1028–1047](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1028-L1047); [backtesting/backtesting.py:1362–1379](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1362-L1379)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native strategy backtest and parameter optimization; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtesting/backtesting.py:1505–1559](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/backtesting.py#L1505-L1559)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Pinned repository CI configuration.

CI contains source tests/coverage across Python/dependency variants and commit-pinned checkout/setup actions; dependencies are installed/upgraded without a hash-closed environment in the inspected workflow.

**Limit:** Configured CI was inspected, not executed or verified as a protected hosted gate. A keepalive job has separately scoped actions write access; dependency provenance and all release paths require separate review.

**Executable sources:** [.github/workflows/ci.yml:12–65](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/.github/workflows/ci.yml#L12-L65); [.github/workflows/ci.yml:93–99](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/.github/workflows/ci.yml#L93-L99)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Adversarial numerical and execution assertions in native tests plus the local helper probe.

Tests assert missing/OHLC rejection, insufficient-margin behavior, stop precedence and adverse-gap prices. A separate recorded-fixture probe reproduces non-prefix-invariant percentage-trailing stop distances.

**Limit:** The candidate suite was inspected, not run as a full security campaign. No general malformed-input fuzzer, crash-recovery mutation coverage or live execution guarantee is inferred.

**Executable sources:** [backtesting/test/_test.py:100–110](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/test/_test.py#L100-L110); [backtesting/test/_test.py:238–249](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/test/_test.py#L238-L249); [backtesting/test/_test.py:1245–1268](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/test/_test.py#L1245-L1268); [backtesting/test/_test.py:1297–1313](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/backtesting/test/_test.py#L1297-L1313)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

