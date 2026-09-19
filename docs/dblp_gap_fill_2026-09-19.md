# DBLP Capture Gap Fill — September 19, 2026

Completed 2026-09-19 15:10 EDT.

## Results

Captured and accepted all 84 DBLP URLs in the approved backlog, filling 87 previously blank `dblp_profile_crawl_date` cells: 83 Fellows and four Turing Award rows.
Richard Karp, David Patterson and Jim Gray share profiles across the two rosters and received matching dates.
Every imported date is the accepted capture's UTC date, September 19, 2026.
The [row audit](dblp_gap_fill_2026-09-19.csv) records each stored URL, requested and final URL, title, bibliography count, timestamp, capture hash and local HTML path.
Resolve its capture paths from the repository root.

All 1,641 distinct stored DBLP profiles now have accepted capture dates and retained HTML.
The 1,557 previously captured profiles remain dated September 17–18; they were not fetched again.
Fifteen Fellows still have blank DBLP URLs, which are missing-link cases rather than pending crawl tasks.
The [capture/import queue](profile_capture_queue.json) now contains only the five existing Scholar tasks.

## Acquisition and Review

Used sequential Safari navigation with randomized 5–7-second delays and 60–90-second cooldowns after every 25 attempts, plus a 60-second page-load timeout.
Reviewed a five-profile pilot before continuing the remaining 79 profiles; batch counters and cooldown state persisted across invocations.
The first sandboxed launch failed before opening Safari or fetching a profile; the authorized run then used native Safari access.
The first two captures paused because the pilot name matcher expected given-name order while the roster supplied comma-separated surname-first names.
Inspected and accepted Yun Fu and Adam D. Smith's saved pages, retaining the original failed-screen attempt records and explicit review decisions.
A run-local adapter reordered comma-separated names only for the existing name screen; the immutable input snapshot, source crawler, URLs and pacing were preserved.
All 84 saved pages reparse as author profiles at the requested PID, allowing the normal `.html` suffix redirect.
No access block or unexpected redirect remained unresolved.

Verified every saved HTML file's byte count and SHA-256, page heading, final PID and publication markup.
Compared profile names, available affiliation metadata and chronological publication-title samples against the accepted links and recorded ACM contributions.
This is capture acceptance and an identity/subject consistency check, not a new exhaustive publication-quality review.
Existing quality decisions remain unchanged, including the approved `N` profiles.

## Validation and Retained Evidence

The import script verified that only the 87 previously blank DBLP date cells changed, with roster ordering, all stored URLs, quality flags and existing dates preserved.
All 41 offline Python tests passed, including canonical associations, shared-profile dates, backlog consistency and published snapshot checks.
Validation commands:

- `python -B -m unittest discover -s tests -v`
- `git diff --check`

Scholar data, CSRankings data and visualization snapshots remain unchanged.
Input snapshots, raw HTML, attempt history, pacing state, logs, extracted bibliographies, review decisions, exact cell changes and the acceptance manifest are retained under `../bigcows-crawler/.cache/dblp-gap-fill-2026-09-19-145403/`.
The shared cache is local and Git-ignored.
