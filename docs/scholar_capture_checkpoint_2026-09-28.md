# Scholar Capture Checkpoint: September 28, 2026

The Safari refresh of stored Google Scholar links across both award rosters finished its final batch on September 28, 2026 at 13:43 EDT.
All 1,264 distinct input URLs were attempted: 1,263 have successful captures and one remains `redirect_review`.
This is a capture checkpoint, not a completed profile-quality review or an import into canonical datasets.
No crawl or automatic restart remains scheduled.

## Scope and Coverage

The input snapshots contain 1,638 Fellows and 81 Turing Award recipients.
There are 1,254 Fellows Scholar links and 40 Turing links, with 30 URLs shared across the rosters, yielding 1,264 unique URLs.
Both canonical award CSVs still match the SHA-256 hashes recorded when the crawl inputs were prepared.

| Capture Outcome | Profiles |
| --- | ---: |
| Successful with 100 publication rows | 1,246 |
| Successful with fewer than 100 rows and an exhausted list | 17 |
| Redirect requiring review | 1 |
| Unattempted | 0 |

The shorter successful lists contain 34–99 publication rows; the captured Show More button is disabled for each.
Success validates the requested Scholar ID, complete profile markup and first-page coverage, not publication authorship, deduplication or profile quality.
The report flags 69 name mismatches for review; these are heuristic flags, not confirmed identity errors.
The broader Scholar/CSRankings audit remains unfinished, as recorded in the [current review status](profile_review_status.md).

## Retained Evidence

All input snapshots, captures, manifests, reports and run logs remain in the sibling crawler's Git-ignored `.cache/scholar-safari-refresh-2026-09-24-074715/` directory.
From this repository, that path is `../bigcows-crawler/.cache/scholar-safari-refresh-2026-09-24-074715/`.
These local artifacts are absent from a fresh clone and are not included in this documentation checkpoint.

- `preparation.json` records the original input hashes and command; its initial pacing metadata is historical.
- `fellows-input.csv`, `turing-input.csv` and `combined-input.csv` retain the input snapshots.
- `cache.json` and `report.json` record the final derived outcomes.
- `cache-captures/manifest.json` and the referenced HTML files retain individual attempts, including earlier failures.
- `crawl.log`, `process.json` and batch plan/status files record bounded execution and pauses.

All 1,264 current cache entries reference present HTML files whose SHA-256 hashes match their recorded values.
All current entries use `safari-applescript`; these are Safari page-source captures, not original HTTP response bytes or headers.
Their capture timestamps span September 24 at 07:47:29 EDT through September 28 at 13:43:01 EDT.
The final batch exited successfully at 13:43:16 EDT.
Earlier traffic blocks remain in the attempt history; the final 60-profile batch completed without new capture failures.

The final pacing was 10–20 seconds between profiles, with 60–90 seconds after every 25 new requests.
User-controlled runs were bounded to 75 new profiles, with 60 in the final run.
The temporary automatic schedule used 30-minute pauses between completed batches and was removed when the redirect required review; subsequent batches were explicitly started by the user.
See the [crawler reference](https://github.com/lintool/bigcows-crawler/blob/main/README_FOR_AGENTS.md#google-scholar-profile-crawler) for transport and cache behavior.

## Remaining Redirect and Import Work

Lawrence Charles Paulson's stored Scholar ID [`Sv1hcjEAAAAJ`](https://scholar.google.com/citations?user=Sv1hcjEAAAAJ) redirected to [`x4toSGEAAAAJ`](https://scholar.google.com/citations?user=x4toSGEAAAAJ&hl=en) on September 28 at 07:44:59 EDT.
The crawler preserved the page and rejected it as `redirect_review` because the final ID differed from the requested ID.
The destination has not been accepted as a replacement identity, and this event was not classified as a traffic block.
The failed entry remained intact while later batches continued with uncached profiles.

The five canonical missing-date tasks still exist because no capture dates or statistics have been imported.
Four now have successful 100-row captures in this run: Paola Inverardi, David Abramson, Richard DeMillo and Vishwani Agrawal.
Paulson remains unresolved.
The [capture queue](profile_capture_queue.json) describes canonical import state; it does not imply those four still lack local captures.

Next work is to review the redirect and flagged identities, then obtain authorization for any canonical data import or correction.
Award rows, profile links, quality flags, Scholar statistics and visualization snapshots were unchanged by this checkpoint.
