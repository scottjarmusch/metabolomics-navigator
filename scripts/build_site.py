#!/usr/bin/env python
from __future__ import annotations

import argparse
import html
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlencode

from jinja2 import Environment, FileSystemLoader, select_autoescape

from common import (
    ROOT,
    counts_for,
    date_display,
    derive_base_path,
    label_maps,
    load_tools,
    load_vocab,
    record_date,
    validator,
)

OUT = ROOT / "dist"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base-path",
        default=None,
        help="URL path prefix, e.g. /metabolomics-tool-atlas",
    )
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    vocab = load_vocab()
    labels = label_maps(vocab)
    tools_raw = load_tools()
    check = validator()
    for record in tools_raw:
        path = record.pop("_path")
        errors = list(check.iter_errors(record))
        if errors:
            raise SystemExit(
                f"Cannot build: {path} failed schema validation. "
                "Run scripts/validate_tools.py."
            )

    site = load_yaml(ROOT / "config" / "site.yml")
    github_repository = os.getenv("GITHUB_REPOSITORY", "")
    repository_url = os.getenv(
        "PUBLIC_REPOSITORY_URL", site["repository_url"]
    ).rstrip("/")
    if github_repository and "OWNER" in repository_url:
        repository_url = f"https://github.com/{github_repository}"
    base_path = derive_base_path(args.base_path)
    site_url = os.getenv("SITE_URL", "").rstrip("/")
    if not site_url and github_repository:
        owner, _repo = github_repository.split("/", 1)
        site_url = f"https://{owner.lower()}.github.io"
    generated_at = datetime.now(timezone.utc).strftime("%d %B %Y")

    def url(path: str = "") -> str:
        path = str(path).lstrip("/")
        if not path:
            return f"{base_path}/" if base_path else "/"
        return f"{base_path}/{path}" if base_path else f"/{path}"

    def absolute_url(path: str = "") -> str:
        local = url(path)
        return f"{site_url}{local}" if site_url else local

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(["html", "xml"]),
    )
    env.globals.update(url=url, absolute_url=absolute_url)

    tools = [enrich_tool(record, labels) for record in tools_raw]
    tools.sort(key=lambda item: item["name"].casefold())
    tool_by_slug = {item["slug"]: item for item in tools}

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(ROOT / "assets", OUT / "assets")
    (OUT / "schemas").mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "schemas" / "tool.schema.json", OUT / "schemas" / "tool.schema.json")
    (OUT / "data").mkdir(parents=True, exist_ok=True)
    shutil.copy2(
        ROOT / "data" / "controlled-vocabulary.yml",
        OUT / "data" / "controlled-vocabulary.yml",
    )
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    context = {
        "site": site,
        "repository_url": repository_url,
        "generated_at": generated_at,
    }

    function_counts = counts_for(tools_raw, "functions.primary")
    featured_ids = [
        "preprocessing",
        "quality_control",
        "annotation_identification",
        "spectral_analysis",
        "molecular_networking",
        "statistics",
        "pathway_interpretation",
        "workflow_reproducibility",
    ]
    icons = {
        "preprocessing": "⌁",
        "quality_control": "✓",
        "annotation_identification": "◇",
        "spectral_analysis": "∿",
        "molecular_networking": "⌘",
        "statistics": "∑",
        "pathway_interpretation": "↗",
        "workflow_reproducibility": "⟳",
    }
    functions_by_id = {item["id"]: item for item in vocab["functions"]}
    featured = [
        {
            **functions_by_id[item_id],
            "count": function_counts[item_id],
            "icon": icons[item_id],
        }
        for item_id in featured_ids
    ]
    recent = sorted(
        tools,
        key=lambda item: (item["created_at"], item["name"]),
        reverse=True,
    )[:5]
    stats = {
        "tools": len(tools),
        "functions": len(vocab["functions"]),
        "platforms": len(vocab["platforms"]),
        "developer_verified": sum(
            bool(item["provenance"].get("developer_verified")) for item in tools
        ),
    }
    render(
        env,
        "home.html",
        OUT / "index.html",
        **context,
        active="home",
        stats=stats,
        featured_functions=featured,
        recent_tools=recent,
    )

    filters = [
        make_filter(
            "function",
            "Scientific function",
            "functions",
            vocab["functions"],
            function_counts,
        ),
        make_filter(
            "platforms",
            "Analytical platform",
            "platforms",
            vocab["platforms"],
            counts_for(tools_raw, "platforms"),
        ),
        make_filter(
            "interfaces",
            "Interface",
            "interfaces",
            vocab["interfaces"],
            counts_for(tools_raw, "interfaces"),
        ),
        make_filter(
            "access",
            "Access model",
            "access models",
            vocab["access_models"],
            counts_for(tools_raw, "access.model"),
        ),
        make_filter(
            "resourceTypes",
            "Resource type",
            "resource types",
            vocab["resource_types"],
            counts_for(tools_raw, "resource_types"),
        ),
    ]
    render(
        env,
        "tools.html",
        OUT / "tools" / "index.html",
        **context,
        active="tools",
        tools=tools,
        filters=filters,
    )

    for tool in tools:
        explicit = [
            tool_by_slug[item["slug"]]
            for item in tool.get("related_tools", [])
            if item["slug"] in tool_by_slug
        ]
        if explicit:
            related = explicit[:4]
        else:
            related = [
                item
                for item in tools
                if item["slug"] != tool["slug"]
                and item["functions"]["primary"] == tool["functions"]["primary"]
            ][:4]
        query = urlencode(
            {
                "template": "update-tool.yml",
                "title": f"[Tool update]: {tool['name']}",
            }
        )
        update_url = f"{repository_url}/issues/new?{query}"
        source_url = (
            f"{repository_url}/blob/main/content/tools/{quote(tool['slug'])}.yml"
        )
        render(
            env,
            "tool.html",
            OUT / "tools" / tool["slug"] / "index.html",
            **context,
            active="tools",
            tool=tool,
            related_tools=related,
            update_url=update_url,
            source_url=source_url,
        )

    sections = [
        browse_section(
            "Scientific functions",
            "The main analytical or research task a resource supports.",
            "function",
            vocab["functions"],
            function_counts,
        ),
        browse_section(
            "Analytical platforms",
            "The acquisition technologies or platform-independent data supported.",
            "platforms",
            vocab["platforms"],
            counts_for(tools_raw, "platforms"),
        ),
        browse_section(
            "Interfaces",
            "How a researcher interacts with or runs the resource.",
            "interfaces",
            vocab["interfaces"],
            counts_for(tools_raw, "interfaces"),
        ),
        browse_section(
            "Resource types",
            "The kind of software, service, database, library, or infrastructure represented.",
            "resourceTypes",
            vocab["resource_types"],
            counts_for(tools_raw, "resource_types"),
        ),
    ]
    render(
        env,
        "browse.html",
        OUT / "browse" / "index.html",
        **context,
        active="browse",
        sections=sections,
    )

    submit_query = urlencode(
        {"template": "submit-tool.yml", "title": "[Tool submission]: "}
    )
    update_query = urlencode(
        {"template": "update-tool.yml", "title": "[Tool update]: "}
    )
    required_fields = [
        "Tool name",
        "Best link",
        "Short neutral description",
        "Resource type",
        "Primary function",
        "Analytical platform",
        "Interface",
        "Access model",
        "Your relationship to the tool",
    ]
    render(
        env,
        "submit.html",
        OUT / "submit" / "index.html",
        **context,
        active="submit",
        required_fields=required_fields,
        submission_url=f"{repository_url}/issues/new?{submit_query}",
        update_form_url=f"{repository_url}/issues/new?{update_query}",
    )

    pages = static_pages(repository_url, url)
    for slug, page in pages.items():
        render(
            env,
            "static.html",
            OUT / slug / "index.html",
            **context,
            active=page.get("active", ""),
            page=page,
        )
    render(env, "404.html", OUT / "404.html", **context, active="")

    export = [
        {key: value for key, value in record.items() if not key.startswith("_")}
        for record in tools_raw
    ]
    (OUT / "tool-data.json").write_text(
        json.dumps(export, indent=2, ensure_ascii=False, default=str) + "\n",
        encoding="utf-8",
    )
    write_sitemap(OUT, tools, absolute_url)
    (OUT / "robots.txt").write_text(
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {absolute_url('sitemap.xml')}\n",
        encoding="utf-8",
    )
    print(
        f"Built {len(tools)} tool pages in {OUT} "
        f"with base path '{base_path or '/'}'."
    )


