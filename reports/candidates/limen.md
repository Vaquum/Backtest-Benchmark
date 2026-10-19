# Limen

**Frozen source:** [Vaquum/Limen @ 29837e666604eee74a2ac94f328fb9803724342a](https://github.com/Vaquum/Limen/tree/29837e666604eee74a2ac94f328fb9803724342a)

**Observed license label:** MIT  
**Layer:** Managed research workflow plus snapshot/event execution

[Full grid](../comparison-grid.md) · [Replay results](../performance-results.md) · [Protocol](../../protocol/README.md)

**Computation:** Full snapshot is admitted to the common zero-cost replay; historical fitted-preparation reuse reduced fit counts without a demonstrated whole-campaign speedup.

**Academic:** Native temporal research, selection statistics and reserved-holdout machinery; a reproduced batch-quantile predictor violation and restricted holdout compatibility limit the relevant paths.

**Safety:** Research record/integrity and account controls coexist with reproduced resolver and manifest-read boundaries, inconsistent direct cost admission and a static nonfinite-parameter liveness defect.

## P01

### Parameter-space construction and retained memory

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Standard ParamSpace versus MSQ Grid initialization for identical domains and requested candidate count k

Legacy ParamSpace materializes requested candidates; MSQ Grid avoids Cartesian materialization. Construction time and scaling were not measured.

**Limit:** ParamSpace materializes O(k*d) values; MSQ Grid retains dimensions only initially. Comparing only initialization misses the legacy deletion bottleneck.

**Measurement state:** Historical Limen baseline; new common-contract measurements are separate

**Executable sources:** [limen/utils/param_space.py:73–109](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/utils/param_space.py#L73-L109); [limen/experiment/param_search/grid_strategy.py:36–61](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/param_search/grid_strategy.py#L36-L61)

**Repeatable criterion protocol:** Freeze parameter domains, types, ordering, intended candidate count and work layer. Measure domain construction separately from candidate consumption; report peak RSS, actual objects/rows retained and Cartesian cardinality. Distinguish task windows, raw data sharing and true lazy generation.

## P02

### Candidate generation throughput, novelty and exhaustion

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Standard generate(); MSQ Grid/Random/Sobol accepted candidate stream

Legacy generate repeatedly filters remaining rows; MSQ retains accepted hashes and random/Sobol retries can exhaust. Enumeration throughput was not measured.

**Limit:** Standard full consumption scans ~k² row positions; Grid has O(k) seen hashes; Random/Sobol impose 1000 retries. Uniformity/discrepancy criteria belong with methodological quality, not just speed.

**Measurement state:** Historical Limen baseline; new common-contract measurements are separate

**Executable sources:** [limen/utils/param_space.py:132–144](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/utils/param_space.py#L132-L144); [limen/experiment/param_search/search_strategy.py:130–175](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/param_search/search_strategy.py#L130-L175); [limen/experiment/param_search/random_strategy.py:51–60](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/param_search/random_strategy.py#L51-L60); [limen/experiment/param_search/sobol_strategy.py:50–66](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/param_search/sobol_strategy.py#L50-L66)

**Repeatable criterion protocol:** Freeze the accepted candidate sequence when comparing engine cost. Separately measure sampler generation across occupancy levels; retain proposed/accepted/duplicate/rejected/failed counts and timestamps. Distinguish deterministic finite enumeration from random or adaptive proposals.

## P03

### Cold process and first valid result latency

**Partial** · Measured, Tested · applicability `native` · capability `implemented`

**Scope:** Fresh source/pipeline construction through one semantically complete accepted output

First kernel calls: 0.910244 / 0.893429 ms. Adapter preparation: 102.716028 / 85.407332 ms. True process-to-first-valid-result latency remains unmeasured.

**Limit:** First-call figures belong to the declared public API/component scope. Process-launch-to-first-valid includes identity, imports, data, oracle and validation, not just engine startup. No full trained research campaign or fleet-level latency guarantee.

**Measurement state:** Measured for the linked finite single-host replay campaign; broader criterion scopes remain unmeasured

**Recorded measurements:**

```json
[
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "buy_and_hold",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "first_full_common_ms_median": 2.780865,
    "first_full_common_ms_min": 2.714034,
    "first_full_common_ms_max": 4.053496,
    "launch_to_ready_ms_median": 32.784438,
    "launch_to_first_valid_ms_median": 474.254026
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "first_full_common_ms_median": 2.528865,
    "first_full_common_ms_min": 2.376036,
    "first_full_common_ms_max": 3.256478,
    "launch_to_ready_ms_median": 28.026706,
    "launch_to_first_valid_ms_median": 411.346615
  }
]
```

**Executable sources:** [tests/backtest_benchmark/worker.py:78–105](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/backtest_benchmark/worker.py#L78-L105); [tests/benchmark_backtest_strategies.py:141–156](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/benchmark_backtest_strategies.py#L141-L156); [tests/benchmark_indicators.py:59–77](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/benchmark_indicators.py#L59-L77)

**Repeatable criterion protocol:** Separate process startup, source/build verification, dependency and engine imports, input reading, adapter construction, first native call, lazy extraction and parity. Use fresh processes and empty optional JIT caches; freeze native thread limits and retain first-versus-warm differences.

## P04

### Complete research campaign throughput and stage attribution

**Unknown** · Measured · applicability `native` · capability `implemented`

**Scope:** Specified split/model/search/recording contract from local source load through durable successful rounds

One 48-round pair: complete process 10.552471 s with fresh fitted preparation; 10.597700 s with reuse. General campaign throughput remains workload dependent.

**Limit:** No universal native model workload equivalence: DLinear uses ridge SVD; optional backends delegate training. A faster run that produces less evidence or different predictions is not comparable.

**Measurement state:** Historical Limen baseline; new common-contract measurements are separate

**Executable sources:** [limen/experiment/experiment_core.py:294–371](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L294-L371); [limen/experiment/experiment_core.py:579–599](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L579-L599); [limen/experiment/experiment_core.py:672–737](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L672-L737); [limen/sfd/reference_architecture/dlinear_regressor.py:102–116](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/reference_architecture/dlinear_regressor.py#L102-L116)

**Repeatable criterion protocol:** Freeze model family, temporal folds, preprocessing, accepted candidate sequence, precision, losses and output retention. Measure source/preparation/fit/predict/execution/metrics/persistence separately and end-to-end; count all attempts. An execution-only loop requires an explicit research adapter.

## P05

### Fitted preparation and prediction reuse

**Optional** · Measured · applicability `native` · capability `implemented`

**Scope:** Eligible serial deterministic snapshot GridStrategy workloads with factorize=True

Opt-in fitted reuse reduced target and scaler fits 24 to 1; model fits stayed 24. Outputs equal at 12 decimals; end-to-end ratio 0.995732, no demonstrated gain.

**Limit:** Harness varies fitted-prep reuse only, with signal reuse enabled in both arms. 128-entry caches; narrow admissible models/targets/scalers; incompatible with parallel/event/walk-forward/pruning. One pair cannot establish stable speedup.

**Measurement state:** Historical Limen baseline; new common-contract measurements are separate

**Executable sources:** [limen/experiment/_factorize.py:80–123](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_factorize.py#L80-L123); [limen/experiment/_factorize.py:177–273](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_factorize.py#L177-L273); [limen/experiment/_factorized_prep.py:41–80](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_factorized_prep.py#L41-L80); [tests/benchmark_factorized_preparation.py:119–229](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/benchmark_factorized_preparation.py#L119-L229)

**Repeatable criterion protocol:** Identify actual fitted-state or prediction reuse separately from raw-data sharing, deterministic feature caches or result memoization. Fix training support, models, candidate order and cost axes; count transform/model fits, compare complete scientific outputs and record cold/hit/invalidation/eviction cases. No speedup claim from availability alone.

## P06

### Indicator and feature kernel throughput by n and lookback

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** SMA/EMA/RSI/CCI/linearreg/stochastic/Hilbert/line features/FFD, preserving full aligned arrays

Mixture of NumPy scans, Python recurrences, O(n*w) windows and pairwise line searches. No uniform kernel speed or scaling claim is supported.

**Limit:** Kernel complexity is mixed: O(n) array scans or Python recurrences, O(n*w) windows, O(n*H) line detection. Archived exact parity is continuity evidence, not independent formula correctness; TA-Lib helper alone drops NaN positions.

**Measurement state:** Historical Limen baseline; new common-contract measurements are separate

**Executable sources:** [limen/indicators/sma.py:10–31](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/indicators/sma.py#L10-L31); [limen/indicators/_ema.py:16–36](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/indicators/_ema.py#L16-L36); [limen/indicators/cci.py:23–46](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/indicators/cci.py#L23-L46); [limen/indicators/stoch.py:69–111](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/indicators/stoch.py#L69-L111); [limen/utils/_line_arrays.py:21–47](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/utils/_line_arrays.py#L21-L47); [tests/test_indicators_vs_talib.py:1858–1876](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_indicators_vs_talib.py#L1858-L1876)

**Repeatable criterion protocol:** Compare actual aligned native outputs for equal recorded prefixes, period, lookback, dtype, null/NaN policy and timestamp availability. Separate core, wrapper, compilation and memory. A common externally prepared signal is not a native indicator benchmark.

## P07

### Snapshot backtest latency under full execution parity

**Partial** · Measured, Tested · applicability `native` · capability `implemented`

**Scope:** Zero-cost close-to-close all-in long/flat buy_and_hold and sma_cross on supplied 1h fixture

Independent execution parity passed on two zero-cost snapshot cases. Warm kernel medians 0.375106 / 0.342447 ms; full snapshot 2.150025 / 1.699665 ms for 8,783 bars.

**Limit:** One recorded single-instrument zero-cost contract and two fixed signals. Native APIs perform different extra work. Components and internal kernels cannot receive full-engine ratios; costs, data-size scaling, native indicators and other markets require separate campaigns.

**Measurement state:** Measured for the linked finite single-host replay campaign; broader criterion scopes remain unmeasured

**Recorded measurements:**

```json
[
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "buy_and_hold",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "warm_full_common_ms_median": 2.588815,
    "warm_engine_ms_median": 2.243234,
    "warm_extraction_common_ms_median": 0.306492,
    "warm_full_common_cpu_ms_median": 2.593646,
    "warm_process_medians_ms": [
      2.588815,
      2.280451,
      2.707605,
      2.758792,
      2.375383
    ],
    "warm_process_median_ms_min": 2.280451,
    "warm_process_median_ms_max": 2.758792,
    "warm_evaluation_bars_per_second": 3392671.936774161,
    "relative_to_limen_warm_full_common": 1.0
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "warm_full_common_ms_median": 2.00799,
    "warm_engine_ms_median": 1.702318,
    "warm_extraction_common_ms_median": 0.239572,
    "warm_full_common_cpu_ms_median": 2.012382,
    "warm_process_medians_ms": [
      2.067591,
      1.889551,
      2.00799,
      2.122612,
      1.773845
    ],
    "warm_process_median_ms_min": 1.773845,
    "warm_process_median_ms_max": 2.122612,
    "warm_evaluation_bars_per_second": 4374025.767060593,
    "relative_to_limen_warm_full_common": 1.0
  }
]
```

**Executable sources:** [limen/backtest/long_flat_strategy.py:96–133](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/long_flat_strategy.py#L96-L133); [tests/backtest_benchmark/contract.py:49–89](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/backtest_benchmark/contract.py#L49-L89); [tests/backtest_benchmark/worker.py:42–140](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/backtest_benchmark/worker.py#L42-L140); [tests/benchmark_backtest_strategies.py:123–184](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/benchmark_backtest_strategies.py#L123-L184)

**Repeatable criterion protocol:** Version cash, units, fees, slippage, decision/fill lag, liquidation, holding/equity conventions and every required observable. Admit only parity-verified native results against an independent oracle. Measure fresh native call and lazy common extraction together and separately; label full engine, native component and internal core distinctly.

## P08

### Event execution and forward-label scaling

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Full account ledger and both-side forward labels, with sparse/dense timers and funding modes

Event plans are bounded but timer ledgers can grow beyond plan limits. Forward trade labels can revisit long suffixes. Throughput and scaling remain unmeasured.

**Limit:** 8 plans/1M source-event cache does not bound timer ledger rows. Funding disables timer-span shortcut. Barrier-only forward labels may traverse long suffixes; funded candidate path recreates full ledger/source bindings.

**Measurement state:** Historical Limen baseline; new common-contract measurements are separate

**Executable sources:** [limen/backtest/_event_plan.py:21–67](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/_event_plan.py#L21-L67); [limen/backtest/_event_clock.py:10–33](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/_event_clock.py#L10-L33); [limen/backtest/trade_execution.py:246–357](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_execution.py#L246-L357); [limen/targets/trade_outcome.py:38–89](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/targets/trade_outcome.py#L38-L89); [limen/targets/trade_outcome.py:129–148](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/targets/trade_outcome.py#L129-L148)

**Repeatable criterion protocol:** Freeze recorded events, calendars, products, tie ordering, precision, queue/fill assumptions, funding, barriers and required output tape. Scale real input prefixes and actual event/asset/timer counts; separate event execution, ledger materialization and optional forward labels. Do not synthesize missing market depth from OHLC.

## P09

### Peak memory and resource amplification

**Partial** · Measured, Tested · applicability `native` · capability `implemented`

**Scope:** Complete serial/parallel campaign including sources, caches, IPC, models, logs and ledgers

Snapshot process peak RSS 99.859375 / 100.234375 MiB; fitted-preparation pair 358.746094 / 362.976563 MiB. Process-tree and scale behavior remain unmeasured.

**Limit:** Process high-water RSS includes imported dependencies, compilation and earlier calls; it is not incremental engine memory, process-tree PSS or a hard resource bound. Multi-asset/grid/parallel memory scaling remains unmeasured.

**Measurement state:** Measured for the linked finite single-host replay campaign; broader criterion scopes remain unmeasured

**Recorded measurements:**

```json
[
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "buy_and_hold",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "peak_rss_bytes_median": 131436544
  },
  {
    "campaign_id": "2026-10-19-common-zero-single-thread",
    "report": "results/campaigns/2026-10-19-common-zero-single-thread/report.json",
    "strategy": "sma_cross",
    "rank_against_full_engine": true,
    "independent_processes": 5,
    "peak_rss_bytes_median": 132571136
  }
]
```

**Executable sources:** [limen/utils/_computation_cache.py:23–64](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/utils/_computation_cache.py#L23-L64); [limen/experiment/_factorize.py:227–233](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_factorize.py#L227-L233); [limen/experiment/_parallel_rounds.py:167–174](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_rounds.py#L167-L174); [tests/benchmark_parallel_rounds.py:39–64](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/benchmark_parallel_rounds.py#L39-L64)

**Repeatable criterion protocol:** Record input/retained/output sizes, per-process high-water RSS and, in a dedicated campaign, process-tree RSS/PSS with sampling interval. Include worker sharing, IPC, compilation, caches, models and records. Distinguish entry-count cache limits, live allocations, resident memory and proven hard resource bounds.

## P10

### Parallel speedup, efficiency and load imbalance

**Optional** · Inspected · applicability `native` · capability `implemented`

**Scope:** Eligible compiled CPU logreg/LightGBM rounds at workers 1,2,4,... with native_threads=1

Restricted spawned CPU workers, bounded pending queue and ordered commitment. No speedup or utilization measurement; factorization is rejected in parallel mode.

**Limit:** Compiled CPU logreg/LightGBM only; factorization and post_processing rejected. FIFO pending[0] wait and worker-count pending capacity reduce heterogeneous utilization. Do not interpret the visible CPU affinity mask as guaranteed effective CPU quota.

**Measurement state:** Historical Limen baseline; new common-contract measurements are separate

**Executable sources:** [limen/experiment/_parallel_rounds.py:43–63](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_rounds.py#L43-L63); [limen/experiment/_parallel_rounds.py:167–237](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_rounds.py#L167-L237); [limen/experiment/_parallel_worker.py:101–120](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_worker.py#L101-L120); [limen/experiment/_parallel_worker.py:196–245](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_worker.py#L196-L245); [tests/benchmark_parallel_rounds.py:144–175](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/benchmark_parallel_rounds.py#L144-L175)

**Repeatable criterion protocol:** Run a fixed accepted workload at workers1,2,4,... with native inner threads fixed, after full scientific-output parity. Retain scheduling order, start/end intervals, worker/parent commit time and process-tree memory. Distinguish I/O prefetch from parallel simulation or model fitting; no inferred speedup from worker availability.

## P11

### Cache locality, hit cost and optimization coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Computation, fitted-prep, prediction and EventPlan caches at cold/warm/eviction boundaries

Serial reuse and narrow factorization caches exist. Factorized caches are capped at 128 entries, not bytes; workers do not share the parent reuse context.

**Limit:** Array keys require O(n) scan/bytes even on hits; failures/unsafe configurations bypass or reject reuse. Sources/functions admitted differ across factorization/parallel paths; a cache hit is not zero work and unknown coverage is not a pass.

**Measurement state:** Historical Limen baseline; new common-contract measurements are separate

**Executable sources:** [limen/utils/_computation_cache.py:32–49](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/utils/_computation_cache.py#L32-L49); [limen/utils/_computation_cache.py:86–122](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/utils/_computation_cache.py#L86-L122); [limen/experiment/_factorized_prep.py:64–83](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_factorized_prep.py#L64-L83); [limen/backtest/_event_plan.py:27–67](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/_event_plan.py#L27-L67); [tests/test_factorized_cache_bounds.py:32–158](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_factorized_cache_bounds.py#L32-L158)

**Repeatable criterion protocol:** Name the exact cached entity: raw bytes, features, fit state, predictions, quotes, execution plan or result. Compare cold/hit/eviction/resume under identical outputs; mutate consumed source/config fields individually and require fresh-equivalent results. Measure hash/copy/lookup cost, actual bytes and retained-entry limits.

## P12

### Recording/checkpoint overhead and restart recovery

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Full terminal prefix with recording variants and interrupted serial/parallel campaigns

Content-addressed recording avoids repeated disk blobs after serialization and hashing. Recovery validates/reconstructs history. Recording and restart scaling unmeasured.

**Limit:** Dedup avoids repeated blob writes after serializing/hashing complete payload each round. CSV/results remain append/log work. Parallel resume loads committed payloads and rewrites/truncates prefix; fitted caches are cold. Individual blob size limits do not bound total run storage.

**Measurement state:** Historical Limen baseline; new common-contract measurements are separate

**Executable sources:** [limen/experiment/experiment_core.py:672–739](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L672-L739); [limen/experiment/_parallel_commit.py:125–139](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_commit.py#L125-L139); [limen/experiment/_round_storage.py:133–178](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_round_storage.py#L133-L178); [limen/experiment/_parallel_resume.py:171–259](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_resume.py#L171-L259); [limen/experiment/checkpoint_manager.py:126–151](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/checkpoint_manager.py#L126-L151)

**Repeatable criterion protocol:** Treat plain result serialization and complete checkpoint continuation as distinct sub-capabilities. Measure writes/bytes/hash/compression and output-equivalent recording modes; interrupt at declared commit boundaries and compare the full durable ordered prefix after restart. Distinguish process crash, power loss and competing writers.

## A01

### Causal predictor invariance

**Fails** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Point-in-time predictor values from native batch features; successive-prefix inference evaluated separately

Reproduced within-split lookahead in quantile_price_lines: 173 of 192 existing rows changed after extending to 384 rows. Both control configurations changed zero rows. Failed independent probe on quantile_price_lines; no generic causal enforcement.

**Limit:** Observed count describes this fixture/configuration only; it is not a population defect rate. Split-first processing does not remove this within-split lookahead. Shipped native LightGBM prep includes this feature. This is a failure of historical row values computed over complete evaluation batches. Using only the final row of successive available prefixes can be causal; that distinct path is not invalidated merely by calling the same function.

**Executable sources:** [limen/features/quantile_price_lines.py:146–189](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/features/quantile_price_lines.py#L146-L189); [limen/sfd/foundational_sfd/lightgbm_binary.py:82–103](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/foundational_sfd/lightgbm_binary.py#L82-L103); [limen/features/__init__.py:62–70](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/features/__init__.py#L62-L70); [tests/test_feature_causality.py:17–57](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_feature_causality.py#L17-L57)

**Repeatable criterion protocol:** For each supported interface, declare the decision time and information set. Compare historical outputs on an unchanged recorded prefix with the corresponding outputs after a future extension, excluding legitimately incomplete targets and declared warmup rows. Retain changed-row counts, first divergence, numerical tolerance, and a causal control. Separately test latest-row-only prefix replay and point-in-time data getters. Distinguish a native future-dependent operation from caller-supplied future inputs or unrestricted custom callbacks; an execution engine's callback ordering does not prove arbitrary user features causal.

## A02

### Training and evaluation isolation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Built-in MLManifest preparation versus arbitrary Python callbacks

Native path splits raw input first and fits preprocessing on training data. Custom callbacks and a pre-split selector can see broader data; no universal isolation guarantee. Implemented for built-in split-first and fitted preprocessing; caller-dependent for custom functions.

**Limit:** Pre-split selector sees complete admitted frame; arbitrary feature callables are not inspected for causality; custom architecture gets entire prepared dictionary.

**Executable sources:** [limen/experiment/manifest_core.py:1888–1907](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/manifest_core.py#L1888-L1907); [limen/experiment/manifest_core.py:1647–1658](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/manifest_core.py#L1647-L1658); [limen/experiment/manifest_core.py:1693–1714](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/manifest_core.py#L1693-L1714); [tests/test_walk_forward_uel.py:289–363](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_walk_forward_uel.py#L289-L363)

**Repeatable criterion protocol:** Identify which component owns each fitted object and record its exact source-row support, fit cutoff, and evaluation membership. With split identities fixed, change only later held-out records using permitted recorded observations and compare fitted state and earlier outputs. Trace target construction, feature processing, model selection, and cache reuse as well as model fitting. Do not infer a managed research capability from a generic training callback. Where the execution layer has no native fitted model, mark the research requirement as adapter-required rather than grading the engine as a failed learner.

## A03

### Label availability and censoring

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Built-in forward targets and bound private trade labels

Built-in shifted labels are censored within splits; trade labels expose availability. Custom label horizons and availability require explicit verification. Partial: split-local forward-label censoring and explicit trade-label availability; caller-supplied label semantics unverified.

**Limit:** No universal derivation of generic walk-forward purge from target horizon. Physical split-local generation already prevents these built-in targets from reading next split, so missing auto sizing is not itself demonstrated leakage.

**Executable sources:** [limen/targets/next_return.py:39–42](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/targets/next_return.py#L39-L42); [limen/targets/next_bar_up.py:34–37](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/targets/next_bar_up.py#L34-L37); [limen/targets/tradeline_long_binary.py:100–120](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/targets/tradeline_long_binary.py#L100-L120); [limen/sfd/reference_architecture/direction_sizing.py:61–76](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/reference_architecture/direction_sizing.py#L61-L76)

**Repeatable criterion protocol:** Retain source-row identity, decision time, local observation time where relevant, label completion time, and fit cutoff for every consumed target. Verify that fit support excludes unfinished outcomes and that split-terminal targets are censored or purged according to the implemented horizon. Inspect negative shifts and forward windows as target operations separately from predictor construction. Check actual post-filter membership and adaptive event horizons, not just a configured gap. A known future calendar event is not itself an unavailable outcome. For engines without native targets, identify the adapter obligation explicitly.

## A04

### Temporal split geometry

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Configured walk-forward and ordinary ratio/date splitters

Walk-forward enforces ordered timestamps, fold geometry and configured purge/embargo. Gaps are not generally derived automatically from target horizons. Implemented explicit walk-forward geometry; stronger validation than default positional splitter.

**Limit:** Walk-forward requires sorted unique datetimes but does not enforce a universal regular cadence; raw row-count gaps are not automatically label/event-time gaps. Generic ratio split slices current row order.

**Executable sources:** [limen/data/utils/split_walk_forward.py:48–67](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/utils/split_walk_forward.py#L48-L67); [limen/experiment/_walk_forward_split.py:63–88](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_walk_forward_split.py#L63-L88); [limen/data/utils/splits.py:22–44](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/utils/splits.py#L22-L44); [tests/test_walk_forward_contracts.py:39–103](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_walk_forward_contracts.py#L39-L103)

**Repeatable criterion protocol:** Declare identical raw observation windows, chronology, rolling or expanding policy, retained history, and evaluation schedule before comparing solutions. Audit actual sample membership after label censoring, missing-value removal, warmup, and transform filtering. Verify any purge or embargo against the outcomes actually used and state whether the guard is mandatory or configured. Test boundary ordering and empty or insufficient windows. Separate an online trailing estimator from a supervised cross-validation workflow; replay chunks, reporting periods, and rebalance schedules do not by themselves implement independent validation.

## A05

### Fold-local preprocessing and stacking

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Walk-forward ML and conditional direction/sizing

Walk-forward refits copied manifests per fold. Conditional stacking uses earlier completed labels and refits its scaler/PCA inside inner folds. Implemented locally with explicit availability purge.

**Limit:** The underlying feature functions have already been applied to raw training rows; noncausal features remain possible. This is not a universal nested-validation protocol.

**Executable sources:** [limen/experiment/_walk_forward_run.py:152–165](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_walk_forward_run.py#L152-L165); [limen/sfd/reference_architecture/direction_sizing.py:163–188](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/reference_architecture/direction_sizing.py#L163-L188); [limen/experiment/_prepare_trade_context.py:306–325](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_prepare_trade_context.py#L306-L325)

**Repeatable criterion protocol:** Hold observation identities and folds fixed. For every learned transform and estimator, inspect fit support, application support, state reuse, and refit timing. Verify that validation or evaluation data cannot alter an earlier fitted object and that out-of-fold predictions are produced without training on the current row or any outcome unavailable at its decision time. Include nested preprocessing and second-stage model labels. Distinguish a deterministic rolling calculation from a learned transform, and report absent native model ownership as adapter-required rather than asserting leakage from the absence of a pipeline manager.

## A06

### Calibration and threshold selection

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Built-in binary model calibration and event validation objective

Native calibration and threshold selection use validation data. Using the same validation sample for both is selection, not an independent performance estimate. Validation-only selection implemented; independent calibration assessment remains external.

**Limit:** Configured validation score is optimized on that same sample, so it is not an unbiased future-performance estimate. Objective currently permits specific binary built-ins and event execution only.

**Executable sources:** [limen/calibration/probability.py:17–42](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/calibration/probability.py#L17-L42); [limen/calibration/pipeline.py:61–69](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/calibration/pipeline.py#L61-L69); [limen/calibration/_objective_threshold.py:18–30](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/calibration/_objective_threshold.py#L18-L30); [limen/experiment/_objective.py:86–130](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_objective.py#L86-L130)

**Repeatable criterion protocol:** Record separate sample identities and evidence access for estimator training, calibration, policy selection, and final evaluation. Trace whether calibration labels or policy-objective outcomes are reused in the reported selection score. Declare the action space, costs, risk constraints, and optimization objective; include an all-flat action when it is admissible under that economic decision contract. Evaluate the frozen selected policy on an external final sample. Distinguish parameter optimization from probability calibration and do not require an execution-only engine to implement either without a stated research adapter.

## A07

### Metric definitions and aggregation

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Binary metrics, walk-forward summaries and execution return tapes

Explicit metric implementations exist, but finite fold results are averaged arithmetically. balanced_metric means precision times square root of positive prediction rate. Implemented with materially different conventions requiring normalization.

**Limit:** Mean fold return is not concatenated compounded return; averaged counts are not pooled confusion counts. Finite-only averaging can hide unavailable fold metrics.

**Executable sources:** [limen/metrics/binary_metrics.py:53–64](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/metrics/binary_metrics.py#L53-L64); [limen/experiment/_walk_forward_run.py:107–121](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_walk_forward_run.py#L107-L121); [limen/experiment/_walk_forward_run.py:58–73](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_walk_forward_run.py#L58-L73); [limen/metrics/balanced_metric.py:39–45](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/metrics/balanced_metric.py#L39-L45)

**Repeatable criterion protocol:** Recompute comparable metrics from a shared audited observation and equity or return tape. Pin prediction and action semantics, currency and capital basis, cash flows, gross or net costs, sampling calendar, annualization, compounding, variance and moment conventions, and benchmark alignment. Record warmup and terminal-position policies, missing or nonfinite handling, zero-variance sentinels, and fallback return bases. Distinguish averages of fold metrics from metrics on pooled ordered returns. A matching metric name or output hash is insufficient evidence of a matching mathematical quantity.

## A08

### Numerical and mathematical verification

**Partial** · Inspected, Measured · applicability `native` · capability `implemented`

**Scope:** DSR/PBO and numerical correctness test surfaces

DSR/PBO formulas, edge checks and alternate in-repository formula assertions exist. Snapshot execution parity was independently measured. Numerical agreement does not establish inferential calibration or generalization. Implemented formulas and local oracle/property checks; statistical calibration unproven.

**Limit:** An alternate formula in the same repository is useful verification but not independent academic validation or empirical false-positive calibration.

**Executable sources:** [limen/metrics/deflated_sharpe_ratio.py:24–55](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/metrics/deflated_sharpe_ratio.py#L24-L55); [limen/metrics/probability_of_backtest_overfitting.py:37–58](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/metrics/probability_of_backtest_overfitting.py#L37-L58); [tests/test_acceptance_gates.py:32–114](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_acceptance_gates.py#L32-L114)

**Repeatable criterion protocol:** Separate independent analytical or ledger oracles, optimized-versus-reference parity, metamorphic temporal checks, empirical probability calibration, and empirical execution-model validation. Prefer expected quantities derived without reusing the implementation under test. Retain exact source and dependency identity, executable or binary identity where available, fixture hashes, tolerances, test invocation, and result artifacts. Label source-inspected assertions separately from tests actually executed in this assessment, and report the bounded test set. Passing an implementation parity test does not establish statistical calibration or real-market execution fidelity.

## A09

### Convergence and fit stability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Experiment successful/failed round records

Convergence warnings and missing evidence are recorded. A warned model can remain successful/selected; diagnostic reporting is not an admission gate. Diagnostic warning frequency implemented; no automatic model exclusion.

**Limit:** Absence of this warning is not proof of optimization convergence. Default warning evidence does not prevent downstream selection; user warning-as-error settings can abort.

**Executable sources:** [limen/experiment/convergence_report.py:33–52](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/convergence_report.py#L33-L52); [limen/experiment/convergence_report.py:55–91](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/convergence_report.py#L55-L91); [limen/experiment/experiment_core.py:157–164](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L157-L164)

**Repeatable criterion protocol:** For each applicable fitting stage, retain termination reason, iteration or evaluation budget, warnings, exceptions, and any fallback selected. Carry warned successes and failed attempts into the declared attempt denominator and predeclare their selection eligibility. Check whether downstream records distinguish an optimized solution from a default or equal-weight fallback. Assess stability of the selected result under meaningful repeated fits or perturbations when supported and authorized. A completed simulation is not evidence of model convergence; a framework with no iterative fitted component has an adapter requirement rather than a convergence failure.

## A10

### Search-family history completeness

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Per-run returns/CSV and explicitly supplied experiment families

Recorded local successes/failures and family identity checks support accounting. Unlogged, deleted, external or pruned search history is not globally recoverable. Partial local inventory; no global complete search history.

**Limit:** Failed attempts lack return tracks; supplied runs do not reveal deleted, crashed, pruned, external or undisclosed searches. Local count is not effective independent-trial count.

**Executable sources:** [limen/experiment/acceptance_report.py:86–100](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/acceptance_report.py#L86-L100); [limen/experiment/experiment_core.py:365–368](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L365-L368); [limen/experiment/_family_evidence.py:232–267](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_family_evidence.py#L232-L267)

**Repeatable criterion protocol:** Predeclare the search family or adaptive search policy, evidence-access rules, and budget. Append every attempted configuration and occurrence, including failed, warned, cancelled, repeated, and resumed attempts, with seeds, costs, data identity, source identity, and terminal disposition. Reconcile searchable results with the attempt ledger and preserve selection decisions. Distinguish a local parameter product or a supplied collection of successful results from the full effective research family; count choices made outside that collection when they influenced selection. A final best-result object alone is not a complete search history.

## A11

### Multiple-selection and dependence control

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** DSR and CSCV PBO reports

DSR/PBO diagnostics are conditional on retained comparable tracks. Default two-block PBO has only three possible values; no serial-covariance correction in DSR. Implemented conditional diagnostics, with important inferential limits.

**Limit:** Statistics are not auto acceptance gates: report verdict false/null does not reject training or Sensor creation. No universal correction for adaptive search, regime dependence or hidden trials.

**Executable sources:** [limen/metrics/deflated_sharpe_ratio.py:33–55](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/metrics/deflated_sharpe_ratio.py#L33-L55); [limen/metrics/probability_of_backtest_overfitting.py:47–58](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/metrics/probability_of_backtest_overfitting.py#L47-L58); [limen/experiment/_acceptance_settings.py:15–19](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_acceptance_settings.py#L15-L19); [limen/experiment/_acceptance_settings.py:105–115](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_acceptance_settings.py#L105-L115); [limen/experiment/acceptance_report.py:138–159](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/acceptance_report.py#L138-L159); [limen/experiment/experiment_core.py:157–159](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L157-L159)

**Repeatable criterion protocol:** Declare the inferential target, null, candidate family or adaptive policy, and dependence assumptions. Use aligned observations and the complete declared selection family where the method requires them. Distinguish marginal significance or probabilistic Sharpe from corrections for multiple selection, and a diagnostic from an enforced admission rule. Audit effective sample size, horizon overlap, serial dependence, moment conventions, resampling unit, and degenerate outcomes. Evaluate calibration separately where empirical evidence exists. Never treat combinatorial partitions or overlapping folds as independent observations, or a zero Monte Carlo exceedance count as a proven zero error probability.

## A12

### Cross-run evaluation comparability

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Family acceptance reports over supplied directories

Family diagnostics check aligned timestamps and execution identity and withhold unsupported conclusions. Snapshot joint PBO lacks full comparable source identity. Implemented conservative grouping; snapshot joint PBO withheld.

**Limit:** Declared source identities are not independently verified; snapshot artifacts lack full OHLC execution identity so family PBO is unavailable; family selection itself can add multiplicity.

**Executable sources:** [limen/experiment/acceptance_report.py:36–83](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/acceptance_report.py#L36-L83); [limen/experiment/_family_evidence.py:130–171](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_family_evidence.py#L130-L171); [limen/experiment/_family_evidence.py:174–229](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_family_evidence.py#L174-L229); [limen/experiment/family_acceptance_report.py:32–56](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/family_acceptance_report.py#L32-L56); [limen/experiment/family_acceptance_report.py:98–105](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/family_acceptance_report.py#L98-L105)

**Repeatable criterion protocol:** Require the same ordered evaluation identities and a declared mapping of assets, decision times, data availability, capital, costs, and return conventions. Retain actual post-warmup observations, configuration, source and environment identifiers, input digests, and failure dispositions. Reject incompatible results with reasons rather than silently intersecting samples. Check whether persisted artifacts and asynchronous logging preserve the evidence needed to reproduce selection. Distinguish a canonical output digest from input or build identity and a date-based data-vintage selector from immutable content verification. Report native compatibility checks separately from adapter checks.

## A13

### Final holdout protocol and compatibility

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Reserved local holdout for native dated binary Sensors/Cohorts

Reserved holdout freezes supported fitted state and records attempts before loading data. Research and final-assessment compatibility is substantially restricted. Strong restricted protocol; incompatible with several principal research modes.

**Limit:** Only native exact LogRegBinary/LightGBMBinary inference with dated non-event data; reservation refuses custom SFDs, WF, parallel/factorized/resume/profile/bars/event/funding/callbacks. Repeated assessments are labelled, not prohibited; external exposure always unknown.

**Executable sources:** [limen/experiment/_holdout_research.py:71–100](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_research.py#L71-L100); [limen/experiment/_holdout_research.py:225–240](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_research.py#L225-L240); [limen/experiment/_holdout_freeze.py:159–225](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_freeze.py#L159-L225); [limen/experiment/_holdout_freeze.py:281–342](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_freeze.py#L281-L342); [limen/experiment/_holdout_assessment.py:91–113](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_assessment.py#L91-L113); [limen/experiment/_holdout_assessment.py:153–174](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_assessment.py#L153-L174); [limen/experiment/_holdout_report.py:146–162](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_report.py#L146-L162)

**Repeatable criterion protocol:** Freeze the selected policy, fitted objects or allowed refit rule, features, data interpretation, costs, and execution scenarios before final-data access. Record an attempt durably before exposure and retain every attempt, result, failure, and subsequent access in the owned workflow. Verify point-in-time evaluation and state the supported and rejected paths. Label access history as initial-recorded, subsequent, unknown, or post-release as appropriate. Do not equate a train/test split or a repeatedly viewed optimization test window with a reserved final holdout, or claim that a local ledger prevents external reading of the same data.

## A14

### Baseline quality and external validity

**Unknown** · Inspected · applicability `native` · capability `implemented`

**Scope:** Fixed strategy baselines, random actions and future use claims

Executable strategy references exist. No external-comparator ranking, profitable generalization or cross-venue robustness was established in this review. Baseline code available; comparative profitable generalization unknown.

**Limit:** RandomBinary maps random actions to .9/.1 scores and uses global RNG, so it is not a calibrated probabilistic null. Correct implementation tests do not establish market edge.

**Executable sources:** [limen/sfd/rule_based/common_strategies.py:17–34](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/rule_based/common_strategies.py#L17-L34); [limen/sfd/rule_based/common_strategies.py:72–139](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/rule_based/common_strategies.py#L72-L139); [limen/sfd/reference_architecture/random_binary.py:53–56](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/reference_architecture/random_binary.py#L53-L56); [limen/sfd/foundational_sfd/common_strategies.py:33–47](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/sfd/foundational_sfd/common_strategies.py#L33-L47)

**Repeatable criterion protocol:** Match data availability, evaluation dates, costs, exposure and risk budget, capacity assumptions, execution semantics, and selection opportunity across candidate and reference strategies. Use buy-and-hold, fixed rules, random or resampled controls, and simple learned baselines where relevant, recording all choices. Assess predictive generalization separately from execution-model fidelity and distinguish code capability from demonstrated empirical validity. Use recorded data appropriate to each specialist track; do not manufacture order-book evidence from OHLC bars. State which assets, periods, regimes, fill assumptions, and real-world effects remain unvalidated.

## A15

### Sensitivity, ablation and reproducibility

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Feature ablation, recorded evidence and parameter diagnostics

Seeded feature ablation and replay mechanisms exist. IID trial-row correlation bootstrap is not a dependence-aware market-return uncertainty estimate. Partial mechanisms implemented; robustness outcomes require measurement.

**Limit:** IID trial-row bootstrap intervals describe sampled trial correlations, not time-series strategy-return uncertainty or causal feature importance. Rich artifacts alone do not guarantee stable generalization.

**Executable sources:** [limen/experiment/manifest_core.py:1551–1605](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/manifest_core.py#L1551-L1605); [limen/log/_experiment_parameter_correlation.py:123–140](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/log/_experiment_parameter_correlation.py#L123-L140); [limen/experiment/_holdout_freeze.py:317–342](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_freeze.py#L317-L342); [tests/test_walk_forward_uel.py:366–414](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_walk_forward_uel.py#L366-L414)

**Repeatable criterion protocol:** Predeclare a bounded set of meaningful perturbations such as feature removal, parameter changes, costs, latency, queue assumptions, model seeds, and recorded market regimes. Preserve observation, configuration, source, dependency, and runtime identity and compare each perturbation against the same declared reference contract. Distinguish the existence of configurable knobs or a bootstrap helper from an executed sensitivity or ablation result. Report uncertainty intervals with the resampling unit and dependence assumptions, retain failures and repeated draws, and check whether fixed seeds unintentionally reproduce the same sample instead of generating a reproducible sequence.

## S01

### Untrusted configuration callable boundary

**Fails** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** YAML parse/validate/build_manifest/data-source execution when manifests are supplied by another party

Allowed-prefix traversal resolves limen.data.historical_data.os.system; modified manifest validates and binds that callable. Identity checked only; callable never invoked.

**Limit:** Namespace-prefix matching followed by unrestricted getattr permits imported external objects. This is a consequential failure for hostile configuration, not evidence of an exposed remote deployment. Trusted Python callbacks remain trusted execution by design.

**Executable sources:** [limen/yaml/resolver.py:39–55](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/resolver.py#L39-L55); [limen/data/historical_data.py:3–20](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/historical_data.py#L3-L20); [limen/yaml/rules.py:28–46](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/rules.py#L28-L46); [limen/yaml/compiler.py:104–119](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/compiler.py#L104-L119); [limen/experiment/manifest_core.py:207–236](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/manifest_core.py#L207-L236)

**Repeatable criterion protocol:** Trace parser, schema, resolver, attribute lookup and final invocation together. Where executable guards constrain code selection, check disallowed names, prefix collisions, imported-attribute traversal, trust-flag types and pickle globals without invoking dangerous targets. Record defaults and explicit opt-outs. Treat ordinary trusted Python/compiled strategies as code, not a sandbox failure; a fixed engine without a constrained configuration surface is out of scope for that surface.

## S02

### Input schema and numeric admission consistency

**Partial** · Inspected, Reproduced, Measured · applicability `native` · capability `implemented`

**Scope:** Manifest validation versus public direct snapshot/event/sensor APIs

Native Manifest/event paths reject negative costs; direct snapshot accepts negative fee/slippage. Numeric admission guarantees vary by API.

**Limit:** Many Manifest checks are strong; direct snapshot helpers omit equivalent cost admission. Unknown YAML keys default to warnings in some blocks. A validation percentage must not hide route-specific failures.

**Executable sources:** [limen/yaml/parser.py:24–69](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/parser.py#L24-L69); [limen/yaml/rules.py:253–279](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/rules.py#L253-L279); [limen/backtest/_snapshot_execution.py:45–123](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/_snapshot_execution.py#L45-L123); [limen/backtest/long_flat_strategy.py:74–133](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/long_flat_strategy.py#L74-L133); [limen/experiment/_resolve_backtest_config.py:42–47](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_resolve_backtest_config.py#L42-L47); [limen/backtest/trade_contract.py:107–126](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_contract.py#L107-L126)

**Repeatable criterion protocol:** Run the same applicable invalid-type, NaN/Inf, bound, missing/duplicate field, axis/shape and unknown-key corpus at each route. Record rejection type and stage, unchanged-state checks and any numerical consequences of accepted inputs. Test Python assertions under the declared optimization mode. Separate intended sentinels, score domains, fee rebates and borrowing from invalid values; never compare rejection percentages across different applicable corpora.

## S03

### Algorithm and process resource bounds

**Fails** · Inspected · applicability `native` · capability `implemented`

**Scope:** Feature generation, input parsing, event scheduling and worker runtime

Nonfinite fractional-difference parameters can create an unbounded weight loop (static proof). No general per-round deadline or process memory quota.

**Limit:** NaN d or nonzero d with NaN threshold passes fractional_diff guards; weights append forever because the only comparison-based break stays false. Parser reads whole input. Storage/cache caps do not imply an experiment-wide RAM, disk or runtime quota. Static proof only; no harmful loop executed.

**Executable sources:** [limen/features/fractional_diff.py:30–40](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/features/fractional_diff.py#L30-L40); [limen/features/fractional_diff.py:74–97](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/features/fractional_diff.py#L74-L97); [limen/yaml/parser.py:27–33](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/parser.py#L27-L33); [limen/experiment/_round_storage.py:24–25](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_round_storage.py#L24-L25); [limen/backtest/_event_plan.py:21–24](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/_event_plan.py#L21-L24); [limen/backtest/_event_plan.py:62–66](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/_event_plan.py#L62-L66); [limen/experiment/_parallel_rounds.py:208–218](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_rounds.py#L208-L218)

**Repeatable criterion protocol:** Inspect progress/termination conditions, finite parameter checks, dimensions, queue capacities, concurrency limits and workload deadlines. Probe extreme small inputs only under an external process deadline and memory limit. Report admitted work, peak RSS, wall time and cleanup, separating simulated-time deadlines, polling intervals, managed-heap monitors and hard process limits. Do not execute an unbounded case without containment.

## S04

### Data source network, archive and path boundaries

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** HistoricalData CSV/Parquet/ZIP/local/HTTP(S) ingestion and dataset cache

Main HTTP path has timeout/retries but no response/decompression size cap or general destination/path containment. Legacy Binance helper omits a request timeout.

**Limit:** General file and URL access is trusted-local functionality. A shared service would need external destination/path restrictions. Main downloads are bounded by a request timeout but read full content; the legacy Binance request has no explicit timeout. ZIP members are streamed to a parser rather than extracted, so conventional extract-path traversal is not observed. Cache hits trust filename identity.

**Executable sources:** [limen/data/historical_data.py:71–73](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/historical_data.py#L71-L73); [limen/data/historical_data.py:302–322](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/historical_data.py#L302-L322); [limen/data/historical_data.py:349–387](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/historical_data.py#L349-L387); [limen/data/historical_data.py:427–466](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/historical_data.py#L427-L466); [limen/data/historical_data.py:539–561](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/historical_data.py#L539-L561); [limen/data/_internal/binance_file_to_polars.py:20–29](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/data/_internal/binance_file_to_polars.py#L20-L29)

**Repeatable criterion protocol:** Use controlled local fixtures to check scheme/address policy, redirect behavior, path normalization and containment, connection/read/overall timeouts, response bytes, decompressed bytes/member counts and cache/source revalidation. Keep traversal probes entirely inside one newly created temporary root. Attribute guarantees only to actual call paths and the pinned standard-library/dependency version. An already-loaded-array engine requires a separately audited ingestion adapter.

## S05

### Manifest content-address verification on read

**Partial** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Committed manifest URI resolution, existing-content reuse, and family-evidence verification

A manifest URI still resolves after scratch content changes while retaining its lineage label. Other execution/family paths do recompute content identity.

**Limit:** URI/store paths check label rather than current content. Family evidence and runtime-generated metadata do recompute hashes, so the failure is not universal across provenance consumers. Hashes establish consistency, not authenticity against an owner able to rewrite all records.

**Executable sources:** [limen/yaml/store.py:45–47](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/store.py#L45-L47); [limen/yaml/store.py:175–186](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/store.py#L175-L186); [limen/yaml/store.py:244–260](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/yaml/store.py#L244-L260); [limen/experiment/experiment_core.py:1017–1019](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/experiment_core.py#L1017-L1019); [limen/experiment/_family_evidence.py:65–88](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_family_evidence.py#L65-L88); [tests/test_yaml_store.py:167–176](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_yaml_store.py#L167-L176)

**Repeatable criterion protocol:** Declare exactly which bytes and semantic fields each identifier binds. Change a non-identity field or referenced artifact while retaining the claimed digest/key and require consumers claiming that identity to recompute and reject mismatches. Test malformed hashes, alias/prefix ambiguity and changed reference targets. Distinguish UUIDs, configuration-only cache keys, canonical result digests and full study manifests. Fixed execution routes need an identity adapter for a managed-research comparison.

## S06

### Recorded round corruption and reference integrity

**Enforced** · Inspected, Tested · applicability `native` · capability `implemented`

**Scope:** gzip-jsonl-v2 rounds and content-addressed market/signal blobs

Round readers enforce digest/reference contracts and bounded members. Corruption tests verify rejection before stored bytes or modification times change.

**Limit:** Enforced within the inspected compressed recording contract. Per-record integrity and content hashes are not signatures, global file quotas, protection from symlink-owner attacks, or proof all consumer paths validate identical semantics. The cited corruption/reference tests ran in the selected local test campaign; this is not a full-suite claim.

**Executable sources:** [limen/experiment/_round_storage.py:28–45](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_round_storage.py#L28-L45); [limen/experiment/_round_storage.py:54–78](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_round_storage.py#L54-L78); [limen/experiment/_round_storage.py:102–129](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_round_storage.py#L102-L129); [limen/experiment/_round_signals.py:19–28](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_round_signals.py#L19-L28); [tests/test_round_storage.py:171–211](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_round_storage.py#L171-L211); [tests/test_round_signals.py:241–285](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_round_signals.py#L241-L285)

**Repeatable criterion protocol:** For the declared format, mutate headers/checksums, encoding, order, duplicate IDs, references, digests, missing members, counts and aligned arrays. Verify the documented-by-code error route, expected logical reconstruction and whether failure changes bytes/mtime. Distinguish explicit cache invalidation/recompute from fail-closed immutable admission, type allowlists from integrity hashes, and hashes from tamper authentication. State which optional backend and verifier must be enabled.

## S07

### Crash/restart consistency and durable commit frontier

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Experiment checkpoint and parallel resume over CSV, compressed records, blobs and audits

Atomic replacement and prefix validation aid restart. No fsync, experiment-directory writer lock or single transaction across all output files.

**Limit:** Extensive prefix validation and ordered commit design; ordinary checkpoint replacement is atomic at the file-name level but has no fsync, output files are separately written and no directory-wide writer lock is present. Power-loss/network-filesystem/multi-writer guarantees are unestablished.

**Executable sources:** [limen/experiment/checkpoint_manager.py:282–300](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/checkpoint_manager.py#L282-L300); [limen/experiment/_parallel_commit.py:123–135](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_commit.py#L123-L135); [limen/experiment/_parallel_resume.py:147–214](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_resume.py#L147-L214); [limen/experiment/_parallel_resume.py:235–259](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_resume.py#L235-L259); [limen/experiment/_round_storage.py:231–259](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_round_storage.py#L231-L259)

**Repeatable criterion protocol:** Interrupt at write, flush, rename, database commit, watermark and acknowledgement boundaries. Require exact logical committed-prefix identity, coherent parameters/predictions/orders/results and defined recovery of in-flight work. Test competing writers and malformed committed evidence. Report process kill, write exception, OS/power loss and network-storage cases separately. Do not equate a local atomic batch with exactly-once external orders, or in-memory caches with durable experiment restart.

## S08

### Parallel worker failure handling and bounded dispatch

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Admitted built-in compiled CPU logreg/lightgbm parallel rounds

Supported workers use native thread limits, bounded dispatch and failure cleanup. These are operational controls, not a security sandbox or production deadline.

**Limit:** Status applies to failure handling in admitted workloads; worker processes are not hostile-code isolation. The 0.1-second timeout polls for completion and does not limit a round duration. Built-in-only restrictions materially narrow supported workflows.

**Executable sources:** [limen/experiment/_parallel_worker.py:101–129](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_worker.py#L101-L129); [limen/experiment/_parallel_worker.py:148–191](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_worker.py#L148-L191); [limen/experiment/_parallel_worker.py:237–245](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_worker.py#L237-L245); [limen/experiment/_parallel_rounds.py:166–246](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_rounds.py#L166-L246); [limen/experiment/_parallel_rounds.py:105–115](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_parallel_rounds.py#L105-L115); [tests/test_parallel_rounds.py:487–532](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_parallel_rounds.py#L487-L532)

**Repeatable criterion protocol:** Exercise successful work, ordinary exceptions, initializer failure, panic, worker death, failed result publication and cancellation at zero/outstanding/final work. Capture caller-visible error, remaining queue entries, worker/orphan count, shutdown time and completed-prefix identity. Check that EOF/disconnection and no-progress reads terminate. If restart is offered, compare resumed output under the same order/seed/state contract; a simulated-time timeout or thread join is not a workload deadline.

## S09

### Inference output validity and unavailable-signal behavior

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Python Sensor versus compiled Sensor handoff to downstream consumers

PythonSensorBase validates finite outputs and probability bounds. Compiled scalar extraction lacks the same central guard; exceptions become unavailable results.

**Limit:** Python callbacks/fitted objects remain ordinary trusted in-process code; declared training/selection cutoffs cannot prove no leakage. Compiled extraction passes numeric values without centralized finite/probability admission. No inference response alone creates a trading kill switch.

**Executable sources:** [limen/inference/_python_sensor.py:65–100](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/inference/_python_sensor.py#L65-L100); [limen/inference/_python_sensor.py:104–133](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/inference/_python_sensor.py#L104-L133); [limen/inference/_python_sensor.py:183–195](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/inference/_python_sensor.py#L183-L195); [limen/inference/sensor.py:124–143](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/inference/sensor.py#L124-L143); [limen/inference/sensor.py:229–247](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/inference/sensor.py#L229-L247); [limen/inference/sensor.py:294–310](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/inference/sensor.py#L294-L310)

**Repeatable criterion protocol:** Identify the native or adapter output contract and follow it to execution. Test warmup, missing/nonfinite features, invalid length/shape, nonfinite scores/quantities, probability bounds when relevant, callback exceptions and rejection status. Verify invalid output is distinguished from a valid flat decision and whether prior intent/protective orders are retained, canceled or rejected. A caller-visible mask counts as a mask unless an execution gate consumes it; fixed non-ML routes do not inherit a probability contract.

## S10

### Execution chronology and source evidence admission

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Event-engine observations/signals/funding and their declared availability timestamps

Event execution validates chronology, positive finite prices, row order, nonoverlap and source bindings. Price-gap guard is optional.

**Limit:** Validation establishes consistency of supplied metadata, not authenticity of external timestamps. Direct snapshot arrays have a different causality contract and permit zero lag. Fingerprints are not signed source attestations.

**Executable sources:** [limen/backtest/execution_events.py:20–51](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/execution_events.py#L20-L51); [limen/backtest/execution_events.py:60–108](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/execution_events.py#L60-L108); [limen/backtest/trade_contract.py:184–186](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_contract.py#L184-L186); [limen/backtest/_event_plan.py:27–67](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/_event_plan.py#L27-L67)

**Repeatable criterion protocol:** Declare observation, availability, decision, submission and executable times. Use identical recorded events to test prehistory queries, duplicates, reordered/overlapping intervals, malformed OHLC, delayed availability, simultaneous events and partition boundaries. Require no fill or historical decision based on unavailable evidence. Test default and cheat/alternate modes separately. Timestamp validation does not authenticate a feed or repair future-dependent user features; array adapters must explicitly align signals, fills and valuation.

## S11

### Economic affordability, exposure and quantity constraints

**Enforced** · Inspected, Reproduced · applicability `native` · capability `implemented`

**Scope:** Event-engine target sizing, cash spot and linear perpetual accounting

Event policies enforce target exposure, affordability and lot rounding in their supported products. Maintenance breach raises; it is not a liquidation simulator.

**Limit:** max_exposure is checked for the requested target, not continuously rebalanced as prices move. Margin/equity breach aborts rather than simulating venue liquidation/bankruptcy. No market-depth participation or venue risk limits are established.

**Executable sources:** [limen/backtest/trade_contract.py:26–47](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_contract.py#L26-L47); [limen/backtest/trade_contract.py:107–126](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_contract.py#L107-L126); [limen/backtest/trade_execution.py:26–51](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_execution.py#L26-L51); [limen/backtest/trade_execution.py:76–82](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_execution.py#L76-L82); [limen/backtest/trade_execution.py:97–158](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_execution.py#L97-L158)

**Repeatable criterion protocol:** Replay the same recorded prices with declared costs, lot steps, minimum notionals, account currency and leverage. Reconcile cash/equity, fees, funding, realized/unrealized PnL and reservations; test post-cost affordability, reversal, pending orders, reduce-only, liquidation and no-mutation on rejected transactions. Identify required risk-model registration and bypass modes. Do not label intentional borrowed cash or an order-book PnL balance as an affordability defect; add a capital adapter where the selected engine omits that policy.

## S12

### Exit rules, gap treatment and execution uncertainty

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Event stop-loss/take-profit/time-stop logic and comparison with snapshot conventions

Stops take precedence on dual-touch bars and adverse gaps affect fills. Snapshot closes terminal holdings; event ledger can mark remaining inventory.

**Limit:** The event engine rejects some insufficient intrabar evidence and uses conservative precedence, but recorded OHLC cannot establish an exact intrabar path. Fill rules use fixed slippage and do not establish order-book queues, partial fill dynamics or guaranteed live stop execution.

**Executable sources:** [limen/backtest/trade_execution.py:97–117](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_execution.py#L97-L117); [limen/backtest/trade_execution.py:191–211](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_execution.py#L191-L211); [limen/backtest/trade_execution.py:325–341](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_execution.py#L325-L341); [limen/backtest/long_flat_strategy.py:118–131](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/long_flat_strategy.py#L118-L131); [limen/backtest/trade_contract.py:198–207](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/backtest/trade_contract.py#L198-L207)

**Repeatable criterion protocol:** Use recorded windows containing adverse gaps, simultaneous barriers, intrabar entry/resize, repeated signals and terminal inventory; use real order-book events for queue tests. Declare stop/limit precedence, trigger versus executable price, slippage, volume, partial-fill, order rejection, latency, randomness and market-impact assumptions. Match these semantics before comparing outcomes. Record uncertainty and counterfactual replay limits; a simulated protective rule is not a guarantee of a live fill.

## S13

### Protected holdout reservation and exposure accounting

**Enforced** · Inspected · applicability `native` · capability `implemented`

**Scope:** Supported local project-bound protected holdout mode

Local holdout ledger uses transactional attempts, admission leases and exposure categories; used reservations cannot simply be withdrawn. Owner secrecy is not enforced.

**Limit:** Protected mode rejects callbacks, resume, parallel, factorization, walk-forward, and event/funding execution. It records local research use, not secrecy from a machine owner, tamper-proof global history, or proof of no earlier external exposure.

**Executable sources:** [limen/experiment/_holdout_history.py:90–137](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_history.py#L90-L137); [limen/experiment/_holdout_history.py:196–250](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_history.py#L196-L250); [limen/experiment/_holdout_attempts.py:88–119](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_attempts.py#L88-L119); [limen/experiment/_holdout_research.py:71–100](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/limen/experiment/_holdout_research.py#L71-L100)

**Repeatable criterion protocol:** Reserve a declared future holdout, attempt overlap/revision changes and concurrent use, attempt withdrawal after exposure, and interrupt before/after evaluation starts. Verify started/completed/failed history, used-reservation retention and explicit refusal of unsupported modes. Separate temporal train/test splits, account reservations and experiment UUIDs from durable holdout governance. A bounded unsuccessful implementation search yields Unknown with the searched paths; it is not proof of repository-wide absence.

## S14

### Executable supply-chain and security CI coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Checked-in CI/release configuration and vulnerability audit implementation

Checked-in CI pins dependencies/actions and configures security scans and attestations. Live CI state, branch protection and all optional dependency risks unverified.

**Limit:** The pip-audit gate reads only project.dependencies and resolves that set; it does not cover all optional research backends or every allowed version. Configured workflows and rulesets do not prove current successful execution or actual server-side enforcement.

**Executable sources:** [.github/workflows/pr_checks_lint.yml:38–61](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/.github/workflows/pr_checks_lint.yml#L38-L61); [.github/workflows/pr_checks_lint.yml:83–103](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/.github/workflows/pr_checks_lint.yml#L83-L103); [.github/workflows/pr_checks_codeql.yml:15–55](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/.github/workflows/pr_checks_codeql.yml#L15-L55); [governance/check_dependency_vulnerabilities.py:38–47](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/governance/check_dependency_vulnerabilities.py#L38-L47); [governance/check_dependency_vulnerabilities.py:74–92](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/governance/check_dependency_vulnerabilities.py#L74-L92); [pyproject.toml:52–66](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/pyproject.toml#L52-L66); [.github/workflows/pr_publish_pypi.yml:142–194](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/.github/workflows/pr_publish_pypi.yml#L142-L194)

**Repeatable criterion protocol:** Inspect exact dependency/tool/action identities, mutable tags, workflow permissions, credential persistence, audit target sets, exception expiry and attestations. Record whether controls are merely configured or actually executed. Separately verify hosted enforcement, resolved advisories and released-byte provenance when permitted. A successful source build, matching version string or auxiliary source tag does not by itself prove wheel/binary identity.

## S15

### Adversarial validation evidence and mutation coverage

**Partial** · Inspected · applicability `native` · capability `implemented`

**Scope:** Property tests, fuzz harness, corruption tests and worker lifecycle tests

Property and mutation/corruption tests cover specific surfaces. Config fuzzing stops at parse/validate, so it does not test compiled execution boundaries.

**Limit:** The fuzz harness does not compile/execute manifests. The declared property families cover permutation counts, parameter cardinality/determinism and splitter partitions. Existing namespace/lineage tests miss demonstrated boundary cases. Execution counts refer to the selected local test campaign; no broad security assurance follows from coverage alone.

**Executable sources:** [fuzz/fuzz_yaml_manifest.py:9–35](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/fuzz/fuzz_yaml_manifest.py#L9-L35); [.github/workflows/fuzz_smoke.yml:30–37](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/.github/workflows/fuzz_smoke.yml#L30-L37); [tests/test_property_contracts.py:29–41](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_property_contracts.py#L29-L41); [tests/test_property_contracts.py:70–169](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_property_contracts.py#L70-L169); [tests/test_yaml.py:191–208](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_yaml.py#L191-L208); [tests/test_yaml_store.py:167–176](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_yaml_store.py#L167-L176); [tests/test_parallel_rounds.py:686–738](https://github.com/Vaquum/Limen/blob/29837e666604eee74a2ac94f328fb9803724342a/tests/test_parallel_rounds.py#L686-L738)

**Repeatable criterion protocol:** Publish a case-by-case expected-outcome matrix and distinguish Inspected, Tested, Reproduced and Measured. Record applicable case counts, skips, run results, environment, script/source/data hashes and limitations. Include relevant resolver, nonfinite resource, archive, invalid inference, stale identity, EOF, worker death, writer race and crash cases. Keep code/branch coverage separate from reachable attack-case and mutation coverage; neither test count nor a failed-build workaround is a global safety score.

