---
name: pr-description
description: Update a PR description based on what's actually in the diff. Use when user says 'update PR description', 'write PR description', 'fill in PR description', 'pr description', or after creating a new PR. Writes the description as if from scratch -- not influenced by chat history or brainstorming.
allowed-tools: Bash, Read, Glob
---

# PR Description

## Key Rules

1. **Write from scratch** — ignore the conversation history. Describe what's in the diff, not what was debated. Follow the `write` skill for prose style.
2. **Be brief** — the diff is the source of truth. Don't restate it. Explanatory sections (e.g. "How") get a one-to-two sentence overview, not a play-by-play. Summary is a short bulleted list. Cut anything a reader could get from reading the changes.
3. **Testing sections = manual only** — CI covers build, lint, and unit tests. Only include steps that validate behavior beyond CI.
4. **Write to a temp file** — write the body to a temp file and pass it via `gh pr edit --body-file`. This is less error-prone than a heredoc (no backtick/quote escaping issues).
5. **No Boilerplate** — avoid mentioning the context of the graphite stack, or any other obvious boilerplate text. The user can already deduce that from the graphite comment or other context already provided.

## Workflow

1. Fetch diff and current state:
```bash
gh pr view --json title,body,files
git diff $(git main)...HEAD
```

2. Check for a PR template:
```bash
cat .github/PULL_REQUEST_TEMPLATE.md 2>/dev/null || cat .github/pull_request_template.md 2>/dev/null
```
Fill every section. If no template, use Summary + Test Plan.

3. Write the description by writing the body to a temp file (e.g. with the Write tool), then:
```bash
gh pr edit --body-file /tmp/pr-body.md
```

## Diagrams

If the changes involve a non-obvious flow (e.g. a new state machine, multi-service interaction, or complex branching logic), add a Mermaid diagram using the `diagram` skill. GitHub renders Mermaid natively in PR descriptions -- output as an inline fenced block, no file needed. Only add a diagram when it meaningfully aids understanding; don't add one just to have one.

## QA links (UI PRs only)

```bash
HASH=$(yarn hash --hash-only)
```

- **Serverless-only**: `https://ddserverless-${HASH}.datadoghq.com/<inferred-path>`
- **Cross-team** (touches shared/non-serverless code): both `ddserverless-${HASH}` and `app-${HASH}` URLs
- Ambiguous? Ask.

Infer path from changed file paths. Feature flags: `?config_flag-name=value` URL params.
