# Current Profile Review Status

## Current Workflow Stages

Use the [four-stage workflow](../README_FOR_AGENTS.md#four-stage-workflow) to distinguish evidence collection, review decisions, canonical extraction and displayed snapshots.

| Stage | Current State |
| --- | --- |
| Crawl | Current linked Scholar profiles have retained successful captures; no new fetch is scheduled by this index. |
| Review | Scholar identity/quality decisions are complete within documented sampling limits, including the 19 subsequently approved profiles; DBLP review is complete within its scope; the bounded CSRankings identity audit is complete, with all 117 approved historical associations adopted. |
| Extract | All 1,279 stored Scholar profiles have statistics from the accepted selected captures; DBLP metadata and publication-year aggregates for all 1,641 stored profiles are extracted into `data/dblp_extracted_data.json`; the canonical capture/import gap queue is empty. |
| Visualize | Both September 29 snapshots still match their canonical visualization inputs, and snapshot/renderer checks pass; CSRankings associations are not consumed by these timelines, so their later adoption does not require regeneration. |

The gap queue is not a stage tracker; an empty queue alone cannot prove that review is complete, all newer captures are extracted or visualizations are synchronized.

## CSRankings Identity Audit

The [September 29 retained-source audit](csrankings_identity_audit_2026-09-29.md) records outcomes for all 1,719 award rows, completing the previously unfinished 338-Fellow segment and reconciling earlier inspection notes.
The 851 previously existing award-row associations remain supported within the documented evidence scope.
The user approved and adopted 117 additional historical identities across 123 award rows: 115 Fellows and eight Turing rows, with six shared recipients.
Canonical coverage is now 974 award-row associations (948 Fellows and 26 Turing rows), representing 952 distinct keys, including 128 historical keys.
The [proposal table](csrankings_identity_proposals_2026-09-29.csv) records exact original source fields and evidence; its review-time recommendations were adopted on September 29, with alignment dates set to `2026-09-29`.
Reviewed publication links, quality ratings and capture dates are unchanged; Manish Gupta retains DBLP 0002 and Scholar fHISoWoAAAAJ independently of his historical source key.
Nine recipient cases have rejected candidate associations: seven have wrong-person findings and the user confirmed unsupported matches for Wei Chen and Li Erran Li.
Another 736 award rows have no supported match in the bounded retained-source search.
The earlier six historical-source gaps remain resolved.
No CSRankings download, canonical extraction, import or visualization update occurred.
Current CSRankings membership and exhaustive historical coverage are not established by this audit.

## Profile-or-Search Coverage

The September 29 consistency sweep confirms that every row in both award rosters has a profile link or a recorded search for each publication service.
Fresh [CSRankings searches](csrankings_missing_search_2026-09-29.md) now cover all 745 blank-link award rows, deduplicated to 704 people; no additional supported matches were found.
The new ledger contains only these fresh retained-source attempts, with no backfill of earlier audits or already linked recipients.
The user confirmed leaving Wei Chen and Li Erran Li unlinked; their six candidate keys are classified as unsupported matches, with no further user decision pending.
These are award-row counts; recipients shared across rosters appear in both totals.

| Service | Roster | Linked | Blank With Search | Neither |
| --- | --- | ---: | ---: | ---: |
| Google Scholar | ACM Fellows | 1,269 | 369 | 0 |
| Google Scholar | Turing Winners | 40 | 41 | 0 |
| DBLP | ACM Fellows | 1,623 | 15 | 0 |
| DBLP | Turing Winners | 81 | 0 | 0 |
| CSRankings | ACM Fellows | 948 | 690 | 0 |
| CSRankings | Turing Winners | 26 | 55 | 0 |

Links rated N count as linked; a search record does not establish that a matching profile exists or is currently available.
The offline `tests/test_profile_searches.py` regression check enforces coverage and ledger integrity without fetching sources.

## Review History and Scope

This is the current progress and open-work index for the September 18–19, 2026 reviews and the September 28 Scholar capture checkpoint and holistic audit.
**DBLP is in an approved state across both award rosters: the review is complete within its documented scope, all user decisions are applied, every stored link has an accepted capture, and no DBLP decision or capture task is pending.**
Approved N ratings, four user-approved holds and 15 missing-link Fellow rows remain intentional; approved state does not mean every profile is rated Y.
The [September 29 missing-DBLP search](dblp_missing_search_2026-09-29.md) records fresh attempts for all 15 blank-link Fellows in the prospective [DBLP search ledger](../data/dblp_profile_searches.csv): six rediscovered excluded profiles and nine not-found replacement searches, with no supported new candidates.
Existing linked profiles were excluded, no historical searches were backfilled, and all earlier decisions remain in force.
The [detailed report](check_profiles_full_2026-09-18.md) retains historical observations and the 18 explicit user dispositions.
The [September 28 Scholar holistic audit](scholar_holistic_review_2026-09-28.md) is complete within its existing-evidence sampling limits: all 1,264 distinct linked profiles were individually judged and all 1,719 award rows have recorded outcomes, including 425 blank links.
The [user-directed lenient recalibration](scholar_recalibration_2026-09-28.md) accepts 38 of the original 43 flags under a roughly 20% contamination tolerance.
All five remaining cases are now resolved by explicit user decisions: Lixin Gao, Robert Morris, Michael F. Cohen and Dana Scott are N; Yorick Wilks is Y.
The decisions are applied across both rosters where present, and the [current Scholar review queue](scholar_recalibration_queue_2026-09-28.csv) is empty; preserve these explicit decisions.
Current canonical Scholar totals are 1,265 distinct linked Y profiles and 14 distinct linked N profiles: Fellows have 1,255 linked Y, 14 linked N and 369 blank links; Turing winners have 38 linked Y, two linked N and 41 blank links.
The original audit ledger and proposal queue are historical; the [final disposition ledger](scholar_recalibration_2026-09-28.csv) supersedes their pending recommendations.
Complete/recent publication coverage and live availability remain unverified.
The September 29 retained-source CSRankings identity audit is complete; its 117 historical proposals are now adopted as canonical associations.
The separately authorized [September 28 Scholar refresh](scholar_capture_checkpoint_2026-09-28.md) has 1,263 successful captures and one recorded redirect across 1,264 distinct input URLs; Paulson’s retained destination capture has now been accepted and imported; four more captures are now imported in the [nineteen-profile import](scholar_reviewed19_import_2026-09-28.md); the remaining 1,259 profiles are now imported in the [September 29 full statistics update](scholar_full_import_2026-09-29.md).
The user has since confirmed Paulson’s destination ID `x4toSGEAAAAJ`, and his canonical link is corrected; a subsequent user-authorized targeted Safari crawl captured 100 entries at 2026-09-28 22:17:11 UTC, reviewed and accepted as documented in the [Paulson import report](paulson_scholar_import_2026-09-28.md#latest-accepted-capture-100-entries).
Its reported statistics and date match the already imported values; both canonical dates remain 2026-09-28.
Paulson’s capture/import task is complete; all 100 captured entries were inspected with no apparent unrelated cluster, and quality Y is retained.
Complete bibliography and recent-sorted coverage remain unverified.
Canonical Scholar extraction now lives in `data/google_scholar_extracted_data.json` with native field types and per-profile capture provenance; historical CSV filenames below refer to their original checkpoints.
Both award visualization snapshots were regenerated with explicit user authorization on September 29 and pass the full snapshot-synchronization checks.
No new crawl or source refresh is authorized by maintaining this index.
The lookup table now preserves [CSRankings-generated DBLP links](../README_FOR_AGENTS.md#csrankings-dblp-link-generation), independently of reviewed award links.
Historical audits and saved resume scripts used roster-derived lookup URLs; update any such writer to regenerate from source names before applying another checkpoint.
Do not restore their old DBLP cells or blank exceptions, and do not treat their agreement with award URLs as independent corroboration.

The subsequent [first-ten missing-link search](scholar_missing_first10_2026-09-28.md) found one supported identity candidate (Markopoulou) and two initially unresolved directory leads (Dukkipati and Walid, subsequently rejected as invalid); the user subsequently accepted Markopoulou’s link with quality Y, and its capture date and metrics are now imported.
This discovery follow-up is separate from the closed quality-review queue and the now-completed 19 canonical capture/import tasks.
The subsequent [next-thirty search](scholar_missing_next30_2026-09-28.md) initially recorded two supported identity candidates (Mount and Jackson), five further exact-ID candidates, one initially unresolved lead (subsequently rejected as invalid), 19 profiles not located and three preserved prior rejections.
The user subsequently reported Jackson’s `PXY96lkAAAAJ`, Gerla’s `mO3xwbwAAAAJ` and Kannan’s `4oW5Q1wAAAAJ` links inaccessible; all three are on hold.
The user also rejected Leino’s `mGYQLekAAAAJ` candidate as pointing to the wrong person; keep his canonical Scholar link blank and do not reintroduce the rejected association from directory evidence.
Jackson’s, Gerla’s and Kannan’s canonical Scholar links remain blank; old indexed content and third-party links do not establish current availability.
The user subsequently supplied and approved different URLs for Mount, Mei and Ricart; browser checks identified all three, and their links and Y ratings are applied with accepted capture dates and imported metrics.
See the [acceptance evidence](scholar_missing_next30_2026-09-28.md#subsequent-user-accepted-profiles); their old candidate IDs remain superseded history.
The [Scholar search-history CSV](../data/google_scholar_profile_searches.csv) now records 429 candidate/search rows across 392 recipients from fifteen Fellows discovery batches and the [September 29 Turing search](scholar_missing_turing_2026-09-29.md), including 15 accepted profile associations, three superseded candidates and subsequent user corrections.
Its search timestamps track completed discovery work separately from review decisions and successful capture dates; see the [schema and maintenance rules](../README_FOR_AGENTS.md#scholar-search-history).

The [third discovery batch](scholar_missing_batch3_2026-09-28.md) adds 30 searches: one accepted profile (Kasik, Y after browser/DBLP review and user approval), one initially unresolved lead (Kitsuregawa, subsequently rejected as invalid), 21 initially not found, five unavailable/invalid associations and two excluded namesakes after the user reported Barroso’s `7stTzUMAAAAJ` URL invalid.
Barroso is excluded from actionable recommendations; preserve his blank canonical link and the [user decision](scholar_missing_batch3_2026-09-28.md#subsequent-user-decision).
Kasik’s link and Y rating are applied with an accepted capture date and imported metrics; the other third-batch dispositions remain unchanged.
See the [Kasik assessment](kasik_scholar_review_2026-09-28.md) for all 122 displayed Scholar entries, retained DBLP comparison and limited attribution noise.
All 369 missing-link Fellows now have search-history CSV records; zero remain without a recorded search.
This completes bounded Fellows discovery, including held and rejected associations; older Data Notes searches are not comprehensively backfilled and the linked-profile quality audit is a separate workflow.
All 41 blank-link Turing winners also have fresh recorded general-web searches: no supported new candidates, 34 not-found replacement searches, four preserved wrong-person exclusions and three preserved unavailable holds.
No new Scholar capture, availability verification, canonical association, quality change or visualization regeneration was performed.

The [fourth discovery batch](scholar_missing_batch4_2026-09-28.md) covers 25 more Fellows: Fischer is a user-approved Y profile with one suspect entry among 20 inspected; full/recent coverage remains unassessed.
The batch also records 18 not found, five unavailable associations (three freshly observed 404s and two preserved prior holds), and Shyamasundar’s preserved rejection.
Fischer’s link and Y rating are applied; his capture date and metrics are now imported.

The [fifth discovery batch](scholar_missing_batch5_2026-09-28.md) covers 25 more Fellows: Fayyad and Brooks are user-approved Y profiles based on live 20-entry samples; full/recent coverage remains unassessed.
Their links and Y ratings are applied with accepted capture dates and imported metrics; see the [acceptance record](scholar_missing_batch5_2026-09-28.md#subsequent-user-acceptance).
It records 17 not found, three unavailable associations and three recipients with wrong-person associations, plus an additional wrong-person Motwani candidate.
Norvig, Vianu and Dubois retain prior dispositions; Motwani’s plausible candidate returned a visible 404, and directory associations for Motwani, Umesh Vazirani and Bubenko resolved to other people.

The [sixth discovery batch](scholar_missing_batch6_2026-09-28.md) covers 25 more Fellows, from Schroeder through Parker: no new supported profile, 23 not found and two unavailable associations.
Grosz’s directory candidate returned a visible 404; Schroeder retains the prior hold without a new direct fetch.
Sohi and Iyer directory links were placeholders, and Ferrari’s link was a general Scholar search; no exact profile was established for these leads.

The [seventh discovery batch](scholar_missing_batch7_2026-09-28.md) covers 25 more Fellows, from Pohl through Lewis: Bhuyan is a user-approved Y profile based on a live 20-entry sample, with full/recent coverage still unassessed.
His Scholar link and Y rating are applied with an accepted capture date and imported metrics; see the [acceptance record](scholar_missing_batch7_2026-09-28.md#subsequent-user-acceptance).
It also records two unavailable associations (Schlichting’s newly observed 404 and Steinmetz’s prior hold) and 22 searches without a supported profile, preserving Banerjee’s and Williams’s earlier rejections.

The [eighth discovery batch](scholar_missing_batch8_2026-09-28.md) covers 25 more Fellows, from Martin through Rangan: Agrawal and Lam are user-approved Y profiles based on live 20-entry samples.
The user accepted Jones’s link with quality N after five suspect entries among 20 inspected (25%); preserve this explicit decision.
All three links are applied with accepted capture dates and imported metrics; see the [acceptance record](scholar_missing_batch8_2026-09-28.md#subsequent-user-acceptance).
The batch also preserves Clarke’s unavailable hold and records 21 searches without a supported profile ID; full/recent coverage remains unassessed.

The [ninth discovery batch](scholar_missing_batch9_2026-09-28.md) covers 25 more Fellows, from Ryder through Akeley: Ryder and Akeley are user-approved Y profiles based on live 20-entry samples, with no obvious unrelated entries.
Both links and Y ratings are applied with accepted capture dates and imported metrics; full/recent coverage remains unassessed.
See the [acceptance record](scholar_missing_batch9_2026-09-28.md#subsequent-user-acceptance).
The batch also preserves Pratt’s unavailable hold and records 22 searches without a supported profile, including preservation of Shaw’s prior namesake exclusion.

The [tenth discovery batch](scholar_missing_batch10_2026-09-28.md) covers 25 more Fellows, from Borg through Yovits: no usable new profile was established.
Ferrante’s directory link returned a visible Scholar 404; Wasserman’s unavailable hold and Savage’s earlier namesake exclusion remain preserved.
The batch records two unavailable associations and 23 searches without a supported author-profile ID.

The [eleventh discovery batch](scholar_missing_batch11_2026-09-28.md) covers 25 more Fellows, from Abrahams through Preparata: Dorothy Denning is a user-approved Y profile based on a live 20-entry sample, with no obvious unrelated entries.
Her link and Y rating are applied with an accepted capture date and imported metrics; full/recent coverage remains unassessed.
See the [acceptance record](scholar_missing_batch11_2026-09-28.md#subsequent-user-acceptance).
The batch also preserves Booch’s unavailable hold, excludes the battery-research Goodenough namesake, and records 22 searches without a supported author-profile ID.

The [twelfth discovery batch](scholar_missing_batch12_2026-09-28.md) covers 25 more Fellows, from Snyder through Cerf: no new confirmed match, two wrong-person exclusions (Yao and Evans), and 23 searches without a supported ID.
The user [rejected Yao’s c8Gq7AkAAAAJ association](scholar_missing_batch12_2026-09-28.md#subsequent-user-decision) as wrong; the review item is closed.
Keep his Scholar link blank in both award rosters and do not restore the rejected ID from directory evidence.
The 19-task discovery-era capture/import backlog is now resolved by the subsequent import.

The [thirteenth discovery batch](scholar_missing_batch13_2026-09-28.md) covers 25 more Fellows, from Chamberlin through Green: no new supported candidate, 23 not found, Dijkstra’s historical unavailable hold and Goldberg’s preserved wrong-person exclusion.
DeFanti’s NRP source could not be retrieved and did not establish an exact ID; the source limitation is retained in the report.
No canonical links or capture/import tasks changed.

The [fourteenth discovery batch](scholar_missing_batch14_2026-09-28.md) covers 25 more Fellows, from Hammer through McCluskey: no new supported candidate, 21 not found, three wrong-person associations and McCarthy’s historical unavailable hold.
The Hartmanis directory association points to John Hopcroft in indexed Scholar content; Lindsay’s and Liu’s earlier exclusions remain preserved.
No canonical links or capture/import tasks changed.

The [final Fellows discovery batch](scholar_missing_batch15_2026-09-28.md) covers the remaining 39 Fellows, from McCracken through Wulf, using 60 paced queries.
No new supported candidate was found: 37 not found, Simon’s historical unavailable hold and Stonebraker’s preserved wrong-person association.
Milner’s prior user rejection remains preserved; no canonical links or capture/import tasks changed.

## Progress

| Work | Current State | Next Step |
| --- | --- | --- |
| September 28 Scholar holistic audit | Complete using retained evidence; 1,264 linked profiles inspected, all 1,719 award rows recorded | [Five user decisions applied](scholar_recalibration_2026-09-28.md#resolved-user-decisions); no pending quality decisions, broader coverage limits explicit; no new crawling. |
| September 28 Scholar refresh | All 1,264 distinct URLs attempted; 1,263 original successful captures plus Paulson’s resolved redirect and subsequent successful 100-entry capture; crawl stopped | All original successful captures and Paulson’s subsequent destination capture are accepted and imported; the 69 heuristic name flags were covered by the completed holistic audit; no restart scheduled. |
| DBLP-only September 19 reassessment | All 1,719 award rows have recorded outcomes; the four new coverage flags are resolved and applied as N | Preserve the [four user-approved holds](dblp_reassessment_review_queue_2026-09-19.csv); all presented decisions are applied. |
| Fellows 1–100 | Trial audit recorded for 100 recipients and 300 services | Preserve the [trial outcomes and evidence limits](check_profiles_trial_100_2026-09-18.md). |
| Fellows 101–1,300 | Earlier individual inspection notes reconciled in the September 29 CSRankings identity audit | Preserve resolved decisions; the supported historical proposals have been adopted. |
| Fellows 1,301–1,638 | CSRankings identity inspection complete: 55 supported existing links, 32 historical proposals and 251 other missing associations | No further initial CSRankings inspection is pending in this segment; the 32 proposed historical associations are now adopted. |
| Turing Award roster | All 81 rows have the earlier 243 service outcomes; the September 18 decisions and Hopcroft historical link are applied | September 29 CSRankings review adds eight approved and adopted historical associations; existing Scholar and DBLP outcomes are preserved. |
| Explicit user dispositions | The earlier 18 cases, three DBLP quality decisions and five further profile decisions are resolved and applied | Preserve the [earlier decisions](check_profiles_full_2026-09-18.md#explicit-user-decisions) and all [subsequent Turing decisions](check_profiles_turing_2026-09-18.md#subsequent-user-decisions), including the rejected Manuel Blum Scholar ID. |
| Rob Cook DBLP candidate | Approved and applied as Y in batch three | Captured and imported September 19. |
| Final service audit | The full 5,157-assessment audit is not assembled | Combine the separate completed service audits if requested, retaining their evidence limits and the completed CSRankings adoption decision. |
| Visualization | Both award snapshots regenerated September 29 from the latest canonical statistics, dates and quality flags | The full Python suite, including snapshot synchronization, and JavaScript renderer checks pass. |

The saved notes extend through Fellow 1,300, although the last bulk CSV checkpoint was through Fellow 1,285 before the subsequent user dispositions.
These are different milestones; the earlier checkpoint totals are historical.
Rob Cook's saved proposal is [c/RobertLCook](https://dblp.org/pid/c/RobertLCook), with 14 inspected records and a documented contextual coverage rationale.
It is now an accepted CSV value rated Y with an accepted September 19 capture.
The user subsequently rejected Shyamasundar, Rudrapatna K's Scholar association `gNhIpRwAAAAJ`; its URL, capture date and imported statistics were removed, with quality retained as `N`.
Do not restore that association from earlier review artifacts.

## DBLP Reassessment and Review Queue

The [DBLP consistency audit](dblp_consistency_2026-09-19.md) verifies all current links, quality dispositions and 1,641 capture hashes, with no new decision required.
The [current row snapshot](dblp_current_status_2026-09-19.csv) separates final values from the historical original-profile audit.

The [September 19 DBLP reassessment](dblp_reassessment_2026-09-19.md) records every Fellow and Turing row separately, reusing evidence for shared recipients.
After seventeen approved replacements, 1,598 distinct stored profiles are supported as Y within the recorded sampling scope and 43 distinct linked profiles remain N.
The user explicitly rated Burton Smith, Chung-Jen Tan, Aaron Finerman and Herbert Grosch N; all four changes are applied, with URLs and capture dates preserved.
These four coverage cases are resolved and must not be reopened from the initial pending-review text.
The 15 Fellows without stored DBLP links remain missing-link cases; prior rejections are preserved.
The [four-case review queue](dblp_reassessment_review_queue_2026-09-19.csv) retains only user-approved holds: Gupta, Adams, Friedman and Harris.
The [first five replacement recommendations](dblp_replacement_recommendations_2026-09-19.md) now support different candidate profiles for Robert Constable, Richard P. Gabriel, David S. Johnson, Kai Li and Allen Tucker, each approved and applied as Y.
The user approved all five replacements; their new URLs and Y ratings are applied, and September 19 captures have now been accepted.
The [second recommendation batch](dblp_replacement_recommendations_batch2_2026-09-19.md) is approved and applied: Y replacements for Dhiraj Pradhan, Ahmed Sameh, John Rice and J. Nievergelt; David MacQueen was initially held, then explicitly switched by the user to [84/3383](https://dblp.org/pid/84/3383), retaining N for coverage; its replacement capture is now accepted with a September 19 date.
All four holds retain their existing URLs, N ratings and capture dates; no further user decision is requested without new evidence.
The [third recommendation batch](dblp_replacement_recommendations_batch3_2026-09-19.md) is approved and applied: seven Y replacements for Cook, Miller, Goodenough, Kim, Hillis, Lindsay and Liu; N holds for Gupta, Adams, Friedman and Harris.
The batch corrects Lindsay’s discovery lead to Bruce G. Lindsay 0001 and identifies Frank L. Friedman’s candidate, whose coverage remains insufficient for Y.
The [74-case exception inventory](dblp_reassessment_exceptions_2026-09-19.csv) additionally includes known N cases without a new action and the missing links.
Other replacement leads are not accepted good-quality profiles; several earlier direct candidate inspections encountered access failures.
The four authorized quality downgrades and seventeen approved replacements are applied; the earlier gap-fill evidence remains intact.
This DBLP outcome inventory includes 503 freshly sampled profiles and 1,138 reused content assessments of identical retained captures.
That DBLP review did not complete the CSRankings portion of the earlier full-service review; the September 29 CSRankings audit now records the name-association outcomes, and the separate September 28 Scholar audit supplies the retained-evidence Scholar outcomes.

## Unresolved Scholar Discovery Leads

No unresolved Scholar discovery leads remain.
The user rejected the four directory leads for Nandita Dukkipati, Anwar Walid, Ricardo Bianchini and Masaru Kitsuregawa as invalid.
Their search outcomes are now `not_found`, with blank candidate URLs and original search timestamps preserved; this does not assert that no matching profile exists.
See the recorded decisions in [batch one](scholar_missing_first10_2026-09-28.md#user-rejection-of-invalid-directory-leads), [batch two](scholar_missing_next30_2026-09-28.md#user-rejection-of-invalid-directory-leads) and [batch three](scholar_missing_batch3_2026-09-28.md#user-rejection-of-invalid-directory-leads).
The 19 accepted-link capture/import tasks were subsequently completed after user approval.

## Capture and Import Backlog

The [September 19 gap fill](dblp_gap_fill_2026-09-19.md) captured and imported all 84 accepted DBLP links that lacked capture dates, filling 87 award-roster cells.
That gap fill completed the then-accepted URLs.
The [replacement gap fill](dblp_replacement_captures_2026-09-19.md) captured all seventeen subsequently approved DBLP URLs and imported their September 19 capture dates.
All 1,641 distinct stored DBLP profiles have accepted captures; no DBLP capture gap remains.
The [machine-readable queue](profile_capture_queue.json) is empty.
The user reviewed and approved all 19 pending Scholar profiles; their retained 100-entry captures are now accepted, metrics imported and Fellow dates populated, as documented in the [import report](scholar_reviewed19_import_2026-09-28.md).
This includes the fifteen new captures and the earlier captures for Inverardi, Abramson, DeMillo and Vishwani Agrawal.
Existing quality decisions are preserved, including Neil Jones's N; no further fetch is needed for these completed tasks.
All 1,279 current stored Scholar links now have accepted capture dates and statistics from their latest selected captures, including the completed broad refresh and subsequent targeted captures.
Missing links and unadopted discovery candidates remain outside this queue.
Use the [queue-generation workflow](../README_FOR_AGENTS.md#capture-and-import-backlog) after relevant CSV updates, then update these counts.

## Resolved Unavailable Scholar Candidates

The user instructed removal of all failed Scholar candidates on September 18 at 16:01 EDT.
The 13 discovery cases below and the historical candidates for Herbert Simon, Edsger Dijkstra and John McCarthy are resolved: their award-roster links and dates remain blank with quality `N`.
All 19 affected award rows (16 Fellows and three Turing rows) already had those values, and none of the failed IDs occurs in the canonical Scholar statistics table, so no CSV edits were needed.
The links below are retained as historical evidence, not an active review queue or accepted associations.
Victor Vianu's original CSRankings `scholarid` remains untouched under the user's source-preservation policy.
The observations were made on September 18 and do not establish intentional withdrawal.
Do not restore an association from search-index text or treat retained evidence as proof of current availability.

| Person | Candidate | Recorded Finding |
| --- | --- | --- |
| Elena Ferrari | [kOc4beIAAAAJ](https://scholar.google.com/citations?user=kOc4beIAAAAJ) | Visible 404. |
| Steven Hand | [QE17xR4AAAAJ](https://scholar.google.com/citations?user=QE17xR4AAAAJ) | Redirected to unrelated Steven Hansen, despite historical search-index text for Hand. |
| Ramanathan Guha | [wMxEtKgAAAAJ](https://scholar.google.com/citations?user=wMxEtKgAAAAJ) | Visible 404. |
| Gaetano Borriello | [wUS-iRsAAAAJ](https://scholar.google.com/citations?user=wUS-iRsAAAAJ) | Visible 404. |
| Jeffrey Dean | [NMS69lQAAAAJ](https://scholar.google.com/citations?user=NMS69lQAAAAJ) | Visible 404. |
| Laurie Hendren | [uouHKIkAAAAJ](https://scholar.google.com/citations?user=uouHKIkAAAAJ) | Visible 404; the alternative 14-paper McLAB profile was rejected for inadequate coverage. |
| Chandramohan Thekkath | [B_uwswQAAAAJ](https://scholar.google.com/citations?user=B_uwswQAAAAJ) | Visible 404. |
| Guang Gao | [KYj0CvEAAAAJ](https://scholar.google.com/citations?user=KYj0CvEAAAAJ) | Visible 404. |
| Peter Norvig | [Ol0vcWgAAAAJ](https://scholar.google.com/citations?user=Ol0vcWgAAAAJ) | Visible 404. |
| Victor Vianu | [CK_GLC8AAAAJ](https://scholar.google.com/citations?user=CK_GLC8AAAAJ) | Visible 404. |
| Michael D. Schroeder | [mPzCK6EAAAAJ](https://scholar.google.com/citations?user=mPzCK6EAAAAJ) | Visible 404. |
| Richard Schlichting | [K2We_X0AAAAJ](https://scholar.google.com/citations?user=K2We_X0AAAAJ) | Visible 404. |
| Ralf Steinmetz | [S8m0ZkkAAAAJ](https://scholar.google.com/citations?user=S8m0ZkkAAAAJ) | Visible 404. |

Paola Inverardi is resolved and is not part of this availability list; her approved successor capture and statistics are imported.

## Resolved Historical CSRankings Source Gaps

All six associations below are now linked using original rows recovered from upstream commit `4b714f69c839ca538825054f94bdf57f5d4ea3da` of December 30, 2020.
The [recovery report](csrankings_historical_recovery_2026-09-18.md) records the exact source values, identity evidence, historical scope and applied changes.
The historical source predates ORCID; that unavailable field is explicitly represented as blank, and the four actual source values remain unmodified.
The following links retain the initial discovery leads; these cases no longer await source recovery.

| Person | Candidate Key | Existing Lead |
| --- | --- | --- |
| Peter Bartlett | Peter L. Bartlett | [Public historical mirror](https://csrankings.swag.cispa.de/). |
| Larry Davis | Larry S. Davis | [Historical CSRankings-related study](https://leonidk.com/pdfs/jcdl2019.pdf). |
| Joseph Hellerstein | Joseph M. Hellerstein | [Public historical mirror](https://csrankings.swag.cispa.de/). |
| Allan Gottlieb | Allan Gottlieb | [Historical source mirror](https://gitee.com/mirrors/CSrankings/blob/gh-pages/csrankings-a.csv). |
| Laxmi Bhuyan | Laxmi N. Bhuyan | [Institution-hosted 2019 printout](https://vsclab.engr.ucr.edu/media/261/download?attachment=). |
| John Hopcroft | John E. Hopcroft | [Public historical mirror](https://csrankings.swag.cispa.de/), identified during the [Turing sweep](check_profiles_turing_2026-09-18.md). |

Together with Donald Greenberg, Georg Gottlob, Judith S. Olson, Luca Cardelli and Ruby B. Lee, these were the 11 previously accepted historical keys; the September 29 adoption adds 117, bringing the canonical lookup table to 952 keys, including 128 historical keys.
The accepted historical fields are protected by the [source-field manifest](csrankings_source_fields.json).

## Evidence and Resume Point

The retained run is `../bigcows-crawler/.cache/check-profiles-full-2026-09-18/`.
It contains the input snapshots, `queue.json`, `inspection-notes-1286-1300.json`, `candidate-decisions-1286-1300.json`, earlier batch notes and `user-dispositions-2026-09-18.json`.
The public status index consolidates that progress without claiming the unfinished notes constitute a final audit.
The separate completed Turing audit and discovery follow-ups are retained in `../bigcows-crawler/.cache/check-profiles-turing-2026-09-18/` and summarized in the [Turing report](check_profiles_turing_2026-09-18.md).
The September 29 [CSRankings identity audit](csrankings_identity_audit_2026-09-29.md) supersedes the old resume point at Fellow 1,301 and reconciles earlier follow-ups.
All 117 supported historical proposals are adopted; no CSRankings adoption decision remains pending.
A combined three-service audit remains separate.
Preserve completed DBLP decisions and the separate September 28 Scholar ledger.
Preserve the explicit user dispositions, original CSRankings source fields and finalized ACM award data; regenerate visualization snapshots only when requested.
