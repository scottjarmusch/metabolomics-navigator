# v5.2 pre-population hardening

v5.2 freezes the core information model before broad catalogue population. It adds richer relationships, protocol context fields, clearer governance, duplicate protection, and a scaling test while preserving the existing site design and GitHub review/deployment workflow.

## What changes

### Tools
- aliases are now first-class searchable metadata
- aliases/acronyms are checked for collisions with existing tools
- relationships can describe alternatives, integrations, dependencies, parent/child resources, successors/predecessors, and hosted/contained resources

### Protocols
- optional structured sample types
- optional biological contexts
- optional free-text organism names
- protocol browsing can filter by sample type and biological context

### Governance
- explicit inclusion criteria for tools and protocols
- precise definitions for Community submitted, Developer verified, Author verified, and Editorially reviewed
- verification is explicitly not an endorsement
- comparative performance claims require independent evidence
- lifecycle policy retains archived/deprecated tools for reproducibility
- one canonical page per tool rather than separate pages for routine software versions

### Scaling
- `scripts/stress_test.py` can generate a temporary synthetic catalogue
- the 500-tool test passed successfully

## Safe upload order

v5.2 changes both the public forms in `.github` and the root catalogue schema/validation logic. Upload the form helper first so the repository never enters a state where a new validator expects forms that have not yet been installed.

### Step 1 — GitHub form helper

1. Extract `metabolomics-tool-atlas-v5-2-github-helper.zip`.
2. In GitHub open your repository, then go to **Code → .github**.
3. Choose **Add file → Upload files**.
4. Upload the `ISSUE_TEMPLATE` folder from the helper package.
5. Commit directly to `main` with:
   `Update submission forms for v5.2`

The existing site should continue to validate because the old validator ignores the new optional fields.

### Step 2 — root update

1. Extract `metabolomics-tool-atlas-v5-2-root-update.zip`.
2. Return to the repository root.
3. Choose **Add file → Upload files**.
4. Upload everything inside the extracted folder.
5. Commit directly to `main` with:
   `Apply v5.2 pre-population hardening`
6. Let validation and deployment run automatically.

## Naming

The current package intentionally retains the existing Metabolomics Tool Atlas name and repository path. Rename the project only after a final project name is selected, so naming and URL migration can be handled once rather than repeatedly.
