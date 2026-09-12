# SEO rollout

Centralized metadata covers every rendered page. Tool and Strategy descriptions reuse curated summaries. Homepage JSON-LD uses WebSite and CreativeWork, without institutional ownership claims. Social cards use summary with no image because no suitable committed image was supplied. The 404 is noindex and excluded from the sitemap.

Validation: 150 canonical routes match the sitemap; root and project-path builds pass. Metadata escaping, valid JSON-LD, catalogue, forms, editorial coverage, terminology, contributors, links and catalogue JS checks pass.

Production build: `python scripts/build_site.py --strict --base-path /metabolomics-navigator`; run `python scripts/check_seo.py --base-path /metabolomics-navigator`. GitHub Actions derives the project prefix from GITHUB_REPOSITORY. SITE_URL can override the configured origin.

Manual follow-up: add the URL-prefix property https://scottjarmusch.github.io/metabolomics-navigator/ in Google Search Console, verify ownership using Google's supplied verification token/file, submit sitemap.xml and inspect/request indexing for the homepage. No token was supplied; ownership verification and submission were not performed. The project-path robots.txt is retained, but crawler-wide robots rules are read from the host root, which this repository does not control.

Google's site-name feature does not support subdirectory-level sites; structured data remains truthful but cannot guarantee a branded site-name display or indexing timing. See https://developers.google.com/search/docs/appearance/site-names and https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls .

Ask Navigator remains the public visual preview; unpublished workflow work stays on its separate local branch. Tool population is paused by the latest user instruction; the population automation was deleted. PR #20 remains unmerged.


12 September branded-search refinement: strengthened homepage title/description, visible resource definition, About introduction and README live-site link. Retained WebSite and CreativeWork nodes; linked their identities and added metabolomics/mass-spectrometry Thing subjects. No generic alternate name was added because it would not improve identification of the full brand.

The SEO check now independently requires the exact production project URL on scottjarmusch.github.io, so a consistently wrong root URL cannot pass. It also checks the homepage brand in title, description, visible HTML and both JSON-LD entities, plus homepage sitemap inclusion and the project sitemap reference in robots.txt. Hidden/script/template text does not satisfy the visible-text assertion. CI's existing GITHUB_REPOSITORY-based URL derivation remains unchanged.

For CI-equivalent local validation, set GITHUB_REPOSITORY=scottjarmusch/metabolomics-navigator before running build_site.py --strict and check_seo.py. Root-path previews remain possible with an explicit alternate SITE_URL; they must not masquerade as the production GitHub Pages homepage.
