"""Missing implementation references must fail, rather than disappear in rendered pages."""
import contextlib
import io
import unittest
from unittest.mock import patch
import validate_catalogue as catalogue

class ImplementationReferenceTests(unittest.TestCase):
    def test_step_alternatives_use_catalogue_functions(self):
        from build_site import enrich_strategy
        from common import label_maps, load_vocab, load_tools, load_strategies
        tools={t['slug']: t for t in load_tools()}
        labels=label_maps(load_vocab())
        record=next(r for r in load_strategies() if r['slug']=='feature-level-pathway-inference')
        result=enrich_strategy(record, labels, tools)
        self.assertEqual(result['workflow_steps_enriched'][0]['alternative_functions'], [])
        self.assertEqual(result['workflow_steps_enriched'][1]['alternative_functions'][0]['id'], 'pathway_interpretation')

    def test_missing_tool_is_rejected(self):
        records = catalogue.load_strategies()
        records[0].setdefault('implementations', []).append({
            'title': 'Test implementation', 'doi': '10.1000/test',
            'tool_slugs': ['missing-regression-tool'],
        })
        with patch.object(catalogue, 'load_strategies', return_value=records), contextlib.redirect_stdout(io.StringIO()) as output:
            result = catalogue.main()
        self.assertEqual(result, 1)
        self.assertIn("implementation tool 'missing-regression-tool' does not exist", output.getvalue())

if __name__ == '__main__':
    unittest.main()
