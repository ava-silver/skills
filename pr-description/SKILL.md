---
name: pr-description
description: Update a PR description based on what's actually in the diff. Use when user says 'update PR description', 'write PR description', 'fill in PR description', 'pr description', or after creating a new PR. Writes the description as if from scratch -- not influenced by chat history or brainstorming.
allowed-tools: Bash, Read, Glob
---

# PR Description

Updates a PR description based solely on what's in the diff -- not the conversation history.

## Key Rules

1. **Write as if from scratch.** Ignore the conversation history when composing the description. The description should reflect what's actually in the PR, not what was debated, explored, or considered along the way.
2. **Source of truth is the diff.** If it's unclear what's in scope, re-fetch from GitHub (`gh pr view --json body,title,files`) or read the local branch diff (`git diff $(git main)...HEAD`).
3. **No chat archaeology.** Don't carry over rejected ideas, alternative approaches, or intermediate decisions from the session.
4. **Testing sections are for non-CI checks.** Assume build, lint, and unit tests are covered by pre-commit/CI. In any Test Plan, Testing, QA, or similar section, include only manual testing or QA steps that validate behavior beyond what CI already checks.

## Workflow

### Step 1: Get the diff

```bash
gh pr view --json title,body,files     # see current description + changed files
git diff $(git main)...HEAD            # full diff if more detail needed
```

### Step 2: Check the PR template

```bash
cat .github/PULL_REQUEST_TEMPLATE.md 2>/dev/null || cat .github/pull_request_template.md 2>/dev/null
```

Fill in every section of the template. If there's no template, use a minimal Summary + Test Plan structure.

### Step 3: Write the description

Base it only on:
- The actual file changes in the diff
- The Jira ticket (if one was provided by the user)
- The existing PR template sections

```bash
gh pr edit --body "$(cat <<'EOF'
## Summary
- ...

## ...
EOF
)"
```

**Heredoc note:** Use `<<'EOF'` (single-quoted) -- everything inside is literal, no escaping needed. Do NOT escape backticks with `\`` inside a single-quoted heredoc.

### Step 4: QA Links (UI PRs only)

When the PR touches UI code, add clickable staging links to the QA Instructions section. Compute the hash with the web-ui hash command:

```bash
HASH=$(yarn hash --hash-only)
```

**Serverless PRs** -- classify from the diff:
- **Serverless-only** (all changes within serverless product scope):
  → `https://ddserverless-${HASH}.datadoghq.com/<inferred-path>`
- **Cross-team** (also touches shared or non-serverless code):
  → Both `https://ddserverless-${HASH}.datadoghq.com/<inferred-path>`
    and `https://app-${HASH}.datadoghq.com/<inferred-path>`
- Ambiguous? Ask.

Infer the path from changed file paths (e.g. `/serverless/aws/lambda?config_your-feature-flag=true`). Feature flags use `?config_flag-name=value` URL params.
