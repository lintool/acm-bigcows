# DBLP Reassessment, September 19, 2026

All 1,638 ACM Fellows and 81 Turing Award rows have a recorded DBLP outcome in the [row audit](dblp_reassessment_2026-09-19.csv).
Following the explicit user decisions below, 1,598 distinct stored profiles are supported as `Y` within the documented sampling scope and 43 are rated `N`.
All four new coverage flags are resolved as `N`.
Fifteen Fellows have no stored DBLP link.
The initial review was read-only; subsequent authorized updates applied four quality downgrades and seventeen approved replacements across the [first](dblp_replacement_recommendations_2026-09-19.md), [second](dblp_replacement_recommendations_batch2_2026-09-19.md) and [third](dblp_replacement_recommendations_batch3_2026-09-19.md) batches.
Sixteen replacement URLs are Y and MacQueen’s replacement remains N by explicit user decision; all seventeen now have accepted September 19 captures from the [replacement gap fill](dblp_replacement_captures_2026-09-19.md).
The review queue retains four user-approved holds: Gupta, Adams, Friedman and Harris.
Award fields, Scholar data and visualization files remain unchanged.

MacQueen’s later user instruction was applied 2026-09-19 16:28 EDT: adopt [84/3383](https://dblp.org/pid/84/3383), retain N for incomplete coverage and clear the old capture date.

## Evidence and Inspection Scope

Used the latest accepted retained HTML for every stored URL: September 17–19, including the 84 profiles captured in the approved gap fill.
Verified all 1,641 source hashes and reparsed 414,937 publication records; these are bibliography records, not a deduplicated paper count.
The name sweep covered every linked row, including manual review of all 500 nonexact name mappings and all 44 strict name-screen exceptions.
The strict exceptions are explainable aliases, accents, reordered names or abbreviations; Danny Hillis is a valid name variant even though the stored bibliography is only a one-record fragment.
Lexical compatibility also misses wrong-person cases such as Kai-Ming Li and R. Todd Constable, so the content and ACM-recognized work determine the identity finding.
Fresh manual chronological samples and expanded concern checks covered 503 distinct profiles: every existing N, every small bibliography (40 or fewer records), every weakly corroborated larger Y, and every newly gap-filled profile.
For the other 1,138 profiles, this pass reused the prior content assessment of the identical SHA-256 capture, together with fresh extraction and name screening; it did not manually reread all of their publications.
All 414,937 records remain available in the retained evidence for expansion; extraction is not a claim of manual inspection of every paper.
Publication-count bands selected inspection work only and did not determine ratings.
Scholar title overlap is limited corroboration, not independent proof of authorship or a new Scholar quality audit.
A few isolated attribution errors, alternate names and location differences were not treated as automatic downgrades.
Capture dates were not advanced by reparsing, and retained captures do not establish live availability on September 19.

## Award-Row Outcomes

| Roster | Supported Y | Poor Quality N | Unresolved Current Y | Missing Link | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| acm_fellows.csv | 1,581 | 42 | 0 | 15 | 1,638 |
| turing_award_winners.csv | 77 | 4 | 0 | 0 | 81 |

These outcomes include the four applied user decisions.
The row audit preserves original-profile findings, including assessment fields for URLs later replaced; `review_status` and `action_taken` record subsequent dispositions.
Use the [current row snapshot](dblp_current_status_2026-09-19.csv) and [consistency report](dblp_consistency_2026-09-19.md) for final URLs, ratings and accepted capture dates.
The historical row audit, exception inventory and review queue retain `capture_path` values relative to the parent directory containing both repositories.
The current row snapshot and capture-import audits instead use paths relative to this repository root.
Shared Fellows/Turing rows reuse the same profile evidence and agree in their assessment.
The existing Turing N cases remain Catmull, Thacker, Hamming and Wilkinson; all 77 other Turing links remain supported within the evidence scope.

## Resolved User Decisions

The user explicitly selected `N` for Burton Smith, Chung-Jen Tan, Aaron Finerman and Herbert Grosch.
Applied all four quality changes on 2026-09-19 15:40 EDT, preserving the stored URLs and capture dates.
For Tan, the user chose `N` over the subsequent provisional `Y` recommendation.
No replacement was adopted; all four cases have been removed from the active review queue.

The table below preserves the initial evidence and recommendations as historical context; its pending-review language is superseded by these decisions.

| Recipient | Rating at Initial Review | Records | Initial Assessment (Now Resolved N) | Evidence |
| --- | --- | ---: | --- | --- |
| Smith, Burton | Y | 11 | The complete stored list has 11 records, mainly later systems work and retrospective HEP/Tera chapters. A separate Burton J. Smith bibliography contains earlier Horizon/Tera, hardware-description and scheduling work missing here. This is a split bibliography, not just a spelling difference; recommend N for the stored fragment and review the combined identity before selecting any replacement. | [Stored profile](https://dblp.org/pid/64/4805); [Source 1](https://dblp.org/pid/36/6104); [Source 2](https://www.microsoft.com/en-us/research/people/burtons/) |
| Tan, Chung Jen | Y | 14 | The 14-record list supports Chung-Jen Tan through early circuit work and later e-commerce, but omits his IBM-confirmed 1995 Deep Blue publication, indexed under C. J. Tan on a separate page. Assess whether the split still leaves meaningful career coverage; preserve Y pending that decision. | [Stored profile](https://dblp.org/pid/54/1393); [Source 1](https://research.ibm.com/publications/deep-blue-computer-chess-and-massively-parallel-systems); [Source 2](https://dblp.org/pid/14/2685) |
| Finerman, Aaron | Y | 7 | The seven-record list supports the computing-education/service identity, but contains only two of the seven significant publications listed in the IEEE biography. The omitted books, management and education work make substantial coverage uncertain; preserve Y pending review. | [Stored profile](https://dblp.org/pid/11/4555); [Source 1](https://history.computer.org/pioneers/finerman.html) |
| Grosch, Herbert R J | Y | 8 | The eight-record list fits Grosch, but omits all three bibliography items in the IEEE biography, including his computing memoir and two history articles; that source also describes regular writing absent here. Review the coverage exception; preserve Y pending review. | [Stored profile](https://dblp.org/pid/62/2002); [Source 1](https://history.computer.org/pioneers/pdfs/G/Grosch.pdf) |

## Existing N Profiles and Replacement Leads

At the initial review, 55 distinct already-N profiles had poor-quality findings; the table below preserves those original-profile findings, including URLs subsequently replaced.
They are existing issues, not 55 newly discovered downgrades.
The [September 18 full review](check_profiles_full_2026-09-18.md) and [Turing decisions](check_profiles_turing_2026-09-18.md) retain the earlier primary-source corroboration and explicit user dispositions.
The table separates name/identity conflicts from incomplete coverage and mixed bibliographies.
The table retains the initial discovery findings; seventeen replacements were subsequently approved as documented above.
Other replacement URLs remain discovery leads, not approved good-quality replacements.
General web searches were run for every linked N profile and every missing link; candidate-page inspection was attempted for the principal distinct leads.
Several candidate pages returned tool timeouts, cache misses, HTTP 503 or access denial; those outcomes do not prove removal, and complete replacement quality remains unverified.
Richard P. Gabriel and Allen B. Tucker initially remained leads; the subsequent five-profile review completed their assessments and the user approved their replacements.
All seventeen subsequently approved replacement URLs now have accepted September 19 captures.
Rob Cook’s 14-record replacement is now approved as Y and captured, as documented in the current status index.
No previously rejected association was restored.

| Recipient | Stored Heading | Records | Finding | Replacement Lead |
| --- | --- | ---: | --- | --- |
| Cao, Pei | [Pei Cao](https://dblp.org/pid/87/3674) | 65 | Systems/web-caching core is mixed with recurring unrelated biomedical, catalysis and vision work; preserve the explicit N decision. | No newly verified replacement |
| Yang, Junfeng | [Junfeng Yang](https://dblp.org/pid/71/3724) | 282 | Columbia systems core is mixed with sustained optimization and other namesake work; preserve the explicit N decision. | No newly verified replacement |
| Dubey, Pradeep | [Pradeep Dubey](https://dblp.org/pid/47/4438) | 129 | Intel parallel-computing work is mixed with a persistent economics/game-theory bibliography belonging to the Stony Brook economist. | No newly verified replacement |
| Balakrishnan, Meenakshi | [M. Balakrishnan](https://dblp.org/pid/24/4827) | 128 | IIT Delhi embedded-systems core is mixed with the previously documented namesake cluster; explicit user-retained N. | No newly verified replacement |
| Pop, Mihai | [Mihai Pop](https://dblp.org/pid/p/MihaiPop) | 72 | UMD genomics core is present, but the user retained this mixed-identity bibliography as N; the new capture does not resolve that concern. | No newly verified replacement |
| Kass, Michael | [Michael Kass](https://dblp.org/pid/46/6511) | 35 | Graphics/vision core is mixed with recurring neutron/imaging and clinical namesake records, beyond an isolated outlier. | No newly verified replacement |
| Franz, Michael | [Michael Franz](https://dblp.org/pid/f/MichaelFranz) | 174 | UCI compilers/security core is mixed with a persistent clinical/histopathology cluster; the prior primary-source distinction still applies. | No newly verified replacement |
| Lin, Chih-Jen | [Chih-Jen Lin](https://dblp.org/pid/61/1218) | 151 | Machine-learning core is mixed with seven VLSI/BIST records from 1991–1998 by a distinct Intel researcher, inconsistent with the recipient career chronology. | No newly verified replacement |
| Bundy, Alan | [Alan Bundy](https://dblp.org/pid/b/AlanBundy) | 229 | Edinburgh automated reasoning is mixed with a persistent Australian library-science bibliography, including 2008–2016 book reviews. | No newly verified replacement |
| Srinivasan, Aravind | [Aravind Srinivasan](https://dblp.org/pid/s/AravindSrinivasan) | 314 | Algorithms core is mixed with repeated eye-care and other documented namesake clusters; an accepted Scholar Y does not reverse DBLP N. | No newly verified replacement |
| Anderson, James H | [James H. Anderson](https://dblp.org/pid/a/JamesHAnderson) | 305 | UNC real-time/synchronization work is mixed with surgical/vascular imaging records and an incompatible 1967 boiler thesis. | No newly verified replacement |
| Singhal, Amit | [Amit Singhal 0001](https://dblp.org/pid/s/AmitSinghal) | 54 | Information-retrieval publications are mixed with a recurring Kodak/Rochester computer-vision namesake bibliography. | No newly verified replacement |
| Alvisi, Lorenzo | [Lorenzo Alvisi](https://dblp.org/pid/a/LAlvisi) | 144 | Cornell/UT distributed systems is mixed with eleven recent disinformation/Telegram records attributed in the prior primary-source review to an IMT Lucca namesake. | No newly verified replacement |
| Bhatkar, Vijay P | [Vijay P. Bhatkar](https://dblp.org/pid/18/4677) | 5 | Only five records, 1989–1999, versus the recipient biography documenting 80 research papers and 12 books; PARAM identity fits but coverage is inadequate. | No newly verified replacement |
| Dean, Jeffrey A | [Jeffrey Dean](https://dblp.org/pid/d/JeffreyDean) | 127 | Google systems/AI core is mixed with eight 1992–1999 insect-locomotion papers by a Cleveland State biologist; this is a sustained cluster. | No newly verified replacement |
| Levin, Roy | [Roy Levin](https://dblp.org/pid/83/749) | 32 | HYDRA/Grapevine/Vesta identity is present alongside the previously documented IBM Israel route-search namesake cluster; retain N. | No newly verified replacement |
| Agarwal, Anant | [Anant Agarwal](https://dblp.org/pid/a/AAgarwal) | 123 | MIT parallel-computing core is mixed with seven SiC power-electronics papers and two recent traffic papers independently attributed to namesakes. | No newly verified replacement |
| Cook, Rob | [Rob Cook](https://dblp.org/pid/84/2471) | 2 | The two stored records concern Australian bioinformatics/spectral data, not the ACM-recognized RenderMan/graphics contribution. | [Inspect candidate](https://dblp.org/pid/c/RobertLCook) |
| MacQueen, David | [David MacQueen](https://dblp.org/pid/54/6101) | 5 | Five records mix a small late ML fragment with opioid-monitoring work and omit the established Standard ML/type-system bibliography. | [Inspect candidate](https://dblp.org/pid/84/3383) |
| Pradhan, Dhiraj | [Dhiraj Pradhan](https://dblp.org/pid/236/7010) | 1 | A single guest editorial cannot represent the established fault-tolerant systems and VLSI testing career. | [Inspect candidate](https://dblp.org/pid/p/DhirajKPradhan) |
| Sameh, Ahmed | [Ahmed Sameh](https://dblp.org/pid/s/AhmedSameh) | 55 | The Prince Sultan/Cairo medical/network bibliography does not represent the Purdue numerical analyst; preserve the explicitly retained N link pending a separate replacement decision. | [Inspect candidate](https://dblp.org/pid/46/2473) |
| Gabriel, Richard P. | [Richard Gabriel](https://dblp.org/pid/170/8185) | 4 | Four records on biomedical/mood/cryptographic topics do not represent the Lisp and object-oriented programming recipient. | [Inspect candidate](https://dblp.org/pid/g/RichardPGabriel) |
| Gupta, Gopal Krishna | [Gopal Gupta 0001](https://dblp.org/pid/g/GopalGupta) | 304 | The linked Gopal Gupta 0001 is the UT Dallas logic-programming researcher; the ACM recipient is the Monash database researcher Gopal Krishna Gupta. | [Inspect candidate](https://dblp.org/pid/60/5294) |
| Li, Kai | [Kai-Ming Li](https://dblp.org/pid/65/8684) | 32 | The heading is Kai-Ming Li and the publications concern radar, rather than Princeton systems researcher Kai Li. | [Inspect candidate](https://dblp.org/pid/l/KaiLi1) |
| Miller, Raymond | [Raymond Miller](https://dblp.org/pid/141/1845) | 1 | One game-learning record does not cover the recipient’s parallel-computation theory career; identity is not established by the common name. | [Inspect candidate](https://dblp.org/pid/m/RaymondEMiller) |
| Zanella, Paolo | [Paolo Zanella](https://dblp.org/pid/52/1184) | 1 | The one high-energy-computing record is plausible for the CERN recipient but does not establish meaningful career coverage. | No newly verified replacement |
| Rice, John | [John Rice](https://dblp.org/pid/06/3409) | 4 | The four-record clinical/traffic/measurement bibliography does not represent mathematical-software researcher John R. Rice. | [Inspect candidate](https://dblp.org/pid/r/JohnRRice) |
| Catmull, Edwin | [Edwin E. Catmull](https://dblp.org/pid/c/EdwinECatmull) | 12 | Graphics identity is supported but the 12-record bibliography remains the explicitly accepted N coverage case. | No newly verified replacement |
| Constable, Robert | [R. Todd Constable](https://dblp.org/pid/63/6962) | 96 | R. Todd Constable is an MRI/fMRI researcher; the recipient is Cornell logic and Nuprl researcher Robert L. Constable. | [Inspect candidate](https://dblp.org/pid/c/RobertLConstable) |
| Goodenough, John B | [John B. Goodenough 0001](https://dblp.org/pid/84/1640) | 1 | The stored chemistry bibliography belongs to the solid-state/battery scientist, not the ACM-recognized software-engineering researcher. | [Inspect candidate](https://dblp.org/pid/181/2396-2) |
| Johnson, David S | [David M. S. Johnson](https://dblp.org/pid/198/1125) | 5 | David M. S. Johnson’s robotics bibliography does not represent algorithms and complexity researcher David S. Johnson. | [Inspect candidate](https://dblp.org/pid/j/DavidSJohnson) |
| Kennedy, Kenneth W | [Kenneth W. Kennedy](https://dblp.org/pid/05/9528) | 2 | Two historical records are only a fragment of Ken Kennedy’s compiler and high-performance-computing career. | No newly verified replacement |
| Kim, Won | [Won-Bin Kim](https://dblp.org/pid/244/5227) | 16 | Won-Bin Kim’s IoT/cloud-security work does not represent the database researcher Won Kim. | [Inspect candidate](https://dblp.org/pid/86/2627-1) |
| Nievergelt, J | [Jay Nievergelt](https://dblp.org/pid/294/3258) | 1 | Jay Nievergelt’s single shared-workspace record does not represent Jürg Nievergelt’s algorithms and education bibliography. | [Inspect candidate](https://dblp.org/pid/n/JurgNievergelt) |
| Adams, James M | [James M. Adams](https://dblp.org/pid/144/4286) | 5 | The five-record recent RL/fuzzy-control bibliography is unsupported for the historical ACM service recipient; the name alone is insufficient. | No newly verified replacement |
| Blasgen, Michael W | [Michael W. Blasgen](https://dblp.org/pid/172/8567) | 1 | A single RISC System/6000 record omits the System R recovery/database body recognized by ACM. | No newly verified replacement |
| Bob O Evans | [Bob O. Evans](https://dblp.org/pid/174/0100) | 2 | Two System/360/SPREAD records fit the recipient but remain a sparse fragment of the established systems career. | No newly verified replacement |
| Bradshaw, Charles L | [Charles L. Bradshaw](https://dblp.org/pid/199/7422) | 1 | One proceedings record establishes neither substantial coverage nor a justified coverage exception. | No newly verified replacement |
| Bricklin, Daniel S | [Dan Bricklin](https://dblp.org/pid/91/4250) | 4 | Four records include duplicate TYPESET material and do not cover the VisiCalc contribution; identity alone is insufficient. | No newly verified replacement |
| Brotz, Douglas K | [Douglas K. Brotz](https://dblp.org/pid/58/3707) | 3 | Three printing/messaging/geometry records fit the recipient but do not establish substantial coverage of the PostScript career. | No newly verified replacement |
| D'Auria, Thomas A | [Thomas A. D'Auria](https://dblp.org/pid/49/1062) | 3 | Three service/panel/proceedings records remain a sparse bibliography without evidence supporting a coverage exception. | No newly verified replacement |
| Dunwell, Stephen | [Stephen W. Dunwell](https://dblp.org/pid/87/6954) | 2 | Two APL/Stretch records are only a historical fragment; no broader coverage is established. | No newly verified replacement |
| Friedman, Frank L | [Frank F. Friedman](https://dblp.org/pid/287/8232) | 1 | The one-record Frank F. Friedman classroom page is not enough to establish the Frank L. Friedman identity or career coverage. | No newly verified replacement |
| Hamming, Richard W | [Richard Wesley Hamming](https://dblp.org/pid/h/RWHamming) | 16 | Correct numerical-computing identity, but the 16-record bibliography remains explicitly accepted as N for coverage. | No newly verified replacement |
| Harris, Fred H | [Fredric J. Harris](https://dblp.org/pid/06/421-1) | 115 | Fredric J. Harris’s signal-processing bibliography does not establish the ACM professional-certification/service recipient Fred H. Harris. | No newly verified replacement |
| Hillis, William Daniel | [Danny Hillis](https://dblp.org/pid/40/8885) | 1 | Danny Hillis is a valid name variant, but the lone Minsky tribute omits the Connection Machine and parallel-algorithm body. | [Inspect candidate](https://dblp.org/pid/19/28) |
| Lindsay, Bruce | [Bruce D. Lindsay](https://dblp.org/pid/288/0534) | 1 | Bruce D. Lindsay’s atrial-fibrillation record is a cardiologist’s work, not the System R database researcher. | [Inspect candidate](https://dblp.dagstuhl.de/pid/l/BLindsay.html) |
| Liu, C.L. | [Chengliang Liu](https://dblp.org/pid/30/5444) | 39 | Chengliang Liu’s hydraulics/vision bibliography does not represent Chung Laung Liu’s algorithms/design/education career. | [Inspect candidate](https://dblp.org/pid/l/CLLiu) |
| Maisel, Herbert | [Herbert Maisel](https://dblp.org/pid/27/474) | 4 | Four service/education records remain a sparse bibliography without a demonstrated coverage exception. | No newly verified replacement |
| McCracken, Daniel D | [Daniel McCracken](https://dblp.org/pid/199/9066) | 1 | A single public-policy panel does not represent the programming-textbook author’s established body of work. | No newly verified replacement |
| Poucher, William B | [William B. Poucher](https://dblp.org/pid/20/10566) | 3 | Three ICPC/education/combinatorics records support identity but do not establish substantial career coverage. | No newly verified replacement |
| Taylor, Robert W | [Robert W. Taylor](https://dblp.org/pid/31/1172) | 19 | Alto-related person metadata is combined with a mainly database-conversion/environment bibliography; the header does not establish authorship of the list. | No newly verified replacement |
| Thacker, Charles P | [Charles P. Thacker](https://dblp.org/pid/58/4470) | 12 | Correct computer-systems identity; the 12-record profile remains explicitly retained as N for coverage. | No newly verified replacement |
| Tucker, Allen | [Allen Tucker](https://dblp.org/pid/146/9346) | 2 | Two handbook records are a split fragment of the programming-language/computing-education career. | [Inspect candidate](https://dblp.org/pid/t/AllenBTucker) |
| Wilkinson, J. H. | [James Hardy Wilkinson](https://dblp.org/pid/15/4740) | 25 | The accepted replacement identifies Wilkinson, but its 25-record numerical-analysis coverage remains explicitly rated N. | No newly verified replacement |

## Missing Stored Links

The 15 missing associations remain N with blank URLs and capture dates.
Repeated discovery of an already rejected sparse profile does not reopen the user’s decision.
No new, independently verified good replacement was established in this sweep.

| Recipient | Finding |
| --- | --- |
| Miller, Victor | No stored DBLP link; preserve prior rejection where documented. |
| Gosling, James | No stored DBLP link; preserve prior rejection where documented. |
| Scott, Steven | No stored DBLP link; preserve prior rejection where documented. |
| House, Charles H | No stored DBLP link; preserve prior rejection where documented. |
| York, Bryant W | No stored DBLP link; preserve prior rejection where documented. |
| Bourne, Stephen | No stored DBLP link; preserve prior rejection where documented. |
| Karin, Sidney | No stored DBLP link; preserve prior rejection where documented. |
| Birnbaum, Joel S | No stored DBLP link; preserve prior rejection where documented. |
| Duncan, Karen | No stored DBLP link; preserve prior rejection where documented. |
| Williams, Robin | No stored DBLP link; preserve prior rejection where documented. |
| DeBlasi, Joseph S | No stored DBLP link; preserve prior rejection where documented. |
| Geschke, Charles M | No stored DBLP link; preserve prior rejection where documented. |
| Bate, Roger R | No stored DBLP link; preserve prior rejection where documented. |
| Young, Paul | No stored DBLP link; preserve prior rejection where documented. |
| Wolfson, Seymour J | No stored DBLP link; preserve prior rejection where documented. |

## Accepted Exceptions and Informational Notes

Preserved the explicit Y decisions for Stephen David Crocker, Sung Mo Kang, Prithviraj Banerjee and George Varghese.
Preserved explicit N/link-retention decisions, including Meenakshi Balakrishnan, Mihai Pop and the four Turing cases.
Small historical bibliographies were assessed in context; examples of positive central-work evidence include BASIC for Kurtz, PUP/Alpine/PDF for Taft, DEL/QA4 for Rulifson and the graphics core specification for Herzog.
These are contextual judgments, not guarantees of completeness or a general exemption for service recipients.
The isolated concerns for S. E. Robertson, Philip M. Lewis, Robert M. Graham and Eric A. Weiss remain informational; no substantial recurring cluster was established on expanded inspection.

## Artifacts and Validation

- [All 1,719 award-row outcomes](dblp_reassessment_2026-09-19.csv).
- [74-case exception inventory](dblp_reassessment_exceptions_2026-09-19.csv): 55 existing N profiles, four user-resolved N coverage cases and 15 missing links.
- [Actionable review queue](dblp_reassessment_review_queue_2026-09-19.csv): four retained distinct cases, all on user-approved hold; this is separate from the accepted capture/import backlog.
- Retained input snapshots, full parsed bibliographies, source manifests, searches, decisions and validation: `../bigcows-crawler/.cache/dblp-reassessment-2026-09-19-152400/`.

The initial read-only phase validated one outcome per roster row, matching decisions across shared URLs and byte-identical canonical CSVs against the review-start snapshots.
All 41 Python tests passed, including the CSRankings source-field manifest checks; `git diff --check` was clean.
The earlier gap-fill changes remain present; this assessment did not modify them.
All four new coverage flags are now resolved by explicit user decisions; it does not complete the separate unfinished Scholar/CSRankings full-roster review.

The subsequent update was validated against its own input snapshot: exactly four `dblp_profile_quality` cells changed from `Y` to `N`, and every other canonical cell was preserved.
