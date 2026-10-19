# QSTrader

**Frozen source:** [mhallsmoore/qstrader @ 4c59e1584e83fcc2be644b820f827c0dd1b45c02](https://github.com/mhallsmoore/qstrader/tree/4c59e1584e83fcc2be644b820f827c0dd1b45c02)

**Observed license label:** MIT  
**Layer:** Daily portfolio workflow; native broker/portfolio components measured

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Hourly broker/portfolio component replay is admitted; the benchmark supplies the driver, so no full-engine Limen duration ratio is assigned.

**Academic:** A public prehistory getter returns the final future quote; native first-peak drawdown handling also has a source-level issue. Native daily output conventions need alignment.

**Safety:** The prehistory probe and an insufficient-cash one-unit fill are reproduced; the latter fails a required cash-only policy, with borrowing treated separately.

## P01

### Parameter-space construction and retained memory

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Configured quant-system/portfolio workflow versus search-family generation

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qstrader/trading/backtest.py:206–215](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L206-L215); [qstrader/trading/backtest.py:382–432](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L382-L432)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** BacktestTradingSession versus candidate proposal/exhaustion

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qstrader/trading/backtest.py:206–215](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L206-L215); [qstrader/trading/backtest.py:382–432](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L382-L432)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Native SimulatedBroker and Portfolio components under an explicit hourly driver

The native full session builds a daily business-day simulation engine. The admitted hourly replay times native account components under benchmark orchestration.

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
    "first_full_common_ms_median": 52.037716,
    "first_full_common_ms_min": 50.329493,
    "first_full_common_ms_max": 54.159881,
    "launch_to_ready_ms_median": 31.965709,
    "launch_to_first_valid_ms_median": 1333.363554
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": false,
    "independent_processes": 5,
    "first_full_common_ms_median": 54.85003,
    "first_full_common_ms_min": 50.874329,
    "first_full_common_ms_max": 59.466292,
    "launch_to_ready_ms_median": 36.096087,
    "launch_to_first_valid_ms_median": 1309.992128
  }
]
```

**Executable sources:** [qstrader/trading/backtest.py:206–215](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L206-L215); [qstrader/trading/backtest.py:382–432](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L382-L432)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Broker/portfolio component replay versus native research workflow

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qstrader/trading/backtest.py:206–215](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L206-L215); [qstrader/trading/backtest.py:382–432](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L382-L432)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Native portfolio allocation/backtest session versus supervised preparation

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qstrader/trading/backtest.py:206–215](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L206-L215); [qstrader/trading/backtest.py:382–432](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L382-L432)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native buffered SMA and volatility signal kernels

The native SMA signal calculates the mean of its buffered prices; the volatility signal calculates return dispersion. Native-kernel throughput is unmeasured.

**Limit:** The component adapter uses common externally prepared SMA decisions, so its timing excludes these native feature kernels.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qstrader/signals/sma.py:29–61](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/signals/sma.py#L29-L61); [qstrader/signals/vol.py:68–81](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/signals/vol.py#L68-L81)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Native broker/portfolio components; excluded from full-engine rankings

The adapter uses actual native execution and account state but supplies the hourly event loop.

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
    "warm_full_common_ms_median": 54.671549,
    "warm_engine_ms_median": 54.465608,
    "warm_extraction_common_ms_median": 0.215675,
    "warm_full_common_cpu_ms_median": 54.673305,
    "warm_process_medians_ms": [
      50.807313,
      64.128334,
      54.671549,
      55.712954,
      51.042775
    ],
    "warm_process_median_ms_min": 50.807313,
    "warm_process_median_ms_max": 64.128334,
    "warm_evaluation_bars_per_second": 160650.2863125389,
    "relative_to_limen_warm_full_common": null
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": false,
    "independent_processes": 5,
    "warm_full_common_ms_median": 52.235422,
    "warm_engine_ms_median": 52.008099,
    "warm_extraction_common_ms_median": 0.226582,
    "warm_full_common_cpu_ms_median": 52.237794,
    "warm_process_medians_ms": [
      50.480368,
      52.218053,
      53.128583,
      52.235422,
      61.035997
    ],
    "warm_process_median_ms_min": 50.480368,
    "warm_process_median_ms_max": 61.035997,
    "warm_evaluation_bars_per_second": 168142.60637159206,
    "relative_to_limen_warm_full_common": null
  }
]
```

