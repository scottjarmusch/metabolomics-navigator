# Codex implementation prompt

Implement Education as a **lightweight curated guide to external learning resources**.

Read:
- handoff/education-resource-2026-09-26/README.md
- handoff/education-resource-2026-09-26/IMPLEMENTATION.md
- handoff/education-resource-2026-09-26/education.schema.json
- handoff/education-resource-2026-09-26/education.html
- handoff/education-resource-2026-09-26/education-seed-candidates.tsv
- handoff/education-resource-2026-09-26/broader-tutorial-leads.tsv

Requirements:

1. Add **Education** to the main header between Strategies and Ask Navigator.
2. Add Education to Footer → Explore.
3. Add `/education/` as a static route and include it in sitemap.xml.
4. Create `schemas/education.schema.json` and `content/education/`.
5. Use the simplified schema from the handoff.
6. Each resource must link to at least one existing Navigator `tool_slug`; fail the build for unknown tool slugs.
7. Render resources as simple external links grouped primarily by tool.
8. Show only useful metadata: title, provider, resource type, one-line description, optional experience level, optional currentness/legacy note.
9. Add a lightweight client-side text search. Do not add a JS framework.
10. Do not embed YouTube or any third-party media.
11. Do not add thumbnails, view counts, likes, popularity ranking, or “best” labels.
12. Add deterministic SEO metadata and sitemap/canonical checks.
13. Build the inverse relationship in memory so a future tool-page “Learn this tool” section can reuse the same records.
14. Convert a small number of the strongest verified seed links into real Education YAML records if desired, but do not publish anything without checking that the link still resolves and clearly matches the linked tool.
15. Keep the implementation static, small, accessible, and neutral.
16. Run the full validation/build test suite and fix regressions.

Product principle:

> Navigator curates and points outward. It does not become the tutorial platform.
