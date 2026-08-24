---
name: mcp
description: Call MCP servers for Datadog metrics and Slack through the `mcp` tool. Load this skill whenever a task needs either service, MCP, or pi-mcp-adapter.
---

# MCP via pi-mcp-adapter

Use MCP for Datadog and Slack. Use `acli` directly for Jira and Confluence.

The `pi-mcp-adapter` extension exposes one `mcp` tool. Servers start when you first call one of their tools, and tool metadata is cached.

## Servers

| Server | Use for |
|---|---|
| `datadog-staging` | Datadog on staging (`datad0g.com`) |
| `datadog-prod` | Datadog on prod (`datadoghq.com`) |
| `slack` | Datadog Slack: read and search channels and threads, and post messages |

## Workflow

The `mcp` tool accepts one object. Its mode precedence is `action > tool > server > describe > search > nothing`.

```
mcp({})
mcp({ server: "datadog-prod" })
mcp({ search: "metric" })
mcp({ describe: "<tool_name>" })
mcp({ tool: "<tool_name>", args: '{"arg": "value"}' })
mcp({ tool: "<tool_name>", server: "datadog-prod", args: '{...}' })
```

Always describe a tool before calling it.

## Authentication

The adapter manages OAuth for the Datadog servers. Authenticate interactively with `/mcp-auth <server>`, or use:

```
mcp({ action: "auth-start", server: "<name>" })
mcp({ action: "auth-complete", server: "<name>", args: '{"redirectUrl":"..."}' })
```

Authenticate once for each Datadog org. If Slack reports that authentication is required, call `slack_auth`.
