# Limen academic robustness: code delta and independent rerun

**Latest:** 25e47866422d007da55cb19625344183599ba671, assessed 29 October 2026. **Baseline:** 29837e666604eee74a2ac94f328fb9803724342a, the retained 19 October benchmark pin. This compares against the actual benchmark baseline, not an exact fourteen-day interval. Executable source, tests, configuration and retained executed probes establish behavior. Documentation, comments and release narratives do not.

## Assessment

Limen has made substantive progress in research-workflow integrity. The clearest independently demonstrated improvement is the repair of the quantile-line feature's use of future observations. The code also strengthens inner-fold preprocessing, validation decisions, trial identity, protected research composition and observed execution-cost scenarios. These changes improve supported experiments' trustworthiness. They do not establish that the additional models predict better, that selected strategies generalize, or that probabilities and simulated market fills are empirically calibrated.

**A01 changes from Fails to Partial:** the demonstrated local feature defect is repaired, while arbitrary feature functions and pre-split selectors remain outside a general causal guarantee. **A05 remains Enforced within its original native fold-local scope. A14 remains Unknown** because independent model-quality and external-validity evidence is absent. The other twelve criteria remain Partial, with substantive improvements within that broad class. These are scoped assurance classes, not numerical quality scores. The [structured delta](academic_delta.json) contains all fifteen criteria and 133 validated, pinned current/baseline source references.

## Independently confirmed causal-feature repair

For positive quantiles, the implementation now computes a separate expanding threshold for each direction using lines completed through the current row, then evaluates the existing trailing aggregates against that row's threshold. This affects hours-since-line, density, momentum, average height and direction bias. Both research-flag modes give those five columns the same meaning. The zero-quantile path remains separate. [Output and routing][quantile-output] · [expanding thresholds and row evaluation][quantile-causal]

The independent probe admits each exact source pin, requires clean tracked files and verifies the original recorded fixture SHA256 a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72. It compares the first 192 observations evaluated alone with the same historical rows after extension to 384 unchanged market observations. No prices were synthesized.

| Recorded-fixture case | Baseline changed rows | Latest changed rows |
|---|---:|---:|
| Ordinary price_lines; research-only output excluded | 0 / 192 | 0 / 192 |
| Quantile lines; q = 0; research-only output excluded | 0 / 192 | 0 / 192 |
| Quantile lines; q = 0.7; five end-event columns | 173 / 192 | 0 / 192 |
| Quantile lines; q = 0.8; five end-event columns | 138 / 192 | 0 / 192 |

The positive-quantile results hold with either value of include_research_only. Latest historical values also match **160 scalar values** from the last available row of the frozen baseline evaluated on successive prefixes: four quantiles, eight cutoffs and five columns. There were **zero mismatches** at relative and absolute tolerances of 1e-12; maximum absolute difference was 1.2789769243681803e-13. This checks preservation of the original available-prefix meaning, as well as invariance to appended data. [Retained comparison](causal-prefix-comparison.json) · [portable probe](probe_causal_prefix.py) · [cross-version checker](compare_causality_reports.py)

The explicitly research-only active_quantile_count remains retrospective. Extension changes 192 rows at q = 0.7 and 150 at q = 0.8 in both revisions. Our receipts record matching counts, maximum differences and first divergences, without claiming a separate complete-byte equality proof for that column. The native test source additionally compares it with the archived implementation. The public flag still defaults to including that research-only output. This is a narrowly scoped repair, not a claim that every output is a live-safe predictor. [Research-only branch][quantile-output] · [native assertions][quantile-tests]

These changed-row counts describe one recorded fixture/configuration, not a population defect rate. The pre-split selector still receives the admitted complete research frame, and feature functions remain caller code. [Preparation order][prepare]

## Fitting, target availability and validation decisions

Raw splitting still precedes per-split feature construction and fitted preprocessing. New dated-window admission checks raw, formed and retained stages and refuses a declared positive partition that becomes empty. Hosted-bar endpoint checks cover the recognized native source and interval grid; arbitrary custom-source timing is not self-validating. Ratio splitting still uses supplied row order. [Split and transform order][split-transform] · [dated support][dated] · [split dispatch][split]

Inner-fold preparation now refits automatic fractional-difference shims using feature history available before the first prediction cutoff, then fits scaler/compression state on retained training rows and applies it to prediction rows. Original row identity and order are checked. This avoids reusing an automatic shim estimated on the entire outer training population within every inner fold. Raw features have already been computed, however, and unsupervised shim estimation uses the available feature prefix, which need not equal the label-eligible supervised subset. [Inner-fold preparation][fold-prep]

