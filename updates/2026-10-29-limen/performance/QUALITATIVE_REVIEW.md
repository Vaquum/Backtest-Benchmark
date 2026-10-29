# Limen performance: source delta before timing

Baseline `29837e666604eee74a2ac94f328fb9803724342a`; latest `25e47866422d007da55cb19625344183599ba671`. This assessment was completed before the old/new timed campaign. All twelve coarse criterion status labels are retained; updated scopes and code changes are stated below. A status is not a numeric performance score. Code-inferred work changes are separated from forthcoming measurements.

The matched replay can reuse the complete frozen runner and adapter: the long-flat kernel and snapshot-ledger module are byte-identical. The most meaningful code changes are broader, explicitly admitted factorization and parallel support; added source/holdout/parameter validation; causal quantile feature computation; and less repeated state/plan work when generating trade-outcome labels. None alone establishes a speedup.

## P01 — Parameter-space construction (Partial)

ParamSpace now validates every supplied choice through the shared canonical execution identity and rejects collisions. Requested candidates are still materialized; Grid construction is byte-identical.

Choice admission adds work proportional to the supplied choices and their serialized size. Legacy candidate columns still retain O(k*d) values; Grid initially retains dimensions without expanding the Cartesian product.

**Limit:** No parameter construction latency or memory scaling rerun is prescribed. Added identity validation is meaningful work, not a demonstrated regression.

