# Contributing

The easiest contribution route is through the repository's **Issues → New issue** page.

## Submit a tool

Use **Submit a metabolomics tool** for software, packages, databases, spectral libraries, repositories, services, and workflow systems. Only a small set of fields is required. A structured draft is generated automatically for editorial review.

## Submit a protocol

Use **Submit a metabolomics protocol** for a published, transferable experimental or computational strategy that combines metabolomics methods/tools to solve a defined problem. Protocols should be reusable beyond the single study in which they were introduced.

## Suggest an update

Use the relevant update form when an existing entry is outdated or incomplete.

## Direct pull requests

Experienced contributors may edit YAML records directly. Before opening a pull request, run:

```bash
python scripts/validate_catalogue.py
python scripts/check_form_sync.py
python scripts/build_site.py --strict
```

Please describe tools and protocols neutrally. Performance claims should be supported by cited evidence. Developer-submitted information is welcome and is identified through provenance metadata rather than treated as independent endorsement.
