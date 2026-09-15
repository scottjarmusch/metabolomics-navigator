import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import yaml
import check_editorial_readiness as editorial
from tool_history import history_for


class AcceptanceTests(unittest.TestCase):
    def result(self, status):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            (root/'content/tools').mkdir(parents=True)
            (root/'content/tools/example.yml').write_text(yaml.safe_dump({'status':status}),encoding='utf-8')
            with patch.object(editorial,'ROOT',root), contextlib.redirect_stdout(io.StringIO()):
                return editorial.main()

    def test_unreviewed_stub_does_not_require_editorial_additions(self):
        self.assertEqual(self.result({'entry':'stub','review':'unreviewed'}),0)

    def test_promotion_requires_editorial_fields(self):
        self.assertEqual(self.result({'entry':'published','review':'unreviewed'}),1)
        self.assertEqual(self.result({'entry':'stub','review':'editorially_reviewed'}),1)

    def test_existing_tool_has_real_history(self):
        history=history_for('mzmine')
        self.assertTrue(history['events'])
        self.assertEqual(len(history['events'][0]['sha']),40)
        if history['complete']:
            self.assertEqual(history['events'][-1]['kind'],'First committed entry')


if __name__=='__main__':
    unittest.main()
