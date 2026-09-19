# DBLP Consistency and Decision Closure

Completed 2026-09-19 16:46 EDT.
The current DBLP associations, quality flags, capture dates and applied user decisions are consistent across both award rosters.
DBLP is in an approved state within the documented review scope, with no outstanding user decision or capture task.
No canonical data changes or new quality decisions were needed.
The [current row snapshot](dblp_current_status_2026-09-19.csv) records all 1,719 rows with their current URL, rating, date, decision status and capture evidence.
Its capture paths resolve relative to the repository root; `decision_note` preserves the application-time note, which may predate the current accepted capture date.

## Current Totals

| Roster | Linked Y | Linked N | Missing Link | Total |
| --- | ---: | ---: | ---: | ---: |
| ACM Fellows | 1,581 | 42 | 15 | 1,638 |
| Turing Award Winners | 77 | 4 | 0 | 81 |

The 1,641 distinct linked profiles comprise 1,598 Y and 43 N.
All have accepted raw HTML captures and populated dates derived from their UTC capture timestamps.
The 15 missing links are explicitly N with blank dates; they are not crawl gaps.
All 63 people shared across rosters have matching normalized DBLP URLs, ratings and dates.
No normalized DBLP URL is assigned to conflicting ACM recipient IDs.

## Decisions and Quality Rationale

Verified all 17 replacement URLs against their recorded approved candidates: 16 are Y and MacQueen remains N as explicitly requested.
All other canonical URLs and ratings match the recorded reassessment outcomes and subsequent four explicit N decisions.
The remaining four review records are user-approved N holds for Gupta, Adams, Friedman and Harris; none requests a new decision.
Known poor or unresolved associations remain stored where the user approved retention; a stored URL and successful capture do not imply a Y rating or verified identity.

The recorded quality judgments remain defensible under the agreed criteria.
Identity alone does not establish quality; N covers wrong or unresolved identities, substantial unrelated clusters and inadequate career coverage.
Cook, Hillis and the earlier Crocker decision are contextual coverage exceptions supported by central contributions, not a general exemption for small bibliographies.
MacQueen’s better candidate is still N because later verified work is omitted, as the user explicitly decided.
A few isolated questionable records in otherwise coherent bibliographies do not by themselves require N; sustained namesake clusters remain N even when relevant work forms a majority.
This consistency review found no new evidence requiring a changed judgment.

## Verification and Limits

Verified the SHA-256 and complete HTML ending for each of the 1,641 selected captures, matched every canonical date to its accepted timestamp, and checked all 17 replacement record counts against the retained inspections.
Verified there are no unapplied presented decisions and no DBLP tasks in the capture backlog.
Canonical CSV hashes are unchanged by this audit.
The earlier full DBLP assessment combined fresh samples of 503 profiles with 1,138 reused assessments of identical retained captures; replacement candidates were subsequently inspected separately.
This audit reconciles that evidence and the approved decisions; it does not independently re-verify authorship of every publication or establish fresh availability for unchanged September 17–18 captures.
A Y rating therefore remains a supported profile-level judgment within the documented inspection scope, not a guarantee of a complete or error-free bibliography.

Clarified stale historical wording in the reassessment report about pending captures and the meaning of its original-profile assessment fields.
The original row audit retains rejected-profile evidence; use the current snapshot for final values.
Retained machine-readable checks and verified capture references under `../bigcows-crawler/.cache/dblp-consistency-2026-09-19-164601/`.
