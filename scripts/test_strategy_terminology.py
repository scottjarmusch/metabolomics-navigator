"""Regression checks for owned versus external citation URLs."""
import re
import unittest
from audit_strategy_terminology import OLD, strip_external_url

class TerminologyURLTests(unittest.TestCase):
    def clean(self, url):
        return re.sub(r'https?://[^\s<>"\)]+', strip_external_url, url)

    def test_owned_schema_url_is_not_exempt(self):
        url=f'https://scottjarmusch.github.io/metabolomics-navigator/schemas/{OLD}.schema.json'
        self.assertIn(OLD,self.clean(url))

    def test_owned_form_query_is_not_exempt(self):
        url=f'https://github.com/scottjarmusch/metabolomics-navigator/issues/new?template=submit-{OLD}.yml'
        self.assertIn(OLD,self.clean(url))

    def test_external_publication_url_is_preserved_by_audit(self):
        self.assertEqual('',self.clean(f'https://www.nature.com/{OLD}s/article'))

if __name__=='__main__':unittest.main()
