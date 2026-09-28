# Paulson Scholar Capture Acceptance and Import

## Latest Accepted Capture: 100 Entries

The user subsequently authorized one targeted Paulson crawl for 100 entries, with no other profiles to be crawled.
Safari captured the corrected ID directly on September 28, 2026 at 22:17:11 UTC (18:17:11 EDT), returning 100 entries with status `ok` and no blocking.
A preceding sandbox attempt failed to control Safari before navigation; the native-access retry completed and the crawler exited.
No further crawl or restart is scheduled.
The new HTML SHA-256 is `e3157ca56a9606520cce966d22175654b472a78d393fd76c0198ad5df2dd1436` (223,360 bytes).
All 100 entries were inspected; titles, coauthors and venues support Paulson's theorem-proving, logic, programming-language and formal-verification work, with no apparent unrelated cluster.
All entries credit Paulson; 80 titles match the retained September 17 DBLP bibliography after normalization, with the remaining books, manuals, technical-report versions and title variants consistent with the same research body.
Retain quality Y: identity and substantial coverage are supported within this expanded scope.
The page is not exhausted; complete bibliography coverage and recent-sorted work remain unverified, and entries include duplicate editions or versions.

The newly accepted capture supersedes the earlier 20-entry evidence for current review and import provenance.
Its metrics, affiliation, interests and annual citation series exactly match the already imported row, and its UTC date is also 2026-09-28, so no additional canonical CSV value changes were necessary.
The capture/import queue remains at four other profiles; no other capture was fetched or imported, and no visualization was regenerated.
The fresh capture, raw manifest, input snapshots, 100-entry review list, DBLP corroboration and import acceptance are retained under `../bigcows-crawler/.cache/paulson-100-2026-09-28/`.
The explicit import script verifies the selected row and preserves all other canonical records.
All 40 canonical-data tests, exact before/after checks and `git diff --check` passed after this targeted refresh.

## Earlier 20-Entry Import

The following records the earlier import as historical provenance; its 20-entry review limitation is superseded by the 100-entry review above.


The user authorized importing the retained capture for Lawrence Charles Paulson at `https://scholar.google.com/citations?user=x4toSGEAAAAJ`.
The capture was accepted and imported without any new network request or visualization regeneration.

### Accepted Evidence

The Safari page was captured on September 28, 2026 at 11:44:59 UTC (07:44:59 EDT), following a redirect from `Sv1hcjEAAAAJ` to the user-confirmed destination `x4toSGEAAAAJ`.
The original crawler status remains `redirect_review` as historical transport evidence; a separate application acceptance record documents this reviewed destination capture.
Validated the 170,812-byte HTML against SHA-256 `b1bf0bee3ca7fed0e34e79abbe9e7ee9c910a4f09532d0f09dadd5128302dcc2`, complete page markup, absence of blocking indicators, final destination ID and all six parsed metric fields.
The page identifies Lawrence Paulson at the University of Cambridge, with computational logic and formal-verification interests and representative Isabelle/HOL, Isabelle, ML and protocol-verification works.
All 20 captured publication entries name Paulson; this supports identity and sampled relevance, not complete bibliography coverage or recent-work verification.

### Imported Values

| Field | Value |
| --- | --- |
| Capture date in Fellow row and statistics row | 2026-09-28 |
| Citations / h-index / i10-index | 23,632 / 60 / 146 |
| Recent-period citations / h-index / i10-index | 4,602 / 26 / 60 |
| Captured citation-history years | 1988–2026 |
| Retained publication entries | 20 |

Added one record to `data/google_scholar_profiles.csv`, including affiliation, interests and the captured annual citation series.
Set only Paulson's `google_scholar_profile_crawl_date` in `data/acm_fellows.csv`; his accepted URL and quality Y remain unchanged.
The date records the actual capture, not the later acceptance time.
All other statistics and award fields, including the latest explicit quality decisions, are preserved.
The [capture/import queue](profile_capture_queue.json) now contains four tasks: Inverardi, Abramson, DeMillo and Agrawal.
At this earlier checkpoint, Paulson had no remaining capture/import task, but coverage and contamination beyond 20 entries remained unverified; the later 100-entry review above supersedes that scope.
The other 1,263 refresh profiles remain unimported from this run; their previous canonical records are preserved.

### Provenance and Validation

The original HTML is retained under `../bigcows-crawler/.cache/scholar-safari-refresh-2026-09-24-074715/cache-captures/d14d554ed0a5904c/20260928T114459Z-p0-8aad9466ae2e49f4b06387128a658387.html`.
Before snapshots, the explicit import script, parsed values, acceptance decision and resulting hashes are retained in `../bigcows-crawler/.cache/paulson-reviewed-import-2026-09-28/`.
These local evidence artifacts are absent from a fresh clone.
Validated the sole roster-date change, the single appended statistics record, matching dates, unchanged other records, unique URLs, LF line endings and the four-task queue.
All 40 canonical-data tests and `git diff --check` passed; visualization synchronization is deliberately deferred.
