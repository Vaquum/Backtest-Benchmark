# Jesse

**Frozen source:** [jesse-ai/jesse @ 4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae](https://github.com/jesse-ai/jesse/tree/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae)

**Observed license label:** MIT  
**Layer:** Crypto minute replay, optimization and research helpers

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Pinned Python source and declared native dependency import; Ray candle sharing and Rust kernels are inspected, with no relabelled-hourly minute benchmark.

**Academic:** Separate training/testing metrics and optional stationary-bootstrap rule testing; exposed testing feedback is not a protected final holdout or full search-family correction.

**Safety:** Native account and operational controls have explicit limits; strategy/module paths, pickle cache ownership and dashboard-versus-research persistence are separate scopes.

## P01

### Parameter-space construction and retained memory

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native random optimizer proposals and active Ray tasks

Research optimization samples trial parameters as tasks are launched and keeps a bounded number of active references; full training/testing candle arrays are placed in Ray shared storage.

**Limit:** No parameter-family construction-memory sweep. This is random search, not the same accepted sequence as Grid/Sobol.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [jesse/research/optimize/__init__.py:39–70](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/optimize/__init__.py#L39-L70); [jesse/research/optimize/__init__.py:237–281](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/optimize/__init__.py#L237-L281)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native trial generation/collection

The optimizer repeatedly generates parameters and launches up to its active-reference limit until the trial budget is consumed.

**Limit:** No measured duplicate-family occupancy or guaranteed exhaustive enumeration; proposals and completed valid trials must be counted separately.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [jesse/research/optimize/__init__.py:237–281](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/optimize/__init__.py#L237-L281)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Source-built Python plus native jesse-rust runtime and complete simulator setup

The exact source imports in an isolated environment; native observed-minute and dense-minute replay paths are distinct.

**Limit:** No matching recorded one-minute workload was admitted. No hourly prices are relabeled as one-minute observations to obtain a timing.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [jesse/modes/backtest_mode.py:541–570](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L541-L570); [jesse/modes/backtest_mode.py:1887–1926](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L1887-L1926)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native optimization over training/testing windows and Ray workers

Research and dashboard optimization share candle objects and invoke parallel trial evaluation; dashboard persists study trials while research retains selected results.

**Limit:** No matched full research campaign timing; default/fast modes and tested versus training score scope must be fixed first.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [jesse/research/optimize/__init__.py:237–281](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/optimize/__init__.py#L237-L281); [jesse/modes/optimize_mode/Optimize.py:480–562](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/Optimize.py#L480-L562)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**Partial** · Inspected · applicability `native` · capability `unknown`

**Scope:** Fitted preparation/prediction reuse, distinguished from adjacent raw or deterministic computation reuse

The optimizer puts training/testing and warmup candle arrays in Ray once, then passes object references to workers.

**Limit:** The cited adjacent data/processing mechanism does not establish a fitted-state or prediction-reuse cache. This is data sharing, not demonstrated fold-fitted scaler/model/prediction reuse. No fitted-reuse ablation.

**Measurement state:** Not measured in this criterion scope

**Distinct sub-capabilities:** fitted_state_or_prediction_reuse_in_inspected_path: Unknown; no fitted-reuse speedup inferred; adjacent_input_or_deterministic_reuse: Implemented as described in finding; not the canonical fitted capability

**Executable sources:** [jesse/research/optimize/__init__.py:250–264](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/optimize/__init__.py#L250-L264); [jesse/modes/optimize_mode/Optimize.py:499–509](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/Optimize.py#L499-L509)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native Rust candle aggregation and indicator delegation

A bounded contiguous float64 aggregation path calls the imported Rust candle kernel; other cases use NumPy aggregation.

**Limit:** No matched native indicator/candle kernel comparison. The separate public jesse-rust source version corresponds to the dependency, but wheel-to-commit binary equivalence is not independently proven.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [jesse/modes/backtest_mode.py:2047–2068](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L2047-L2068); [jesse/indicators/sma.py:29–39](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/indicators/sma.py#L29-L39)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native full/fast and observed-timestamp minute replay

The dispatcher chooses dense/timestamp replay and fast mode; the skip loop aggregates source candle steps before native order simulation.

**Limit:** Not admitted to the common hourly close contract. Different sampled balance cadence or aggregated intrabar paths cannot be timed as if they returned an identical equity/fill tape.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [jesse/modes/backtest_mode.py:541–570](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L541-L570); [jesse/modes/backtest_mode.py:1887–1926](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L1887-L1926)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Dense minute stepping versus observed-timestamp replay and fast batching

Noncontiguous or unequal source timelines select timestamp handling; fast mode can batch source rows when pipelines allow it.

**Limit:** No event-density/fast-mode full ledger parity or timing experiment. Code comments about speed are not evidence.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [jesse/modes/backtest_mode.py:541–570](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L541-L570); [jesse/modes/backtest_mode.py:941–969](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L941-L969); [jesse/modes/backtest_mode.py:1897–1921](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L1897-L1921)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Candle store preallocation and Ray object/reference retention

The simulator can grow numeric candle storage; optimization retains shared training/testing arrays and active task references.

**Limit:** Actual process-tree/sharing memory and deep strategy/Rust allocations are unmeasured.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [jesse/modes/backtest_mode.py:1120–1155](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L1120-L1155); [jesse/research/optimize/__init__.py:237–281](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/optimize/__init__.py#L237-L281)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Ray task dispatch with one CPU per trial

The native optimizer caps active references at min(2*cores,remaining trials), submits per-trial one-CPU tasks, then waits for completed tasks.

**Limit:** No worker-scaling or model-result parity campaign. The scheduler setting alone does not establish speedup.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [jesse/modes/optimize_mode/Optimize.py:509–562](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/Optimize.py#L509-L562)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Persistent pickle cache and per-method lru_cache

Cache records keyed payloads and expiration metadata; cache hits renew expiry; method wrappers use lru_cache.

**Limit:** No cache hit-cost/invalidation/scaling benchmark. Expiration metadata is not a verified input/model content address.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [jesse/services/cache.py:31–97](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/cache.py#L31-L97); [jesse/services/cache.py:121–129](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/cache.py#L121-L129)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Dashboard Optuna SQLite and resumed trial counters

The dashboard optimizer creates persisted study storage and can load prior trial state before dispatching remaining work.

**Limit:** Research helper persistence differs. No controlled crash boundary, durable-prefix equivalence or recording latency measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [jesse/modes/optimize_mode/Optimize.py:113–159](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/Optimize.py#L113-L159); [jesse/modes/optimize_mode/Optimize.py:480–509](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/Optimize.py#L480-L509)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Timestamp replay and shipped indicator recurrences

Timestamp replay applies the current event before executing only routes updated by it. The inspected Rust SMA and EMA bodies consume backward windows/recurrences.

**Limit:** This scopes native event delivery and two indicator implementations; it does not prove arbitrary strategy callbacks or every indicator causal. Native Python wrappers depend on jesse-rust; matching source version is pinned separately, but wheel/source binary identity was not established.

**Executable sources:** [jesse/modes/backtest_mode.py:987–1014](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L987-L1014); [src/moving_averages.rs:108–139](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/src/moving_averages.rs#L108-L139); [src/moving_averages.rs:350–382](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/src/moving_averages.rs#L350-L382)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Optimization training/testing backtests

Fitness runs separate training and testing backtests; the returned optimization score is computed from training metrics only.

**Limit:** Caller-supplied dates/candle dictionaries determine separation; the inspected date loader does not establish that the two windows are disjoint. Testing metrics are exposed for each eligible candidate, allowing human selection on them.

**Executable sources:** [jesse/modes/optimize_mode/fitness.py:39–49](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/fitness.py#L39-L49); [jesse/modes/optimize_mode/fitness.py:91–116](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/fitness.py#L91-L116); [jesse/modes/optimize_mode/__init__.py:156–174](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/__init__.py#L156-L174)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native rule-significance next-bar response

Rule significance aligns signal at t with log return from close t to close t+1 and drops the final signal without a next return.

**Limit:** This validates the response alignment in this diagnostic only. Native general ML target censoring/availability contracts were not located in the inspected strategy optimization path; an ML adapter must supply them.

**Executable sources:** [jesse/research/rule_significance_testing/rule_significance.py:144–173](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/rule_significance_testing/rule_significance.py#L144-L173)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native optimization windows

Training and testing periods have explicit separate start/end dates and their own warmup candles.

**Limit:** No purge, embargo, nested fold generator or automatic overlap rejection was located in the inspected optimization date loader/research API. Reusing a testing window across trials does not create independent final evidence.

**Executable sources:** [jesse/modes/optimize_mode/__init__.py:156–174](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/__init__.py#L156-L174); [jesse/research/optimize/__init__.py:163–220](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/optimize/__init__.py#L163-L220)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** ML preprocessing/stacking adapter

The native optimization path passes strategy hyperparameters and separately supplied candle sets into isolated backtests; it does not supply a general fold-fitted feature/stacking pipeline in the inspected surface.

**Limit:** For the execution track this is outside the native contract. Compare preprocessing leakage only after an ML adapter defines fit and transform ownership.

**Executable sources:** [jesse/modes/optimize_mode/fitness.py:28–49](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/fitness.py#L28-L49)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Strategy parameter selection; no probability calibration contract

The native optimizer selects on a training objective while separately calculating testing metrics for eligible candidates.

**Limit:** Testing outcomes remain visible during search. Probability calibration, threshold nesting and a final untouched calibration assessment were not located in this optimization path.

**Executable sources:** [jesse/modes/optimize_mode/fitness.py:51–103](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/fitness.py#L51-L103); [jesse/modes/optimize_mode/Optimize.py:440–461](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/Optimize.py#L440-L461)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native daily-balance and rule-significance metrics

Sharpe uses sample standard deviation and an explicit default 365 observations/year; smart Sharpe applies a lag-one autocorrelation-derived penalty. CAGR/Calmar are withheld when timestamps are unavailable. The significance diagnostic reports detrended signed next-bar returns.

**Limit:** The significance response is not realized net strategy P&L. Observation annualization, timestamp support, undefined metrics and the assumed autocorrelation model must be aligned before comparing native headline ratios.

**Executable sources:** [jesse/services/metrics.py:71–121](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/metrics.py#L71-L121); [jesse/services/metrics.py:418–436](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/metrics.py#L418-L436); [jesse/research/rule_significance_testing/rule_significance.py:183–189](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/rule_significance_testing/rule_significance.py#L183-L189)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected numerical, alignment and isolation tests

Indicator tests assert fixed expected values and sequential/scalar agreement; rule-significance tests assert next-bar alignment, seeded batch-count invariance and runtime cleanup. Public Rust indicator source is available at a separately pinned revision.

**Limit:** Tests were inspected, not executed for this assessment. Same-code scalar/vector agreement is not an independent financial oracle; matching Rust dependency version alone does not prove installed binary identity.

**Executable sources:** [tests/test_indicators.py:11–32](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/tests/test_indicators.py#L11-L32); [tests/test_rule_significance_testing.py:239–282](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/tests/test_rule_significance_testing.py#L239-L282); [src/moving_averages.rs:350–419](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/src/moving_averages.rs#L350-L419); [requirements.txt:34–34](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/requirements.txt#L34-L34)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** General estimator convergence adapter

The inspected native search evaluates strategy hyperparameters through backtests, not a managed statistical estimator fit loop.

**Limit:** Model convergence, conditioning, calibration stability and fit-warning acceptance become applicable when an ML adapter is added. Optimizer budget completion should not be called model convergence.

**Executable sources:** [jesse/research/optimize/__init__.py:218–241](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/optimize/__init__.py#L218-L241); [jesse/modes/optimize_mode/fitness.py:28–49](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/fitness.py#L28-L49)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Dashboard Optuna history versus research API

Dashboard optimization creates/resumes a SQLite-backed Optuna study and stores parameters, score and training/testing metrics for returned trials.

**Limit:** The research API keeps only ranked best candidates in its return. Fitness catches general failures and returns a low-score/empty-metric result, so a completed trial is not necessarily a successful experiment; complete external search history is not enforced.

**Executable sources:** [jesse/modes/optimize_mode/Optimize.py:113–117](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/Optimize.py#L113-L117); [jesse/modes/optimize_mode/Optimize.py:151–156](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/Optimize.py#L151-L156); [jesse/modes/optimize_mode/Optimize.py:314–329](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/Optimize.py#L314-L329); [jesse/modes/optimize_mode/fitness.py:118–131](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/fitness.py#L118-L131); [jesse/research/optimize/__init__.py:306–327](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/optimize/__init__.py#L306-L327)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Single-rule stationary-bootstrap inference

Optional rule significance zero-centers signed detrended next-bar returns and samples geometrically sized contiguous blocks with circular wraparound. Seeded output is independent of batching; the reported p-value is the fraction of simulated means at least the observed mean.

**Limit:** This handles a chosen local dependence model, not a searched family. No multiple-rule/parameter-selection correction is applied in this entry point. Finite Monte Carlo estimates can be zero because the implementation uses the raw exceedance fraction.

**Executable sources:** [jesse/research/rule_significance_testing/bootstrap.py:29–66](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/rule_significance_testing/bootstrap.py#L29-L66); [jesse/research/rule_significance_testing/rule_significance.py:183–224](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/rule_significance_testing/rule_significance.py#L183-L224)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Research assumptions and per-session outcomes

Optimization forwards balance, fee, simulation model, annualization, leverage and warmup explicitly into isolated worker backtests and attaches train/test metrics to saved trials.

**Limit:** This improves assumption traceability but no exact input-byte/code/environment acceptance manifest or cross-run comparability gate was located in these paths. Different windows or simulation assumptions must remain separate cohorts.

**Executable sources:** [jesse/modes/optimize_mode/fitness.py:10–25](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/fitness.py#L10-L25); [jesse/modes/optimize_mode/Optimize.py:314–325](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/Optimize.py#L314-L325)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Testing period in optimizer

A testing backtest uses the same candidate parameters after training evaluation, and its metrics do not enter the computed score.

**Limit:** Testing metrics are published for many candidates; the path does not implement a reserved single-use final holdout or a freeze-before-access gate. Treat this as repeated validation, not protected final evidence.

**Executable sources:** [jesse/modes/optimize_mode/fitness.py:91–116](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/fitness.py#L91-L116); [jesse/modes/optimize_mode/Optimize.py:440–461](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/Optimize.py#L440-L461)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Predictive/execution external validity

Native rule-significance and Monte Carlo paths can evaluate a supplied strategy under explicit assumptions; tests include noise/signal examples.

**Limit:** No matched cross-solution experiment here establishes real-market predictive edge, economic generalization or fidelity of assumed fills. A diagnostic on a selected strategy is not independent holdout evidence.

**Executable sources:** [tests/test_rule_significance_testing.py:218–235](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/tests/test_rule_significance_testing.py#L218-L235); [jesse/research/rule_significance_testing/rule_significance.py:131–139](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/rule_significance_testing/rule_significance.py#L131-L139); [jesse/modes/optimize_mode/fitness.py:10–25](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/optimize_mode/fitness.py#L10-L25)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Seeded dependence and candle perturbation sensitivity

Stationary-bootstrap block length and seed are exposed. A moving-block candle pipeline resamples contiguous multivariate blocks using an explicit RNG; Monte Carlo supports alternative candle perturbation models.

**Limit:** These are optional robustness experiments with assumed perturbation distributions. Their existence does not show a strategy passed sensitivity analysis, and independently sourced market regimes remain necessary.

**Executable sources:** [jesse/research/rule_significance_testing/rule_significance.py:42–55](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/rule_significance_testing/rule_significance.py#L42-L55); [jesse/research/rule_significance_testing/bootstrap.py:39–66](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/research/rule_significance_testing/bootstrap.py#L39-L66); [jesse/candle_pipelines/moving_block_bootstrap.py:27–50](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/candle_pipelines/moving_block_bootstrap.py#L27-L50); [jesse/modes/monte_carlo_mode/MonteCarloRunner.py:306–341](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/monte_carlo_mode/MonteCarloRunner.py#L306-L341)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Authenticated local platform routes, strategy loading and cached artifacts.

Backtest endpoints require the shared-token authentication dependency. Strategy loading resolves and executes local Python strategy classes; the pickle cache loads trusted local Python objects. The native coordinator separately checks its token, protocol version, namespace and service generation before processing commands.

**Limit:** Authentication is not a strategy sandbox or per-tenant isolation. Trusted strategy/cache ownership is required; this review did not establish a constrained public arbitrary-code interface. The auxiliary Rust source version matches the dependency declaration, but source-to-wheel identity is not proven.

**Executable sources:** [jesse/services/auth.py:14–51](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/auth.py#L14-L51); [jesse/controllers/backtest_controller.py:30–74](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/controllers/backtest_controller.py#L30-L74); [jesse/helpers.py:380–421](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/helpers.py#L380-L421); [jesse/services/cache.py:20–29](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/cache.py#L20-L29); [coordination/src/lib.rs:219–241](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/coordination/src/lib.rs#L219-L241)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Observed-minute candle and changed protective-order admission.

Candle validation requires a nonempty six-column ndarray and finite, minute-aligned, strictly increasing unique timestamps. Changed stop-loss/take-profit values are checked for finite quantities and prices before old protective orders are replaced.

**Limit:** The candle function does not validate finite-positive OHLC, OHLC cross-consistency or volume, and exchange configuration converts fee/balance/leverage values without establishing a universal finite economic contract. Protective-order checks do not imply every entry/custom callback is identically validated.

**Executable sources:** [jesse/services/candle_service.py:455–463](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/candle_service.py#L455-L463); [jesse/strategies/Strategy.py:799–808](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/strategies/Strategy.py#L799-L808); [jesse/strategies/Strategy.py:979–1030](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/strategies/Strategy.py#L979-L1030); [jesse/config.py:188–199](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/config.py#L188-L199)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native coordinator quotas and managed child-process lifecycle.

The coordinator bounds frames, payloads, total state, keys, clients, subscribers and queued event bytes; its parser has read deadlines. The Python process manager has a global graceful-shutdown budget followed by termination/kill escalation for remaining children.

**Limit:** add_task does not impose a general process-count, per-strategy memory or execution-time quota. Coordinator bounds apply to the inspected auxiliary source, whose identity with the installed native wheel is unverified; no hostile-load or shutdown stress run was performed.

**Executable sources:** [coordination/src/lib.rs:17–31](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/coordination/src/lib.rs#L17-L31); [coordination/src/lib.rs:147–151](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/coordination/src/lib.rs#L147-L151); [coordination/src/lib.rs:467–499](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/coordination/src/lib.rs#L467-L499); [coordination/src/lib.rs:587–634](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/coordination/src/lib.rs#L587-L634); [jesse/services/multiprocessing.py:95–120](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/multiprocessing.py#L95-L120); [jesse/services/multiprocessing.py:135–180](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/multiprocessing.py#L135-L180)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Local coordinator connection and chart-download destination boundaries.

The native coordinator rejects non-loopback binding, requires a sufficiently long token and bounds protocol reads. The authenticated chart endpoint parses the session as a UUID and permits only a fixed chart-name set before constructing its file path.

**Limit:** These controls are route specific and do not establish common timeouts, byte/digest validation, archive containment or credential handling across every exchange/data-import adapter. The native source-to-wheel caveat also applies here.

**Executable sources:** [coordination/src/lib.rs:779–811](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/coordination/src/lib.rs#L779-L811); [coordination/src/lib.rs:587–634](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/coordination/src/lib.rs#L587-L634); [jesse/controllers/backtest_controller.py:80–99](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/controllers/backtest_controller.py#L80-L99)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**Unknown** · Inspected · applicability `unknown` · capability `not_located`

**Scope:** Managed backtest session and local cache content identity.

BacktestSession records a UUID, status, strategy code and result fields; the cache stores path/expiry metadata. An externally verified digest binding all study inputs/code/environment at result/cache read was not located in the inspected routes.

**Limit:** The bounded inspection did not establish enforcement or prove repository-wide absence. Require an implementation pointer and executable acceptance results before treating this capability as present.

**Executable sources:** [jesse/models/BacktestSession.py:26–52](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/models/BacktestSession.py#L26-L52); [jesse/services/cache.py:31–47](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/cache.py#L31-L47); [jesse/services/cache.py:49–97](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/cache.py#L49-L97)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Local pickle cache corruption behavior and coordinator generation checks.

The cache catches selected decoding/missing-file failures and removes or resets the affected cache metadata, returning a cache miss. The native coordinator rejects a stale generation before mutation after service restart.

**Limit:** Cache recovery deliberately mutates metadata and is not immutable research-round fail-closed admission; other valid pickle values can be accepted without expected content hashes. Local pickle is trusted code/data. Coordinator generation is service-session identity, not durable experiment evidence.

**Executable sources:** [jesse/services/cache.py:20–29](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/cache.py#L20-L29); [jesse/services/cache.py:49–97](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/cache.py#L49-L97); [coordination/src/lib.rs:219–241](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/coordination/src/lib.rs#L219-L241)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Cache/session writes and ephemeral coordinator state.

Cache set writes metadata before the value file, using separate direct pickle writes. Backtest session result/status updates are database operations, while coordinator restart is detected through a changed generation.

**Limit:** No atomic frontier spanning cache metadata, result files, database session state and strategy execution was established. Direct cache writes can be interrupted; a detected coordinator restart does not recover its previous state. Process-kill or power-loss recovery was not executed.

**Executable sources:** [jesse/services/cache.py:31–47](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/cache.py#L31-L47); [jesse/services/cache.py:94–97](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/cache.py#L94-L97); [jesse/models/BacktestSession.py:235–276](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/models/BacktestSession.py#L235-L276); [coordination/src/lib.rs:219–241](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/coordination/src/lib.rs#L219-L241)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Python child-process failure publication and shutdown cleanup.

The child wrapper catches ordinary exceptions, publishes exception details and terminates the session. Failed starts remove the process registration. Shutdown requests cooperative cancellation and escalates to terminate/kill; cleanup joins and removes dead workers.

**Limit:** Publication depends on the coordinator remaining available. These paths do not prove exact resume from the completed task prefix, durable failure delivery, absence of all orphans or correctness under hard process death and shutdown races; no live services were exercised.

**Executable sources:** [jesse/services/multiprocessing.py:26–45](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/multiprocessing.py#L26-L45); [jesse/services/multiprocessing.py:95–120](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/multiprocessing.py#L95-L120); [jesse/services/multiprocessing.py:135–180](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/multiprocessing.py#L135-L180); [jesse/services/multiprocessing.py:212–250](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/multiprocessing.py#L212-L250)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Changed strategy protective-order outputs before downstream execution.

Changed stop-loss and take-profit arrays pass finite quantity/price checks before the saved protective array is updated and existing stop orders are canceled.

**Limit:** This is a concrete strategy-output safety gate, not a shared fitted-probability model contract. A generic model's shape, unavailable-inference representation and downstream behavior still belong to its adapter. The check does not establish validity of all order semantics.

**Executable sources:** [jesse/strategies/Strategy.py:799–808](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/strategies/Strategy.py#L799-L808); [jesse/strategies/Strategy.py:979–1030](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/strategies/Strategy.py#L979-L1030)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Observed candle timestamps and replay dispatch order.

The observed-minute validator rejects nonfinite, unaligned, duplicate or decreasing timestamps. The backtest applies the event/batch, executes updated routes and then processes active and simulated market orders for the affected source pairs.

**Limit:** The clock trusts supplied observations; source authenticity, causal strategy features and intra-bar path remain separate. Fast/native aggregation code also requires the auxiliary source-to-binary identity caveat. Equivalent slow/fast outcomes were not tested in this safety campaign.

**Executable sources:** [jesse/services/candle_service.py:455–463](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/candle_service.py#L455-L463); [jesse/modes/backtest_mode.py:483–515](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L483-L515); [jesse/modes/backtest_mode.py:981–1014](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L981-L1014)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Simulated spot affordability and futures margin admission.

Futures order submission rejects non-reducing orders that exceed available margin before booking the reservation. Spot submission rejects excessive spend or sale, but the buy branch subtracts cash before raising InsufficientBalance.

**Limit:** The spot failure path does not restore the prior balance within the inspected method; a fresh aborted-run reset is a different contract from continuing after a caught exception. Both methods return early in live mode, so this evidence cannot establish live exchange risk enforcement. No live order or spot failure probe was executed.

**Executable sources:** [jesse/models/SpotExchange.py:36–73](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/models/SpotExchange.py#L36-L73); [jesse/models/FuturesExchange.py:106–128](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/models/FuturesExchange.py#L106-L128)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Finite protective updates and isolated-margin liquidation model.

Protective updates validate finite values before cancellation/replacement. The backtest liquidation check handles a liquidation threshold within the bar or crossed between previous close and current open, then submits a reducing close at the configured bankruptcy price.

**Limit:** The liquidation function returns without that simulation unless the position mode is isolated. Bar-level fills, bankruptcy price and barrier ordering are model assumptions; cross-margin and live capital behavior require separate evidence. No guaranteed real protective fill follows.

**Executable sources:** [jesse/strategies/Strategy.py:799–808](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/strategies/Strategy.py#L799-L808); [jesse/strategies/Strategy.py:979–1018](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/strategies/Strategy.py#L979-L1018); [jesse/modes/backtest_mode.py:1723–1768](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/modes/backtest_mode.py#L1723-L1768)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**Unknown** · Inspected · applicability `unknown` · capability `not_located`

**Scope:** Protected holdout admission in the platform's managed research route.

No durable protected holdout reservation/exposure ledger was located in the bounded platform inspection. Backtest sessions, cached candles and coordinator key namespaces serve different contracts.

**Limit:** The bounded inspection did not establish enforcement or prove repository-wide absence. Require an implementation pointer and executable acceptance results before treating this capability as present.

**Executable sources:** [jesse/models/BacktestSession.py:26–52](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/models/BacktestSession.py#L26-L52); [jesse/services/cache.py:31–47](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/jesse/services/cache.py#L31-L47)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native coordinator build/test CI and Python CodeQL configuration.

The coordinator workflow has read-only repository permission, bounded job duration, a multi-platform/Python matrix and locked cargo build, clippy and test commands against the 1.3.1 source tag. A separate workflow configures Python CodeQL analysis.

**Limit:** A tag/version match does not prove the audited auxiliary commit produced the installed jesse-rust wheel. Some action references are version tags; configured scanners and tests do not establish current hosted enforcement or a complete audited release dependency graph.

**Executable sources:** [.github/workflows/native-coordination.yml:13–50](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/.github/workflows/native-coordination.yml#L13-L50); [.github/workflows/codeql-analysis.yml:23–81](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/.github/workflows/codeql-analysis.yml#L23-L81); [requirements.txt:34–34](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/requirements.txt#L34-L34); [Cargo.toml:1–20](https://github.com/jesse-ai/jesse-rust/blob/bab04ada5f652fc369de06141ff6ea84896130a6/Cargo.toml#L1-L20)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected native coordinator malformed-input and state-transition assertions.

Tests assert invalid nonfinite/nonpositive TTL leaves the prior value unchanged, namespace separation, token/generation rejection before mutation, survival after a malformed frame and rejection of an oversized payload without inserting its key.

**Limit:** These assertions and the configured native test commands were inspected, not executed by this safety campaign. They do not prove all strategy, cache corruption, process-kill, fill or native wheel boundaries; no aggregate coverage score is assigned.

**Executable sources:** [tests/test_coordination.py:158–163](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/tests/test_coordination.py#L158-L163); [tests/test_coordination.py:198–217](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/tests/test_coordination.py#L198-L217); [tests/test_coordination.py:293–309](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/tests/test_coordination.py#L293-L309); [.github/workflows/native-coordination.yml:30–50](https://github.com/jesse-ai/jesse/blob/4fcbcdd500b9cd14ca9bdb142e4f46a34884a1ae/.github/workflows/native-coordination.yml#L30-L50)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

