# Backtrader

**Frozen source:** [mementum/backtrader @ b853d7c90b6721476eb5a5ea3135224e33db1f14](https://github.com/mementum/backtrader/tree/b853d7c90b6721476eb5a5ea3135224e33db1f14)

**Observed license label:** GPL-3.0  
**Layer:** Strategy, broker, feed and indicator execution framework

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Full Cerebro replay is admitted; preload/runonce, exactbars and optimization multiprocessing are distinct native tradeoffs.

**Academic:** Default event/indicator chronology has concrete controls, while cheat modes, external reads and user-owned research stages require explicit contracts.

**Safety:** Native cash/submission checks and cancellation behavior are scoped controls; arbitrary strategy code remains trusted and durable research governance is an adapter responsibility.

## P01

### Parameter-space construction and retained memory

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Cerebro.optstrategy parameter construction

Nested itertools.product calls construct parameter pools. The outer product consumes optargs and optkwargs, so an iterator return type does not make all Cartesian parameter construction lazy.

**Limit:** Retained pools and completed runstrats can grow with the parameter family; no memory-versus-family-size sweep was executed.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtrader/cerebro.py:891–906](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L891-L906); [backtrader/cerebro.py:1126–1153](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1126-L1153)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native finite optstrategy enumeration

Cerebro consumes the configured product and retains results, with serial and process-pool branches.

**Limit:** No accepted-candidate throughput, duplicate-domain behavior or exhaustion scaling measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtrader/cerebro.py:1126–1157](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1126-L1157); [backtrader/cerebro.py:1649–1711](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1649-L1711)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Fresh Cerebro source-built process through extracted result

Imports, adapter construction, first native run and common-output extraction are separated by the benchmark runner.

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
    "first_full_common_ms_median": 740.089799,
    "first_full_common_ms_min": 636.90746,
    "first_full_common_ms_max": 888.406114,
    "launch_to_ready_ms_median": 31.646045,
    "launch_to_first_valid_ms_median": 2453.576366
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "first_full_common_ms_median": 692.079575,
    "first_full_common_ms_min": 628.118666,
    "first_full_common_ms_max": 848.223453,
    "launch_to_ready_ms_median": 31.360242,
    "launch_to_first_valid_ms_median": 2230.690846
  }
]
```

**Executable sources:** [backtrader/cerebro.py:1126–1157](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1126-L1157); [backtrader/cerebro.py:1649–1711](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1649-L1711)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Cerebro fixed-rule execution versus a model-selection campaign

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtrader/cerebro.py:1126–1157](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1126-L1157); [backtrader/cerebro.py:1649–1711](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1649-L1711)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Native Cerebro indicator/strategy execution versus learned preprocessing

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtrader/cerebro.py:1126–1157](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1126-L1157); [backtrader/cerebro.py:1649–1711](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1649-L1711)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** runonce indicators versus next/event execution

The runonce path runs indicator once methods before bar iteration; exactbars can disable runonce/preload.

**Limit:** The shared SMA decisions are prepared outside every engine timing. Native indicator-kernel throughput and equivalence were not measured.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtrader/cerebro.py:1061–1075](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1061-L1075); [backtrader/cerebro.py:1649–1665](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1649-L1665)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** One-strategy Cerebro with preload/runonce and disabled optional observers

A fresh Cerebro strategy/broker path executes every evaluation; full-common timing includes extraction and explicit delayed close fills.

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
    "warm_full_common_ms_median": 690.585529,
    "warm_engine_ms_median": 688.656367,
    "warm_extraction_common_ms_median": 0.721619,
    "warm_full_common_cpu_ms_median": 690.536354,
    "warm_process_medians_ms": [
      656.077672,
      690.585529,
      671.561543,
      691.38636,
      789.3858
    ],
    "warm_process_median_ms_min": 656.077672,
    "warm_process_median_ms_max": 789.3858,
    "warm_evaluation_bars_per_second": 12718.192940877567,
    "relative_to_limen_warm_full_common": 266.7573886121642
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "warm_full_common_ms_median": 661.02671,
    "warm_engine_ms_median": 660.305411,
    "warm_extraction_common_ms_median": 0.784644,
    "warm_full_common_cpu_ms_median": 661.003221,
    "warm_process_medians_ms": [
      683.216707,
      661.02671,
      653.369654,
      672.146249,
      646.042415
    ],
    "warm_process_median_ms_min": 646.042415,
    "warm_process_median_ms_max": 683.216707,
    "warm_evaluation_bars_per_second": 13286.906364192153,
    "relative_to_limen_warm_full_common": 329.19820815840717
  }
]
```

