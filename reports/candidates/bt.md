# bt

**Frozen source:** [pmorissette/bt @ 4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12](https://github.com/pmorissette/bt/tree/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12)

**Observed license label:** MIT  
**Layer:** Hierarchical portfolio allocation and account simulation

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Source-compiled Cython portfolio replay is admitted, including native ffn statistics; a single-asset result does not establish tree/grid scaling.

**Academic:** Native trailing portfolio estimators operate on bounded histories; supervised research, multiple-search correction and final holdout require an adapter.

**Safety:** Targeted finite-cost/state-preservation checks and bounded allocation iteration; direct transaction, borrowing and fixed-income semantics need a declared account contract.

## P01

### Parameter-space construction and retained memory

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Supplied Backtest objects and algorithm tree versus a parameter-domain generator

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [bt/backtest.py:236–244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L236-L244); [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Sequential supplied-backtest collection versus search proposal/exhaustion

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [bt/backtest.py:17–36](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L17-L36)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Fresh source-compiled bt process through native run/statistics

The build compiles core.py with Cython; Backtest deep-copies the strategy and computes native statistics after the date loop.

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
    "first_full_common_ms_median": 5082.93494,
    "first_full_common_ms_min": 4962.742817,
    "first_full_common_ms_max": 6086.576166,
    "launch_to_ready_ms_median": 33.067982,
    "launch_to_first_valid_ms_median": 6710.300237
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "first_full_common_ms_median": 4978.945781,
    "first_full_common_ms_min": 4642.414749,
    "first_full_common_ms_max": 5086.581349,
    "launch_to_ready_ms_median": 33.475505,
    "launch_to_first_valid_ms_median": 6409.784947
  }
]
```

**Executable sources:** [bt/backtest.py:236–244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L236-L244); [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488); [pyproject.toml:124–132](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/pyproject.toml#L124-L132)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Native portfolio algorithm stack versus matched ML campaign

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [bt/backtest.py:236–244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L236-L244); [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Rolling portfolio allocation algorithms versus fitted supervised preprocessing

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [bt/backtest.py:236–244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L236-L244); [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** User/algorithm-stack feature and allocation work

Native strategy trees cache backing numeric arrays; algorithm choices can invoke external optimization/statistics routines.

**Limit:** No comparable native indicator-kernel throughput measurement; common SMA decisions are computed before timed calls.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [bt/core.py:140–177](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L140-L177); [bt/core.py:2214–2232](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L2214-L2232); [bt/algos.py:1231–1244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1231-L1244); [bt/algos.py:1318–1330](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1318-L1330)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Source-compiled hierarchical portfolio Backtest.run

Fresh strategy state runs across dates, invokes native transaction/account updates and computes native ffn statistics.

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
    "warm_full_common_ms_median": 5308.30286,
    "warm_engine_ms_median": 95.619316,
    "warm_extraction_common_ms_median": 5221.771042,
    "warm_full_common_cpu_ms_median": 5307.879589,
    "warm_process_medians_ms": [
      5308.30286,
      5571.318686,
      5031.107884,
      5465.755874,
      4866.026563
    ],
    "warm_process_median_ms_min": 4866.026563,
    "warm_process_median_ms_max": 5571.318686,
    "warm_evaluation_bars_per_second": 1654.5777872214323,
    "relative_to_limen_warm_full_common": 2050.475935901175
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "warm_full_common_ms_median": 5088.201298,
    "warm_engine_ms_median": 87.143287,
    "warm_extraction_common_ms_median": 5005.687387,
    "warm_full_common_cpu_ms_median": 5087.734535,
    "warm_process_medians_ms": [
      4956.331892,
      5097.217632,
      5375.004831,
      5088.201298,
      4517.369153
    ],
    "warm_process_median_ms_min": 4517.369153,
    "warm_process_median_ms_max": 5375.004831,
    "warm_evaluation_bars_per_second": 1726.150261282371,
    "relative_to_limen_warm_full_common": 2533.977409250046
  }
]
```

