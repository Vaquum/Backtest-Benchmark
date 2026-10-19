# vectorbt (public-source edition)

**Frozen source:** [polakowo/vectorbt @ 0875d984fbd66f8305d172980e55ee30a45153e3](https://github.com/polakowo/vectorbt/tree/0875d984fbd66f8305d172980e55ee30a45153e3)

**Observed license label:** Apache-2.0 with Commons Clause 1.0  
**Layer:** Public-source array portfolio and parameter/indicator toolkit

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Native Numba from_signals replay is admitted, including lazy common-output extraction; first/JIT and warm results are separate.

**Academic:** Optional rolling/expanding splits and DSR calculation; input signals, lookahead discipline and complete selection history remain caller-owned.

**Safety:** Detailed native order-domain checks, with native sentinel/rebate/rejection choices; trusted-object serialization is not an authenticated research manifest.

## P01

### Parameter-space construction and retained memory

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** IndicatorFactory parameter product/broadcast

Parameter products and tuple maps are constructed in memory; output columns scale with parameter combinations and input columns.

**Limit:** Measure parameter count, full output width and retained arrays; a single portfolio column is not a parameter-grid memory benchmark.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [vectorbt/indicators/factory.py:1663–1696](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L1663-L1696); [vectorbt/indicators/factory.py:1937–1961](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L1937-L1961)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** IndicatorFactory run_unique and run_raw paths

Optional run_unique deduplicates parameter tuples and maps results back; use_raw reconstructs requested outputs from a prior parameter map.

**Limit:** This is array-work reuse rather than a complete search-family occurrence ledger; accepted-candidate/exhaustion timing unmeasured.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [vectorbt/indicators/factory.py:1687–1698](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L1687-L1698); [vectorbt/indicators/factory.py:1771–1785](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L1771-L1785)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Public from_signals Numba backend, empty per-process JIT cache

The selected compiled primitives use Numba cache=True. Fresh-process first calls include compilation and lazy output materialization; warm calls create new Portfolios.

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
    "first_full_common_ms_median": 17313.420987,
    "first_full_common_ms_min": 16475.353735,
    "first_full_common_ms_max": 17857.866709,
    "launch_to_ready_ms_median": 32.480717,
    "launch_to_first_valid_ms_median": 23180.635691
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "first_full_common_ms_median": 18181.646832,
    "first_full_common_ms_min": 16203.978103,
    "first_full_common_ms_max": 18972.843171,
    "launch_to_ready_ms_median": 29.896648,
    "launch_to_first_valid_ms_median": 23914.300314
  }
]
```

**Executable sources:** [vectorbt/portfolio/nb.py:65–86](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L65-L86); [vectorbt/portfolio/nb.py:1915–1918](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L1915-L1918)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Single native portfolio simulation versus a fitted model-selection campaign

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [vectorbt/portfolio/base.py:2937–2953](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L2937-L2953); [vectorbt/portfolio/dispatch.py:1097–1127](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/dispatch.py#L1097-L1127)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Indicator array reuse versus fold-fitted preprocessing

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [vectorbt/portfolio/base.py:2937–2953](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L2937-L2953); [vectorbt/portfolio/dispatch.py:1097–1127](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/dispatch.py#L1097-L1127)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native Numba indicator kernels and IndicatorFactory wrapper

The admitted source implements MA/dispersion/RSI/stochastic caches and apply functions with compiled loops.

**Limit:** No native-kernel cross-engine comparison was run. The common external SMA signal avoids conflating different warmup/missing-value semantics.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [vectorbt/indicators/nb.py:23–69](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/nb.py#L23-L69); [vectorbt/indicators/nb.py:137–174](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/nb.py#L137-L174)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Native from_signals, Numba backend, common trace extraction

The native portfolio executes signals and native assets/cash/value accessors materialize the common arrays. The benchmark includes these lazy accessors in the full-common timer.

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
    "warm_full_common_ms_median": 61.283693,
    "warm_engine_ms_median": 9.865247,
    "warm_extraction_common_ms_median": 50.016689,
    "warm_full_common_cpu_ms_median": 61.288757,
    "warm_process_medians_ms": [
      49.776272,
      61.283693,
      58.394477,
      77.907897,
      62.044804
    ],
    "warm_process_median_ms_min": 49.776272,
    "warm_process_median_ms_max": 77.907897,
    "warm_evaluation_bars_per_second": 143317.0811034511,
    "relative_to_limen_warm_full_common": 23.67248837788718
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "warm_full_common_ms_median": 58.794726,
    "warm_engine_ms_median": 9.49848,
    "warm_extraction_common_ms_median": 49.722795,
    "warm_full_common_cpu_ms_median": 58.800692,
    "warm_process_medians_ms": [
      53.622057,
      61.117293,
      63.69892,
      58.794726,
      57.030457
    ],
    "warm_process_median_ms_min": 53.622057,
    "warm_process_median_ms_max": 63.69892,
    "warm_evaluation_bars_per_second": 149384.14714272163,
    "relative_to_limen_warm_full_common": 29.280387850537103
  }
]
```

