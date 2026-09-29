"""Validate native Scholar extraction types and capture provenance at the read boundary."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from scripts.scholar_data import DEFAULT_SCHOLAR, read_scholar

ROOT = Path(__file__).resolve().parents[1]


class ScholarDataTests(unittest.TestCase):
    def setUp(self):
        self.profile = read_scholar()[0]

    def read_document(self, document):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'scholar.json'
            path.write_text(json.dumps(document))
            return read_scholar(path)

    def test_native_zero_null_and_collections(self):
        row = copy.deepcopy(self.profile)
        row.update(citations=0, h_index=None, affiliation=None, interests=[], citation_by_year={})
        self.assertEqual(self.read_document({'schema_version': 1, 'profiles': [row]}), [row])

    def test_rejects_unsupported_schema_and_duplicate_profiles(self):
        for document in [{'schema_version': 2, 'profiles': []},
                         {'schema_version': True, 'profiles': []},
                         {'schema_version': 1, 'profiles': {}},
                         {'schema_version': 1, 'profiles': [self.profile, self.profile]}]:
            with self.subTest(document=document), self.assertRaises(ValueError):
                self.read_document(document)

    def test_rejects_bad_types_and_provenance(self):
        for field, value in [('citations', '123'), ('h_index', True), ('i10_index', -1),
                             ('interests', '[]'), ('citation_by_year', {'2026': '3'}),
                             ('citation_by_year', {'2026': False}), ('crawl_date', '1999-01-01'),
                             ('capture', None), ('profile', 'not-a-profile')]:
            row = copy.deepcopy(self.profile)
            row[field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                self.read_document({'schema_version': 1, 'profiles': [row]})
        for field, value in [('html_sha256', 'bad-hash'), ('capture_id', ''),
                             ('fetched_at', '2026-09-27T12:00:00')]:
            row = copy.deepcopy(self.profile)
            row['capture'][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.read_document({'schema_version': 1, 'profiles': [row]})

    def test_rejects_duplicate_json_keys(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'scholar.json'
            path.write_text('{"schema_version":1,"profiles":[],"profiles":[]}')
            with self.assertRaisesRegex(ValueError, 'Duplicate JSON key'):
                read_scholar(path)

    def test_queue_cannot_overwrite_canonical_json(self):
        before = DEFAULT_SCHOLAR.read_bytes()
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/build_profile_capture_queue.py'),
                                 '--output', str(DEFAULT_SCHOLAR)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('cannot overwrite canonical inputs', result.stderr)
        self.assertEqual(DEFAULT_SCHOLAR.read_bytes(), before)
