---
name: plan-project
description: Take a project from an RFC/design doc to fully-fleshed Jira tickets under an epic, through four phases — context, scoping, planning, upload. Use when the user says "plan project", "/plan-project", "turn this RFC into tickets", "scope this project", or wants to break a design doc into Jira tickets.
allowed-tools: Read, Write, Bash, Glob, Grep, Skill
---

# Plan Project

Drives a project from research/RFC context to fleshed-out Jira tickets under an epic. Produces three artifacts in the **current working directory**: `CONTEXT.md`, `SCOPE.md`, `TICKETS.md`. Each phase produces a durable artifact, so **planning can resume from any phase** — on invocation, glob for these files and, if any exist, summarize them and ask whether to resume from the furthest-along phase or start fresh.

Load the `atlassian` skill before any Jira call.

## Phase 0 — Inputs (fail fast)

Ask for (or use provided): context path/link, RFC/design doc, target epic key.
- Local files → `Read`. Confluence → atlassian MCP. Figma → Figma MCP.
- Google Docs can't be fetched — ask the user to "Download as Markdown" and provide the file.
- **Fetch the epic via Jira and confirm its summary back** before proceeding; bail if the key doesn't resolve.

`grill-me` is required for phases 1–2. Check `~/.claude/skills/grill-me/SKILL.md` (or agent equivalent); if missing, install: `bunx skills add https://github.com/mattpocock/skills -g -y -a claude-code` (fall back to `npx` if `bunx` isn't on PATH).

## Phase 1 — Context → `CONTEXT.md`

Explore the inputs, then invoke the `grill-me` skill focused on the **concepts and terminology** of the RFC. Goal: a shared vocabulary, since it shapes every ticket.
- Identify key concepts. Suggest a project **name** (from the doc or your judgment) and explicitly ask if it's right or should differ.
- Surface any terms that seem conceptually **confused/conflated**; have the user clarify until the distinctions are clear.
- Write the agreed concepts, definitions, and name to `CONTEXT.md`.

## Phase 2 — Scoping → `SCOPE.md`

Invoke `grill-me` again (with `CONTEXT.md`) to nail down what's **explicitly in vs. out of scope**. Write `SCOPE.md` with:
- In-scope work (group into **milestones** only if it helps; not always needed) and out-of-scope.
- **Hard dependencies** for the work.
- **Observability / success metrics** — telemetry to prove rollout works and measure success.
- **Maintenance** — ownership and operational burden post-rollout; include code ownership only if there are cross-team ownership considerations.
- **Documentation** — docs/runbooks the work obligates, and optionally a blogpost if it warrants an announcement.
- **Rollout** (optional / minimal) — consider feature flags for anything public/customer-facing (UI, APIs, backend behavior); otherwise sequence code/docs changes correctly. Plus staged rollout/rollback where relevant.

Follow the structure in `SCOPE-FORMAT.md` (bundled alongside this skill). `SCOPE.md` is for stakeholder sharing — do not reference local files or `CONTEXT.md` in it. For any Prior Reading entry without a URL, use `[LINK NEEDED]` or ask the user for the link before writing.

Then **soft-nudge** sharing with stakeholders/PMs/EMs (it's easier to catch scoping issues before tickets exist): run `pbcopy < SCOPE.md` and tell the user it's already on their clipboard, ready to "Paste from Markdown" into a Google Doc. Don't block — let the user say proceed.

## Phase 3 — Planning → `TICKETS.md`

1. List the tickets implied by `SCOPE.md`. A task in the scoping doc doesn't map 1:1 to a ticket — carefully consider whether each task should be one ticket or several. The target is roughly a couple days of engineering time and a single conceptual task per ticket. Flag anything that looks too big or too small, and offer to split or consolidate. If a scaffolding ticket (shared types, base components, infra setup) would make downstream tickets more parallelizable, propose one. Iterate until they approve the split.
2. Write the drafts to `TICKETS.md`, each separated by `---`, numbered from `1` (no real keys yet), following the structure in `TICKETS-FORMAT.md` (bundled alongside this skill).
3. For each dependency, confirm it's **hard** (blocking) vs. soft (conceptual) — check the doc/context, ask the user if unclear. Only hard deps go in the template.
4. Have the user thoroughly review; iterate until they say it's ready to upload.

## Phase 4 — Upload

- Create every ticket under the **epic from Phase 0** (`parent: { key }`), defaulting to issue type **Task** per the `atlassian` skill; override per-ticket only if explicitly flagged as a Bug/Story. Everything except dependencies maps into the description; the Summary becomes the Jira title.
- **Do not** put dependencies in the description. After all tickets exist, create Jira issue links of type **"Blocks"** (ticket B "is blocked by" A). Print the full planned link list for confirmation before creating any links.
- Write the **real keys back into `TICKETS.md`** (annotate each `## N.` with its `SVLS-XXXX`) so re-runs don't double-create.
