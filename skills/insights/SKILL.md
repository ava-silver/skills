---
name: insights
description: 'Retrospective: mine pi session logs for pain points and improvement signals. Triggers: "run insights", "analyze sessions", "what has been frustrating", "session retrospective".'
disable-model-invocation: true
---

# Insights

Excavate pi session logs for friction and pain points, cross-referenced against the current setup, to surface what's worth improving.

**State file:** `~/skills/skills/insights/reviewed.json` -- a JSON array of session IDs already analyzed. Never re-read those sessions. Create the file if it doesn't exist.

## Setup context

Load before analyzing:
- **Skills:** `~/skills/skills/` -- what's already been addressed
- **Dotfiles/pi:** `~/dotfiles/pi/` (extensions, settings, prompts, keybindings) -- what's been configured
- **AGENTS.md:** `~/.pi/agent/AGENTS.md` -- standing agent instructions

## Session log format

Sessions live at `~/.pi/agent/sessions/<cwd-slug>/*.jsonl` (one `.jsonl` per session). Extract the session ID from the filename (UUID after the timestamp).

Each line is a JSON record. Relevant types:
- `session` -- `cwd`, `timestamp`
- `message` -- `message.role` (`"user"` or `"assistant"`), `message.content[].text`
- `model_change` -- which model was active
- `custom_message` where `customType == "subagent-result"` -- subagent outcomes (check `details.status`)

## Extraction script

Run `python3 ~/skills/skills/insights/extract_sessions.py` to get a JSON array of unreviewed sessions. Read that file for the full implementation.

## Mining signals

Fan sessions out to parallel subagents (via `workflow`). For each session, ask the subagent to identify:

- **Corrections/retries:** user saying "no", "wait", "actually", "that's wrong", "try again"
- **Explicit frustration:** complaints about verbosity, missed context, wrong tool, slow/expensive responses
- **Tool/subagent failures:** errors in `custom_message` records
- **Abandoned tasks:** long sessions that end without resolution
- **Model switches:** `model_change` events mid-session (often frustration-driven)
- **Workarounds:** user doing something manually that an existing skill should handle

Schema for each subagent:
```json
{ "pain_points": [{ "quote": "...", "category": "...", "severity": 1-3 }], "already_addressed_by": "..." }
```

## Synthesis

After fan-out, synthesize across all sessions:
1. Rank by frequency × severity
2. Note which pain points are already covered by an existing skill or dotfiles config (deprioritize)
3. For each top pain point, suggest a concrete fix: new skill, AGENTS.md change, dotfiles tweak, or extension

## After analysis

Update the state file with all newly reviewed session IDs (append the new IDs to `~/skills/skills/insights/reviewed.json`).