**Executable sources:** [vectorbt/portfolio/base.py:2937–2953](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L2937-L2953); [vectorbt/portfolio/dispatch.py:1097–1127](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/dispatch.py#L1097-L1127); [vectorbt/portfolio/base.py:4332–4347](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L4332-L4347); [vectorbt/portfolio/base.py:4546–4580](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L4546-L4580)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** OHLC portfolio simulation versus exchange queue/event-ledger forward labels

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [vectorbt/portfolio/base.py:2937–2953](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L2937-L2953); [vectorbt/portfolio/dispatch.py:1097–1127](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/dispatch.py#L1097-L1127)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Portfolio arrays, records, JIT/runtime and full common outputs

Parameter/input broadcast and cached output arrays create memory beyond the source close series.

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
    "peak_rss_bytes_median": 522354688
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "peak_rss_bytes_median": 522244096
  }
]
```

**Executable sources:** [vectorbt/indicators/factory.py:1663–1696](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L1663-L1696); [vectorbt/portfolio/base.py:4446–4485](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L4446-L4485)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** IndicatorFactory Python/Numba loop and optional Ray path

The factory exposes Numba-loop execution and a separate optional Ray concatenation path.

**Limit:** No claim that the selected single-column Numba portfolio uses Ray or parallel speedup; no worker-count sweep.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [vectorbt/indicators/factory.py:3317–3326](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L3317-L3326); [vectorbt/base/combine_fns.py:269–283](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/base/combine_fns.py#L269-L283)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Indicator raw/cache reuse and cached portfolio accessors

Indicator cache_func/use_cache reuse and cached assets/cash/value methods are distinct mechanisms; fresh Portfolios prevent reusing old simulation output in timings.

**Limit:** Cache invalidation, retained-byte ceilings and cross-run fitted state equivalence are not measured.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [vectorbt/indicators/factory.py:3368–3389](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L3368-L3389); [vectorbt/portfolio/base.py:4332–4347](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L4332-L4347); [vectorbt/portfolio/base.py:4546–4580](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/base.py#L4546-L4580)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Pickleable persistence of native objects

Public save/load serializes complete Python objects.

**Limit:** Serialization is not a demonstrated atomic multi-round checkpoint/resume frontier. Recording latency and recovery were not measured.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [vectorbt/utils/config.py:229–254](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/utils/config.py#L229-L254)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native signal simulation and MA implementation

Signal simulation passes the current row/column context and native entry/exit adapters select signals at that index. The inspected MA path uses rolling/exponential history.

**Limit:** The engine accepts batch arrays/custom functions and does not establish how input signals were produced. Predictor prefix invariance and execution lag belong to the signal contract; no general native causality proof follows from vectorization.

**Executable sources:** [vectorbt/portfolio/nb.py:2696–2706](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L2696-L2706); [vectorbt/portfolio/nb.py:2943–2973](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L2943-L2973); [vectorbt/indicators/nb.py:23–28](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/nb.py#L23-L28)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Managed estimator train/evaluation isolation

Range/rolling/expanding splitters produce index sets, while the signal simulation consumes supplied arrays. No automatic estimator fit/evaluate owner was located in these inspected surfaces.

**Limit:** Split helpers alone do not keep feature fitting or tuning inside training. An ML adapter must enforce fit ownership; the fixed-signal execution track is not a model-training test.

**Executable sources:** [vectorbt/generic/splitters.py:81–103](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/generic/splitters.py#L81-L103); [vectorbt/portfolio/nb.py:2943–2973](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L2943-L2973)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Forward label utilities

Fixed labels explicitly compute future relative returns using a backward shift; future mean labels reverse the series and use full-window rolling then shift.

**Limit:** These are intended target generators, not causal predictors. No availability-time metadata or automatic censoring at train/evaluation boundaries was located in these label/split helpers; create targets within the admitted horizon or purge externally.

**Executable sources:** [vectorbt/labels/nb.py:26–34](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/labels/nb.py#L26-L34); [vectorbt/labels/nb.py:78–84](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/labels/nb.py#L78-L84); [vectorbt/generic/splitters.py:95–103](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/generic/splitters.py#L95-L103)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native index splitters

RollingSplitter builds moving windows, ExpandingSplitter anchors starts at zero, and range sets have configurable lengths with empty/oversized-set checks.

**Limit:** The inspected splitters cut by position, not event-end availability. They do not automatically purge label overlap, embargo folds or orchestrate nested fitting. Window overlap must not be counted as independent observations.

**Executable sources:** [vectorbt/generic/splitters.py:81–103](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/generic/splitters.py#L81-L103); [vectorbt/generic/splitters.py:213–239](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/generic/splitters.py#L213-L239); [vectorbt/generic/splitters.py:255–275](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/generic/splitters.py#L255-L275)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Fold-local fitted transforms/stacking

The inspected indicator factory constructs parameter products and outputs; splitters expose indices rather than an estimator pipeline.

**Limit:** No managed fold-local fitted transform/OOF stacking contract was located here. Compare that capability through an explicit ML adapter, not raw simulation speed.

**Executable sources:** [vectorbt/indicators/factory.py:3045–3064](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L3045-L3064); [vectorbt/generic/splitters.py:95–103](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/generic/splitters.py#L95-L103)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Probability calibration and nested threshold selection

The native signal adapter reads supplied entry/exit booleans; parameter combinations can be generated by the indicator factory.

**Limit:** Calibration and threshold-fit validation were not located in these execution/research primitives. A model adapter must supply their disjoint fit/evaluation protocol.

**Executable sources:** [vectorbt/portfolio/nb.py:2943–2973](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L2943-L2973); [vectorbt/indicators/factory.py:3057–3064](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L3057-L3064)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native return metric definitions

Sharpe uses per-observation risk-free adjustment, nan-aware mean/std with configurable ddof and annualization from year frequency divided by data frequency. It returns NaN for fewer than two rows and infinity for zero standard deviation.

**Limit:** NaN support, risk-free units, frequency, period count and zero-variance behavior must be normalized across candidates. A native ratio with the same label need not equal another framework's ratio.

**Executable sources:** [vectorbt/returns/nb.py:411–421](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/returns/nb.py#L411-L421); [vectorbt/returns/accessors.py:279–289](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/returns/accessors.py#L279-L289)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected numeric regression and formula tests

Tests assert fixed Sharpe/rolling Sharpe results and DSR values, including an explicit moment-formula calculation over incomplete return arrays.

**Limit:** Tests were inspected, not executed in this academic audit. The DSR formula comparison reuses the same expected-maximum helper and does not independently validate statistical assumptions or all execution paths.

**Executable sources:** [tests/test_returns.py:435–473](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/tests/test_returns.py#L435-L473); [tests/test_returns.py:476–490](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/tests/test_returns.py#L476-L490)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Managed model-fit convergence

Native parameter products and signal execution do not perform a managed statistical estimator fit in the inspected paths.

**Limit:** Model convergence/conditioning belongs to an added estimator adapter. Completion of a compiled array simulation is not evidence of model fit stability.

**Executable sources:** [vectorbt/indicators/factory.py:3057–3064](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L3057-L3064); [vectorbt/portfolio/nb.py:2696–2706](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L2696-L2706)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Parameter-column family accounting

Parameter products preserve parameter combinations and DSR can infer trial count from current columns or accept an explicit value.

**Limit:** Column count is not a complete search ledger: discarded, failed, manually tried or previous-run candidates are not recovered. The family and effective trial count remain caller responsibilities.

**Executable sources:** [vectorbt/indicators/factory.py:3057–3064](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L3057-L3064); [vectorbt/returns/accessors.py:684–694](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/returns/accessors.py#L684-L694)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native deflated Sharpe diagnostic

DSR uses an expected-maximum Sharpe threshold based on trial count/variance and a skew/kurtosis-adjusted normal-CDF statistic. Annualized inputs are converted back to per-period values.

**Limit:** The helper is diagnostic, not automatic candidate admission. Default current-column count and variance do not establish the true search family/effective independent trials, and the inspected formula contains no serial-covariance correction.

**Executable sources:** [vectorbt/returns/metrics.py:12–38](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/returns/metrics.py#L12-L38); [vectorbt/returns/accessors.py:684–696](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/returns/accessors.py#L684-L696)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Indexed parameter arrays and saved objects

Split arrays and parameter-labelled combinations retain local evaluation structure; pickle-based object persistence is available.

**Limit:** Object persistence does not establish canonical input-byte, source-revision, environment or benchmark-contract equivalence. Cross-run evidence acceptance needs an external manifest and common return/fill schema.

**Executable sources:** [vectorbt/generic/splitters.py:95–103](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/generic/splitters.py#L95-L103); [vectorbt/indicators/factory.py:3045–3064](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L3045-L3064); [vectorbt/utils/config.py:231–251](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/utils/config.py#L231-L251)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Protected final holdout admission

Index splitters can create held-out ranges, but the inspected primitives do not own model selection or reserve final data access.

**Limit:** A held-out index set is not a frozen single-use holdout protocol. For platform comparison supply an adapter; for fixed-signal simulation this criterion is outside native scope.

**Executable sources:** [vectorbt/generic/splitters.py:81–103](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/generic/splitters.py#L81-L103)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Economic and predictive external validity

Native metrics and parameterized simulations can evaluate supplied paths and benchmark returns.

**Limit:** No matched cross-solution holdout experiment here establishes model edge or real fill validity. Signal production, universe/data revisions and execution assumptions remain material external inputs.

**Executable sources:** [vectorbt/returns/nb.py:411–421](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/returns/nb.py#L411-L421); [vectorbt/portfolio/nb.py:2943–2973](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L2943-L2973)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Parameter and temporal sensitivity primitives

Parameter Cartesian products, rolling/expanding windows and direct DSR arguments support repeatable sensitivity sweeps.

**Limit:** These are optional building blocks; the inspected code does not require ablations, seed sweeps, parameter plateau checks or independent regime replication before a result is accepted.

**Executable sources:** [vectorbt/indicators/factory.py:3057–3064](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/indicators/factory.py#L3057-L3064); [vectorbt/generic/splitters.py:213–239](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/generic/splitters.py#L213-L239); [vectorbt/generic/splitters.py:255–275](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/generic/splitters.py#L255-L275); [vectorbt/returns/accessors.py:684–696](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/returns/accessors.py#L684-L696)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Trusted portfolio/configuration serialization and callable extensions.

Config persistence loads Python pickle/dill objects and portfolio execution supports trusted callbacks. Loading such files is an executable-object trust decision.

**Limit:** No constrained hostile-pickle sandbox is established. This is a local serialization API, not evidence of an unauthenticated remote execution path. The reviewed edition is public source with a Commons Clause restriction, not unrestricted OSS.

**Executable sources:** [vectorbt/utils/config.py:231–277](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/utils/config.py#L231-L277)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Numba execute_order numeric contract; matching Rust checks inspected separately.

The core order kernel rejects invalid state, nonpositive/nonfinite execution price, nonfinite fees and negative/nonfinite slippage, bad granularity and out-of-range rejection probability. NaN order size/price deliberately returns an ignored status; selected infinity sentinels have explicit semantics.

**Limit:** This is a typed numerical kernel contract, not global DataFrame chronology/OHLC validation. Explicit fee rebates and infinity sentinels are valid model inputs. Full Numba/Rust behavioral equivalence was not established by this safety review.

**Executable sources:** [vectorbt/portfolio/nb.py:343–443](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L343-L443); [rust/src/portfolio.rs:1153–1233](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/rust/src/portfolio.rs#L1153-L1233); [vectorbt/portfolio/dispatch.py:60–109](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/dispatch.py#L60-L109)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Finite-shaped portfolio arrays and record capacity.

Native simulation checks order/log record capacities and raises when preallocated record arrays are exhausted. Array dimensions determine the main simulation work.

**Limit:** A shape-bounded loop is not an admission quota for huge broadcasts or a wall-clock limit for trusted callbacks/JIT compilation. No process-wide RAM or runtime ceiling was established.

**Executable sources:** [vectorbt/portfolio/nb.py:648–709](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L648-L709); [vectorbt/portfolio/dispatch.py:555–624](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/dispatch.py#L555-L624)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native already-loaded portfolio arrays; full managed research workflow is a separate layer.

The selected portfolio simulation accepts arrays. Data connector fetching and local serialized-file trust are separate ingestion surfaces, which require their own source/timeout policy.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [vectorbt/portfolio/dispatch.py:555–624](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/dispatch.py#L555-L624)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native portfolio/config result serialization; full managed research workflow is a separate layer.

Config/result object serialization is not a content-addressed managed study manifest. A content-identity adapter is required for the complete research contract.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [vectorbt/utils/config.py:231–277](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/utils/config.py#L231-L277)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**Partial** · Inspected · applicability `adapter_required` · capability `implemented`

**Scope:** Native serialized config/result object loading.

Serialized objects are read and decoded with pickle/dill; decoding errors can propagate, but the inspected loader does not bind bytes to an expected digest or external research-round references.

**Limit:** Trusted object files can carry executable code. Decode success is neither authenticated provenance nor content identity; the Limen managed-round schema needs a separate adapter.

**Executable sources:** [vectorbt/utils/config.py:231–277](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/utils/config.py#L231-L277)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**Partial** · Inspected · applicability `adapter_required` · capability `implemented`

**Scope:** Native object save path.

The inspected save method writes serialized bytes directly to a supplied file; its corresponding load reads that file.

**Limit:** No multi-artifact transaction, atomic replacement, fsync frontier or completed-experiment restart protocol is established by this path. This does not claim every external storage adapter behaves identically.

**Executable sources:** [vectorbt/utils/config.py:231–251](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/utils/config.py#L231-L251)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native array simulation engine dispatch; full managed research workflow is a separate layer.

Vectorized array execution/Numba-or-Rust dispatch is not a managed multiworker experiment executor. Worker death and durable-prefix recovery require a separately audited executor.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [vectorbt/portfolio/dispatch.py:555–624](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/dispatch.py#L555-L624)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Numba order status and unavailable numerical inputs.

NaN order size/price is explicitly ignored; invalid state and finite-value contract violations raise. Rejected orders raise only when raise_reject is enabled, otherwise status information is returned.

**Limit:** There is no inferred probability bound for arbitrary research signals. Callers must inspect rejection/ignored statuses and decide whether unavailable input means no order, failed run or stale prior intent.

**Executable sources:** [vectorbt/portfolio/nb.py:378–443](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L378-L443); [vectorbt/portfolio/nb.py:648–709](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L648-L709)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Array-supplied prices, signals and valuation timing.

Simulation consumes caller-supplied arrays and resolves signal/stop behavior at each array row. Data preparation may fill missing OHLC components from other prices.

**Limit:** The array API does not establish source availability timestamps or automatically delay every close-derived signal to the next open. Comparisons must explicitly align price, signal and valuation rows; trusted callbacks may use future arrays.

**Executable sources:** [vectorbt/portfolio/nb.py:2076–2135](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L2076-L2135); [vectorbt/portfolio/dispatch.py:555–624](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/dispatch.py#L555-L624)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Numba buy/sell affordability, cash sharing and short-cash locking.

Buy sizing accounts for fees, slippage, minimums, granularity and available cash, with optional partial fills. Short-side free-cash constraints depend on lock_cash, which defaults false in the public dispatch.

**Limit:** Unrestricted short cash, shared cash and explicit rebates are selectable economics, not universal cash-only margin rules. Compare identical settings and record rejected/partial orders before comparing returns.

**Executable sources:** [vectorbt/portfolio/nb.py:72–213](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L72-L213); [vectorbt/portfolio/dispatch.py:60–74](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/dispatch.py#L60-L74); [rust/src/portfolio.rs:969–1013](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/rust/src/portfolio.rs#L969-L1013)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Numba OHLC stops and intrabar assumptions.

Stop-price logic uses the opening price for qualifying gaps; the signal simulation checks stop loss before take profit. Missing open/high/low may be inferred from close and available endpoints.

**Limit:** This creates explicit bar-model assumptions, not observed intrabar ordering, queue priority or endogenous market impact. Rust parity beyond the inspected numerical guards remains outside this row.

**Executable sources:** [vectorbt/portfolio/nb.py:1861–1889](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L1861-L1889); [vectorbt/portfolio/nb.py:2076–2135](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/nb.py#L2076-L2135)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native portfolio array simulation; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [vectorbt/portfolio/dispatch.py:555–624](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/vectorbt/portfolio/dispatch.py#L555-L624)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Pinned source CI including the optional Rust engine.

CI installs editable test dependencies and runs pytest across OS/Python matrices; a Rust job builds the local Rust extension and also runs tests.

**Limit:** Actions and toolchains use moving tags/stable in this workflow; a locked release dependency identity and hosted gate outcome were not verified. Public-source eligibility does not remove its license restriction.

**Executable sources:** [.github/workflows/tests.yml:13–78](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/.github/workflows/tests.yml#L13-L78)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Numerical rejection and state assertions in native tests.

Tests explicitly exercise NaN/infinite state, infinite prices/fees, invalid slippage and rejection-probability boundaries.

**Limit:** These test bodies were inspected only. Test inventory is not proof of comprehensive malformed-file, concurrency, Rust/Numba parity or mutation coverage.

**Executable sources:** [tests/test_portfolio.py:172–269](https://github.com/polakowo/vectorbt/blob/0875d984fbd66f8305d172980e55ee30a45153e3/tests/test_portfolio.py#L172-L269)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

