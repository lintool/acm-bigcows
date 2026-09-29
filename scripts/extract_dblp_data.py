#!/usr/bin/env python3
"""Extract compact DBLP metadata and yearly counts from an accepted capture audit; never fetch."""
import argparse
from collections import Counter
import csv
import hashlib
import html
import json
from pathlib import Path
import re

try:
    from profile_validation import normalize_dblp_url
except ModuleNotFoundError:
    from scripts.profile_validation import normalize_dblp_url

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / 'data/dblp_extracted_data.json'


def clean(text):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', text))).strip()


def parse_profile(body):
    headline = re.search(r'<header\b[^>]*\bid="headline"[^>]*>(.*?)</header>', body, re.S)
    if not headline:
        raise ValueError('Missing DBLP author headline')
    pid = re.search(r'\bdata-pid="([^"]+)"', headline[0])
    heading = re.search(r'<h1\b[^>]*>(.*?)</h1>', headline[1], re.S)
    if not pid or not heading:
        raise ValueError('Missing DBLP PID or name')
    names = [clean(x) for x in re.findall(r'<span\b[^>]*class="name[^\"]*"[^>]*>(.*?)</span>', headline[1], re.S)]
    name = names[0] if names else clean(heading[1])
    affiliations = []
    for item in re.findall(r'<li\b[^>]*itemprop="affiliation"[^>]*>(.*?)</li>', body, re.S):
        value = re.search(r'<span\b[^>]*itemprop="name"[^>]*>(.*?)</span>', item, re.S)
        if value and clean(value[1]) not in affiliations:
            affiliations.append(clean(value[1]))
    entries = re.findall(r'<li\b[^>]*class="entry [^\"]*"[^>]*\bid="([^"]+)"[^>]*>(.*?)(?=<li\b[^>]*class="entry |\Z)', body, re.S)
    publications = {}
    for key, entry in entries:
        cite = re.search(r'<cite\b[^>]*>(.*?)</cite>', entry, re.S)
        if not cite or not re.search(r'class="title"', cite[1]):
            raise ValueError(f'Missing publication citation: {key}')
        years = set(re.findall(r'itemprop="datePublished"[^>]*>\s*(\d{4})\s*</', cite[1]))
        if len(years) != 1:
            raise ValueError(f'Missing or ambiguous publication year: {key}')
        year = years.pop()
        if key in publications and publications[key] != year:
            raise ValueError(f'Conflicting repeated publication: {key}')
        publications[key] = year
    if '</html>' not in body.lower():
        raise ValueError('Truncated HTML')
    if not publications:
        raise ValueError('No publication entries found; review before recording zero')
    return {'pid': html.unescape(pid[1]), 'name': name,
            'name_variants': list(dict.fromkeys(n for n in names[1:] if n != name)),
            'affiliations': affiliations, 'publication_count': len(publications),
            'publications_by_year': dict(sorted(Counter(publications.values()).items())),
            'coverage': {'status': 'unknown', 'note': 'All distinct publication entries present in the retained HTML were counted; completeness of the DBLP bibliography is not independently established.'}}


def extract(audit, root=ROOT):
    """Use only captures explicitly selected by the accepted audit, matching current roster dates."""
    expected = {}
    for name in ['acm_fellows.csv', 'turing_award_winners.csv']:
        with (root / 'data' / name).open(newline='') as stream:
            for row in csv.DictReader(stream):
                if row['dblp_profile']:
                    url = normalize_dblp_url(row['dblp_profile'])
                    day = row['dblp_profile_crawl_date']
                    if url in expected and expected[url] != day:
                        raise ValueError(f'Conflicting roster dates: {url}')
                    expected[url] = day
    profiles = []
    seen = set()
    for item in audit:
        url = normalize_dblp_url(item['url'])
        if url not in expected or url in seen or item['fetched_at'][:10] != expected[url]:
            raise ValueError(f'Capture audit does not match current accepted roster: {url}')
        seen.add(url)
        path = Path(item['path'])
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != item['sha256'] or len(raw) != item['bytes']:
            raise ValueError(f'Capture hash/size mismatch: {url}')
        body = raw.decode('utf-8')
        raw_count = len(re.findall(r'<cite\b[^>]*>.*?class="title".*?</cite>', body, re.S))
        entry_count = len(re.findall(r'<li\b[^>]*class="entry [^\"]*"[^>]*\bid="[^"]+"', body))
        if entry_count != raw_count:
            raise ValueError(f'Publication entries and citations disagree: {url}')
        if raw_count != item['records']:
            raise ValueError(f'Visible entry count differs from accepted audit: {url}')
        parsed = parse_profile(body)
        if parsed['publication_count'] > raw_count:
            raise ValueError(f'Parsed count exceeds visible entry count: {url}')
        if parsed['publication_count'] < raw_count:
            parsed['coverage']['note'] += f' Repeated DBLP keys were counted once ({raw_count} displayed entries).'
        if len(seen) % 200 == 0:
            print(f'Validated {len(seen)} accepted captures', flush=True)
        if url != 'https://dblp.org/pid/' + parsed['pid']:
            raise ValueError(f'Captured PID differs from accepted URL: {url}')
        relative = path.relative_to(root.parent / 'bigcows-crawler/.cache')
        profiles.append({'profile': url, **parsed, 'capture': {
            'fetched_at': item['fetched_at'], 'capture_id': path.stem,
            'html_sha256': item['sha256'], 'source_run': relative.parts[0]}})
    if seen != set(expected):
        raise ValueError('Accepted audit does not cover every stored DBLP profile')
    return {'schema_version': 1, 'profiles': sorted(profiles, key=lambda p: p['profile'])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accepted-captures', type=Path, required=True, help='Reviewed capture-verification JSON audit with url, path, sha256, bytes, records and fetched_at.')
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.output.resolve() == args.accepted_captures.resolve() or (args.output.resolve().parent == (ROOT / 'data').resolve() and args.output.resolve() != DEFAULT_OUTPUT.resolve()):
        parser.error('Output cannot overwrite acceptance evidence or other canonical inputs')
    result = extract(json.loads(args.accepted_captures.read_text()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    print(f'Extracted {len(result["profiles"])} profiles; no requests made')


if __name__ == '__main__':
    main()
