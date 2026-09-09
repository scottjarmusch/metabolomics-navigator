# Phase 0 — canonical Analytical Strategies

Based on main commit 2663bf95610ff06c534518e6c28a25357c3a4ff5. Renamed the method collection directory, schema, two templates, issue parser, two issue forms and all associated code, vocabulary keys, routes and JSON fields. No resources added or removed: 79 Tools and 13 Strategies remain in this phase. Canonical routes use `/strategies/`; supporting recipe links use `method_url` and `method_available`.

Publications, external names and external URLs remain unchanged. Branding audits distinguish these from Navigator-owned text. History and closed PR descriptions are not rewritten. No Ask Navigator implementation is part of this phase.

Validation: catalogue/schema, form synchronization, editorial coverage, strict GitHub Pages base-path build, catalogue JavaScript tests, 3,502 local links across 107 pages, Strategy terminology and Navigator branding audits all pass. The CI workflow runs the same structural, editorial, terminology and link checks.

All six historical branches listed in the master handoff have confirmed merged PRs (#4 and #6–#10); branch cleanup follows the migration merge. Subsequent phases must start only after Phase 0 is complete.
