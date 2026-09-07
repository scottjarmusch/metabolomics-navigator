# Contributing

Metabolomics Navigator is designed so that researchers can contribute without knowing Git, YAML, or the site architecture.

## Submit a tool

Use the **Submit a metabolomics tool** issue form. A minimal submission needs a name, link, neutral description, resource type, primary function, analytical platform, interface, access model, and submitter relationship. Aliases and alternative spellings are optional but encouraged for discoverability and duplicate detection.

## Submit a protocol

Use the **Submit a metabolomics protocol** issue form. Protocols must be published and transferable, not simply application studies that happen to use metabolomics. Sample type and biological context are optional structured fields that improve discovery.

## What happens after submission

New-tool and new-protocol forms create structured drafts through automation. The **Update an existing tool** and **Update an existing protocol** forms create issues for an editor to review and implement. All GitHub forms require a free account.

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

Follow [the editorial model](docs/tool-editorial-model.md) for coverage, source selection, and verification. The homepage review is organized in `config/guide.yml`; when adding a tool, consider where it belongs in that guide as well as the searchable catalogue.