def load_yaml(path: Path):
    import yaml

    return yaml.safe_load(path.read_text(encoding="utf-8"))


def make_filter(key, label, all_label, options, counts):
    return {
        "key": key,
        "label": label,
        "all_label": all_label,
        "options": [
            {**item, "count": counts[item["id"]]}
            for item in options
            if counts[item["id"]] > 0
        ],
    }


def browse_section(title, description, param, items, counts):
    return {
        "title": title,
        "description": description,
        "param": param,
        "items": [
            {**item, "count": counts[item["id"]]}
            for item in items
        ],
    }


def enrich_tool(record, labels):
    tool = dict(record)
    status = tool.get("status", {})
    maintenance = tool.get("maintenance", {})
    data = tool.get("data", {}) or {}
    access = tool.get("access", {})
    provenance = tool.get("provenance", {})

    tool["created_at"] = record_date(tool, "created_at")
    tool["updated_at"] = record_date(tool, "updated_at")
    tool["updated_display"] = date_display(tool["updated_at"])
    tool["primary_function_label"] = labels["functions"].get(
        tool["functions"]["primary"], tool["functions"]["primary"]
    )
    tool["secondary_function_labels"] = [
        labels["functions"].get(item, item)
        for item in tool["functions"].get("secondary", [])
    ]
    tool["capability_labels"] = [
        labels["capabilities"].get(item, item)
        for item in tool["functions"].get("capabilities", [])
    ]
    tool["resource_type_labels"] = [
        labels["resource_types"].get(item, item) for item in tool["resource_types"]
    ]
    tool["platform_labels"] = [
        labels["platforms"].get(item, item) for item in tool["platforms"]
    ]
    tool["interface_labels"] = [
        labels["interfaces"].get(item, item) for item in tool["interfaces"]
    ]
    tool["analysis_type_labels"] = [
        labels["analysis_types"].get(item, item)
        for item in tool.get("analysis_types", [])
    ]
    tool["access_label"] = labels["access_models"].get(
        access["model"], access["model"]
    )
    tool["maintenance_label"] = labels["maintenance_statuses"].get(
        maintenance.get("status", "unclear"), "Not assessed"
    )
    tool["entry_status_label"] = labels["entry_statuses"].get(
        status["entry"], status["entry"]
    )
    tool["input_type_labels"] = [
        labels["common_data_types"].get(item, item)
        for item in data.get("input_types", [])
    ]
    tool["output_type_labels"] = [
        labels["common_data_types"].get(item, item)
        for item in data.get("output_types", [])
    ]
    tool["input_format_labels"] = [
        labels["common_data_formats"].get(item, item)
        for item in data.get("input_formats", [])
    ] + data.get("other_input_formats", [])
    tool["output_format_labels"] = [
        labels["common_data_formats"].get(item, item)
        for item in data.get("output_formats", [])
    ] + data.get("other_output_formats", [])

    role = provenance.get("submitted_by", "other")
    tool["provenance_label"] = {
        "developer": "Developer submitted",
        "maintainer": "Maintainer submitted",
        "user": "Community submitted",
        "curator": "Curator submitted",
        "other": "Community submitted",
    }.get(role, "Community submitted")
    tool["card_badges"] = (
        tool["platform_labels"][:2]
        + tool["interface_labels"][:1]
        + [tool["access_label"]]
    )[:4]
    tool["page_badges"] = (
        tool["platform_labels"]
        + tool["interface_labels"]
        + [tool["access_label"]]
    )[:8]

    link_names = {
        "primary": "Primary access",
        "homepage": "Homepage",
        "web_app": "Web application",
        "repository": "Source repository",
        "documentation": "Documentation",
        "download": "Download",
        "tutorial": "Tutorial",
        "issue_tracker": "Issue tracker",
        "biotools": "bio.tools record",
        "workflowhub": "WorkflowHub record",
    }
    seen = set()
    display_links = []
    for key, href in tool["links"].items():
        if href in seen:
            continue
        seen.add(href)
        display_links.append(
            (link_names.get(key, key.replace("_", " ").title()), href)
        )
    tool["display_links"] = display_links

    search_parts = [
        tool["name"],
        tool.get("acronym", ""),
        tool["summary"],
        tool["primary_function_label"],
        *tool["secondary_function_labels"],
        *tool["capability_labels"],
        *tool["platform_labels"],
        *tool["interface_labels"],
        *tool["analysis_type_labels"],
        tool["access_label"],
        *tool["input_format_labels"],
        *tool["output_format_labels"],
    ]
    tool["search_text"] = " ".join(str(item) for item in search_parts).lower()
    return tool


