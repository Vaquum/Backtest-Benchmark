# Vaquum/Limen: code assessment and comparison framework

Assessment date: 19 October 2026 · Package version: 5.40.1

Pinned implementation: 29837e666604eee74a2ac94f328fb9803724342a

## 1. Assessment

Limen implements substantial infrastructure for computational financial research: configurable preparation and model execution, search, two distinct simulation paths, output recording and recovery, temporal evaluation, statistical diagnostics, and restricted frozen holdout assessment. Those mechanisms are substantive implementation. Their guarantees depend on the admitted execution path and configuration, and several important mechanisms cannot be combined.

The performance conclusion is workload specific. Two small snapshot workloads passed an independent cash-and-quantity execution oracle and had warm full-snapshot medians of 2.150025 ms and 1.699665 ms for 8,783 evaluated bars. A fitted-preparation ablation reduced target/scaler fits from 24 to 1 without demonstrating an end-to-end speed gain. No competitor was benchmarked, and parallel scaling, event throughput and large-history recovery remain unmeasured.

The most consequential scientific finding is a reproducible causal defect in a shipped feature used by native LightGBM preparation. With quantile_price_lines and include_research_only=False, appending later observations changed 173 of 192 earlier rows in the inspected configuration. The code computes a quantile threshold over the whole supplied frame and applies it to earlier line events. Separating training and evaluation frames does not remove future dependence within an evaluation frame. This finding prevents treating every native feature path as a causal predictor. It does not measure the amount of any resulting backtest inflation.

The safety conclusion depends on the threat model. Limen has meaningful local research integrity, execution admission, corruption rejection and recovery controls. It does not establish a hostile-configuration sandbox. A namespace-prefixed path resolves to os.system, survives manifest validation and is bound as a data source. This review checked the object identity without invoking it. Additional issues include stale manifest URI resolution and an unbounded fractional-difference weight loop for nonfinite parameters. Broker order safety was not established by the simulation and inference code assessed here.

The accompanying comparison workbook contains 42 scoped criteria, 28 measurement rows and 198 pinned code references. Its candidate fields are deliberately empty. It separates implementation status, observed evidence, capability coverage and quantitative outcomes; it contains no aggregate score that could average away a causal or security failure.

## 2. Evidence standard and review boundary

Only executable implementation, executable configuration, actual test assertions and local execution results support the findings. Documentation, README content, comments and docstrings are not treated as authority. Configuration is evidence only where executable code consumes it, such as the supplied model manifest or a CI workflow. Operating instructions were read to govern the review, not to substantiate product claims.

The reviewed source is pinned to the full commit above. Tracked source files were not changed. Package installation and test output were isolated from production systems. The benchmark environment reported Python 3.12.14, NumPy 2.2.6, pandas 2.3.3, Polars 1.42.1, scikit-learn 1.7.2 and LightGBM 4.6.0 on Linux x86_64. The virtual environment allowed system site packages: those research-library imports were verified inside the virtual environment, while build tools came from the primary runtime. It was not fully hermetic. Native thread pools were limited to one. Nine logical CPUs were exposed, but the physical CPU identity and effective container quota were not established; timing claims therefore remain local to this environment.

The campaign executed 82 selected test modules containing 1,771 distinct tests. Initially 1,768 passed and three failed because the package was not installed for subprocess/metadata access and the default temporary directory inherited the cloned Git context. An editable installation and a temporary directory outside that clone resolved those conditions. Only the three failures were rerun, and all three passed. No source change was made to obtain the result. This is 1,771 distinct targeted tests passing after setup correction, not a full-suite or hosted-CI pass claim. Combined selected statement coverage was 16,301 of 23,882 statements, 68.26%; that is coverage of this selected campaign, not an overall quality score.

The new benchmark and boundary-probe runs reused the unchanged repository fixture tests/fixtures/spot_1h_20240101_20241231.parquet. It contains 8,784 rows; its SHA-256 is a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72. The causal probe used prefixes of these rows. No new market observations were fabricated. Matching these bytes establishes reproducibility, not independent authentication of venue provenance.

Evidence labels have different meanings. Inspected means the relevant code path was traced. Tested means an existing assertion was executed locally. Reproduced means an independent, bounded counterexample was executed. Measured means a benchmark or quantity was actually collected. None implies formal verification or external empirical validation. The test campaign is recorded separately so that a broad pass count does not masquerade as proof of every grid row.

## 3. Canonical implementation model

### 3.1 The principal paths

UEL coordinates candidate parameters, preparation, model/rule execution, evaluation, recording and optional postprocessing. It accepts custom Python structure/function definitions as well as native manifests compiled from YAML. That flexibility makes trusted callback behavior part of the contract. The older ParamSpace path and the MSQ search strategies have different memory, sampling and reproducibility properties.

In the native Manifest path, raw input is admitted, an optional selector may run before splitting, and raw splits are formed before per-split bars, features and targets. Target/scaler state and PCA are fitted on training support and reused on later splits. Earlier raw context can support later rolling features. The implementation invokes generic feature functions and custom model code; it does not inspect their information use or prove their causality. Code anchors: [A02], [A03], [A05].

Snapshot execution provides array-based return and metric computations. Event execution uses explicit signal/observation availability, product and trade policies, source bindings, timer events, funding and an economic ledger. They are distinct execution contracts, including their treatment of terminal inventory. Recording stores results and increasingly structured evidence; resume reconstructs and validates committed history. Trainer and Sensor/Cohort paths reconstruct fitted models and produce inference outcomes with path-specific guards. Code anchors: [P07], [P08], [P12], [S09]–[S12].

### 3.2 Compatibility is part of the product contract

