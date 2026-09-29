"""Search-ledger integrity and complete profile-or-search roster coverage."""
import csv
from datetime import datetime
from pathlib import Path
import re
import unittest
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['acm_profile', 'name', 'searched_at', 'candidate_url', 'outcome', 'reviewed_at', 'evidence']
OUTCOMES = {'candidate', 'accepted', 'not_found', 'unresolved_lead', 'inaccessible',
            'wrong_person', 'rejected_quality', 'superseded'}


def read(path):
    with path.open(newline='', encoding='utf-8') as stream:
        reader = csv.DictReader(stream)
        return reader.fieldnames, list(reader)


def anchors(text):
    result = set(re.findall(r'(?:id|name)=[\"\x27]([^\"\x27]+)', text))
    counts = {}
    for line in text.splitlines():
        if re.match(r'^#{1,6} ', line):
            anchor = re.sub(r'[^\w\- ]', '', line.lstrip('# ').lower()).replace(' ', '-')
            count = counts.get(anchor, 0)
            counts[anchor] = count + 1
            result.add(anchor + (f'-{count}' if count else ''))
    return result


def canonical_name_matches(row, people):
    return any(person['acm_fellow_profile'] == row['acm_profile']
               and person['name'] == row['name'] for person in people)


def has_scholar_user(query):
    values = parse_qs(query, keep_blank_values=True).get('user', [])
    return len(values) == 1 and bool(values[0].strip())


class ProfileSearchTests(unittest.TestCase):
    def test_scholar_query_requires_exact_nonempty_user(self):
        for query in ['user=abc', 'hl=en&user=abc', 'user=abc&hl=en']:
            self.assertTrue(has_scholar_user(query), query)
        for query in ['', 'notuser=abc', 'user=', 'user', 'user=%20',
                      'q=user=abc', 'user=abc&user=def', 'user=abc&user=']:
            self.assertFalse(has_scholar_user(query), query)

    def test_acm_identity_must_match_a_canonical_roster_name(self):
        people = [dict(acm_fellow_profile='acm/alice', name='Person, Alice'),
                  dict(acm_fellow_profile='acm/bob', name='Person, Bob'),
                  dict(acm_fellow_profile='acm/alice', name='Person, Alice A.')]
        for name in ['Person, Alice', 'Person, Alice A.']:
            self.assertTrue(canonical_name_matches(dict(acm_profile='acm/alice', name=name), people))
        for url, name in [('acm/bob', 'Person, Alice'), ('acm/alice', 'Person, Bob'),
                          ('acm/unknown', 'Person, Alice')]:
            self.assertFalse(canonical_name_matches(dict(acm_profile=url, name=name), people))

    def test_ledgers_and_profile_or_search_coverage(self):
        rosters = {name: read(ROOT / 'data' / name)[1] for name in
                   ['acm_fellows.csv', 'turing_award_winners.csv']}
        people = [row for rows in rosters.values() for row in rows]
        known_ids = {row['acm_fellow_profile'] for row in people if row['acm_fellow_profile']}
        for service in ['google_scholar', 'dblp']:
            fields, searches = read(ROOT / 'data' / f'{service}_profile_searches.csv')
            self.assertEqual(fields, FIELDS)
            keys, searched = set(), set()
            for row in searches:
                with self.subTest(service=service, name=row['name'], searched_at=row['searched_at']):
                    self.assertEqual(set(row), set(FIELDS))
                    self.assertTrue(all(isinstance(value, str) for value in row.values()))
                    if row['acm_profile']:
                        self.assertIn(row['acm_profile'], known_ids)
                        self.assertTrue(canonical_name_matches(row, people),
                                        'ACM URL does not belong to the recorded canonical name')
                        identity = ('acm', row['acm_profile'])
                    else:
                        matches = [person for person in people if person['name'] == row['name']]
                        self.assertEqual(len(matches), 1, 'Name fallback must be unambiguous')
                        self.assertFalse(matches[0]['acm_fellow_profile'])
                        identity = ('name', row['name'])
                    key = (identity, row['searched_at'], row['candidate_url'])
                    self.assertNotIn(key, keys)
                    keys.add(key)
                    searched.add(identity)
                    times = [datetime.fromisoformat(row[field]) for field in ['searched_at', 'reviewed_at']]
                    self.assertTrue(all(time.utcoffset() is not None for time in times))
                    self.assertGreaterEqual(times[1], times[0])
                    self.assertIn(row['outcome'], OUTCOMES)
                    if row['outcome'] not in {'not_found', 'unresolved_lead'}:
                        self.assertTrue(row['candidate_url'])
                    if row['candidate_url']:
                        url = urlsplit(row['candidate_url'])
                        self.assertEqual(url.scheme, 'https')
                        if service == 'dblp':
                            self.assertEqual(url.netloc, 'dblp.org')
                            self.assertTrue(url.path.startswith('/pid/'))
                        else:
                            self.assertEqual(url.netloc, 'scholar.google.com')
                            self.assertEqual(url.path, '/citations')
                            self.assertTrue(has_scholar_user(url.query),
                                            'Scholar URL requires exactly one nonempty user parameter')
                    path, anchor = row['evidence'].split('#', 1)
                    evidence = ROOT / path
                    self.assertTrue(evidence.is_file())
                    self.assertIn(anchor, anchors(evidence.read_text()))
            for roster, rows in rosters.items():
                for row in rows:
                    with self.subTest(service=service, roster=roster, name=row['name']):
                        if not row[f'{service}_profile']:
                            identity = ('acm', row['acm_fellow_profile']) if row['acm_fellow_profile'] else ('name', row['name'])
                            self.assertIn(identity, searched, 'Neither a profile nor a recorded search')


if __name__ == '__main__':
    unittest.main()
