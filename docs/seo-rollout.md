# SEO rollout

Centralized metadata covers every rendered page. Tool and Strategy descriptions reuse curated summaries. Homepage JSON-LD uses WebSite and CreativeWork, without institutional ownership claims. Social cards use summary with no image because no suitable committed image was supplied. The 404 is noindex and excluded from the sitemap.

Validation: 150 canonical routes match the sitemap; root and project-path builds pass. Metadata escaping, valid JSON-LD, catalogue, forms, editorial coverage, terminology, contributors, links and catalogue JS checks pass.

Production build: `python scripts/build_site.py --strict --base-path /metabolomics-navigator`; run `python scripts/check_seo.py --base-path /metabolomics-navigator`. GitHub Actions derives the project prefix from GITHUB_REPOSITORY. SITE_URL can override the configured origin.

Manual follow-up: add the URL-prefix property https://scottjarmusch.github.io/metabolomics-navigator/ in Google Search Console, verify ownership using Google's supplied verification token/file, submit sitemap.xml and inspect/request indexing for the homepage. No token was supplied; ownership verification and submission were not performed. The project-path robots.txt is retained, but crawler-wide robots rules are read from the host root, which this repository does not control.

Google's site-name feature does not support subdirectory-level sites; structured data remains truthful but cannot guarantee a branded site-name display or indexing timing. See https://developers.google.com/search/docs/appearance/site-names and https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls .

Ask Navigator remains the public visual preview; unpublished workflow work stays on its separate local branch. Next: resume specialist population before returning to Ask Navigator, per the user's latest order.
