# QuantConnect LEAN

**Frozen source:** [QuantConnect/Lean @ d4cac37514427c84d40064cecbf3f0e6be4b0137](https://github.com/QuantConnect/Lean/tree/d4cac37514427c84d40064cecbf3f0e6be4b0137)

**Observed license label:** Apache-2.0  
**Layer:** Full local market/algorithm/account engine and optimizer

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Pinned launcher builds, including locked NuGet restore; common-contract execution latency remains unmeasured.

**Academic:** Native algorithm-time/history guards and portfolio diagnostics; reported PSR is a marginal statistic and does not include search-family deflation.

**Safety:** Buying-power/resource/storage controls are real and route-dependent; a bounded native reproduction confirms path escape in the public ZIP overwrite helper.

## P01

### Parameter-space construction and retained memory

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native GridSearch/StepBase parameter construction

Step recursively yields ParameterSet dictionaries while traversing the configured dimensions.

**Limit:** No parameter-family memory sweep. Recursive queues/dictionaries and optimizer result retention still allocate memory.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Optimizer/Strategies/StepBaseOptimizationStrategy.cs:178–236](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/Strategies/StepBaseOptimizationStrategy.cs#L178-L236)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native optimizer candidate traversal

GridSearch consumes the Step enumerator and processes incoming optimization results.

**Limit:** The campaign does not execute a matched optimizer family or measure duplicate/exhaustion costs.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Optimizer/Strategies/GridSearchOptimizationStrategy.cs:40–60](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/Strategies/GridSearchOptimizationStrategy.cs#L40-L60); [Optimizer/Strategies/StepBaseOptimizationStrategy.cs:178–236](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/Strategies/StepBaseOptimizationStrategy.cs#L178-L236)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Source-built .NET launcher and complete local algorithm initialization

The pinned native launcher was built separately; no matched algorithm/data-feed adapter was admitted for cold execution timing.

**Limit:** Build completion is a reproducibility check, not an engine-latency observation.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Launcher/Program.cs:53–104](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Launcher/Program.cs#L53-L104)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native optimizer plus local engine campaign

The optimizer coordinates results and optional analysis; the engine runs a synchronized data/event/account pipeline.

**Limit:** No common model/search/evidence-retention campaign was implemented or timed; hosted QuantConnect services are outside the audited source.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Engine/AlgorithmManager.cs:191–225](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L191-L225); [Engine/AlgorithmManager.cs:697–749](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L697-L749); [Optimizer/LeanOptimizer.cs:161–213](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/LeanOptimizer.cs#L161-L213)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Arbitrary QCAlgorithm model code versus a specified native fold-fitted reuse contract

The selected native execution path does not perform this research-stage operation; a separately declared research adapter and matching scientific work are required.

**Limit:** N/A is a scope decision, not a negative quality or speed score; arbitrary user strategies may call external training/search code.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Engine/AlgorithmManager.cs:191–225](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L191-L225); [Engine/AlgorithmManager.cs:697–749](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L697-L749)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native indicator implementations and consolidator updates

Engine updates indicators/consolidators as part of time-slice processing; no matched native indicator-array benchmark was run.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Engine/AlgorithmManager.cs:191–225](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L191-L225); [Engine/AlgorithmManager.cs:697–749](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L697-L749); [Engine/AlgorithmManager.cs:456–484](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L456-L484)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Full native local LEAN algorithm and account engine

The source supports full synchronized algorithm execution; this campaign only built the launcher and inspected/ran bounded safety checks.

**Limit:** No admitted same-contract adapter, result trace or timing. This is an unmeasured row, never a zero, failure ranking or hosted-service result.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Engine/AlgorithmManager.cs:191–225](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L191-L225); [Engine/AlgorithmManager.cs:697–749](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L697-L749)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Synchronized event loop, securities, cash and callbacks

AlgorithmManager iterates Stream, checks cancellation/state, advances system time and dispatches execution work.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Engine/AlgorithmManager.cs:191–225](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L191-L225); [Engine/AlgorithmManager.cs:697–749](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L697-L749)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Full local launcher, data subscriptions, caches and optimizer workers

