# Latest Scholar Statistics Import

The user authorized updating `data/google_scholar_profiles.csv` from the most recent saved crawl evidence.
The import reconciles all 1,279 currently stored Scholar URLs across both award rosters, using the latest successful capture from the completed refresh and subsequent targeted runs.
No network requests or visualization regeneration were performed.

The user subsequently authorized visualization regeneration on September 29; both snapshots now reflect these imports and all 41 Python tests pass, including snapshot synchronization.
The deferred-visualization statements below describe the import checkpoint before that authorization.

## Imported Scope

| Source Run Under `../bigcows-crawler/.cache/` | Profiles |
| --- | ---: |
| `scholar-safari-refresh-2026-09-24-074715` | 1,263 |
| `paulson-100-2026-09-28` | 1 |
| `scholar-new15-2026-09-28-230031` | 15 |

Updated 1,259 existing statistics records; the nineteen previously imported records and Paulson's record already match their latest captures and remain unchanged.
Synchronized 1,249 Fellow and 40 Turing Scholar capture-date cells with the corresponding statistics rows.
These changes are incremental to the [nineteen-profile import](scholar_reviewed19_import_2026-09-28.md).
All 1,279 statistics records now reflect the selected captures; no records were added or removed by this full refresh import.
Existing row order, profile URLs, all quality flags and unrelated roster fields are preserved.
This includes the user-approved N ratings; reported Scholar metrics are retained without implying that the underlying attribution is clean.

## Capture Dates and Coverage

Dates are the actual capture dates in UTC, not the import date.

| UTC Capture Date | Profiles |
| --- | ---: |
| 2026-09-24 | 96 |
| 2026-09-26 | 96 |
| 2026-09-27 | 528 |
| 2026-09-28 | 544 |
| 2026-09-29 | 15 |

There are 1,262 captures containing 100 entries and 17 exhausted publication lists containing 34–99 entries.
These bounded captures do not establish complete or recent-sorted bibliography coverage.
All selected captures have status `ok`, no retained fetch error, a matching final profile ID and verified HTML SHA-256 and byte count.
Statistics and annual citation histories were reparsed from retained HTML and checked against the cache before writing canonical data.
The 1,263 original-run capture hashes match the evidence used by the completed holistic review; its final user dispositions and the separately approved targeted captures remain authoritative.
Paulson's original redirected URL was excluded in favor of his subsequently accepted direct destination capture.

## Retained Import Evidence

The run-specific importer, pre-import canonical snapshots, per-profile source/capture/hash records, imported values and validation are retained in `../bigcows-crawler/.cache/scholar-full-reviewed-import-2026-09-29/` relative to the repository root.
The [capture/import queue](profile_capture_queue.json) remains empty.
Visualization snapshots remain deliberately unchanged and may lag the refreshed canonical CSVs.

## Validation

All 40 canonical-data tests and `git diff --check` passed.
Exact before/after checks verified all 1,279 statistics rows against accepted parsed values, matching dates in both rosters, unique URLs, unchanged profile ordering, LF line endings and preserved links, quality flags and unrelated fields.
The capture/import queue is empty and visualization files are unchanged.
