# <Project Name> — Tickets

> Template for `TICKETS.md`. One ticket per block, separated by `---`, numbered from `1`
> (no real keys until upload). Each ticket must be self-contained — no bare references to
> local files, milestone markers (e.g. `M1.1`), or `SCOPE.md`/`CONTEXT.md` sections.
> Inline the relevant context directly; if an external doc (RFC, Confluence, Google Doc)
> is genuinely needed, link to its hosted URL. After upload, annotate each `## N.` heading
> with its real key (e.g. `## 3. [SVLS-1234] Title`) so re-runs don't double-create.

---

## 1. <Title>

**Summary:** one-liner of the work (becomes the Jira title).

**Context:** why this ticket exists and what problem it solves. Inline the relevant
background directly — do not reference local files or milestone markers. If an external
doc is needed, link to its hosted URL (e.g. Google Doc, Confluence). Self-contained
enough that someone can pick it up cold without reading the RFC.

**Code links:** relevant files/dirs, `file:line` where known.

**Acceptance criteria:**
- [ ] concrete, checkable outcome
- [ ] ...

**Caveats / notes:** (optional) edge cases, gotchas, non-obvious decisions. Omit if there's nothing genuinely surprising — don't restate dependencies or context already captured above.

**Hard dependencies:** Ticket #X (blocking only — omit soft/conceptual deps; these
become Jira "Blocks" links at upload, not description text).

---

## 2. <Title>

**Summary:** ...

**Context:** ...

**Code links:** ...

**Acceptance criteria:**
- [ ] ...

**Caveats / notes:** ...

**Hard dependencies:** none
