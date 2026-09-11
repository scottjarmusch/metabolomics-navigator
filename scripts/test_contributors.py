"""Regression checks for consent, attribution and the rendered directory."""
import unittest
from pathlib import Path
import json
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jsonschema import Draft202012Validator
from contributors import CONSENT_TEXT, build_contributors, parse_attribution

ROOT = Path(__file__).resolve().parents[1]


def record(name='Jane Doe', orcid=None, consent=True, status='published'):
    p = {'submitter_name': name, 'public_attribution_consent': consent}
    if orcid:
        p['submitter_orcid'] = orcid
    return {'provenance': p, 'status': {'entry': status}}


class ContributorTests(unittest.TestCase):
    def test_consent_and_legacy(self):
        records = [record(), record('False', consent=False), record('String', consent='true'),
                   record('Draft', status='stub'), {'provenance': {'submitter_name': 'Legacy'}}]
        self.assertEqual([p['name'] for p in build_contributors(records)], ['Jane Doe'])

    def test_identity_and_sorting(self):
        oid = '0000-0002-1825-0097'
        people = build_contributors([record('Zoe'), record(' Jane  Doe ', oid),
                                     record('jane doe'), record('J. Doe', oid)])
        self.assertEqual(len(people), 2)
        self.assertEqual(people[0]['orcid'], oid)
        self.assertEqual(people[0]['contributions'], 3)

    def test_shared_name_does_not_merge_distinct_orcids(self):
        people = build_contributors([record('Jane Doe', '0000-0002-1825-0097'),
                                     record('Jane Doe', '0000-0001-2345-678X')])
        self.assertEqual(len(people), 2)

    def test_parser_matches_actual_forms(self):
        for kind in ('tool', 'strategy'):
            form = yaml.safe_load((ROOT / f'.github/ISSUE_TEMPLATE/submit-{kind}.yml').read_text(encoding='utf-8'))
            fields = {x['id']: x for x in form['body'] if 'id' in x}
            self.assertTrue(fields['submitter-name']['validations']['required'])
            option = fields['contributor-consent']['attributes']['options'][0]
            self.assertTrue(option['required'])
            self.assertEqual(option['label'], CONSENT_TEXT)
            sections = {'Contributor name': 'Jane Doe', 'ORCID iD': '0000-0002-1825-0097',
                        'Contributor attribution and privacy': '- [X] ' + option['label']}
            self.assertEqual(parse_attribution(sections)['submitter_orcid'], '0000-0002-1825-0097')
            for checkbox in ('- [ ] ', ''):
                sections['Contributor attribution and privacy'] = checkbox + option['label']
                with self.assertRaises(ValueError):
                    parse_attribution(sections)

    def test_invalid_identity(self):
        for name, oid in [('Jane Doe', 'https://orcid.org/0000-0002-1825-0097'),
                          ('Jane Doe', 'invalid'), ('', ''), ('person@example.org', '')]:
            with self.assertRaises(ValueError):
                parse_attribution({'Contributor name': name, 'ORCID iD': oid,
                                   'Contributor attribution and privacy': '- [x] ' + CONSENT_TEXT})
        self.assertEqual(build_contributors([record('person@example.org'), record(orcid='bad')]), [])

    def test_schemas_optional_boolean(self):
        for kind in ('tool', 'strategy'):
            schema = json.loads((ROOT / f'schemas/{kind}.schema.json').read_text())
            provenance = schema['properties']['provenance']
            self.assertNotIn('public_attribution_consent', provenance.get('required', []))
            field = provenance['properties']['public_attribution_consent']
            self.assertFalse(field['default'])
            self.assertTrue(list(Draft202012Validator(field).iter_errors('true')))
            self.assertFalse(list(Draft202012Validator(field).iter_errors(True)))

    def test_rendering_escapes_identity(self):
        env = Environment(loader=FileSystemLoader(ROOT / 'templates'), autoescape=select_autoescape())
        env.globals['url'] = lambda p: '/metabolomics-navigator/' + p
        html = env.get_template('submit.html').render(site={}, contributors=[
            {'name': '<script>alert(1)</script>', 'orcid': '0000-0002-1825-0097'}])
        self.assertNotIn('<script>alert(1)</script>', html)
        self.assertIn('https://orcid.org/0000-0002-1825-0097', html)
        self.assertIn('Right to erasure.', html)
        self.assertIn('/metabolomics-navigator/privacy/', html)

    def test_built_routes(self):
        for route in ('submit', 'contribute'):
            html = (ROOT / f'dist/{route}/index.html').read_text(encoding='utf-8')
            self.assertIn('id="contributors-heading"', html)
            self.assertIn('Right to erasure.', html)
        self.assertTrue((ROOT / 'dist/privacy/index.html').exists())
        self.assertIn('/privacy/', (ROOT / 'dist/sitemap.xml').read_text())
        self.assertIn('>Privacy</a>', (ROOT / 'dist/index.html').read_text(encoding='utf-8'))

    def test_privacy_form(self):
        html = (ROOT / 'dist/privacy/index.html').read_text(encoding='utf-8')
        self.assertIn('action="https://formspree.io/f/maeyvljl" method="post"', html)
        self.assertIn('name="email" type="email"', html)
        self.assertIn('name="message"', html)
        self.assertNotIn('TODO BEFORE PUBLICATION', html)
        self.assertNotIn('mailto:', html)
        self.assertNotIn('@', html)


if __name__ == '__main__':
    unittest.main()
