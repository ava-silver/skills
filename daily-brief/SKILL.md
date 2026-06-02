---
name: daily-brief
description: Pulls together today's calendar, Jira tickets, and GitHub PRs into a single prioritized brief. Also updates the "PR Review Time" calendar event with PRs needing review. Use when the user says 'daily brief', 'morning brief', 'what's on my plate', 'show me my day', or invokes /daily-brief.
user_invocable: true
allowed-tools:
  - Bash
  - mcp__claude_ai_Google_Calendar__list_events
  - mcp__claude_ai_Google_Calendar__list_calendars
  - mcp__claude_ai_Google_Calendar__update_event
  - mcp__claude_ai_Atlassian__searchJiraIssuesUsingJql
---

# Daily Brief

## Constants

| Key | Value |
|-----|-------|
| Jira assignee ID | `61ccbfd6e763790068b0b735` |
| Jira cloud ID | `66c05bee-f5ff-4718-b6fc-81351e5ef659` |
| Calendar event to update | `PR Review Time` (today only) |

## Step 1 — Parallel fetch (all four at once)

1. **Calendar** — `list_events` for today (midnight–23:59:59 ISO 8601 with timezone). Capture event IDs; note the ID of "PR Review Time" if present.
2. **Jira** — `searchJiraIssuesUsingJql` with `cloudId: 66c05bee-f5ff-4718-b6fc-81351e5ef659`, `jql: project = SVLS AND assignee = "61ccbfd6e763790068b0b735" AND statusCategory != Done ORDER BY priority DESC, updated DESC`, fields: summary, status, priority, sprint, parent, maxResults: 50.
3. **My open PRs** — `gh search prs --author @me --state open --org DataDog --json title,url,repository,updatedAt,reviewDecision --limit 50`
4. **PRs to review** — `gh search prs --review-requested @me --state open --org DataDog --json title,url,repository,author,updatedAt --limit 50`

## Step 2 — Output brief

1. **Today's schedule** — timed events with start/end. Skip all-day unless notable (OOO, deadline, release).
2. **PRs to review** — from fetch 4.
3. **In-progress** — Jira tickets with status "In Progress".
4. **Up-next** — remaining assigned tickets, current sprint first, then by priority.
5. **My open PRs** — from fetch 3, with review state (approved / changes requested / pending).
6. **Suggested focus** — 1–3 sentences on what to tackle first.

## Step 3 — Update "PR Review Time" calendar event

If the event exists today: call `update_event` to set its description to the review-requested PR list (`Title — URL`, one per line). Preserve all other fields.

If it doesn't exist: note "No PR Review Time event found today — skipping calendar update."

Confirm at end: `Updated PR Review Time event with N PRs.`
