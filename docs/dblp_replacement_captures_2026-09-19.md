# DBLP Replacement Capture Gap Fill

Completed 2026-09-19 16:36 EDT.
Captured and accepted all 17 approved replacement DBLP URLs, including MacQueen, and filled exactly 17 Fellow capture-date cells from the captures’ UTC timestamps.
All 1,641 distinct stored DBLP URLs now have accepted captures; 15 Fellows still lack DBLP links and are outside the capture backlog.
No Turing Award cells changed.
Quality flags and URLs are unchanged, including MacQueen’s explicit N.
Google Scholar data and its five pending capture/import tasks are unchanged.

The [capture audit](dblp_replacement_captures_2026-09-19.csv) records final URLs, names, publication counts, timestamps, hashes and retained HTML paths.
Resolve the audit’s HTML paths relative to the repository root.
Each raw HTML file was checked against its recorded byte count and SHA-256 and reparsed as a complete author profile.
Author headings, available person metadata and chronological publication samples were checked against the accepted candidate reviews and retained ACM context.
All 17 bibliography counts match the earlier candidate inspections.
This checks capture acceptance and consistency, not a new exhaustive publication-quality review.

Used the existing Safari crawler with sequential requests and randomized 5–7-second spacing.
The five-profile pilot was reviewed before continuation; the 25-attempt batch threshold was not reached.
The first sandboxed launch failed before any fetch; the authorized launch used native Safari access.
Inputs, HTML, attempt history, state, logs, extracted bibliography records, acceptance decisions and import validation are retained under `../bigcows-crawler/.cache/dblp-replacement-gap-fill-2026-09-19-163416/`.
Only the 17 previously blank DBLP capture dates changed; all other canonical cells and visualization files were preserved.
