# Submission design

## Objective

A researcher should be able to create a useful stub entry in about two minutes without knowing Git, Markdown, YAML, EDAM, or SPDX.

## Required public fields

1. Tool name
2. Best link
3. Neutral one- or two-sentence description
4. Resource type
5. Primary function
6. Supported analytical platform or platform-independent status
7. User interface or access route
8. Access model
9. Submitter relationship

These fields are sufficient to create a page, place it in the catalogue, and support the principal filters.

## Optional public fields

- Secondary functions
- Primary publication or DOI
- Documentation, repository, tutorial, and dataset links
- Submitter name or ORCID for attribution
- Versions, licenses, data formats, limitations, and other notes

## Curator-enriched fields

The following should not burden the initial submitter:

- Stable slug
- Fine-grained capabilities
- Input and output data types
- Controlled data formats
- Operating systems and programming languages
- Maintenance status and release metadata
- External identifiers and EDAM mappings
- Review status
- Related-tool relationships
- Link-check dates

## Provenance labels

Keep these separate rather than treating them as a single review hierarchy:

- Developer submitted: `provenance.submitted_by` is `developer` or `maintainer`.
- Developer verified: `provenance.developer_verified` is `true`.
- Editorially reviewed: `status.review` is `editorially_reviewed`.
- Independently benchmarked: one or more publications have `type: benchmark` and are clearly independent.

## Neutrality policy

Tool entries should describe purpose, access, compatibility, documented capabilities, and sourced limitations. Avoid unsourced superlatives, rankings, star ratings, and claims that a tool is universally superior.
