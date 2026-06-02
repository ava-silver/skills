# <Project Name> — Scoping

> Template for `SCOPE.md`. Keep sections that apply; drop ones that don't. Link back
> to concepts in `CONTEXT.md` and to RFC sections so vocabulary stays consistent.


## Prior Reading
Links: RFC/design doc, Figma, related PRs, prior examples, relevant docs. Keep this minimal to what is actually needed for understanding the scope.

## Goal

One or two sentences: what this project delivers and why.

## Background

Context a reader needs to evaluate the scope — prior work, existing systems/frameworks
being built on, and any in-flight efforts that do or don't block this. Link sources.

## In Scope

The work being planned into tickets. If it helps, group into **milestones** (only when
grouping clarifies — not every project needs them). Within each, list concrete tasks
and reference the code/areas they touch.

### Milestone 1: <name>
**Scope:** one line on what this milestone covers.
**Tasks:**
1. ...
2. ...
*Depends on: <other milestone, or none>.*

### Milestone 2: <name>
...

## Out of Scope

Work explicitly **not** being planned here, and why (deferred, owned by another team,
deprecated, etc.). Being explicit here prevents scope creep during planning.

## Hard Dependencies

Blocking prerequisites — work that must land before (parts of) this can proceed.
Note whether each is internal to this plan or external (another team/system), and
its status if known.

## Observability / Success Metrics

How we'll know the rollout works and whether it succeeded:
- **Telemetry:** metrics, logs, traces, dashboards to add or rely on.
- **Success metrics:** the numbers that define success (adoption, error rate, latency,
  conversion, etc.) and where they're measured.

## Maintenance

Operational burden after rollout:
- **Ownership:** who owns this going forward. Include **code ownership / CODEOWNERS**
  only if there are cross-team ownership considerations.
- **Operational:** alerting, runbooks, on-call impact, recurring upkeep.

## Rollout (optional)

Keep minimal or omit if not relevant: feature-flag strategy, staged rollout / cohorts,
rollback plan.

## Open Questions

Unresolved decisions, each with current leaning or who needs to decide. Resolve or
explicitly defer these before planning tickets.
