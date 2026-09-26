# Education resource — implementation handoff

Goal: add an **Education** resource to Metabolomics Navigator for curated external tutorials, workshop recordings, and practical training videos related to tools already represented in Navigator.

This handoff is intentionally separate from the tool catalogue and analytical-strategy model.

## Product intent

Education should answer:

> “I found the tool. Where can I learn how to use it?”

The first supported resource type is **video tutorial / workshop recording**, especially YouTube content from official tool developers, workshops, training schools, conferences, or established metabolomics community organizations.

Education is **not**:
- a ranking of tutorials;
- a replacement for official documentation;
- a new tool category;
- an endorsement of a software ecosystem;
- a place for generic metabolomics lectures with no practical connection to Navigator content.

## Navigation

Add **Education** to the main header:

Guide · Tools · Strategies · Education · Ask Navigator · About · Contribute

Route:

`/education/`

Also add Education under the footer's Explore section.

## Recommended information architecture

The Education landing page should be searchable/filterable and show tutorial cards.

Primary browsing dimensions:

- Tool
- Format: workshop recording / tutorial / walkthrough / lecture-demo
- Experience level: introductory / intermediate / advanced / mixed
- Scientific function, inherited from linked tool(s)
- Analytical platform, inherited from linked tool(s)
- Provider / workshop
- Year

Do not create tool-specific category taxonomies inside Education when those dimensions can be inherited from existing Navigator tool records.

## Data model principle

Education resources reference Navigator tools using `tool_slugs`.

Example:

```yaml
tool_slugs:
  - mzmine
```

This creates a stable relationship:

Tool → educational resources  
Education resource → tool(s)

A tutorial may reference multiple tools when a workshop genuinely covers an interoperable workflow.

## Initial scope

Phase 1:
- hosted video links, especially YouTube;
- tool-focused workshop recordings;
- official/community tutorials;
- curated metadata;
- no embedded tracking-heavy YouTube iframes by default.

Prefer thumbnail + metadata + “Watch on YouTube” external link. If embedding is introduced later, use privacy-enhanced embeds and do not load third-party content before user interaction.

## Editorial rule

The existence of an education resource does not mean Navigator endorses the method or tool.

Prefer:
1. official developer/maintainer tutorial;
2. established workshop or training-school material;
3. community tutorial with clear authorship and sufficient technical value.

Store provenance and verification dates.

## Package contents

- `IMPLEMENTATION.md` — exact repository changes
- `education.schema.json` — proposed resource schema
- `education.example.yml` — example records using placeholders
- `education.html` — proposed Jinja template
- `CODEX_PROMPT.md` — ready-to-run implementation prompt

No production files outside this handoff directory are modified by this branch.
