# Nineteen Scholar Capture Imports

The user reviewed the 19 pending profile links and approved all of them for import while preserving existing quality ratings.
All 19 retained captures were accepted and imported without making new network requests.
Neil Jones remains N; the other 18 remain Y.

The remaining broad-refresh statistics were subsequently imported in the [September 29 full update](scholar_full_import_2026-09-29.md); the deferred-import counts below describe this earlier checkpoint.

## Imported Captures

Capture dates below use UTC, consistently with the canonical datasets; the fifteen-profile run occurred on September 28 in Toronto but September 29 UTC.
Each retained page contains 100 publication entries.

| Fellow | Scholar Profile | Capture Date (UTC) | Quality |
| --- | --- | --- | :---: |
| LAM, SIMON S | [Simon Lam](https://scholar.google.com/citations?user=0XV1sFsAAAAJ) | 2026-09-29 | Y |
| Ricart, Glenn | [Glenn Ricart](https://scholar.google.com/citations?user=1gWf6F0AAAAJ) | 2026-09-29 | Y |
| Jones, Neil | [Neil Jones](https://scholar.google.com/citations?user=2ADsKV4AAAAJ) | 2026-09-29 | N |
| Denning, Dorothy E | [Dorothy Denning](https://scholar.google.com/citations?user=4nX0ljsAAAAJ) | 2026-09-29 | Y |
| Brooks, Rodney A | [rodney brooks](https://scholar.google.com/citations?user=BCGgwlEAAAAJ) | 2026-09-29 | Y |
| Agrawal, Vishwani D | [Vishwani Agrawal](https://scholar.google.com/citations?user=C_m6dhIAAAAJ) | 2026-09-28 | Y |
| Agrawal, Dharma P | [Dharma Agrawal](https://scholar.google.com/citations?user=Cky-RdoAAAAJ) | 2026-09-29 | Y |
| Bhuyan, Laxmi Narayan | [Laxmi Bhuyan](https://scholar.google.com/citations?user=EITmT94AAAAJ) | 2026-09-29 | Y |
| Inverardi, Paola | [Paola Inverardi](https://scholar.google.com/citations?user=FxKiXx0AAAAJ) | 2026-09-27 | Y |
| Fischer, Gerhard | [Gerhard Fischer](https://scholar.google.com/citations?user=NJSK64sAAAAJ) | 2026-09-29 | Y |
| Ryder, Barbara Gershon | [Barbara G. Ryder](https://scholar.google.com/citations?user=OdWimfcAAAAJ) | 2026-09-29 | Y |
| Mei, Hong | [Hong Mei](https://scholar.google.com/citations?user=QMIdsa8AAAAJ) | 2026-09-29 | Y |
| Mount, David M | [David M. Mount](https://scholar.google.com/citations?user=QNkNlu4AAAAJ) | 2026-09-29 | Y |
| Fayyad, Usama M | [Usama Fayyad](https://scholar.google.com/citations?user=RlpTB_UAAAAJ) | 2026-09-29 | Y |
| Markopoulou, Athina | [Athina Markopoulou](https://scholar.google.com/citations?user=WIXl6-gAAAAJ) | 2026-09-29 | Y |
| Akeley, Kurt B | [Kurt Akeley](https://scholar.google.com/citations?user=fag2MKIAAAAJ) | 2026-09-29 | Y |
| Kasik, David J | [Dave Kasik](https://scholar.google.com/citations?user=j2vMBDgAAAAJ) | 2026-09-29 | Y |
| DeMillo, Richard | [Richard DeMillo](https://scholar.google.com/citations?user=kK3b1SAAAAAJ) | 2026-09-28 | Y |
| Abramson, David A | [David Abramson](https://scholar.google.com/citations?user=o5NbsPEAAAAJ) | 2026-09-28 | Y |

## Provenance and Scope

The fifteen new captures are documented in the [crawl checkpoint](scholar_new15_capture_2026-09-28.md).
The other four are from `../bigcows-crawler/.cache/scholar-safari-refresh-2026-09-24-074715/`.
The reviewed import script, before snapshots, acceptance records with complete capture metadata, and validation results are retained under `../bigcows-crawler/.cache/scholar-reviewed19-import-2026-09-28/` relative to the repository root.
All selected HTML hashes and byte counts were verified; captures have status `ok`, no retained fetch errors, matching final Scholar IDs and complete parsed metrics.
Metrics were reparsed from the retained HTML and checked against cache values before import.
The user-approved identity and quality decisions are preserved; importing a 100-entry sample does not establish complete bibliography or recent-sorted coverage.

Added 19 shared statistics records and populated exactly 19 Fellow Scholar capture-date cells from the same evidence.
Existing statistics records, all other Fellow fields and the entire Turing roster are unchanged.
The regenerated [capture/import queue](profile_capture_queue.json) is empty.
Of the earlier 1,263 successful refresh captures, four have now been imported here; 1,259 remain unimported from that refresh and retain their existing canonical statistics.
Paulson's separately accepted destination capture remains imported.
An empty missing-capture/import queue does not mean every existing statistics record has been refreshed from the September crawl.
Visualization regeneration remains explicitly deferred.

## Validation

All 40 canonical-data tests and `git diff --check` passed.
Exact before/after checks confirm 19 added statistics records, 19 Fellow date changes, preserved quality ratings and unrelated fields, unique statistics URLs and an empty queue.
Visualization synchronization checks remain deferred with regeneration.
