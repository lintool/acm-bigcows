"""Check compact DBLP extraction without fetching pages."""
import csv
import json
import hashlib
import tempfile
from pathlib import Path
import unittest
from scripts.extract_dblp_data import parse_profile, capture_date, extract
from scripts.profile_validation import normalize_dblp_url

ROOT = Path(__file__).resolve().parents[1]


def page(entries):
    return ('<html><header id="headline" data-pid="12/345"><h1>'
            '<span class="name primary">Alex &amp; Example</span>'
            '</h1><div class="note-line"><span class="name secondary" itemprop="alternateName">A. Example</span></div></header>'
            '<li itemprop="affiliation"><em>affiliation:</em><span itemprop="name">University A</span></li>'
            '<li itemprop="affiliation"><span itemprop="name">University B</span></li>'
            '<span itemprop="name">Unrelated Coauthor</span>' + entries + '</html>')


def entry(key, year):
    return (f'<li class="entry article toc" id="{key}"><cite>'
            f'<span class="title">Title</span><span itemprop="datePublished">{year}</span></cite></li>')


class DblpExtractionTests(unittest.TestCase):
    def test_metadata_and_counts_deduplicate_by_publication_key(self):
        record = parse_profile(page(entry('a', 2020) + entry('b', 2020) + entry('a', 2020) + entry('c', 2021)))
        self.assertEqual(record['name'], 'Alex & Example')
        self.assertEqual(record['name_variants'], ['A. Example'])
        self.assertEqual(record['affiliations'], ['University A', 'University B'])
        self.assertEqual(record['publication_count'], 3)
        self.assertEqual(record['publications_by_year'], {'2020': 2, '2021': 1})
        self.assertEqual(record['coverage']['status'], 'unknown')

    def test_bad_or_partial_content_does_not_become_zero_or_complete(self):
        for body in [page(''), page(entry('a', '')), page(entry('a', 2020))[:-7],
                     page(entry('a', 2020) + entry('a', 2021)), '<html>blocked</html>']:
            with self.subTest(body=body), self.assertRaises(ValueError):
                parse_profile(body)

    def test_extraction_requires_full_utc_timestamp_and_matching_date(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            root = workspace / 'app'
            (root / 'data').mkdir(parents=True)
            url = 'https://dblp.org/pid/12/345'
            for name in ['acm_fellows.csv', 'turing_award_winners.csv']:
                (root / 'data' / name).write_text(
                    'dblp_profile,dblp_profile_crawl_date\n' + url + ',2026-09-19\n')
            path = workspace / 'bigcows-crawler/.cache/test/safari/captures/example.html'
            path.parent.mkdir(parents=True)
            raw = page(entry('a', 2020)).encode()
            path.write_bytes(raw)
            item = {'url': url, 'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(),
                    'bytes': len(raw), 'records': 1}
            for value in ['2026-09-19T12:30:00Z', '2026-09-19T12:30:00+00:00',
                          '2026-09-19T12:30:00.123Z']:
                result = extract([{**item, 'fetched_at': value}], root)
                self.assertEqual(result['profiles'][0]['capture']['fetched_at'], value)
            for value in ['2026-09-19garbage', '2026-09-19', '2026-09-19T12:30:00',
                          '2026-09-19T23:30:00-04:00', '2026-09-19T01:00:00+04:00',
                          '2026-09-19T25:00:00Z', '2026-02-30T12:00:00Z',
                          '2026-09-20T00:00:00Z', None, 20260919]:
                with self.subTest(value=value), self.assertRaises(ValueError):
                    extract([{**item, 'fetched_at': value}], root)

    def test_canonical_coverage_and_aggregate_totals(self):
        data = json.loads((ROOT / 'data/dblp_extracted_data.json').read_text())
        self.assertEqual(data['schema_version'], 1)
        records = {p['profile']: p for p in data['profiles']}
        self.assertEqual(len(records), len(data['profiles']))
        expected = {}
        for name in ['acm_fellows.csv', 'turing_award_winners.csv']:
            with (ROOT / 'data' / name).open(newline='') as stream:
                for row in csv.DictReader(stream):
                    if row['dblp_profile']:
                        expected[normalize_dblp_url(row['dblp_profile'])] = row['dblp_profile_crawl_date']
        self.assertEqual(set(records), set(expected))
        for url, row in records.items():
            self.assertEqual(url, 'https://dblp.org/pid/' + row['pid'])
            self.assertTrue(row['name'])
            self.assertIsInstance(row['name_variants'], list)
            self.assertIsInstance(row['affiliations'], list)
            self.assertTrue(all(isinstance(v, str) for v in row['name_variants'] + row['affiliations']))
            self.assertEqual(row['publication_count'], sum(row['publications_by_year'].values()))
            for year, count in row['publications_by_year'].items():
                self.assertRegex(year, r'^\d{4}$')
                self.assertIs(type(count), int)
                self.assertGreater(count, 0)
            self.assertIn(row['coverage']['status'], ['complete', 'partial', 'unknown'])
            self.assertEqual(capture_date(row['capture']['fetched_at']), expected[url])
            self.assertRegex(row['capture']['html_sha256'], r'^[0-9a-f]{64}$')
            self.assertTrue(row['capture']['capture_id'])
            self.assertTrue(row['capture']['source_run'])
            self.assertNotIn('publications', row)
