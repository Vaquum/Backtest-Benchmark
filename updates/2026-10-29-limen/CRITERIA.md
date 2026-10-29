# All 42 criteria — baseline and current Limen

Baseline `29837e6` → current `25e4786`. Symbols summarize the original scoped status, not a numerical rating. **●** Enforced in the declared native boundary; **◐** Partial; **○** a demonstrated failure; **—** Unknown. Unknown is never treated as absence. Optional controls are explicitly labelled. An unchanged broad status can contain substantial repaired behavior.

Performance is reported as measurements in [PERFORMANCE_RESULTS.md](performance/PERFORMANCE_RESULTS.md). Its status words below describe the coverage of an assessment, not engine speed. The canonical JSON rows retain code references, test membership, scope and limitations. Whole-module test membership is execution evidence, not assertion-level proof.

## Computation

[Canonical records and implementation evidence](performance/performance_update.json).

| ID | Criterion | Baseline | Current | What changed / remaining scope |
|---|---|:---:|:---:|---|
| P01 | Parameter-space construction | Partial | Partial | Canonical choice validation added; construction scaling unmeasured. |
| P02 | Candidate consumption | Partial | Partial | Candidate identity strengthened; no new consumption-throughput measurement. |
| P03 | First valid output | Partial | Partial | First call and launch-to-admitted-output measured separately. |
| P04 | Complete research-campaign throughput | Unknown | Unknown | One native 48-round pair per revision; general throughput unestablished. |
| P05 | Preparation and signal reuse | Optional | Optional | Both revisions reduce target/scaler fits 24→1; scientific digests agree. |
| P06 | Indicator and feature computation | Partial | Partial | Feature implementation reviewed; scaling not timed. |
| P07 | Matched snapshot replay | Partial | Partial | Five processes per revision/strategy; identical outputs, overlapping ranges. |
| P08 | Event ledger and forward-label work | Partial | Partial | Event/label code reviewed; no new throughput experiment. |
| P09 | Memory and resource footprint | Partial | Partial | Process peak RSS measured; allocation-only and scaling costs unmeasured. |
| P10 | Parallel campaign execution | Optional | Optional | Parallel implementation reviewed; no parallel-speedup experiment. |
| P11 | Cache key, hit and eviction costs | Partial | Partial | Cache identities/reuse reviewed; key/hit/eviction overhead unmeasured. |
| P12 | Recording and recovery costs | Partial | Partial | Recovery integrity strengthened; recording/restart cost unmeasured. |

## Academic robustness

[Canonical records and implementation evidence](academic/academic_delta.json).

| ID | Criterion | Baseline | Current | What changed / remaining scope |
|---|---|:---:|:---:|---|
| A01 | Causal predictor invariance | ○ | ◐ | Quantile historical leakage repaired; retrospective output still exists. |
| A02 | Training and evaluation isolation | ◐ | ◐ | Split/preparation admission strengthened; custom feature causality remains a contract. |
| A03 | Label availability and censoring | ◐ | ◐ | Formed/linkage availability strengthened; arbitrary horizons not inferred. |
| A04 | Temporal split geometry | ◐ | ◐ | Chronological contracts remain scoped; no universal purge/embargo inference. |
| A05 | Fold-local preprocessing and stacking | ● | ● | Fold-local automatic FFD now joins scaler/PCA refitting and row checks. |
| A06 | Calibration and threshold selection | ◐ | ◐ | Calibration/decision receipts strengthened; shared validation selection remains. |
| A07 | Metric definitions and aggregation | ◐ | ◐ | Binary confusion admission improved; fold averages remain unpooled. |
| A08 | Numerical and mathematical verification | ◐ | ◐ | Independent prefix oracle and native assertions added; no universal proof. |
| A09 | Convergence and fit stability | ◐ | ◐ | More model implementations; no common convergence-quality gate. |
| A10 | Search-family history completeness | ◐ | ◐ | Typed identity and local failure recording; outside search history unknown. |
| A11 | Multiple-selection and dependence control | ◐ | ◐ | PBO accepts supported even block counts; retained-family diagnostic only. |
| A12 | Cross-run evaluation comparability | ◐ | ◐ | Fold/source evidence strengthened; complete economic comparability remains scoped. |
| A13 | Final holdout protocol and compatibility | ◐ | ◐ | Protected research broader; final admission remains deliberately narrow. |
| A14 | Baseline quality and external validity | — | — | No independent external predictive/live-execution validity study. |
| A15 | Sensitivity, ablation and reproducibility | ◐ | ◐ | Observed-cost scenarios and repeatable perturbation/surrogate diagnostics added. |

## Safety

[Canonical records and implementation evidence](safety/safety-delta.json).

| ID | Criterion | Baseline | Current | What changed / remaining scope |
|---|---|:---:|:---:|---|
| S01 | Untrusted configuration callable boundary | ○ | ● | External callable re-export blocked; installed Python is still trusted. |
| S02 | Input schema and numeric admission consistency | ◐ | ◐ | More numeric/parser checks; direct snapshot cost admission gap remains. |
| S03 | Algorithm and process resource bounds | ○ | ◐ | Five FFD invalid/overflow cases reject; general resource limits unestablished. |
| S04 | Data source network, archive and path boundaries | ◐ | ◐ | Optional recorded-Parquet SHA check added; broader ingestion limits remain. |
| S05 | Manifest content-address verification on read | ◐ | ◐ | Body-verified read/reuse repaired; index rebuilding remains narrower. |
| S06 | Recorded round corruption and reference integrity | ● | ● | Recorded-round integrity retained and extended to exits/checkpoints. |
| S07 | Crash/restart consistency and durable commit frontier | ◐ | ◐ | Typed/protected resume strengthened; no whole-output transaction/fsync. |
| S08 | Parallel worker failure handling and bounded dispatch | ● | ● | Bounded dispatch/failure propagation retained; protected worker authority added. |
| S09 | Inference output validity and unavailable-signal behavior | ◐ | ◐ | Six invalid Sensor canaries become unavailable; full signal semantics remain scoped. |
| S10 | Execution chronology and source evidence admission | ● | ● | Chronology/source admission extended to declared dynamic barriers. |
| S11 | Economic affordability, exposure and quantity constraints | ● | ● | Supported event affordability/exposure constraints retained. |
| S12 | Exit rules, gap treatment and execution uncertainty | ◐ | ◐ | Observed-cost and exit controls added; live fill fidelity unestablished. |
| S13 | Protected holdout reservation and exposure accounting | ● | ● | Protected composition/resume broader; final holdout still restricted. |
| S14 | Executable supply-chain and security CI coverage | ◐ | ◐ | CI evidence/supply-chain controls strengthened; runtime gate currently fails. |
| S15 | Adversarial validation evidence and mutation coverage | ◐ | ◐ | Independent repaired-boundary probes and full native assertions executed. |

## Status changes

A01: Fails → Partial; S01: Fails → Enforced; S03: Fails → Partial. No numerical index is calculated.

Generated from the three canonical criterion records by `python render_criteria.py`. The brief notes are editorial summaries; consult the linked records for exact evidence and boundaries.
