import json
import unittest
from jinja2 import Environment, FileSystemLoader, select_autoescape
from common import ROOT
from seo import page_metadata
from check_seo import Head, VisibleText, expected_home, check_homepage, PRODUCTION_HOME
from unittest.mock import patch
from common import derive_base_path


class SeoTests(unittest.TestCase):
    def test_html_and_json_escaping(self):
        value = 'Research "names" & </script><script>alert(1)</script>'
        context = {'site': {'title': value, 'description': value,
                           'homepage_title': value, 'homepage_description': value},
                   'repository_url': 'https://github.com/example/project'}
        metadata = page_metadata('home.html','',context,lambda path: 'https://example.org/project/'+path)
        env = Environment(loader=FileSystemLoader(ROOT/'templates'),autoescape=select_autoescape(['html']))
        env.globals['url'] = lambda p='': '/project/'+p
        output = env.get_template('base.html').render(**context,seo=metadata)
        parsed = Head(output)
        self.assertEqual(parsed.titles,[value])
        self.assertEqual(parsed.values('meta','name','description'),[value])
        self.assertEqual(json.loads(parsed.ld[0])['@graph'][0]['name'],value)
        self.assertNotIn('<script>alert(1)</script>',output)

    def test_project_canonical_guard(self):
        with patch.dict('os.environ', {'GITHUB_REPOSITORY': 'scottjarmusch/metabolomics-navigator'}, clear=True):
            self.assertEqual(expected_home('https://scottjarmusch.github.io', derive_base_path()), PRODUCTION_HOME)
        for path in ('', '/wrong-project'):
            with self.assertRaisesRegex(AssertionError, 'retain'):
                expected_home('https://scottjarmusch.github.io', path)
        self.assertEqual(expected_home('https://example.org', ''), 'https://example.org/')

    def test_visible_brand_excludes_hidden_content(self):
        html = '<html><head><title>Metabolomics Navigator</title></head><body>'
        for attrs in ('hidden', 'aria-hidden="true"', 'style="display: none"', 'style="visibility:hidden"'):
            html += '<div ' + attrs + '>Metabolomics Navigator</div>'
        html += '<script>Metabolomics Navigator</script><template>Metabolomics Navigator</template><p>Visible text</p></body></html>'
        self.assertEqual(''.join(VisibleText(html).parts), 'Visible text')

    def test_homepage_brand_assertions(self):
        html = (ROOT / 'dist/index.html').read_text(encoding='utf-8')
        head = Head(html)
        check_homepage(head, html, PRODUCTION_HOME)
        head.titles = ['Generic scientific resource']
        with self.assertRaisesRegex(AssertionError, 'title'):
            check_homepage(head, html, PRODUCTION_HOME)
        head = Head(html)
        for _, attrs in head.tags:
            if attrs.get('name') == 'description': attrs['content'] = 'Generic scientific resource'
        with self.assertRaisesRegex(AssertionError, 'description'):
            check_homepage(head, html, PRODUCTION_HOME)
        with self.assertRaisesRegex(AssertionError, 'visible'):
            check_homepage(Head(html), '<body><span hidden>Metabolomics Navigator</span></body>', PRODUCTION_HOME)

    def test_reject_relative_canonical(self):
        with self.assertRaises(ValueError):
            page_metadata('tools.html','tools/',{'site':{'title':'Test','description':'Test'}},lambda p:'/'+p)


if __name__ == '__main__': unittest.main()
