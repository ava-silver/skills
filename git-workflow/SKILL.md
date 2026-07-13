---
name: git-workflow
description: Ava's git/Graphite (gt) workflow at Datadog. Load BEFORE any git, gt, or gh pr command -- including git commit, git push, git ac, git cr, gt ss, gt s, gt submit, creating branches, opening PRs, syncing, or worktrees. Contains required aliases (git cr, git ac, gt ss --no-edit -q), branch naming (ava.silver/TICKET/desc), and the rule to never use git push.
user_invocable: false
---

# Git Workflow

All repos use **Graphite (`gt`)** for stacked PRs.

## Branch naming
`ava.silver/{ticket}/{short-description}` — e.g. `ava.silver/svls-1234/fix-timeout`
Chore/no-ticket: `ava.silver/chore/{description}`

## Starting work — branch + first commit + PR in one shot
```bash
git cr svls-1234 short description here
# → creates branch, stages all, commits [SVLS-1234] short description here, opens PR
# chore: git cr chore short description → commit "chore: short description"
```

**Already on a branch** (e.g. in a worktree with no commits yet): skip `git cr`:
```bash
git ac short description here
gt ss --no-edit -q
```

## Stacked (child) PRs — default path
**Always use `git cr` from the parent branch.** Do NOT reach for `gt create` — it is not part of this workflow.

```bash
# On parent branch ava.silver/svls-1234/parent-work:
git cr svls-1235 child description here
# → creates ava.silver/svls-1235/child-description-here off the current branch,
#    stages all, commits, opens a child PR stacked on the parent
gt ss --no-edit -q   # pushes the full stack
```

`gt create` is not the default. Only use it if `git cr` cannot achieve the desired branch shape, and document why.

## Adding commits
```bash
git ac short description here   # stages all + commits (does NOT push)
gt ss --no-edit -q              # push + create/update PR(s) in the stack
```

`git ac` auto-prepends the ticket from the branch name: `[SVLS-1234] short description`.

## Message style
Commit and branch messages describe intent, not the implementation detail. Keep them concise -- usually under seven words.

- Good: `pr feedback`, `fix redirect behavior`, `implement x feature`
- Avoid: `drop unneeded impl entry for connection_string_names passthrough`, `make flat sticky_settings local the source of truth`

## Key rules
- **Never use `git push`** — always use `gt ss --no-edit -q`
- Use `gt s` instead of `git pull` to sync
- After creating a PR, update the description with `/pr-description`
- Do not add Claude as a co-author to any commit

## Worktrees
Live at `~/dd/{repo-name}.worktrees/{branch-name}/` (slashes → `-`).
```bash
git worktree add ~/dd/{repo}.worktrees/{branch} {branch}
git checkout $(git main)
```