def render(env, template, destination, **context):
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        env.get_template(template).render(**context),
        encoding="utf-8",
    )


def static_pages(repository_url, url):
    about = f"""
<h2>Purpose</h2>
<p>The Metabolomics Tool Atlas is a living encyclopedia of the resources researchers use to design, process, annotate, interpret, and share metabolomics studies.</p>
<p>It is designed to answer a practical question: <strong>Which tools could help me perform this task, and what should I know before choosing one?</strong></p>
<h2>What the catalogue includes</h2>
<ul><li>Software applications and programming packages</li><li>Web services, APIs, and workflow platforms</li><li>Databases, knowledgebases, spectral libraries, and repositories</li><li>Executable pipelines and reproducibility resources</li></ul>
<h2>What inclusion means</h2>
<p>Inclusion documents that a resource exists and falls within scope. It is not an endorsement, certification, or ranking.</p>
<h2>Open project</h2>
<p>Every entry is stored as a versioned YAML record. The public catalogue, review history, and machine-readable data are generated from the same source.</p>
<p><a href="{repository_url}">View the repository on GitHub</a>.</p>
"""
    contribute = f"""
<h2>Three ways to contribute</h2>
<h3>1. Submit a missing tool</h3>
<p>Use the short submission form. A researcher only needs to provide the information required to create and categorize a stub page.</p>
<p><a class="button primary" href="{url('submit/')}">Submit a tool</a></p>
<h3>2. Improve an existing page</h3>
<p>Each tool page has a <strong>Suggest an update</strong> link. Corrections, new documentation, publications, versions, formats, and developer verification are welcome.</p>
<h3>3. Work directly in GitHub</h3>
<p>Experienced contributors can edit YAML records and open pull requests. Validation checks the metadata before an entry can be merged.</p>
<div class="callout"><strong>Neutrality:</strong> describe documented capabilities and sourced limitations. Avoid promotional language, unsourced performance claims, and universal “best tool” statements.</div>
<h2>Review labels</h2>
<ul><li><strong>Developer submitted:</strong> the original information came from a developer or maintainer.</li><li><strong>Developer verified:</strong> a named developer reviewed the current entry.</li><li><strong>Editorially reviewed:</strong> an editor checked scope, categorization, links, and neutral presentation.</li><li><strong>Independently benchmarked:</strong> an independent comparative publication is linked.</li></ul>
<p><a href="{repository_url}/blob/main/CONTRIBUTING.md">Read the full contribution guide</a>.</p>
"""
    governance = f"""
<h2>Editorial model</h2>
<p>The catalogue separates provenance, editorial review, and independent benchmarking. These describe different kinds of trust and should not be collapsed into one score.</p>
<h2>Routine decisions</h2>
<p>New entries and corrections are reviewed through GitHub pull requests. Editors check fit, categorization, factual presentation, links, and conflicts of interest.</p>
<h2>Conflicts of interest</h2>
<p>Developers may submit and verify their own pages, but another editor should review substantial evaluative claims. Commercial access must be clearly identified.</p>
<h2>Archiving</h2>
<p>Unavailable, deprecated, and superseded tools are normally retained with an archived status so that old publications and workflows remain understandable.</p>
<p><a href="{repository_url}/blob/main/GOVERNANCE.md">Read the repository governance file</a>.</p>
"""
    return {
        "about": {
            "title": "About the atlas",
            "eyebrow": "Project",
            "description": "A transparent, community-maintained map of the metabolomics tool landscape.",
            "body": about,
        },
        "contribute": {
            "title": "Contribute",
            "eyebrow": "Community",
            "description": "Add a tool, improve an entry, or help maintain the controlled vocabulary.",
            "body": contribute,
            "active": "contribute",
        },
        "governance": {
            "title": "Governance and review",
            "eyebrow": "Trust and transparency",
            "description": "How entries are reviewed, attributed, corrected, and archived.",
            "body": governance,
        },
    }


def write_sitemap(out, tools, absolute_url):
    paths = [
        "",
        "tools/",
        "browse/",
        "submit/",
        "about/",
        "contribute/",
        "governance/",
    ] + [f"tools/{item['slug']}/" for item in tools]
    xml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path in paths:
        xml.append(f"  <url><loc>{html.escape(absolute_url(path))}</loc></url>")
    xml.append("</urlset>")
    (out / "sitemap.xml").write_text("\n".join(xml) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
