---
name: atlassian
description: Ava's Atlassian (Jira, Confluence) workflow. Load this skill whenever using any Atlassian MCP tools.
user_invocable: false
---

# Atlassian

**Cloud ID**: `66c05bee-f5ff-4718-b6fc-81351e5ef659` — use for all MCP tool calls.

## SVLS Jira ticket defaults

| Field | Value |
|---|---|
| Project | SVLS (`15505`) |
| Issue type | Task (`10002`) |
| Team (`customfield_15831`) | Serverless Onboarding & Enablement (`22498`) |
| Labels | `["Team - SVLS"]` |
| Priority | **Omit entirely** |
| Assignee | Leave blank unless requested |
| Parent (epic) | Always required — ask if not provided |

Parent syntax — use `parent`, not `customfield_10014`:
```json
"parent": { "key": "SVLS-XXXX" }
```

## Team IDs (`customfield_15831`)

| Team | ID |
|---|---|
| Agent | 19143 |
| APM | 19141 |
| App | 19140 |
| Data | 19139 |
| DevEx | 19142 |
| Integrations | 19144 |
| Serverless AWS | 22447 |
| Serverless Azure | 22448 |
| Serverless Cloud Tracing | 22451 |
| Serverless Edge Computing | 22450 |
| Serverless Experiences | 22449 |
| Serverless Onboarding & Enablement | 22498 |

Return ticket URL: `https://datadoghq.atlassian.net/browse/<KEY>`
