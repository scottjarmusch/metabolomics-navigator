"""Missing implementation references must fail, rather than disappear in rendered pages."""
import contextlib
import io
import unittest
from unittest.mock import patch
import validate_catalogue as catalogue

class ImplementationReferenceTests(unittest.TestCase):
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
