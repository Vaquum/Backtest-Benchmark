# NautilusTrader

**Frozen source:** [nautechsystems/nautilus_trader @ 42c3ca5f8f8d537f69772277e77792bb5b307ea5](https://github.com/nautechsystems/nautilus_trader/tree/42c3ca5f8f8d537f69772277e77792bb5b307ea5)

**Observed license label:** LGPL-3.0  
**Layer:** Native event/actor/account engine and optional durable event store

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Pinned v2 source is assessed; native test compilation timed out twice before completion. No runtime throughput or older-release figure is substituted.

**Academic:** Availability-time replay and canonical result bytes provide concrete primitives; they do not establish complete input identity, research isolation or market calibration.

**Safety:** Configured risk gates and transactional/hash-verified redb persistence are substantive; bypass, backend selection and trusted callbacks delimit enforcement.

## P01

### Parameter-space construction and retained memory

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Native BacktestRunConfig collection versus search-domain construction

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/backtest/src/node.rs:151–179](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L151-L179)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Supplied native run configs versus candidate generation

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/backtest/src/node.rs:151–179](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L151-L179)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native v2 backtest crate initialization

This campaign attempts the exact pinned native Rust backtest crate tests; Python v1 wheels are not substituted.

**Limit:** Crate test/build duration is not a semantically complete first market result. Python v2 adapter and full data initialization are unmeasured.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/backtest/src/engine.rs:842–905](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L842-L905)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Native execution/replay node versus fitted research campaign

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/backtest/src/engine.rs:842–905](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L842-L905)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Native execution node versus supervised preparation reuse

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/backtest/src/engine.rs:842–905](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L842-L905)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native indicator/actor callback execution

The native engine starts traders and drains callback/data command queues before replaying the event stream.

**Limit:** No common native indicator kernels or aligned array comparisons were run.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/backtest/src/engine.rs:842–905](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L842-L905)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native v2 engine with accounts, actors, data and timers

The pinned event engine is inspectable; no same-contract v2 adapter was admitted.

**Limit:** No timing inherited from v1 releases or claims based only on Rust implementation.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/backtest/src/engine.rs:842–905](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L842-L905)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** One-shot versus streaming native replay

Node supports one-shot load/sort/run and streaming catalog inputs. Aligned chunks preserve equal boundary timestamps; in batch_deltas mode, a per-instrument batcher assembles deltas through F_LAST and rejects unfinished groups.

**Limit:** No event/asset/timer density sweep. Streaming chunk_size is a target, not a hard event-count memory cap.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/backtest/src/node.rs:427–468](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L427-L468); [crates/backtest/src/node.rs:607–641](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L607-L641); [crates/backtest/src/node.rs:460–475](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L460-L475); [crates/backtest/src/node.rs:764–797](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L764-L797)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** One-shot data retention versus aligned stream chunks

One-shot loads all configured data; streaming allocates target-sized chunks then extends through equal timestamps.

**Limit:** A large equal-timestamp group can exceed target chunk_size. Actual full process memory and multi-asset scaling were not measured.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/backtest/src/node.rs:427–468](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L427-L468); [crates/backtest/src/node.rs:607–641](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L607-L641)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Backtest node/config scheduling versus event-loop execution

The engine itself advances ordered data and timers; parallelism must be measured at a declared multi-run layer.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/backtest/src/engine.rs:842–905](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L842-L905); [crates/backtest/src/node.rs:151–179](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L151-L179)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native catalog/replay state reuse

One-shot and streaming use different data-loading/retention paths, with explicit catalog creation per config.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/backtest/src/node.rs:427–469](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L427-L469)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Optional native event store and replay records

The source has a native event-store durability path in addition to backtest execution.

