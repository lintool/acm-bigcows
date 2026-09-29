# First Ten Missing Scholar Links — September 28, 2026

Current disposition: the user [rejected the invalid directory leads](#user-rejection-of-invalid-directory-leads); none remains open from this batch.
The discovery outcomes below retain their original evidence and must be read with the subsequent user decisions.

Reviewed the first ten blank Scholar links in current ACM Fellows roster order using general web searches and selective source-page inspection.
Outcome: one supported identity candidate, two unresolved directory leads, six profiles not located, and one previously rejected candidate with no verified alternative.
The initial discovery changed no canonical data; the subsequent user acceptance below records the approved link and quality change.
The search does not establish current availability or full profile quality.
Search batches were spaced by 15 seconds, generally with one or two queries per batch.
No bulk crawler was run, no visualizations were regenerated, and no recurring task was created.
The browser tool returned internal errors for several source pages; a single direct directory request returned HTTP 403 and was not retried.

## Subsequent User Acceptance

The user accepted Athina Markopoulou's match after this discovery pass.
Her canonical Scholar URL is now `https://scholar.google.com/citations?user=WIXl6-gAAAAJ`, with quality Y based on the supported identity and relevant inspected publication sample.
The capture date remains blank, and no statistics were imported; the older indexed 20-entry page does not establish a fresh capture or complete/recent bibliography coverage.
Her new capture/import task is recorded in the canonical queue; the discovery results below preserve the initial findings.

## Results

Search timestamps and current dispositions are indexed in the [separate search-history CSV](../data/google_scholar_profile_searches.csv).
The table below retains the original discovery outcomes; subsequent acceptance is recorded above.

| Roster Row | Fellow | Outcome | Evidence and Limitation |
| --- | --- | --- | --- |
| 3 | Allman, Eric | not_found | No direct profile located; DBLP generic Scholar search links are not profile matches. |
| 20 | Dukkipati, Nandita | unresolved_lead | [Candidate or lead](https://adscientificindex.com/scientist/weitao-wang/5646789/). Directory lists Nandita Dukkipati, Google LLC, with a Scholar link; destination could not be resolved by browser tool. A direct directory fetch returned 403 and was not retried. |
| 38 | Markopoulou, Athina | supported_identity_candidate | [Candidate or lead](https://scholar.google.com/citations?user=WIXl6-gAAAAJ). Scholar page returned by web tool identifies UCI professor with verified uci.edu email and 20 coherent networking/privacy entries. Tool labels capture approximately 1.8 years old; not a fresh live capture or full quality verification. |
| 85 | Crocker, Stephen David | not_found | Steve/Stephen Crocker searches did not locate a direct profile. |
| 98 | Housley, Russell | not_found | Russ/Russell Housley searches did not locate a direct profile. Scholar link in IETF quoted email belongs to another researcher, not Housley. |
| 105 | Madni, Azad M | not_found | Azad/Azad M. Madni searches did not locate a direct profile; generic publisher author-search links excluded. |
| 120 | Walid, Anwar | unresolved_lead | [Candidate or lead](https://adscientificindex.com/scientist/jaehyun-hwang/1302244/). Directory lists Anwar Walid (Elwalid), Bell Labs, with Scholar link; actual profile ID unresolved. Columbia and DBLP support networking identity/name variants, not the candidate URL. |
| 135 | Berners-Lee, Tim | not_found | No direct profile found; UOC library guide explicitly describes a preconfigured Scholar search, not a personal profile. |
| 152 | Goldberg, Ian | not_found | Waterloo institutional sources corroborate identity and research; no direct Scholar profile found. |
| 190 | Varma, Manik | previously_rejected | [Candidate or lead](https://scholar.google.com/citations?user=2efybZkAAAAJ). Existing September 18 report rejected this correct-person candidate for contamination; no verified alternative found. Current search surfaces directory/alphaXiv leads but does not establish a different ID or changed quality. Preserve rejection. |

## Identity Evidence and Next Steps

[Athina Markopoulou's Scholar page](https://scholar.google.com/citations?user=WIXl6-gAAAAJ) identifies her as a UCI EECS professor, with verified university email and network measurement/privacy interests.
The 20 visible entries include Facebook sampling with Gjoka/Kurant/Butts, IP backbone failures, PhishDef, AntMonitor and smart-home traffic signatures; these converge with her ACM citation and [university group's publications](https://athinagroup.eng.uci.edu/publications/).
The web tool reports the Scholar content as approximately 1.8 years old; retain it as discovery evidence, not a fresh capture or approved statistics import.
Dukkipati and Walid were initially retained as leads because their actual Scholar IDs were not resolved; the user subsequently rejected both directory leads as invalid.
The [prior Varma rejection](check_profiles_full_2026-09-18.md#rejected-discovery-candidate) remains in effect; a fresh quality assessment was not performed.
A failed search does not prove that a public profile does not exist.

## Search Log

All searches were performed September 28, 2026.
- `"Eric Allman" "Google Scholar"`
- `"Nandita Dukkipati" "Google Scholar"`
- `"Athina Markopoulou" "Google Scholar"`
- `"Steve Crocker" "Google Scholar" profile`
- `"Russ Housley" "scholar.google.com/citations"`
- `"Azad Madni" "Google Scholar"`
- `"Anwar Walid" "Google Scholar"`
- `"Tim Berners-Lee" "scholar.google.com/citations"`
- `"Ian Goldberg" "Google Scholar" Waterloo`
- `"Manik Varma" "Google Scholar"`
- `"Athina Markopoulou" "citations?user"`
- `"Anwar Elwalid" "citations?user"`
- `"Nandita Dukkipati" scholar profile Google`
- `"Anwar Walid" scholar profile Bell Labs`
- `"Eric Allman" site:scholar.google.com/citations`
- `"Stephen Crocker" site:scholar.google.com/citations`
- `"Azad M. Madni" site:scholar.google.com`
- `"Russell Housley" "Google Scholar"`
- `"Ian Goldberg" site:scholar.google.com/citations`
- `"Tim Berners-Lee" "Google Scholar" profile`
- `"Anwar Walid" "Elwalid" "Google Scholar"`
- `"Nandita Dukkipati" "scholar.google"`

The row-level search record is retained in `../bigcows-crawler/.cache/scholar-discovery-first10-2026-09-28/search-review.json`.

## User Rejection of Invalid Directory Leads

At 2026-09-28T22:40:26.252611-04:00, the user rejected the directory leads for Dukkipati, Nandita, Walid, Anwar as invalid.
These cases are closed with search outcome `not_found`: no matching Scholar author-profile ID was established.
The original discovery observations above remain historical provenance, not active recommendations.
Search timestamps and blank candidate URLs are preserved; no profile identity or publication-quality rejection is inferred from this directory-lead decision.
Canonical Scholar links remain blank, and no new searches or crawls were performed.
