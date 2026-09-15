# Contributing

Metabolomics Navigator is designed so that researchers can contribute without knowing Git, YAML, or the site architecture.

## Submit a tool

The current scope is **MS-based metabolomics**. NMR-only and other non-MS-only tools and strategies are outside scope. Shared reference databases, statistical tools and platforms remain eligible when they support MS metabolomics; entries should describe that use. A platform-independent label alone does not establish eligibility.

Use the **Submit a metabolomics tool** issue form. A minimal submission needs a name, link, neutral description, resource type, primary function, analytical platform, interface, access model, and submitter relationship. Aliases and alternative spellings are optional but encouraged for discoverability and duplicate detection.

## Submit a strategy

Use the **Submit a metabolomics strategy** issue form. Strategies must be published and transferable, not simply application studies that happen to use metabolomics. Sample type and biological context are optional structured fields that improve discovery.

## What happens after submission

New-tool and new-strategy forms create structured drafts through automation. The **Update an existing tool** and **Update an existing strategy** forms create issues for an editor to review and implement. All GitHub forms require a free account.

1. GitHub Actions converts the form into a structured draft record.
2. A pull request is opened for review.
3. Automated checks validate the schema, controlled vocabulary, names/aliases, and cross-links.
4. An editor checks scope and neutral presentation.
5. Once merged, the site rebuilds automatically.

## Entry quality

A **stub** contains enough information to identify and categorize the resource. A **complete entry** should additionally document detailed capabilities, data compatibility, documentation, publication(s), version/freshness, scope and considerations, and provenance.

## Neutrality

Describe documented functionality and scope. Avoid unsupported statements such as “best,” “most accurate,” or “superior.” Comparative performance claims should be supported by independent evidence.

## Writing complete entries

Follow [the editorial model](docs/tool-editorial-model.md) for coverage, source selection, and verification. The task guide is organized in `config/guide.yml`; when adding a tool, consider where it belongs in that guide as well as the searchable catalogue.

## Publication scope

Include only the resource introduction, substantial updates, or directly implemented methods. Do not list papers merely because they use a tool, or credit a tool with a separate resource’s paper. Editors separate software/documentation citations from scholarly publications. See [publication selection](GOVERNANCE.md#publication-selection) and the [September 2026 audit](docs/publication-audit-2026-09-08.md).


## Accepting tool submissions and recording updates

Submission acceptance is separate from editorial completion. Maintainers check the required form information, scope, duplicate status, links and public attribution consent. Schema, vocabulary, relationship, build and link checks remain mandatory. A tool may be merged with `status.entry: stub` and `status.review: unreviewed`; its page clearly shows editorial additions pending. Missing optional details do not block acceptance. No approval label or status field substitutes for a maintainer merging the protected pull request.

Later editorial additions belong in a separate pull request. An entry promoted beyond an unreviewed stub must pass the full editorial coverage check; only set `editorially_reviewed` and an editorial review date after that review actually occurs. Strategy criteria are unchanged.

Each tool page includes committed entry history with dates, commit summaries, diffs and immutable revisions, plus its source submission issue when available. This is catalogue history, not software release history. Original submission wording is preserved through the source issue and Git revisions; do not rewrite a submitter's issue to imitate the current entry. Use clear commit summaries so subsequent updates are understandable. Full-history checkouts are required for deployment. Older entries without a submission issue start at their first committed catalogue record; no submission or approval event is fabricated.
