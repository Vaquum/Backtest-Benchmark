# Comparison protocol

## Evidence rule

Only executable implementation, executable configuration, tests, and observations obtained from running admitted code establish a behavioral claim. READMEs, websites, product documentation, paper claims, comments, and a test's name are not behavioral evidence. A source comment may help locate a path; the executable statements must support the finding. A test that has merely been read is **Inspected**, not **Tested**. Repository metadata establishes identity; license files establish the observed licensing label, not engine behavior.

Every assessment belongs to a specific commit, entry point, configuration and threat model. A native feature, an optional feature, user strategy code, an external research adapter, and a hosted service are separate scopes. A public engine's findings do not transfer to the vendor's service or another release. Limen is subject to the same rule.

The original Limen baseline is preserved under `baseline/limen/`. Its measurements are historical observations under its own contracts, environment and sample counts. The new common-contract campaign is independently recorded under `results/`; its timings are not mixed with historical samples.

## The three assessment axes

`criteria.json` defines 12 computation, 15 academic and 15 safety criteria. Each solution receives all 42 rows, including explicit inapplicability and unknowns. Each cell records applicability, capability, status, evidence type, scope, finding, limitation and pinned source references. The exhaustive *grid structure* does not claim exhaustive source-path inspection.

| Status | Meaning within the stated scope |
|---|---|
| Enforced | The inspected path enforces the stated property under its listed assumptions. This is not formal verification or a whole-product guarantee. |
| Optional | The implementation provides the mechanism, but a user must select/configure the relevant path. |
| Partial | The mechanism or observation has material scope gaps or boundary differences. |
| Fails | A specific stated property is contradicted in the stated path. Evidence distinguishes a reproduction from a source-derived counterexample. |
| Unknown | This campaign has insufficient admitted evidence to decide or quantify the criterion. |
| N/A | The selected native layer does not perform that operation; compare at another declared layer or add an adapter. |

Evidence types are **Inspected**, **Tested**, **Reproduced**, and **Measured**. They are complementary labels, not numerical scores. A nonfinite result, an unsupported contract, a missing environment and an unmeasured value are distinct states. None becomes a zero.

There is no aggregate winner or star rating. Do not average latency with safety, count optional features as enforced controls, penalize an execution library for omitting an ML trainer, or let speed compensate for a violated required property. Choose the scientific/operational contract first, apply its mandatory gates, and compare the eligible solutions on their remaining measured tradeoffs.

## Admission and identity

1. Admit inspectable engine implementation with its actual license terms. Public source is not automatically an unrestricted open-source license. Closed or unspecified engine implementations stay in `catalog/exclusions.json`, with a re-entry condition and no inferred quality verdict.
2. Freeze repository URL and full commit. `fetch_sources.py` refuses divergent or tracked-modified existing checkouts. The Limen baseline is deliberately retained at its original reviewed revision; other candidates use the captured revisions in the catalog.
3. Freeze the data bytes, source event timestamps, availability convention, dataset scope and limitations. This campaign uses one recorded upstream fixture, with SHA-256 verification. It does not establish that the fixture independently authenticates an exchange feed or represents other assets/regimes.
4. Build separate source environments using committed dependency hash locks. Verify imported distribution/source provenance, tracked-source cleanliness, dependency versions and installed distribution RECORD hashes. Record Python/native toolchain identity and source build attempts. Binary-identical native builds across machines are not promised.
5. Admit a benchmark adapter only when its native execution and observed common result match the independent oracle. Unsupported semantics stay visible with a reason. A native component driver cannot enter the full-engine ranking.
6. Freeze the benchmark code hashes before the campaign. Retain the order, raw successful and failed attempts, environment identity, configuration, outputs' digests and parity results. Publish a new campaign when any admitted code, data, contract or adapter changes.

The native Linux x86-64 toolchain lock includes official artifact URLs and SHA-256/SHA-512 hashes. LEAN NuGet locks and the separately captured hftbacktest Cargo lock are included; Nautilus supplies its own pinned Cargo lock. The first HFT attempt with `--locked` failed because upstream did not commit a workspace lock; the subsequent captured resolution and test result remain separate evidence. Build duration is never substituted for backtest latency.

## Common recorded-bar contract

