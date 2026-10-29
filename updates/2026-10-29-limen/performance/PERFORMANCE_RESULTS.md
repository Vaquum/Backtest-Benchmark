# Limen computation rerun — 29 October 2026

The latest revision passes the same replay contract as the original baseline, with unchanged observed equity, held-position and fill outputs. Its aggregate warm medians are lower in this run, but the process ranges overlap. The return kernel and snapshot-ledger module are byte-identical, so these measurements do not establish an algorithmic speedup.

**Revisions:** baseline `29837e666604eee74a2ac94f328fb9803724342a`; latest `25e47866422d007da55cb19625344183599ba671`. The complete [source delta](QUALITATIVE_REVIEW.md) and [P01–P12 update](performance_update.json) separate code changes from timing evidence. The frozen historical catalog, original benchmark Python and old evidence were not edited.

## Shared replay: the main old/new comparison

The recorded hourly fixture has 8,784 source rows; 8,783 rows are evaluated and one real row supplies delayed settlement. Signals are computed before engine timing. Decisions available after close t can fill at close t+1; entries use all affordable units, positions remain long or flat, costs are zero, and liquidation occurs at the penultimate real close. The same independent cash/quantity oracle checks every equity sample, held state and fill bar/side/price.

Five fresh measurement processes per revision and strategy each make one first full-wrapper call and nine warm calls. Revisions alternate within paired blocks, and strategy order alternates. The reported warm median is the median of five within-process warm medians. The range is the observed minimum and maximum of those five process medians; it is not a confidence interval.

| Strategy | Baseline warm median (ms) | Baseline process range (ms) | Latest warm median (ms) | Latest process range (ms) | Latest / baseline duration |
|---|---:|---:|---:|---:|---:|
| Buy and hold | 2.511363 | 2.285354–2.625195 | 2.273964 | 2.128224–2.822942 | 0.905470 |
| SMA crossover | 2.135285 | 1.975507–2.500479 | 2.046498 | 1.866960–2.681001 | 0.958419 |

The two ratios divide the aggregate medians; they are not medians of paired ratios. They correspond to 9.45% and 4.16% lower observed duration. Five process units on one host and overlapping ranges do not support a durable improvement claim. Every sample, including a 6.034497 ms latest buy-and-hold first call, is retained. No competitor was rerun, and no ratio uses the October 19 host timings.

Full-common time includes native snapshot validation, return execution, native bar metrics, extraction of common outputs and the common summary. It excludes source verification, imports, prepared-input loading, the independent oracle, parity checks and explicit between-call collection. Garbage collection triggered inside a timed call remains included. These boundaries match the frozen external benchmark.

### Startup and memory are separate observations

| Revision | Strategy | First full-common call, median (ms) | Launch to first admitted result, median (ms) | Process peak RSS, median (MiB) |
|---|---|---:|---:|---:|
| baseline | buy_and_hold | 2.869959 | 664.748453 | 135.449 |
| baseline | sma_cross | 2.491598 | 785.783638 | 137.352 |
| latest | buy_and_hold | 2.609340 | 734.606985 | 136.730 |
| latest | sma_cross | 2.479566 | 740.955536 | 135.871 |

The launch boundary includes the benchmark's source-install verification, imports, data loading, independent oracle and successful validation. It is not engine import time alone. RSS is the process-lifetime high-water after full calls, including imported libraries and earlier work; it is not incremental engine allocation or process-tree memory.

### Internal kernel diagnostic

| Strategy | Baseline warm kernel median (ms) | Latest warm kernel median (ms) |
|---|---:|---:|
| Buy and hold | 0.559239 | 0.550226 |
| SMA crossover | 0.622213 | 0.549872 |

This diagnostic calls the internal return kernel and follows all full-wrapper calls in each process. Its first call is therefore not process-cold. Kernel, native execution, extraction and full-common timing must remain separate. Independently aggregated component medians need not add to the full-common median.

## Original native snapshot harness

The original harness and all of its snapshot helpers are byte-identical across the two revisions. Each revision runs buy-and-hold and SMA in a fresh process per strategy, with one first call and seven warm repeats. Its original contract uses a signal at close t for the close-t-to-close-t+1 interval, which differs from the delayed decision contract above. Its rows must not be pooled with the shared replay.

| Revision | Strategy | Warm kernel median (ms) | Kernel + common-output median (ms) | Full native snapshot median (ms) |
|---|---|---:|---:|---:|
| baseline | buy_and_hold | 0.305207 | 0.519458 | 1.637653 |
| baseline | sma_cross | 0.278948 | 0.448552 | 1.282932 |
| latest | buy_and_hold | 0.365386 | 0.616480 | 1.562063 |
| latest | sma_cross | 0.287449 | 0.495420 | 1.407412 |

