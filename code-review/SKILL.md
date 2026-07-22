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
- **Standards:** infer norms from surrounding code, tests, and recurring repository patterns. Use dedicated coding-standard documents when clearly applicable. Explicit repo guidance overrides inferred conventions and heuristics; skip checks already enforced by tooling.

## Review

Inspect every changed hunk and report actionable findings with severity, file/line, evidence, impact, and a concrete fix.

### Standards
Cite documented rules when present; otherwise show the recurring surrounding-code pattern. Apply these smell heuristics:

- **Mysterious Name:** a name hides what a value or operation means. Rename it; if no honest name fits, clarify the design.
- **Duplicated Code:** the same logic shape appears in multiple places. Extract the shared shape and call it from each site.
- **Feature Envy:** code reaches into another object's data more than its own. Move the behavior closer to the data.
- **Data Clumps:** the same fields or parameters repeatedly travel together. Bundle them into a type.
- **Primitive Obsession:** a primitive stands in for a domain concept. Introduce a small domain type.
- **Repeated Conditionals:** the same switch or if-cascade recurs. Centralize it with polymorphism or a shared map.
- **Shotgun Surgery:** one logical change requires scattered edits. Gather the changing behavior into one module.
- **Divergent Change:** one module changes for unrelated reasons. Split it by responsibility.
- **Speculative Generality:** abstractions or hooks serve no current requirement. Remove or inline them until needed.
- **Message Chains:** callers navigate deep object graphs. Hide the traversal behind a method on the owning object.
- **Middle Man:** code mostly delegates without adding meaning. Remove it and call the real target directly.
- **Refused Bequest:** a subtype ignores most inherited behavior. Replace inheritance with composition.

Also flag tangled functions, weak boundaries, and opaque tests when extracting steps, moving responsibility, or rewriting tests around observable behavior would reduce concrete change risk.
Label heuristic findings as maintainability judgements, not hard violations. Exclude personal taste and require a concrete readability, change-risk, or testability cost.

### Spec and Correctness

Find missing or partial requirements, scope creep, incorrect implementations, logic errors, regressions, crashes, security problems, data loss, races, leaks, broken error handling, contract or compatibility breaks, and tests that miss plausible failures. Quote the relevant requirement when available. Do not report speculation without an evidence-backed failure path.

## Output

Report `## Standards` and `## Spec and Correctness` separately. If an axis has no findings, say so. End with finding counts and the highest-severity issue in each axis; do not collapse them into one ranking.