Native full-engine state and data subscriptions create a different memory footprint from a return kernel.

**Limit:** No engine-run process-tree memory measurement. Build/compiler RSS and duration are deliberately not substituted.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Engine/AlgorithmManager.cs:191–225](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L191-L225); [Engine/AlgorithmManager.cs:697–749](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L697-L749)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Optimizer/engine execution scheduling

The native optimizer exposes campaign orchestration, but this review does not assign worker scaling from source structure alone.

**Limit:** The campaign does not measure this stage independently; implementation language or the presence of a cache is not a speed measurement.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Optimizer/LeanOptimizer.cs:270–307](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/LeanOptimizer.cs#L270-L307)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Data/feed/algorithm reuse under a fixed local configuration

Native Stream and synchronization are the inspected data execution path; the cache population and retention profile depend on selected handlers.

**Limit:** No cold/warm source-cache or fitted-reuse ablation. Public service behavior is outside the scope.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Engine/AlgorithmManager.cs:191–225](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L191-L225); [Engine/AlgorithmManager.cs:697–749](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L697-L749)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native result/optimizer recording versus complete interrupted-run replay

Optimizer result processing and final analysis are executable source paths.

**Limit:** Recording overhead and exact-prefix restart recovery have not been benchmarked; successful build is not durability evidence.

**Measurement state:** Not measured in this criterion scope

