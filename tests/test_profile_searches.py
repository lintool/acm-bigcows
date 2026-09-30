"""Search-ledger integrity and complete profile-or-search roster coverage."""
import csv
from collections import Counter
import json
from datetime import datetime
from pathlib import Path
import re
import unittest
from urllib.parse import parse_qs, urlsplit

from scripts.profile_validation import acm_recipient_id

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
    return bool(row['acm_profile']) and any(acm_recipient_id(person['acm_fellow_profile']) == acm_recipient_id(row['acm_profile'])
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

    def test_search_identity_accepts_legacy_urls_without_merging_namesakes(self):
        people = [dict(acm_fellow_profile='https://awards.acm.org/award-recipients/newname_A123',
                       name='Person, Alice')]
        self.assertTrue(canonical_name_matches(dict(
            acm_profile='http://awards.acm.org/award-recipients/OLDNAME_a123.cfm',
            name='Person, Alice'), people))
        self.assertFalse(canonical_name_matches(dict(
            acm_profile='https://awards.acm.org/award-recipients/newname_B456',
            name='Person, Alice'), people))
        self.assertFalse(canonical_name_matches(dict(acm_profile='', name='Person, Alice'), people))

    def test_csrankings_search_ledger_and_coverage(self):
        fields, searches = read(ROOT / 'data/csrankings_profile_searches.csv')
        expected = ['acm_profile', 'name', 'searched_at', 'candidate_name',
                    'source_scope', 'outcome', 'reviewed_at', 'evidence']
        self.assertEqual(fields, expected)
        people = [row for filename in ['acm_fellows.csv', 'turing_award_winners.csv']
                  for row in read(ROOT / 'data' / filename)[1]]
        keys, searched = set(), set()
        def identity(row, field):
            if row[field]:
                return ('acm', acm_recipient_id(row[field]))
            return ('name', row['name'])
        for row in searches:
            with self.subTest(name=row['name'], candidate=row['candidate_name']):
                self.assertEqual(set(row), set(expected))
                self.assertTrue(all(isinstance(v, str) for v in row.values()))
                if row['acm_profile']:
                    self.assertTrue(canonical_name_matches(row, people))
                else:
                    matches = [p for p in people if p['name'] == row['name']]
                    self.assertEqual(len(matches), 1)
                    self.assertFalse(matches[0]['acm_fellow_profile'])
                person = identity(row, 'acm_profile')
                key = (person, row['searched_at'], row['candidate_name'])
                self.assertNotIn(key, keys)
                keys.add(key)
                searched.add(person)
                start, reviewed = [datetime.fromisoformat(row[f]) for f in ['searched_at', 'reviewed_at']]
                self.assertIsNotNone(start.utcoffset())
                self.assertIsNotNone(reviewed.utcoffset())
                self.assertGreaterEqual(reviewed, start)
                self.assertIn(row['outcome'], {'candidate', 'accepted', 'not_found', 'unsupported_match', 'wrong_person', 'superseded'})
                self.assertEqual(bool(row['candidate_name']), row['outcome'] != 'not_found')
                for field in ['evidence', 'source_scope']:
                    path, anchor = row[field].split('#', 1)
                    self.assertTrue((ROOT / path).is_file())
                    self.assertIn(anchor, anchors((ROOT / path).read_text()))
        for row in people:
            if not row['csrankings_name']:
                self.assertIn(identity(row, 'acm_fellow_profile'), searched, row['name'])

    def test_initial_csrankings_attempt_evidence(self):
        evidence = json.loads((ROOT / 'docs/csrankings_missing_search_2026-09-29.json').read_text())
        started = datetime.fromisoformat(evidence['started_at'])
        completed = datetime.fromisoformat(evidence['searched_at'])
        self.assertLessEqual(started, completed)
        self.assertEqual(len(evidence['source_hashes']), 46)
        for digest in evidence['source_hashes'].values():
            self.assertRegex(digest, r'^[a-f0-9]{64}$')
        records = read(ROOT / 'data/csrankings_profile_searches.csv')[1]
        expected, actual = set(), set()
        for person in evidence['people']:
            self.assertTrue(person['search_names'])
            names = {c['source']['name'] for c in person['candidates']}
            for candidate in person['candidates']:
                self.assertTrue(candidate['paths'])
                self.assertTrue(set(candidate['paths']) <= set(evidence['source_hashes']))
            for candidate, outcome in person['outcomes']:
                if candidate:
                    self.assertIn(candidate, names)
                expected.add((person['acm_profile'], person['name'], candidate, outcome))
        for row in records:
            if row['searched_at'] == evidence['searched_at']:
                actual.add((row['acm_profile'], row['name'], row['candidate_name'], row['outcome']))
        self.assertEqual(actual, expected)
        self.assertEqual(evidence['counts'], dict(Counter(
            r['outcome'] for r in records if r['searched_at'] == evidence['searched_at'])))

    def test_ledgers_and_profile_or_search_coverage(self):
        rosters = {name: read(ROOT / 'data' / name)[1] for name in
                   ['acm_fellows.csv', 'turing_award_winners.csv']}
        people = [row for rows in rosters.values() for row in rows]
        known_ids = {acm_recipient_id(row['acm_fellow_profile']) for row in people if row['acm_fellow_profile']}
        removed = set()
        decisions = read(ROOT / 'docs/holistic_profile_audit_2026-09-29_dispositions.csv')[1]
        latest = {(r['roster'], r['roster_row'], r['service']): r for r in decisions}
        for (roster, number, service), decision in latest.items():
            if decision['action'].startswith('Cleared DBLP URL'):
                person = rosters[roster][int(number) - 1]
                self.assertEqual(person['name'], decision['name'])
                self.assertEqual(service, 'dblp')
                self.assertEqual(person['dblp_profile'], '')
                self.assertEqual(person['dblp_profile_crawl_date'], '')
                self.assertEqual(person['dblp_profile_quality'], 'N')
                key = ('acm', acm_recipient_id(person['acm_fellow_profile']))
                removed.add(key)

        for service in ['google_scholar', 'dblp']:
            fields, searches = read(ROOT / 'data' / f'{service}_profile_searches.csv')
            self.assertEqual(fields, FIELDS)
            keys, searched = set(), set()
            for row in searches:
                with self.subTest(service=service, name=row['name'], searched_at=row['searched_at']):
                    self.assertEqual(set(row), set(FIELDS))
                    self.assertTrue(all(isinstance(value, str) for value in row.values()))
                    if row['acm_profile']:
                        self.assertIn(acm_recipient_id(row['acm_profile']), known_ids)
                        self.assertTrue(canonical_name_matches(row, people),
                                        'ACM URL does not belong to the recorded canonical name')
                        identity = ('acm', acm_recipient_id(row['acm_profile']))
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
                            identity = ('acm', acm_recipient_id(row['acm_fellow_profile'])) if row['acm_fellow_profile'] else ('name', row['name'])
                            self.assertTrue(identity in searched or (service == 'dblp' and identity in removed),
                                            'Neither a profile, a recorded search nor an explicit removal')


if __name__ == '__main__':
    unittest.main()