| Mechanism | Admitted implementation | Material composition limit |
| --- | --- | --- |
| Parallel rounds | Reconstructed, unchanged compiled CPU LogReg/LightGBM manifests; MSQ; frozen static sources; n_jobs=1 | Rejects factorization, custom callbacks and postprocessing; workers repeat preparation and model work |
| Factorization | Exact GridStrategy and conservative dependency checks; selected rule and DLinear/LightGBM snapshot paths | Opt-in; narrow feature, target, scaler and callback restrictions; fitted-preparation reuse is narrower again |
| Walk-forward | Configured anchored/rolling temporal folds; copied manifest and new fitted state per fold | Purge/embargo geometry is explicit; reserved holdout rejects this mode |
| Validation execution objective | Supported native binary models and event execution, with validation-aligned source evidence | Reducers must use the objective; its score is optimized on validation |
| Reserved holdout research | Admitted source prefix with retained local reservation/history | Rejects custom SFD, walk-forward, parallel, factorization, resume/profile, bars, callbacks, alternate test source and event/funding execution |
| Frozen final holdout | Exact native dated binary Sensor/Cohort with fitted LogRegBinary or LightGBMBinary state | No arbitrary model or event trade contract; repeated attempts are classified and retained |

These restrictions are enforced admissions, not merely documentation caveats. A comparison must record supported combinations. Crediting every mechanism as if all could run in one pipeline would overstate Limen's coverage; marking an unsupported required combination N/A would hide the same limitation. Code anchors: [P05], [P10], [A06], [A13], [S13].

## 4. Computation performance

### 4.1 Measurements with an independent execution contract

The existing backtest comparison harness ran only the Limen engine on buy-and-hold and the repository's SMA crossover. Both evaluated 8,783 bars and reserved the final real fixture bar for settlement. The contract was zero fees and slippage, all-in long/flat exposure, close timing, one-bar lag and terminal liquidation. This benchmark did not cover funding, shorts, stop execution, market impact or the event ledger.

The harness independently replayed cash, quantity and equity, checking each equity sample, held bar, fill bar, side and price before accepting a run. Equity tolerance was relative 1e-10 and absolute 1e-6 at initial equity 1,000,000. All samples passed. Each scenario used one fresh process and seven warm repetitions, so the results describe these runs rather than an estimated production latency distribution. Raw outputs and all samples are retained in the reproducibility kit. Code anchors: [P07], [A08]; measured record: evidence/performance/measurements.json.

| Timing or check | Buy and hold | SMA crossover |
| --- | ---: | ---: |
| First return-kernel call | 0.910244 ms | 0.893429 ms |
| Warm return-kernel median | 0.375106 ms | 0.342447 ms |
| Warm kernel plus common outputs median | 0.595398 ms | 0.520566 ms |
| First full-snapshot call | 2.384609 ms | 2.166230 ms |
| Warm full-snapshot median | 2.150025 ms | 1.699665 ms |
| Warm full-snapshot minimum–maximum | 2.106771–2.206992 ms | 1.612584–7.946189 ms |
| Adapter/import/preparation stage | 102.716028 ms | 85.407332 ms |
| Peak process RSS | 99.859375 MiB | 100.234375 MiB |
| Maximum absolute equity error | 7.82311e-8 | 1.23400e-8 |

The return kernel is a narrower operation than a full snapshot, and the adapter stage dominates the first-call kernel on these small inputs. Whole worker durations include repetitions and output persistence, so they are not process-to-first-result latency. The 7.946189 ms SMA observation remains in the record. Seven warm observations cannot support a reliable p95 service claim, and their within-process dependence must not be ignored.

### 4.2 Fitted-preparation reuse: mechanism verified, system benefit unproven

The existing factorized-preparation benchmark ran 48 rounds: 24 small, eight-tree LightGBM configurations, each at two fee values. Its lag range was 0 through 192 inclusive, producing 193 lag columns. Both arms enabled factorization. The ablation disabled only the fitted-target/scaler cache in one arm; it was not a comparison of all factorization off versus on.

| Quantity | Fresh fitted preparation | Reused fitted preparation |
| --- | ---: | ---: |
| Successful rounds | 48 | 48 |
| Target fits | 24 | 1 |
| Scaler fits | 24 | 1 |
| Model fits | 24 | 24 |
| Preparation calls | 24 | 24 |
| Internal campaign elapsed | 8.153872 s | 8.068698 s |
| Complete process elapsed | 10.552471 s | 10.597700 s |
| Peak process RSS | 358.746094 MiB | 362.976563 MiB |

Scientific outputs matched under the harness's 12-decimal normalization. The complete-process speed ratio, fresh divided by reuse, was 0.995732. There was no demonstrated end-to-end speed gain. This was one fixed-order fresh/reuse pair; the small timing difference is insufficient to conclude a stable slowdown either. Target and scaler fitting together accounted for roughly 0.20 seconds of the baseline's 8.15-second internal campaign, while model fitting accounted for about 5.17 seconds. The measured stage proportions explain why a 24-to-1 fit reduction need not materially change the system runtime. Code anchor: [P05]; measured record: evidence/performance/measurements.json.

### 4.3 Computational structure and likely scaling limits

Candidate generation differs materially by path. Legacy ParamSpace materializes the requested candidates and removes each consumed row by indexing and filtering the remaining Polars frame. Consuming k candidates therefore traverses approximately k(k+1)/2 row positions through these removal passes, in addition to construction. MSQ Grid avoids materializing the Cartesian product but retains accepted SHA-256 identities, so memory still grows with accepted candidates. Random/Sobol paths bound retry attempts and can exhaust before delivering all requested unique proposals. Enumeration comparisons must report accepted candidates and raw draws, not just requested permutations. The standard UEL ParamSpace path also does not forward a seed, while directly constructed ParamSpace and MSQ can be seeded. Code anchors: [P01], [P02].

