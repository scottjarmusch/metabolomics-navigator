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

The colony-MALDI IDBac candidate has a discoverable preprint, but the proposed journal DOI still needs independent verification. Do not infer that the final paper is absent from a stale preprint index. The OzID candidate lacks a DOI and currently cites a software paper: review whether a distinct methodological source should replace it under the Strategy inclusion test.

## Phase dependencies

Five missing Tool slugs occur across five candidates: `idbac`, `mibig`, `nplinker`, `lipidoz`, `ili`. These Tools belong to later population phases. The existing schema permits named external resources, so use verified external links in Phase 2 where appropriate, record the pending relationships, and convert them to internal links in the later relationship pass. Do not weaken cross-link validation or reorder phases.

Next: finish publication and scope checks; preserve the useful content of the 11 retiring routine workflows on their existing Tool pages; curate the new Strategy records and validate the complete phase before advancing.
