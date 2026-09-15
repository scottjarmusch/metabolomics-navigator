"""Check editorial coverage, not factual correctness or software availability."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    'description', 'links.documentation', 'functions.capabilities', 'common_uses',
    'scope.designed_for', 'scope.not_designed_for', 'scope.requirements',
    'scope.considerations', 'data.input_types', 'data.output_types',
    'access.notes', 'provenance.notes', 'status.last_editorial_review',
)

def get(record, path):
    value = record
    for key in path.split('.'):
        value = value.get(key) if isinstance(value, dict) else None
    return value

def gaps(record):
    missing = [key for key in REQUIRED if not get(record, key)]
    for direction in ('input', 'output'):
        if not (get(record, f'data.{direction}_formats') or get(record, f'data.other_{direction}_formats')):
            missing.append(f'data.{direction}_formats or explicit interface description')
    if record.get('publications'):
        if any(not pub.get('citation') for pub in record['publications']):
            missing.append('human-readable publication citations')
    elif not record.get('resource_citations') and not any(term in record.get('provenance', {}).get('notes', '').lower() for term in ('no dedicated', 'no single', 'no standalone')):
        missing.append('publication or explicit citation exception')
    return missing

def main():
    failures = []
    pending = 0
    files = sorted((ROOT / 'content/tools').glob('*.yml'))
    for path in files:
        record = yaml.safe_load(path.read_text(encoding='utf-8'))
        if record.get('status', {}).get('entry') == 'stub' and record.get('status', {}).get('review') == 'unreviewed':
            pending += 1
            continue
        missing = gaps(record)
        if missing: failures.append(f'{path.stem}: {", ".join(missing)}')
    if failures:
        print('\n'.join(failures))
        return 1
    print(f'{len(files)-pending} tools meet editorial coverage; {pending} accepted-submission candidates await enrichment. Schema validation remains required for all records.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