Feature throughput depends on the actual kernel. SMA uses an O(n) NumPy scan; EMA/RSI retain Python recurrences. CCI and rolling regressions perform O(n × lookback) arithmetic. Line detection can examine O(n × min(n, horizon)) pairs and retain a large line pool. The DLinear implementation builds a dense decomposition of lagged return columns and fits a centered ridge solution with NumPy SVD; comparing it to an iterative neural trainer without matching its objective and design matrix would confuse architecture and implementation costs. Code anchors: [P06], [P09].

Reuse is not uniform. Serial computation reuse has an accounting budget, while factorized preparation and signal caches are bounded by 128 entries rather than bytes. Hashing, serialization, alignment copies and transform reconstruction still have costs on hits. Spawned workers reconstruct manifests and do preparation/model work each round; they do not share the parent's computation-reuse context. Factorization and parallel execution therefore cannot be assumed to deliver multiplicative speed benefits. Code anchors: [P05], [P10], [P11].

Parallel scheduling favors ordered recoverable history. The number of pending tasks is bounded by workers, and the parent waits for pending[0] before committing and refilling. A slow early round can leave workers idle after later tasks finish. Feedback and checkpoint boundaries drain pending work. These are understandable determinism/recovery choices, but speedup and efficiency on heterogeneous tasks must be measured. This review did not run a parallel scaling campaign. Code anchor: [P10].

Event plans cap eight plans and one million source events, but timers are generated afterward and the returned ledger can include their state rows. Funding can force per-timer processing. Thus a plan limit is not a ledger-output bound. Forward trade-outcome labels can simulate long and short suffixes from every row, approaching quadratic work if exits do not terminate early. Recording deduplicates identical blobs only after serialization and hashing, and recovery reconstructs committed history rather than providing constant-time restart. Code anchors: [P08], [P12], [S03].

A further numerical-comparison detail matters: the TA-Lib comparison helper drops NaNs independently from the two arrays before comparing values. Such an assertion can miss differing missing-value positions. Archived-Limen comparisons that retain whole arrays establish continuity with historical implementation, not independence of the oracle. Future benchmarks must compare the complete aligned time axis and null/NaN masks before numeric tolerances. Code anchor: [P06].

The performance baseline is therefore useful but incomplete: fast small snapshot computations, verified narrow reuse, identifiable scaling bottlenecks, and meaningful correctness contracts. External rankings, energy consumption, GPU/distributed performance, parallel utilization, large-event throughput and long-history recovery remain unknown.

## 5. Academic rigor and robustness

### 5.1 A causal feature failure with a controlled reproduction

quantile_price_lines detects lines over the complete supplied array, computes long/short quantile thresholds from those full pools, and assigns retained line ends to historical rows. Its filter executes heights >= np.quantile(heights, quantile). Later line heights can therefore change whether an earlier completed line was retained. include_research_only=False removes an active-span output but leaves the full-frame quantile selection in the other five outputs. The function is publicly exported and registered by native LightGBM preparation. Code anchor: [A01].

The independent probe compared the first 192 fixture rows calculated alone with the identical prefix calculated inside the first 384 rows. Parameters were max_duration_hours=48, min_height_pct=0.002, quantile_threshold=0.70 and include_research_only=False; relative and absolute tolerance were both 1e-12.

| Retained feature | Earlier rows changed | Maximum absolute difference |
| --- | ---: | ---: |
| hours_since_quantile_line | 56 | 37 |
| quantile_line_density_48h | 173 | 131 |
| quantile_momentum_6h | 105 | 1.406303026 |
| avg_quantile_height_24h | 157 | 0.027375197 |
| quantile_direction_bias | 92 | 1 |

In total, 173 of the original 192 rows changed in at least one retained output. The first divergence was row 19, at 2024-01-01 19:00 UTC, 172 rows before the prefix boundary. Density changed from 1 to 2 there. This is not just a difference at the last few partially observed line events. Controls using ordinary price_lines with research-only outputs excluded, and quantile_price_lines with quantile_threshold=0, both produced zero changed rows. The fixture-specific denominator is retained; 173/192 is not an estimated population failure rate. Measured record: evidence/academic/causal_prefix_probe.json.

Existing prefix tests cover other features, while quantile context tests exercise zero quantile and output omission. Passing those assertions does not establish nonzero-quantile causality. Split-first preparation and outcome-availability-aware stacking do not repair a feature matrix that already incorporates later observations. Empirical results using this feature computed over complete evaluation batches must be recomputed with point-in-time feature values before supporting an online predictive claim. Successive-prefix evaluation is a distinct path: using the final row of each available prefix can be causal and must be assessed on its own.

### 5.2 Genuine isolation and temporal evaluation safeguards

Raw splits precede native per-split preparation. Learned target parameters, scalers and PCA use training support. Walk-forward deep-copies the manifest and refits each fold. Existing tests assert distinct fitted objects and unchanged training/validation selection when held-out data are perturbed. Conditional direction/sizing stacking is particularly explicit: it fits only earlier signals whose long and short simulated outcomes are both available before the prediction block, and refits scaler/PCA inside each inner fold. These are meaningful local protections. Code anchors: [A02]–[A05].

Their scope remains bounded. An optional pre-split selector receives the admitted frame, generic feature functions can compute whole-frame statistics, and custom model code receives the prepared split dictionary. Walk-forward checks unique ordered timestamps and explicit train/validation/test gaps, but generic row-count purge is not automatically derived from every target's completion time. Built-in forward targets generate labels within physical splits and null unavailable tails; missing universal purge inference alone does not demonstrate cross-split leakage in those built-ins.

Validation calibration uses a frozen fitted classifier, then threshold selection uses the same validation sample. The supported execution objective checks alignment and clips observation/funding evidence to validation support. Those controls help isolate the test partition. The resulting optimized validation score is still a model-selection score, not an independent estimate of deployed utility. A candidate comparison should measure calibration and selection quality on separate untouched observations. Code anchor: [A06].

