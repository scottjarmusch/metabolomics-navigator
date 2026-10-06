# Enveda batch 3: annotation and prioritization software

This branch is stacked on the QC batch in PR #72. It adds three tools and connects them to existing Strategies; it does not deploy Education or Ask Navigator.

| Candidate | Decision |
|---|---|
| LC-MS2Struct (row 2) | Python software, not a database as proposed in the intake. Requires candidate structures, precomputed spectral scores, retention times and suitable model data. The official implementation supports Linux. Link the existing 2022 implementation in the retention-order Strategy to the new tool record. |
| MS2DECIDE (row 52) | Separate software record linked to the existing community-submitted Strategy. Preserve Morgane Mauduit's original attribution and review status. Document GNPS/SIRIUS/ISDB evidence inputs, account/network requirements, and K-score limitations. |
| ROASMI (row 71) | Neural retention-order software; initial model applicability depends on RPLC/pH. Add the 2025 paper as an extension of the existing retention-order Strategy rather than a new Strategy card. HILIC retraining examples do not imply that initial RPLC models work universally. |

All three official repository license files declare MIT. Documentation and primary-paper metadata were checked on 2026-10-05. No installation, execution or independent benchmarking was performed. Maintenance is not inferred from repository availability. Rankings and scores do not establish compound identity or novelty.

## Sources

- LC-MS2Struct: https://github.com/aalto-ics-kepaco/msms_rt_ssvm and https://github.com/aalto-ics-kepaco/lcms2struct_exp; primary paper https://doi.org/10.1038/s42256-022-00577-2 (2022). The repository cites a preprint; the catalogue cites the journal article.
- MS2DECIDE: https://github.com/MejriY/MS2DECIDE; primary paper https://doi.org/10.1002/cmtd.202400088 (2025, not the year embedded in the DOI).
- ROASMI: https://github.com/FangYuan717/ROASMI; primary paper https://doi.org/10.1186/s13321-025-00968-8 (2025). The journal title supersedes the manuscript title in the README.

The intake ledger now tracks 15 validated candidates across this batch, PR #72 and PR #71. Pending merge does not mean publicly deployed.

## Validation

Schema validation passed for 155 tools and 40 Strategies. The strict build and all CI-equivalent checks passed. After the final cross-link edits, the rebuilt site passed 7,520 local links/fragments, 301 relationships and SEO checks across 216 pages. Explicit rendered-page checks confirmed that all three new tool links appear on the intended Strategy pages. Duplicate DOI checks found no existing tool record for any of the three primary papers.
