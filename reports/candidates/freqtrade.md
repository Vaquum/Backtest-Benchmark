# Freqtrade

**Frozen source:** [freqtrade/freqtrade @ 3ce38b587d6c7a1ea479fb3e59d724dee5195561](https://github.com/freqtrade/freqtrade/tree/3ce38b587d6c7a1ea479fb3e59d724dee5195561)

**Observed license label:** GPL-3.0  
**Layer:** Crypto execution/backtest platform, hyperopt and FreqAI research

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Pinned source builds/imports; data preprocessing and batched joblib optimization are implemented, but matching execution and research timings remain unmeasured.

**Academic:** Optional lookahead/recursive diagnostics and FreqAI temporal workflow; label-horizon, inner-validation and search-selection assumptions need explicit auditing.

**Safety:** Wallet, authentication and operational controls are scoped; arbitrary strategies are trusted and prediction-mask/cache admission requires care.

## P01

### Parameter-space construction and retained memory

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native hyperopt Optuna proposal batches

Hyperopt requests n_points from its configured optimizer, retaining asked trials and completed trial history.

**Limit:** No Cartesian-size/accepted-count memory sweep; sampler/history complexity differs from finite grid enumeration.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt.py:144–184](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L144-L184)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Hyperopt duplicates and bounded proposal retry

The inspected path compares proposed parameters against complete trials and batch entries, then retries up to 2*n_points.

**Limit:** Novelty correctness and duplicate-heavy/exhaustion performance were not dynamically verified; source comparisons should not be promoted to proven uniqueness.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt.py:150–184](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L150-L184)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Source-built Freqtrade and native strategy/exchange/data/wallet preparation

The source imports in an isolated environment. Full Backtesting initialization configures additional strategy/exchange state before the event loop.

