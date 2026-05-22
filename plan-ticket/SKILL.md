---
name: plan-ticket
description: Create an implementation plan from the current worktree branch, Jira ticket, and relevant codebase context. Use when the user says "plan ticket", "/plan-ticket", "create a plan", "implementation plan", or wants planning from a branch like ava.silver/svls-1234/description; accepts "no grill", "skip grill", or "--no-grill" to skip the grill-me review.
---

# Plan Ticket

Creates a grounded implementation plan from the active worktree. By default, the plan is stress-tested with the `grill-me` skill before treating it as settled.

## Arguments

- Default: gather context, draft the plan, then use `grill-me`.
- `--no-grill`, `no grill`, or `skip grill`: gather context and draft the plan, but skip `grill-me`.
- Any other argument text is extra planning context from the user. Use it alongside the ticket and codebase context.

## Key Rules

1. This is planning only. Do not edit code, commit, push, or update tickets unless the user explicitly asks.
2. If any git command is needed, first load `git-workflow`.
3. If any Atlassian tool is needed, first load `atlassian`.
4. If grill is enabled, load `$grill-me` after the initial plan exists and pass it the plan plus unresolved questions.
5. Ask clarifying questions only after ticket and codebase exploration. If the answer can be found in code or Jira, find it instead of asking.

## Workflow

### Step 1: Parse inputs

1. Detect whether grill is disabled by argument text.
2. Capture any remaining argument text as extra context.
3. Get the current branch:

```bash
git branch --show-current
```

4. Extract the first ticket-like segment from the branch, such as `svls-1234`, and uppercase it to `SVLS-1234`.
5. If the branch has no ticket, use a ticket key from the user input. If neither exists, ask for the ticket or permission to plan from code context only.

### Step 2: Load ticket context

Use the Atlassian workflow to fetch the Jira issue. Capture:

- Summary, status, type, description, acceptance criteria, labels, parent, assignee
- Comments or linked context that changes the implementation approach
- Linked Confluence pages, PRDs, designs, related issues, or external docs when available

Treat the ticket as the initial problem statement, not as the whole source of truth.

### Step 3: Gather codebase context

Explore enough of the repo to make the plan concrete:

- Search with `rg` for terms from the ticket summary and description.
- Find existing implementations, similar features, tests, routes, services, components, config, and ownership boundaries.
- Read nearby tests before proposing a test plan.
- Prefer existing patterns and local helper APIs.

Do not stop at file names if behavior matters. Read the relevant code.

### Step 4: Draft the plan

Produce a concise plan with:

- Goal and non-goals
- Current behavior and target behavior
- Proposed implementation steps
- Files or modules likely to change
- Test plan
- Risks, tradeoffs, and open questions

Use clickable file references when citing local code.

### Step 5: Validate the plan

If grill is enabled, invoke `grill-me` with the drafted plan and unresolved questions. Let it question the plan one decision at a time, and revise the plan as answers settle.

If grill is disabled, do not run the grill. Include remaining open questions in the plan and ask the most important clarifying question if one blocks useful progress.
