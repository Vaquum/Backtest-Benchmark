# Selected test campaign: setup failures and retest evidence

The original targeted run selected **82 modules and 1,771 distinct test cases**. Its unmodified `run_manifest.json` is the exact recorded command and environment-override list. `pytest.log`, `junit.xml` and `test_runtime_profile.json` are the original outputs.

The original run passed 1,768 cases and failed three. No tracked Limen source file was changed to make them pass.

| Test | Observed initial failure | Setup correction |
| --- | --- | --- |
| `tests/test_holdout_research.py::test_holdout_revision_admission` | The nominally ordinary temporary project inherited the enclosing source Git repository, so project binding existed when the test expected none. | Place pytest temporary projects outside every enclosing Git checkout. |
| `tests/test_holdout_assessment.py::test_holdout_frozen_causal_assessment` | `importlib.metadata.PackageNotFoundError` for the `vaquum-limen` distribution. | Install the pinned checkout as an editable package with `--no-deps --no-build-isolation`. |
| `tests/test_factorize_equivalence.py::test_four_cli_experiments_match_precision_baseline_at_12_decimals` | The fixture-generation subprocess failed with `ModuleNotFoundError: No module named 'limen'`. | The same editable install makes the package importable from the script's subprocess path. |

Only these three cases were rerun after the environment corrections. The original `retest_junit.xml` records **3 tests, 0 failures, 0 errors and 0 skipped**, with JUnit elapsed time **12.254 seconds**. `retest_runtime_profile.json` separately records a **13.409666-second** suite span. These timers have different scopes and are not substitutes for each other. Initial JUnit elapsed time was 157.750 seconds; the external initial-run manifest recorded 160.45481643699895 seconds.

There are **1,771 distinct selected tests with passing executions across the two runs**, and **1,774 executions** in total. A fresh passing execution of all 1,771 cases after correction was not performed. Neither the full repository suite nor live CI was run.

## What was captured and what was reconstructed

- The original initial command is available verbatim in `run_manifest.json`; it does **not** include `--basetemp`.
- `original_scripts/amended_run_review_tests.py` preserves the review runner as it stood after adding external `--basetemp`. It is historical working material with original absolute paths, not the exact initial command transcript. The command manifest resolves this difference.
- The original editable-install shell transcript and the exact three-case retest shell command were not retained. No synthetic transcript or retest stdout log has been created.
- The three retest case identities, their results, the external temporary-directory location and the reported setup correction are established by the original artifacts and the executing reviewer's record. The preserved initial and combined coverage JSON files show the coverage recorded for the selected work.
- The kit's setup recipe and portable runners are **reproduction instructions**, not additional completed measurements. `scripts/run_selected_tests.py --selection retest3` repeats only the same three cases with a fresh independent coverage database. It does not pretend to reproduce the precise historical shell invocation or append to the archived coverage state.

The combined selected coverage report contains **16,301 covered statements out of 23,882 (68.2564274348882%)**. This is selected-campaign coverage, not a measure of the full suite or a claim that Limen's hosted full-suite coverage gate passed or failed.
