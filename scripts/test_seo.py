import json
import unittest
from jinja2 import Environment, FileSystemLoader, select_autoescape
from common import ROOT
from seo import page_metadata
from check_seo import Head


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

    def test_reject_relative_canonical(self):
        with self.assertRaises(ValueError):
            page_metadata('tools.html','tools/',{'site':{'title':'Test','description':'Test'}},lambda p:'/'+p)


if __name__ == '__main__': unittest.main()
