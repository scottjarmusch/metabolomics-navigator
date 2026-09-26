# Education — lightweight curated guide

Goal: add **Education** to Metabolomics Navigator as a simple guide to trustworthy external learning resources for tools already represented in Navigator.

Navigator should not become a course platform, video host, or replacement for official documentation.

The product promise is simple:

> **Found a tool? Navigator helps you find good places to learn it.**

## Navigation

Add **Education** to the main header:

Guide · Tools · Strategies · Education · Ask Navigator · About · Contribute

Route:

`/education/`

Also add Education under Footer → Explore.

## What belongs here

Education resources should be practical and clearly attributable:

- official tool tutorials;
- developer or maintainer walkthroughs;
- workshop recordings;
- training-school materials;
- trusted community tutorials;
- hands-on written tutorials;
- official documentation/training hubs.

Avoid:
- generic lectures with no practical tool connection;
- popularity-based recommendations;
- copied tutorial content;
- embedded video hosting;
- rankings such as “best tutorial.”

## Core relationship

Each Education resource points to one or more existing Navigator tools:

```yaml
tool_slugs:
  - mzmine
```

A resource can reference multiple tools when it teaches an actual workflow boundary, for example:

```yaml
tool_slugs:
  - ms-dial
  - ms-finder
```

## Minimal metadata

Each record needs only:

- title
- external URL
- linked tool slug(s)
- provider/source
- resource type
- one-line description
- optional experience level
- optional legacy/currentness note
- lightweight provenance

No duration, thumbnails, video IDs, presenter databases, popularity metrics, or complex topic taxonomy are required for phase 1.

## Resource types

Use a deliberately small vocabulary:

- `video`
- `workshop`
- `tutorial`
- `documentation`
- `training_hub`

These describe how the user learns, not the scientific function.

## Currentness

Use an optional `note` field for important context such as:

- “Uses the MZmine 2 interface; workflow concepts remain useful.”
- “Recorded in 2020; verify current GNPS interface before following step-by-step.”
- “Current official tutorial hub.”

Do not invent a numeric freshness score.

## Display model

The Education page should behave like a guide:

### MZmine

**Data preprocessing in MZmine 3**  
Functional Metabolomics Lab · Workshop  
Hands-on introduction to LC-MS preprocessing.  
[Open resource ↗]

**MZmine Learners Corner**  
MZmine project · Training hub  
Official collection of videos, workshops, and learning material.  
[Open resource ↗]

Resources can be grouped by linked tool and optionally searched.

## Editorial role

Navigator curates and points outward.

The existence of a resource does not imply endorsement of the tool, tutorial, presenter, or analytical approach.

Prefer official and established training material, but include strong community resources when authorship and practical value are clear.

## Seed material already collected

See:

- `education-seed-candidates.tsv`
- `broader-tutorial-leads.tsv`

These contain an initial set from Functional Metabolomics, GNPS, MZmine, MS-DIAL, MetaboAnalyst, OpenMS/pyOpenMS, XCMS, MetFrag, patRoon, Workflow4Metabolomics, MS-FINDER, and related training sources.

No production files outside this handoff directory are modified by this branch.
