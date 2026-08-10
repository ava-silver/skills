---
name: diagram
description: 'Create a Mermaid diagram (.mmd) and render it to an image. Use when the user wants to visualize a flow, architecture, sequence, state machine, ER diagram, or any structured relationship. Trigger phrases: "make a diagram", "draw this", "diagram this", "visualize", "flowchart", "sequence diagram", "architecture diagram", "mermaid".'
---

# Diagram

Creates a Mermaid diagram, writes it to a `.mmd` file, and renders it interactively using `tldraw-mermaid`.

## Before Writing Anything

Ask the user to clarify any ambiguity before generating:
- What **type** of diagram (flowchart, sequence, state, ER, class, etc.) -- suggest one if unclear
- The **scope**: what nodes/actors/entities are in vs. out
- Any **layout preference** (top-down vs. left-right for flowcharts)
- Whether labels need to be short/abbreviated or can be verbose

If the request is clear enough to proceed without ambiguity, skip the questions and go.

## Readability Principles

- **Keep labels short** -- node labels under ~30 chars; abbreviate if needed
- **Avoid crossing edges** -- arrange nodes to minimize overlaps; prefer `TD` for hierarchies, `LR` for pipelines
- **Group related nodes** with `subgraph` blocks, but only when they add clarity
- **No wall-of-text nodes** -- if a label needs explanation, add a comment in the source, not in the node
- **Limit depth** -- more than ~4 levels of nesting makes diagrams unreadable; flatten or split instead
- **One diagram, one story** -- if it needs two separate explanations, make two diagrams

## Workflow

1. Clarify (if needed) per above
2. Determine output mode:
   - **Inline** (GitHub PR/issue descriptions, Markdown files, Confluence, any context that renders Mermaid natively): output the diagram as a fenced `mermaid` code block -- no file, no render step
   - **Rendered image** (presentations, docs that don't render Mermaid, user asked for a PNG/SVG, or interactive editing): write a `.mmd` file, then run `tldraw-mermaid diagram.mmd` -- it opens a live tldraw canvas in the browser with hot-reload on save. Shapes are real tldraw objects (draggable, resizable, restyle-able). Export to PNG/SVG from the tldraw UI if a static image is needed. (`bun link` in `~/repos/tldraw-mermaid/` to install if missing)
3. If the output mode isn't obvious from context, ask before proceeding
