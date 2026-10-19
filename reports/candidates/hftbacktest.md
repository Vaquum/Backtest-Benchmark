# hftbacktest

**Frozen source:** [nkaz001/hftbacktest @ 5f3ec40b2afb764e0fea112f941ed85523ef4e88](https://github.com/nkaz001/hftbacktest/tree/5f3ec40b2afb764e0fea112f941ed85523ef4e88)

**Observed license label:** MIT  
**Layer:** Specialist recorded order-book, queue and latency replay

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Native library tests pass 22/22 after dependency lock capture; no suitable recorded-depth workload was admitted, so there is no false OHLC speed ranking.

**Academic:** Distinct local/exchange clocks and queue/fill models are meaningful; venue calibration, sampling/return units and general research governance remain separate obligations.

**Safety:** Native replay/state behavior is inspected and library tests ran; malformed NPY/read-thread liveness counterexamples remain inspected, not executed hangs.

## P01

### Parameter-space construction and retained memory

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Specialized market-depth replay engine versus research parameter-space generator

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:343–378](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L343-L378); [hftbacktest/src/backtest/data/reader.rs:386–437](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L437)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Specialized market-depth replay engine versus search-family proposals

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:343–378](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L343-L378); [hftbacktest/src/backtest/data/reader.rs:386–437](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L437)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native source-built crate and recorded market-depth loading

The campaign attempts the native backtest library tests with a separately frozen dependency lock because upstream has no committed workspace lock.

**Limit:** No admitted recorded market-depth dataset: compilation and unit test execution are not a full first backtest result.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:343–378](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L343-L378); [hftbacktest/src/backtest/data/reader.rs:386–437](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L437)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Depth/latency replay versus fitted research campaign

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:343–378](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L343-L378); [hftbacktest/src/backtest/data/reader.rs:386–437](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L437)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Depth replay/state versus fold-fitted preparation

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:343–378](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L343-L378); [hftbacktest/src/backtest/data/reader.rs:386–437](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L437)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Order-book state and execution latency models versus common OHLC indicator kernels

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:343–378](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L343-L378); [hftbacktest/src/backtest/data/reader.rs:386–437](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L437)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**N/A** · Inspected · applicability `out_of_scope` · capability `implemented`

**Scope:** Depth/queue simulation versus the common hourly close snapshot

This campaign has only recorded OHLCV bars; they do not determine queue position, book depth or exchange/local timestamps.

**Limit:** No fabricated book data or OHLC performance ranking is assigned. A recorded order-book contract is the required comparison track.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:343–378](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L343-L378); [hftbacktest/src/backtest/data/reader.rs:386–437](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L437)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native depth replay, queue models, partial/nonpartial exchange processing

The source implements separate exchange processors with queue models and local/feed/order state.

**Limit:** Requires real event/latency/depth inputs and identical queue/fill assumptions before performance can be compared.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/proc/nopartialfillexchange.rs:96–137](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/proc/nopartialfillexchange.rs#L96-L137); [hftbacktest/src/backtest/proc/local.rs:59–90](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/proc/local.rs#L59-L90)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native loaded event data cache and prefetch

Cache keeps loaded Data with checkout/return accounting; parallel_load preloads the next key while the active input is consumed.

**Limit:** No data-scale RSS measurement. Cache removal scans entries and pending asynchronous loads contribute memory.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:90–153](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L90-L153); [hftbacktest/src/backtest/data/reader.rs:347–361](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L347-L361)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Asynchronous data file loading

The reader spawns threads to load NPY/NPZ files and receives data through a channel.

**Limit:** This is I/O prefetch, not demonstrated parallel strategy-simulation speedup. No worker-scaling benchmark.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:343–378](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L343-L378); [hftbacktest/src/backtest/data/reader.rs:386–437](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L437)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Reader cache/release and next-file prefetch

Native Cache maps file keys to shared loaded data; release removes an entry only after outstanding checkouts are returned.

**Limit:** No cache hit/retention cost benchmark. The separate loader failure/liveness finding limits robust operation on malformed files.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:90–153](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L90-L153); [hftbacktest/src/backtest/data/reader.rs:343–378](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L343-L378); [hftbacktest/src/backtest/data/reader.rs:386–437](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L437)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** In-memory specialist replay versus durable multi-trial checkpoint/resume

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:343–378](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L343-L378); [hftbacktest/src/backtest/data/reader.rs:386–437](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L437)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Separate local/exchange event and response timelines

