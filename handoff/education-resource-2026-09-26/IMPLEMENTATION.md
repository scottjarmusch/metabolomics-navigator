# Implementation specification

## 1. Add the route and navigation

### `templates/base.html`

Add between Strategies and Ask Navigator:

```html
<a href="{{ url('education/') }}"{% if active == 'education' %} aria-current="page"{% endif %}>Education</a>
```

Under Footer → Explore add:

```html
<a href="{{ url('education/') }}">Education</a>
```

### `scripts/build_site.py`

Load education records from `content/education/*.yml`, validate them, enrich them with referenced tools, and render:

`dist/education/index.html`

Pass:
- `education_resources`
- `tools`
- filter metadata if implemented client-side

Add `education/` to the sitemap.

## 2. Add data directories

Create:

`content/education/`

and:

`schemas/education.schema.json`

One YAML file per educational resource.

Suggested filename convention:

`<tool-slug>-<short-tutorial-slug>.yml`

Example:

`mzmine-intro-workshop.yml`

## 3. Data model

Required:
- slug
- title
- summary
- url
- format
- tool_slugs
- provider
- provenance
- status

Recommended:
- publication_date
- duration_minutes
- experience_level
- language
- workshop
- presenters
- topics
- notes

### Format vocabulary

Start narrowly:

- `workshop_recording`
- `video_tutorial`
- `software_walkthrough`
- `lecture_demo`

Do not create an unrestricted format vocabulary in phase 1.

### Experience levels

- `introductory`
- `intermediate`
- `advanced`
- `mixed`
- `unspecified`

This describes the tutorial, not the tool.

## 4. Tool relationship

During build:

```python
resource['tools'] = [
    tool_by_slug[slug]
    for slug in resource['tool_slugs']
    if slug in tool_by_slug
]
```

Build must fail if a referenced `tool_slug` does not exist.

This allows cards to show tool names and link directly to Navigator tool pages.

Later, tool pages can gain a “Learn this tool” section by building the inverse index.

## 5. Education landing page

Page heading:

**Education**

Suggested introduction:

“Practical tutorials and workshop recordings for metabolomics tools in Navigator. Education resources are linked to the tools they demonstrate and are provided for learning, not as endorsements or performance rankings.”

Card structure:

- title
- provider / workshop
- format + year
- linked tool chips
- experience level
- short summary
- external CTA: “Watch tutorial”

Filters:
- search
- tool
- experience level
- format

Avoid displaying subscriber counts, view counts, likes, or popularity rankings.

## 6. Video handling

Phase 1 should link externally rather than embed YouTube.

Benefits:
- avoids third-party cookies/tracking on page load;
- simpler static implementation;
- no API dependency;
- fewer stale embed issues.

Optionally store:
- `video_id`
- `thumbnail_url`

but do not require them.

If thumbnails are used, prefer a locally cached editorial thumbnail or a simple neutral card; avoid making remote YouTube image availability a build dependency.

## 7. SEO

### `scripts/seo.py`

Add:

```python
'education.html': (
    'Metabolomics Education',
    'Practical tutorials and workshop recordings for metabolomics tools catalogued by Metabolomics Navigator.'
),
```

The route should have:
- canonical URL;
- index,follow;
- normal Open Graph metadata.

Do not create individual tutorial pages in phase 1 unless there is enough unique editorial content to justify them.

## 8. Build validation

Add checks:
- all records validate;
- all `tool_slugs` exist;
- all external URLs are HTTPS where possible;
- duplicate URLs are rejected;
- duplicate slugs are rejected;
- publication dates use YYYY-MM-DD when known;
- Education appears in sitemap;
- rendered Education page has a canonical.

## 9. Catalogue neutrality

Education sorting should default to:
1. tool name, then
2. publication/workshop date descending, or title

Do not sort by “best,” views, popularity, or Navigator preference.

For multiple tutorials for one tool, show them as alternatives with descriptive metadata.

## 10. Future extension

The schema should leave room for:
- written tutorials;
- workshop exercises;
- notebooks;
- course modules;
- slides;
- recorded webinars.

Do not implement these formats yet unless trivial to support without weakening the first release.