**Executable sources:** [backtrader/cerebro.py:1126–1157](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1126-L1157); [backtrader/cerebro.py:1649–1711](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1649-L1711)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native event loop, feeds, broker and strategy state

Both next and runonce paths advance engine state; richer order/feed/timer workloads add work absent from this fixed close contract.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtrader/cerebro.py:1498–1538](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1498-L1538); [backtrader/cerebro.py:1649–1711](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1649-L1711)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Single-process preload/runonce and native history retention

Native exactbars changes retained line history and disables execution optimizations; the admitted benchmark uses full input histories.

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
    "peak_rss_bytes_median": 131973120
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "peak_rss_bytes_median": 131973120
  }
]
```

**Executable sources:** [backtrader/cerebro.py:1061–1075](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1061-L1075); [backtrader/cerebro.py:1137–1154](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1137-L1154)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** optstrategy multiprocessing pool

The optimization branch preloads eligible data and uses Pool.imap, with configured maxcpus and returned strategy/optreturn work.

**Limit:** No worker-count sweep, speedup, scheduling imbalance or cross-worker scientific equivalence campaign was run.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtrader/cerebro.py:1126–1157](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1126-L1157); [backtrader/cerebro.py:1649–1711](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1649-L1711)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Line/indicator object cache and optimization preload

Cerebro clears and selectively enables indicator/line caches at run start; eligible optimization shares preloaded inputs.

**Limit:** These caches are not fitted-model reuse. Hit cost, eviction and invalidation under source mutation are unmeasured.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [backtrader/cerebro.py:1054–1060](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1054-L1060); [backtrader/cerebro.py:1137–1157](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1137-L1157)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native result recording, separately from research checkpoint/resume

Native optional WriterFile records engine data/statistics.

**Limit:** Native result-write overhead is unmeasured. Crash-safe continuation and an exact multi-round durable commit frontier are not established by these serialization paths.

**Measurement state:** Not measured in this criterion scope

**Distinct sub-capabilities:** native_recording: Implemented; complete_checkpoint_continuation: Unknown/not located in the cited result-write path

**Executable sources:** [backtrader/cerebro.py:1475–1492](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1475-L1492); [backtrader/writer.py:117–163](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/writer.py#L117-L163)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native chronological dispatch and precomputed mode

The event loop advances data and dispatches broker updates before ordinary strategy callbacks. The vectorized mode resets computed lines and advances only feeds with the earliest next timestamp before callbacks.

**Limit:** User code remains trusted: line indexing directly addresses the backing array at current index plus offset, so preloaded future values can be accessed deliberately. Cheat-on-open is an explicit alternate execution contract, not evidence that normal chronology fails.

**Executable sources:** [backtrader/cerebro.py:1538–1559](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1538-L1559); [backtrader/cerebro.py:1620–1635](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1620-L1635); [backtrader/cerebro.py:1656–1700](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1656-L1700); [backtrader/linebuffer.py:162–163](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/linebuffer.py#L162-L163)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Managed estimator train/evaluation isolation

Cerebro runs supplied strategy classes over configured data feeds and enumerates parameter combinations.

**Limit:** A native supervised fit/evaluate owner was not located in this inspected surface. Strategy-level estimation needs an adapter that freezes training and evaluation data separately.

**Executable sources:** [backtrader/cerebro.py:892–906](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L892-L906); [backtrader/cerebro.py:1127–1136](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1127-L1136)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Forward target availability/censoring

The inspected engine/feed loop consumes market data and strategy callbacks; it does not own a supervised target stage.

**Limit:** Future label horizons and availability-time censoring become applicable to an added ML research adapter, not a fixed-signal execution test.

**Executable sources:** [backtrader/cerebro.py:1538–1559](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1538-L1559); [backtrader/cerebro.py:1632–1635](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1632-L1635)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Temporal validation coordinator

optstrategy forms Cartesian parameter combinations over the configured feeds.

**Limit:** A purge/embargo/nested validation coordinator was not located in this API. Separate data feed date ranges can be caller-configured, but they are not automatic statistical isolation.

**Executable sources:** [backtrader/cerebro.py:892–906](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L892-L906); [backtrader/cerebro.py:1127–1151](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1127-L1151)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Fold-local fitted preprocessing and stacking

Indicators may precompute over arrays while strategy callbacks advance one event at a time.

**Limit:** No fold-owned estimator preprocessing/OOF stacking protocol was located in this engine path. Mathematical causality of custom indicators and transform fit boundaries remain adapter obligations.

**Executable sources:** [backtrader/cerebro.py:1656–1700](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1656-L1700)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Probability calibration and threshold nesting

The native optimization API enumerates strategy parameter sets and returns parameter/analyzer results.

**Limit:** A native calibrated-probability or nested threshold-selection owner was not located here. Compare this capability when a model adapter is supplied, not from analyzer headline metrics.

**Executable sources:** [backtrader/cerebro.py:892–906](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L892-L906); [backtrader/cerebro.py:1322–1336](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1322-L1336)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native Sharpe and time-return analyzers

TimeReturn can track portfolio NAV, fund value or a data price. Sharpe defaults to yearly periods, 1% annual risk-free rate, population standard deviation and no additional annualization; factors and sample correction are configurable.

**Limit:** These defaults differ materially from peers using daily sample volatility and zero risk-free rate. Return source, first-open rule, timeframe, annualization and fund treatment must be fixed explicitly in shared comparisons.

**Executable sources:** [backtrader/analyzers/timereturn.py:96–141](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/analyzers/timereturn.py#L96-L141); [backtrader/analyzers/sharpe.py:112–132](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/analyzers/sharpe.py#L112-L132); [backtrader/analyzers/sharpe.py:153–202](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/analyzers/sharpe.py#L153-L202)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected mode-parity and known-value regressions

Indicator test harnesses exercise preload/runonce/exactbars combinations against fixed expected values. The optimized-strategy test asserts expected cash/equity vectors across execution modes and parameter periods.

**Limit:** These tests were inspected, not executed in this academic audit. Their equivalence coverage is meaningful but does not prove all user strategies or independent fill-model realism.

**Executable sources:** [tests/test_ind_sma.py:29–46](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/tests/test_ind_sma.py#L29-L46); [tests/testcommon.py:73–111](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/tests/testcommon.py#L73-L111); [tests/testcommon.py:206–223](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/tests/testcommon.py#L206-L223); [tests/test_strategy_optimized.py:125–145](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/tests/test_strategy_optimized.py#L125-L145)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Managed statistical fit convergence

Cerebro parameter optimization schedules strategy simulations rather than a native supervised model-fitting loop.

**Limit:** Estimator convergence/warnings and conditioning must be evaluated in the model adapter. Indicator warmup and simulator completion are different properties.

**Executable sources:** [backtrader/cerebro.py:1127–1151](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1127-L1151)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native optimization outputs

Cerebro retains all returned run results and invokes callbacks for finished candidates; optimized return objects carry parameters, analyzers and strategy class.

**Limit:** This is in-memory completed-result coverage, not a durable ledger of failed, interrupted, external or previous searches. A full search family requires caller-owned recording and common admission rules.

**Executable sources:** [backtrader/cerebro.py:1127–1163](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1127-L1163); [backtrader/cerebro.py:1322–1336](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1322-L1336)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Unknown** · Inspected · applicability `native` · capability `not_located`

**Scope:** Multiple-selection/dependence inference

The inspected optimization and Sharpe analyzer paths enumerate candidates and calculate marginal return moments.

**Limit:** No search-family DSR/PBO, dependence-aware uncertainty or automatic multiplicity gate was located in these surfaces. Native parameter sweep availability alone is not statistical evidence after selection.

**Executable sources:** [backtrader/cerebro.py:892–906](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L892-L906); [backtrader/analyzers/sharpe.py:182–202](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/analyzers/sharpe.py#L182-L202)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Parameter/analyzer result comparability

Native optimized results retain parameters and analyzers; TimeReturn emits dated period returns under explicit NAV/fund/data modes.

**Limit:** No canonical code/data-byte/environment equality gate was located in these paths. Shared comparison must align timeframe, capital flows, fund mode, execution mode and analyzer configuration.

**Executable sources:** [backtrader/cerebro.py:1333–1338](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1333-L1338); [backtrader/analyzers/timereturn.py:96–141](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/analyzers/timereturn.py#L96-L141)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Protected final holdout protocol

Native parameter enumeration runs configured feeds and returns their results.

**Limit:** No reserve/freeze/first-access final holdout mechanism was located in this API. That research capability needs a separate adapter; it is outside a raw execution-engine claim.

**Executable sources:** [backtrader/cerebro.py:1127–1163](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1127-L1163)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Economic external validity and benchmark semantics

A TimeReturn analyzer can observe an external data price as a benchmark, and executable regressions retain expected strategy cash/equity.

**Limit:** A price-return benchmark is not automatically cost/exposure matched. No matched held-out experiment here establishes predictive edge or market realism of a particular configured broker/fill path.

**Executable sources:** [backtrader/analyzers/timereturn.py:112–141](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/analyzers/timereturn.py#L112-L141); [tests/test_strategy_optimized.py:125–145](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/tests/test_strategy_optimized.py#L125-L145)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Parameter and engine-mode sensitivity

Cartesian parameter sweeps and native test matrices across preload/runonce/exactbars support local sensitivity and implementation parity checks.

**Limit:** These are optional experiments. The inspected API does not require parameter stability, independently selected regimes, complete seeds or scientific ablations before results are reported.

**Executable sources:** [backtrader/cerebro.py:892–906](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L892-L906); [tests/testcommon.py:73–111](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/tests/testcommon.py#L73-L111); [tests/test_strategy_optimized.py:125–145](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/tests/test_strategy_optimized.py#L125-L145)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native trusted Python strategy/feed/broker; full managed research workflow is a separate layer.

Cerebro runs supplied Python strategy types and broker/feed objects; the selected route is ordinary trusted program execution, not a constrained declarative resolver.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtrader/cerebro.py:1127–1163](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1127-L1163)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** BackBroker execution admission.

The broker checks simulated cash before accepting submitted orders and cancels opening quantity that would make cash negative; commission and fill behavior are configurable Python objects.

**Limit:** The selected cash checks are not a comprehensive finite-value/schema validator for every data feed and numeric route. The reviewed feed/broker path does not establish a hostile-data validation corpus.

**Executable sources:** [backtrader/brokers/bbroker.py:558–583](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L558-L583); [backtrader/brokers/bbroker.py:769–804](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L769-L804)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Cerebro data preload and optimization dispatch.

The optimization worker count is parameterized by maxcpus and inputs are finite; optional preloading stores market data before the run.

**Limit:** No wall-clock or RAM quota for user strategy/feed code is established, and maxcpus=None delegates process count to multiprocessing. A finite input does not bound arbitrary user callbacks.

**Executable sources:** [backtrader/cerebro.py:1127–1163](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1127-L1163)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native Yahoo HTTP feed.

Retry count is bounded, but the inspected Session.get calls omit an explicit timeout and read response text before CSV processing.

**Limit:** This is a route-specific timeout/resource gap. Other feeds, network libraries and broker connectors have separate boundaries; no universal URL or archive claim is made.

**Executable sources:** [backtrader/feeds/yahoo.py:253–340](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/feeds/yahoo.py#L253-L340)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native Cerebro in-memory simulation and returned strategies; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtrader/cerebro.py:1127–1163](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1127-L1163)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native Cerebro in-memory simulation and returned strategies; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtrader/cerebro.py:1127–1163](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1127-L1163)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native Cerebro in-memory simulation and returned strategies; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtrader/cerebro.py:1127–1163](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1127-L1163)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Cerebro multiprocessing optimization branch.

Cerebro uses a multiprocessing Pool and consumes imap results; pool.close is reached after normal iteration.

**Limit:** The inspected branch lacks a pool context manager or finally block around result iteration. A propagated worker/callback exception can skip that normal cleanup; no task deadline or durable-prefix restart was demonstrated.

**Executable sources:** [backtrader/cerebro.py:1147–1163](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1147-L1163)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native trusted strategy-to-order callbacks; full managed research workflow is a separate layer.

A common probability-valued inference/unavailable-signal protocol is outside the selected broker route; strategies determine when to submit orders.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtrader/brokers/bbroker.py:687–719](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L687-L719)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Default market-order chronology and explicit cheat modes.

The ordinary market-order path requires the current data timestamp to exceed order creation; cheat-on-open/cheat-on-close options deliberately alter that rule.

**Limit:** The chronology claim depends on configured modes, feed time semantics and causal strategy calculations. It does not authenticate timestamps or constrain arbitrary preloaded-array access by trusted code.

**Executable sources:** [backtrader/brokers/bbroker.py:224–242](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L224-L242); [backtrader/brokers/bbroker.py:850–870](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L850-L870)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** BackBroker default submission and opening-fill cash checks.

checksubmit defaults true; submitted orders are pseudo-executed against cloned positions and rejected for negative cash. At actual opening, insufficient cash prevents the new position after commission/leverage accounting.

**Limit:** Configured margin, shortcash, commission models and disabled checksubmit change the economic model. This is a simulated broker guarantee under its selected model, not a live broker guarantee.

**Executable sources:** [backtrader/brokers/bbroker.py:224–242](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L224-L242); [backtrader/brokers/bbroker.py:558–583](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L558-L583); [backtrader/brokers/bbroker.py:769–804](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L769-L804)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** OHLC stop fills and optional volume filler.

Stop orders crossing on the opening gap fill at the open; otherwise the stop barrier participates in bar logic. The default filler=None fills the remaining order size; an optional callable can impose volume fills.

**Limit:** Default full fills do not establish observed market capacity, queue priority or counterfactual market impact. Custom filler equivalence must be audited separately.

**Executable sources:** [backtrader/brokers/bbroker.py:687–700](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L687-L700); [backtrader/brokers/bbroker.py:921–944](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/brokers/bbroker.py#L921-L944)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native Cerebro backtest/optimization; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [backtrader/cerebro.py:1127–1163](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/backtrader/cerebro.py#L1127-L1163)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Executable legacy CI at the pinned source revision.

The checked-in Travis configuration runs nosetests across a listed Python matrix.

**Limit:** No active hosted run, supply-chain audit, hash-pinned dependency closure or protected gate was verified. The old source pin and checked-in legacy CI must not be presented as current service assurance.

**Executable sources:** [.travis.yml:1–22](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/.travis.yml#L1-L22)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected broker accounting tests.

Native tests assert stock/futures commission, operation cost, PnL and cash adjustments, providing executable accounting examples.

**Limit:** Those assertions were inspected only. They do not establish malformed-feed fuzzing, worker-kill recovery, every fill model or full mutation coverage.

**Executable sources:** [tests/test_comminfo.py:39–81](https://github.com/mementum/backtrader/blob/b853d7c90b6721476eb5a5ea3135224e33db1f14/tests/test_comminfo.py#L39-L81)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

