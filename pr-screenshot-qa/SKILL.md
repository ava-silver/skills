---
name: pr-screenshot-qa
description: Paired before-and-after screenshot QA for a Graphite PR stack. Use only when explicitly invoked to catalog screenshot cases, open production and local URLs, maintain a checklist, update PR Changes sections with HTML screenshot tables, or fix visual issues found during capture.
disable-model-invocation: true
allowed-tools: Read Write Edit Bash
---

# Paired PR Screenshot QA

Run a paired, user-guided screenshot pass for a PR stack. The user captures images; maintain the state, URLs, branches, and PR documentation.

## Start

Ask for any missing inputs before opening URLs:

- Stack root or PR numbers, plus the intended order.
- Before and local hostnames, feature flags, and any clean-org exception for empty-state routes.
- Permission-test mechanism and whether branch switching, fixes, commits, and submission are allowed.

Before any git, `gt`, or `gh` command, load the `git-workflow` skill. Use `gt log short` only as a starting point; resolve the actual PR branches and base refs before declaring the stack. Exclude adjacent Graphite branches that are not in scope.

Create one checklist at a user-specified OS-temp path. If none is supplied, create a Markdown file with `mktemp` under the OS temporary directory. Each row tracks the PR, branch, route, state/mocking, expected visual result, and before/after status.

## Catalog each PR

1. Read its current PR description before editing it.
2. Inspect the PR diff and relevant tests. Derive screenshot cases from actual UI branches, API failure paths, permissions, responsive breakpoints, and user navigation.
3. Capture meaningful UI deltas. For navigation or other non-visual behavior, record concise before/after behavior in the table instead of forcing screenshots.
4. Deduplicate shared behavior, but preserve provider-specific states when their UI or API differs.
5. For every case, record:
   - branch that contains it;
   - direct route and clicks needed from page load;
   - flags and query parameters;
   - permission or mock state;
   - expected before and after result.

Use repository-supported permission overrides and feature flags to reach permission- or rollout-dependent states. If an override exposes an endpoint-specific failure, preserve the shared testing mechanism and route the narrow backend fix to that endpoint's owner unless the user explicitly wants a broader change.

## Synthetic error states

Prefer supported permission overrides and feature flags before introducing test state locally. When an error state cannot be reached safely otherwise:

1. Add the smallest reversible local mock or request interception in the current worktree.
2. Scope it to the target endpoint and test case; keep ordinary page behavior unchanged.
3. Record the mock, expected error UI, and removal step in the checklist.
4. Remove the temporary mock after capture. Commit a mock only when it is durable automated-test coverage.

## PR description

Ensure the **Changes** section has one paste-ready HTML table:

```html
<table>
<thead><tr><th>Case</th><th>Before</th><th>After</th></tr></thead>
<tbody>
<tr><td>Meaningful visual case</td><td><!-- Paste screenshot --></td><td><!-- Paste screenshot --></td></tr>
</tbody>
</table>
```

- Preserve existing valid screenshot attachments.
- Add all meaningful UI and behavior cases, including connected and disconnected variants where they differ.
- Keep exactly **Case**, **Before**, and **After** columns.
- Use paste-ready screenshot cells only for UI deltas. For behavior-only rows, link the case URL and write the before/after behavior as text.
- Do not add control-only rows or visible placeholder prose.
- Update the PR description only after rereading its current body.

## Capture loop

For one case at a time:

1. Switch this worktree to the case branch when permitted. Verify the changed code is present before opening local.
2. Open the PR and the **before** URL. State whether it is local or not. Wait for the user to capture it.
3. Mark before complete, open the matching **local** URL, and state whether it is local or not. Wait for capture.
4. Explain the exact expected visual delta before asking the user to compare.
5. Mark the case complete only after the user confirms it.
6. Move to the next unchecked screenshot row.

For routes that require a clean/new org, use the user-specified alternate host. If local routing is supplied through a browser extension, open the alternate host and explicitly say it is not local.

## Fixes found during QA

When the user authorizes a fix:

1. Confirm the branch contains the relevant PR before editing.
2. Isolate the cause from the rendered UI, network request, diff, and source. Avoid hiding unrelated backend errors merely to clean a screenshot.
3. Make the smallest scoped change. Prefer a component-scoped style override over changing a shared layout component.
4. Run focused tests and `git diff --check`.
5. Preserve user untracked files. Stage explicit paths rather than a blanket add when needed.
6. Commit with the repository workflow and submit with `gt ss --no-edit -q`. Report the commit and residual issue.

## Finish

Return the checklist path, completed versus remaining cases, updated PR URLs, commits submitted, and any endpoint/backend follow-up.
