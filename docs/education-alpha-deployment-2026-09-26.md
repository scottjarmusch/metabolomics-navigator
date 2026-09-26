# Education alpha deployment — 2026-09-26

Source: alpha/education-links at bad837c. Destination: separate metabolomics-navigator-alpha repository, /education/.

57 resource records validate; currentness and content review labels remain visible. Education added to header/footer. Fixed card overflow on narrow phones. Existing Ask alpha content and shared assets preserved; no production merge or deployment.

Validation: catalogue/schema and form sync; strict build; 7,396 build links and 290 relationships; 5,188 staged alpha links. Headless Edge checks: search, combined tool filter, empty state, reset, menu, noindex, widths 320/375/768/1440. Mobile screenshot visually inspected. External videos have not been watched end to end.

Reproduction: build with --base-path /metabolomics-navigator-alpha/, then scripts/stage_education_alpha.py PATH_TO_EXISTING_ALPHA_SNAPSHOT. Keep the alpha robots exclusion and noindex metadata. Staging intentionally leaves the current Ask snapshot intact.
