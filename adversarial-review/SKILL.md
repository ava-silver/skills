---
name: adversarial-review
disable-model-invocation: true
description: 'Run two independent adversarial reviews of the current diff, adjudicate every finding, fix accepted issues, and report the outcome.'
---

# Adversarial Review

Stress-test the current change with two independent reviewers, then own the verdict and fixes.

## Workflow

1. Define the review scope from the user's arguments. Otherwise use working-tree changes versus `HEAD`, including staged, unstaged, and untracked files. If the scope is empty, report that and stop.
2. Spawn exactly two subagents in parallel. Give both the scope, repository path, and these shared rules:
   - Inspect the diff plus relevant surrounding code and tests.
   - Make no edits. Use only read-only git commands.
   - Report actionable findings with severity, file/line, evidence, impact, and a concrete fix.
   - Exclude style preferences, speculative concerns without a plausible failure path, and duplicates within the report.
3. Give the reviewers different adversarial lenses:
   - **Correctness breaker:** hunt for logic errors, regressions, crashes, security problems, data loss, races, resource leaks, and broken error handling.
   - **Assumption breaker:** challenge edge cases, API and integration contracts, compatibility, state transitions, operational behavior, and test gaps that can hide real defects.
4. Wait for both reports. Verify every finding yourself against the code; do not accept a claim merely because a reviewer made it. Merge duplicates only after verification.
5. Fix every finding you agree with, using the smallest coherent change. Run focused tests or checks for each fix, then broader relevant checks when practical.
6. For every rejected finding, record the concrete reason it does not apply. Treat uncertain findings as unresolved and investigate until you can accept or reject them.
7. Report concise results under:
   - **Fixed:** severity, issue, changed files, and verification.
   - **Disagreed:** severity, claim, and reason.
   - **Remaining risk:** only checks you could not run or issues blocked from resolution.

## Guardrail

Git access is read-only. Never stage, commit, amend, switch branches, reset, rebase, or push during this workflow.
