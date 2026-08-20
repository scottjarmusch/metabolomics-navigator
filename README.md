# Metabolomics Tool Atlas

A community-maintained, Wikipedia-style catalogue of software, databases, spectral libraries, repositories, web services, and workflow resources used in metabolomics.

The site is built from small YAML records. Researchers can submit a tool through a short GitHub form; automation converts the submission into a draft entry and opens a pull request for editorial review. 

## What is included

- Searchable and filterable catalogue
- Permanent encyclopedia page for every tool
- Browse pages organized by scientific function and analytical platform
- Two-minute researcher submission form
- Automated issue-to-YAML draft generation
- JSON Schema validation and controlled vocabularies
- GitHub Pages build and deployment workflows
- Machine-readable `tool-data.json` export
- Eight starter entries demonstrating the catalogue structure

## Local preview

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/build_site.py
python -m http.server 8000 --directory dist
```

Open `http://localhost:8000`.

## Publish on GitHub Pages

1. Create an empty public GitHub repository.
2. This copy is already configured for `scottjarmusch/metabolomics-tool-atlas`. No local configuration step is required.
3. Upload or push the files to the `main` branch.
4. In **Settings → Pages**, select **GitHub Actions** as the source.
5. Create the labels listed in `docs/github-setup.md`.
6. Push the changes. The deployment workflow will build and publish the site.

The build automatically detects the repository name and adds the correct GitHub Pages base path.

## Add a tool manually

Copy an existing YAML file in `content/tools/`, change the values, and run:

```bash
python scripts/validate_tools.py
python scripts/build_site.py
```

## Repository design

```text
content/tools/                 Tool records
schemas/tool.schema.json       Machine validation rules
data/controlled-vocabulary.yml Stable categories and labels
templates/                     Site templates
assets/                        CSS and browser-side search/filter code
scripts/                       Build, validation, and submission automation
.github/ISSUE_TEMPLATE/        Public submission and update forms
.github/workflows/             Validation, draft generation, and deployment
```

## Editorial principle

Entries describe a tool's purpose, access, compatibility, documented capabilities, and sourced limitations. The catalogue does not rank tools or declare a universal “best” option.

## Attribution

The original idea was inspired by the open, collaborative publishing model of the [Comprehensive Overview of Bottom-Up Proteomics using Mass Spectrometry](https://jessegmeyerlab.github.io/proteomics-tutorial/). This repository uses original code, structure, and metabolomics-focused content.

## Licensing

- Code: MIT License, see `LICENSE-CODE`
- Catalogue text and metadata: CC BY 4.0, see `LICENSE-CONTENT`