The reference workload has one long/flat instrument, initial cash 1,000,000 currency units, continuous units, no leverage, no ongoing target-weight rebalancing, and no invented market data. The actual recorded fixture has 8,784 hourly bars. The full campaign evaluates the first 8,783 and uses the final unchanged real bar only to settle engines with delayed bookkeeping. Data originally timestamped at bar open is explicitly released at its bar close by adding the declared 3,600-second interval. Original timestamps are retained in prepared metadata.

Decisions use a prefix ending at close `t`; their earliest permitted fill is close `t+1`. Flat, buy-and-hold and 50/200 SMA crossover signals are fixed before a run. The campaign ranks buy-and-hold and SMA; the all-flat case is an untimed control. The shared signal computation is outside every native engine interval, so these are execution measurements, not native indicator benchmarks.

The final exit is predeclared at the penultimate real close, before the settlement row. It is the same policy for every engine and is not a performance-selected exit. The benchmark does not change input opens/highs/lows/closes to force a fill policy. Native small-unit representation conversion in FractionalBacktest is disclosed explicitly, with its resulting observed quantities and prices checked.

For fee rate `f` and slippage rate `s` (both basis points divided by 10,000), entry fill price is `close * (1+s)` and exit fill price is `close * (1-s)`. The reference all-affordable quantity on entry is `cash / (entry_price * (1+f))`. Fees are actual fill notional times `f`; marked equity after the fill is `cash + units * raw_close`. Inventory held over the interval ending at a close is recorded separately from the post-fill state. Inputs, fees and slippage must be finite and admitted by `Contract`.

No market impact, queue priority, partial fills, exchange outages, funding, borrow, dividends, corporate actions, exchange calendars, lot sizes or price limits are implicit in this contract. They require separate declared workloads. In particular, hourly OHLCV does not determine a limit order book. hftbacktest remains in the specialist grid without fabricated depth or a false OHLC timing.

### Equality gate

`bench/contract.py` contains an explicit cash-and-quantity oracle with no engine imports. Before ranking, the runner checks:

| Field | Gate |
|---|---|
| All evaluation timestamps | Exact equality |
| Every interval holding state | Exact equality |
| Every fill bar and side | Exact equality |
| Every fill price | `rtol=1e-12`, `atol=1e-8` |
| Every marked equity observation | `rtol=1e-10`, `atol=1e-6` |
| Native cash, units, fill quantities and fees, when exposed | Checked against the reference at declared tolerances; missing fields disclosed |

An adapter cannot fill a missing native ledger field with the oracle and call it an observed engine output. Limen's snapshot path exposes a return/holding trace rather than an order cash/quantity ledger; its fill trace is reconstructed from native exposure transitions and recorded prices. This narrower observability is explicit. Equality here establishes the common observed trace, not equivalence of all internal ledger invariants.

The native common **zero-cost** snapshot contract is admitted for five full engines: Limen, Backtrader, vectorbt's public-source Numba path, backtesting.py and bt. QSTrader's SimulatedBroker/Portfolio and Qlib's Exchange/Position are component adapters because the harness supplies their hourly driver. A separate 5-bps fee plus 5-bps slippage preflight exercises compatible vectorbt and Qlib paths; no missing Limen costed comparison is invented. A rejected adapter cost convention does not mean its engine has no cost modeling.

## Timing, memory and uncertainty

The canonical corrective campaign is preregistered before timing: 8,783 evaluation rows; two fixed strategies; seven adapters; five independent process blocks; one first call and nine subsequent warm calls per process; named native compute-pool limits of one; separate untimed preflight; an empty per-worker Numba cache. Loaded BLAS and Polars pools are observed before execution and after every full/core call, outside its timed region. Missing required observations or a loaded pool exceeding one reject admission. The declared environment and `loaded-pools-v1` observations are retained; this does not mean that the process has only one operating-system thread or that every possible third-party background runtime is observable.

The first campaign omitted `POLARS_MAX_THREADS` and did not observe Polars. A bounded post-campaign diagnostic using its same eight configured controls returned nine Polars threads; original worker pool counts remain unobserved. Its complete records and exact runner are preserved under `results/campaigns/2026-10-19-common-zero-original/`, with a superseded-control disposition. It does not feed the canonical timing tables. The corrective run has a new identity and code freeze; raw original outcomes are not edited into corrected results.

Every timed result is checked after the timed interval. A fresh native run object/state is created for each timed call. Garbage collection before a call is outside timing; collections that happen during the call remain included. An empty JIT cache does not imply a cold operating-system file cache.

Engine order rotates between process blocks, reverses between the two strategies, and strategy order alternates. This balances average engine position jointly across both strategies; five blocks do not cover all seven positions within either individual strategy. No discarded outliers or post-result selection is allowed.

