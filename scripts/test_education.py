"""Education review labels and unavailable-resource handling."""
import unittest
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from build_site import education_is_visible

ROOT=Path(__file__).resolve().parents[1]

class EducationTests(unittest.TestCase):
    def test_archived_and_rejected_resources_are_not_recommended(self):
        for status in ['unreviewed','source_checked','validated']:
            self.assertTrue(education_is_visible({'status':{'entry':'published'},'validation_status':status}))
            self.assertFalse(education_is_visible({'status':{'entry':'archived'},'validation_status':status}))
        self.assertFalse(education_is_visible({'status':{'entry':'published'},'validation_status':'rejected'}))

    def test_labels_distinguish_source_checks_from_content_review(self):
        env=Environment(loader=FileSystemLoader(ROOT/'templates'),autoescape=select_autoescape())
        env.globals['url']=lambda p:'/metabolomics-navigator/'+p
        for status,label in [('validated','Reviewed'),('source_checked','Source checked'),('unreviewed','Needs review')]:
            resource={'slug':'example','title':'Example resource','url':'https://example.org','resource_type_label':'Video','provider':'Example provider','summary':'Example learning resource.','tool_slugs':[],'search_text':'example','validation_status':status}
            page=env.get_template('education.html').render(site={},seo={'title':'Education','description':'Learning','robots':'index,follow'},education_resources=[resource],education_tools=[])
            self.assertIn('>'+label+'</span>',page)
            self.assertIn('not watched end to end',page)

    def test_built_directory_matches_visible_records(self):
        from common import load_education
        records=load_education()
        page=(ROOT/'dist/education/index.html').read_text(encoding='utf-8')
        self.assertEqual(page.count('data-education-item'),sum(education_is_visible(r) for r in records))
        for r in records:
            if not education_is_visible(r):
                self.assertNotIn('href="'+r['url']+'"',page)

if __name__=='__main__':unittest.main()