**Executable sources:** [qstrader/broker/simulated_broker.py:567–603](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L567-L603); [qstrader/broker/portfolio/portfolio.py:214–233](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/portfolio/portfolio.py#L214-L233)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native daily event loop and broker marking/order queue

The full session updates broker and quant system per daily event; broker marks all portfolios and processes submitted orders.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qstrader/trading/backtest.py:206–215](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L206-L215); [qstrader/trading/backtest.py:382–432](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L382-L432); [qstrader/broker/simulated_broker.py:650–682](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L650-L682)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Partial** · Inspected, Tested, Measured · applicability `native` · capability `implemented`

**Scope:** Broker/portfolio histories under custom hourly driver

The broker walks held assets and drains/sorts orders; component replay retains common output arrays.

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
    "peak_rss_bytes_median": 131072000
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": false,
    "independent_processes": 5,
    "peak_rss_bytes_median": 133193728
  }
]
```

**Executable sources:** [qstrader/broker/simulated_broker.py:650–682](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L650-L682)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Single native trading session versus parallel research campaign

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qstrader/trading/backtest.py:206–215](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L206-L215); [qstrader/trading/backtest.py:382–432](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L382-L432)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** In-memory historical bars and broker account state

The daily CSV data source keeps per-symbol frames and resolves a requested timestamp using an index lookup.

**Limit:** This is historical data lookup, not trained-preparation reuse. Hit cost and invalidation unmeasured; the before-start boundary counterexample is separately recorded.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [qstrader/data/daily_bar_csv.py:217–247](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/data/daily_bar_csv.py#L217-L247)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native result recording, separately from research checkpoint/resume

Native JSON statistics output writes the generated statistics to a file.

**Limit:** Native result-write overhead is unmeasured. Crash-safe continuation and an exact multi-round durable commit frontier are not established by these serialization paths.

**Measurement state:** Not measured in this criterion scope

**Distinct sub-capabilities:** native_recording: Implemented; complete_checkpoint_continuation: Unknown/not located in the cited result-write path

**Executable sources:** [qstrader/statistics/json_statistics.py:384–391](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/statistics/json_statistics.py#L384-L391)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Fails** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Native CSVDailyBarDataSource prehistory getter

A recorded-fixture public-getter probe queried before the first available quote and received the final future quote: bid/ask 45,056.0 at query 2024-01-01 14:29:59 UTC came from 2024-01-02 21:00 UTC. get_indexer(method=pad) returns -1, which the implementation passes to iloc.

**Limit:** Scope is the native CSV bid/ask getter before source history begins. No claim is made that every trading-session loop issues that query. The fixture retained original selected open/close values; the source itself synthesized daily quote times.

**Executable sources:** [qstrader/data/daily_bar_csv.py:217–248](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/data/daily_bar_csv.py#L217-L248); [qstrader/signals/signals_collection.py:53–62](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/signals/signals_collection.py#L53-L62)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Managed estimator train/evaluation isolation

Native fixed/single alpha signals and equal/fixed-weight portfolio optimizers expose callable execution interfaces.

**Limit:** A native supervised train/validation/test manager was not located in these alpha/portfolio/runner surfaces. A learned-model adapter must establish fit isolation.

**Executable sources:** [qstrader/alpha_model/single_signal.py:45–46](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/alpha_model/single_signal.py#L45-L46); [qstrader/portcon/optimiser/equal_weight.py:47–51](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/portcon/optimiser/equal_weight.py#L47-L51); [qstrader/portcon/optimiser/fixed_weight.py:41–41](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/portcon/optimiser/fixed_weight.py#L41-L41)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Forward target availability

The inspected signal collection appends latest prices to bounded history and supplies technical signals, rather than constructing forward supervised targets.

**Limit:** Label horizon/censoring belongs to an added predictive-model workflow. Getter chronology is separately tested under A01.

**Executable sources:** [qstrader/signals/signals_collection.py:53–62](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/signals/signals_collection.py#L53-L62); [qstrader/signals/buffer.py:53–58](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/signals/buffer.py#L53-L58)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Purged/nested temporal validation

The runner supports start/end dates, burn-in and configurable rebalance dates.

**Limit:** Burn-in controls trading/performance recording, not train/test horizon overlap. A purged/nested research split coordinator was not located in this runner/portfolio surface.

**Executable sources:** [qstrader/trading/backtest.py:243–259](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L243-L259); [qstrader/trading/backtest.py:399–425](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L399-L425)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Fold-fitted transforms and stacking

Signal buffers use bounded deques of observed prices; equal/fixed-weight optimizers do not fit supervised transforms.

**Limit:** No OOF stack or fold-owned learned preprocessing contract was located in this surface. An ML adapter must supply and verify it.

**Executable sources:** [qstrader/signals/buffer.py:53–58](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/signals/buffer.py#L53-L58); [qstrader/portcon/optimiser/equal_weight.py:47–51](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/portcon/optimiser/equal_weight.py#L47-L51)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Probability calibration and nested thresholds

Native single-signal alpha returns a configured scalar per current asset and equal-weight optimization maps it to weights.

**Limit:** No probability calibration or nested classification-threshold protocol was located in these built-ins. This is outside the fixed-allocation track.

**Executable sources:** [qstrader/alpha_model/single_signal.py:45–46](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/alpha_model/single_signal.py#L45-L46); [qstrader/portcon/optimiser/equal_weight.py:47–51](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/portcon/optimiser/equal_weight.py#L47-L51)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native summary metric formulas

Sharpe uses zero-target arithmetic mean/population std with default252; Sortino divides by the standard deviation of negative returns. CAGR uses row count/periods and expects normalized cumulative equity.

**Limit:** These are not interchangeable with sample-std Sharpe, downside-RMS Sortino or elapsed-calendar CAGR. The drawdown routine seeds high-water marks at zero and starts at row1, omitting the first cumulative-equity value as a possible peak; initial declines can therefore be understated. This metric issue is source-inspected, not separately runtime-reproduced.

**Executable sources:** [qstrader/statistics/performance.py:40–65](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/statistics/performance.py#L40-L65); [qstrader/statistics/performance.py:82–98](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/statistics/performance.py#L82-L98); [qstrader/statistics/tearsheet.py:36–54](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/statistics/tearsheet.py#L36-L54)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Inspected accounting regressions and executed boundary probe

Integration tests compare full portfolio history and approximate final holdings/P&L against stored expectations. A focused recorded-data probe reproduced the public prehistory getter defect.

**Limit:** The broader source suite was inspected, not executed in this academic audit. Golden histories do not independently validate all market assumptions, and the focused defect is not a global failure-rate estimate.

**Executable sources:** [tests/integration/trading/test_backtest_e2e.py:65–74](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/tests/integration/trading/test_backtest_e2e.py#L65-L74); [qstrader/data/daily_bar_csv.py:217–248](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/data/daily_bar_csv.py#L217-L248)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Statistical optimizer convergence

The shipped equal/fixed-weight optimizers perform direct arithmetic/pass-through in the inspected portfolio surface.

**Limit:** Estimator solver convergence is not applicable to those direct algorithms. A different learned optimizer/model requires an adapter and its own convergence acceptance evidence.

**Executable sources:** [qstrader/portcon/optimiser/equal_weight.py:47–51](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/portcon/optimiser/equal_weight.py#L47-L51); [qstrader/portcon/optimiser/fixed_weight.py:41–41](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/portcon/optimiser/fixed_weight.py#L41-L41)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Search-family trial ledger

The native statistics writer emits one configured strategy/benchmark result and allocation history.

**Limit:** A managed hyperparameter/search-family trial ledger was not located in this runner/statistics surface. For a strategy-selection study, capture all attempts externally.

**Executable sources:** [qstrader/statistics/json_statistics.py:40–61](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/statistics/json_statistics.py#L40-L61); [qstrader/statistics/json_statistics.py:389–391](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/statistics/json_statistics.py#L389-L391)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Post-selection and dependence inference

Native summary functions calculate point estimates of return/risk statistics.

**Limit:** No managed strategy search or selection-adjusted/dependence-aware inference was located in these statistics/optimizer paths. This capability needs a research adapter.

**Executable sources:** [qstrader/statistics/performance.py:40–65](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/statistics/performance.py#L40-L65); [qstrader/portcon/optimiser/fixed_weight.py:41–41](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/portcon/optimiser/fixed_weight.py#L41-L41)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native daily equity and JSON export

The runner records daily closing equity after optional burn-in and exports strategy/benchmark IDs, curves and allocations.

**Limit:** The native equity accessor reduces timestamps to calendar dates; JSON conversion also reduces them to midnight and replaces NaN values with zero. This output is not a lossless intraday/provenance artifact and does not establish code/data/environment identity.

**Executable sources:** [qstrader/trading/backtest.py:343–347](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L343-L347); [qstrader/trading/backtest.py:420–425](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L420-L425); [qstrader/statistics/json_statistics.py:79–88](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/statistics/json_statistics.py#L79-L88); [qstrader/statistics/json_statistics.py:389–391](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/statistics/json_statistics.py#L389-L391)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Protected final holdout

The runner executes configured date ranges and rebalances; burn-in can suppress early trading and equity recording.

**Limit:** No model freeze, reservation or first-access final holdout protocol was located in this surface. Burn-in is not a protected statistical holdout.

**Executable sources:** [qstrader/trading/backtest.py:399–425](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L399-L425)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Portfolio baselines and economic external validity

Equal/fixed-weight allocation and optional benchmark equity provide simple portfolio comparators, and end-to-end accounting regressions exist.

**Limit:** External predictive/economic validity is unmeasured. Daily simulated quote clocks, fees, exposure and the tested prehistory boundary must be considered before treating native benchmark results as a realistic market experiment.

**Executable sources:** [qstrader/portcon/optimiser/equal_weight.py:47–51](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/portcon/optimiser/equal_weight.py#L47-L51); [qstrader/statistics/json_statistics.py:40–61](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/statistics/json_statistics.py#L40-L61); [tests/integration/trading/test_backtest_e2e.py:65–74](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/tests/integration/trading/test_backtest_e2e.py#L65-L74)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Rebalance/burn-in/signal-window sensitivity

The runner supports buy-and-hold/daily/weekly/end-of-month rebalance policies, optional burn-in and signal history lengths.

**Limit:** These knobs enable manually coordinated sensitivity studies; no required ablation, seeded search manifest or independent-regime replication was located in this surface.

**Executable sources:** [qstrader/trading/backtest.py:243–259](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L243-L259); [qstrader/trading/backtest.py:399–425](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/trading/backtest.py#L399-L425); [qstrader/signals/buffer.py:53–58](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/signals/buffer.py#L53-L58)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native Python broker/data-handler objects; full managed research workflow is a separate layer.

The selected simulated broker accepts trusted Python model/data objects; no declarative callable sandbox is part of this route.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [qstrader/broker/simulated_broker.py:46–71](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L46-L71)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** CSV quotes, public orders and transactions.

CSV data are sorted and timezone-localized; portfolio transactions reject dates before the portfolio clock. Public Order and Transaction construction largely assigns supplied numeric fields.

**Limit:** These selected routes do not establish finite-positive OHLC/order validation or complete cash admission. Both reproduced findings use valid unchanged recorded prices, so they do not depend on malformed financial values.

**Executable sources:** [qstrader/data/daily_bar_csv.py:91–99](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/data/daily_bar_csv.py#L91-L99); [qstrader/execution/order.py:30–44](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/execution/order.py#L30-L44); [qstrader/broker/transaction/transaction.py:25–40](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/transaction/transaction.py#L25-L40); [qstrader/broker/portfolio/portfolio.py:204–232](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/portfolio/portfolio.py#L204-L232)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Daily CSV loading and quote caches.

The source reads full CSV files and builds open/close quote frames; bid/ask getters use bounded LRU entry counts.

**Limit:** No input byte, aggregate memory or wall-clock budget is enforced by the selected loading/backtest route. Bounded cache entry count does not bound the size of preloaded market frames.

**Executable sources:** [qstrader/data/daily_bar_csv.py:91–99](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/data/daily_bar_csv.py#L91-L99); [qstrader/data/daily_bar_csv.py:148–177](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/data/daily_bar_csv.py#L148-L177); [qstrader/data/daily_bar_csv.py:200–247](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/data/daily_bar_csv.py#L200-L247)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Local CSV source path handling.

The source joins a caller-supplied CSV directory and filenames/symbol-derived names before reading. It does not perform network acquisition in this route.

**Limit:** Paths belong to a trusted local researcher. No containment boundary for hostile filenames/symbols or capped file admission is established.

**Executable sources:** [qstrader/data/daily_bar_csv.py:91–126](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/data/daily_bar_csv.py#L91-L126)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native in-memory simulated broker/portfolio; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [qstrader/broker/portfolio/portfolio.py:33–78](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/portfolio/portfolio.py#L33-L78); [qstrader/broker/simulated_broker.py:650–682](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L650-L682)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native in-memory simulated broker/portfolio; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [qstrader/broker/portfolio/portfolio.py:33–78](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/portfolio/portfolio.py#L33-L78); [qstrader/broker/simulated_broker.py:650–682](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L650-L682)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native in-memory simulated broker/portfolio; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [qstrader/broker/portfolio/portfolio.py:33–78](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/portfolio/portfolio.py#L33-L78); [qstrader/broker/simulated_broker.py:650–682](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L650-L682)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native sequential simulated-broker queue drain; full managed research workflow is a separate layer.

The native route drains its order queue in one process. A parallel managed experiment executor is outside this selected route.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [qstrader/broker/simulated_broker.py:650–682](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L650-L682)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** BacktestDataHandler unavailable-quote behavior.

The data handler catches source exceptions and returns NaN when no usable quote is obtained. The latest bid/ask pair helper returns the bid value twice.

**Limit:** Returning (bid,bid) is harmless for the built-in equal-bid/ask CSV source but does not preserve a spread from a custom source. No typed prediction/probability validity or unavailable-signal-to-order contract is established.

**Executable sources:** [qstrader/data/backtest_data_handler.py:16–54](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/data/backtest_data_handler.py#L16-L54)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Fails** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Public CSVDailyBarDataSource prehistory bid/ask lookup.

For a query before the first quote, pandas pad indexing returns -1 and the code reads the final quote. The recorded-fixture probe returned 45,056.0 from 2024-01-02 21:00 UTC for a 2024-01-01 14:29:59 UTC query before the first native quote.

**Limit:** This is a reachable public getter boundary, not proof every stock-loop configuration queries prehistory. The probe uses two unchanged midnight fixture observations; QSTrader's synthetic daily open/close clock is not treated as faithful instrument session metadata.

**Executable sources:** [qstrader/data/daily_bar_csv.py:217–247](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/data/daily_bar_csv.py#L217-L247)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Fails** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Default simulated-broker route when a cash-only affordability contract is required.

Insufficient cash emits a warning and still executes unchanged quantity. With recorded price 42,283.58 and cash 21,141.79, public submit_order/update filled 1 unit and left cash -21,141.79.

**Limit:** Negative cash can represent intentional borrowing; the demonstrated failure is the absence of a hard cash-only admission rule on this default route. It does not imply live orders, unbounded credit at a broker or that every QSTrader allocation algorithm overspends.

**Executable sources:** [qstrader/broker/simulated_broker.py:586–603](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L586-L603); [qstrader/broker/portfolio/portfolio.py:216–232](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/portfolio/portfolio.py#L216-L232)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Default simulated fill and supplied cost-model parameters.

The broker selects a bid/ask price and executes the order; fee_model defaults to ZeroFeeModel. Constructor arguments slippage_model and market_impact_model are assigned None in the inspected implementation.

**Limit:** The selected default path does not establish depth/volume partial fills, price impact or intrabar stop uncertainty. Passing those two constructor arguments does not establish implemented slippage/impact behavior.

**Executable sources:** [qstrader/broker/simulated_broker.py:46–71](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L46-L71); [qstrader/broker/simulated_broker.py:543–603](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L543-L603)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native portfolio/backtest simulation; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [qstrader/broker/simulated_broker.py:650–682](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L650-L682)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Legacy executable Travis configuration.

Checked-in CI installs base/test requirements and runs pytest coverage plus flake8 on a listed Python matrix.

**Limit:** No hosted status, protected gate or dependency hash closure was verified; the frozen 2024 source and legacy CI configuration do not establish current deployment assurance.

**Executable sources:** [.travis.yml:1–21](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/.travis.yml#L1-L21)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Inspected portfolio assertions and two bounded public-route probes.

Native portfolio tests exercise date ordering/accounting. Independent probes using unchanged recorded fixture rows reproduce a prehistory quote and a default cash-only affordability counterexample.

**Limit:** No candidate-wide fuzz, corruption, worker-kill or live test campaign was run. The two probes establish their precise reachable paths only.

**Executable sources:** [tests/unit/broker/portfolio/test_portfolio.py:170–238](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/tests/unit/broker/portfolio/test_portfolio.py#L170-L238); [qstrader/data/daily_bar_csv.py:217–247](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/data/daily_bar_csv.py#L217-L247); [qstrader/broker/simulated_broker.py:586–603](https://github.com/mhallsmoore/qstrader/blob/4c59e1584e83fcc2be644b820f827c0dd1b45c02/qstrader/broker/simulated_broker.py#L586-L603)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