Report separate measurements for dependency/engine import and preparation; first native call; warm native calls; native-output extraction; full-common result; and parent-observed launch through first validated output. The last includes identity checks, data loading, oracle and validation work; it is not pure engine initialization. Full-common call latency includes native execution and common-output extraction, including lazy accessors. Optional internal core timing is diagnostic and has no full-engine ratio. Limen's direct core diagnostics run after all full snapshot calls; their phase named `first` is the first direct invocation and is not process-cold.

For each process, take the median of its nine warm calls. The reported warm figure is the median of the five process medians. Retain all five medians, their minimum/maximum, every raw call and first-call measurements. Repeated calls within one process are not independent experiments. This small single-host campaign does not justify a precise confidence interval, p95 tail guarantee or population-wide performance claim. The report deliberately publishes spread and raw observations instead.

Where eligible, the relative-duration ratio is `candidate warm median / Limen warm median` under the exact same strategy and contract. Lower means less elapsed time for that admitted public API workload. No ratio is emitted for native components, unsupported contracts, incomplete measurements or mismatched inputs. An approximate bars/second figure divides the number of evaluated recorded bars by that same elapsed time; it is not maximum sustainable trading throughput.

Each native API also performs different extra work. Limen's snapshot validates/computes its metrics; backtesting.py and bt compute native statistics; vectorbt exposes lazy arrays and selected accessors are materialized; Backtrader has selected optional observers disabled. The comparison therefore answers public-API workload latency with declared output parity, not equal-instruction microkernel efficiency. The full scope/settings travel with each row.

Process high-water RSS includes imported dependencies, compilation and prior calls in that process. It is not allocation count, incremental engine memory, process-tree PSS, or a measured hard memory bound. Physical CPU identity/effective quotas that could not be observed remain unknown. All ranked calls run sequentially after local builds and probes have ended; host contention outside this task is not controlled.

The campaign does not quantify parameter-grid scaling, native indicator kernels, multi-asset/depth scaling, complete trained research throughput, parallel speedup, cache eviction or crash-recovery latency. Their cells contain scoped source evidence and explicit unmeasured states. Protocol definitions specify what a later campaign must execute before adding numbers.

## Academic and safety probes

Academic comparison checks actual information availability, fit support, labels/censoring, temporal folds, preprocessing, calibration, metric formulas, numerical checks, fit warnings, family selection history, multiple-testing/dependence control, cross-run population identity, final holdout exposure, baseline relevance and sensitivity. Native research workflows and execution-only libraries receive different applicability labels, with ownership of missing research stages assigned to the adapter. PSR, DSR, bootstrap significance and PBO are distinct calculations and are not interchangeable assurances.

Safety comparison declares trusted local research, untrusted configuration/artifact ingestion, economic account restrictions, and operational recovery separately. Arbitrary Python strategy execution is a trusted-code boundary unless an actual isolation mechanism is shown; code configuration is not automatically a sandbox. Optional constraints are not promoted to defaults. A failure reproduced in a helper does not prove network reachability or product-wide compromise.

Bounded probes are local, temporary and harmless. The resolver test checks callable identity without invoking an operating-system command. The ZIP test writes a marker only inside a fresh temporary parent and cleans it. Known unbounded input loops are described from code rather than executed without containment. Prior result files are retained when scripts acquire stricter admission checks; both script hashes are recorded.

## Adding a solution or a new workload

Add a fixed revision and license observations to `catalog/candidates.json`, its source/dependency build recipe, and all 42 assessment rows. Start with explicit Unknown/N/A where justified; do not copy conclusions from a product description. Add exact pinned executable-source references and scope every positive/negative claim. Use `catalog/exclusions.json` when engine implementation is unavailable.

Implement `create_adapter(data, contract)` using `bench/api.py`. Return actual native observables, declare every transformation/assumption, name native extra work, and raise `UnsupportedContract` when semantics cannot be represented honestly. Set `rank_against_full_engine=False` for a component driver. Add meaningful adapter/parity controls and run untimed verification against recorded data before timing.

For a new workload, version the contract and independent oracle first. Freeze the information set, sample IDs, capital/risk/cost assumptions, timing endpoints and retained outputs. Establish equivalence before numbers, keep all unsuccessful attempts, and rerender the grid with the new campaign linked to the affected cells. The older campaign remains immutable evidence.
