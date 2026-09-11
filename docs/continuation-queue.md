# Current continuation order

The user approved continuing and publishing validated work on 11 September 2026.

1. Publish rMSI, rMSIproc and MSiReader: committed as 9317b48.
2. Complete the GNPS2 inventory in phase-3-inventory-status.md and MS2LDA enrichment.
3. Complete specialist population in phase-4-specialist-checkpoint.md.
4. Complete relationships, direct access and page-quality review.
5. Implement Ask Navigator only after those gates pass.
6. Reconcile metabolomics_navigator_live_handoff_2026-09-10.zip against main and
   PR #13, then implement the remaining review-derived entries. This package is
   explicitly queued after task 5, not an instruction to supersede current work.
7. Complete release QA.

The new package has manifests and an existing-card update list, not just new
cards. Its historical files must not overwrite newer repository decisions.
README_IMPLEMENTATION.md was read to establish scope; the remaining files are
to be reviewed when this queue item starts.

Reset-aware continuation is reactivated in the existing three-day automation,
with its original deadline of 12 September 2026 at 15:11 UTC. It must not consume
reserve capacity or create duplicate scheduled tasks.
