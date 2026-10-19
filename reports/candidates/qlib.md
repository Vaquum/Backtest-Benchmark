# Qlib

**Frozen source:** [microsoft/qlib @ 54355232463878d2eebb91fe0ee5fa7fa1f5976c](https://github.com/microsoft/qlib/tree/54355232463878d2eebb91fe0ee5fa7fa1f5976c)

**Observed license label:** MIT  
**Layer:** Model/dataset/task research platform; exchange/position components measured

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Native Exchange/Position replay passes the common trace contract; full executor, provider, training and recorder throughput are unmeasured.

**Academic:** Train-bounded processors, segmented datasets and horizon-aware rolling tasks make it a close research-workflow comparator; static and rolling paths have different leakage guards.

**Safety:** Native guarded paths coexist with trusted configuration/artifacts; AsyncCaller was reproduced returning normally after worker failure and leaving later work unexecuted.

## P01

### Parameter-space construction and retained memory

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native rolling research task generation

The rolling task generator constructs task definitions with temporal windows rather than a finite Cartesian parameter-grid engine.

**Limit:** A task-list construction benchmark must freeze windows, model families and retained artifacts, not compare raw task count with an execution-only engine.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qlib/workflow/task/gen.py:146–189](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/gen.py#L146-L189); [qlib/workflow/task/gen.py:230–261](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/gen.py#L230-L261)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Task generation and Trainer task consumption

TrainerR accepts task lists and traverses them in order, recording returned models/recorders.

**Limit:** No matched parameter novelty/exhaustion benchmark; a temporal task is not interchangeable with a hyperparameter candidate.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qlib/model/trainer.py:254–285](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/model/trainer.py#L254-L285)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Native Exchange/Position component replay with a recorded quote provider

The adapter directly loads recorded quotes, then calls native order/account code. It excludes the normal data provider, full executor and research recorders.

**Limit:** First-call figures belong to the declared public API/component scope. Process-launch-to-first-valid includes identity, imports, data, oracle and validation, not just engine startup. No full trained research campaign or fleet-level latency guarantee.

**Measurement state:** Measured for the linked finite single-host replay campaign; broader criterion scopes remain unmeasured

**Recorded measurements:**

```json
[
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "buy_and_hold",
    "rank_against_full_engine": false,
    "independent_processes": 5,
    "first_full_common_ms_median": 61.752982,
    "first_full_common_ms_min": 58.693234,
    "first_full_common_ms_max": 71.42795,
    "launch_to_ready_ms_median": 32.626199,
    "launch_to_first_valid_ms_median": 1413.847189
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": false,
    "independent_processes": 5,
    "first_full_common_ms_median": 61.872404,
    "first_full_common_ms_min": 58.296415,
    "first_full_common_ms_max": 78.529785,
    "launch_to_ready_ms_median": 33.444712,
    "launch_to_first_valid_ms_median": 1520.437773
  }
]
```

**Executable sources:** [qlib/backtest/exchange.py:421–464](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L421-L464); [qlib/backtest/position.py:342–420](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/position.py#L342-L420)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native task/dataset/model/recorder workflow

TrainerR executes tasks serially, can isolate training in a subprocess, and tags recorders; TrainerRM offers task-manager workers.

**Limit:** The recorded Exchange/Position replay is not the complete Qlib research workflow. No common fitted campaign was timed.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qlib/model/trainer.py:254–305](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/model/trainer.py#L254-L305); [qlib/model/trainer.py:481–509](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/model/trainer.py#L481-L509)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**Partial** · Inspected · applicability `native` · capability `unknown`

**Scope:** Fitted preparation/prediction reuse, distinguished from adjacent raw or deterministic computation reuse

Qlib research tasks contain dataset/model processing; execution quote caching is a separate mechanism.

**Limit:** The cited adjacent data/processing mechanism does not establish a fitted-state or prediction-reuse cache. No fold-fitted preparation reuse ablation on a fixed matched family; native availability is not evidence of speedup or leakage resistance.

**Measurement state:** Not measured in this criterion scope

**Distinct sub-capabilities:** fitted_state_or_prediction_reuse_in_inspected_path: Unknown; no fitted-reuse speedup inferred; adjacent_input_or_deterministic_reuse: Implemented as described in finding; not the canonical fitted capability

**Executable sources:** [qlib/model/trainer.py:254–285](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/model/trainer.py#L254-L285); [qlib/data/dataset/handler.py:480–546](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/dataset/handler.py#L480-L546)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native compiled rolling feature kernels and Python expression wrapper

Native Cython rolling mean and slope kernels loop over the supplied series; the expression layer invokes the compiled rolling-slope path.

**Limit:** No full-array semantic parity or native-kernel throughput comparison was executed. The component replay times quote/account processing, not native feature generation.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qlib/data/_libs/rolling.pyx:34–46](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/_libs/rolling.pyx#L34-L46); [qlib/data/_libs/rolling.pyx:64–88](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/_libs/rolling.pyx#L64-L88); [qlib/data/_libs/rolling.pyx:183–207](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/_libs/rolling.pyx#L183-L207); [qlib/data/ops.py:1248–1253](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/ops.py#L1248-L1253)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Native Exchange and Position components; explicit hourly replay driver

The adapter calls native deal_order and actual Position account updates using unchanged recorded quotes and declared fee/slippage inputs.

**Limit:** One recorded single-instrument zero-cost contract and two fixed signals. Native APIs perform different extra work. Components and internal kernels cannot receive full-engine ratios; costs, data-size scaling, native indicators and other markets require separate campaigns.

**Measurement state:** Measured for the linked finite single-host replay campaign; broader criterion scopes remain unmeasured

**Recorded measurements:**

```json
[
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "buy_and_hold",
    "rank_against_full_engine": false,
    "independent_processes": 5,
    "warm_full_common_ms_median": 60.783126,
    "warm_engine_ms_median": 60.607561,
    "warm_extraction_common_ms_median": 0.186502,
    "warm_full_common_cpu_ms_median": 60.786154,
    "warm_process_medians_ms": [
      57.411377,
      60.783126,
      75.14089,
      56.489655,
      61.997786
    ],
    "warm_process_median_ms_min": 56.489655,
    "warm_process_median_ms_max": 75.14089,
    "warm_evaluation_bars_per_second": 144497.33960704817,
    "relative_to_limen_warm_full_common": null
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": false,
    "independent_processes": 5,
    "warm_full_common_ms_median": 61.008531,
    "warm_engine_ms_median": 60.832795,
    "warm_extraction_common_ms_median": 0.184138,
    "warm_full_common_cpu_ms_median": 61.010809,
    "warm_process_medians_ms": [
      66.579911,
      61.008531,
      60.506724,
      63.660226,
      57.514796
    ],
    "warm_process_median_ms_min": 57.514796,
    "warm_process_median_ms_max": 66.579911,
    "warm_evaluation_bars_per_second": 143963.4729116818,
    "relative_to_limen_warm_full_common": null
  }
]
```

**Executable sources:** [qlib/backtest/exchange.py:421–464](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L421-L464); [qlib/backtest/position.py:342–420](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/position.py#L342-L420)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native exchange deal/position account components versus complete nested executor

Native order processing and position updates are exercised at recorded bar closes.

**Limit:** Execution/timer/nested frequency and multi-asset event scaling are not measured by the component driver.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qlib/backtest/exchange.py:421–464](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L421-L464); [qlib/backtest/position.py:342–420](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/position.py#L342-L420)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Native quote arrays, Position and component replay output

NumpyQuote retains grouped instrument arrays and a bounded entry-count lru_cache for quote lookup.

**Limit:** Process high-water RSS includes imported dependencies, compilation and earlier calls; it is not incremental engine memory, process-tree PSS or a hard resource bound. Multi-asset/grid/parallel memory scaling remains unmeasured.

**Measurement state:** Measured for the linked finite single-host replay campaign; broader criterion scopes remain unmeasured

**Recorded measurements:**

```json
[
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "buy_and_hold",
    "rank_against_full_engine": false,
    "independent_processes": 5,
    "peak_rss_bytes_median": 230035456
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": false,
    "independent_processes": 5,
    "peak_rss_bytes_median": 213544960
  }
]
```

**Executable sources:** [qlib/backtest/high_performance_ds.py:136–181](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/high_performance_ds.py#L136-L181)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Serial TrainerR and task-manager TrainerRM workers

TrainerR loops task lists, optionally in separate subprocesses; TrainerRM provides worker execution against a task manager.

**Limit:** No worker-count sweep, process-tree memory or identical fitted-result campaign; component replay is single-process.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qlib/model/trainer.py:254–285](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/model/trainer.py#L254-L285); [qlib/model/trainer.py:481–509](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/model/trainer.py#L481-L509)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** NumpyQuote indexed arrays and lru_cache(maxsize=512)

Native quote lookup caches stock/time/field requests, with separate single-value and interval paths.

**Limit:** Entry-count limit is not a byte limit; cache hit costs, eviction and source-update correctness have not been measured.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qlib/backtest/high_performance_ds.py:136–203](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/high_performance_ds.py#L136-L203)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native workflow recorders and queued asynchronous callbacks

The native workflow has recorders and an asynchronous call queue; the bounded callback probe demonstrates silent propagation failure after a queued callback raises.

**Limit:** No end-to-end checkpoint latency/recovery campaign. The callback reproduction does not establish that every recorder path loses results.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qlib/utils/paral.py:93–116](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/paral.py#L93-L116); [qlib/workflow/recorder.py:360–405](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L360-L405)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Alpha158 feature expressions and native signal strategies

Expression engine explicitly supports positive and negative Ref offsets. Native TopkDropout and WeightStrategy query the previous trade-calendar step for their prediction signal. This is real execution-lag control.

**Limit:** Arbitrary expressions/signals are trusted; a negative Ref in a predictor can consume future data. No universal prefix-invariance enforcement is present in these paths.

**Executable sources:** [qlib/data/ops.py:800–824](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/ops.py#L800-L824); [qlib/contrib/strategy/signal_strategy.py:137–145](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/strategy/signal_strategy.py#L137-L145); [qlib/contrib/data/loader.py:102–110](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/data/loader.py#L102-L110)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** DatasetH, DataHandlerLP and LGBModel fitting

LGBModel obtains only named train/valid segments for fitting and uses the infer feature view for test prediction. Built-in learned normalizers restrict fit observations to explicitly supplied dates.

**Limit:** DataHandler prepares whole requested data before segment fetch; arbitrary processors receive full frames, and fit bounds are supplied separately from dataset segments. Matching bounds and callback information use remain caller obligations.

**Executable sources:** [qlib/contrib/model/gbdt.py:34–54](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/model/gbdt.py#L34-L54); [qlib/contrib/model/gbdt.py:93–97](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/model/gbdt.py#L93-L97); [qlib/data/dataset/processor.py:231–258](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/dataset/processor.py#L231-L258); [qlib/data/dataset/handler.py:529–539](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/dataset/handler.py#L529-L539)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Alpha158 forward labels and configured static versus rolling workflows

Alpha158 label is Ref(close,-2)/Ref(close,-1)-1. Raw labels are prepared for the handler range, then DatasetH selects date segments; the shipped static LightGBM YAML has contiguous train/valid/test periods. Rolling wrapper explicitly truncates non-test support by horizon+1.

**Limit:** Static segment slicing does not itself censor labels at each segment end; boundary-label completion can cross into the next segment. This is inspected control flow, not an executed leakage-rate estimate. Properly configured truncation is a distinct protected path.

**Executable sources:** [qlib/contrib/data/handler.py:151–152](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/data/handler.py#L151-L152); [qlib/data/dataset/handler.py:190–194](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/dataset/handler.py#L190-L194); [qlib/data/dataset/__init__.py:171–183](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/dataset/__init__.py#L171-L183); [examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml:49–56](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml#L49-L56); [qlib/contrib/rolling/base.py:194–199](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/rolling/base.py#L194-L199)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** RollingGen and MultiHorizonGen temporal task construction

Expanding/sliding generators shift named segments and deepcopy task configurations. Configured trunc_days removes non-test support near test start; MultiHorizonGen uses horizon+label_leak_n.

**Limit:** Direct RollingGen defaults trunc_days to None. The helper is not automatically applied to all DatasetH tasks, and dates alone do not prove target availability.

**Executable sources:** [qlib/workflow/task/gen.py:128–154](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/gen.py#L128-L154); [qlib/workflow/task/gen.py:205–228](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/gen.py#L205-L228); [qlib/workflow/task/gen.py:288–299](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/gen.py#L288-L299); [qlib/workflow/task/gen.py:340–350](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/gen.py#L340-L350)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Learned processors across rolling tasks

Normalizers fit inside explicit date bounds; processor fit/transform pipelines and task deep copies are implemented.

**Limit:** Rolling handler modification extends its load end date; it does not universally derive new processor fit bounds from every training segment. Rolling also supports a shared cached handler. Independent fold-local fitting must be checked for the selected configuration.

**Executable sources:** [qlib/data/dataset/processor.py:238–258](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/dataset/processor.py#L238-L258); [qlib/data/dataset/handler.py:529–539](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/dataset/handler.py#L529-L539); [qlib/workflow/task/gen.py:109–125](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/gen.py#L109-L125); [qlib/contrib/rolling/base.py:163–176](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/rolling/base.py#L163-L176)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** LGBModel validation selection and native signal analysis

Training can use validation observations for LightGBM early stopping, and test prediction is a separate operation. Native signal records preserve predictions and test labels.

**Limit:** A general probability-calibration/threshold-fitting pipeline with independent calibration assessment was not located in these inspected model/record paths. Regression rank signals are not implicitly calibrated probabilities.

**Executable sources:** [qlib/contrib/model/gbdt.py:69–97](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/model/gbdt.py#L69-L97); [qlib/workflow/record_temp.py:197–213](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/record_temp.py#L197-L213)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** risk_analysis and portfolio analysis records

Risk analysis supports sum and product accumulation; default sum annualizes arithmetic mean and computes drawdown on cumulative summed returns. Native portfolio records analyze excess returns with and without cost.

**Limit:** Default daily scaler is238, not a universal252/365 convention. Product mode uses geometric per-period mean with log-return standard deviation. Match accumulation, baseline, cost and annualization before comparing metric names.

**Executable sources:** [qlib/contrib/evaluate.py:26–26](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/evaluate.py#L26-L26); [qlib/contrib/evaluate.py:49–90](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/evaluate.py#L49-L90); [qlib/workflow/record_temp.py:512–524](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/record_temp.py#L512-L524)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Processor, temporal sampler and order-fill assertions

Tests contain alternate normalization calculations, temporal-sampler alignment assertions and explicit fill-ratio expectations.

**Limit:** These assertions were inspected, not executed in this comparative sub-audit. No universal independent numerical oracle or empirical calibration result follows from their presence.

**Executable sources:** [tests/data_mid_layer_tests/test_processor.py:14–54](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/tests/data_mid_layer_tests/test_processor.py#L14-L54); [tests/data_mid_layer_tests/test_dataset.py:120–124](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/tests/data_mid_layer_tests/test_dataset.py#L120-L124); [tests/backtest/test_file_strategy.py:112–117](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/tests/backtest/test_file_strategy.py#L112-L117)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** LGBModel optimization history and failure semantics

LightGBM early stopping and per-iteration train/validation metric logging are implemented. Fit raises on missing/empty/multilabel data outside its supported contract.

**Limit:** Stopping on validation is model selection, not proof of numerical convergence or seed stability. Backend optimization mathematics remain delegated; no package-wide convergence admission policy was established.

**Executable sources:** [qlib/contrib/model/gbdt.py:34–53](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/model/gbdt.py#L34-L53); [qlib/contrib/model/gbdt.py:69–91](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/model/gbdt.py#L69-L91)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** MLflow recorder and rolling experiment inventory

Recorder has running/finished/failed states, run IDs, parameters, artifacts and end-run status. Rolling orchestrates a supplied task list.

**Limit:** This is retained experiment history, not a complete global search ledger. Rolling can delete the previous named experiment before retraining; externally attempted or selectively supplied searches remain unknown.

**Executable sources:** [qlib/workflow/recorder.py:345–370](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L345-L370); [qlib/workflow/recorder.py:390–405](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L390-L405); [qlib/contrib/rolling/base.py:206–216](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/rolling/base.py#L206-L216)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Unknown** · Inspected · applicability `native` · capability `not_located`

**Scope:** Selection-adjusted inference in inspected evaluation and record paths

Inspected risk and portfolio analysis calculate return/volatility, information ratio, drawdown and benchmark-relative statistics. No DSR/PBO or full-family adaptive-selection adjustment was located in these paths or the bounded package search.

**Limit:** Not located is not a proof of repository-wide absence. Reported performance and IC diagnostics do not alone establish dependence-aware inferential validity.

**Executable sources:** [qlib/contrib/evaluate.py:65–90](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/evaluate.py#L65-L90); [qlib/workflow/record_temp.py:512–526](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/record_temp.py#L512-L526)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Experiment provenance and emitted prediction/portfolio artifacts

MLflow recorder logs invocation, selected environment variables and Git working-state outputs; signal/portfolio records retain indexed predictions, labels, returns and positions. A focused native AsyncCaller probe also reproduced that a worker callback exception can let wait return normally while later queued work never runs.

**Limit:** No Limen-style exact cross-family sample/execution compatibility admission was established in these record paths. Immutable input bytes and model/dependency identities must be supplied by the benchmark adapter. Only AsyncCaller was executed in that probe; implications for MLflowRecorder completion/artifact persistence follow from inspected decorator/wait wiring, not an executed recorder failure.

**Executable sources:** [qlib/workflow/recorder.py:364–386](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L364-L386); [qlib/workflow/record_temp.py:197–213](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/record_temp.py#L197-L213); [qlib/workflow/record_temp.py:493–504](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/record_temp.py#L493-L504); [qlib/utils/paral.py:84–116](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/paral.py#L84-L116); [qlib/workflow/recorder.py:390–405](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L390-L405); [qlib/workflow/recorder.py:490–506](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L490-L506)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**Unknown** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Protected final-holdout admission versus named test segment

LGBModel predicts a named test segment and SignalRecord saves test labels; recorder allocates an ordinary experiment run. No protected data reservation, frozen-selection-before-access gate or exposure-attempt ledger was located in these paths.

**Limit:** Named test data and experiment tracking are useful but do not by themselves protect an untouched final assessment. A separate benchmark-owned holdout protocol is required for that claim.

**Executable sources:** [qlib/contrib/model/gbdt.py:93–97](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/model/gbdt.py#L93-L97); [qlib/workflow/record_temp.py:179–213](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/record_temp.py#L179-L213); [qlib/workflow/recorder.py:345–370](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L345-L370)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Executable Alpha158 LightGBM strategy and benchmark configuration

A concrete LightGBM/Alpha158 workflow supplies dates, market, benchmark, top-k strategy, account and transaction costs, enabling reproducible candidate specification.

**Limit:** No equal-budget cross-solution or untouched cross-market quality experiment was executed here. Executable benchmark configuration and recorded examples do not establish an edge.

**Executable sources:** [examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml:1–30](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml#L1-L30); [examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml:31–71](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml#L31-L71)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Rolling sensitivity and reconstruction artifacts

Task generators parameterize horizons and rolling windows; recorder saves parameters, working-tree evidence and serialized artifacts.

**Limit:** These mechanisms do not prove stable outcomes across costs, seeds, dates or features. Optional cached handlers, backend seeds and provider data must be frozen to reconstruct the same experiment.

**Executable sources:** [qlib/workflow/task/gen.py:340–350](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/gen.py#L340-L350); [qlib/workflow/recorder.py:364–386](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L364-L386); [qlib/workflow/recorder.py:407–421](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L407-L421)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native configuration parsing, module loading and artifact deserialization.

Configuration YAML uses a safe loader. Loading a .py file requires an actual boolean trusted=True before module execution; default artifact loading restricts pickle globals. Installed module names are still imported and selected callables are invoked with configuration kwargs.

**Limit:** The explicit file/pickle trust gates do not turn general installed-module configuration into an allowlisted code sandbox. Trusted opt-in and custom unpicklers widen the boundary; allowlisted classes and dependencies remain trusted. No arbitrary callable or pickle payload was executed in this review.

**Executable sources:** [qlib/utils/__init__.py:245–258](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/__init__.py#L245-L258); [qlib/utils/mod.py:32–35](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/mod.py#L32-L35); [qlib/utils/mod.py:50–96](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/mod.py#L50-L96); [qlib/utils/mod.py:143–168](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/mod.py#L143-L168); [qlib/utils/mod.py:218–243](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/mod.py#L218-L243); [qlib/workflow/recorder.py:449–482](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L449-L482)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native Exchange data/price admission and selected configuration checks.

Exchange checks selected price/cost configuration types and rejects nontradable orders. get_deal_price substitutes the close quote when the selected quote is missing, NaN or near zero.

**Limit:** The fallback is a changed pricing rule, not proof that the replacement close is finite and economically valid. These checks do not establish a common finite-positive contract for all data, costs, user models and callbacks; some checks are assertions.

**Executable sources:** [qlib/backtest/exchange.py:139–192](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L139-L192); [qlib/backtest/exchange.py:404–442](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L404-L442); [qlib/backtest/exchange.py:494–514](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L494-L514)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Async logging and task-executor resource contracts.

AsyncCaller uses an unbounded Queue and joins its thread without a deadline. The task runner can isolate one task in ProcessPoolExecutor(max_workers=1), but waits for its result without an execution timeout.

**Limit:** Process count is not a total memory limit, and optional process recycling does not preempt a stuck callback. The harmless failure probe tested exception handling, not memory exhaustion or an unbounded workload.

**Executable sources:** [qlib/utils/paral.py:84–116](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/paral.py#L84-L116); [qlib/workflow/task/manage.py:526–548](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/manage.py#L526-L548)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Selected dataset download and temporary archive utilities.

The dataset helper streams HTTP with a 60-second timeout and status checking. Archive utilities extract through standard-library APIs; the buffer helper creates a temporary extraction directory and cleans up after use.

**Limit:** The inspected paths do not establish an expected content digest or an aggregate response/decompression quota. Archive filtering depends on the selected format and Python runtime; this review does not infer a universal traversal defect from the use of a standard-library extractor.

**Executable sources:** [qlib/tests/data.py:55–69](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/tests/data.py#L55-L69); [qlib/tests/data.py:119–131](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/tests/data.py#L119-L131); [qlib/utils/file.py:123–151](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/file.py#L123-L151)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**Unknown** · Inspected · applicability `unknown` · capability `not_located`

**Scope:** Managed experiment content identity at recorder/artifact admission.

The recorder stores run identity, code diff/status and selected environment information, and logs artifacts. An externally expected digest binding all study data/code/environment bytes at artifact read was not located in the inspected route.

**Limit:** The bounded inspection did not establish enforcement or prove repository-wide absence. Require an implementation pointer and executable acceptance results before treating this capability as present.

**Executable sources:** [qlib/workflow/recorder.py:345–420](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L345-L420); [qlib/workflow/recorder.py:449–482](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L449-L482)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Default recorder object loading and restricted pickle globals.

RestrictedUnpickler allows explicit module/name pairs and raises UnpicklingError for other globals. Recorder loading uses it by default, wraps failures and does not silently retry as unrestricted pickle.

**Limit:** Type admission is distinct from a content digest, ordered research-round/reference validation or tamper authenticity. An attacker able to rewrite allowed data can change values without violating a class allowlist; trusted/custom loading explicitly changes the boundary.

**Executable sources:** [qlib/utils/pickle_utils.py:178–198](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/pickle_utils.py#L178-L198); [qlib/workflow/recorder.py:449–482](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L449-L482)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Mongo task claim/result transitions and recorder completion.

Task fetching uses find_one_and_update to claim a waiting task; ordinary exceptions and KeyboardInterrupt return it to the prior status, and a result/status update is submitted together. Recorder completion waits for its AsyncCaller before ending the MLflow run.

**Limit:** A hard kill can bypass the return context; lease recovery and an atomic transaction spanning MLflow artifacts and task state were not established. The separate AsyncCaller probe shows join can return after a logging callback failed, so recorder completion alone is not evidence that all queued logging succeeded; MLflow itself was not executed.

**Executable sources:** [qlib/workflow/task/manage.py:265–310](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/manage.py#L265-L310); [qlib/workflow/task/manage.py:354–382](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/manage.py#L354-L382); [qlib/workflow/recorder.py:390–405](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L390-L405); [qlib/utils/paral.py:93–116](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/paral.py#L93-L116)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**Fails** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Native AsyncCaller callback exception propagation.

A harmless ValueError callback ran and terminated the worker thread. Native wait() returned normally without raising; the following queued callback never ran and two queue items remained. The bounded probe captured the thread exception and worker termination.

**Limit:** This is a reproduced AsyncCaller failure, not a claim that every Qlib worker loses errors. The MLflowRecorder use of this helper was inspected but no recorder, MLflow server or remote storage operation was executed.

**Executable sources:** [qlib/utils/paral.py:84–116](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/paral.py#L84-L116); [qlib/workflow/recorder.py:360–405](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L360-L405)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Cached model signal to native signal strategy.

ModelSignal calls the model's predict method, converts a DataFrame result to its first column and caches it. The strategy requests the preceding prediction interval and returns an empty trade decision when the result is None.

**Limit:** The inspected boundary does not establish universal shape, finite-value or probability-range validation of custom model outputs. Scores need not be probabilities; missing-result handling is specific to this strategy and does not prove all strategies stop on invalid inference.

**Executable sources:** [qlib/backtest/signal.py:42–75](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/signal.py#L42-L75); [qlib/contrib/strategy/signal_strategy.py:137–148](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/strategy/signal_strategy.py#L137-L148)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Period-scoped signal selection and configured execution quotes.

The native Topk strategy requests predictions from the preceding trade interval, and SignalWCache selects signal data within requested start/end bounds. Orders carry their execution interval to Exchange quote selection.

**Limit:** Correct timestamps, model fit boundaries and causal feature construction remain prerequisites. A period selection cannot repair a full-data predictor that used future observations; period aggregate prices do not prove tick-level availability or execution order.

**Executable sources:** [qlib/contrib/strategy/signal_strategy.py:137–148](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/strategy/signal_strategy.py#L137-L148); [qlib/backtest/signal.py:42–75](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/signal.py#L42-L75); [qlib/backtest/exchange.py:873–884](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L873-L884)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Finite-input native Exchange execution with a supplied position and configured costs.

The position-backed route clips sales to holdings, checks cash against minimum/variable costs, reduces unaffordable buys and rounds amounts through its trade-unit rule. Configured volume limits can further clip the executable amount.

**Limit:** The cash/holding guarantee is conditional on supplying a position and valid economic inputs; a position=None route deliberately omits the balance gate. Lot rounding is configuration dependent. This is simulated admission, not a live capital guarantee or general fee/NaN validation.

**Executable sources:** [qlib/backtest/exchange.py:757–832](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L757-L832); [qlib/backtest/exchange.py:859–952](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L859-L952)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native aggregate-quote execution, volume clipping and impact cost.

Exchange selects a configured deal quote, clips order amounts by configured volume limits and applies proportional/minimum cost plus an impact term based on order value relative to period trading value.

**Limit:** This is a period-price execution model. It does not establish stop precedence, path inside an OHLC bar, order-book queue position or real-world protective fills. Those semantics must be supplied and matched before an execution comparison.

**Executable sources:** [qlib/backtest/exchange.py:494–514](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L494-L514); [qlib/backtest/exchange.py:786–832](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L786-L832); [qlib/backtest/exchange.py:873–892](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L873-L892); [qlib/backtest/exchange.py:947–952](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py#L947-L952)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**Unknown** · Inspected · applicability `unknown` · capability `not_located`

**Scope:** Protected holdout reservation and exposure history in managed Qlib research.

No durable protected holdout reservation/exposure ledger was located in the bounded workflow inspection. Task claims, MLflow run identity and configured train/test periods address different contracts.

**Limit:** The bounded inspection did not establish enforcement or prove repository-wide absence. Require an implementation pointer and executable acceptance results before treating this capability as present.

**Executable sources:** [qlib/workflow/task/manage.py:265–310](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/task/manage.py#L265-L310); [qlib/workflow/recorder.py:345–405](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/recorder.py#L345-L405)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Checked-in source test/dependency CI.

The source workflow pins checkout/setup action commits, installs its test environment, runs pip check and executes selected pytest suites.

**Limit:** Unversioned installation steps, including the selected Torch install, do not establish a hash-locked dependency closure. Configured workflows are distinct from successful current runs, branch protection and release artifact provenance.

**Executable sources:** [.github/workflows/test_qlib_from_source.yml:31–56](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/.github/workflows/test_qlib_from_source.yml#L31-L56); [.github/workflows/test_qlib_from_source.yml:74–75](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/.github/workflows/test_qlib_from_source.yml#L74-L75); [.github/workflows/test_qlib_from_source.yml:149–159](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/.github/workflows/test_qlib_from_source.yml#L149-L159)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Inspected module/artifact security assertions and the executed async failure probe.

Security assertions reject an untrusted Python file before its marker executes, reject nonboolean trust values and deny dangerous pickle globals while allowing selected data round-trips. The independent bounded AsyncCaller probe reproduced lost callback completion/error propagation.

**Limit:** The repository security assertions were inspected, not run in this safety campaign. Only the stated harmless AsyncCaller probe was executed here; no malicious pickle target was invoked and no exhaustive dependency, denial-of-service or concurrency coverage is claimed.

**Executable sources:** [tests/security/test_module_loading.py:44–51](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/tests/security/test_module_loading.py#L44-L51); [tests/security/test_module_loading.py:78–121](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/tests/security/test_module_loading.py#L78-L121); [tests/security/test_pickle_utils.py:31–64](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/tests/security/test_pickle_utils.py#L31-L64); [tests/security/test_pickle_utils.py:84–107](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/tests/security/test_pickle_utils.py#L84-L107); [qlib/utils/paral.py:84–116](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/utils/paral.py#L84-L116)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

