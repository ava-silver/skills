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

Produces a structured morning brief covering calendar, Jira, and GitHub, then updates the "PR Review Time" calendar event with PRs needing review.

## Constants

| Key | Value |
|-----|-------|
| Jira assignee ID | `61ccbfd6e763790068b0b735` |
| Jira cloud ID | `66c05bee-f5ff-4718-b6fc-81351e5ef659` |
| Jira project | `SVLS` |
| GitHub org | `DataDog` |
| Calendar event to update | `PR Review Time` (today only) |

## Step 1 -- Parallel fetch (run all four at once)

### 1a. Google Calendar

Call `mcp__claude_ai_Google_Calendar__list_events` for today. Use `timeMin` = start of today (midnight) and `timeMax` = end of today (23:59:59), both in ISO 8601 with timezone. Request all calendars the user has access to.

Capture:
- Each event's title, start time, end time, and event ID
- The event ID of any event titled "PR Review Time"

### 1b. Jira SVLS tickets

Call `mcp__claude_ai_Atlassian__searchJiraIssuesUsingJql` with:
- `cloudId`: `66c05bee-f5ff-4718-b6fc-81351e5ef659`
- `jql`: `project = SVLS AND assignee = "61ccbfd6e763790068b0b735" AND statusCategory != Done ORDER BY priority DESC, updated DESC`
- `fields`: `["summary", "status", "priority", "sprint", "parent"]`
- `maxResults`: 50

### 1c. My open PRs

```bash
gh search prs --author @me --state open --org DataDog --json title,url,repository,updatedAt,reviewDecision --limit 50
```

### 1d. PRs needing my review

```bash
gh search prs --review-requested @me --state open --org DataDog --json title,url,repository,author,updatedAt --limit 50
```

## Step 2 -- Synthesize brief

Output the brief with these sections in order:

### 1. Today's schedule
List timed calendar events with start/end times. Skip all-day events unless the title suggests something notable (e.g. OOO, deadline, release). Format: `HH:MM–HH:MM  Event title`.

### 2. PRs to review
List from step 1d results. Format: `- [title](url) — repo, by author`.

### 3. In-progress work
Jira tickets whose status category is "In Progress". Format: `- SVLS-XXXX: summary (status)`.

### 4. Up-next / todo
Remaining assigned Jira tickets not yet in progress, prioritized by sprint urgency (current sprint first, then by priority). Format: `- SVLS-XXXX: summary (priority, sprint name if available)`.

### 5. Open PRs
My authored PRs from step 1c. Show review state: approved ✓, changes requested ✗, review pending (blank). Format: `- [title](url) — repo (state)`.

### 6. Suggested focus
1–3 sentences recommending what to tackle first. Consider: calendar gaps (free blocks for deep work), sprint deadlines, size of review backlog, and any PRs with requested changes.

## Step 3 -- Update "PR Review Time" calendar event

Using the PR list from step 1d:

- **If "PR Review Time" exists today**: call `mcp__claude_ai_Google_Calendar__update_event` to set the event's description to the list of review-requested PRs, one per line in the format `Title — URL`. Preserve all other event fields.
- **If it doesn't exist**: note "No PR Review Time event found today -- skipping calendar update" in the brief output.

## Step 4 -- Output

Print the full brief. At the end, on its own line, confirm the calendar update: `Updated PR Review Time event with N PRs.` (or the skip note).
