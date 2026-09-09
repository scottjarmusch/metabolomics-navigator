Metabolomics Navigator v5.3.1 migration compatibility patch

Upload the contents of this folder at the ROOT of the GitHub repository.
It replaces scripts/common.py and adds documentation only.
No .github workflow changes are required.

This patch lets legacy v5.2 Strategy records using sample_contexts or host_microbiome load safely under the v5.3 information model.

The old dummy test Strategy should still be deleted from content/strategies because it is not real catalogue content.