### 5.3 Statistical implementation is distinct from inferential validity

DSR validates finite one-dimensional returns with at least four observations and positive variance, then applies a sample-Sharpe calculation, skew/kurtosis adjustment and a trial-count benchmark. There is no serial-covariance or effective-time-sample correction in that formula. Its single-run trial inventory comes from retained successful return tracks. Failed, pruned, unrecorded, deleted and external experiments are not automatically represented by a complete return pool. Code anchors: [A08], [A10], [A11].

PBO evaluates a finite synchronous trial-by-bar matrix using equal contiguous blocks and complementary half-block partitions. It selects an in-sample Sharpe winner and assesses its out-of-sample rank, including explicit tie handling. It does not refit models or add purge/embargo inside this operation. The default is two blocks, giving only two nominal partitions and PBO values 0, 0.5 or 1. Four, six and eight blocks yield 6, 20 and 70 nominal partitions. Those overlapping partitions are not independent replications. Alternative in-repository formula assertions at tight tolerance check implementation consistency; they do not establish empirical false-positive calibration under serial dependence or adaptive search.

Acceptance reports calculate Boolean or unavailable verdicts, write them and return. The UEL caller ignores that return and continues. A false or unavailable DSR/PBO verdict does not automatically prevent Trainer or Sensor creation. Convergence reporting similarly records sklearn warning presence and frequency; a warned successful model can remain eligible. Reporting a statistic and enforcing an admission rule are different capabilities and are separate comparison criteria. Code anchors: [A09], [A11].

Family diagnostics provide a notable conservative control. They compare ordered timestamps, return evidence and execution identities, reconcile retained successes where inventory exists, and withhold conclusions for unknown or fragmented supplied coverage. Snapshot-family joint PBO is withheld where full comparable OHLC execution identity is absent. These checks improve integrity of the supplied family; they cannot discover hidden prior experiments or prove that the researcher supplied every relevant family. Code anchor: [A12].

### 5.4 Holdout accounting and metric semantics

The reserved holdout protocol owns a copy of supported fitted state, records specification/state digests, validates that state, and durably allocates an attempt before loading assessment data. Predictions are generated from successive raw prefixes. Started and failed attempts remain in the history, prior overlaps are tracked, and later or unknown exposure is explicitly classified. Those are stronger controls than simply naming a dataframe test. They are local accounting, however: repeated assessment is classified rather than prohibited, and external exposure remains unknown. The compatibility restrictions in Section 3 are essential to the claim. Code anchor: [A13], [S13].

Several metric conventions must be normalized before comparing libraries. Walk-forward aggregation averages finite numeric fold values arithmetically and skips nonfinite values. An averaged return is not necessarily the compounded return of a concatenated equity curve; averaged confusion counts are not pooled counts. balanced_metric means precision multiplied by the square root of positive-prediction rate, not balanced accuracy. Binary AUC uses probabilities, with one-class cases unavailable. The random-action reference emits scores 0.9/0.1 using global NumPy randomness, so it is not a calibrated probabilistic null. The parameter-correlation bootstrap resamples trial rows IID; it is not a block bootstrap of dependent market returns. Code anchors: [A07], [A14], [A15].

The resulting academic judgment is mixed in a precise way: substantial mechanisms for disciplined experiments, a concrete causal failure on a shipped path, conditional rather than universal selection diagnostics, and unmeasured empirical generalization. Code and passing tests can establish mechanism and implementation properties; they cannot establish profitable out-of-sample robustness across assets, eras or venues without the corresponding experiments.

## 6. Safety properties

### 6.1 Separate four threat models

For a trusted local researcher, useful questions concern input validation, causal execution, preserved evidence, unavailable outputs and recovery. For third-party manifests or datasets, the questions expand to callable authority, paths, network destinations and resource limits. For crashing or concurrent workers, commit consistency and cleanup matter. For capital-at-risk execution, independent broker and operational risk controls would need inspection. Success in one setting does not establish safety in the others.

### 6.2 Concrete boundary failures and inconsistencies

The resolver accepts strings beginning with an allowed namespace, then progressively imports and traverses attributes using unrestricted getattr. Because historical_data imports os, limen.data.historical_data.os.system resolves to the external command callable. The direct name os.system is rejected, while the prefixed name resolves, validates in a modified bundled manifest and binds as its source method. The dangerous callable was never invoked. This is a consequential boundary failure if a host treats another party's manifest as safe configuration; the review did not find or exercise a remotely exposed service. Code anchor: [S01]; reproduced record: evidence/safety/safety_boundary_results.json.

Manifest store resolution has a narrower integrity gap. canonical_manifest_id hashes content excluding lineage, but resolve_manifest_uri compares the stored filename with lineage.id without recomputing that content hash. In a disposable scratch store, changing only metadata.name while retaining lineage changed the actual hash but left the original manifest URI resolvable. Experiment metadata and family evidence do recompute identity, so the finding is not that all provenance is unchecked. Code anchor: [S05].

Fractional differencing accepts NaN through comparisons that only reject d < 0 or threshold <= 0. Its weight loop exits only when abs(weight) < threshold. With nonfinite order, or nonzero order and a NaN threshold, that condition remains false and the list keeps growing before data length is considered. This is a direct code-path proof; no unbounded invocation was attempted. Per-record and event-plan limits elsewhere do not supply a general process deadline or weight budget. Code anchor: [S03].

Input guards also vary by route. A direct snapshot call accepts negative fees and slippage that the native Manifest and event policy reject; the same fixture returns finite values, including a negative recorded cost with negative slippage. Negative fees could intentionally model rebates and negative slippage price improvement, so the finding is inconsistent admission without a common explicit policy. A zero-lag option alone is not proof of lookahead; the caller's signal-availability evidence determines whether it is valid. Code anchor: [S02].

