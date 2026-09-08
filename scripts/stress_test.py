#!/usr/bin/env python
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def size_mb(path: Path) -> float:
    if path.is_file():
        return path.stat().st_size / 1024 / 1024
    return sum(p.stat().st_size for p in path.rglob('*') if p.is_file()) / 1024 / 1024


def synthetic_tool(i: int) -> dict:
    platform = ['lc_ms', 'gc_ms', 'ce_ms', 'multi_platform'][i % 4]
    function = ['preprocessing', 'annotation_identification', 'statistics', 'quality_control', 'reference_data_search'][i % 5]
    interface = ['web_app', 'desktop_gui', 'r_package', 'python_package', 'command_line'][i % 5]
    slug = f'synthetic-tool-{i:04d}'
    return {
        '$schema': '../../schemas/tool.schema.json',
        'slug': slug,
        'name': f'Synthetic Tool {i:04d}',
        'aliases': [f'SynthTool{i:04d}'],
        'summary': f'Synthetic metabolomics resource {i:04d} used only to stress-test catalogue generation, search indexing, filtering, and page creation.',
        'links': {'primary': f'https://example.org/{slug}'},
        'resource_types': ['software_application'],
        'functions': {'primary': function, 'secondary': [], 'capabilities': []},
        'platforms': [platform],
        'analysis_types': ['untargeted'],
        'interfaces': [interface],
        'access': {'model': 'open_source'},
        'publications': [],
        'common_uses': [],
        'scope': {},
        'acquisition': {},
        'related_tools': [],
        'maintenance': {'status': 'active', 'last_checked': '2026-08-24'},
        'credits': [],
        'provenance': {'submitted_by': 'curator', 'developer_verified': False},
        'status': {'entry': 'published', 'review': 'editorially_reviewed', 'created_at': '2026-08-24', 'updated_at': '2026-08-24', 'last_verified': '2026-08-24'},
    }


def run(cmd, cwd, env=None):
    start = time.perf_counter()
    result = subprocess.run(cmd, cwd=cwd, env=env, text=True, capture_output=True)
    elapsed = time.perf_counter() - start
    if result.returncode:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(result.returncode)
    return elapsed, result.stdout.strip()


def main():
    parser = argparse.ArgumentParser(description='Build a temporary large synthetic catalogue and report static-site scaling metrics.')
    parser.add_argument('--tools', type=int, default=500, help='Number of synthetic tools to add (default: 500)')
    args = parser.parse_args()

    with tempfile.TemporaryDirectory(prefix='metabo-atlas-stress-') as tmp:
        target = Path(tmp) / 'site'
        shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns('dist', '__pycache__', '*.pyc'))
        tools_dir = target / 'content' / 'tools'
        for i in range(args.tools):
            record = synthetic_tool(i)
            (tools_dir / f"{record['slug']}.yml").write_text(yaml.safe_dump(record, sort_keys=False, allow_unicode=True, width=1000), encoding='utf-8')

        validate_time, validation = run(['python3', 'scripts/validate_catalogue.py'], target)
        env = os.environ.copy(); env['BASE_PATH'] = '/metabolomics-navigator'
        build_time, build = run(['python3', 'scripts/build_site.py', '--strict'], target, env=env)
        dist = target / 'dist'
        tools_html = dist / 'tools' / 'index.html'
        tools_json = dist / 'tool-data.json'
        generated_tool_pages = len(list((dist / 'tools').glob('*/index.html')))
        total_tools = generated_tool_pages

        print('Stress-test passed')
        print(f'Synthetic tools added: {args.tools}')
        print(f'Total tool pages generated: {total_tools}')
        print(f'Validation time: {validate_time:.2f} s')
        print(f'Build time: {build_time:.2f} s')
        print(f'Tools catalogue HTML: {size_mb(tools_html):.2f} MB')
        print(f'Tool JSON export: {size_mb(tools_json):.2f} MB')
        print(f'Total generated site: {size_mb(dist):.2f} MB')
        print(validation)
        print(build)


if __name__ == '__main__':
    main()