All four native snapshot workers passed the original oracle parity checks. Prepared-array payloads and result-array payloads are identical between revisions for each strategy. The full native snapshot is timed after the kernel/common-output calls; these are seven repeats within one process per revision/strategy, not seven independent processes. Small differences change direction across layers and strategies, which further limits attribution.

## Original fitted-preparation harness

The unchanged recorded-data workload has 24 learning-rate choices and two fee settings: 48 terminal rounds per arm. Each arm trains 24 LightGBM models; prediction reuse across the fee axis remains active. The fresh arm clears only fitted-preparation cache state before each round.

| Revision | Arm | Complete process time (s) | Campaign region (s) | Target fits | Scaler fits | Model fits |
|---|---|---:|---:|---:|---:|---:|
| baseline | Fresh fitted preparation | 13.158962 | 8.259699 | 24 | 24 | 24 |
| baseline | Reuse fitted preparation | 13.060715 | 7.812996 | 1 | 1 | 24 |
| latest | Fresh fitted preparation | 14.679945 | 9.152950 | 24 | 24 | 24 |
| latest | Reuse fitted preparation | 13.110479 | 8.126040 | 1 | 1 | 24 |

Both revisions reduce target/scaler fits from 24 to one while preserving 24 model fits and 48 results. The benchmark scientific-output digest, normalized to 12 decimal places, is identical across all four arms. The strongest result is preserved scientific output and reduced fitted work. There is only one fixed-order fresh/reuse timing pair per revision; process startup, training, data preparation, recording and scheduling contribute to total duration. The observed fresh/reuse ratios, 1.007522 for baseline and 1.119711 for latest, are descriptive workload observations, not a general throughput claim.

## Admission, environment and coverage

The measured native Linux host reports **AMD EPYC 9V74 80-Core Processor**, nine visible logical CPUs, affinity 0–8, an eight-CPU cgroup quota and an 8 GiB memory limit. Both environments use Python 3.12.14 and identical archived core dependencies plus hash-checked LightGBM 4.6.0. Only Limen differs. Installed LightGBM Python/native/metadata fingerprints match between the two environments.

All nine native-thread environment controls remain one. The common campaign records 40 worker-runtime observations (20 preflight and 20 measured processes) and 400 successful post-call thread/parity admissions (200 full-common and 200 internal-core calls). Loaded OpenBLAS and Polars pools are observed at one. This is a configured/observed native-pool claim, not a claim that each process has exactly one operating-system thread.

The external replay imports verified noneditable source wheels and retains code/installed-file/source-SHA admission. The original native harnesses execute from their separately pinned source checkouts with the matching environment interpreter. Tracked source was clean at admission and post-run checks; the latest checkout contained untracked test-generated temporary directories from the preceding native suite, which are outside the source and harness code paths. No benchmark code, scientific expectation or source file was patched to pass.

For each strategy, all common-call output digests agree across both revisions. The common replay checks 8,783 equity rows and 2 buy-and-hold or 52 SMA fills. Limen's fills are reconstructed from native held segments; native cash, units, fill quantities and fees are not independently observed. Zero-cost snapshot evidence does not establish event-ledger, costed cash-spot or liquidity-model equivalence.

The qualitative P01–P12 review covers parameter-space construction/consumption, pipeline throughput, reuse, indicators, snapshot/event execution, memory, parallelism, cache costs and recovery. New measurements cover only the prescribed shared replay and original native workloads. Indicator scaling, event-label throughput, parameter-search throughput, parallel speedups, cache-boundary microbenchmarks and restart latency remain unmeasured. The full native suite is independent correctness evidence; it is not substituted for those missing performance experiments.

## Evidence and rerun entry points

- [Measured results and verification counts](measurements.json).
- [Paired raw aggregate and command manifest](paired-campaign/paired_report.json); every command retains its raw worker reports and logs.
- [Native command manifest](native-campaign/native_report.json); original report files retain all samples, fit counters, digests and native pools.
- [Paired preregistration](paired-preregistration.json), [native preregistration](native-preregistration.json), and [independent driver review](driver-review-note.json).
- [Before-timing code review](qualitative_delta.json) and [criterion update with measured scope](performance_update.json).
- [Paired outer driver](run_paired_replay.py) and [native outer driver](run_native_replay.py). The sixteen external benchmark Python files in both overlays are byte-identical to the frozen benchmark repository.

The shared replay refuses changed plan-bound code, catalog/manifests, source and fixture identity. The native driver pins source and harness/fixture hashes. Both refuse an existing output directory. The plans retain the observed absolute source/environment paths. Repeating on another host requires an explicitly recorded new setup and plan with the same pinned source identities; the original plan and evidence should be preserved. The native Linux execution amendment was recorded before timing after a sandbox `/proc` visibility issue affected the unrelated full-suite launch. Earlier sandbox preflight is retained as functional evidence; each measured invocation also ran its own native preflight.
