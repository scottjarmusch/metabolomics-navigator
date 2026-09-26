# Codex implementation prompt

Implement the Education resource described in this handoff against the current Metabolomics Navigator repository.

Read first:
- handoff/education-resource-2026-09-26/README.md
- handoff/education-resource-2026-09-26/IMPLEMENTATION.md
- handoff/education-resource-2026-09-26/education.schema.json
- handoff/education-resource-2026-09-26/education.html

Requirements:

1. Add **Education** to the main navigation between Strategies and Ask Navigator.
2. Add `/education/` as a first-class rendered route and include it in sitemap.xml.
3. Add `schemas/education.schema.json` and `content/education/`.
4. Implement loader + JSON Schema validation for education records.
5. Fail the build when a tutorial references a nonexistent Navigator tool slug.
6. Render the Education page using a design consistent with the existing editorial UI.
7. Add lightweight client-side search/filtering for title, tool, provider, topic and experience level. Do not add a framework or external dependency.
8. Link tutorials externally; do not embed YouTube in phase 1.
9. Add Education to footer Explore links.
10. Add deterministic SEO metadata.
11. Extend `scripts/check_seo.py` or relevant tests so the Education canonical and sitemap entry are verified.
12. Add at least one **fixture/example only for automated tests** if needed, but do not publish fake tutorial content on the live page.
13. Do not modify the tool taxonomy just to support Education.
14. Do not rank resources by popularity or preference.
15. Run the full existing validation/build suite and fix regressions.

Optional but desirable:
- build the inverse relationship so tool pages can later expose `education_resources`, without rendering that section yet;
- emit `education-data.json` if consistent with the project's existing public data approach.

Keep code small, deterministic, static-site friendly, accessible, and neutral.
