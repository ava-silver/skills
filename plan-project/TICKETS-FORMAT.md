# <Project Name> — Tickets

> Template for `TICKETS.md`. One ticket per block, separated by `---`, numbered from `1`
> (no real keys until upload). Each ticket must be self-contained — no bare references to
> local files, milestone markers (e.g. `M1.1`), or `SCOPE.md`/`CONTEXT.md` sections.
> Inline the relevant context directly; if an external doc (RFC, Confluence, Google Doc)
> is genuinely needed, link to its hosted URL.

## Cross-references — the `[[TN]]` token

Every reference to another ticket in this file — in prose **and** in `### Dependencies` —
uses the token `[[TN]]`, where `N` is the ticket's `## N.` number (e.g. `[[T3]]`). This is
the only form allowed; never write bare `Ticket 3`, `Ticket #3`, or `M1.2`. The `## N.`
heading is the lookup table: `## 3.` defines what `[[T3]]` points at.

- Keep pairing the token with the name (per the skill's naming rule): `[[T3]] (auth middleware)`.
  The token is the substitution target; the `(name)` stays put for readability.
- After upload, annotate each `## N.` heading with its real key — `## 3. [SVLS-1234] Title` —
  so re-runs don't double-create, then find/replace every `[[T3]]` →
  `[SVLS-1234](https://<domain>/browse/SVLS-1234)`. One replace per ticket; the token's
  rigid shape makes this safe. `rg '\[\[T\d+\]\]' TICKETS.md` must come back empty afterward.

---

## 1. <Title>

**Summary:** one-liner of the work (becomes the Jira title).

**Context:** why this ticket exists and what problem it solves. Inline the relevant
background directly — do not reference local files or milestone markers. If an external
doc is needed, link to its hosted URL (e.g. Google Doc, Confluence). Self-contained
enough that someone can pick it up cold without reading the RFC.

**Code links:** (optional) GitHub links to relevant packages, files, or specific lines. Omit if not applicable.

**Acceptance criteria:**
- [ ] concrete, checkable outcome
- [ ] ...

**Caveats / notes:** (optional) edge cases, gotchas, non-obvious decisions. Omit if there's nothing genuinely surprising — don't restate dependencies or context already captured above.

### Dependencies
`[[T2]], [[T4]]` (or `none`; blocking only — omit soft/conceptual deps; these become Jira
"Blocks" links at upload, not description text)

---

## 2. <Title>

**Summary:** ...

**Context:** ... (reference other tickets inline with the token, e.g. "extends the schema from [[T1]] (data model)")

**Code links:** ...

**Acceptance criteria:**
- [ ] ...

**Caveats / notes:** ...

### Dependencies
`none`
