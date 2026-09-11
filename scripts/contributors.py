"""Explicit public-attribution consent shared by submission converters and builds."""
import re
import unicodedata

ORCID_PATTERN = r"0000-000[0-9]-[0-9]{4}-[0-9]{3}[0-9X]"
CONSENT_TEXT = (
    "I consent to Metabolomics Navigator publishing my name and, if provided, my ORCID iD in the public Contributor Directory. "
    "I understand that this submission is made through a public GitHub issue and that the information I enter in this form "
    "will also be publicly visible on GitHub. I have read the [Metabolomics Navigator Privacy Policy]"
    "(https://scottjarmusch.github.io/metabolomics-navigator/privacy/)."
)


def parse_attribution(sections):
    name = ' '.join(sections.get('Contributor name', '').split())
    orcid = sections.get('ORCID iD', '').strip()
    if orcid in ('_No response_', 'No response'):
        orcid = ''
    if not name or name in ('_No response_', 'No response') or '@' in name:
        raise ValueError('Contributor name is required and must not contain an email address')
    if orcid and not re.fullmatch(ORCID_PATTERN, orcid):
        raise ValueError('ORCID iD must use the format 0000-0000-0000-0000')
    checked = sections.get('Contributor attribution and privacy', '')
    if not any(re.fullmatch(r'\s*[-*] \[[xX]\] ' + re.escape(CONSENT_TEXT) + r'\s*', line)
               for line in checked.splitlines()):
        raise ValueError('Explicit Contributor Directory consent is required for this public submission route')
    result = {'submitter_name': name, 'public_attribution_consent': True}
    if orcid:
        result['submitter_orcid'] = orcid
    return result


def build_contributors(records):
    rows = []
    for record in records:
        if record.get('status', {}).get('entry') != 'published':
            continue
        p = record.get('provenance') or {}
        if p.get('public_attribution_consent') is not True:
            continue
        name = ' '.join((p.get('submitter_name') or '').split())
        orcid = (p.get('submitter_orcid') or '').strip()
        if not name or '@' in name or (orcid and not re.fullmatch(ORCID_PATTERN, orcid)):
            continue
        normalized = unicodedata.normalize('NFKC', name).casefold()
        rows.append((name, normalized, orcid))
    # Merge a name-only credit with an identified credit only if the name is unambiguous.
    name_ids = {}
    for _, normalized, orcid in rows:
        if orcid:
            name_ids.setdefault(normalized, set()).add(orcid)
    people = {}
    for name, normalized, orcid in sorted(rows):
        ids = name_ids.get(normalized, set())
        identity = orcid or (next(iter(ids)) if len(ids) == 1 else '')
        key = ('orcid', identity) if identity else ('name', normalized)
        person = people.setdefault(key, {'name': name, 'orcid': identity or None, 'contributions': 0})
        person['contributions'] += 1
    return sorted(people.values(), key=lambda x: x['name'].casefold())
