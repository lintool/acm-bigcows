# CSRankings Identity Audit Using Retained Sources

## Adoption Follow-Up

The user approved all 117 historical associations on September 29, 2026.
Applied 115 Fellows and eight Turing row links with alignment date `2026-09-29`, yielding 974 linked award rows and 952 distinct canonical keys.
Original historical fields and generated CSRankings DBLP URLs are preserved; reviewed award DBLP/Scholar fields, capture dates and quality decisions are unchanged.
The source-field manifest was independently regenerated from retained sources.
Input snapshots and validation evidence are retained in `../bigcows-crawler/.cache/csrankings-adoption-2026-09-29/`.
The outcome counts, CSV proposals and audit hashes below remain the pre-adoption review snapshot; their pending actions are superseded by this approval and adoption.
No new download, extraction or visualization update occurred.

## Outcome

Completed the bounded CSRankings name-association audit for all 1,638 Fellows and 81 Turing award rows.
The [row audit](csrankings_identity_audit_2026-09-29.csv) contains 1,719 outcomes, combining earlier retained inspections with the remaining 338-Fellow inspection and a new retained-source candidate search across every blank association.
All 851 existing associations remain supported within the documented evidence scope; these represent 835 distinct CSRankings keys.
The broader historical search found 117 additional supported historical identities, represented by 123 award rows, in the already retained December 30, 2020 upstream file.
The [proposal table](csrankings_identity_proposals_2026-09-29.csv) records exact keys, original source fields, commit/hash provenance, institutional evidence and proposed actions.
These are review proposals only: all canonical files, alignment/capture dates, extracted statistics, source manifests, capture/import queues and visualization snapshots remain unchanged.

| Outcome | Fellows | Turing | Award Rows |
| --- | ---: | ---: | ---: |
| Existing association supported | 833 | 18 | 851 |
| Supported historical candidate, awaiting adoption | 115 | 8 | 123 |
| Missing association; specific misleading candidate rejected | 9 | 0 | 9 |
| Missing association; no supported candidate in bounded search | 681 | 55 | 736 |
| Total | 1,638 | 81 | 1,719 |

The original unfinished Fellows segment has 55 supported existing links, 32 supported historical proposals and 251 other missing associations.
The new candidate search also revisited earlier missing rows and the Turing roster using the full retained historical file; it does not invalidate the earlier completed Turing audit within that audit's narrower evidence scope.
No supported existing key requires removal or replacement in this review.
Missing rows are completed bounded-search outcomes, not claims that no matching profile has ever existed.

## Evidence and Limits

No CSRankings data was downloaded.
The search used all 26 retained September 18 alphabetical faculty files, the retained combined file, DBLP aliases and name-change data, the complete retained December 30, 2020 combined file, and the available partial alphabetical files from 2022, 2024, 2025 and June 2026.
There are 44 searched faculty-source files, plus the two alias/name-change files; historical-year coverage is uneven and is not a complete repository-history search.
The source and supporting-evidence hashes are in the [evidence manifest](csrankings_identity_evidence_2026-09-29.json).
All 26 current retained shard hashes match the independently recorded source manifest.
Original source fields for the 824 currently sourced and 11 accepted historical lookup keys remain protected by that manifest.

Candidate generation searched award names, retained Scholar/DBLP names and variants, upstream aliases, name changes, exact non-placeholder Scholar IDs, and relaxed surname/first-name forms, including nicknames.
Generation produced candidates for 235 of the 868 blank award rows; 132 had a name/alias or shared-ID lead stronger than the deliberately broad relaxed-name filter.
Those 132 comprise the 123 historical proposals and nine rejected misleading candidates below.
The other 103 candidate-bearing rows have only unsupported relaxed-name leads; 633 rows had no generated candidate in the selected evidence.
These counts describe candidate generation, not independent identity verification by the matcher.
Each historical proposal was assessed against the award identity/citation and corroborating institution/homepage or prior publication-profile identity evidence.
Institution changes and old affiliations were not treated as contradictions by themselves.
A shared Scholar ID or similar name alone was never sufficient to accept a candidate.

