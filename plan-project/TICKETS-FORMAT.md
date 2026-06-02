# <Project Name> — Tickets

> Template for `TICKETS.md`. One ticket per block, separated by `---`, numbered from `1`
> (no real keys until upload). Link back to `CONTEXT.md` concepts and RFC/`SCOPE.md`
> sections so vocabulary stays consistent. After upload, annotate each `## N.` heading
> with its real key (e.g. `## 3. [SVLS-1234] Title`) so re-runs don't double-create.

---

## 1. <Title>

**Summary:** one-liner of the work (becomes the Jira title).

**Context:** why this ticket exists — link to the RFC section / `SCOPE.md` milestone /
`CONTEXT.md` concepts it comes from. Enough that someone can pick it up cold.

**Code links:** relevant files/dirs, `file:line` where known.

**Acceptance criteria:**
- [ ] concrete, checkable outcome
- [ ] ...

**Caveats / notes:** edge cases, gotchas, decisions already made.

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
