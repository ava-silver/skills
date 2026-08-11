---
name: subagents
description: Right-size subagent delegations by deliberately choosing the model and reasoning effort before using subagent tools or workflow.
allowed-tools: subagent_spawn, subagent_wait, subagent_cancel, subagent_check, subagent_list, workflow
---

# Subagents

Right-size each delegation before creating an agent.

## Right-size the delegation

1. Confirm delegation is worthwhile: the task is independently executable and substantial enough to offset coordination cost.
2. Recommend `openai-codex/gpt-5.6-terra` by default. Recommend `openai-codex/gpt-5.6-sol` instead when the task requires more thorough reasoning, such as ambiguous architecture, broad synthesis, or high-risk work. Override this choice only when another model materially improves the outcome.
3. Right-size reasoning effort:
   - `off`/`minimal`: deterministic or clerical work.
   - `low`: routine, tightly scoped work.
   - `medium`: nontrivial implementation, debugging, or review.
   - `high`: ambiguous, cross-cutting, or high-risk work.
   - `xhigh`/`max`: exceptional problems where added cost is justified.
4. Make the prompt self-contained: include the goal, working directory, relevant context and paths, constraints, expected output, and verification.
5. Use `subagent_spawn` for standalone background work. Use `workflow` for phased dependencies, structured results, or coordinated fan-out. Parallelize only independent tasks.
6. State the chosen model and effort in one line, with a rationale.
7. Validate returned work against the parent task before relying on it.