PythonSensorBase checks finite values, probability bounds, output length and UTC ordered unique timestamps. Compiled Sensor scalar extraction lacks the same centralized finite/probability guard, although exceptions become unavailable sensor-error outcomes. No built-in model was observed producing invalid values in this review. A declared cutoff and callback metadata cannot prove a custom callback's information use. Code anchor: [S09].

### 6.3 Local integrity and simulated execution strengths

Round storage enforces digest/reference syntax, rejects malformed or corrupt records and checks consistency before resume mutates state. References are constrained to 64 hex characters, decompressed round members to 512 MiB, and market/signal blobs to 128 MiB. Existing corruption tests assert byte and modification-time preservation after rejection. These are substantial integrity and local resource controls, although they are neither authenticated external provenance nor a total experiment-size budget. Code anchor: [S06].

Parallel resume validates the committed prefix across settings, occurrence identities, parameters, predictions, market evidence and trade contracts before truncating uncommitted tails. Checkpoints use temporary-file replacement. Worker dispatch is bounded, native threads are restricted, failure paths clean up workers, and tests exercise termination and recovery phases. However, ordinary recording lacks fsync, a directory-wide competing-writer lock and a single transaction spanning all files. A 0.1-second future timeout is polling, not a round deadline; the test's 20-second shutdown assertion is not a production execution SLA. Code anchors: [S07], [S08].

Event admission checks finite positive OHLC, unique ordered identities/timestamps, nonoverlap, availability chronology, partition coverage and source bindings. Price-gap limits are optional. Trade policy constrains requested exposure/notional rate, lot rounding and affordability; spot shorts cannot borrow cash. Maintenance breach raises instead of simulating a complete liquidation system. A target exposure cap does not imply continuous rebalancing after market drift. Code anchors: [S10], [S11].

The event engine gives stop loss precedence if both barriers touch, handles adverse opening gaps, and requires an explicit flat signal before re-entry after a forced exit. It can reject insufficient intrabar evidence. These are explicit simulation conventions, not knowledge of the actual OHLC event ordering. Fixed slippage does not represent volume-dependent impact, queue position or partial fills. Snapshot charges closure of its final held segment, while event execution can mark remaining inventory; a comparison must align the terminal convention before interpreting return differences. Code anchor: [S12].

### 6.4 Network, dependencies and adversarial evidence

The main historical-data request path has a 60-second timeout and five retries but consumes the full response without a size quota. Local and HTTP(S) data paths do not establish general destination or filesystem containment. ZIP members are read rather than extracted to disk, so this review does not claim an extract-to-path traversal on that route. Decompression budgets are absent there, and an older Binance helper omits an explicit request timeout. Code anchor: [S04].

Checked-in workflows install hash-pinned dependencies, pin actions, configure Python CodeQL and configure release attestations/SBOM generation. This is executable configuration evidence, not observed live CI, repository protection or a current advisory audit. The vulnerability gate reads project dependencies without passing every optional research backend group or auditing every version allowed by a range. Fuzzing exercises parse plus validate, not compiled callbacks, with explicit text/time/RSS budgets. Specific property and corruption tests are useful, but their count cannot certify the untested callable boundary. Code anchors: [S14], [S15].

## 7. Repeatable framework for another open solution

### 7.1 Freeze a comparison contract before measuring

The unit of comparison is a pinned solution, exact configuration, workload and resource envelope. Record both commits and adapter diffs; dependency locks; hardware/runtime/thread limits; immutable input hash and ordered timestamps; seeds and candidate order; and required outputs and persistence. The attached JSON supplies a Limen baseline and blank candidate fields. Future comparisons should rerun both solutions together because machine conditions and dependency versions affect results.

Compare four layers separately: primitives/search; fixed-signal execution; end-to-end research and selection; and inference/final holdout. Mark capabilities native, adapted, unsupported or outside the agreed scope. An execution-only library can be compared fairly on an execution contract while recording research orchestration as an additional required layer. Adapter engineering and unsupported combinations remain visible; neither becomes a hidden runtime advantage.

For fixed-signal simulation, predeclare signal availability, bar alignment, fill reference, position sizing, rounding, costs, funding, stops, terminal settlement and missing-signal behavior. For learning, predeclare feature/target semantics, training support, horizon, folds, purge/embargo, calibration, objective, search budget and final untouched assessment. Equal model names do not establish equal work.

### 7.2 Apply validity checks before speed ranking

First compare output semantics, time alignment and null/NaN masks, then numerical values within declared tolerances. Recompute ledger quantities independently. Run predictor prefix-extension invariance at multiple real-data cutoffs after warmup, audit target completion times, and verify train/fitted-state support and selection isolation. A faster result failing the required contract is a failed comparison, not a speed winner.

Academic comparisons should distinguish formulas, numerical agreement, inferential assumptions and empirical outcomes. Record every attempted, successful, failed, pruned, repeated and unavailable trial category that can be established; unknown history remains unknown. Report effective support and dependence treatment for uncertainty. Quality metrics can include held-out Brier/log loss, paired net utility, drawdown and stability across predeclared costs/splits/seeds, but only after those outcomes have actually been measured under the same contract.

Safety comparisons should record which invalid inputs are rejected, the number of applicable mutation cases, whether rejection leaves storage unchanged, termination/orphan behavior and committed-prefix equivalence. Scope the adversary explicitly. Dangerous callable identity can be checked without invocation; a statically proven unbounded loop does not require allowing a process to exhaust memory to be a valid finding.

### 7.3 Measure comparable work and preserve uncertainty

Separate startup, first valid result, warm core, common-output normalization, full pipeline and persisted end-to-end work. Capture wall time, CPU time, peak process-tree memory, output bytes and failure rates. Sweep real-data prefix length, lookback, features, candidates, timer cadence and workers. Report actual admitted work, cache hits/misses and successful equivalent results.