**Executable sources:** [Optimizer/LeanOptimizer.cs:161–213](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/LeanOptimizer.cs#L161-L213); [Optimizer/LeanOptimizer.cs:415–439](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/LeanOptimizer.cs#L415-L439)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Algorithm time, History API and native return windows

AlgorithmManager sets current algorithm time/slice before scheduled and data callbacks. Native History clamps requests ending after UtcTime. ReturnsSymbolData maintains a bounded rolling window of updates and admits ROC observations only once ready.

**Limit:** These are concrete native information-set protections. They do not prove point-in-time correctness of arbitrary custom data, external reads, training callbacks or every indicator/model; provider timestamp/normalization semantics still matter.

**Executable sources:** [Engine/AlgorithmManager.cs:242–256](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L242-L256); [Engine/AlgorithmManager.cs:581–595](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/AlgorithmManager.cs#L581-L595); [Algorithm/QCAlgorithm.History.cs:1045–1061](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm/QCAlgorithm.History.cs#L1045-L1061); [Algorithm.Framework/Portfolio/ReturnsSymbolData.cs:43–48](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm.Framework/Portfolio/ReturnsSymbolData.cs#L43-L48); [Algorithm.Framework/Portfolio/ReturnsSymbolData.cs:94–110](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm.Framework/Portfolio/ReturnsSymbolData.cs#L94-L110)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native online portfolio estimation versus general ML

Mean-variance portfolio construction warms bounded return state from current History and optimizes that local return matrix; algorithm Train schedules caller-supplied training code.

**Limit:** This provides native online estimation boundaries, not an enforced supervised training/evaluation split. Train does not inspect feature fitting, targets or test reuse; full ML research isolation requires an adapter.

**Executable sources:** [Algorithm.Framework/Portfolio/MeanVarianceOptimizationPortfolioConstructionModel.cs:256–264](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm.Framework/Portfolio/MeanVarianceOptimizationPortfolioConstructionModel.cs#L256-L264); [Algorithm.Framework/Portfolio/MeanVarianceOptimizationPortfolioConstructionModel.cs:311–326](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm.Framework/Portfolio/MeanVarianceOptimizationPortfolioConstructionModel.cs#L311-L326); [Algorithm/QCAlgorithm.cs:3246–3261](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm/QCAlgorithm.cs#L3246-L3261)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** General supervised label availability

Native Train forwards an action to the scheduler; the inspected portfolio path consumes current insight magnitudes and bounded returns.

**Limit:** A general label horizon/censoring protocol was not located in these native scheduling/portfolio APIs. Custom supervised models need an adapter with explicit outcome-availability timestamps.

**Executable sources:** [Algorithm/QCAlgorithm.cs:3246–3261](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm/QCAlgorithm.cs#L3246-L3261); [Algorithm.Framework/Portfolio/MeanVarianceOptimizationPortfolioConstructionModel.cs:223–235](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm.Framework/Portfolio/MeanVarianceOptimizationPortfolioConstructionModel.cs#L223-L235)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Online history length and training schedules

ReturnsSymbolData has explicit ROC lookback and window period; Train can schedule updates on configured date/time rules.

**Limit:** These are online-window controls, not purged/embargoed/nested validation. Native parameter optimization enumerates configurations without automatically constructing a disjoint final research holdout.

**Executable sources:** [Algorithm.Framework/Portfolio/ReturnsSymbolData.cs:43–48](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm.Framework/Portfolio/ReturnsSymbolData.cs#L43-L48); [Algorithm/QCAlgorithm.cs:3259–3261](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm/QCAlgorithm.cs#L3259-L3261); [Optimizer/Strategies/StepBaseOptimizationStrategy.cs:178–184](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/Strategies/StepBaseOptimizationStrategy.cs#L178-L184)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native return matrix and portfolio fitting boundary

Portfolio construction creates a return matrix from bounded symbol state and passes it to the selected optimizer, which derives covariance/expected returns if not supplied.

**Limit:** General fold-fitted transforms and OOF stacking are not owned by this interface. Insight magnitudes and custom optimizers remain supplied code; historical-moment fitting does not establish nested supervised validation.

**Executable sources:** [Algorithm.Framework/Portfolio/MeanVarianceOptimizationPortfolioConstructionModel.cs:223–235](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm.Framework/Portfolio/MeanVarianceOptimizationPortfolioConstructionModel.cs#L223-L235); [Algorithm.Framework/Portfolio/MeanVarianceOptimizationPortfolioConstructionModel.cs:256–264](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm.Framework/Portfolio/MeanVarianceOptimizationPortfolioConstructionModel.cs#L256-L264); [Algorithm.Framework/Portfolio/MaximumSharpeRatioPortfolioOptimizer.cs:89–95](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm.Framework/Portfolio/MaximumSharpeRatioPortfolioOptimizer.cs#L89-L95)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Probability calibration and nested thresholds

The generic Train API schedules arbitrary training actions and the optimizer can target user-chosen statistics.

**Limit:** A built-in supervised probability-calibration/threshold-nesting protocol was not located in these APIs. Such behavior can be implemented by users but requires a separately audited adapter.

**Executable sources:** [Algorithm/QCAlgorithm.cs:3246–3261](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm/QCAlgorithm.cs#L3246-L3261); [Optimizer/Strategies/StepBaseOptimizationStrategy.cs:162–168](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/Strategies/StepBaseOptimizationStrategy.cs#L162-L168)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native portfolio Sharpe/CAGR/PSR definitions

Portfolio statistics separately calculate elapsed-time compounded annual return. The AnnualPerformance helper compounds the arithmetic mean daily return, while annual variance multiplies daily variance by tradingDaysPerYear; portfolio Sharpe uses that annual performance and a modeled risk-free rate.

**Limit:** This native Sharpe numerator is not mean daily excess return times sqrt(periods), nor realized geometric CAGR. Sortino uses variance of below-target returns. Standard-deviation/moment dependency conventions, annualization, risk-free source and zero sentinels must be normalized in a common metric contract.

**Executable sources:** [Common/Statistics/Statistics.cs:57–72](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Statistics/Statistics.cs#L57-L72); [Common/Statistics/Statistics.cs:98–112](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Statistics/Statistics.cs#L98-L112); [Common/Statistics/PortfolioStatistics.cs:284–312](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Statistics/PortfolioStatistics.cs#L284-L312)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Inspected numerical and model regression tests

PSR tests cover equal/greater/lower benchmark and risk-free response. Portfolio optimizer tests assert known weight vectors and explicit equal-weight fallback cases.

**Limit:** Tests were inspected, not executed in this academic audit. Boundary expectations and same-implementation PSR benchmark comparisons do not independently validate moment conventions, statistical assumptions or all fill/accounting paths.

**Executable sources:** [Tests/Common/Statistics/ProbabilisticSharpeRatioTests.cs:25–78](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Tests/Common/Statistics/ProbabilisticSharpeRatioTests.cs#L25-L78); [Tests/Common/Statistics/ProbabilisticSharpeRatioTests.cs:82–107](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Tests/Common/Statistics/ProbabilisticSharpeRatioTests.cs#L82-L107); [Tests/Algorithm/Framework/Portfolio/MaximumSharpeRatioPortfolioOptimizerTests.cs:99–137](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Tests/Algorithm/Framework/Portfolio/MaximumSharpeRatioPortfolioOptimizerTests.cs#L99-L137)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native portfolio solver failure behavior

MaximumSharpeRatioPortfolioOptimizer tests positive-excess-return feasibility, inspects solver success and normalizes the solution; infeasibility/solver failure/nonpositive recovery sum falls back to equal weights.

**Limit:** Fallback is a usable allocation convention, not proof a fitted optimum converged. It is returned as an ordinary weight vector without a distinct downstream convergence record in this interface. General user Train convergence remains caller-owned.

**Executable sources:** [Algorithm.Framework/Portfolio/MaximumSharpeRatioPortfolioOptimizer.cs:89–137](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm.Framework/Portfolio/MaximumSharpeRatioPortfolioOptimizer.cs#L89-L137); [Algorithm/QCAlgorithm.cs:3246–3261](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm/QCAlgorithm.cs#L3246-L3261)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native optimizer counts and completed metrics

LeanOptimizer tracks completed/failed/running/queued counts and retains parsed per-backtest metrics with parameters/backtest IDs. Grid search processes results only after nonempty JSON arrives.

**Limit:** Null/invalid result metrics are omitted from completed analysis; counters/logs do not reconstruct every failed artifact or external/manual trial. Post-search analysis explicitly filters to parsed portfolio statistics and selects its summary best by Sharpe, irrespective of the optimization target.

**Executable sources:** [Optimizer/LeanOptimizer.cs:248–288](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/LeanOptimizer.cs#L248-L288); [Optimizer/LeanOptimizer.cs:328–338](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/LeanOptimizer.cs#L328-L338); [Optimizer/Strategies/GridSearchOptimizationStrategy.cs:40–55](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/Strategies/GridSearchOptimizationStrategy.cs#L40-L55); [Optimizer/Analysis/OptimizationAnalyzer.cs:35–59](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/Analysis/OptimizationAnalyzer.cs#L35-L59)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native probabilistic Sharpe and optional objective constraints

PSR uses observed Sharpe, skewness/kurtosis and sample count against a fixed benchmark; reported portfolio PSR uses annual Sharpe1 deannualized. Optimizer constraints can filter result statistics.

**Limit:** PSR is not deflated Sharpe: no searched-trial count or family maximum enters this formula, and no serial-covariance correction appears. It is reported evidence, not an automatic protected-research admission rule. Moment conventions inherited from MathNet were not independently verified here.

**Executable sources:** [Common/Statistics/Statistics.cs:200–236](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Statistics/Statistics.cs#L200-L236); [Common/Statistics/PortfolioStatistics.cs:310–312](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Statistics/PortfolioStatistics.cs#L310-L312); [Optimizer/Strategies/StepBaseOptimizationStrategy.cs:162–168](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/Strategies/StepBaseOptimizationStrategy.cs#L162-L168)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Saved algorithm results and optimization analysis

Backtest result construction includes chart/order/P&L/statistics/configuration/state outputs; optimization tracks result IDs and parameters before computing parameter/family summaries.

**Limit:** The inspected output and optimizer paths do not establish equality of all market-input bytes, source/dependency revisions and statistical protocols across independent runs. Common run manifests are still needed; completed-result analysis alone omits null failures.

**Executable sources:** [Engine/Results/BacktestingResultHandler.cs:397–431](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Results/BacktestingResultHandler.cs#L397-L431); [Optimizer/LeanOptimizer.cs:263–288](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/LeanOptimizer.cs#L263-L288); [Optimizer/Analysis/OptimizationAnalyzer.cs:62–80](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/Analysis/OptimizationAnalyzer.cs#L62-L80)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**N/A** · Inspected · applicability `adapter_required` · capability `not_located`

**Scope:** Protected final holdout protocol

Native optimizer applies target/constraint selection to returned backtest results, while Train accepts arbitrary user code.

**Limit:** No native reserved single-use final holdout/freeze-before-access protocol was located in these scheduling/optimizer surfaces. A separate research adapter must distinguish repeated validation from untouched final evidence.

**Executable sources:** [Algorithm/QCAlgorithm.cs:3246–3261](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm/QCAlgorithm.cs#L3246-L3261); [Optimizer/Strategies/StepBaseOptimizationStrategy.cs:162–168](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/Strategies/StepBaseOptimizationStrategy.cs#L162-L168)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Benchmark-relative performance and economic generalization

Native portfolio statistics include benchmark beta/alpha/tracking/information ratios and a configurable risk-free-rate model; bounded online portfolio estimators and detailed execution engines can produce controlled experiments.

**Limit:** No matched independent comparison here establishes real-market predictive edge or exact live fill fidelity. The choice and availability of benchmark/universe/input revisions remain part of the experimental contract.

**Executable sources:** [Common/Statistics/PortfolioStatistics.cs:290–312](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Statistics/PortfolioStatistics.cs#L290-L312); [Algorithm.Framework/Portfolio/MaximumSharpeRatioPortfolioOptimizer.cs:89–137](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm.Framework/Portfolio/MaximumSharpeRatioPortfolioOptimizer.cs#L89-L137)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native optimization sensitivity analysis

OptimizationAnalyzer computes the distribution of completed Sharpe ratios, parameter slices, clustering and modes from the supplied parameter grid; it also summarizes failed/zero-order cases available in that collection.

**Limit:** These are optional post-search diagnostics over retained parsed results. They are not independent ablations, complete failed-search coverage, dependence-adjusted uncertainty or a mandatory holdout gate.

**Executable sources:** [Optimizer/Analysis/OptimizationAnalyzer.cs:35–80](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Optimizer/Analysis/OptimizationAnalyzer.cs#L35-L80)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Trusted algorithm assembly/Python extension loading.

The loader reads and loads the supplied algorithm assembly, resolves its algorithm type and creates an instance.

**Limit:** Algorithm code is trusted local code. The Isolator name does not imply a security sandbox; no untrusted-code process isolation or filesystem/network prohibition is established by this loader.

**Executable sources:** [AlgorithmFactory/Loader.cs:207–274](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/AlgorithmFactory/Loader.cs#L207-L274); [Common/Isolator.cs:62–79](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Isolator.cs#L62-L79)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Default algorithm order prechecks and configured security models.

Order prechecks reject warmup submissions, missing securities, zero/sub-lot quantity, nontradable securities and missing market data. Buying-power model errors produce unsuccessful order responses.

**Limit:** The .NET decimal-valued order path differs from float-based signal APIs; it is not evidence of equivalent validation for every custom data/model or Python boundary. Source timestamps and instrument metadata remain supplied inputs.

**Executable sources:** [Algorithm/QCAlgorithm.Trading.cs:844–876](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm/QCAlgorithm.Trading.cs#L844-L876); [Algorithm/QCAlgorithm.Trading.cs:942–955](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm/QCAlgorithm.Trading.cs#L942-L955); [Engine/TransactionHandlers/BrokerageTransactionHandler.cs:1216–1260](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/TransactionHandlers/BrokerageTransactionHandler.cs#L1216-L1260)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Engine Isolator runtime and managed-memory monitoring.

The engine runs algorithm work with maximum runtime and step-limit callbacks. Isolator samples managed GC memory, compares smoothed/spike limits and cancels/throws on exceeded limits; a nonpositive memory cap disables that memory limit.

**Limit:** GC.GetTotalMemory is not total process/Python/native-array RAM. Cancellation is cooperative, and polling permits overshoot; this is not a hard OS memory cap or hostile-code sandbox.

**Executable sources:** [Common/Isolator.cs:82–179](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Isolator.cs#L82-L179); [Engine/Engine.cs:352–390](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Engine.cs#L352-L390)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**Fails** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Public Compression.Unzip overwrite=true archive extraction boundary.

The overwrite branch combines the destination with entry.FullName and writes without checking resolved-path containment. A bounded native probe wrote an innocuous parent-relative marker to a sibling of the intended extraction directory and Unzip returned true.

**Limit:** All probe writes stayed inside a new temporary root. This proves the public helper boundary, not remote exploitability of ordinary data feeds. The non-overwrite branch uses .NET ExtractToDirectory; LocalObjectStore.SaveBytes has separate path/depth/storage guards.

**Executable sources:** [Compression/Compression.cs:539–564](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Compression/Compression.cs#L539-L564); [Engine/Storage/LocalObjectStore.cs:319–340](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Storage/LocalObjectStore.cs#L319-L340); [Engine/Storage/LocalObjectStore.cs:377–424](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Storage/LocalObjectStore.cs#L377-L424)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**N/A** · Inspected · applicability `adapter_required` · capability `not_implemented`

**Scope:** Selected native engine result/local object storage; full managed research workflow is a separate layer.

The selected local object store reads user-keyed bytes; it is not a content-addressed managed research manifest whose expected digest is recomputed on read.

**Limit:** N/A applies to this execution track only. A comparison requiring the complete Limen research contract must implement and audit an adapter; N/A is not a pass or evidence of repository-wide absence.

**Executable sources:** [Engine/Storage/LocalObjectStore.cs:290–310](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Storage/LocalObjectStore.cs#L290-L310); [Engine/Storage/LocalObjectStore.cs:600–621](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Storage/LocalObjectStore.cs#L600-L621)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**Partial** · Inspected · applicability `adapter_required` · capability `implemented`

**Scope:** LocalObjectStore byte persistence.

The store checks read/write permissions, key syntax/depth and expected aggregate bytes/file count; object reads return stored bytes.

**Limit:** Those admission checks do not establish expected content digests, round-reference integrity or malicious pickle safety in algorithm-defined content. A managed research artifact contract requires an adapter.

**Executable sources:** [Engine/Storage/LocalObjectStore.cs:290–310](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Storage/LocalObjectStore.cs#L290-L310); [Engine/Storage/LocalObjectStore.cs:319–371](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Storage/LocalObjectStore.cs#L319-L371); [Engine/Storage/LocalObjectStore.cs:377–435](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Storage/LocalObjectStore.cs#L377-L435)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Local storage writes and live brokerage startup reconciliation.

Local object persistence is serialized by a process-local lock and writes dirty entries. Brokerage startup fetches existing orders/holdings and returns an initialization failure when fetching open orders raises.

**Limit:** Individual WriteAllBytes calls are not an atomic research-log transaction or fsync frontier. Brokerage reconciliation does not restore arbitrary strategy state or prove exactly-once external order effects; no live brokerage was contacted.

**Executable sources:** [Engine/Storage/LocalObjectStore.cs:569–621](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Storage/LocalObjectStore.cs#L569-L621); [Engine/Setup/BrokerageSetupHandler.cs:400–436](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Setup/BrokerageSetupHandler.cs#L400-L436)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Algorithm worker exception and cancellation handling.

Algorithm exceptions set RuntimeError; enclosing Isolator errors also set RuntimeError and feed the engine error path. Monitor limits request cancellation rather than interpreting a failed callback as a successful run.

**Limit:** Cancellation need not stop uncooperative trusted code immediately. This row does not establish worker-process kill/restart equivalence, no-orphan guarantees or all optimizer/distributed-job behavior.

**Executable sources:** [Engine/Engine.cs:352–390](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Engine.cs#L352-L390); [Common/Isolator.cs:158–179](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Isolator.cs#L158-L179)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Framework Insight construction and order admission downstream.

Insight stores caller-supplied magnitude, confidence and weight; order prechecks later prevent submissions without security data. Model-specific portfolio processing determines how insight values are interpreted.

**Limit:** A universal finite/probability-bound/unavailable-signal guard is not established by the Insight constructor. The selected primitive's freely supplied metadata is a trusted-model boundary, not a proof that every portfolio model consumes an invalid value.

**Executable sources:** [Common/Algorithm/Framework/Alphas/Insight.cs:195–212](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Algorithm/Framework/Alphas/Insight.cs#L195-L212); [Algorithm/QCAlgorithm.Trading.cs:942–947](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Algorithm/QCAlgorithm.Trading.cs#L942-L947)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Default equity fill model, exchange state and staleness decision.

Equity market fills require an open exchange and use side-specific best-effort bid/ask plus slippage; a stale-data branch can wait for fresh data. Stop fills request a trade bar relative to order time.

**Limit:** The exact staleness, bar-resolution and custom fill-model policy matters. These checks do not authenticate feed timestamps, establish feature causality or prohibit trusted algorithm code from requesting external data.

**Executable sources:** [Common/Orders/Fills/EquityFillModel.cs:124–172](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Orders/Fills/EquityFillModel.cs#L124-L172); [Common/Orders/Fills/EquityFillModel.cs:203–218](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Orders/Fills/EquityFillModel.cs#L203-L218)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Configured native buying-power admission with ordinary non-null models.

The transaction handler requires sufficient portfolio buying power and returns an error on model failure or insufficiency. CashBuyingPowerModel accounts for reserved open orders, side-specific balances and order fees.

**Limit:** Instrument/account-specific margin semantics are model-dependent. NullBuyingPowerModel deliberately always returns sufficient, and custom models are trusted. No live liquidation or loss ceiling is inferred from this backtest admission property.

**Executable sources:** [Engine/TransactionHandlers/BrokerageTransactionHandler.cs:1216–1260](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/TransactionHandlers/BrokerageTransactionHandler.cs#L1216-L1260); [Common/Securities/CashBuyingPowerModel.cs:82–169](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Securities/CashBuyingPowerModel.cs#L82-L169); [Common/Securities/NullBuyingPowerModel.cs:28–40](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Securities/NullBuyingPowerModel.cs#L28-L40)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Native equity stop/market fills and custom slippage.

Equity stop-market fills use adverse opening-gap prices and apply the security's configured slippage model; otherwise they fill at the qualifying stop price.

**Limit:** The selected equity model is one instrument/fill route. It does not reconstruct every intrabar event, endogenous liquidity or queue priority, and other asset classes/custom models require separate matching.

**Executable sources:** [Common/Orders/Fills/EquityFillModel.cs:203–259](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Common/Orders/Fills/EquityFillModel.cs#L203-L259)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**Unknown** · Inspected · applicability `unknown` · capability `not_located`

**Scope:** Local engine/optimizer protected holdout governance.

No protected dataset reservation/exposure history was located in the bounded engine/optimizer inspection. Runtime limits and object storage do not establish this research admission rule.

**Limit:** The bounded inspection did not establish enforcement or prove repository-wide absence. Require an implementation pointer and executable acceptance results before treating this capability as present.

**Executable sources:** [Engine/Storage/LocalObjectStore.cs:319–371](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Storage/LocalObjectStore.cs#L319-L371); [Engine/Engine.cs:352–390](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Engine/Engine.cs#L352-L390)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Checked-in open-engine CI configuration.

The workflow builds/tests in a configured container with CPU/memory limits; dotnet tests have a hang timeout and crash collection.

**Limit:** The workflow uses a moving container tag, tagged checkout action and configured self-hosted runner; actual hosted protections, token scoping and dependency audit coverage were not verified. No secrets were read by this review.

**Executable sources:** [.github/workflows/gh-actions.yml:14–44](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/.github/workflows/gh-actions.yml#L14-L44)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Native timeout assertions and a bounded archive boundary reproduction.

Isolator tests assert TimeoutException for long-running C#/Python work. The separate native ZIP probe confirms the public overwrite helper's containment failure against the built pinned assembly.

**Limit:** The candidate test suite was not run by this safety campaign; timeout test presence does not establish termination of every arbitrary callback or mutation coverage. The archive probe tests a helper, not a live ingestion service.

**Executable sources:** [Tests/Common/IsolatorTests.cs:82–125](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Tests/Common/IsolatorTests.cs#L82-L125); [Compression/Compression.cs:539–564](https://github.com/QuantConnect/Lean/blob/d4cac37514427c84d40064cecbf3f0e6be4b0137/Compression/Compression.cs#L539-L564)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

