# Education implementation specification

## 1. Add navigation

In `templates/base.html`, add Education between Strategies and Ask Navigator:

```html
<a href="{{ url('education/') }}"{% if active == 'education' %} aria-current="page"{% endif %}>Education</a>
```

Add Education under Footer → Explore.

## 2. Add route and content

Create:

- `content/education/`
- `schemas/education.schema.json`
- `templates/education.html`

Render:

`/education/`

Add the route to sitemap.xml.

## 3. Minimal record model

One YAML file per external learning resource.

Required:
- slug
- title
- summary
- url
- resource_type
- tool_slugs
- provider
- status

Optional:
- experience_level
- note
- provenance

Example:

```yaml
$schema: ../../schemas/education.schema.json
slug: mzmine-learners-corner
title: MZmine Learners Corner
summary: Official collection of MZmine videos, workshops, and practical learning material.
url: https://mzmine.github.io/mzmine_documentation/latest/learners_corner.html
resource_type: training_hub
tool_slugs:
  - mzmine
provider: MZmine project
experience_level: mixed
note: Current official training hub.
provenance:
  submitted_by: curator
  last_checked: '2026-09-26'
status:
  entry: published
```

## 4. Controlled values

### resource_type

- `video`
- `workshop`
- `tutorial`
- `documentation`
- `training_hub`

### experience_level

Optional:
- `introductory`
- `intermediate`
- `advanced`
- `mixed`
- `unspecified`

Experience level describes the resource, not the tool.

## 5. Tool relationships

During the build, resolve `tool_slugs` against existing Navigator tools.

Fail the build if a referenced tool slug does not exist.

Enrich each resource with the resolved tool records.

Build the inverse relationship in memory so tool pages can later expose a “Learn this tool” section without duplicating metadata.

## 6. Education page

Keep it simple.

Heading:

**Education**

Intro:

“Find tutorials, workshops, walkthroughs, and training resources for tools in Metabolomics Navigator.”

Suggested browsing:
- search by resource title, provider, or tool;
- filter by tool;
- optionally filter by resource type.

Do not add elaborate faceting in phase 1.

Group or sort resources primarily by tool name.

Each card/list item should show:
- title;
- provider;
- resource type;
- linked tool(s);
- one-line description;
- optional experience level;
- optional note;
- “Open resource ↗”.

Do not show:
- views;
- likes;
- subscriber counts;
- popularity rank;
- “best” labels.

## 7. External links only

Do not embed YouTube or other third-party content.

Navigator should link out using a normal external link with appropriate `rel` attributes.

No thumbnails are required.

## 8. Currentness

Use the optional `note` field for editorial context.

Examples:
- “Uses MZmine 2; workflow concepts remain useful, but the interface is outdated.”
- “Current official tutorial hub.”
- “Older workshop; check current GNPS interface before following click-by-click instructions.”

Avoid a complex freshness model.

## 9. SEO

Add deterministic metadata in `scripts/seo.py`:

Title:
**Metabolomics Education**

Description:
**Find external tutorials, workshops, walkthroughs, and training resources for metabolomics tools catalogued by Metabolomics Navigator.**

Include the route in the sitemap and normal canonical checks.

## 10. Validation

Validate:
- unique slug;
- unique URL where practical;
- URL is a valid external URI;
- all `tool_slugs` exist;
- resource_type is controlled;
- optional experience_level is controlled;
- required summary/provider fields are present.

No external API is required at build time.

## 11. Seed data

Use the curated handoff files as source material:

- `education-seed-candidates.tsv`
- `broader-tutorial-leads.tsv`

Verify each link before publication and convert strong resources into individual YAML records.

## 12. Future extension

Later, tool pages can show:

**Learn this tool**

with Education links resolved from the shared records.

Do not add hosted courses, progress tracking, accounts, video playback, or complex learning-path functionality unless the product direction explicitly changes.
