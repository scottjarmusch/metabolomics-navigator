# Strategy curation checkpoint — 9 September 2026

Phase 2 is in progress; no new candidate has been published or retired yet.

## Migration follow-up

The Strategy schema still had its retired self-identifier, and both README files linked to obsolete submission forms. The earlier terminology audit removed all URLs before checking them. Corrected these five URLs and made Navigator-owned URLs subject to the audit. Added regression checks for schema URLs, form query parameters and external publication URLs.

## Candidate audit

All 11 supplied Strategy candidates pass the current schema structurally. That does not establish editorial readiness.

Publisher-deposited Crossref metadata confirms two author corrections are required:

- MSI-guided molecular networking: Kuo TH, Huang HC, Hsu CC; DOI 10.1016/j.aca.2019.05.070. The supplied author list is incorrect.
- Stable-isotope labeling and molecular networking: Klitgaard A, Nielsen JB, Frandsen RJN, Andersen MR, Nielsen KF; DOI 10.1021/acs.analchem.5b01934. The supplied author list is incorrect.

Seven candidate DOI/title identities were confirmed through Crossref. Three requests were rate-limited; those are not failed DOI resolutions. The 3D cartography title, authors and 2018 volume/page citation were separately confirmed on the Nature publisher page (online publication was December 2017).

The colony-MALDI IDBac journal paper was subsequently confirmed on the ACS publisher page: DOI 10.1021/acs.jnatprod.6c00765, published 24 August 2026. Its older preprint remains separately indexed; use the final publication.

Chemoselective metabolomics was confirmed in PubMed (42467898), DOI 10.1002/advs.76599, published 17 July 2026.

The OzID candidate cites the LipidOz software paper. PubMed 37076550 identifies the correct authors as Ross DH, Lee J-Y, Bilbao A, et al., DOI 10.1038/s42004-023-00867-9, Communications Chemistry 6, 74 (2023); the supplied Harris attribution is incorrect. Review whether a distinct methodological source should replace it under the Strategy inclusion test.

The official Bioactive Molecular Networks repository confirms MZmine 2 / Optimus inputs, an R-based notebook, GNPS and Cytoscape. Its candidate should clarify historical version/file compatibility and add the missing Cytoscape relationship. A generic MassIVE homepage is insufficient evidence for a dataset-specific raw-data link.

Sources: [IDBac publisher record](https://pubs.acs.org/jnprdf/article/doi/10.1021/acs.jnatprod.6c00765/5324210/MALDI-Tandem-Mass-Spectrometry-for-Colony-Based), [chemoselective paper](https://pubmed.ncbi.nlm.nih.gov/42467898/), [LipidOz paper](https://pubmed.ncbi.nlm.nih.gov/37076550/), [bioactivity workflow repository](https://github.com/DorresteinLaboratory/Bioactive_Molecular_Networks).

## Phase dependencies

Five missing Tool slugs occur across five candidates: `idbac`, `mibig`, `nplinker`, `lipidoz`, `ili`. These Tools belong to later population phases. The existing schema permits named external resources, so use verified external links in Phase 2 where appropriate, record the pending relationships, and convert them to internal links in the later relationship pass. Do not weaken cross-link validation or reorder phases.

Next: finish publication and scope checks; preserve the useful content of the 11 retiring routine workflows on their existing Tool pages; curate the new Strategy records and validate the complete phase before advancing.