A practical starting experiment design is ten independent fresh-process pairs in balanced A/B and B/A order, with thirty warm calls per process. These are protocol design choices, not universal sufficiency thresholds. Predeclare required precision or power, treat the process pair as the independent unit for timing uncertainty, and expand only to resolve that need. Preserve all raw values, outliers, failures and order. Use paired uncertainty for speed ratios; a nonsignificant difference does not establish equivalence without a declared equivalence margin.

For positive lower-is-better quantities, candidate advantage equals Limen value divided by candidate value. For higher-is-better quantities, it equals candidate divided by Limen. Values above one favor the candidate. Ratios are calculated only when both measurements exist, semantic compatibility is confirmed and the denominator is positive. Error/count comparisons use candidate-minus-Limen differences where division would obscure zero or meaning. Unknown, zero and N/A remain different states.

### 7.4 Record status and evidence separately

| Status | Meaning in this framework |
| --- | --- |
| Enforced | Checked on the specified admitted path or required by its contract; not universal across APIs |
| Optional | Exists but requires opt-in and compatible configuration; benefit may still be unmeasured |
| Partial | Some relevant properties/paths are covered, with explicit remaining gaps |
| Fails | A scoped property has a concrete counterexample or direct contradicting code path |
| Unknown | The conclusion has not been established; partial observations may still exist |
| N/A | Outside the agreed scope, with a reason; never a substitute for unsupported required capability |

For every criterion retain scope, Limen status and evidence, baseline result with units/denominator, candidate status/evidence/result, comparison protocol, limitations, exact source references and a final verdict. Verdicts are candidate better, equivalent within declared tolerance, Limen better, incomparable or unknown. Implementation categories are not numeric quality grades. Safety and validity failures are not averaged with speed; on common admitted workloads, present capability coverage and the quality/latency/memory tradeoff directly.

## 8. Interpretation and next priorities

For batch evaluation using the affected native feature path, the first priority is point-in-time quantile computation and causal tests covering deployed predictors. Candidate remedies include thresholds fitted only on prior training data or expanding/trailing thresholds over events available at the prediction time. Their exact semantics must be declared, affected batch results re-evaluated, and original evidence retained. This review did not modify Limen.

For third-party configuration use, resolve explicitly registered allowed callables rather than relying on textual namespace prefixes and transitive attributes. Recompute manifest content identity at URI resolution, with consistent behavior when content and lineage disagree. Bound fractional-difference weights and validate finiteness before entering iterative kernels. Align public numeric and inference admission policies across direct helpers and native routes. These are proposed remediation targets derived from the observed code, not completed fixes.

For research governance, make any desired statistical/convergence admission policy explicit and executable, document it through code/configuration, and preserve unavailable verdicts and search-history limits. For performance, measure the remaining scale-sensitive paths before increasing claims: candidate consumption, event/timer output, trade-label suffix work, parallel imbalance and history recovery. The existing narrow benchmark parity contract is a useful base to extend.

The assessment supports using Limen as a substantial research implementation with explicit local strengths and limitations. It does not support a universal performance lead, universal causal validity, a hostile-input sandbox or an inference-to-live-trading safety guarantee. The prepared grid makes those limits testable and comparable for the next solution at a pinned revision.

## Appendix A. Comparison criterion inventory

The full editable rows, protocols, limitations and source ranges are in Limen_Comparison_Grid.xlsx and baseline/limen_baseline.json in the reproducibility kit. The inventory below keeps the baseline dimensions visible in this report.

The companion archive includes the unified baseline and protocol, original benchmark reports/logs and raw samples, targeted-test manifests and JUnit/runtime results, and portable bounded reproduction scripts. Its README distinguishes originally captured commands from reconstructed rerun instructions and describes the three environment setup failures. It does not include a repository or dependency-environment copy; the pinned repository and hash-locked research requirements identify those inputs. Inspect the fixture digest before rerunning. The candidate baseline is unfilled because no other solution was assessed in this review.

### Computation performance

| ID | Criterion | Limen status |
| --- | --- | --- |
| P01 | Parameter-space construction and retained memory | Partial |
| P02 | Candidate generation throughput, novelty and exhaustion | Partial |
| P03 | Cold process and first valid result latency | Unknown |
| P04 | Complete research campaign throughput and stage attribution | Unknown |
| P05 | Fitted preparation and prediction reuse | Optional |
| P06 | Indicator and feature kernel throughput by n and lookback | Partial |
| P07 | Snapshot backtest latency under full execution parity | Enforced |
| P08 | Event execution and forward-label scaling | Partial |
| P09 | Peak memory and resource amplification | Partial |
| P10 | Parallel speedup, efficiency and load imbalance | Optional |
| P11 | Cache locality, hit cost and optimization coverage | Partial |
| P12 | Recording/checkpoint overhead and restart recovery | Partial |

### Academic rigor/robustness

| ID | Criterion | Limen status |
| --- | --- | --- |
| A01 | Causal predictor invariance | Fails |
| A02 | Training and evaluation isolation | Partial |
| A03 | Label availability and censoring | Partial |
| A04 | Temporal split geometry | Partial |
| A05 | Fold-local preprocessing and stacking | Enforced |
| A06 | Calibration and threshold selection | Partial |
| A07 | Metric definitions and aggregation | Partial |
| A08 | Numerical and mathematical verification | Partial |
| A09 | Convergence and fit stability | Partial |
| A10 | Search-family history completeness | Partial |
| A11 | Multiple-selection and dependence control | Partial |
| A12 | Cross-run evaluation comparability | Partial |
| A13 | Final holdout protocol and compatibility | Partial |
| A14 | Baseline quality and external validity | Unknown |
| A15 | Sensitivity, ablation and reproducibility | Partial |

### Safety properties

