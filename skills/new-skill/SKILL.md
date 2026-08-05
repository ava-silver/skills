---
name: new-skill
disable-model-invocation: true
description: Create a new Agent skill. Only use when directly invoked.
---

# New Skill

Creates a new Agent skill in the skills repo.

Skills live at `~/skills/skills/<skill-name>/SKILL.md`. Write only the skill file; installation, commits, branches, and PRs require an explicit user request.

A skill exists for **predictability**: the agent takes the same *process* every run. Every choice below serves that.

## Workflow

**Step 1: Gather requirements** -- ask the user what the skill does, what to call it (kebab-case), and what tools it needs. Settle two things:

- **Invocation.** Model-invoked keeps a `description`, so the agent fires it autonomously and other skills can reach it -- but it sits in context every turn. User-invoked (`disable-model-invocation: true`) costs zero context but only the human can trigger it by name. Pick model-invocation only when the agent must reach the skill on its own.
- **Leading word.** Find the compact concept the agent already holds from pretraining that the skill turns on (e.g. *tight*, *tracer bullets*). Repeat it as a token throughout the body, and word the description with it -- it anchors both invocation and execution in the fewest tokens.

**Step 2: Write the skill file**

> **YAML gotcha:** If the description contains `: ` (colon-space), wrap it in single quotes -- otherwise the YAML parser treats it as a mapping key and the skill is silently skipped. Trigger phrase lists like `Triggers: "foo", "bar"` are the common culprit.

```markdown
---
name: <skill-name>
description: '<One-line description + trigger phrases so the agent knows when to invoke it.>'
---

# <Title>

<What it does, in 1-2 sentences.>

## Key Rules / Workflow

<Concrete steps or constraints. End each step on a checkable completion criterion. Cut anything derivable from reading the code.>
```

Before finishing, prune against these failure modes:

- **No-op** -- a line the model already obeys by default. Test each: does it change behavior versus the default? If not, delete it. A weak leading word (*be thorough*) is a no-op; the fix is a stronger word (*relentless*), not more words.
- **Negation** -- steering by prohibition backfires (*don't write verbose comments* makes verbosity available). Prompt the positive target instead (*write one-line comments*); keep a ban only as a hard guardrail, paired with what to do.
- **Duplication** -- the same meaning in two places. Keep one source of truth.
- **Sprawl** -- push on-demand reference into a linked file (progressive disclosure) so `SKILL.md` stays legible.
