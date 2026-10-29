# Limen reassessment — 29 October 2026

**Limen has made substantial progress in research integrity and safety. All five priority repair areas from the previous assessment now have independent before/after evidence. Repeated performance workloads retain their scientific outputs and broadly similar runtimes; they do not establish a new algorithmic speed advantage.**

This update reviews all 42 original criteria and reruns the previous Limen workloads, independent defect probes, and complete current native test suite. It adds an assessment at a new immutable revision. Original results are preserved; competitors are not re-ranked using measurements from a different machine.

## Scope and evidence

| Item | Frozen baseline | Current assessment |
|---|---|---|
| Limen source | [`29837e6`](https://github.com/Vaquum/Limen/tree/29837e666604eee74a2ac94f328fb9803724342a) | [`25e4786`](https://github.com/Vaquum/Limen/tree/25e47866422d007da55cb19625344183599ba671) |
| Source commit date | 19 October 2026 | 28 October 2026 |
| Package metadata | 5.40.1 | 5.46.2, including subsequent main commits |
| Performance comparison | Rerun on the current host | Rerun on the same host and dependency versions |
| Behavioral authority | Executable source, test assertions and executed results | Executable source, test assertions and executed results |

The previous measured assessment is ten days before this report. The full fourteen-day Git history was inspected, but measured conclusions use the frozen 19 October baseline. Main was checked again after execution and still pointed to the assessed SHA. Documentation, release notes and issue closure do not establish behavior. [Source identities and change inventory](environment/source-comparison.json).

Both revisions use the same recorded fixture, SHA256 `a634bbd4f3692fac7bc88512da588e7772f4bd1b749567606d5314e54d0adf72`. The assessment verifies those bytes; it does not independently authenticate exchange provenance. The [42-criterion grid](CRITERIA.md), [academic evidence](academic/academic_delta.json), [safety evidence](safety/safety-delta.json) and [performance evidence](performance/performance_update.json) retain scopes and implementation references.

## How much the work moves the needle

| Area | Assessment of movement | Strongest evidence | Remaining boundary |
|---|---|---|---|
| Computation performance | **Broadly retained. No demonstrated material speed breakthrough.** | Identical outputs; five fresh processes per revision and strategy; unchanged return kernel and snapshot-ledger implementation; preserved factorization outputs. | Small one-host samples, overlapping ranges and unmeasured scaling workloads do not establish a general speedup or equivalence. |
| Academic robustness | **Substantial improvement in the integrity of a research result.** | Historical quantile features stop changing when future rows are appended; fold-local preparation and validation identities are stronger; protected research and cost-sensitivity evidence are broader. | No independent predictive edge, calibrated uncertainty, complete external search history or broad final-holdout eligibility is established. |
| Safety properties | **Substantial improvement at concrete failure boundaries.** | Resolver namespace escape, altered manifest acceptance, invalid FFD recurrence and invalid compiled-Sensor outputs distinguish old and current code in independent probes. | Trusted Python, direct snapshot cost admission, index rebuilding, general resource bounds and persistence transactions remain scoped or incomplete. |

The coarse framework changes three status labels: **A01 Fails → Partial; S01 Fails → Enforced within its declared namespace boundary; S03 Fails → Partial.** Other criteria improve inside existing Partial or Enforced categories. Counting changed circles would understate practical progress; converting circles into precise scores would overstate the measurement. Remaining Partial labels retain their broad requirements.

## Five priority repairs: independent before and after

These symbols describe only the named, exercised boundary. **●** means that boundary passed the stated independent check; **○** means the baseline exhibited the defect. They are not whole-product safety or scientific-validity ratings.

| Tested boundary | Baseline | Current | Measured change |
|---|:---:|:---:|---|
| Historical quantile end-event features remain unchanged when later rows are added | ○ | ● | At quantile 0.7, 173 of the first 192 rows changed before and zero now; at 0.8, 138 changed before and zero now. |
| YAML callable resolution rejects external re-exports | ○ | ● | The baseline resolved and bound the actual external `os.system` object; current lookup/compilation reject it and validation fails. The callable was never executed. |
| Reading or reusing a committed manifest verifies its body identity | ○ | ● | Full URI, short URI and recommit accepted an altered body before; all three now reject it without changing object/index bytes or timestamps. |
| FFD rejects the exercised nonfinite/overflow parameters | ○ | ● | Four old cases reached the probe's memory cap and the identity shortcut accepted a NaN threshold; all five current cases emitted completed `ValueError` results. |
| Compiled Sensor rejects invalid numeric predictions/probabilities | ○ | ● | Six invalid-output canaries appeared successful before; current single and batch calls return unavailable `sensor-error` results with null numeric outputs and preserved time alignment. |

The quantile probe also checks a separate cross-version oracle: current historical values match the old implementation's prefix-final values at four quantiles, eight cutoffs and five columns: **160 scalar comparisons, zero mismatches**, `rtol=atol=1e-12`. Valid safety controls remain valid. [Causality results](academic/causal-prefix-comparison.json) · [Safety results](safety/probe-comparison.json).

Two qualifications matter. The deliberately retrospective `active_quantile_count` still changes with future rows and is included unless disabled; the whole feature API is not universally causal. The FFD probe's 0.35-second outer deadline includes interpreter shutdown: every child flushed its completed method outcome before termination and was reaped. Outer deadline labels are not method timings or evidence of a current FFD hang. This establishes admission/overflow behavior, not universal finite-workload bounds. [Quantile implementation](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/features/quantile_price_lines.py#L98-L148) · [FFD qualification](safety/safety-delta.md#ffd-harness-qualification).

## Qualitative assessment

### Research decisions are better tied to their evidence

Automatic fractional-difference preparation now refits inside chronological inner folds alongside learned scaling/compression, with original row identity checked. Formed bars validate raw constituents and use their latest availability. Validation evidence binds ordered inputs, labels, calibrated probabilities and selected decisions; repeated predictions and the selected objective are checked. These protect against valid-looking results built from the wrong rows, state or decision vector. [Fold preparation](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_fold_preparation.py#L35-L127) · [Validation identity](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_validation_decisions.py#L38-L102).

Calibration and threshold selection can still share validation observations, so the optimized validation score is not an independent estimate. Raw features are computed before inner-fold preparation, so their own causality remains part of the contract; outer raw-data splitting still precedes feature construction. [Calibration](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_validation_calibration.py#L59-L121) · [Threshold checks](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_objective_optimizer.py#L40-L77) · [Outer split and feature order](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/manifest_core.py#L1012-L1068).

### Protected research covers more of the workflow

Source identities, folds, factorized reuse, workers, coordinator authority and resumed checkpoints are checked together. Typed parameter restoration and result-field collision checks improve identity and recovery. Bounded record-on-error exists for ordinary unprotected serial research; integrity failures remain fatal. [Protected composition](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_holdout_composition.py#L78-L118) · [Result admission](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_result_fields.py#L14-L71) · [Error policy](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_round_errors.py#L31-L100).

Final holdout remains narrower than protected research. It admits exact supported native LogRegBinary/LightGBMBinary implementations and ordinary dated inference. Formed bars, walk-forward, alternate test sources, extensions and nonunit decoder lookback are rejected. A contract-bearing single Sensor has further policy restrictions; contract-bearing Cohorts, funding, external execution sources and dynamic barriers remain outside that final path. [Final admission](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_holdout_freeze.py#L163-L239) · [Execution restrictions](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/experiment/_resolve_trade_policy.py#L151-L188).

### Observed execution costs are a meaningful new control

The new layer admits normalized fill histories, checks chronology/support, freezes typed identities, binds candidate inputs/policies and distinguishes unavailable evidence from economic failure. It compares a frozen candidate's original policy with an observed-slippage scenario while retaining fees. This makes a specific cost-sensitivity question reproducible and harder to answer using incompatible evidence. [History admission](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_cost_history.py#L127-L184) · [Replay](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_cost_comparison.py#L198-L242).

Histories may still be concentrated or incomplete, and these checks do not independently authenticate original source/delivery. Retrospective slippage does not establish future costs, queue position, partial fills or live execution fidelity. External validity remains Unknown. [Support and implementation limitations](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/backtest/_cost_statistics.py#L107-L195).

### The research surface is broader; predictive improvement is unproven

Public reference-architecture exports add nine model classes: CNN1D, LSTM, Gaussian HMM, RBF SVM, feature-linked and weight-linked binary models, pseudo-label binary, residual regression and entropy/VaR regression. New cohort/allocation and perturbation mechanisms also exist. The detailed review checks actual training and prediction boundaries. No independent experiment here establishes improved out-of-sample trading results. [Executable exports](https://github.com/Vaquum/Limen/blob/25e47866422d007da55cb19625344183599ba671/limen/sfd/reference_architecture/__init__.py) · [Source-linked model review](academic/qualitative-review.md#new-models-and-robustness-mechanisms).

## Performance: same-host repetitions

### 1. Matched external snapshot replay

The unchanged common contract evaluates 8,783 rows plus one real settlement row, long/flat positions, zero costs and next-close execution. Signals are prepared before timing. Full-common time includes native validation, return execution, native bar metrics, extraction and common summary; imports, the independent oracle and parity checks are outside it.

Five fresh measured processes per revision/strategy each make one first call and nine warm calls. Versions and strategy order alternate. Warm time is the median of five process medians; the range is their observed minimum–maximum, not a confidence interval.

| Strategy | Baseline warm median | Current warm median | Observed duration change | Baseline process range | Current process range |
|---|---:|---:|---:|---:|---:|
| Buy and hold | 2.511 ms | 2.274 ms | −9.45% | 2.285–2.625 ms | 2.128–2.823 ms |
| SMA crossover | 2.135 ms | 2.046 ms | −4.16% | 1.976–2.500 ms | 1.867–2.681 ms |

All common output digests agree; the oracle checks 8,783 equity samples and 2/52 fills. Return-kernel and snapshot-ledger code are unchanged. Lower medians with overlapping ranges and small one-host samples do not establish durable or algorithmic speedup. Native cash, units and fill quantities/fees are not independently observed on this return/exposure route. No competitor was rerun. [Raw campaign](performance/paired-campaign/paired_report.json) · [All measurement layers and limits](performance/PERFORMANCE_RESULTS.md).

### 2. Original native workloads

The unchanged native snapshot harness has a different signal-time convention and is kept separate. Each cell contains seven warm repeats within one process per revision/strategy.

| Native snapshot strategy | Baseline full snapshot median | Current full snapshot median |
|---|---:|---:|
| Buy and hold | 1.638 ms | 1.562 ms |
| SMA crossover | 1.283 ms | 1.407 ms |

The original fitted-preparation campaign evaluates 48 rounds per arm and fits 24 LightGBM models. Reuse reduces target/scaler fits from 24 to one in **both** revisions: preserved behavior, not a new interval gain. All four scientific-output digests agree at the harness's 12-decimal normalization.

| Fitted-preparation arm | Baseline process duration | Current process duration | Target fits | Scaler fits | Model fits |
|---|---:|---:|---:|---:|---:|
| Fresh preparation | 13.159 s | 14.680 s | 24 | 24 | 24 |
| Reused preparation | 13.061 s | 13.110 s | 1 | 1 | 24 |

There is one fixed-order fresh/reuse pair per revision. The reused path is nearly unchanged here; the fresh path is slower. Neither establishes general throughput movement. Indicator scaling, event-label throughput, search throughput, parallel speedups, cache overhead and restart latency remain unmeasured. [Native command/results manifest](performance/native-campaign/native_report.json) · [Derived measurements](performance/measurements.json).

## Tests, coverage and CI

The complete current native suite ran against the exact assessed source on native Linux:

| Check | Result |
|---|---|
| Collected and executed cases | 7,391 |
| Passed / failed / skipped | **7,388 / 0 / 3** |
| Skips | One CUDA XGBoost case; two opt-in TabPFN model cases |
| Worker evidence | Four receipts reconciled |
| Statement coverage | **31,136 / 32,875 = 94.7103%** |
| Coverage gaps | 1,739 missed statements; 507 excluded; no branch coverage |

The research environment follows current CI pins/hashes with an explicitly recorded CPU-only PyTorch replacement. GPU/opt-in TabPFN execution is not established. Test passes prove the executed assertions, not every scientific claim. The old 1,771-test curated campaign and current full suite have different scopes; their ratio is not suite growth. [Native evidence](native-suite/run_manifest.json) · [CPU selection](environment/research-cpu-selection.json).

The initial restricted attempt was interrupted after public-network and `/proc` limitations; its worker evidence is incomplete and is not admitted. Failed and successful attempts are preserved separately. Some native tests fetch floating public recorded data, limiting exact repetition; the independent probes and timings use the pinned fixture.

Exact-SHA upstream CI also reports **7,388 passed, three skipped**, and passing coverage. Its runtime job **fails: 293.049 seconds versus 280**, 13.049 seconds over budget. The local 160.391-second suite profile is a different-host observation, not code-speedup evidence or a repaired upstream gate. [Upstream run](https://github.com/Vaquum/Limen/actions/runs/40757971723) · [Retrieved CI receipt](environment/upstream-ci.json).

## Remaining narrow interventions

These are recommendations, not new source changes or tickets.

1. **Apply the existing finite, nonnegative cost rule at the direct snapshot entry point.** Its fee/slippage route lacks equivalent manifest/event admission. Add only the guard and direct regression cases.
2. **Reuse canonical body verification when rebuilding the manifest index.** Reads/reuse reject alteration, but rebuilding still checks filename/lineage without recomputing body identity before copying metadata.
3. **Profile the hosted CI runtime overrun.** Reduce demonstrated unnecessary work before changing the budget. Local suite success does not resolve that failure.
4. **Use existing pinned recorded fixtures for native core tests.** Keep live-download checks explicit; do not fabricate market data.

The first two remaining gaps are current source-inspected findings; this update does not claim to have freshly exploited them. Trusted Python, finite-workload bounds, partial transaction durability and narrow final-holdout eligibility remain explicit in the [safety records](safety/safety-delta.json).

## Reproduce and inspect

Start with [REPRODUCE.md](REPRODUCE.md) and the [42-criterion grid](CRITERIA.md). Scripts, environment selections, exact command manifests, preregistrations, raw outputs, failed-attempt receipts and publication hashes accompany this report. Original benchmark code, catalog, historical results and Limen source are preserved.

From the benchmark repository root, `python updates/2026-10-29-limen/verify_evidence.py` checks the published file hashes and all 230 archived binary members without importing Limen or rerunning a model. The binary archive restores the original relative paths; extraction and per-member verification are documented in the reproduction guide.

Current Limen makes several previously misleading or unsafe outcomes harder to produce and easier to reject. That materially improves the credibility of a completed experiment. This evidence supports that conclusion more strongly than a new speed advantage, broad deployment assurance or better trading returns.
