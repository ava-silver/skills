---
name: check-pr-comments
disable-model-invocation: true
description: Check a PR's review comments and determine if each has been addressed -- either by a reply in the thread or by code changes. Flags anything still needing a response or fix. Use when user says 'check PR comments', 'are comments addressed', 'what's unaddressed', 'review comment status', 'which comments need responses', 'did I address all feedback', or invokes /check-pr-comments.
allowed-tools: Bash
---

# Check PR Comments

Fetch all review threads, classify each, and report only threads still needing action. If no PR number provided, infer with `gh pr view --json number`.

## Key Rules

1. Check **both** inline review comments (`pulls/{pr}/comments`) and PR-level issue comments (`issues/{pr}/comments`).
2. **Do not trust GitHub's "resolved" toggle** — check the actual substance.
3. **REPLY CLAIMS CHANGE NOT FOUND**: if the author's reply claims a fix ("fixed", "updated", "done", "addressed", "pushed") but the diff shows no corresponding change at that file/area, flag it prominently — they likely forgot to push.
4. Output only unresolved threads. If all addressed, one line is enough.

## Commands

```bash
gh api repos/{owner}/{repo}/pulls/{pr}/comments --paginate \
  --jq '[.[] | {id, path, line: .original_line, body, user: .user.login, created_at, in_reply_to_id}]'
gh api repos/{owner}/{repo}/issues/{pr}/comments --paginate \
  --jq '[.[] | {id, body, user: .user.login, created_at}]'
gh api repos/{owner}/{repo}/pulls/{pr}/reviews --jq '[.[] | {state, user: .user.login}]'
gh pr diff {pr}
```

Group inline comments by `in_reply_to_id` (null = thread root). Classify each thread:

- **ADDRESSED** — author replied after reviewer, and any claimed code change is in the diff
- **REPLY CLAIMS CHANGE NOT FOUND** — author says "fixed" but diff doesn't confirm it
- **NEEDS REPLY** — question or request with no author reply
- **NEEDS CODE CHANGE** — change requested, no diff change found
- **AMBIGUOUS** — reply exists but unclear if concern is resolved

Output format:
```
[STATUS] @reviewer · path/to/file.go:line
> <first ~80 chars of reviewer comment>
Why: <one sentence>
```

Append one line if CHANGES_REQUESTED reviews haven't been re-reviewed.