| ID | Criterion | Limen status |
| --- | --- | --- |
| S01 | Untrusted configuration callable boundary | Fails |
| S02 | Input schema and numeric admission consistency | Partial |
| S03 | Algorithm and process resource bounds | Fails |
| S04 | Data source network, archive and path boundaries | Partial |
| S05 | Manifest content-address verification on read | Partial |
| S06 | Recorded round corruption and reference integrity | Enforced |
| S07 | Crash/restart consistency and durable commit frontier | Partial |
| S08 | Parallel worker failure handling and bounded dispatch | Enforced |
| S09 | Inference output validity and unavailable-signal behavior | Partial |
| S10 | Execution chronology and source evidence admission | Enforced |
| S11 | Economic affordability, exposure and quantity constraints | Enforced |
| S12 | Exit rules, gap treatment and execution uncertainty | Partial |
| S13 | Protected holdout reservation and exposure accounting | Enforced |
| S14 | Executable supply-chain and security CI coverage | Partial |
| S15 | Adversarial validation evidence and mutation coverage | Partial |


## Appendix B. Code evidence index

Bracketed criterion identifiers in this report map to the workbook and JSON. The links below point to selected directly relevant source ranges at the pinned commit. The workbook Evidence tab contains all 198 range references, including tests. Local measurement files are retained separately so that implementation claims and observed outcomes can be checked independently.

**P01 · Parameter-space construction and retained memory**

