# Zipline-reloaded

**Frozen source:** [stefan-jansen/zipline-reloaded @ cf649ac06fddce76f6caa2403cd8494ac84f72ad](https://github.com/stefan-jansen/zipline-reloaded/tree/cf649ac06fddce76f6caa2403cd8494ac84f72ad)

**Observed license label:** Apache-2.0  
**Layer:** Calendar/asset-aware algorithm engine and Pipeline factors

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Pinned zipline-reloaded source builds/imports; no matching native hourly calendar/bundle adapter was admitted for this campaign.

**Academic:** Substantial point-in-time pricing/event-loader machinery and local rolling estimators; model-selection folds and final holdout governance require another layer.

**Safety:** Native CSV/tar ingestion checks and optional trading controls; control registration, log-versus-raise behavior and provider ownership matter.

## P01

### Parameter-space construction and retained memory

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** TradingAlgorithm/Pipeline versus parameter-space generation

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [src/zipline/gens/tradesimulation.py:118–159](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L118-L159); [src/zipline/gens/tradesimulation.py:223–262](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L223-L262)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** One native algorithm simulation versus search-family generation

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [src/zipline/gens/tradesimulation.py:118–159](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L118-L159); [src/zipline/gens/tradesimulation.py:223–262](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L223-L262)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Source-built zipline-reloaded import and algorithm/bundle initialization

The pinned source built and imported; full native runs require a declared asset/calendar/data bundle contract.

**Limit:** Source build/import checks are not a semantically complete first backtest result.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [src/zipline/algorithm.py:2252–2269](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/algorithm.py#L2252-L2269); [src/zipline/gens/tradesimulation.py:118–159](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L118-L159); [src/zipline/gens/tradesimulation.py:223–262](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L223-L262)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** TradingAlgorithm plus Pipeline versus fitted research campaign

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [src/zipline/gens/tradesimulation.py:118–159](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L118-L159); [src/zipline/gens/tradesimulation.py:223–262](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L223-L262)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**Partial** · Inspected · applicability `native` · capability `unknown`

**Scope:** Fitted preparation/prediction reuse, distinguished from adjacent raw or deterministic computation reuse

Pipeline computes terms and caches output blocks by date; this is reusable feature computation.

**Limit:** The cited adjacent data/processing mechanism does not establish a fitted-state or prediction-reuse cache. It does not establish a common supervised fit/transform/model/prediction cache contract. No fitted-work ablation was run.

**Measurement state:** Not measured in this criterion scope

**Distinct sub-capabilities:** fitted_state_or_prediction_reuse_in_inspected_path: Unknown; no fitted-reuse speedup inferred; adjacent_input_or_deterministic_reuse: Implemented as described in finding; not the canonical fitted capability

**Executable sources:** [src/zipline/pipeline/engine.py:566–625](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/engine.py#L566-L625); [src/zipline/algorithm.py:2252–2269](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/algorithm.py#L2252-L2269)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Pipeline term graph and chunk execution

SimplePipelineEngine evaluates a dependency graph in chunked date/asset workspaces.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [src/zipline/pipeline/engine.py:271–333](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/engine.py#L271-L333); [src/zipline/pipeline/engine.py:566–625](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/engine.py#L566-L625)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Full native algorithm/calendar/data-portal simulation

Native bar events process previous orders/transactions/commissions before handle_data, with session-end reporting.

**Limit:** No honest sparse-hourly-to-native calendar adapter was admitted in this campaign. No timing or inference from another Zipline fork/version.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [src/zipline/gens/tradesimulation.py:118–159](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L118-L159); [src/zipline/gens/tradesimulation.py:223–262](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L223-L262)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native BAR/SESSION/MINUTE events and account metrics

The simulator handles bar, session-start/end, before-trading-start and minute-end actions and asset auto-close.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [src/zipline/gens/tradesimulation.py:118–159](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L118-L159); [src/zipline/gens/tradesimulation.py:223–262](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L223-L262); [src/zipline/gens/tradesimulation.py:281–295](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L281-L295)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Pipeline workspace, history, assets and metrics output

Pipeline computes chunked terms while TradingAlgorithm stores cached result windows.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [src/zipline/pipeline/engine.py:271–333](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/engine.py#L271-L333); [src/zipline/algorithm.py:2252–2269](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/algorithm.py#L2252-L2269)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** One TradingAlgorithm simulation versus parallel model-search scheduling

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [src/zipline/gens/tradesimulation.py:118–159](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L118-L159); [src/zipline/gens/tradesimulation.py:223–262](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L223-L262)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Date-valid Pipeline output cache and chunking

A cache miss runs the next Pipeline block and stores it until valid_until; each daily access selects that day from the cache.

**Limit:** No hit/miss/cold-memory or invalidation benchmark. Cached Pipeline blocks are not a scientific holdout boundary.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [src/zipline/algorithm.py:2252–2275](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/algorithm.py#L2252-L2275)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native result recording, separately from research checkpoint/resume

The native run wrapper can serialize the resulting performance frame using to_pickle.

**Limit:** Native result-write overhead is unmeasured. Crash-safe continuation and an exact multi-round durable commit frontier are not established by these serialization paths.

**Measurement state:** Not measured in this criterion scope

**Distinct sub-capabilities:** native_recording: Implemented; complete_checkpoint_continuation: Unknown/not located in the cited result-write path

**Executable sources:** [src/zipline/utils/run_algo.py:244–247](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/utils/run_algo.py#L244-L247)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native equity/event Pipeline and bar callback chronology

Equity pricing loader shifts daily OHLCV requests back one trading session and supplies adjustment-aware arrays. Event loaders admit next events only after knowledge timestamps and previous events after max(event date, knowledge time). Bar simulation processes existing orders before calling handle_data.

**Limit:** These are substantial native point-in-time primitives. Custom loaders/factors/external data remain trusted; supplied knowledge timestamps and corporate-action adjustments require validation. They do not prove all user predictors causal.

**Executable sources:** [src/zipline/pipeline/loaders/equity_pricing_loader.py:79–115](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/loaders/equity_pricing_loader.py#L79-L115); [src/zipline/pipeline/loaders/utils.py:57–78](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/loaders/utils.py#L57-L78); [src/zipline/pipeline/loaders/utils.py:115–140](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/loaders/utils.py#L115-L140); [src/zipline/gens/tradesimulation.py:115–141](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L115-L141)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Window-local Pipeline statistical factors

CustomFactor consumes the next window for each date; native rolling regression fits each supplied historical window and exposes coefficient/statistic outputs.

**Limit:** This local estimation boundary is not a managed supervised train/validation/test pipeline. Factor parameters, feature fitting outside Pipeline and full strategy selection still need an explicit research adapter.

**Executable sources:** [src/zipline/pipeline/mixins.py:190–226](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/mixins.py#L190-L226); [src/zipline/pipeline/factors/statistical.py:175–205](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/factors/statistical.py#L175-L205)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Supervised target horizon/censoring

Native event knowledge cutoffs and lagged pricing define observable predictor inputs, while rolling regressions fit supplied contemporaneous windows.

**Limit:** A future supervised label availability/censoring protocol was not located in these Pipeline/run surfaces. Event knowledge time is useful input infrastructure, not automatic label purging.

**Executable sources:** [src/zipline/pipeline/loaders/utils.py:115–140](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/loaders/utils.py#L115-L140); [src/zipline/pipeline/factors/statistical.py:175–205](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/factors/statistical.py#L175-L205)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Rolling factor window geometry versus research folds

Native regression length must be at least2 and defines the input window; Pipeline can compute the same requested date range in chunks.

**Limit:** Rolling estimation and chunked execution do not create purged/nested independent evaluation folds. A model-selection adapter must own train/test geometry and outcome horizon exclusions.

**Executable sources:** [src/zipline/pipeline/factors/statistical.py:177–188](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/factors/statistical.py#L177-L188); [src/zipline/pipeline/engine.py:314–332](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/engine.py#L314-L332)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Window-local factor transforms and adjustment-aware data

Pipeline formats each date's masked input window, and rolling regression derives its estimates from that window; pricing loaders attach dated corporate-action adjustments.

**Limit:** No general fold-fitted preprocessing/OOF stacking manager was located in these surfaces. Custom stateful factors must be checked for correct reset/reuse across chunks and independent evaluation.

**Executable sources:** [src/zipline/pipeline/mixins.py:190–226](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/mixins.py#L190-L226); [src/zipline/pipeline/factors/statistical.py:190–205](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/factors/statistical.py#L190-L205); [src/zipline/pipeline/loaders/equity_pricing_loader.py:103–115](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/loaders/equity_pricing_loader.py#L103-L115)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Probability calibration/nested decision thresholds

Pipeline returns factor values and statistical regression outputs for strategy callbacks.

**Limit:** A native supervised calibration/nested threshold-selection workflow was not located in this factor/runner surface. Add a model adapter for comparable decision-policy research.

**Executable sources:** [src/zipline/pipeline/factors/statistical.py:175–205](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/factors/statistical.py#L175-L205); [src/zipline/gens/tradesimulation.py:141–150](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L141-L150)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native daily-return wrappers and delegated empyrical metrics

ReturnsStatistic evaluates only daily returns through the current session and maps nonfinite scalars to None. Native metric registration delegates Sharpe/Sortino/drawdown to empyrical; period reports mask benchmark dates and convert NaN Sharpe to0.

**Limit:** Dependency formulas are bounded by empyrical-reloaded>=0.5.7 in this source audit, not an independently inspected exact dependency revision. Cumulative versus period missing-value conventions differ, so common raw return metrics should define them explicitly.

**Executable sources:** [src/zipline/finance/metrics/metric.py:299–310](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/metrics/metric.py#L299-L310); [src/zipline/finance/metrics/__init__.py:85–87](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/metrics/__init__.py#L85-L87); [src/zipline/finance/metrics/metric.py:474–506](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/metrics/metric.py#L474-L506); [pyproject.toml:48–48](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/pyproject.toml#L48-L48)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected point-in-time, adjustment and chunk tests

Tests compare Pipeline output to expected asset/date values across chunk schedules, explicitly check event eligibility against knowledge/event dates, and compare adjustment-aware windows with separately constructed expected adjusted arrays.

**Limit:** Tests were inspected, not executed in this academic audit. They substantiate specific temporal/adjustment semantics but do not establish every data vendor/factor or independent fill-model validity.

**Executable sources:** [tests/pipeline/test_pipeline_algo.py:307–332](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/tests/pipeline/test_pipeline_algo.py#L307-L332); [tests/pipeline/test_events.py:201–227](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/tests/pipeline/test_events.py#L201-L227); [tests/pipeline/test_us_equity_pricing_loader.py:650–679](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/tests/pipeline/test_us_equity_pricing_loader.py#L650-L679)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Managed iterative estimator convergence

Native rolling linear regression delegates each supplied window to scipy.stats.linregress and exposes standard errors and related statistics.

**Limit:** No general fitted-model convergence/conditioning acceptance owner was located in the inspected Pipeline/runner surface. Closed-form regression output is not evidence of arbitrary model convergence.

**Executable sources:** [src/zipline/pipeline/factors/statistical.py:190–205](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/factors/statistical.py#L190-L205)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Complete parameter/search-family ledger

The native run utility executes one algorithm against a selected bundle and can serialize its performance frame.

**Limit:** A managed complete strategy/parameter search ledger was not located in these run/Pipeline surfaces. An external experiment adapter must retain failed, discarded and repeated attempts.

**Executable sources:** [src/zipline/utils/run_algo.py:93–109](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/utils/run_algo.py#L93-L109); [src/zipline/utils/run_algo.py:244–247](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/utils/run_algo.py#L244-L247)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native rolling-regression significance output

RollingLinearRegression exposes slope/intercept/r-value/p-value/stderr from SciPy for each window.

**Limit:** These are marginal regression statistics, not post-strategy-selection inference. No overlapping-window/serial-dependence or multiple-family correction is applied in this factor, and native headline return metrics do not add such a protocol.

**Executable sources:** [src/zipline/pipeline/factors/statistical.py:175–205](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/factors/statistical.py#L175-L205); [src/zipline/finance/metrics/__init__.py:85–87](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/metrics/__init__.py#L85-L87)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Bundle vintage and dated performance outputs

run_algo accepts a bundle timestamp; bundle loading selects an ingestion on or before that cutoff. Performance output can be serialized, and Pipeline loaders preserve calendar/adjustment semantics.

**Limit:** An ingestion timestamp is a useful reproducibility selector, not an immutable input-byte/source/environment manifest. Native default bundle time can float, and output pickle alone does not enforce experimental comparability.

**Executable sources:** [src/zipline/utils/run_algo.py:93–97](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/utils/run_algo.py#L93-L97); [src/zipline/data/bundles/core.py:510–524](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/data/bundles/core.py#L510-L524); [src/zipline/data/bundles/core.py:557–559](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/data/bundles/core.py#L557-L559); [src/zipline/utils/run_algo.py:244–247](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/utils/run_algo.py#L244-L247)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Protected final holdout admission

The native run utility accepts requested simulation dates and bundle vintage; Pipeline computes selected date ranges.

**Limit:** No model freeze/reservation/first-access final holdout mechanism was located in this surface. A separate research adapter must own final evaluation rather than relying on simulation dates alone.

**Executable sources:** [src/zipline/utils/run_algo.py:93–109](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/utils/run_algo.py#L93-L109); [src/zipline/pipeline/engine.py:314–332](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/engine.py#L314-L332)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Benchmark-relative analysis and external validity

Native metrics compare algorithm and benchmark returns on matched report dates; pricing/event loaders support point-in-time input treatment.

**Limit:** No matched independent experiment here establishes predictive/economic edge or live-fill realism. Universe survivorship, data-vintage truth, benchmark support, costs and execution timing remain part of the research contract.

**Executable sources:** [src/zipline/finance/metrics/metric.py:474–506](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/metrics/metric.py#L474-L506); [src/zipline/pipeline/loaders/equity_pricing_loader.py:79–115](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/loaders/equity_pricing_loader.py#L79-L115)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Window/chunk/calendar/adjustment sensitivity primitives

Regression windows and Pipeline chunk sizes can vary, with native tests exercising randomized chunk schedules and corporate-action adjustment windows.

**Limit:** These are optional parameter/implementation checks. The inspected runner does not require model ablations, seed ensembles, parameter plateaus or independent regime replication before reporting a result.

**Executable sources:** [src/zipline/pipeline/factors/statistical.py:177–188](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/factors/statistical.py#L177-L188); [src/zipline/pipeline/engine.py:314–332](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/pipeline/engine.py#L314-L332); [tests/pipeline/test_pipeline_algo.py:307–332](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/tests/pipeline/test_pipeline_algo.py#L307-L332); [tests/pipeline/test_us_equity_pricing_loader.py:650–679](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/tests/pipeline/test_us_equity_pricing_loader.py#L650-L679)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Trusted Python extension and object-cache routes.

The CLI extension path executes supplied .py source or imports a module. The DataFrame cache can load pickle objects.

**Limit:** These are trusted local extension/artifact surfaces, not a constrained hostile-config sandbox. No remote exposure is inferred from their existence.

**Executable sources:** [src/zipline/utils/run_algo.py:276–293](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/utils/run_algo.py#L276-L293); [src/zipline/utils/cache.py:204–278](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/utils/cache.py#L204-L278)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native trading controls and blotter input checks.

Orders pass registered trading controls; the simulation blotter ignores zero quantity and checks its maximum-share parameter. Optional control constructors validate some bounds.

**Limit:** The inspected paths do not form a universal finite-value/OHLC schema gate. Control behavior depends on registration and on_error mode; arbitrary extension/custom model inputs remain caller-owned.

**Executable sources:** [src/zipline/algorithm.py:1314–1321](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/algorithm.py#L1314-L1321); [src/zipline/finance/blotter/simulation_blotter.py:98–145](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/blotter/simulation_blotter.py#L98-L145); [src/zipline/finance/controls.py:147–183](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/controls.py#L147-L183)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Selected CSV fetch and finite event loop.

RequestsCSV uses a fixed request timeout and streaming document-size check; the engine iterates a bounded simulation clock.

**Limit:** The CSV check can overshoot by a received chunk and does not cap every bundle downloader. Arbitrary Python algorithm runtime, full-data memory and parallel experiments have no established common quota here.

**Executable sources:** [src/zipline/sources/requests_csv.py:105–131](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/sources/requests_csv.py#L105-L131); [src/zipline/sources/requests_csv.py:547–563](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/sources/requests_csv.py#L547-L563); [src/zipline/gens/tradesimulation.py:223–249](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L223-L249)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native RequestsCSV and quantopian-quandl bundle ingestion.

RequestsCSV forces streaming, disables redirects, imposes a timeout and checks document size. Tar-bundle extraction requires Python's data_filter and invokes extractall(filter='data').

**Limit:** That is a positive extraction boundary, not a content-authenticity or global decompression quota. The separate bundle downloader does not inherit every RequestsCSV limit, and other providers require separate inspection.

**Executable sources:** [src/zipline/sources/requests_csv.py:105–131](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/sources/requests_csv.py#L105-L131); [src/zipline/sources/requests_csv.py:547–563](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/sources/requests_csv.py#L547-L563); [src/zipline/data/bundles/quandl.py:294–318](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/data/bundles/quandl.py#L294-L318)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native algorithm/bundle/cache execution; full managed research workflow is a separate layer.

The selected algorithm and cache route is not a content-addressed managed-study manifest. Bundle version selection and a pickle cache are distinct from recomputing an expected study digest.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [src/zipline/gens/tradesimulation.py:109–150](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L109-L150); [src/zipline/utils/cache.py:204–278](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/utils/cache.py#L204-L278)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**Partial** · Inspected · applicability `adapter_required` · capability `implemented`

**Scope:** Native DataFrame cache serialized reads/writes.

The cache serializes entries with pickle by default and can delete temporary cache contents on failure.

**Limit:** This path does not verify a research-round digest/reference graph; pickle requires trusted files. Cache cleanup does not prove corruption-preserving or fail-closed whole-run admission.

**Executable sources:** [src/zipline/utils/cache.py:204–278](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/utils/cache.py#L204-L278)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native in-memory algorithm/blotter state; full managed research workflow is a separate layer.

The selected simulation updates in-memory orders and metrics. Its native event loop is not a durable completed-research-round restart transaction; bundle/cache persistence has a separate contract.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [src/zipline/finance/blotter/simulation_blotter.py:45–76](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/blotter/simulation_blotter.py#L45-L76); [src/zipline/gens/tradesimulation.py:109–150](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L109-L150)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native single algorithm simulation loop; full managed research workflow is a separate layer.

The selected algorithm loop is sequential. Multiworker experiment dispatch and recovery require an external executor.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [src/zipline/gens/tradesimulation.py:223–249](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L223-L249)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**N/A** · Inspected · applicability `out_of_scope` · capability `not_implemented`

**Scope:** Selected native algorithm callbacks and order controls; full managed research workflow is a separate layer.

The native route accepts algorithm orders, not a common fitted-model probability schema. Optional controls do not establish unavailable-prediction semantics.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [src/zipline/algorithm.py:1314–1321](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/algorithm.py#L1314-L1321)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Simulation clock, fill processing and algorithm callback order.

Each bar advances the algorithm clock, processes existing blotter transactions/commissions and then calls handle_data. This gives a concrete default order-to-next-processing-step sequence.

**Limit:** Trusted Python extensions/models can obtain external information; the loop does not authenticate source timestamps or prove causal feature construction. Trading controls and data portal semantics must be matched separately.

**Executable sources:** [src/zipline/gens/tradesimulation.py:109–150](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L109-L150)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Registered native position/order/leverage controls.

The engine supports maximum order count/size, position size, long-only and leverage controls, with validation call sites in the algorithm.

**Limit:** Controls must be registered. on_error='log' reports without raising, and default blotter execution is not a universal cash-only affordability policy. Exposure and pending-order semantics require a matched configured contract.

**Executable sources:** [src/zipline/finance/controls.py:67–116](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/controls.py#L67-L116); [src/zipline/finance/controls.py:191–249](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/controls.py#L191-L249); [src/zipline/finance/controls.py:324–340](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/controls.py#L324-L340); [src/zipline/algorithm.py:1974–2026](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/algorithm.py#L1974-L2026)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native slippage and order-limit models.

Optional VolumeShareSlippage clips by volume share, accounts for volume already consumed and changes fill price with volume-dependent impact. The default equity blotter model is FixedBasisPointsSlippage.

**Limit:** Model choice changes fill eligibility and costs. Volume-share simulation is not an observed queue or a general endogenous order-book response; candidate comparisons must hold these assumptions fixed.

**Executable sources:** [src/zipline/finance/blotter/simulation_blotter.py:45–76](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/blotter/simulation_blotter.py#L45-L76); [src/zipline/finance/slippage.py:267–331](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/finance/slippage.py#L267-L331)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native algorithm/bundle backtest; full managed research workflow is a separate layer.

This fixed execution path does not implement the managed research contract measured by this criterion.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [src/zipline/gens/tradesimulation.py:109–150](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/src/zipline/gens/tradesimulation.py#L109-L150)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Checked-in quick CI workflow.

The workflow runs lint and tox/pytest with bounded retry attempts and per-attempt timeout across OS targets.

**Limit:** Action tags and installed dependencies are not a hash-closed supply chain in this path. Hosted execution, audit coverage and branch protection were not checked.

**Executable sources:** [.github/workflows/ci_tests_quick.yml:17–89](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/.github/workflows/ci_tests_quick.yml#L17-L89)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected slippage boundary and cache-expiry assertions.

Tests assert separate volume-constrained fills for multiple orders, reject negative basis points and zero volume limit, and reject expired cache keys. CI has an executable test command.

**Limit:** Those assertions were inspected, not run by this safety campaign. No numeric attack-case count or fuzz/mutation score is claimed; source-time, margin, file corruption and worker-kill tests remain to run on the selected adapter.

**Executable sources:** [tests/finance/test_slippage.py:1339–1372](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/tests/finance/test_slippage.py#L1339-L1372); [tests/utils/test_cache.py:41–61](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/tests/utils/test_cache.py#L41-L61); [.github/workflows/ci_tests_quick.yml:82–89](https://github.com/stefan-jansen/zipline-reloaded/blob/cf649ac06fddce76f6caa2403cd8494ac84f72ad/.github/workflows/ci_tests_quick.yml#L82-L89)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

