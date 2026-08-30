---
name: stress-test-loop
disable-model-invocation: true
description: 'Run a persistent stress-testing conversation in which a subagent exercises a target and challenges each fix until both agents agree no actionable issues remain.'
---

# Stress-test loop

Pair the parent agent with one persistent stress-testing partner. The parent edits the target; the partner independently exercises it and critiques each change.

## Workflow

1. Define the target, workspace, exercise method, relevant constraints, and success criteria from the request and repository.
2. Read `../subagents/SKILL.md`, then spawn one subagent in the environment where it can exercise the target. Keep this subagent alive for the full loop.
3. Ask the partner to stress-test every plausible edge case it can derive. It must not edit source or spawn subagents.
4. When the partner sends feedback through `ask_parent`, verify each claim. Fix supported issues before replying through `subagent_answer`; explain rejected findings with concrete evidence. If the partner cannot load the change, describe the exact change for it to critique.
5. After each reply, have the partner reassess independently, continue testing, and send another feedback round. Treat disagreement as a conversation: exchange evidence, assumptions, and alternatives until both agents reach a shared conclusion. Neither agent concedes based on role, confidence, or repetition.
6. Ask the user only when resolution requires unavailable product intent or an irreducible tradeoff. Relay the decision and continue the loop.
7. Finish when the partner finds no actionable issues. Report the changes and any risks it could not test.

## Subagent prompt

```text
Act as a persistent stress-testing partner for [target] in [workspace].

Exercise the target using [methods], inspect its relevant source and tests, and explore every plausible edge case you can derive. Do not edit source or spawn subagents. When you find actionable issues, send one concise feedback round with concrete evidence through ask_parent, then wait.

After each answer, reassess the change or proposal independently and continue testing. If you cannot load a change, critique its exact description instead. Discuss disagreements with evidence, assumptions, and alternatives until we reach a shared conclusion. Do not concede based on role, confidence, or repetition.

Finish only when you find no remaining actionable issues. Report any risks you could not test.
```