**Executable sources:** [bt/backtest.py:236–244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L236-L244); [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native date-driven strategy/security account updates

Backtest iterates dates; strategies update their hierarchy and securities transact actual quantities/fees.

**Limit:** This is portfolio allocation/date execution; queue/market microstructure and forward-label scaling are separate workloads.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [bt/backtest.py:470–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L470-L488); [bt/core.py:1532–1605](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L1532-L1605)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Strategy copy, tree state and numeric history arrays

Backtest copies its strategy, while core caches NumPy array views and records cash/fees/value histories.

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
    "peak_rss_bytes_median": 252366848
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "peak_rss_bytes_median": 252469248
  }
]
```

**Executable sources:** [bt/backtest.py:236–244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L236-L244); [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488); [bt/core.py:680–700](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L680-L700)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Top-level bt.run over supplied backtests

The inspected bt.run function loops backtests serially.

**Limit:** This bounded path does not establish that user code cannot parallelize independent runs; no native parallel speedup measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [bt/backtest.py:17–36](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L17-L36)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native state-array views and dirty/update paths

Core checks/caches backing numeric arrays and tracks strategy/security state across date updates.

**Limit:** Internal state reuse is not a prediction/model cache. No cache-hit or invalidation cost ablation.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [bt/core.py:140–177](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L140-L177); [bt/core.py:680–700](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L680-L700); [bt/core.py:916–919](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L916-L919)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Returned native Result/statistics versus crash-safe research resume

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [bt/backtest.py:236–244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L236-L244); [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native portfolio universe and estimation windows

Backtest rejects non-monotone timestamps; the public universe property exposes data through target.now. Inverse-volatility/ERC/mean-variance estimators cut their input to now minus an explicit lag and lookback.

**Limit:** This establishes local information boundaries for the inspected built-ins. Strategy setup/additional data/custom algos remain trusted, and duplicate timestamps are accepted. Signal formation versus rebalance price timing still requires an explicit common contract.

**Executable sources:** [bt/backtest.py:227–240](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L227-L240); [bt/core.py:552–566](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L552-L566); [bt/algos.py:1231–1244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1231-L1244); [bt/algos.py:1318–1330](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1318-L1330); [tests/test_backtest.py:50–60](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/tests/test_backtest.py#L50-L60)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native rolling portfolio estimators

Built-in weight estimators use trailing returns through a configured lagged decision time rather than fitting one covariance over the entire backtest. Backtest deep-copies strategy templates.

**Limit:** This is online portfolio-estimation isolation, not a supervised train/validation/test research manager. Choices of lookback, covariance model and strategy family still need external validation.

**Executable sources:** [bt/algos.py:1231–1244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1231-L1244); [bt/algos.py:1318–1330](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1318-L1330); [bt/backtest.py:235–240](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L235-L240)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Forward supervised target availability

Native inverse-volatility/ERC/mean-variance algos fit return moments rather than future supervised labels.

**Limit:** Target horizon censoring is outside this portfolio-estimation contract. Apply it to an added predictive-model adapter; do not penalize the native engine for absent target construction.

**Executable sources:** [bt/algos.py:1231–1244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1231-L1244); [bt/algos.py:1386–1395](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1386-L1395)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Lookback/lag geometry for portfolio estimation

Inverse-volatility estimation supports trailing row counts or date offsets with lag; ERC and mean-variance use date-window lookbacks.

**Limit:** These rolling estimation windows are not a purged/nested out-of-sample experiment coordinator. When a learned forecast is introduced, its horizon/fit isolation must be supplied separately.

**Executable sources:** [bt/algos.py:1231–1236](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1231-L1236); [bt/algos.py:1318–1328](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1318-L1328); [bt/algos.py:1386–1393](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1386-L1393)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Local moments and covariance fitting

Inverse-volatility recomputes sample volatility within the current lookback and drops invalid weights; ERC/mean-variance pass only trailing returns to covariance/optimization functions.

**Limit:** General feature preprocessing/OOF stacking is outside these algos. Covariance/solver implementation also depends on external ffn; this source audit establishes the passed data boundary, not all dependency internals.

**Executable sources:** [bt/algos.py:1231–1244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1231-L1244); [bt/algos.py:1318–1330](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1318-L1330); [bt/algos.py:1386–1395](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1386-L1395)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Probability calibration/nested classification thresholds

The inspected native portfolio algos return weights derived from historical return moments.

**Limit:** No calibrated prediction or nested classification-threshold selection protocol was located in these algos. That research feature requires an explicit model adapter.

**Executable sources:** [bt/algos.py:1231–1244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1231-L1244); [bt/algos.py:1386–1395](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1386-L1395)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native equity selection and delegated ffn statistics

Backtest creates a virtual initial reference row, preserves strategy equity and computes metric input from one row before the first transaction. Native summary statistics delegate to ffn calc_perf_stats/GroupStats.

**Limit:** Metrics are dependency-bounded in this audit: bt declares ffn>=1.1.2, not an exact source revision. Trade-dependent starting dates can yield different sample lengths for nominally identical input periods; common metrics should use a frozen evaluation interval.

**Executable sources:** [bt/backtest.py:417–423](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L417-L423); [bt/backtest.py:486–509](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L486-L509); [bt/backtest.py:637–641](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L637-L641); [pyproject.toml:38–38](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/pyproject.toml#L38-L38)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected chronology, accounting and baseline regression tests

Tests assert non-monotone date rejection and explicitly solve a costed allocation equation independently before checking resulting position, fees and NAV in random-baseline execution.

**Limit:** These tests were inspected, not executed in this academic audit. They are valuable independent numeric examples but do not prove every strategy/solver/dependency path.

**Executable sources:** [tests/test_backtest.py:38–60](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/tests/test_backtest.py#L38-L60); [tests/test_backtest.py:671–707](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/tests/test_backtest.py#L671-L707)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Portfolio optimization convergence controls

ERC exposes maximum_iterations and tolerance and forwards them with covariance/risk-parity choices to ffn; mean-variance forwards weight bounds and risk-free rate.

**Limit:** The inspected bt wrapper drops NaN weights but does not inspect an explicit convergence report. Dependency solver acceptance and sensitivity remain outside the code boundary reviewed here.

**Executable sources:** [bt/algos.py:1286–1331](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1286-L1331); [bt/algos.py:1386–1396](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1386-L1396)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Returned collections of supplied backtests/random trials

Result retains the supplied backtest list and name mapping; benchmark_random executes the requested simulations under copied assumptions and returns them for comparison.

**Limit:** This preserves locally supplied successful results, not a durable ledger of failed/interrupted or externally selected strategy families. Duplicate names and caller selection require independent provenance checks.

**Executable sources:** [bt/backtest.py:97–113](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L97-L113); [bt/backtest.py:637–641](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L637-L641); [bt/backtest.py:797–802](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L797-L802)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Unknown** · Inspected · applicability `native` · capability `not_located`

**Scope:** Selection/dependence correction

RandomBenchmarkResult separates base and random statistics and plots their distribution against the base.

**Limit:** No multiplicity correction, DSR/PBO or dependence-adjusted hypothesis test was located in this benchmark/result surface. A histogram of an optional random family is not automatically valid post-selection inference.

**Executable sources:** [bt/backtest.py:797–802](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L797-L802); [bt/backtest.py:836–843](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L836-L843)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Matched random-baseline assumptions and native results

benchmark_random preserves original capital, commission/cost model, integer-position policy, impact inputs and copied additional data; Result retains underlying backtests.

**Limit:** Useful local comparability does not establish source/data-byte/environment equality across independent runs. Native stats may start at different first-transaction dates, which the benchmark adapter must normalize.

**Executable sources:** [bt/backtest.py:90–113](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L90-L113); [bt/backtest.py:490–509](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L490-L509); [bt/backtest.py:637–641](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L637-L641); [tests/test_backtest.py:702–707](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/tests/test_backtest.py#L702-L707)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Protected final holdout admission

The native runner evaluates supplied data/strategy configurations and can compare many supplied or randomized backtests.

**Limit:** No reservation, model freeze or first-access holdout mechanism was located in this runner/result surface. Final research evaluation needs a separate adapter.

**Executable sources:** [bt/backtest.py:448–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L448-L488); [bt/backtest.py:97–113](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L97-L113)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Random portfolio baselines and economic generalization

A native random-strategy benchmark reuses capital/cost/position assumptions and retains each baseline. This is a useful basis for matched portfolio nulls.

**Limit:** Null quality depends on the user-supplied random strategy and choices made before looking at outcomes. No independent matched study here establishes economic generalization or predictive edge.

**Executable sources:** [bt/backtest.py:90–113](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L90-L113); [bt/backtest.py:797–802](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L797-L802); [tests/test_backtest.py:671–707](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/tests/test_backtest.py#L671-L707)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Randomized baseline and portfolio-parameter sensitivity

Random strategies, explicit lookback/lag/covariance settings and repeated backtests permit structured sensitivity experiments.

**Limit:** Random selection calls the global Python random generator and random weights delegate to ffn; the inspected benchmark entry point does not own a complete multi-library seed/ablation manifest. Reproducibility and independent regime selection remain caller-owned.

**Executable sources:** [bt/algos.py:1286–1305](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1286-L1305); [bt/algos.py:828–837](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L828-L837); [bt/algos.py:1431–1445](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/algos.py#L1431-L1445); [bt/backtest.py:97–113](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L97-L113)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native Python Strategy tree and callbacks; full managed research workflow is a separate layer.

Backtest deep-copies and runs the caller's Python Strategy tree and callback objects. No constrained declarative callable loader is part of this selected route.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [bt/backtest.py:214–282](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L214-L282); [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Backtest admission, security prices and transaction state mutation.

Duplicate columns and nonmonotone input indices are rejected; optional CostModel inputs require matching axes and finite nonnegative values. Security updates reject nonfinite held values and transaction outlay/costs are checked before financial state changes.

**Limit:** Missing unheld prices and some NaN quantity paths have deliberate skip semantics. These checks do not establish equivalent validation for every Algo/custom callback or all duplicate timestamps.

**Executable sources:** [bt/backtest.py:214–282](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L214-L282); [bt/core.py:1532–1581](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L1532-L1581); [bt/core.py:1788–1816](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L1788-L1816)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native capital-allocation iterative sizing.

The nonlinear outlay sizing loop raises after its iteration counter exceeds 10,000 and also detects stagnant integer quantities and divergence.

**Limit:** This bounds the selected numerical loop, not arbitrary Algo runtime, preprocessing size or process memory. Large data and callback quotas remain caller responsibilities.

**Executable sources:** [bt/core.py:1613–1649](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L1613-L1649); [bt/core.py:1727–1754](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L1727-L1754)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native in-memory portfolio data; full managed research workflow is a separate layer.

The selected backtest receives already-loaded pandas data. Network acquisition and archive containment require separate ingestion adapters.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [bt/backtest.py:214–282](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L214-L282)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native in-memory Strategy tree execution; full managed research workflow is a separate layer.

The native run marks has_run before setup and updates in-memory strategy state. It does not implement a managed-round content identity or durable restart transaction; a failed run requires fresh state for reproducible retry.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native in-memory Strategy tree execution; full managed research workflow is a separate layer.

The native run marks has_run before setup and updates in-memory strategy state. It does not implement a managed-round content identity or durable restart transaction; a failed run requires fresh state for reproducible retry.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native in-memory Strategy tree execution; full managed research workflow is a separate layer.

The native run marks has_run before setup and updates in-memory strategy state. It does not implement a managed-round content identity or durable restart transaction; a failed run requires fresh state for reproducible retry.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native sequential portfolio loop; full managed research workflow is a separate layer.

The selected run executes a strategy sequentially. Multiworker dispatch, worker death and persisted completed-prefix recovery belong to a separate executor.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native Algo-to-allocation route; full managed research workflow is a separate layer.

The selected route models allocations/orders, not a shared probability-output schema. Financial finite-value checks do not create an inference availability contract.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [bt/backtest.py:470–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L470-L488); [bt/core.py:1788–1816](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L1788-L1816)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native chronological Strategy updates.

Backtest requires nondecreasing input index and updates a strategy for each date before/after running its Algo stack; the full data object is available during strategy setup.

**Limit:** Trusted Algos can access future rows in supplied data. Chronological iteration alone does not enforce feature availability or data authenticity.

**Executable sources:** [bt/backtest.py:214–244](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L214-L244); [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Portfolio capital allocation and insolvency model.

Allocation solves for commission-inclusive outlay; finite transaction costs are checked before mutation. A non-fixed-income root strategy is marked bankrupt and flattened when value becomes negative.

**Limit:** Direct transact is not a universal cash-only affordability gate and strategy-defined leverage can be intentional. Fixed-income semantics explicitly differ; no live margin/liquidation claim follows.

**Executable sources:** [bt/core.py:1613–1757](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L1613-L1757); [bt/core.py:1788–1816](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L1788-L1816); [bt/core.py:824–826](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L824-L826)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `adapter_required` · capability `implemented`

**Scope:** Portfolio execution price/cost callbacks.

Security transactions account for provided price, bid/offer and configured costs, with finite outlay checks before mutation.

**Limit:** The selected portfolio-rebalance engine does not reconstruct intrabar SL/TP precedence, order-book depth or queue position. Those execution semantics require an adapter before comparison with Limen event or specialist order-book engines.

**Executable sources:** [bt/core.py:1788–1816](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/core.py#L1788-L1816)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native portfolio strategy backtest; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [bt/backtest.py:440–488](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/bt/backtest.py#L440-L488)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Checked-in build/test workflow.

The workflow uses commit-pinned setup/artifact actions and executes dependency installation, lint/checks and coverage through Make targets.

**Limit:** This inspection does not establish a hash-closed installed graph, vulnerability-free dependencies, hosted success or required branch protections.

**Executable sources:** [.github/workflows/build.yaml:52–88](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/.github/workflows/build.yaml#L52-L88)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Adversarial transaction-cost assertions.

A parameterized test asserts nonfinite transaction cost rejection and verifies unchanged position, cash, fees, stale flags and both state DataFrames.

**Limit:** The assertions were inspected, not executed here. No whole-system crash/fuzz/mutation coverage follows from this targeted state-preservation test.

**Executable sources:** [tests/test_core.py:3467–3511](https://github.com/pmorissette/bt/blob/4b76bad2dbf3a49e99feb49db3eee1dde2ef8e12/tests/test_core.py#L3467-L3511)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

