# Scholar Quality Recalibration — September 28, 2026

The user requested a lenient standard: contamination below roughly 20% is acceptable.
This supersedes the proposed dispositions in the [original holistic audit](scholar_holistic_review_2026-09-28.md), preserving its observations as historical evidence.
The initial recalibration used existing evidence; subsequent explicit user decisions are now applied as recorded below.

## Resolved User Decisions

At 2026-09-28 17:21 EDT, the user explicitly rated Lixin Gao, Robert Morris, Michael F. Cohen and Dana Scott N, and Yorick Wilks Y.
These decisions are applied to all matching award-roster rows, superseding the proposals below.
The current review queue is empty; the recalibration ledger retains the original proposals alongside the final user decisions.
All profile URLs, capture dates, metrics and visualizations remain unchanged.
Dana Scott's explicit N overrides the earlier lenient boundary recommendation; Yorick Wilks's explicit Y resolves the attribution review.
The original observations remain historical evidence and do not reopen these resolved cases.

## Historical Recalibrated Proposals

Of the original 35 proposed N profiles, 31 were recommended to retain Y below the user's approximate tolerance, and Dana Scott was recommended to retain Y as a borderline case at 20%.
Three remained proposed N for review: Lixin Gao (33 flagged entries out of 100), Robert Morris (24/100), and Michael F. Cohen (22/100).
Of the eight previously borderline profiles, seven were recommended to retain Y under the lenient tolerance; Yorick Wilks remained uncertain because 22/100 flagged entries may include legitimate chapters or editorial contributions aggregated into book records.
Thus 38 of the original 43 flags were closed under the revised tolerance; the then-current queue, now resolved, retained five profiles: three proposed Ns and two boundary/attribution cases retaining Y.
The [recalibration ledger](scholar_recalibration_2026-09-28.csv) records all 43 profiles and their 46 award rows, including the original rationales and revised dispositions.
Existing N ratings and prior explicit decisions remain preserved; the new tolerance does not automatically reopen those historical cases or change coverage and identity requirements.

| Profile | Flagged Entries / Captured Entries | Revised Proposal |
| --- | ---: | --- |
| Lixin Gao | 33/100 | N for review |
| Robert Morris | 24/100 | N for review |
| Michael F. Cohen | 22/100 | N for review |
| Dana Scott | 20/100 | Retain Y; borderline under the approximate tolerance |
| Yorick Wilks | 22/100 | Retain Y; attribution remains uncertain |

## Meaning and Limits of the Fractions

Counts deduplicate the entry numbers explicitly identified in the original audit rationales, not the publications themselves.
The denominator is each retained most-cited 100-entry capture; this is not an estimate of the entire profile or a citation-weighted fraction.
Flagged entries are suspected attribution problems, with differing certainty; the counts are neither certified contamination rates nor upper bounds.
A missing exact DBLP title match is not counted as contamination by itself.
The user-approved leniency governs the current proposals despite these sampling limits; below-threshold cases are not claims of error-free bibliographies.
The initial recalibration changed no canonical data; the subsequent user decisions changed only the authorized quality flags.
No new crawling, browsing, metric import or visualization regeneration was performed.

## Current Canonical Outcome

| Scholar Status | ACM Fellows | Turing Winners | Award Rows | Distinct Linked Profiles |
| --- | ---: | ---: | ---: | ---: |
| Linked Y | 1,241 | 38 | 1,279 | 1,251 |
| Linked N | 13 | 2 | 15 | 13 |
| Missing link | 384 | 41 | 425 | — |

The [current review queue](scholar_recalibration_queue_2026-09-28.csv) is empty.
The original full audit ledger and initial queue preserve historical proposals; the recalibration ledger records the final dispositions for all 43 original flags.
Quality approval does not accept capture dates or import statistics; the separate four-task capture/import backlog remains documented in the [status index](profile_review_status.md).
Paulson's subsequent [100-entry capture and review](paulson_scholar_import_2026-09-28.md#latest-accepted-capture-100-entries) is accepted with quality Y, superseding his earlier 20-entry review limitation.

## Validation

All 43 originally flagged profiles and 46 award rows have revised dispositions, with shared-recipient decisions consistent across rosters.
All 43 denominator counts are 100; 38 profiles were accepted under the tolerance and the five remaining cases are now resolved.
Five quality cells changed across the two rosters; Wilks’s existing Y was reaffirmed.
All 40 canonical-data tests and `git diff --check` passed after applying the user decisions.
Original audit evidence and explicit historical ratings are preserved.
