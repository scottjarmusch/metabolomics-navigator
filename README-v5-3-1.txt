Metabolomics Tool Atlas v5.3.1 migration compatibility patch

Upload the contents of this folder at the ROOT of the GitHub repository.
It replaces scripts/common.py and adds documentation only.
No .github workflow changes are required.

This patch lets legacy v5.2 Protocol records using sample_contexts or host_microbiome load safely under the v5.3 information model.

The old dummy test Protocol should still be deleted from content/protocols because it is not real catalogue content.