**Limit:** No matched complete first-result timing; import success is recorded separately.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [freqtrade/optimize/backtesting.py:128–193](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtesting.py#L128-L193)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native hyperopt/FreqAI campaign

Hyperopt precomputes or reloads indicator data, dispatches batches, tells the optimizer and records trial outputs.

**Limit:** The common fixed-rule accounting benchmark is not a FreqAI research-campaign comparison.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt.py:216–283](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L216-L283); [freqtrade/optimize/hyperopt/hyperopt_optimizer.py:454–473](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt_optimizer.py#L454-L473)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**Partial** · Inspected · applicability `native` · capability `unknown`

**Scope:** Fitted preparation/prediction reuse, distinguished from adjacent raw or deterministic computation reuse

Without analyze_per_epoch, native prepare_hyperopt_data computes indicators and dumps reusable preprocessed frames; otherwise it dumps raw data.

**Limit:** The cited adjacent data/processing mechanism does not establish a fitted-state or prediction-reuse cache. Indicator reuse is configuration-sensitive. No matched FreqAI fitted-preparation/prediction-cache ablation or scientific equivalence measurement.

**Measurement state:** Not measured in this criterion scope

**Distinct sub-capabilities:** fitted_state_or_prediction_reuse_in_inspected_path: Unknown; no fitted-reuse speedup inferred; adjacent_input_or_deterministic_reuse: Implemented as described in finding; not the canonical fitted capability

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt_optimizer.py:454–473](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt_optimizer.py#L454-L473)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** User strategy indicator analysis and analyzed frame conversion

Backtesting converts processed frames to lists before the time/pair loop; hyperopt optionally amortizes indicator analysis.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [freqtrade/optimize/backtesting.py:1778–1823](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtesting.py#L1778-L1823); [freqtrade/optimize/hyperopt/hyperopt_optimizer.py:454–473](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt_optimizer.py#L454-L473)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native exchange-aware bar backtest and trade/wallet outputs

The native path processes time/pair events, reversals, open-trade closure, wallet updates and complete result-trade output.

**Limit:** No admitted matching close-fill adapter; native contract assumptions must be harmonized without changing the source OHLC prices. Timings remain unmeasured.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [freqtrade/optimize/backtesting.py:1778–1823](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtesting.py#L1778-L1823)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Pair/time loop, optional short reversal and forced end handling

Each admitted row enters backtest_loop; a reversal can invoke it twice. Remaining open trades are handled at the end.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [freqtrade/optimize/backtesting.py:1778–1823](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtesting.py#L1778-L1823)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Preprocessed market frames, converted lists, trial workers and trade records

Hyperopt stores shared preparation while worker batches execute backtests; complete-trial history and per-backtest state contribute memory.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt.py:216–283](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L216-L283); [freqtrade/optimize/backtesting.py:1778–1823](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtesting.py#L1778-L1823)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Joblib hyperopt batch execution

Parallel(n_jobs=config_jobs) dispatches asked batches and waits for complete results before optimizer tell and collection.

**Limit:** No same-family worker-count sweep. Batch barriers and final-batch size can affect scaling and imbalance.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt.py:229–281](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L229-L281)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Analyzed data pickle and repeated indicator calculation choices

Native hyperopt persists either preprocessed or raw data based on analyze_per_epoch.

**Limit:** A reusable data artifact does not itself verify causal feature construction or fresh-equivalent fitted-model results; no cache-cost benchmark.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt_optimizer.py:454–473](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt_optimizer.py#L454-L473)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Hyperopt trial recording and optimizer state

Completed worker outputs pass through native evaluate_result and study tell calls.

**Limit:** No interrupted campaign, complete durable-prefix or physical-write-overhead experiment was performed.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt.py:263–278](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L263-L278)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native backtesting plus lookahead/recursive analysis

Backtesting shifts signal columns one bar; optional lookahead analysis recomputes truncated runs and compares aligned indicators and entry/exit outcomes. This is stronger native diagnostic coverage than merely accepting arbitrary batch predictors.

**Limit:** The diagnostic is not mandatory admission. It is limited by selected trades/cutoffs, minimum support and skipped forced exits; a clean report is not proof for every predictor/data regime. Full-frame feature callbacks remain trusted.

**Executable sources:** [freqtrade/optimize/backtesting.py:550–566](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtesting.py#L550-L566); [freqtrade/optimize/analysis/lookahead.py:66–95](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/analysis/lookahead.py#L66-L95); [freqtrade/optimize/analysis/lookahead.py:139–169](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/analysis/lookahead.py#L139-L169); [freqtrade/optimize/analysis/lookahead.py:203–251](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/analysis/lookahead.py#L203-L251)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** FreqAI outer windows and base learned preprocessing

For each backtest window, training data are cut before the outer cutoff; base regression/classifier pipelines split inner fit/evaluation data and fit transforms on inner train only.

**Limit:** Features are first populated on the complete supplied dataframe. Arbitrary feature/model callbacks can use broader information; inner shuffle/reversed order are configurable rather than universally forbidden.

**Executable sources:** [freqtrade/freqai/freqai_interface.py:341–359](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/freqai_interface.py#L341-L359); [freqtrade/freqai/base_models/BaseRegressionModel.py:53–79](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/base_models/BaseRegressionModel.py#L53-L79); [freqtrade/freqai/data_kitchen.py:134–158](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L134-L158); [freqtrade/freqai/data_kitchen.py:189–207](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L189-L207)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** FreqAI target completion at outer cutoff and inner split

Targets are regenerated on data ending strictly before outer training stop, then unavailable labels are dropped; an optional buffer trims both ends. This protects ordinary forward-shift targets against reading the next outer prediction period.

**Limit:** Targets are computed before the inner train/test split and no general inner horizon purge is present in that split call. Custom extrema/precomputed labels require an adequate buffer and explicit availability audit.

**Executable sources:** [freqtrade/freqai/freqai_interface.py:347–359](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/freqai_interface.py#L347-L359); [freqtrade/freqai/data_kitchen.py:248–265](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L248-L265); [freqtrade/freqai/data_kitchen.py:1000–1005](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L1000-L1005); [freqtrade/freqai/data_kitchen.py:145–158](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L145-L158)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** FreqAI sliding training/backtesting windows

A window generator validates positive integer training days, advances by configured backtest duration and places each outer prediction window immediately after its training period. Inner split defaults shuffle=False.

**Limit:** Window geometry is native to FreqAI, not a mandatory validation procedure for ordinary strategy hyperopt. Row/horizon overlap and irregular cadence still need the selected-target audit.

**Executable sources:** [freqtrade/freqai/data_kitchen.py:328–372](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L328-L372); [freqtrade/freqai/data_kitchen.py:134–158](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L134-L158)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** FreqAI per-window learned feature and label pipelines

Base regression training creates new feature/label pipelines, fits on inner training features/labels and transforms inner evaluation data. Optional PCA follows scaling in the pipeline.

**Limit:** Cached models/predictions and continual-learning configuration are different paths; raw feature causality is not repaired by fold-local scalers. Custom subclasses can replace the base pipeline.

**Executable sources:** [freqtrade/freqai/base_models/BaseRegressionModel.py:53–86](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/base_models/BaseRegressionModel.py#L53-L86); [freqtrade/freqai/freqai_interface.py:558–591](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/freqai_interface.py#L558-L591); [freqtrade/freqai/freqai_interface.py:328–339](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/freqai_interface.py#L328-L339)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** FreqAI model evaluation and strategy decision thresholds

Native LightGBM receives inner evaluation data separately from fitted observations; example strategy applies explicit thresholds and requires do_predict==1 for entries.

**Limit:** No general independently assessed probability-calibration layer was located in these base/model paths. Strategy threshold choices and hyperopt selection require external untouched assessment; inner evaluation is not the final backtest sample.

**Executable sources:** [freqtrade/freqai/prediction_models/LightGBMRegressor.py:33–60](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/prediction_models/LightGBMRegressor.py#L33-L60); [freqtrade/templates/FreqaiExampleStrategy.py:238–261](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/templates/FreqaiExampleStrategy.py#L238-L261)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Trade-based versus balance-based Sharpe and return metrics

Both trade-profit and daily-balance metric routes exist. Balance-based Sharpe uses daily last balances and percent changes; trade-based Sharpe divides total normalized profit by elapsed days but uses dispersion across trades.

**Limit:** These named Sharpe values are not interchangeable. Native annualization factor is365 and zero/NaN denominator can produce -100 as a selection sentinel; recompute a common equity-based metric before comparing frameworks.

**Executable sources:** [freqtrade/data/metrics.py:341–379](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/data/metrics.py#L341-L379); [freqtrade/data/metrics.py:455–498](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/data/metrics.py#L455-L498)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Lookahead regression tests and metric reference assertions

Tests exercise explicitly biased/no-bias strategies and compare p-value/math behavior against expected/reference results. These are executable checks, including intentional negative controls.

**Limit:** Assertions were inspected in this comparative audit, not executed here. Formula checks do not establish global strategy causality or empirical probability calibration.

**Executable sources:** [tests/optimize/test_lookahead_analysis.py:465–497](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/tests/optimize/test_lookahead_analysis.py#L465-L497); [tests/data/test_metrics.py:477–497](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/tests/data/test_metrics.py#L477-L497)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Hyperopt stagnation and FreqAI model failures

Hyperopt can stop on best-value stagnation. FreqAI catches a failed window fit, records metadata and emits null predictions instead of retaining a usable model for that window.

**Limit:** Stagnation and successful backend fitting are not general convergence/stability proofs. A benchmark must retain failed windows and inspect their effect on evaluation support.

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt_optimizer.py:432–438](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt_optimizer.py#L432-L438); [freqtrade/optimize/hyperopt/hyperopt.py:280–285](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L280-L285); [freqtrade/freqai/freqai_interface.py:369–387](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/freqai_interface.py#L369-L387)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Hyperopt local epoch inventory

Completed epoch records retain loss, parameters, metrics, current index and best/random flags; results append one JSON line per evaluated epoch. Optuna receives evaluated losses.

**Limit:** The active study is created without durable storage in this constructor; only emitted records establish retained coverage. Unknown crashed/external searches and skipped duplicate candidates cannot become independent completed trials.

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt.py:95–119](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L95-L119); [freqtrade/optimize/hyperopt/hyperopt.py:192–214](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L192-L214); [freqtrade/optimize/hyperopt/hyperopt.py:255–275](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L255-L275); [freqtrade/optimize/hyperopt/hyperopt_optimizer.py:438–438](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt_optimizer.py#L438-L438)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native trade p-value and hyperopt-selected utility

Native p-value uses a one-sample t-test on normalized per-trade profit with fewer-than-two/constant-return fallbacks. Hyperopt minimizes a configurable same-backtest loss and applies a minimum-trade penalty.

**Limit:** No full-search multiplicity adjustment or serial-dependence correction is present in these computations. The per-strategy p-value is not a post-hyperopt false-positive guarantee.

**Executable sources:** [freqtrade/data/metrics.py:654–660](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/data/metrics.py#L654-L660); [freqtrade/optimize/hyperopt/hyperopt_optimizer.py:362–388](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt_optimizer.py#L362-L388)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Strategy cache identity and FreqAI prediction reuse

Backtest run ID hashes selected config, parameter-file state and strategy source bytes; reports retain evaluation dates. FreqAI reuses predictions using model path, row count/date-column presence and feature-list checks.

**Limit:** Run ID does not hash market-data bytes in this function. The inspected prediction gate does not compare actual timestamps/values. Immutable source identity and cross-run evaluation alignment need independent benchmark evidence.

**Executable sources:** [freqtrade/optimize/backtest_caching.py:15–37](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtest_caching.py#L15-L37); [freqtrade/freqai/data_kitchen.py:932–945](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L932-L945); [freqtrade/freqai/freqai_interface.py:328–339](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/freqai_interface.py#L328-L339)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**Unknown** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Final protected assessment beyond FreqAI windows/hyperopt

Rolling prediction windows and separate model evaluation arrays are implemented; no reservation plus frozen-selection/exposure-attempt protocol was located in inspected backtest, hyperopt and FreqAI paths.

**Limit:** An ordinary historical timerange can be reused and optimized. A separate final holdout adapter/registry is required for untouched-assessment claims; this is not a defect in ordinary backtest execution.

**Executable sources:** [freqtrade/freqai/data_kitchen.py:348–372](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L348-L372); [freqtrade/optimize/hyperopt/hyperopt.py:201–218](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L201-L218)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Executable strategy templates and quality comparison

A concrete FreqAI template defines forward-return labels and entry/exit decisions, and configurable hyperopt losses produce measurable local objectives.

**Limit:** No same-budget external ranking or untouched cross-asset generalization was measured in this sub-audit. Templates are reproducible logic, not demonstrated economic baselines superior to another framework.

**Executable sources:** [freqtrade/templates/FreqaiExampleStrategy.py:192–199](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/templates/FreqaiExampleStrategy.py#L192-L199); [freqtrade/templates/FreqaiExampleStrategy.py:238–261](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/templates/FreqaiExampleStrategy.py#L238-L261); [freqtrade/optimize/hyperopt/hyperopt_optimizer.py:369–388](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt_optimizer.py#L369-L388)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Recursive sensitivity, feature pipelines and seeded search

Native recursive analysis compares final indicator values across startup lengths and performs a truncated-input check. Hyperopt records/uses a sampler seed; optional PCA, outlier removal and noise expose explicit sensitivity choices.

**Limit:** Recursive diagnostics inspect selected pair/cutoffs and are not a full stability study. Sampler seed alone does not control all custom callbacks, backend randomness or source revisions.

**Executable sources:** [freqtrade/optimize/analysis/recursive.py:47–85](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/analysis/recursive.py#L47-L85); [freqtrade/optimize/analysis/recursive.py:209–229](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/analysis/recursive.py#L209-L229); [freqtrade/optimize/hyperopt/hyperopt.py:216–218](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L216-L218); [freqtrade/optimize/hyperopt/hyperopt_optimizer.py:419–428](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt_optimizer.py#L419-L428)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Trusted strategy/configuration and authenticated API surface.

The resolver executes strategy module code before class filtering; it also accepts base64-encoded strategy source. Config JSON includes can recurse only to a bounded depth. API router groups use authentication dependencies.

**Limit:** Authentication is access control, not isolation between mutually hostile users. The strategy/config/installed-model source must be trusted; arbitrary strategy code and cloudpickle artifacts are not sandboxed by JSON schema.

**Executable sources:** [freqtrade/resolvers/iresolver.py:89–120](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/resolvers/iresolver.py#L89-L120); [freqtrade/resolvers/strategy_resolver.py:281–305](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/resolvers/strategy_resolver.py#L281-L305); [freqtrade/configuration/load_config.py:80–110](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/configuration/load_config.py#L80-L110); [freqtrade/rpc/api_server/webserver.py:222–250](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/rpc/api_server/webserver.py#L222-L250)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Run-mode schema checks and finite feature filtering.

Configuration admission selects required fields for live/dry-run/backtest/webserver modes and validates against its schema. FreqAI replaces feature infinities with NaN and excludes invalid training rows.

**Limit:** Schema validation does not establish every callback/exchange/direct numeric boundary. Prediction inputs use a separate zero-fill plus do_predict mask, and caller strategy behavior must honor it.

**Executable sources:** [freqtrade/configuration/config_validation.py:46–67](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/configuration/config_validation.py#L46-L67); [freqtrade/freqai/data_kitchen.py:234–284](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L234-L284)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Configuration includes, hyperopt scheduling and FreqAI shutdown.

Recursive config loading has a depth guard. Hyperopt schedules a finite total_epochs budget in batches sized to configured workers. FreqAI normally joins training threads during shutdown.

**Limit:** The training-thread join has no timeout; native learner/strategy runtime and process RAM are not bounded by the epoch count. No adversarial training hang was executed.

**Executable sources:** [freqtrade/configuration/load_config.py:80–110](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/configuration/load_config.py#L80-L110); [freqtrade/optimize/hyperopt/hyperopt.py:223–268](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L223-L268); [freqtrade/freqai/freqai_interface.py:195–218](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/freqai_interface.py#L195-L218)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Trusted local include paths, strategy search and authenticated service routes.

Config includes resolve relative to the including file; strategy search can add operator-supplied directories and temporary decoded source. Authenticated API route groups are explicitly configured.

**Limit:** These paths intentionally allow operator filesystem/code access; they are not a containment boundary for hostile configs. Exchange-specific network timeouts, download quotas, redirects and all credential handling were not comprehensively verified in this row.

**Executable sources:** [freqtrade/configuration/load_config.py:95–110](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/configuration/load_config.py#L95-L110); [freqtrade/resolvers/strategy_resolver.py:267–305](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/resolvers/strategy_resolver.py#L267-L305); [freqtrade/rpc/api_server/webserver.py:222–250](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/rpc/api_server/webserver.py#L222-L250)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Backtest result IDs and FreqAI prediction-cache reuse.

Backtest run IDs hash configuration, parameter-file values and strategy source bytes; the backtest may reuse a prior matching result. FreqAI's prediction-file gate checks row count and presence of a date column.

**Limit:** The inspected backtest digest does not include actual market-file bytes, and the FreqAI gate does not compare source timestamps/values. These are narrower cache identities than a fully bound data/code/environment manifest.

**Executable sources:** [freqtrade/optimize/backtest_caching.py:8–37](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtest_caching.py#L8-L37); [freqtrade/optimize/backtesting.py:1892–1928](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtesting.py#L1892-L1928); [freqtrade/freqai/data_kitchen.py:924–945](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L924-L945)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** FreqAI historic prediction and cached model files.

Historic predictions are loaded with cloudpickle; EOFError triggers a backup-file load. Prediction cache validity can accept matching row count plus a date column.

**Limit:** Fallback and shallow shape checks do not verify an expected content digest/reference graph. Pickle files must be trusted; no corruption-preserving research-round transaction or comprehensive mutation campaign was established.

**Executable sources:** [freqtrade/freqai/data_drawer.py:174–203](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_drawer.py#L174-L203); [freqtrade/freqai/data_kitchen.py:924–945](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L924-L945)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Live startup open-order refresh and FreqAI recovery.

Live startup normally fetches recorded open orders and updates trade state; dry_run or skip_open_order_update bypasses this refresh. FreqAI can load a backup after an EOF-corrupted prediction file.

**Limit:** Startup refresh handles some failures by logging/continuing and can assume sufficiently old unavailable orders were cancelled. This is not a single atomic exchange/database transaction or proof of exactly-once live effects; no exchange was contacted.

**Executable sources:** [freqtrade/freqtradebot.py:573–618](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqtradebot.py#L573-L618); [freqtrade/freqai/data_drawer.py:174–203](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_drawer.py#L174-L203)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native hyperopt process batches and FreqAI training threads.

Hyperopt uses a context-managed joblib Parallel pool and bounded epoch batches. FreqAI exposes a stop event and optional waiting for training threads.

**Limit:** Default thread join has no deadline, and stopping the scan loop does not preempt arbitrary learner code. Worker-kill recovery, orphan counts and durable-prefix equality were not tested by this safety review.

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt.py:223–268](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L223-L268); [freqtrade/freqai/freqai_interface.py:195–218](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/freqai_interface.py#L195-L218)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** FreqAI invalid-input mask and native latest-candle guard.

Prediction features with NaN/Inf are zero-filled and exposed through do_predict=0. The strategy interface declines empty/unreadable or sufficiently stale latest candle data.

**Limit:** do_predict is an output that a strategy must use; this inspection does not establish a universal execution gate for every FreqAI/custom model. Finite features do not imply calibrated or in-domain predictions.

**Executable sources:** [freqtrade/freqai/data_kitchen.py:234–284](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L234-L284); [freqtrade/strategy/interface.py:1291–1319](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/strategy/interface.py#L1291-L1319)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native backtest signal lag and strategy feature preparation.

The native backtest replaces missing signal fields with no-entry values, shifts signal/tag fields by one row and drops the leading row before simulation.

**Limit:** The lag does not repair a strategy that computed historical features using future data. Source availability, startup windows, informative-pair joins and live versus vectorized behavior must be held constant in comparisons.

**Executable sources:** [freqtrade/optimize/backtesting.py:552–571](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtesting.py#L552-L571); [freqtrade/strategy/interface.py:1291–1319](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/strategy/interface.py#L1291-L1319)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native wallet stake bounds on the ordinary finite-input trade route.

Stake validation limits requested stake to available balance and exchange maximum, rejects when minimum stake exceeds available funds, and restricts excessive upward adjustment to the minimum.

**Limit:** This is the finite-input wallet sizing rule, not complete validation of arbitrary callback NaNs or a guarantee against exchange-side liquidation. Leverage, fees, minimum notional and live account state still require compatible configuration.

**Executable sources:** [freqtrade/wallets.py:414–457](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/wallets.py#L414-L457); [freqtrade/optimize/backtesting.py:1104–1127](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtesting.py#L1104-L1127)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Backtest stop/liquidation and trailing-stop price rules.

The backtest handles out-of-bar stop/liquidation thresholds with opening-price branches and defines first-bar trailing-stop approximations.

**Limit:** OHLC and detail-timeframe rules remain model assumptions; they do not imply real slippage, queue priority or guaranteed protective exits. Live stop-on-exchange is a separate, connector-dependent control.

**Executable sources:** [freqtrade/optimize/backtesting.py:603–646](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/backtesting.py#L603-L646); [freqtrade/freqtradebot.py:1637–1655](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqtradebot.py#L1637-L1655)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**Unknown** · Inspected · applicability `unknown` · capability `not_located`

**Scope:** Freqtrade/FreqAI/hyperopt protected holdout admission.

No durable protected holdout reservation/exposure ledger was located in the bounded workflow inspection. Training windows and cached model/result identifiers are not that admission mechanism.

**Limit:** The bounded inspection did not establish enforcement or prove repository-wide absence. Require an implementation pointer and executable acceptance results before treating this capability as present.

**Executable sources:** [freqtrade/optimize/hyperopt/hyperopt.py:223–268](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/optimize/hyperopt/hyperopt.py#L223-L268); [freqtrade/freqai/data_kitchen.py:924–945](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/freqtrade/freqai/data_kitchen.py#L924-L945)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Checked-in CI and GitHub Actions security analysis.

The workflow contains pytest/coverage commands and a dedicated zizmor workflow with empty default permissions, pinned checkout/action commits and narrowly scoped security-events write permission.

**Limit:** Configured scanners are not proof of clean dependencies, protected branch enforcement or successful current hosted runs. Native learner/exchange dependency and runtime exposure remain separate scopes.

**Executable sources:** [.github/workflows/zizmor_action.yml:17–34](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/.github/workflows/zizmor_action.yml#L17-L34); [.github/workflows/ci.yml:68–84](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/.github/workflows/ci.yml#L68-L84)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected strategy validation assertions and workflow tests.

Strategy tests assert rejection when analysis changes dataframe length, final close or date. Native CI runs randomized-order pytest and coverage.

**Limit:** Those test assertions were inspected, not executed by this safety campaign. No blanket FreqAI probability safety, hostile-pickle protection, worker-kill recovery or mutation completeness follows.

**Executable sources:** [tests/strategy/test_interface.py:290–319](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/tests/strategy/test_interface.py#L290-L319); [.github/workflows/ci.yml:68–84](https://github.com/freqtrade/freqtrade/blob/3ce38b587d6c7a1ea479fb3e59d724dee5195561/.github/workflows/ci.yml#L68-L84)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