**Limit:** Safety analysis separately inspects canonical hashes and durable commit markers. Recording throughput and crash-recovery time remain unmeasured.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [crates/event_store/src/backend/redb.rs:535–597](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/event_store/src/backend/redb.rs#L535-L597); [crates/event_store/src/backend/redb.rs:823–833](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/event_store/src/backend/redb.rs#L823-L833)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native ts_init replay and callback/timer ordering

Input can be sorted by initialization/availability timestamp; run requires sorted admission. Replay advances clocks before delivering each data item, processes exchange/data queues, and flushes timer/module events at timestamp boundaries.

**Limit:** These are concrete local chronology safeguards, not a proof of arbitrary strategy/indicator information sets. Correct ts_init meaning and complete same-timestamp streaming batches remain caller/data-contract obligations.

**Executable sources:** [crates/backtest/src/engine.rs:420–434](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L420-L434); [crates/backtest/src/engine.rs:760–765](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L760-L765); [crates/backtest/src/engine.rs:907–952](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L907-L952)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Managed ML train/evaluation isolation

The inspected backtest engine constructs and runs configured actors/strategies over admitted timestamped data.

**Limit:** A native supervised train/validation/test owner was not located in the engine/node/analysis surface. Model fitting requires an adapter; this is outside the fixed-signal event-replay contract.

**Executable sources:** [crates/backtest/src/node.rs:162–192](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L162-L192); [crates/backtest/src/engine.rs:907–942](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L907-L942)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Supervised target availability/censoring

Native data replay respects supplied ts_init but does not construct future supervised targets in the inspected engine.

**Limit:** An ML adapter must translate event/label completion and local observation times into target availability rules. Generic event timestamps are not a target censoring protocol.

**Executable sources:** [crates/backtest/src/engine.rs:524–528](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L524-L528); [crates/backtest/src/engine.rs:907–935](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L907-L935)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Purged/nested model validation geometry

Engine run accepts explicit start/end timestamps and node supports whole-run or streaming chunks.

**Limit:** Replay batching and run date ranges are execution geometry, not purged/nested model evaluation. A research adapter must own folds, horizon exclusion and family selection.

**Executable sources:** [crates/backtest/src/engine.rs:701–707](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L701-L707); [crates/backtest/src/node.rs:172–179](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L172-L179)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Fold-fitted transforms/OOF stacking

Configured strategies receive timestamped events through the data engine; no fold-fitted preprocessing/stacking stage was located in this native surface.

**Limit:** Custom estimators may be embedded, but their fitted state and OOF construction require an explicit adapter audit.

**Executable sources:** [crates/backtest/src/engine.rs:924–942](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L924-L942)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Probability calibration and nested thresholds

Native fill models expose execution probabilities with range validation and a seed.

**Limit:** These simulate order execution and are not supervised probability calibration or nested prediction-threshold selection. A learned decision policy needs its own adapter protocol.

**Executable sources:** [crates/execution/src/models/fill.rs:179–204](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/execution/src/models/fill.rs#L179-L204)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native return-source and annualization definitions

Sharpe compounds returns into UTC daily bins, uses sample standard deviation, default252 and NaN for insufficient/near-zero variance. The analyzer prefers resolvable daily portfolio-equity returns and otherwise can retain position-return statistics.

**Limit:** Primary return semantics can change with snapshot/currency/account support; position returns are not interchangeable with portfolio NAV returns. Daily equity calculation fills missing calendar days, so match calendar/return source and denominator explicitly rather than comparing labels alone.

**Executable sources:** [crates/analysis/src/statistics/sharpe_ratio.rs:53–56](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/analysis/src/statistics/sharpe_ratio.rs#L53-L56); [crates/analysis/src/statistics/sharpe_ratio.rs:73–88](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/analysis/src/statistics/sharpe_ratio.rs#L73-L88); [crates/analysis/src/statistic.rs:122–148](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/analysis/src/statistic.rs#L122-L148); [crates/analysis/src/analyzer.rs:283–291](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/analysis/src/analyzer.rs#L283-L291); [crates/analysis/src/analyzer.rs:514–547](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/analysis/src/analyzer.rs#L514-L547); [crates/analysis/src/analyzer.rs:870–876](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/analysis/src/analyzer.rs#L870-L876)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected event-clock, numeric and canonical-output tests

Tests assert same-timestamp timers observe all contemporaneous quotes, exact compounded daily-return examples, finite/undefined Sharpe cases and canonical-result divergence/encoding rejection.

**Limit:** Tests were inspected, not executed in this academic audit. Strong local invariants and serialization checks do not prove all strategy callbacks, fill models or live-market equivalence.

**Executable sources:** [crates/backtest/tests/integration/backtest_engine.rs:5423–5441](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/tests/integration/backtest_engine.rs#L5423-L5441); [crates/analysis/src/statistic.rs:173–187](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/analysis/src/statistic.rs#L173-L187); [crates/analysis/src/statistics/sharpe_ratio.rs:121–149](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/analysis/src/statistics/sharpe_ratio.rs#L121-L149); [crates/backtest/src/result.rs:1393–1457](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/result.rs#L1393-L1457)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Statistical estimator convergence

Native engine run propagates callback/account/module errors, while probabilistic execution models sample configured distributions.

**Limit:** Runtime error propagation is distinct from model-fit convergence. An added estimator must supply conditioning, warning and fit-stability acceptance.

**Executable sources:** [crates/backtest/src/engine.rs:708–738](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L708-L738); [crates/execution/src/models/fill.rs:179–218](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/execution/src/models/fill.rs#L179-L218)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Configured-run results versus complete search history

BacktestResult stores run/config IDs, actual time bounds, iteration/event/order counts and return series; node returns a result for successful configured runs.

**Limit:** With raise_exception disabled, node logs an errored run and skips its result. This is not a durable complete attempted-search family ledger; strategy/model selection history remains external.

**Executable sources:** [crates/backtest/src/result.rs:94–114](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/result.rs#L94-L114); [crates/backtest/src/node.rs:172–192](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L172-L192)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Unknown** · Inspected · applicability `native` · capability `not_located`

**Scope:** Selection-adjusted and dependence-aware inference

The inspected analysis layer supplies marginal return/P&L ratios and optional benchmark-aligned metrics.

**Limit:** No native DSR/PBO, multiple-search-family correction or dependence-aware inferential acceptance protocol was located in the backtest/analysis surface. Seeded fill simulation is not such statistical control.

**Executable sources:** [crates/analysis/src/statistics/sharpe_ratio.rs:73–88](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/analysis/src/statistics/sharpe_ratio.rs#L73-L88); [crates/analysis/src/statistic.rs:93–107](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/analysis/src/statistic.rs#L93-L107)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Canonical result projection and run provenance

The canonical-result type validates a versioned schema, normalization and exact bytes, and provides separate BLAKE3 digest and first-divergence methods. Ordinary results retain run/config/date/count information.

**Limit:** This is substantial native output comparability support. Equal result digests still do not establish identical source, input-market bytes, environments or statistically comparable evaluation protocols; those require an external contract manifest.

**Executable sources:** [crates/backtest/src/result.rs:94–114](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/result.rs#L94-L114); [crates/backtest/src/result.rs:188–222](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/result.rs#L188-L222); [crates/backtest/src/result.rs:1393–1427](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/result.rs#L1393-L1427)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Protected final holdout admission

Node executes configured replay ranges; engine can persist strategy state across managed lifecycle boundaries.

**Limit:** No reserve/freeze/first-access research holdout mechanism was located in the inspected backtest/node/analysis surface. State persistence alone is not a protected final statistical evaluation.

**Executable sources:** [crates/backtest/src/node.rs:162–192](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L162-L192); [crates/backtest/src/engine.rs:701–707](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L701-L707)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Benchmark metrics and execution-model external validity

Native benchmark alignment geometrically compounds daily returns and uses common timestamps; explicit seeded fill probabilities and execution models enable controlled scenarios.

**Limit:** No matched independent market study here validates predictive edge, probability calibration or fill realism. Benchmark timestamps/common support and execution assumptions must be predeclared.

**Executable sources:** [crates/analysis/src/statistic.rs:93–107](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/analysis/src/statistic.rs#L93-L107); [crates/execution/src/models/fill.rs:179–218](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/execution/src/models/fill.rs#L179-L218)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Seeded execution sensitivity and semantic result comparisons

Fill model RNG can be deterministically seeded, run configs can vary assumptions, and canonical result digests/divergence checks support repeatable parity investigations.

**Limit:** These primitives do not force seed ensembles, calibrated model uncertainty, scientific ablations or independent regime tests before reporting a result.

**Executable sources:** [crates/execution/src/models/fill.rs:179–218](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/execution/src/models/fill.rs#L179-L218); [crates/backtest/src/node.rs:172–192](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/node.rs#L172-L192); [crates/backtest/src/result.rs:188–222](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/result.rs#L188-L222); [crates/backtest/src/result.rs:1393–1427](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/result.rs#L1393-L1427)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Importable Python factory/configuration components.

ImportableConfig parses JSON, resolves module:qualified_name via importlib/getattr and constructs the resolved object. JSON export disallows NaN.

**Limit:** The import resolver executes trusted installed components and is not an allowlisted hostile-code sandbox. This row applies to the pinned Rust/Python v2 architecture, not a prior stable Python/Cython release.

**Executable sources:** [python/nautilus_trader/live/config.py:40–108](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/python/nautilus_trader/live/config.py#L40-L108)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Checked quantity construction and native risk admission.

Quantity.new_checked validates representable range/precision. RiskEngine validates order prices/quantities, expiration time and positive configured notional limits before forwarding admitted orders.

**Limit:** The infallible Quantity.new wrapper panics on invalid checked input; binding/direct constructor contracts differ. This is not validation of all trusted Python callbacks, market data or external adapters.

**Executable sources:** [crates/model/src/types/quantity.rs:169–199](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/model/src/types/quantity.rs#L169-L199); [crates/risk/src/engine/config.rs:83–103](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/risk/src/engine/config.rs#L83-L103); [crates/risk/src/engine/mod.rs:1146–1217](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/risk/src/engine/mod.rs#L1146-L1217)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Catalog worker resource budgets and live lifecycle deadlines.

The catalog worker has queue capacity 10 and a 64-open-session limit; live connection/reconciliation code has explicit deadlines, and catalog promotion catches panics into structured errors.

**Limit:** Selected queue/session/deadline bounds do not impose a universal process RAM ceiling or preempt arbitrary strategy/native work. Slow backend operations can still delay synchronous worker calls; no hostile-load stress test was run.

**Executable sources:** [crates/persistence/src/catalog/worker.rs:38–51](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/persistence/src/catalog/worker.rs#L38-L51); [crates/persistence/src/catalog/worker.rs:152–178](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/persistence/src/catalog/worker.rs#L152-L178); [crates/persistence/src/writer/promotion.rs:348–375](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/persistence/src/writer/promotion.rs#L348-L375); [crates/live/src/node/mod.rs:928–961](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/live/src/node/mod.rs#L928-L961)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native Parquet catalog schema admission and configured object stores.

The catalog routes paths through its object-store parser, reads Parquet and validates the catalog schema before constructing target instrument schema/query state.

**Limit:** Schema validation is not authenticity or an exhaustive network/archive/path quota. The bounded review did not establish common timeout/byte/credential guarantees across all object-store and live exchange adapters.

**Executable sources:** [crates/persistence/src/backend/parquet/catalog/query.rs:145–175](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/persistence/src/backend/parquet/catalog/query.rs#L145-L175)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Canonical backtest-result bytes and optional event-store manifest verification.

CanonicalBacktestResult validates schema/normalization and exact canonical serialization, and can compute a BLAKE3 digest. Event-store verification cross-checks manifest progress and indices against recorded entries.

**Limit:** The canonical parser does not receive an expected external digest. A result digest is not a binding of all input/code/environment bytes, and reading a manifest alone does not perform the complete verifier. Full study identity requires an explicit contract.

**Executable sources:** [crates/backtest/src/result.rs:188–222](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/result.rs#L188-L222); [crates/event_store/src/verifier/mod.rs:130–148](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/event_store/src/verifier/mod.rs#L130-L148); [crates/event_store/src/reader/mod.rs:86–108](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/event_store/src/reader/mod.rs#L86-L108)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Configured redb event-store entry reads; separate verifier for broader invariants.

redb scan_seq enforces the durable sequence range, rejects missing slots/decoding failure, checks embedded sequence identity and recomputes each entry hash. The verifier additionally cross-checks indices, snapshots and manifest progress.

**Limit:** Enforcement is scoped to the selected optional event-store backend; live configuration can have no event store. Hashes are not signatures and do not prevent a trusted store owner rewriting both content and hashes. Rust runtime/corruption assertions were not executed by this safety review.

**Executable sources:** [crates/event_store/src/backend/redb.rs:681–708](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/event_store/src/backend/redb.rs#L681-L708); [crates/event_store/src/verifier/mod.rs:130–148](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/event_store/src/verifier/mod.rs#L130-L148); [crates/live/src/node/config.rs:809–825](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/live/src/node/config.rs#L809-L825)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Committed redb event batches and startup reconciliation when configured.

The backend rejects out-of-order batches, writes entries and indices in one transaction with Durability::Immediate, commits before advancing the visible in-memory high-watermark, and validates replay snapshot anchors. Live startup aborts when reconciliation fails before starting the trader.

**Limit:** This is the redb batch frontier, not an atomic transaction with an external exchange, every catalog or arbitrary strategy state. Durability delegates to redb/filesystem behavior; process-kill, power-loss and live reconciliation were not executed here. Event-store/reconciliation configuration matters.

**Executable sources:** [crates/event_store/src/backend/redb.rs:546–607](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/event_store/src/backend/redb.rs#L546-L607); [crates/event_store/src/backend/redb.rs:827–831](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/event_store/src/backend/redb.rs#L827-L831); [crates/event_store/src/reader/mod.rs:142–160](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/event_store/src/reader/mod.rs#L142-L160); [crates/live/src/node/mod.rs:529–545](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/live/src/node/mod.rs#L529-L545)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Catalog worker channels/promotion failures and live startup abort.

The catalog worker keeps a join handle, uses a bounded request channel and maps disconnected replies to errors. Promotion catches panic into a structured failure result; failed live reconciliation aborts startup.

**Limit:** Synchronous reply recv has no universal backend deadline. This evidence does not prove all adapter/strategy panics, shutdown races or worker-kill/resume equivalence; native runtime verification remains separate.

**Executable sources:** [crates/persistence/src/catalog/worker.rs:152–178](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/persistence/src/catalog/worker.rs#L152-L178); [crates/persistence/src/writer/promotion.rs:348–375](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/persistence/src/writer/promotion.rs#L348-L375); [crates/live/src/node/mod.rs:529–545](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/live/src/node/mod.rs#L529-L545)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native strategy order/risk-engine route; full managed research workflow is a separate layer.

The native risk gate validates orders and account exposure. It does not establish a common fitted probability-model output or unavailable-inference contract; that belongs to a model adapter.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [crates/risk/src/engine/mod.rs:587–664](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/risk/src/engine/mod.rs#L587-L664)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Backtest replay driven by data ts_init.

The engine advances its clock from each data item's initialization timestamp, respects the configured end time and stops on shutdown before routing subsequent data to the exchange.

**Limit:** Correct ts_event/ts_init semantics and causal strategy calculations remain prerequisites. A replay clock does not authenticate feed availability, and late/reordered/duplicate source cases require a matched adapter test.

**Executable sources:** [crates/backtest/src/engine.rs:871–931](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/engine.rs#L871-L931)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Default non-bypassed native RiskEngine account/order checks.

The engine checks instrument/order validity, reduce-only constraints, account availability and cumulative reservations before execution. Cash borrowing is an explicit account property; exposure checks use selected account models.

**Limit:** RiskEngine bypass immediately forwards commands and skips this gate, including trading-state restrictions. The guarantee is conditional on routing through the enabled native risk engine and correct adapter/account state, not a universal live loss bound.

**Executable sources:** [crates/risk/src/engine/mod.rs:587–664](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/risk/src/engine/mod.rs#L587-L664); [crates/risk/src/engine/mod.rs:1375–1445](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/risk/src/engine/mod.rs#L1375-L1445); [crates/risk/src/engine/mod.rs:1067–1081](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/risk/src/engine/mod.rs#L1067-L1081)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Selected native stop-order and market-fill implementation paths.

Already-triggered stop orders are rejected or executed according to reject_stop_orders. Market fills cancel a reduce-only order with no reducing position, stop on a fill-model error and filter fills when a protection price is available. The native fill model validates its probability parameters and accepts an explicit random seed.

**Limit:** Trigger-price versus market-price behavior depends on book/model configuration. These inspected paths do not establish identical bar, tick, queue, stochastic or contingent-order outcomes, and a simulated protection threshold is not a guaranteed live fill.

**Executable sources:** [crates/execution/src/matching_engine/mod.rs:3960–4030](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/execution/src/matching_engine/mod.rs#L3960-L4030); [crates/execution/src/matching_engine/mod.rs:4822–4877](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/execution/src/matching_engine/mod.rs#L4822-L4877); [crates/execution/src/models/fill.rs:180–218](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/execution/src/models/fill.rs#L180-L218)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**Unknown** · Inspected · applicability `unknown` · capability `not_located`

**Scope:** Protected research holdout admission at the pinned Rust/Python architecture.

No protected holdout reservation/exposure ledger was located in the bounded research/replay inspection. Event-store hashes and account reservations serve different contracts.

**Limit:** The bounded inspection did not establish enforcement or prove repository-wide absence. Require an implementation pointer and executable acceptance results before treating this capability as present.

**Executable sources:** [crates/event_store/src/verifier/mod.rs:130–148](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/event_store/src/verifier/mod.rs#L130-L148); [crates/backtest/src/result.rs:188–222](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/backtest/src/result.rs#L188-L222)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Executable security/supply-chain CI at the pinned source.

Security CI uses pinned action commits, installs versioned audit tools and invokes a supply-chain audit script. CodeQL and Rust audit/deny commands are separately configured in the repository workflows.

**Limit:** Source configuration is not successful hosted enforcement, an audited released wheel or exact source-to-binary identity. The pinned release candidate requires its own recent Python/Rust toolchain and must not inherit prior stable-version assurance.

**Executable sources:** [.github/workflows/security-audit.yml:199–251](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/.github/workflows/security-audit.yml#L199-L251); [.github/workflows/build.yml:885–910](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/.github/workflows/build.yml#L885-L910); [.github/workflows/build.yml:1082–1092](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/.github/workflows/build.yml#L1082-L1092)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native numeric property tests and event corruption assertions.

Property tests compare fixed-scale ordering against independent wide-integer arithmetic; verifier tests mutate payload bytes and assert a hash-mismatch finding while scanning later entries.

**Limit:** These assertions were inspected only in this safety campaign. They substantiate targeted coverage, not universal parser/adapter, live concurrency or mutation completeness.

**Executable sources:** [crates/model/tests/fixed_scale.rs:334–370](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/model/tests/fixed_scale.rs#L334-L370); [crates/event_store/src/verifier/mod.rs:701–724](https://github.com/nautechsystems/nautilus_trader/blob/42c3ca5f8f8d537f69772277e77792bb5b307ea5/crates/event_store/src/verifier/mod.rs#L701-L724)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

