---
name: adversarial-review
disable-model-invocation: true
description: 'Run two independent reviews of the current diff, adjudicate findings, fix accepted issues, and report the outcome.'
---

# Adversarial Review

Stress-test the current change with two independent applications of the repository's code-review skill, then own the verdict and fixes.

## Workflow

1. Define the scope from the user's arguments. Otherwise review staged, unstaged, and untracked changes versus `HEAD`. Stop if the scope is empty.
2. Read `../code-review/SKILL.md`. Collect the diff, commit list, applicable standards, and available spec sources its process requires.
3. Spawn exactly two subagents in parallel. Give both the repository path, scope, diff command, commit list, standards sources, and spec source. Require each to:
   - Read and apply `code-review/SKILL.md` to the full scope.
   - Inspect every changed hunk plus relevant surrounding code and tests.
   - Make no edits and use only read-only git commands.
   - Spawn no subagents.
4. Add one emphasis to each review without narrowing the shared code-review rubric:
   - **Failure lens:** aggressively test logic, error paths, state transitions, security, compatibility, and operational behavior.
   - **Design lens:** aggressively test clarity, cohesion, duplication, boundaries, change risk, and whether tests expose behavior.
5. Verify every finding yourself against the code, standards, and requirements. Merge duplicates only after verification. Investigate uncertainty until resolved or list it as remaining risk.
6. Before editing, separate findings whose fixes belong to the current work from worthwhile changes outside its scope. Flag out-of-scope fixes as potential scope creep and get explicit user approval before implementing them. Do not treat reviewer agreement as approval.
7. Fix each approved finding with the smallest coherent change. Run focused checks for each fix, then broader relevant checks when practical.
8. Report only:
   - **Fixed:** severity, issue, changed files, and verification.
   - **Disagreed:** severity, claim, and concrete rejection reason.
   - **Remaining risk:** unresolved issues or checks not run.
   - **Summary:** finding count by reviewer lens and the worst issue in each.

## Guardrail

Git access is read-only. Never stage, commit, amend, switch branches, reset, rebase, or push during this workflow.
