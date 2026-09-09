# Metabolomics Navigator: tool editorial model

The existing tool entries provide the baseline for future contributions. A complete entry answers a researcher's selection questions; it is not an exhaustive manual or a certification of the software.

## Required coverage

| Question | Source fields |
| --- | --- |
| What is it and where does it fit? | Name, aliases where useful, summary, description, primary function |
| What can I do with it? | Controlled capabilities and concrete common uses |
| What data can I bring and receive? | Input/output types, formats and interface-specific qualifications |
| When is it appropriate? | Designed for, not designed for, requirements, considerations |
| How do I use or obtain it? | Official access link, documentation, interface/platform, access notes |
| What supports the description? | Readable publication citations and explicit documentation sources |
| How current and trustworthy is the entry? | Editorial date and provenance notes, separate from developer verification and operational checks |
| What connects to it? | Scientifically justified existing tool relationships; leave empty when none is appropriate |

Use OpenMS and MetaboAnalyst as general platform examples, SIRIUS and CANOPUS for parent/component distinctions, and MASST and Pan-ReDU for search and infrastructure resources.

## Research and writing

1. Read current official documentation and maintained project repositories. Use primary methods/resource papers for scientific context. Treat access terms, versions and index coverage as dated claims.
2. Write a neutral overview, then capture inputs, outputs and workflow boundaries. Do not imply that every module accepts every listed format; qualify module-dependent interfaces.
3. State the evidence level of an output. A spectral match, class prediction, ranked structure, atom-level localization or pathway association is not interchangeable with experimental confirmation.
4. Keep one record per resource. Use a separate component entry only when it has a distinct reusable scientific identity. Preserve stable slugs and relationships.
5. Identify preprints visibly in citations. Do not fill a publication gap with an unrelated paper. If no dedicated paper is identified, explain how to cite the actual workflow or resource in provenance notes.
6. Do not invent version numbers, release dates, licenses, credits or verification. Preserve historical verification and maintenance dates unless those checks are actually repeated. An editorial review is distinct from running software, a benchmark or developer approval.
7. Validate the record and inspect its generated page. The coverage check cannot assess factual correctness; it is an editorial checklist, separate from the submission schema.

## Validation

```sh
python scripts/validate_catalogue.py
python scripts/check_form_sync.py
python scripts/check_editorial_readiness.py
python scripts/build_site.py --strict
node scripts/test_catalogue.cjs
python scripts/check_site_links.py
```

The source schema and submission forms remain the existing baseline. The additional readiness check is optional for submissions so a useful draft can still enter through the current review process.

## Source trail for this pass

Each YAML record retains its official links and publications. The following sources informed the practical guidance and additions on 6 September 2026; this was not a full systematic literature review or a live execution test.

| Resources | Documentation or primary source |
| --- | --- |
| GNPS | [GNPS2 documentation](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/) |
| MASST, FASST | [MASST guide](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/masst/), [Fast Search API](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/api/) |
| microbeMASST, plantMASST, foodMASST, microbiomeMASST | [Maintained domainMASST repository](https://github.com/robinschmid/microbe_masst), [plantMASST guide](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/plantmasst/), [foodMASST](https://apps.gnps2.org/foodmasst), [microbiomeMASST preprint](https://doi.org/10.64898/2026.02.04.703849) |
| StructureMASST | [Maintained repository](https://github.com/Wang-Bioinformatics-Lab/Structure_MASST_App), [2026 primary paper](https://doi.org/10.1038/s41587-026-03082-8) |
| Pan-ReDU | [ReDU overview](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/ReDU_overview/) |
| GNPS Dashboard | [Documentation](https://ccms-ucsd.github.io/GNPSDocumentation/lcms-dashboard/), [primary paper](https://doi.org/10.1038/s41592-021-01339-5) |
| CMMC-KB | [2026 preprint record](https://pubmed.ncbi.nlm.nih.gov/41659575/) |
| MetaboApps | [App collection and input guidance](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/metaboapps_overview/) |
| MassQL | [Official documentation](https://mwang87.github.io/MassQueryLanguage_Documentation/) |
| ModiFinder | [Official guide](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/modifinder/) |
| MassIVE | [Dataset creation and sharing](https://ccms-ucsd.github.io/GNPSDocumentation/datasets/) |
| MSMS-Chooser | [Workflow documentation](https://ccms-ucsd.github.io/GNPSDocumentation/msmschooser/) |
| SIRIUS, CSI:FingerID, CANOPUS, MSNovelist | [SIRIUS introduction](https://v6.docs.sirius-ms.io/), [methods and algorithms](https://v6.docs.sirius-ms.io/methods-background/) |
| MZmine | [Official documentation](https://mzmine.github.io/mzmine_documentation/), [current product information](https://mzio.io/mzmine/) |
| MS-DIAL | [Official project page and citations](https://systemsomicslab.github.io/compms/msdial/main.html) |
| xcms | [Bioconductor package page](https://bioconductor.org/packages/xcms/) |
| OpenMS | [Official documentation](https://openms.readthedocs.io/), [OpenMS 3 paper](https://doi.org/10.1038/s41592-024-02197-7) |
| MetaboAnalyst | [Official platform](https://www.metaboanalyst.ca/), [MetaboAnalyst 6.0 paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11223798/) |

MassIVE, MSMS-Chooser and MetaboApps have explicit citation exceptions rather than invented dedicated papers. plantMASST, microbiomeMASST and CMMC-KB retain preprint labels for the cited works. Future editors should check whether a version of record supersedes them.

## Reader experience

The homepage is a topic-based review with a table of contents, plain explanations and direct links to tools. Topic prose and selected tool lists live in `config/guide.yml`. Keep titles descriptive, explain unfamiliar concepts in context, and support newcomers without adding slogans or decorative workflow stages. The searchable catalogue remains available for readers who already know what they need.

## Publication selection

Tool `publications` contain only papers that introduce the named resource, substantially update it, or describe a method/strategy implemented within it. A shared author, compatible export, mention, or use in a biological study is insufficient. Distinct named components belong on their own tool/strategy pages, linked from the parent. Platform papers may be used when the official citation guidance explicitly covers the component; explain that exception in `note`.

Exclude application-only studies, general reviews and papers introducing other resources from the core bibliography. Application-specific extensions can be evaluated as separate strategy candidates rather than automatically expanding a tool bibliography. Independent benchmarks can inform a qualified comparison, but are not core tool publications. Preserve original credit through links to the actual resource.

Put package records and documentation in `resource_citations`, labelled `software` or `documentation`; a package DOI does not make the record a research article. Keep preprints visibly labelled. An empty scholarly bibliography is acceptable when no dedicated paper is established; explain the citation guidance without inventing a substitute. This is a selected bibliography, not a claim of exhaustive coverage. Strategy sources must introduce the transferable strategy described on that page.

Editors must verify title, DOI, resource identity and the paper's actual contribution before accepting it. Schema validation checks structure and permitted types; it cannot determine scientific relevance.
