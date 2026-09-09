#!/usr/bin/env python
from __future__ import annotations

import sys
import re
from collections import Counter

from common import load_strategies, load_tools, validator


def format_path(path):
    return ".".join(str(p) for p in path) or "<root>"


def validate_records(records, kind):
    check = validator(kind)
    failed = False
    slugs=[]; names=[]
    for record in records:
        path=record['_path']
        clean={k:v for k,v in record.items() if k!='_path'}
        errors=sorted(check.iter_errors(clean), key=lambda e:list(e.absolute_path))
        if errors:
            failed=True; print(f"ERROR: {path}")
            for error in errors:
                print(f"  {format_path(error.absolute_path)}: {error.message}")
        slugs.append(record.get('slug')); names.append((record.get('name') or '').casefold())
    for label,values in (("slug",slugs),("name",names)):
        dup=[v for v,c in Counter(values).items() if v and c>1]
        if dup:
            failed=True; print(f"ERROR: duplicate {kind} {label}(s): {', '.join(dup)}")
    if kind == 'tool':
        def norm(value): return re.sub(r'[^a-z0-9]+','',(value or '').casefold())
        seen={}
        for record in records:
            labels=[record.get('name',''), record.get('acronym',''), *record.get('aliases',[])]
            for label in labels:
                key=norm(label)
                if not key: continue
                previous=seen.get(key)
                if previous and previous != record.get('slug'):
                    failed=True; print(f"ERROR: tool name/alias collision '{label}' between '{previous}' and '{record.get('slug')}'")
                else: seen[key]=record.get('slug')
    return failed, set(slugs)


def main():
    tools=load_tools(); strategies=load_strategies()
    failed, tool_slugs=validate_records(tools,'tool')
    f2, strategy_slugs=validate_records(strategies,'strategy'); failed=failed or f2

    for record in tools:
        path=record['_path']
        seen_related=set()
        for related in record.get('related_tools',[]):
            target=related['slug']
            if target not in tool_slugs:
                failed=True; print(f"ERROR: {path}: related tool '{target}' does not exist")
            if target == record.get('slug'):
                failed=True; print(f"ERROR: {path}: a tool cannot relate to itself")
            if target in seen_related:
                failed=True; print(f"ERROR: {path}: duplicate related tool '{target}'")
            seen_related.add(target)
        sup=record.get('maintenance',{}).get('superseded_by')
        if sup and sup not in tool_slugs:
            failed=True; print(f"ERROR: {path}: superseded_by tool '{sup}' does not exist")

    for record in strategies:
        path=record['_path']
        for item in record.get('tools',[]):
            slug=item.get('slug')
            if slug and slug not in tool_slugs:
                failed=True; print(f"ERROR: {path}: tool '{slug}' does not exist")
        for step in record.get('workflow_steps',[]):
            for slug in step.get('tool_slugs',[]):
                if slug not in tool_slugs:
                    failed=True; print(f"ERROR: {path}: workflow tool '{slug}' does not exist")
        for slug in record.get('related_strategies',[]):
            if slug not in strategy_slugs:
                failed=True; print(f"ERROR: {path}: related strategy '{slug}' does not exist")

    if failed: return 1
    print(f"Validated {len(tools)} tool records and {len(strategies)} strategy records successfully.")
    return 0

if __name__=='__main__':
    sys.exit(main())
