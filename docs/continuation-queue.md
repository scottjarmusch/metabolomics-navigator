# Current continuation order

The user approved continuing and publishing validated work on 11 September 2026.

1. Publish rMSI, rMSIproc and MSiReader: committed as 9317b48.
2. At the next usage reset, prioritize Ask Navigator, as explicitly requested
   on 11 September 2026. This supersedes the earlier full-population gate.
   Start with a newcomer with raw LC-MS/MS files. Use existing curated records
   and verify the tools and relationships used by each enabled path. Keep
   unsupported paths explicit; do not imply the full population is complete.
3. Resume specialist population in phase-4-specialist-checkpoint.md after
   Ask Navigator. Supplied spatial and lipidomics groups are now present;
   remaining groups include networks/visualization, computational annotation,
   metabologenomics, IDBac and RaMP-DB.
4. Return to the 12 remaining GNPS2 entries in phase-3-inventory-status.md and
   MS2LDA enrichment after specialist population.
5. Complete the full relationships, direct access and page-quality review.
6. Reconcile metabolomics_navigator_live_handoff_2026-09-10.zip against main and
   PR #13, then implement the remaining review-derived entries. This package is
   still queued after Ask Navigator and the above catalogue work. LipidOz is
   now on main, reconciled with the candidate in PR #13; retain the canonical
   main record when reviewing that PR's remaining entries.
7. Complete release QA.

The new package has manifests and an existing-card update list, not just new
cards. Its historical files must not overwrite newer repository decisions.
README_IMPLEMENTATION.md was read to establish scope; the remaining files are
to be reviewed when this queue item starts.

Reset-aware continuation is reactivated in the existing three-day automation,
with its original deadline of 12 September 2026 at 15:11 UTC. It must not consume
reserve capacity or create duplicate scheduled tasks.