Code: [limen/utils/param_space.py:74–109](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/utils/param_space.py#L74-L109); [limen/_parameter_identity.py:11–33](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/_parameter_identity.py#L11-L33); [limen/experiment/param_search/grid_strategy.py:36–72](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/param_search/grid_strategy.py#L36-L72).

## P02 — Candidate consumption (Partial)

Grid, Random and Sobol implementations are byte-identical. SearchStrategy delegates to the same canonical execution hash. Legacy generate still filters the remaining frame after each draw.

Consuming a legacy k-row frame still repeatedly scans shrinking frames, approximately quadratic total row-position work. MSQ accepted-hash retention and bounded Random/Sobol retries remain.

**Limit:** No enumeration throughput or search-distribution measurement. Domain identity admission should not be represented as a faster enumerator.

Code: [limen/utils/param_space.py:120–146](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/utils/param_space.py#L120-L146); [limen/experiment/param_search/search_strategy.py:116–175](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/param_search/search_strategy.py#L116-L175); [limen/experiment/param_search/random_strategy.py:51–61](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/param_search/random_strategy.py#L51-L61); [limen/experiment/param_search/sobol_strategy.py:51–67](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/param_search/sobol_strategy.py#L51-L67).

## P03 — First valid output (Partial)

The frozen zero-cost snapshot adapter remains signature-compatible. New optional class mapping and explicit-exit support do not activate in this replay.

Old and latest must be measured on the same host with identical dependencies. Process-launch-to-first-valid includes source verification, imports, data, oracle and validation; first API call is a different boundary.

**Limit:** No October19-to-October29 timing ratio. The separate kernel diagnostic first call follows all full-wrapper calls and is not process-cold.

Code: [limen/backtest/_snapshot_execution.py:145–168](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_snapshot_execution.py#L145-L168); [limen/backtest/backtest_snapshot.py:112–128](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/backtest_snapshot.py#L112-L128).

## P04 — Complete research-campaign throughput (Unknown)

Round validation, holdout composition, error handling, and additional recorded evidence have expanded. Per-round result CSV appends and buffered logging remain in the serial/MSQ execution paths.

Richer evidence and admission can change end-to-end cost. The unchanged native 48-round factorized harness can measure its exact workload; it cannot establish general research throughput.

**Limit:** One fresh-versus-reuse pair per revision is a mechanism check, not a repeated latency experiment. No model equivalence or broad scaling claim follows from snapshot replay.

Code: [limen/experiment/experiment_core.py:185–248](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/experiment_core.py#L185-L248); [limen/experiment/experiment_core.py:680–755](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/experiment_core.py#L680-L755); [limen/experiment/experiment_core.py:970–983](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/experiment_core.py#L970-L983).

## P05 — Preparation and signal reuse (Optional)

New explicit stage reuse contracts, native declarations and domain projections broaden admissible signal reuse. Fitted-preparation reuse still has narrower RobustScaler/NextReturn/QuantileBinary/window-return/lag-range admission. Cache hits now compose holdout proofs and replay warnings.

Domain projections can avoid unnecessary Cartesian validation, but custom full-parameter dependencies can still enlarge admission work. Supported factorized paths retain fitted artifacts and signals to avoid repeated fits; bounded entry counts are not byte budgets.

**Limit:** Folds, allocation, objectives, event execution and explicit exits remain outside factorization admission. Only the unchanged recorded-data harness is scheduled to quantify reuse; verify 48 rows, 24 model fits per arm, target/scaler 24 versus 1, and equal 12-decimal outputs within each revision.

Code: [limen/experiment/_factorized_contract.py:11–53](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_factorized_contract.py#L11-L53); [limen/experiment/_factorized_admission.py:72–175](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_factorized_admission.py#L72-L175); [limen/experiment/_factorized_native.py:64–100](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_factorized_native.py#L64-L100); [limen/experiment/_factorized_projection.py:28–78](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_factorized_projection.py#L28-L78); [limen/experiment/_factorized_prep.py:24–65](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_factorized_prep.py#L24-L65); [limen/experiment/_factorize.py:127–214](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_factorize.py#L127-L214).

## P06 — Indicator and feature computation (Partial)

EMA and shared line-array computation are byte-identical. SMA/CCI gain argument validation; stochastic wrapping now supports lazy expressions. Positive-quantile end-event columns use expanding completed-line thresholds. FFD gains finite-input/recurrence checks.

The causal quantile path maintains heaps per direction and scans recent completed events per row. This fixes the information set and changes the work; timing it against the old whole-frame threshold is not equal-semantics optimization. Quantile zero retains the vectorized window-sum path.

**Limit:** No adapted indicator timing is scheduled: the existing hardcoded-data benchmark is not independently matched here. The research-only active-span column still uses whole-frame selection. FFD has no new arbitrary maximum-weight or runtime quota.

Code: [limen/indicators/sma.py:53–63](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/indicators/sma.py#L53-L63); [limen/indicators/cci.py:59–70](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/indicators/cci.py#L59-L70); [limen/indicators/stoch.py:167–207](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/indicators/stoch.py#L167-L207); [limen/features/quantile_price_lines.py:108–148](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/features/quantile_price_lines.py#L108-L148); [limen/features/quantile_price_lines.py:186–241](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/features/quantile_price_lines.py#L186-L241); [limen/features/fractional_diff.py:31–49](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/features/fractional_diff.py#L31-L49); [limen/features/fractional_diff.py:83–115](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/features/fractional_diff.py#L83-L115).

## P07 — Matched snapshot replay (Partial)

The long-flat return kernel and snapshot-ledger module are byte-identical. The wrapper adds optional explicit-exit behavior; the common adapter uses the unchanged default route.

The frozen external contract, oracle, adapter and extraction can be reused byte-for-byte with two explicit source-catalog overlays. Precomputed targets, complete equity/held/fill parity, and post-call thread gates remain mandatory.

**Limit:** Common results do not expose independent native cash/units/fee-ledger fields for Limen; fills are reconstructed from native position segments. Costed common replay remains unsupported by this adapter, and event execution is a separate contract.

Code: [limen/backtest/long_flat_strategy.py:42–133](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/long_flat_strategy.py#L42-L133); [limen/backtest/_snapshot_ledger.py:40–73](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_snapshot_ledger.py#L40-L73); [limen/backtest/_snapshot_execution.py:38–168](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_snapshot_execution.py#L38-L168).

## P08 — Event ledger and forward-label work (Partial)

Event-plan construction can bypass the global key/cache for single-use candidates. TradeOutcomeTarget caches the accrual-presence decision, shares a full plan for no-accrual cases, reuses the immediate long/short candidate plan for accrual cases, disables state retention, and reads episodes directly.

This removes repeated cache-key/ledger/state work from inspected target paths. The event cache remains limited by plan count and source-event count; these limits do not bound emitted timer states.

**Limit:** No event-label throughput or scaling timing is scheduled. Long horizons can still revisit long suffixes. The improvement is code-inferred work avoidance, not a measured speedup.

Code: [limen/backtest/_event_plan.py:27–84](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_event_plan.py#L27-L84); [limen/targets/trade_outcome.py:32–109](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/targets/trade_outcome.py#L32-L109); [limen/backtest/_event_clock.py:10–33](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_event_clock.py#L10-L33).

## P09 — Memory and resource footprint (Partial)

Parallel workers now load a parent-written, hashed, read-only file snapshot of each source frame. Each worker reads bytes and deserializes its own DataFrame. Computation-cache accounting is byte-identical; factorized caches remain entry bounded.

Source admission is stronger and the parent serializes once, but this is not memory mapping or shared DataFrame storage. Per-worker data/model copies and temporary serialization remain possible.

**Limit:** Paired snapshot and native harness RSS is process-lifetime high-water, not incremental allocation, PSS, process-tree memory or a hard bound. No memory-scaling campaign is scheduled.

Code: [limen/experiment/_parallel_sources.py:14–50](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_parallel_sources.py#L14-L50); [limen/experiment/_parallel_worker.py:184–205](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_parallel_worker.py#L184-L205); [limen/utils/_computation_cache.py:23–64](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/utils/_computation_cache.py#L23-L64); [limen/experiment/_factorize.py:127–214](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_factorize.py#L127-L214).

## P10 — Parallel campaign execution (Optional)

Worker admission no longer uses only the old exact MLManifest/logreg/LightGBM whitelist; it reconstructs compiled shapes and checks resolved CPU/native-thread settings. Source snapshots, holdout authority and fold-promotion context enter initialization.

More admitted compiled workloads can execute in workers. Pending work remains bounded, and commits still await pending[0] with checkpoint/feedback barriers, so head-of-line blocking remains.

**Limit:** No parallel timing is newly introduced: the old parallel harness was inspected rather than measured in the original baseline. Native suite results can test correctness but do not establish scaling speedups.

Code: [limen/experiment/_parallel_worker.py:105–151](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_parallel_worker.py#L105-L151); [limen/experiment/_parallel_worker.py:184–258](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_parallel_worker.py#L184-L258); [limen/experiment/_parallel_rounds.py:172–244](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_parallel_rounds.py#L172-L244).

## P11 — Cache key, hit and eviction costs (Partial)

The computation-cache implementation is byte-identical. Prepared/signal cache paths now validate protected source/population/history evidence and refresh recency; unprotected operation has a cheaper binding path. Single-use event plans may opt out of key/cache work.

Computation hits still require source scans/byte-key construction and cloned/copied outputs. Added evidence checks are real cache-hit work; reuse does not imply a zero-cost hit.

**Limit:** No isolated hit/miss/eviction benchmark is scheduled. The factorized harness measures one admitted workload only, and entry bounds do not establish worst-case memory.

Code: [limen/utils/_computation_cache.py:86–122](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/utils/_computation_cache.py#L86-L122); [limen/experiment/_holdout_composition.py:90–132](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_holdout_composition.py#L90-L132); [limen/experiment/_holdout_composition.py:162–226](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_holdout_composition.py#L162-L226); [limen/backtest/_event_plan.py:45–76](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_event_plan.py#L45-L76).

## P12 — Recording and recovery costs (Partial)

Round-storage serialization/compression/dedup code is unchanged apart from an internal frames rename. Recovery now checks applicable evidence, typed parameters and richer holdout/exit/fold outputs. Checkpoints accept a committed state snapshot without rewinding the live sampler.

Recovery correctness work has expanded. Full-prefix validation and serial CSV truncation/rewrite remain; dedup still serializes and hashes before determining that a frame blob is already present.

**Limit:** No interrupted-campaign latency or output-size scaling measurement is scheduled. Stronger recovery validation should not be mistaken for a demonstrated runtime bound.

Code: [limen/experiment/_round_storage.py:133–178](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_round_storage.py#L133-L178); [limen/experiment/_recording.py:54–105](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_recording.py#L54-L105); [limen/experiment/_parallel_resume.py:144–269](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_parallel_resume.py#L144-L269); [limen/experiment/checkpoint_manager.py:95–153](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/checkpoint_manager.py#L95-L153); [limen/experiment/experiment_core.py:878–959](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/experiment_core.py#L878-L959).

## Rerun boundaries

The common replay uses 8,783 evaluation rows from the unchanged recorded 2024 hourly fixture, two strategies, five fresh measurement processes per revision and strategy, one first call plus nine warm calls per process, and alternating old/new order. All native-thread environment controls and observed pool admission remain intact. Raw process medians, ranges, first calls, and kernel diagnostics are retained; only same-machine old/new durations may be compared.

The two original native harnesses are unchanged across both sources. The snapshot harness runs Limen only, buy-and-hold and SMA, seven repeats. The fitted-preparation harness is one 48-round pair per revision with its existing parity/count assertions. The native suite, which is run separately, supplies correctness checks for cache, preparation, parallel and recovery behavior. Indicator or parallel benchmarks that were not independently measured in the original baseline are not converted into new claims.