Formed bars recover contiguous raw constituents, verify OHLC aggregation and use the latest constituent availability. Linked classifiers require the native next-bar target and a regular observation interval; each upstream fit excludes labels unavailable at the first prediction decision. Allocation opportunities retain actual completion time and only supply an outcome when the episode closes before its opening-block boundary. These are native contracts, not inference of arbitrary target horizons or automatic purge/embargo geometry. [Formed support][bar-support] · [chronological linkage][chrono-link] · [allocation outcomes][allocation-outcomes]

Validation receipts bind original ordered inputs/labels, the fitted calibrator's actual probabilities and resulting decisions. Threshold admission recomputes the selected objective and requires the chosen decision vector to have been evaluated. Explicit prediction evidence is bound to original row/source identity and output mode; fitted predictions must repeat on the admitted inputs. These checks improve integrity. Calibration and threshold search can still share validation observations, so the optimized score remains selection evidence. Stable bytes and finite probabilities do not demonstrate calibration on untouched data. [Calibration receipts][calibration] · [optimizer checks][optimizer] · [validation evidence][validation]

## Protected research is broader than final holdout eligibility

Protected research now handles selected fold lineage, source/formed-bar support, factorized reuse, worker authority and checkpoint/Trainer history. Optional fold evidence binds typed source content, original/retained membership, output contract and fitting/selection cutoffs. Reconstruction refuses incompatible evidence. This does not prove that all cross-run families ask the same economic question; snapshot family evidence still marks joint PBO unavailable without complete execution identity. [Fold witnesses][fold-witness] · [reconstruction][fold-read] · [protected composition][composition] · [family limit][family]

Final holdout remains narrower. Freeze requires exact LogRegBinary or LightGBMBinary wrappers and admitted estimator/calibrator state with ordinary dated native binary inference. Effective manifests carrying formed bars, split_walk_forward, alternate test sources, extensions or nonunit decoder lookback are rejected. A contract-bearing single Sensor is supported; contract-bearing Cohorts are not. Final contract assessment also rejects funding, external execution sources and dynamic barriers. Attempt allocation still precedes data loading. These restrictions must accompany claims of broader protected research support. [Final model/pipeline checks][freeze] · [contract candidates][holdout-events] · [execution restrictions][holdout-policy] · [attempt-before-load][holdout-attempt]

## Trial history, metrics and inferential limits

Parameter domains/context cannot use reserved bookkeeping or objective names. Successful results cannot overwrite parameters or bookkeeping. Type-aware identities and restored-prefix checks reduce ambiguity. Optional record-on-error retains bounded failures for ordinary unprotected serial MSQ, checks policy on resume, requires an initial success and keeps protected/storage/evidence errors fatal. It cannot recover hidden, deleted, external or uncommitted searches. Failed models do not produce valid return tracks. [Field admission][fields] · [error policy][round-errors]

PBO admission removes the restriction to block counts 2, 4, 6 and 8, accepting literal even counts of at least two subject to support checks. Geometry reporting handles unavailable or unrenderable combinations explicitly. The default remains two blocks; DSR/PBO remain diagnostics over the retained comparable family. More blocks create more partitions, not more independent market evidence. This does not solve serial dependence, reveal unrecorded selection or create an automatic promotion gate. [Block configuration][pbo-settings] · [geometry][pbo-geometry]

The confusion helper now refuses declared nonbinary modes and nonbinary paired values. Core walk-forward summaries still average finite numeric fold results arithmetically: averaged fold returns are not pooled compounding, averaged counts are not a pooled confusion matrix, and finite-only averaging can omit unavailable folds. Convergence warnings remain diagnostics rather than a shared fit-quality gate. [Confusion admission][confusion] · [fold averaging][averages] · [convergence report][convergence]

## Observed-cost scenarios: a substantive new validity tool

CostCalibration.from_history validates normalized observed facts and freezes a cutoff-bound report. Estimation excludes required price/reference evidence received after the cutoff. It computes reference-notional-weighted price costs, separates buy/sell support, and reports parent/account concentration, effective parent count and empirical parent-cost quantiles. Admission requires at least 20 observed parents and three fill days per side; low effective support gets a distinct disposition. Those support rules do not establish that the sample represents future trading. [Frozen report API][cost-api] · [estimators and sensitivity][cost-statistics] · [receipt/support admission][cost-admission]