[limen/utils/param_space.py:73–109](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/utils/param_space.py#L73-L109); [limen/experiment/param_search/grid_strategy.py:36–61](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/param_search/grid_strategy.py#L36-L61)

**P02 · Candidate generation throughput, novelty and exhaustion**

[limen/utils/param_space.py:132–144](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/utils/param_space.py#L132-L144); [limen/experiment/param_search/search_strategy.py:130–175](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/param_search/search_strategy.py#L130-L175)

**P03 · Cold process and first valid result latency**

[tests/backtest_benchmark/worker.py:78–105](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/backtest_benchmark/worker.py#L78-L105); [tests/benchmark_backtest_strategies.py:141–156](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/benchmark_backtest_strategies.py#L141-L156)

**P04 · Complete research campaign throughput and stage attribution**

[limen/experiment/experiment_core.py:294–371](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L294-L371); [limen/experiment/experiment_core.py:579–599](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L579-L599)

**P05 · Fitted preparation and prediction reuse**

[limen/experiment/_factorize.py:80–123](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_factorize.py#L80-L123); [limen/experiment/_factorize.py:177–273](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_factorize.py#L177-L273)

**P06 · Indicator and feature kernel throughput by n and lookback**

[limen/indicators/sma.py:10–31](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/indicators/sma.py#L10-L31); [limen/indicators/_ema.py:16–36](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/indicators/_ema.py#L16-L36)

**P07 · Snapshot backtest latency under full execution parity**

[limen/backtest/long_flat_strategy.py:96–133](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/long_flat_strategy.py#L96-L133); [tests/backtest_benchmark/contract.py:49–89](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/backtest_benchmark/contract.py#L49-L89)

**P08 · Event execution and forward-label scaling**

[limen/backtest/_event_plan.py:21–67](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/_event_plan.py#L21-L67); [limen/backtest/_event_clock.py:10–33](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/_event_clock.py#L10-L33)

**P09 · Peak memory and resource amplification**

[limen/utils/_computation_cache.py:23–64](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/utils/_computation_cache.py#L23-L64); [limen/experiment/_factorize.py:227–233](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_factorize.py#L227-L233)

**P10 · Parallel speedup, efficiency and load imbalance**

[limen/experiment/_parallel_rounds.py:43–63](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_rounds.py#L43-L63); [limen/experiment/_parallel_rounds.py:167–237](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_rounds.py#L167-L237)

**P11 · Cache locality, hit cost and optimization coverage**

[limen/utils/_computation_cache.py:32–49](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/utils/_computation_cache.py#L32-L49); [limen/utils/_computation_cache.py:86–122](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/utils/_computation_cache.py#L86-L122)

**P12 · Recording/checkpoint overhead and restart recovery**

[limen/experiment/experiment_core.py:672–739](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L672-L739); [limen/experiment/_parallel_commit.py:125–139](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_commit.py#L125-L139)

**A01 · Causal predictor invariance**

[limen/features/quantile_price_lines.py:146–189](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/features/quantile_price_lines.py#L146-L189); [limen/sfd/foundational_sfd/lightgbm_binary.py:82–103](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/foundational_sfd/lightgbm_binary.py#L82-L103)

**A02 · Training and evaluation isolation**

[limen/experiment/manifest_core.py:1888–1907](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/manifest_core.py#L1888-L1907); [limen/experiment/manifest_core.py:1647–1658](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/manifest_core.py#L1647-L1658)

**A03 · Label availability and censoring**

[limen/targets/next_return.py:39–42](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/targets/next_return.py#L39-L42); [limen/targets/next_bar_up.py:34–37](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/targets/next_bar_up.py#L34-L37)

**A04 · Temporal split geometry**

[limen/data/utils/split_walk_forward.py:48–67](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/utils/split_walk_forward.py#L48-L67); [limen/experiment/_walk_forward_split.py:63–88](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_walk_forward_split.py#L63-L88)

**A05 · Fold-local preprocessing and stacking**

[limen/experiment/_walk_forward_run.py:152–165](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_walk_forward_run.py#L152-L165); [limen/sfd/reference_architecture/direction_sizing.py:163–188](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/reference_architecture/direction_sizing.py#L163-L188)

**A06 · Calibration and threshold selection**

[limen/calibration/probability.py:17–42](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/calibration/probability.py#L17-L42); [limen/calibration/pipeline.py:61–69](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/calibration/pipeline.py#L61-L69)

**A07 · Metric definitions and aggregation**

[limen/metrics/binary_metrics.py:53–64](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/metrics/binary_metrics.py#L53-L64); [limen/experiment/_walk_forward_run.py:107–121](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_walk_forward_run.py#L107-L121)

**A08 · Numerical and mathematical verification**

[limen/metrics/deflated_sharpe_ratio.py:24–55](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/metrics/deflated_sharpe_ratio.py#L24-L55); [limen/metrics/probability_of_backtest_overfitting.py:37–58](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/metrics/probability_of_backtest_overfitting.py#L37-L58)

**A09 · Convergence and fit stability**

[limen/experiment/convergence_report.py:33–52](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/convergence_report.py#L33-L52); [limen/experiment/convergence_report.py:55–91](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/convergence_report.py#L55-L91)

**A10 · Search-family history completeness**

[limen/experiment/acceptance_report.py:86–100](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/acceptance_report.py#L86-L100); [limen/experiment/experiment_core.py:365–368](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L365-L368)

**A11 · Multiple-selection and dependence control**

[limen/metrics/deflated_sharpe_ratio.py:33–55](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/metrics/deflated_sharpe_ratio.py#L33-L55); [limen/metrics/probability_of_backtest_overfitting.py:47–58](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/metrics/probability_of_backtest_overfitting.py#L47-L58)

**A12 · Cross-run evaluation comparability**

[limen/experiment/acceptance_report.py:36–83](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/acceptance_report.py#L36-L83); [limen/experiment/_family_evidence.py:130–171](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_family_evidence.py#L130-L171)

**A13 · Final holdout protocol and compatibility**

[limen/experiment/_holdout_research.py:71–100](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_research.py#L71-L100); [limen/experiment/_holdout_research.py:225–240](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_research.py#L225-L240)

**A14 · Baseline quality and external validity**

[limen/sfd/rule_based/common_strategies.py:17–34](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/rule_based/common_strategies.py#L17-L34); [limen/sfd/rule_based/common_strategies.py:72–139](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/rule_based/common_strategies.py#L72-L139)

**A15 · Sensitivity, ablation and reproducibility**

[limen/experiment/manifest_core.py:1551–1605](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/manifest_core.py#L1551-L1605); [limen/log/_experiment_parameter_correlation.py:123–140](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/log/_experiment_parameter_correlation.py#L123-L140)

**S01 · Untrusted configuration callable boundary**

[limen/yaml/resolver.py:39–55](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/resolver.py#L39-L55); [limen/data/historical_data.py:3–20](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/historical_data.py#L3-L20)

**S02 · Input schema and numeric admission consistency**

[limen/yaml/parser.py:24–69](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/parser.py#L24-L69); [limen/yaml/rules.py:253–279](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/rules.py#L253-L279)

**S03 · Algorithm and process resource bounds**

[limen/features/fractional_diff.py:30–40](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/features/fractional_diff.py#L30-L40); [limen/features/fractional_diff.py:74–97](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/features/fractional_diff.py#L74-L97)

**S04 · Data source network, archive and path boundaries**

[limen/data/historical_data.py:71–73](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/historical_data.py#L71-L73); [limen/data/historical_data.py:302–322](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/historical_data.py#L302-L322)

**S05 · Manifest content-address verification on read**

[limen/yaml/store.py:45–47](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/store.py#L45-L47); [limen/yaml/store.py:175–186](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/store.py#L175-L186)

**S06 · Recorded round corruption and reference integrity**

[limen/experiment/_round_storage.py:28–45](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_round_storage.py#L28-L45); [limen/experiment/_round_storage.py:54–78](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_round_storage.py#L54-L78)

**S07 · Crash/restart consistency and durable commit frontier**

[limen/experiment/checkpoint_manager.py:282–300](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/checkpoint_manager.py#L282-L300); [limen/experiment/_parallel_commit.py:123–135](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_commit.py#L123-L135)

**S08 · Parallel worker failure handling and bounded dispatch**

[limen/experiment/_parallel_worker.py:101–129](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_worker.py#L101-L129); [limen/experiment/_parallel_worker.py:148–191](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_worker.py#L148-L191)

**S09 · Inference output validity and unavailable-signal behavior**

[limen/inference/_python_sensor.py:65–100](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/inference/_python_sensor.py#L65-L100); [limen/inference/_python_sensor.py:104–133](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/inference/_python_sensor.py#L104-L133)

**S10 · Execution chronology and source evidence admission**

[limen/backtest/execution_events.py:20–51](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/execution_events.py#L20-L51); [limen/backtest/execution_events.py:60–108](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/execution_events.py#L60-L108)

**S11 · Economic affordability, exposure and quantity constraints**

[limen/backtest/trade_contract.py:26–47](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_contract.py#L26-L47); [limen/backtest/trade_contract.py:107–126](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_contract.py#L107-L126)

**S12 · Exit rules, gap treatment and execution uncertainty**

[limen/backtest/trade_execution.py:97–117](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_execution.py#L97-L117); [limen/backtest/trade_execution.py:191–211](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_execution.py#L191-L211)

**S13 · Protected holdout reservation and exposure accounting**

[limen/experiment/_holdout_history.py:90–137](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_history.py#L90-L137); [limen/experiment/_holdout_history.py:196–250](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_history.py#L196-L250)

**S14 · Executable supply-chain and security CI coverage**

[.github/workflows/pr_checks_lint.yml:38–61](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/.github/workflows/pr_checks_lint.yml#L38-L61); [.github/workflows/pr_checks_lint.yml:83–103](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/.github/workflows/pr_checks_lint.yml#L83-L103)

**S15 · Adversarial validation evidence and mutation coverage**

[fuzz/fuzz_yaml_manifest.py:9–35](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/fuzz/fuzz_yaml_manifest.py#L9-L35); [.github/workflows/fuzz_smoke.yml:30–37](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/.github/workflows/fuzz_smoke.yml#L30-L37)


