# v5 visual redesign upgrade

This package updates the visual design of the Metabolomics Tool Atlas while leaving the working submission, review, validation, and deployment workflows intact.

## Main changes

- cleaner homepage with one dominant search experience
- simplified navigation: Tools, Protocols, About, Submit
- new metabolomics-grounded logo and favicon
- cleaner design system with fewer heavy cards and lighter borders
- refined catalogue, tool-page, and protocol-page presentation
- simplified footer and stronger visual distinction between tools and protocols

## How to apply the update

1. Download and extract the **v5 root update** package.
2. In GitHub, open your repository and go to **Code → Add file → Upload files**.
3. Drag in **everything inside** the extracted root update folder.
4. Commit directly to `main` with a message such as:
   `Apply v5 visual redesign`
5. Wait for **Validate catalogue** and **Deploy catalogue to GitHub Pages** to complete.
6. Refresh your live site.

## Notes

- No `.github` workflow update is required for v5.
- If GitHub asks whether you want to replace existing files, choose the v5 versions.
- The redesign affects styling and templates only; the data model and submission forms remain unchanged.