Comparison checks declared venue, environment, product and reference convention. Each replay observation must match the benchmark price phase, time and availability; unsupported barrier extrema are refused. It runs the frozen candidate under its original policy and an observed-slippage scenario, replacing only slip_bps and retaining the candidate fee model. It records content identities and separates unavailable scenarios from economic failures, so unsupported transfer need not be mistaken for a poor return. [Scenario admission][cost-match] · [replay][cost-compare]

The selected history can be concentrated, account-specific and incomplete at whole-order level. The emitted clock retains assumed exchange-label timing with unknown historical delivery. Maker/account fees are not transferred. Leave-one-day-out ranges and jackknife standard errors have no coverage guarantee. Deterministic recorded-fixture tests can establish arithmetic, admission and replay behavior; they do not independently establish representative costs, future cost survival or live fill fidelity. **A14 remains Unknown**, while A15 records the additional controlled sensitivity mechanism. [Computed support and emitted limitations][cost-admission]

## New models and robustness mechanisms

| Surface | Implemented behavior and scientific boundary |
|---|---|
| Feature/weight linkage | Chronological out-of-fold logistic probabilities feed a downstream feature or sample-weight construction. Named raw return windows, the native next-bar target and regular times are required; outer learned scaling/PCA is refused. This is a narrow linkage protocol, not demonstrated predictive improvement. [Cutoff logic][chrono-link] · [feature linkage][feature-link] · [weight linkage][weight-link] |
| Pseudo-label model | A content-pinned recorded pool must be disjoint from train/validation/test and inside declared chronology. Confident upstream predictions create explicitly identified training labels. Protected holdout research is refused. Observations are not generated; confidence is not an empirical error guarantee. [Pool admission][pseudo-pool] · [training][pseudo-model] |
| Residual regressor | Ridge fits observed training targets; XGBoost fits its in-sample training residuals. Optional early stopping uses validation residuals. Predictions add the scaled correction. This is not out-of-fold stacking. [Implementation][residual] |
| Gaussian HMM | Fits current training returns, then evaluates each test row's completed lag window using its final state and one transition. It does not smooth across the entire future test batch. Convergence and probability quality remain unverified here. [Implementation][hmm] |
| CNN1D/LSTM | Named chronological windows, training-only normalization, local seeded random state and fixed epoch/minibatch budgets. Each prediction uses its own completed window. Bidirectionality within that window does not itself expose later test rows. No shared loss-stability gate. [Shared preparation/training][sequence] |
| Entropy/VaR regressor | Features include binary negative-return-frequency entropy; quantile regression fits observed targets and reports pinball loss and violation rate. Neither nominal tail coverage nor a full return distribution is established. [Implementation][var] |
| Bayesian cohort | Uses outside-selection binary correctness evidence and Beta-Bernoulli mean weights in a fixed weighted vote. It checks availability and identity; it is not a joint dependence model or calibrated ensemble probability. [Implementation][bayesian] |
| Allocation | Builds recorded primary opportunities/outcome availability under regular co-timed target-exposure execution. It rejects protected holdout, walk-forward, formed bars, alternate sources and several custom extensions. [Outcomes][allocation-outcomes] · [admission][allocation-admit] |

The new regime classifier processes ordered observations with per-series trailing state and ranks current values against prior history before inserting them. Checkpoints bind formula/configuration identity. This is a concrete causal construction, while regime labels remain a specified classification system rather than an empirically universal taxonomy. Retrospective regime-block sampling is separate. [Sequential classifier][regime] · [prior-history ranks][regime-ranks]

Target horizon/threshold perturbations are seeded from permutation identity, smoothing changes training labels only, and incompatible factorized reuse is refused. These mechanisms make declared perturbation experiments repeatable; matched outcomes still matter when changing the target definition. Parameter importance keeps duplicate configurations in the same group, holds out configurations, fits categorical encoding only on training rows and repeats permutation importance on a random-forest surrogate. It diagnoses the retained experiment log, not chronological market generalization, causal feature effect or dependence-aware strategy-return uncertainty. [Target perturbation][perturbation] · [surrogate importance][importance]

## Evidence status

