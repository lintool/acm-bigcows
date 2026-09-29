"""Read the canonical, reviewed Google Scholar extraction dataset."""
import json
import re
from datetime import date, datetime
from pathlib import Path

DEFAULT_SCHOLAR = Path(__file__).resolve().parents[1] / 'data/google_scholar_extracted_data.json'
NUMERIC_FIELDS = ('citations', 'h_index', 'i10_index', 'citations_since_5y_ago',
                  'h_index_since_5y_ago', 'i10_index_since_5y_ago', 'first_citation_year')


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def read_scholar(path=DEFAULT_SCHOLAR):
    """Return validated native records; never fetch, infer acceptance or coerce types."""
    data = json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=_unique_object)
    if not isinstance(data, dict) or type(data.get('schema_version')) is not int or data['schema_version'] != 1:
        raise ValueError('Expected Scholar schema_version 1')
    rows = data.get('profiles')
    if not isinstance(rows, list):
        raise ValueError('Expected profiles array')
    seen = set()
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError('Expected profile object')
        url = row.get('profile')
        if not isinstance(url, str) or not re.fullmatch(r'https://scholar\.google\.com/citations\?user=[\w-]{12}', url):
            raise ValueError(f'Invalid Scholar profile URL: {url}')
        if url in seen:
            raise ValueError(f'Duplicate Scholar profile: {url}')
        seen.add(url)
        if not isinstance(row.get('name'), str) or not row['name'].strip():
            raise ValueError(f'Missing name: {url}')
        if 'affiliation' not in row or (row['affiliation'] is not None and not isinstance(row['affiliation'], str)):
            raise ValueError(f'Invalid affiliation: {url}')
        for field in NUMERIC_FIELDS:
            value = row.get(field)
            if field not in row or (value is not None and (type(value) is not int or value < 0)):
                raise ValueError(f'Invalid {field}: {url}')
        if not isinstance(row.get('interests'), list) or not all(isinstance(v, str) for v in row['interests']):
            raise ValueError(f'Invalid interests: {url}')
        history = row.get('citation_by_year')
        if not isinstance(history, dict) or not all(re.fullmatch(r'\d{4}', y) and type(v) is int and v >= 0 for y, v in history.items()):
            raise ValueError(f'Invalid citation_by_year: {url}')
        capture = row.get('capture')
        if not isinstance(capture, dict):
            raise ValueError(f'Missing capture provenance: {url}')
        if not all(isinstance(capture.get(k), str) and capture[k] for k in ('fetched_at', 'capture_id', 'html_sha256', 'source_run')):
            raise ValueError(f'Incomplete capture provenance: {url}')
        if not re.fullmatch(r'[0-9a-f]{64}', capture['html_sha256']):
            raise ValueError(f'Invalid capture hash: {url}')
        try:
            captured = datetime.fromisoformat(capture['fetched_at'].replace('Z', '+00:00'))
            day = date.fromisoformat(row['crawl_date'])
        except (ValueError, TypeError, KeyError) as exc:
            raise ValueError(f'Invalid capture date: {url}') from exc
        if captured.utcoffset() is None or captured.utcoffset().total_seconds() != 0 or captured.date() != day:
            raise ValueError(f'Capture timestamp/date mismatch: {url}')
    return rows
