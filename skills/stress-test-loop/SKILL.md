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
4. Treat each `ask_parent` call as a blocking feedback checkpoint. Verify every claim, fix supported issues, then call `subagent_message` with the resolution. The message answers the pending call so the same partner can continue. Explain rejected findings with concrete evidence.
5. Use `subagent_message` proactively when the partner needs new context, a correction, or an exact change it cannot load. With no pending question, the message steers its current run or continues its settled session.
6. After each message, ask the partner to reassess independently and continue testing. Exchange evidence, assumptions, and alternatives until both agents reach a shared conclusion. Neither agent concedes based on role, confidence, or repetition.
7. Ask the user only when resolution requires unavailable product intent or an irreducible tradeoff. Relay the decision through `subagent_message`, then continue the loop.
8. Finish when the partner finds no actionable issues. Report the changes and any risks it could not test.

## Subagent prompt

```text
Act as a persistent stress-testing partner for [target] in [workspace].

Exercise the target using [methods], inspect its relevant source and tests, and explore every plausible edge case you can derive. Do not edit source or spawn subagents. When you find actionable issues, call ask_parent with one concise feedback round, concrete evidence, and a request for the parent's resolution. Wait for the answer.

After each parent message, reassess the change or proposal independently and continue testing. Treat unsolicited parent messages as new context or steering. If you cannot load a change, critique its exact description instead. Discuss disagreements with evidence, assumptions, and alternatives until we reach a shared conclusion. Do not concede based on role, confidence, or repetition.

Finish only when you find no remaining actionable issues. Report any risks you could not test.
```