The two-revision quantile probe and 160-value semantic comparison executed successfully. The [structured delta](academic_delta.json) records their raw receipts, identities, exact invocation receipt and initial setup errors. The first receipt attempt incorrectly queried the import name limen as a distribution. The corrected distribution is vaquum-limen: both environments have metadata, versions 5.40.1 and 5.46.2. That setup mistake is not a source-code defect.

The completed native Linux suite at the exact latest pin collected and executed **7,391 tests: 7,388 passed, zero failed and three skipped**. All four worker receipts reconcile. The runtime profile records **160.391127 seconds** for the suite; this is regression-suite duration, not a comparative performance result. The three skips are the CUDA XGBoost case and two TabPFN cases. All 58 distinct modules mapped to A01–A15 are present and passed, covering 1,523 distinct tests; per-criterion totals overlap and must not be added. [Native execution receipt](native-suite-academic-evidence.json)

The earlier restricted attempt was interrupted after public-network and /proc limitations and has unreconciled worker evidence. It is retained separately and is not pooled into these admitted totals. Native passes establish the executed assertions, not automatically independent oracles or empirical calibration. No separate model-quality, calibrated-uncertainty or live-execution study has been run by this academic review. The established progress is stronger implementation/protocol integrity and an independently confirmed repair of the original causal-feature defect.

[quantile-output]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/features/quantile_price_lines.py#L98-L148
[quantile-causal]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/features/quantile_price_lines.py#L186-L241
[quantile-tests]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/tests/test_quantile_line_causality.py#L10-L55
[prepare]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/manifest_core.py#L1866-L1883
[split-transform]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/manifest_core.py#L1012-L1068
[dated]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_manifest_preparation.py#L21-L65
[split]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/manifest_core.py#L1899-L1910
[fold-prep]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_fold_preparation.py#L35-L127
[bar-support]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_prepare_trade_context.py#L105-L138
[chrono-link]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/sfd/reference_architecture/_chronological_link.py#L23-L59
[allocation-outcomes]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_allocation_folds.py#L203-L222
[calibration]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_validation_calibration.py#L59-L121
[optimizer]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_objective_optimizer.py#L40-L77
[validation]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_validation_decisions.py#L38-L102
[fold-witness]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_fold_fingerprint.py#L52-L133
[fold-read]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_fold_evidence.py#L170-L222
[composition]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_holdout_composition.py#L78-L118
[family]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_family_evidence.py#L204-L224
[freeze]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_holdout_freeze.py#L163-L239
[holdout-events]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_holdout_events.py#L29-L53
[holdout-policy]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_resolve_trade_policy.py#L151-L188
[holdout-attempt]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_holdout_assessment.py#L191-L235
[fields]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_result_fields.py#L14-L71
[round-errors]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_round_errors.py#L31-L100
[pbo-settings]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_acceptance_settings.py#L8-L25
[pbo-geometry]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_acceptance_settings.py#L105-L121
[confusion]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/log/_permutation_confusion_metrics.py#L137-L146
[averages]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_walk_forward_run.py#L109-L123
[convergence]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/convergence_report.py#L32-L89
[cost-api]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/observed_costs.py#L144-L197
[cost-statistics]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_cost_statistics.py#L13-L104
[cost-admission]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_cost_statistics.py#L107-L195
[cost-match]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_cost_comparison.py#L116-L142
[cost-compare]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_cost_comparison.py#L198-L242
[feature-link]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/sfd/reference_architecture/feature_link_binary.py#L50-L93
[weight-link]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/sfd/reference_architecture/weight_link_binary.py#L50-L93
[pseudo-pool]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/sfd/reference_architecture/_pseudo_pool.py#L24-L55
[pseudo-model]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/sfd/reference_architecture/pseudo_label_binary.py#L64-L124
[residual]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/sfd/reference_architecture/residual_regressor.py#L49-L90
[hmm]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/sfd/reference_architecture/gaussian_hmm_binary.py#L60-L86
[sequence]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/sfd/reference_architecture/_sequence_binary.py#L78-L133
[var]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/sfd/reference_architecture/entropy_var_regressor.py#L37-L97
[bayesian]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/cohort/bayesian.py#L19-L81
[allocation-admit]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_allocation_folds.py#L228-L245
[regime]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/features/classify_market_regime.py#L42-L118
[regime-ranks]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/features/_regime_ranks.py#L16-L29
[perturbation]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/targets/_perturbation.py#L21-L70
[importance]: https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/log/_experiment_parameter_importance.py#L72-L111
