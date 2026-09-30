"""Current removals cover either publication service without dated audit coupling."""
import unittest
from scripts.profile_validation import validate_profile_removals


class ProfileRemovalTests(unittest.TestCase):
    def test_both_services_and_shared_award_rows(self):
        for service, url in [('dblp', 'https://dblp.org/pid/1/2'),
                             ('google_scholar', 'https://scholar.google.com/citations?user=abc')]:
            person = {'name': 'Example, Alice', 'acm_fellow_profile': 'https://awards.acm.org/award-recipients/example_123',
                      service + '_profile': '', service + '_profile_crawl_date': '', service + '_profile_quality': 'N'}
            decision = dict(acm_profile=person['acm_fellow_profile'], name=person['name'], service=service,
                            removed_url=url, decided_at='2027-01-01T12:00:00+00:00', evidence='docs/new-review.md#decision')
            with self.subTest(service=service):
                self.assertEqual(validate_profile_removals([decision], [person, dict(person)]),
                                 {(service, ('acm', '123'))})
                for field, value in [(service + '_profile', url), (service + '_profile_crawl_date', '2027-01-01'),
                                     (service + '_profile_quality', 'Y'), ('name', 'Wrong Person')]:
                    with self.subTest(field=field), self.assertRaises(ValueError):
                        validate_profile_removals([decision], [{**person, field: value}])
                with self.assertRaises(ValueError):
                    validate_profile_removals([decision, decision], [person])
                with self.assertRaises(ValueError):
                    validate_profile_removals([{**decision, 'decided_at': '2027-01-01'}], [person])

    def test_name_fallback_must_be_unambiguous(self):
        person = dict(name='Example', acm_fellow_profile='', dblp_profile='', dblp_profile_crawl_date='', dblp_profile_quality='N')
        decision = dict(acm_profile='', name='Example', service='dblp', removed_url='https://dblp.org/pid/1/2',
                        decided_at='2027-01-01T12:00:00Z', evidence='docs/new-review.md#decision')
        self.assertEqual(validate_profile_removals([decision], [person]), {('dblp', ('name', 'Example'))})
        with self.assertRaises(ValueError):
            validate_profile_removals([decision], [person, dict(person)])