Existing Fellows inspections through row 1,300 and the Turing audit are reused and reconciled, not represented as 1,719 freshly opened websites.
The saved queue indices are retained for traceability, but joins to the current roster use award, ACM identity and year, with exact-name fallback for missing ACM URLs.
The remaining 55 linked Fellows were inspected using the source row, ACM name/citation, retained identity and affiliation evidence, and relevant retained publication examples where available.
Examples include the Emmerich/Emo Welzl, Sambasiva/S. Rao Kosaraju and Gregor V/von Bochmann name variants, the Max Planck `[INF]` tag, and disambiguated Kai Li/David Maier keys.
Later accepted profile replacements supersede older incorrect publication-profile evidence; the old Kai Li DBLP capture is not used to corroborate his Princeton identity.
The original publication-profile quality decisions were not reopened.

Selected primary institutional and recipient evidence was consulted for corroboration, including [UNLV's Hal Berghel entry](https://www.unlv.edu/news/accomplishments/hal-berghel-department-computer-science), [Kosaraju's JHU homepage](https://www.cs.jhu.edu/~kosaraju/), [Portland State's Bryant York listing](https://nanocrystallography.research.pdx.edu/nano-crystallography-group/recent-senior-collaborators/), [Sidney Karin's SDSC biography](https://www.sdsc.edu/~skarin/), [Dana Scott's CMU profile](https://www.cmu.edu/dietrich/philosophy/people/emeritus/dana-scott.html), [Emerson's UT Austin homepage](https://www.cs.utexas.edu/~emerson/) and [MIT's Minsky obituary](https://news.mit.edu/2016/marvin-minsky-obituary-0125).
These checks are separate from the retained CSRankings source dates; they do not establish current CSRankings inclusion.
This was a retained-source discovery audit, not a new general-web CSRankings search for every blank row.
Live availability, present faculty status, reasons for historical disappearance, and exhaustive historical membership remain unverified.
CSRankings-generated DBLP destinations were not fetched; URL generation and roster-derived URLs in old notes were not treated as independent identity evidence.
Where independent institutional evidence supports a key, a bad upstream Scholar identifier or generated DBLP URL is an informational discrepancy, not a request to repair upstream fields.

## Historical Proposals

All 117 proposed keys have original rows in the retained four-column upstream file at commit `4b714f69c839ca538825054f94bdf57f5d4ea3da` of December 30, 2020.
None of the selected keys exists in the September 18 alphabetical snapshot or the canonical lookup table.
The proposal table preserves original affiliation, homepage and Scholar ID; ORCID is explicitly absent from that source schema and represented as blank in the proposal.
Alternate spellings that describe the same institutional identity are retained in the row audit's candidate list; the proposed key prefers the reviewed DBLP spelling when present in the historical file.
No historical row was automatically added or restored, and no reason for absence from the newer sources is inferred.
Adoption is a separate explicit decision under the agreed review-only scope and finalized-roster policy.

The eight Turing proposals are Alfred V. Aho, Pat Hanrahan, Judea Pearl, Edmund M. Clarke, E. Allen Emerson, Richard M. Karp, Dana S. Scott and Marvin Minsky.
The first four, Karp and Scott also appear among the 115 Fellows proposals; this accounts for six duplicated award rows and 117 distinct people.
Other examples include Rebecca N. Wright, Roger B. Dannenberg, Emery D. Berger, Lawrence C. Paulson, Andrew W. Appel and John K. Ousterhout.
The CSV is the complete proposal list; the examples are not an additional queue.

Manish Gupta is a special source-disambiguation case: the historical key is literally `Manish Gupta 0001`, whereas the reviewed award DBLP name is `Manish Gupta 0002`.
The original IIIT Bangalore institution and homepage, retained institutional history, and [ACM election biography](https://www.acm.org/binaries/content/assets/acmelections/acm_india_bios_all.pdf) support the person association independently.
Preserve that original key if adopted, and do not copy its generated DBLP link or original Scholar identifier into the award roster.
On September 29, 2026, the user confirmed [Manish Gupta 0002](https://dblp.org/pid/g/ManishGupta2) and indicated that the existing [Scholar profile fHISoWoAAAAJ](https://scholar.google.com/citations?user=fHISoWoAAAAJ) also appears correct.
This resolves the user-facing profile identity question; it does not adopt the historical CSRankings association or validate all profile publications and metrics.
Bryant York and Sidney Karin illustrate that rejected sparse DBLP profiles do not preclude independently supported historical CSRankings associations.
Dana Scott's explicit Scholar N rating likewise remains unchanged.

## Rejected Candidate Matches

These outcomes reject proposed CSRankings matches only; all nine roster name-link cells were already blank.
Existing DBLP/Scholar links, quality flags and prior user holds remain unchanged.

| Fellow | Reason |
| --- | --- |
| Chen, Wei | The Microsoft network-influence/online-learning Fellow is Wei Chen 0013; the Zhejiang/Peking candidates have different disambiguators and institutional identities. No supported association. |
| Li, Li Erran | Li Erran Li is the Bell Labs/AWS wireless-network researcher; generic Li Li aliases at Monash/Beihang, USTC and Macau do not establish that identity. |
| Zhang, HongJiang | Preserve the earlier rejection: Hong Jiang 0001 at UT Arlington is not HongJiang Zhang, the multimedia researcher; a shared upstream Scholar ID is misleading. |
| Zhang, Hui | The Fellow is Hui Zhang 0001, CMU/Conviva networking researcher; Hui Zhang 0005/Hui Gary Zhang at UCL is a different institutional and research identity. |
| Clark, David D | Preserve the earlier rejection of the UCL David Clark association for the MIT Internet architect David D. Clark; old roster-derived DBLP agreement is circular evidence. |
| Gupta, Gopal Krishna | The UT Dallas Gopal Gupta source record is not supported for Gopal Krishna Gupta: the Australian Fellow was already a Monash lecturer in 1979, whereas the UTD biography records a 1985 B.Tech and 1991 Ph.D. Do not use the deliberately retained N-rated roster DBLP profile to establish a CSRankings association. |
| Chandrasekaran, B. | The Ohio State knowledge-based-systems Fellow is B. Chandrasekaran 0001; VU Amsterdam source names B. Chandrasekaran 0002/Balakrishnan Chandrasekaran 0002 are not a supported identity match. |
| Chris S Wallace | Preserve the documented rejection: the Monash researcher Christopher Stewart Wallace is not Ohio State Christopher Stewart, despite the shared Scholar identifier. |
| Johnson, David S | David S. Johnson is the AT&T/Columbia algorithms researcher; the Kansas David O./David Orville Johnson source record has a different name and institution despite a shared Scholar ID. |

The Gopal Krishna Gupta distinction is supported by [Monash's 1979 staff calendar](https://www.monash.edu/__data/assets/pdf_file/0009/2560797/1979-calendar-part-1.pdf) and [UT Dallas's Gopal Gupta biography](https://profiles.utdallas.edu/gopal.gupta).
The latter records a 1985 bachelor's degree and 1991 doctorate, incompatible with identifying the already-established 1979 Monash lecturer as that same person.
The deliberately retained N-rated DBLP association remains a prior user disposition, not evidence for accepting the CSRankings candidate.
The relaxed `Simon L. Jones` lead for Simon Peyton Jones is also unsupported: [Bath's institutional thesis evidence](https://researchportal.bath.ac.uk/files/302307246/267833720_redacted.pdf) concerns personal informatics rather than the Fellow's functional-programming identity.
Other relaxed-name leads remain in the row audit without being elevated to accepted matches.

## Earlier Follow-Ups

Peter Bartlett, Larry Davis, Joseph Hellerstein, Allan Gottlieb, Laxmi Bhuyan and John Hopcroft already have accepted historical source provenance from the September 18 recovery.
Their earlier pending notes are explicitly superseded by that recovery; none is reopened.
The earlier five historical keys for Donald Greenberg, Georg Gottlob, Judith S. Olson, Luca Cardelli and Ruby B. Lee remain supported.
Existing known upstream identifier errors, including those documented in the trial and full reviews, remain informational once independent identity evidence supports the name association.
The completed name-association audit is distinct from a combined 5,157-row three-service audit, which is not assembled by this CSRankings-only task.

## Validation

- The full offline Python suite passes, including canonical joins, shared identities, source preservation, search-history coverage and unchanged visualization synchronization.
- The audit has exactly one row per current award row, with exact recipient/year coverage and no duplicates.
- All 123 proposal rows resolve literally to the retained source, represent 117 unoccupied keys, and agree for shared ACM recipients.
- Protected-file hashes confirm no changes to canonical datasets, dates, source manifests, capture/import queues or visualization data.
- `git diff --check` passes.

No extraction, import, source refresh, visualization regeneration, staging, commit or publication occurred.
