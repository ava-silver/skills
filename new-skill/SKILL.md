---
name: new-skill
description: Create a new Agent skill. Only use when directly invoked.
allowed-tools: Read, Write, Edit, Bash
---

# New Skill

Creates a new Agent skill, checked into the skills repo and installed via `bunx skills`.

Skills live at `~/skills/<skill-name>/SKILL.md`. Never write directly to `~/.claude/skills/` or `~/.agent/skills/`.

## Workflow

**Step 1: Gather requirements** -- ask the user what the skill does, what to call it (kebab-case), what trigger phrases invoke it, and what tools it needs.

**Step 2: Write the skill file**

> **YAML gotcha:** If the description contains `: ` (colon-space), wrap it in single quotes — otherwise the YAML parser treats it as a mapping key and the skill is silently skipped by `bunx skills add`. Trigger phrase lists like `Triggers: "foo", "bar"` are the common culprit.

```markdown
---
name: <skill-name>
description: '<One-line description + trigger phrases so Claude knows when to invoke it.>'
allowed-tools: <only what the skill actually needs>
---

# <Title>

<What it does, in 1-2 sentences.>

## Key Rules / Workflow

<Concrete steps or constraints. Cut anything derivable from reading the code.>
```

**Step 3: Reinstall**

```bash
bunx skills add ~/skills -g -y -a universal claude-code
```

Tell the user the skill is ready and can be invoked with `/<skill-name>`.
