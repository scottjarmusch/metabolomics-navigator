# Premium redesign preview — 10 September 2026

Status: user approved the preview and authorized publication on 10 September 2026. GitHub main was fetched and matched the branch base, `146ae1935f33702a52512adeb8e4589931e6be8d`. The contribution prompt was strengthened with a teal button and a tinted panel before approval.

## Changes

- `assets/product-refresh.css`: warm paper, deep teal, restrained gold, serif editorial headings, ruled catalogue rows, compact task icons, responsive layouts, keyboard focus and forced-color treatment.
- `templates/base.html` and `config/site.yml`: brand descriptor, Beta mark, quiet navigation and consistent footer.
- `templates/home.html` and new `templates/scientific-collage.html`: six synthetic scientific illustrations, dynamic catalogue counts, search, six task links and contribution prompt. Illustration numbers removed at the user's request. All figures are labelled illustrative rather than real experimental results.
- `templates/tools.html`, `templates/strategies.html`, `templates/submit.html`: approved catalogue and contribution copy; clear Tool/Analytical Strategy routes and editorial process. Existing filters, forms, scientific metadata and submission destinations preserved.
- New `templates/about.html`: mission, creator biographies, official profile links and institutional non-endorsement. Alan's title checked against the current NIEHS profile.
- New `templates/ask.html`: six starting-data choices, workflow outline, explanatory disclosure and visible export placeholders. Choices and exports are disabled and explicitly labelled visual preview. No recommendation engine implemented.
- `scripts/build_site.py`: dedicated About/Ask templates and stylesheet cache invalidation. No catalogue content, schemas, relationships or scientific publication records changed.

## Validation

Passed catalogue validation (91 Tools, 13 Strategies), submission-form synchronization, editorial coverage baseline, strict static build, catalogue JavaScript tests, three Strategy terminology tests, Strategy audit and brand audit. Internal-link validation checked 4,146 links/fragments across 121 pages and 220 relationship links.

Browser checks passed for homepage, Tools, GNPS, MZmine, Strategies, reverse metabolomics, About, Contribute and Ask at 1440, 1024, 390 and 320 pixels: one H1, no horizontal overflow and no JavaScript errors. Nine routes also passed reflow at 200% CSS-rendered zoom; this is not a native browser-zoom test.

Keyboard checks covered the skip link, mobile menu, disclosures and the mobile workflow summary. Homepage search, catalogue empty state/reset and disabled preview choices passed. Reduced-motion behavior and a forced-colors screenshot were checked. Sampled homepage text contrast passed after darkening the eyebrow labels (minimum sampled ratio 5.5:1). This is targeted QA, not a full accessibility certification.

Desktop/mobile screenshots were visually reviewed, including dense MZmine metadata and the Strategy page. Local QA scripts and screenshots are in the parent workspace `work/redesign-browser-qa.cjs`, `work/redesign-interaction-qa.cjs` and `work/redesign-qa/`.

## Review limits

Preview: http://127.0.0.1:8771/metabolomics-navigator/ (this computer only). No merge, push or public deployment performed. Automation remains paused while this redesign awaits review. Ask Navigator functionality remains gated on Tool population and relationship completion. No known blocking responsive issue from the checks above; native browser zoom and a full assistive-technology audit remain unverified.
