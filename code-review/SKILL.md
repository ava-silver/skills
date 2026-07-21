---
name: code-review
description: 'Review a diff for correctness, spec alignment, repository standards, and maintainability.'
---

# Code Review

Review the change directly along two separate axes.

## Scope

1. Use the fixed point or diff scope the user supplies. If absent, ask for it.
2. For a git ref, verify it resolves and review `git diff <ref>...HEAD` plus `git log <ref>..HEAD --oneline`. Stop on an invalid ref or empty diff.
3. For working-tree scope, include staged, unstaged, and untracked changes.

## Sources

Before reviewing, inspect relevant surrounding code and tests, then find:

- **Spec:** user-provided material, issue references in commits, or matching files under `docs/`, `specs/`, and `.scratch/`. If none exists, state that the Spec axis is limited to inferred behavior.
- **Standards:** applicable `AGENTS.md`, `CONTRIBUTING.md`, coding standards, and local conventions visible in adjacent code. Repo guidance overrides generic heuristics; skip checks already enforced by tooling.

## Review

Inspect every changed hunk and report actionable findings with severity, file/line, evidence, impact, and a concrete fix.

### Standards

Cite documented violations. Also inspect for confusing names, duplication, long or tangled functions, feature envy, data clumps, primitive obsession, repeated conditionals, shotgun surgery, divergent responsibilities, speculative generality, message chains, middle men, awkward inheritance, needless indirection, weak boundaries, and tests that obscure behavior.

Label heuristic findings as maintainability judgements, not hard violations. Flag them when they create concrete readability, change-risk, or testability costs; do not dismiss poor code merely because it currently works. Exclude personal taste.

### Spec and Correctness

Find missing or partial requirements, scope creep, incorrect implementations, logic errors, regressions, crashes, security problems, data loss, races, leaks, broken error handling, contract or compatibility breaks, and tests that miss plausible failures. Quote the relevant requirement when available. Do not report speculation without an evidence-backed failure path.

## Output

Report `## Standards` and `## Spec and Correctness` separately. If an axis has no findings, say so. End with finding counts and the highest-severity issue in each axis; do not collapse them into one ranking.