The replay scheduler distinguishes local data, exchange data and local/exchange order events, advances the appropriate processor and stops at the requested timestamp. Order/feed waits expose events when their simulated local response time is reached.

**Limit:** This is meaningful native information-set modeling for order-book replay, conditional on valid event timestamps and chosen latency models. It does not prove arbitrary strategy features causal or validate recorded latency calibration; it is outside an OHLC-bar equivalence track.

**Executable sources:** [hftbacktest/src/backtest/mod.rs:755–855](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/mod.rs#L755-L855); [hftbacktest/src/backtest/mod.rs:1098–1118](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/mod.rs#L1098-L1118)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Managed ML training/evaluation

The native replay scheduler evolves exchange/local/order state rather than owning a supervised estimator workflow.

**Limit:** Train/evaluation isolation requires a research adapter. Missing ML fitting is outside the native order-book execution contract, not a low robustness score.

**Executable sources:** [hftbacktest/src/backtest/mod.rs:775–855](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/mod.rs#L775-L855)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Forward supervised targets

Native local/exchange processors consume timestamped market/order events.

**Limit:** No target horizon/censoring contract was located in this replay surface. A prediction adapter must define label availability using local observation times and exchange/response latency.

**Executable sources:** [hftbacktest/src/backtest/mod.rs:775–855](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/mod.rs#L775-L855)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Purged/nested model validation

The example parameter grid evaluates specified date ranges; statistics helpers can partition output by calendar period.

**Limit:** Calendar report partitions and repeated replay dates are not a managed purged/nested validation coordinator. A model/search adapter must own independent temporal assessment.

**Executable sources:** [hftbacktest/examples/6_gridsearch.py:45–67](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/examples/6_gridsearch.py#L45-L67); [py-hftbacktest/hftbacktest/stats/utils.py:21–36](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/py-hftbacktest/hftbacktest/stats/utils.py#L21-L36)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Fold-fitted preprocessing/stacking

The native engine accepts model implementations and replays state/events without a fold-owned feature fitting phase.

**Limit:** OOF stacking and transform fit locality were not located in this execution surface. They become applicable when an estimator adapter is supplied.

**Executable sources:** [hftbacktest/src/backtest/mod.rs:775–855](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/mod.rs#L775-L855)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Probability calibration/nested thresholds

Queue and latency models parameterize execution behavior; the example search varies strategy spread/grid settings.

**Limit:** Execution probability/latency assumptions are not a supervised probability-calibration protocol. Calibrated predictors and nested trading-threshold fitting require a separate research adapter.

**Executable sources:** [hftbacktest/src/backtest/models/queue.rs:124–155](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/models/queue.rs#L124-L155); [hftbacktest/examples/6_gridsearch.py:110–119](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/examples/6_gridsearch.py#L110-L119)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native mark-to-market P&L and annualized metrics

Recorder stores timestamp, midpoint, balance, position, fees and trade activity. Native Sharpe/Sortino use increments of net equity, annualized by samples/day times configurable252 trading days.

**Limit:** These are P&L-increment ratios, not automatically capital-normalized percentage-return metrics. Sampling frequency is inferred from the first interval; inconsistent intervals only warn. Freeze book size, currency, resampling and annualization before cross-engine comparison.

**Executable sources:** [hftbacktest/src/backtest/recorder.rs:45–60](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/recorder.rs#L45-L60); [py-hftbacktest/hftbacktest/stats/metrics.py:91–130](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/py-hftbacktest/hftbacktest/stats/metrics.py#L91-L130); [py-hftbacktest/hftbacktest/stats/utils.py:9–18](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/py-hftbacktest/hftbacktest/stats/utils.py#L9-L18)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected event-clock and queue model tests

Native tests assert that local/exchange processors skip events not visible to them and that current replay timestamps advance as expected. L3 queue tests assert specific fill/removal outcomes.

**Limit:** Tests were inspected, not executed in this academic audit. These local state invariants do not validate a complete live-exchange fill oracle, latency fit or counterfactual impact model.

**Executable sources:** [hftbacktest/src/backtest/mod.rs:1212–1237](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/mod.rs#L1212-L1237); [hftbacktest/src/backtest/models/queue.rs:1207–1216](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/models/queue.rs#L1207-L1216)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Statistical estimator convergence

The inspected latency model returns configured values and the replay loop evolves deterministic model state.

**Limit:** Model-estimation convergence is outside this native executor contract. Calibrating latency/queue parameters or adding learned forecasts requires an explicit fitting/evaluation adapter.

**Executable sources:** [hftbacktest/src/backtest/models/latency.rs:39–54](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/models/latency.rs#L39-L54); [hftbacktest/src/backtest/mod.rs:755–774](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/mod.rs#L755-L774)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Example grid-search output identity

The executable grid-search example enumerates parameter combinations and embeds spread/grid/skew settings in output names while reporting subprocess return codes.

**Limit:** This is an example-level record convention, not a durable complete trial/failure/selection ledger. Full external searches and parameter families are caller-owned.

**Executable sources:** [hftbacktest/examples/6_gridsearch.py:53–69](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/examples/6_gridsearch.py#L53-L69); [hftbacktest/examples/6_gridsearch.py:110–119](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/examples/6_gridsearch.py#L110-L119)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Unknown** · Inspected · applicability `native` · capability `not_located`

**Scope:** Family/dependence-adjusted strategy evidence

The inspected metric code calculates marginal P&L ratios and the example executes a parameter grid.

**Limit:** No DSR/PBO, multiple-family adjustment or dependence-aware inferential acceptance gate was located in these native stats/example-search surfaces. Different replay assumptions cannot be treated as independent candidate draws automatically.

**Executable sources:** [py-hftbacktest/hftbacktest/stats/metrics.py:95–130](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/py-hftbacktest/hftbacktest/stats/metrics.py#L95-L130); [hftbacktest/examples/6_gridsearch.py:110–119](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/examples/6_gridsearch.py#L110-L119)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Replay state records and execution assumptions

Native per-asset records retain balance/position/fees/activity over time; the example command passes data/latency file paths, tick/lot sizes and strategy parameters explicitly.

**Limit:** These records do not constitute a canonical source/input-byte/environment equality manifest. Record sampling, fee/queue/latency model, event ordering and market-data provenance must be fixed for a fair specialist comparison.

**Executable sources:** [hftbacktest/src/backtest/recorder.rs:45–60](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/recorder.rs#L45-L60); [hftbacktest/src/backtest/recorder.rs:94–112](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/recorder.rs#L94-L112); [hftbacktest/examples/6_gridsearch.py:51–66](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/examples/6_gridsearch.py#L51-L66)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Protected final research holdout

Native replay and its example grid use supplied date/file ranges.

**Limit:** No reserve/freeze/first-access final holdout mechanism was located here. A research adapter must own model selection and final-data access; this is outside the order-book replay primitive.

**Executable sources:** [hftbacktest/examples/6_gridsearch.py:45–67](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/examples/6_gridsearch.py#L45-L67); [hftbacktest/src/backtest/mod.rs:755–774](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/mod.rs#L755-L774)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Order-book/exchange model external validity

Native code distinguishes maker/taker fills, partial remaining quantity, local/exchange latency and queue assumptions, giving the specialist track substantially richer modeled execution than OHLC-only replay.

**Limit:** Model detail is not validation against actual executions. The inspected fill routine updates simulated order/account state, while market observations remain a replay; real counterfactual market response and calibrated queue/latency accuracy are unmeasured here. Do not synthesize a book from OHLC and claim an equivalent benchmark.

**Executable sources:** [hftbacktest/src/backtest/proc/partialfillexchange.rs:208–244](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/proc/partialfillexchange.rs#L208-L244); [hftbacktest/src/backtest/mod.rs:821–841](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/mod.rs#L821-L841); [hftbacktest/src/backtest/models/latency.rs:39–54](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/models/latency.rs#L39-L54)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Execution-assumption and strategy sensitivity

Generic latency/queue implementations and the executable parameter grid allow separate studies of strategy and execution assumptions.

**Limit:** No mandatory latency/queue calibration, sensitivity envelope or independent-regime replication is enforced by these building blocks. Runtime comparisons must stay within a matched order-book track.

**Executable sources:** [hftbacktest/src/backtest/models/queue.rs:124–155](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/models/queue.rs#L124-L155); [hftbacktest/src/backtest/models/latency.rs:39–54](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/models/latency.rs#L39-L54); [hftbacktest/examples/6_gridsearch.py:110–119](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/examples/6_gridsearch.py#L110-L119)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native trusted strategy and data preprocessor; full managed research workflow is a separate layer.

The selected Rust replay route invokes a trusted DataPreprocess object; a declarative callable sandbox is outside this specialist API.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:386–438](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L438)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** NPY admission, event preprocessing and local order submission.

NPY loading checks magic/version and selected dtype/shape properties, and an optional Python validator rejects exchange/local event order reversals. Local order construction checks duplicate IDs but directly converts price/quantity.

**Limit:** This is not complete finite-value or malformed-header admission. Malformed NPY lengths/headers can panic before a structured error; the optional timestamp validator is not evidence every ingestion route invokes it.

**Executable sources:** [hftbacktest/src/backtest/data/npy/mod.rs:235–293](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/npy/mod.rs#L235-L293); [hftbacktest/src/backtest/proc/local.rs:146–178](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/proc/local.rs#L146-L178); [py-hftbacktest/hftbacktest/data/validation.py:139–152](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/py-hftbacktest/hftbacktest/data/validation.py#L139-L152)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Fails** · Inspected · applicability `native` · capability `implemented`

**Scope:** Generic read_npy with declared size exceeding available bytes; loader allocation.

The read loop only adds the returned byte count and never handles Ok(0), so EOF before the declared size has no progress/termination condition. Buffer allocation follows supplied/file/archive size without a configured byte quota.

**Limit:** This is static source proof; no unbounded reproducer was run. An ordinarily truncated file whose metadata reflects its short size may instead reach a bounds panic; not every malformed NPY follows the EOF loop.

**Executable sources:** [hftbacktest/src/backtest/data/npy/mod.rs:235–261](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/npy/mod.rs#L235-L261); [hftbacktest/src/backtest/data/npy/mod.rs:302–356](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/npy/mod.rs#L302-L356)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Local NPY/NPZ and optional S3 data source.

NPZ input reads a named member without extracting paths onto disk. The loader allocates for that member's uncompressed size; the optional S3 route collects a full object before parsing.

**Limit:** No archive-path extraction vulnerability is inferred from this route. Byte/decompression budgets, source authenticity and network deadlines beyond the delegated S3 SDK were not established.

**Executable sources:** [hftbacktest/src/backtest/data/npy/mod.rs:175–223](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/npy/mod.rs#L175-L223); [hftbacktest/src/backtest/data/npy/mod.rs:302–356](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/npy/mod.rs#L302-L356)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native order-book replay and recorder export; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [hftbacktest/src/backtest/recorder.rs:121–139](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/recorder.rs#L121-L139)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**Partial** · Inspected · applicability `adapter_required` · capability `implemented`

**Scope:** NPY/NPZ source admission and recorder files.

The recorder exports compressed NPY members; readers perform format checks. Invalid header indexing and an unchecked header parse can panic rather than yield the advertised I/O Result.

**Limit:** No managed-round expected digest/reference verifier is established. The malformed-reader liveness implication is separately recorded under S08; crash and byte-mutation probes were not executed.

**Executable sources:** [hftbacktest/src/backtest/recorder.rs:121–139](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/recorder.rs#L121-L139); [hftbacktest/src/backtest/data/npy/mod.rs:235–293](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/npy/mod.rs#L235-L293)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**Partial** · Inspected · applicability `adapter_required` · capability `implemented`

**Scope:** Recorder NPZ output and simulation state.

to_npz creates/truncates the target file, writes members and finishes the ZIP container.

**Limit:** The selected recorder does not establish atomic replacement, fsync or a durable research restart frontier. Completion of this export differs from durable replay-state recovery.

**Executable sources:** [hftbacktest/src/backtest/recorder.rs:121–139](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/recorder.rs#L121-L139)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**Fails** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native asynchronous data-loader panic path.

A load thread's JoinHandle is discarded and panics are not converted to a channel result. next_data blocks on recv while Reader retains its own Sender; after a loader panic, the requested cache entry can remain unready indefinitely.

**Limit:** Static route proof combines the malformed-header panic with the channel ownership/control flow. No live hang or process-kill test was run. Ordinary returned I/O errors do propagate as BacktestError.

**Executable sources:** [hftbacktest/src/backtest/data/reader.rs:319–375](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L319-L375); [hftbacktest/src/backtest/data/reader.rs:386–438](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/reader.rs#L386-L438); [hftbacktest/src/backtest/data/npy/mod.rs:246–261](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/npy/mod.rs#L246-L261)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native strategy-driven order-book simulation; full managed research workflow is a separate layer.

A fitted probability model and unavailable-signal policy are outside the selected order-book replay API; strategy code determines order requests.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [hftbacktest/src/backtest/proc/local.rs:146–178](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/proc/local.rs#L146-L178)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Exchange/local event clocks and optional order validator.

The model distinguishes exchange/local event timestamp sequences, and its validator independently rejects decreasing timestamps in each stream. wait_order_response advances a simulated-time deadline.

**Limit:** A simulated timestamp timeout is not a wall-clock worker deadline. Caller data must carry correct event flags/availability times; validation is not signed provenance or proof the source feed is complete.

**Executable sources:** [py-hftbacktest/hftbacktest/data/validation.py:139–152](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/py-hftbacktest/hftbacktest/data/validation.py#L139-L152); [hftbacktest/src/backtest/mod.rs:1069–1093](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/mod.rs#L1069-L1093)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Specialist fill/PnL-accounting track; capital admission requires an added policy.

Native State starts balance at zero and updates balance/position/fees for each fill. This represents fill-derived PnL/accounting, not an initial-capital cash or margin admission model.

**Limit:** It is inappropriate to call ordinary negative balance a borrowing defect under this model. A cash/margin/exposure risk adapter is required before using the same S11 contract as Limen's capital-constrained event route; live risk is not assessed by this specialist row.

**Executable sources:** [hftbacktest/src/backtest/state.rs:22–55](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/state.rs#L22-L55)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Queue-based partial/no-partial fill variants.

A partial-fill exchange consults queue-model filled quantity and caps fills to leaves quantity; a separate no-partial variant fills the remaining size. Market depth and queue assumptions explicitly participate in execution.

**Limit:** This specialist track requires event/order-book data and cannot be ranked against OHLC stop rules using the same fixture alone. Queue model and replay assumptions do not guarantee real counterfactual market impact or live fills.

**Executable sources:** [hftbacktest/src/backtest/proc/partialfillexchange.rs:150–214](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/proc/partialfillexchange.rs#L150-L214); [hftbacktest/src/backtest/proc/nopartialfillexchange.rs:164–195](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/proc/nopartialfillexchange.rs#L164-L195)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native specialist order-book replay; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [hftbacktest/src/backtest/recorder.rs:121–139](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/recorder.rs#L121-L139)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Pinned source CodeQL configuration.

The repository configures scheduled/PR CodeQL analysis for Python using tagged actions.

**Limit:** The inspected CodeQL matrix contains Python only; it does not establish coverage of the Rust reader findings. Hosted success, source-to-binary identity and a complete audited dependency closure were not verified.

**Executable sources:** [.github/workflows/codeql.yml:14–76](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/.github/workflows/codeql.yml#L14-L76)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected, Tested · applicability `native` · capability `implemented`

**Scope:** Executed native backtest-library tests and inspected malformed-reader control flow.

The exact pinned source passed 22 native backtest-library tests, including queue fill/crossing and depth/event assertions, using the retained resolved dependency lock. Queue tests assert fill outcomes and removal of filled backtest orders. Static inspection identified separate malformed-reader liveness cases.

**Limit:** The 22-test campaign is not a malicious-file fuzz or corruption campaign. The EOF and loader-panic counterexamples remain Inspected, not Reproduced. Queue/depth arithmetic coverage cannot stand in for reader failure coverage, and no order-book performance measurement follows from these tests.

**Executable sources:** [hftbacktest/src/backtest/models/queue.rs:1207–1216](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/models/queue.rs#L1207-L1216); [hftbacktest/src/backtest/models/queue.rs:1241–1247](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/models/queue.rs#L1241-L1247); [hftbacktest/src/backtest/data/npy/mod.rs:235–261](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/hftbacktest/src/backtest/data/npy/mod.rs#L235-L261)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

