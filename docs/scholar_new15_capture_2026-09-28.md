# Fifteen New Scholar Captures

The user authorized a 100-publication Safari crawl of the 15 newly accepted Fellow profiles.
The run completed on September 28, 2026 at 23:05 EDT, with all 15 profiles returning exactly 100 publication entries (1,500 total).
Successful page captures span 23:01:10–23:04:49 EDT; the final report was written at 23:05:02 EDT.
No traffic block, redirect or incomplete capture was reported.

The user subsequently approved all 19 pending profiles, and their dates and metrics are now imported; see the [acceptance and import report](scholar_reviewed19_import_2026-09-28.md).
The capture-only state below is historical.

## Retained Evidence

Artifacts are retained under `../bigcows-crawler/.cache/scholar-new15-2026-09-28-230031/` relative to the repository root.
This directory includes roster and statistics snapshots, the exact 15-row input, preparation metadata, both invocation logs, cache, report, completion records and the HTML capture manifest.
The initial sandboxed invocation failed locally with a Safari AppleScript/XPC `browser_error` before obtaining a page; the desktop-authorized retry succeeded for all 15 profiles.
That initial failure remains in the append-only manifest.
The retry exited with code 0.

Pacing was 10–20 seconds between profiles (`--delay 15 --delay-jitter 5`), with `--page-size 100`, `--limit-new 15` and `--no-write-csv`.
The 25-profile batch threshold was not reached.
The crawl is complete and stopped.

## Capture Results

| Fellow | Scholar ID | Entries |
| --- | --- | ---: |
| Markopoulou, Athina | [['WIXl6-gAAAAJ']](https://scholar.google.com/citations?user=WIXl6-gAAAAJ) | 100 |
| Mei, Hong | [['QMIdsa8AAAAJ']](https://scholar.google.com/citations?user=QMIdsa8AAAAJ) | 100 |
| Mount, David M | [['QNkNlu4AAAAJ']](https://scholar.google.com/citations?user=QNkNlu4AAAAJ) | 100 |
| Ricart, Glenn | [['1gWf6F0AAAAJ']](https://scholar.google.com/citations?user=1gWf6F0AAAAJ) | 100 |
| Kasik, David J | [['j2vMBDgAAAAJ']](https://scholar.google.com/citations?user=j2vMBDgAAAAJ) | 100 |
| Fischer, Gerhard | [['NJSK64sAAAAJ']](https://scholar.google.com/citations?user=NJSK64sAAAAJ) | 100 |
| Fayyad, Usama M | [['RlpTB_UAAAAJ']](https://scholar.google.com/citations?user=RlpTB_UAAAAJ) | 100 |
| Brooks, Rodney A | [['BCGgwlEAAAAJ']](https://scholar.google.com/citations?user=BCGgwlEAAAAJ) | 100 |
| Bhuyan, Laxmi Narayan | [['EITmT94AAAAJ']](https://scholar.google.com/citations?user=EITmT94AAAAJ) | 100 |
| Agrawal, Dharma P | [['Cky-RdoAAAAJ']](https://scholar.google.com/citations?user=Cky-RdoAAAAJ) | 100 |
| Jones, Neil | [['2ADsKV4AAAAJ']](https://scholar.google.com/citations?user=2ADsKV4AAAAJ) | 100 |
| LAM, SIMON S | [['0XV1sFsAAAAJ']](https://scholar.google.com/citations?user=0XV1sFsAAAAJ) | 100 |
| Ryder, Barbara Gershon | [['OdWimfcAAAAJ']](https://scholar.google.com/citations?user=OdWimfcAAAAJ) | 100 |
| Akeley, Kurt B | [['fag2MKIAAAAJ']](https://scholar.google.com/citations?user=fag2MKIAAAAJ) | 100 |
| Denning, Dorothy E | [['4nX0ljsAAAAJ']](https://scholar.google.com/citations?user=4nX0ljsAAAAJ) | 100 |

## Validation and Import Status

All 15 retained HTML files match their manifest SHA-256 values and each contains 100 publication rows; all final profile IDs match the requested IDs.
The only automatic name mismatch is David J. Kasik versus Dave Kasik, already resolved by the [user-approved identity assessment](kasik_scholar_review_2026-09-28.md).
This capture check does not constitute a new holistic publication-quality review; Neil Jones retains the user's explicit N rating.
The two award rosters and shared statistics CSV are byte-identical to their pre-run snapshots.
No capture dates or metrics were imported and no visualization was regenerated.

All 19 canonical Scholar capture/import queue entries now have retained 100-entry capture evidence: these 15 plus Inverardi, Abramson, DeMillo and Vishwani Agrawal from the earlier refresh.
The queue remains open for capture acceptance and metric import; its generated `awaiting_refresh_approval` label is not evidence that these pages still require fetching.
No further crawl is scheduled or authorized by this checkpoint.
