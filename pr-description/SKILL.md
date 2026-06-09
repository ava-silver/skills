---
name: pr-description
description: Update a PR description based on what's actually in the diff. Use when user says 'update PR description', 'write PR description', 'fill in PR description', 'pr description', or after creating a new PR. Writes the description as if from scratch -- not influenced by chat history or brainstorming.
allowed-tools: Bash, Read, Glob
---

# PR Description

## Key Rules

1. **Write from scratch** — ignore the conversation history. Describe what's in the diff, not what was debated.
2. **Testing sections = manual only** — CI covers build, lint, and unit tests. Only include steps that validate behavior beyond CI.
3. **Single-quoted heredoc** — use `<<'EOF'` so backticks are literal. Do not escape them with `` \` ``.

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

3. Write the description:
```bash
gh pr edit --body "$(cat <<'EOF'
## Summary
- ...
EOF
)"
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
