# Governance and editorial policy

The Metabolomics Navigator is a community-maintained reference resource for metabolomics tools and transferable protocols. Inclusion records that an entry is within scope; it is not an endorsement, certification, performance ranking, or guarantee of scientific validity.

## Scope and inclusion

The current scope is **MS-based metabolomics**. NMR-only and other non-MS-only tools and protocols are outside scope. Shared reference databases, statistical tools and platforms remain eligible when they support MS metabolomics; entries should describe that use. A platform-independent label alone does not establish eligibility.

### Tools

A tool is in scope when it is a computational, data, analytical, or reference resource that is specifically useful for generating, processing, interpreting, storing, searching, or sharing metabolomics data. This includes software applications, packages, web services, databases, spectral libraries, repositories, workflow systems, APIs, and vendor software.

Historically important or deprecated tools may remain in the catalogue when they are needed to interpret published studies.

### Protocols

A protocol is in scope when it is a published, transferable experimental or computational strategy that addresses a defined metabolomics problem and can reasonably be adapted by another researcher. A paper is not included merely because it used metabolomics; the methodological strategy must itself be reusable or distinctive.

## Verification states

- **Community submitted**: the entry was submitted by a user or community contributor.
- **Developer verified**: a developer or official maintainer confirmed the current tool entry.
- **Author verified**: an author of the underlying protocol publication confirmed the protocol entry.
- **Editorially reviewed**: a Navigator editor checked scope, links, categorization, provenance, neutral wording, and basic metadata.

Verification is not endorsement or independent benchmarking.

## Claims and evidence

Factual metadata, intended scope, requirements, and documented capabilities may be sourced from official documentation, publications, developers, authors, or curators. Comparative claims such as greater accuracy, sensitivity, speed, or superiority require an appropriate independent citation. Unsupported promotional claims are removed or rewritten neutrally.

## Lifecycle and archiving

Tool maintenance is recorded separately from Navigator entry status. Tool lifecycle values are:

- **Actively maintained**
- **Limited or infrequent maintenance**
- **Maintenance status unclear**
- **Archived**
- **Deprecated or superseded**
- **Currently unavailable**

Deprecated and unavailable tools are normally retained rather than deleted when they remain relevant to published research. Successor/predecessor and part-of relationships should be recorded where known.

## Versions

Metabolomics Navigator normally maintains one canonical page per tool rather than one page per software version. The page records the latest known version and release date and may note scientifically important major-version changes. Separate entries should only be created when a successor is functionally a distinct resource.


## Relationship graph

Tool relationships are stored once wherever possible. The site automatically renders safe inverse relationships for symmetric or paired concepts: `alternative` ↔ `alternative`, `complementary` ↔ `complementary`, `integration` ↔ `integration`, `part_of` ↔ `contains`, and `successor` ↔ `predecessor`. Relationships whose inverse would be ambiguous, such as dependencies or generic “uses” links, remain directional. Editors should not add duplicate reverse declarations solely for display.

## Protocol context model

Protocol records use three complementary context fields:

- **Sample types** record specific matrices such as plasma, sputum, tissue, microbial cultures, or environmental samples.
- **Biological contexts** record broad systems such as human, microbial, plant, environmental, or host–microbe interaction.
- **Organisms** provide optional free-text organism names when scientifically useful.

The earlier `sample_contexts` field is retired. New records should use the three fields above. Protocol objectives distinguish the biological or analytical goal, including **Disease-state comparison** and **Host–microbe interaction**.

## Corrections and conflicts

Corrections are accepted through update forms or pull requests. Editors may request citations, neutral wording, or clarification before merging. Conflicts of interest should be disclosed when a submitter is a developer, maintainer, author, vendor, or otherwise directly associated with an entry.

## Publication selection

Tool `publications` contain only papers that introduce the named resource, substantially update it, or describe a method/protocol implemented within it. A shared author, compatible export, mention, or use in a biological study is insufficient. Distinct named components belong on their own tool/protocol pages, linked from the parent. Platform papers may be used when the official citation guidance explicitly covers the component; explain that exception in `note`.

Exclude application-only studies, general reviews and papers introducing other resources from the core bibliography. Application-specific extensions can be evaluated as separate protocol candidates rather than automatically expanding a tool bibliography. Independent benchmarks can inform a qualified comparison, but are not core tool publications. Preserve original credit through links to the actual resource.

Put package records and documentation in `resource_citations`, labelled `software` or `documentation`; a package DOI does not make the record a research article. Keep preprints visibly labelled. An empty scholarly bibliography is acceptable when no dedicated paper is established; explain the citation guidance without inventing a substitute. This is a selected bibliography, not a claim of exhaustive coverage. Protocol sources must introduce the transferable strategy described on that page.

Editors must verify title, DOI, resource identity and the paper's actual contribution before accepting it. Schema validation checks structure and permitted types; it cannot determine scientific relevance.
