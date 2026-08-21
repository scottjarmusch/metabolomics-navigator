#!/usr/bin/env python
from __future__ import annotations

import sys
from collections import Counter

from common import load_protocols, load_tools, validator


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
    return failed, set(slugs)


def main():
    tools=load_tools(); protocols=load_protocols()
    failed, tool_slugs=validate_records(tools,'tool')
    f2, protocol_slugs=validate_records(protocols,'protocol'); failed=failed or f2

    for record in tools:
        path=record['_path']
        for related in record.get('related_tools',[]):
            if related['slug'] not in tool_slugs:
                failed=True; print(f"ERROR: {path}: related tool '{related['slug']}' does not exist")
        sup=record.get('maintenance',{}).get('superseded_by')
        if sup and sup not in tool_slugs:
            failed=True; print(f"ERROR: {path}: superseded_by tool '{sup}' does not exist")

    for record in protocols:
        path=record['_path']
        for item in record.get('tools',[]):
            slug=item.get('slug')
            if slug and slug not in tool_slugs:
                failed=True; print(f"ERROR: {path}: tool '{slug}' does not exist")
        for step in record.get('workflow_steps',[]):
            for slug in step.get('tool_slugs',[]):
                if slug not in tool_slugs:
                    failed=True; print(f"ERROR: {path}: workflow tool '{slug}' does not exist")
        for slug in record.get('related_protocols',[]):
            if slug not in protocol_slugs:
                failed=True; print(f"ERROR: {path}: related protocol '{slug}' does not exist")

    if failed: return 1
    print(f"Validated {len(tools)} tool records and {len(protocols)} protocol records successfully.")
    return 0

if __name__=='__main__':
    sys.exit(main())
