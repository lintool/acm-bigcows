# Missing Scholar Links, Batch Ten — September 28, 2026

Completed at 2026-09-28T21:41:15.668046-04:00 for the next 25 missing-link Fellows without search-history records, from Anita Borg through Marshall C Yovits.
Ran 37 general-web queries, with 15-second pauses between successive search calls or longer source-inspection work, plus focused directory checks and one direct Scholar browser check.
Results: no usable new profiles, one newly observed unavailable association (Ferrante), one preserved unavailable hold (Wasserman), and 23 searches without a supported author-profile ID.
No canonical roster changes, capture-date updates, metrics imports, bulk crawls or visualization regeneration occurred.

## Scope and Evidence Limits

This is bounded Scholar discovery, not a full publication-quality or multi-service audit.
Not found means these searches did not establish a matching author profile; it does not establish that no profile exists.
ACM roster identities and award citations supplied the identity ground truth.
Ferrante’s exact directory link was opened in Chrome and displayed a Google 404 page.
Wasserman’s hold is historical and was not retested directly; a web-tool error on DBLP is not evidence of Scholar availability.
Savage’s earlier wrong-person association remains excluded.
Larry Stockmeyer has a blank ACM URL cell; his exact canonical name was confirmed unique in the roster and used as the search-history fallback key.
No new DBLP or CSRankings audit was performed.

## Results

CSV row numbers include the header.

| CSV Row | Fellow | Outcome | Evidence |
| --- | --- | --- | --- |
| 1406 | Borg, Anita | not_found | No supported author-profile ID located; scholarship-recipient pages are not Borg’s profile. [DBLP](https://dblp.org/pid/b/AnitaBorg). |
| 1407 | Chandrasekaran, B. | not_found | Initial and Ohio State follow-up searches did not establish an ID for the AI researcher. Excluded the SNU Chennai A. Chandrasekaran physics namesake and preserved the earlier VU Amsterdam namesake exclusion. [Prior provenance](data_notes.md). |
| 1410 | Dodd, George | not_found | No supported ID from initial or General Motors-focused search. An Auckland directory namesake was not treated as a match. [GM identity evidence](https://thetatau.org/george-dodd-memorial/). |
| 1411 | Encarnacao, Jose L. | not_found | Unaccented and José Luis Encarnação variants found graphics bibliography, not a supported author-profile ID. [DBLP](https://dblp.org/pid/e/JLEncarnacao.html). |
| 1412 | Ferrante, Jeanne | inaccessible | [Scholar](https://scholar.google.com/citations?user=sMN63KwAAAAJ). [Matching directory](https://research.com/u/jeanne-ferrante) links sMN63KwAAAAJ, but direct Chrome inspection displayed Google’s 404 page for that exact ID. Do not apply. |
| 1413 | Fischer, Michael J | not_found | Theory and consensus references found in initial and Yale-focused searches; no supported exact Scholar ID established. |
| 1415 | Graham, Robert M | not_found | Initial and Multics-focused searches found computing references, but no supported ID. Excluded cardiology and meteorology namesakes. [Multics course reference](https://read.seas.harvard.edu/cs2610/2025/n02-early-monolithic/). |
| 1416 | Harrison, Michael A | not_found | Initial and Berkeley-focused follow-up did not establish the automata researcher’s Scholar ID; plant-biology namesake excluded. |
| 1419 | Jaffe, Jeffrey | not_found | Initial and W3C-focused searches established networking/web identity but no Scholar ID; finance namesake excluded. [W3C biography](https://www.w3.org/staff/alumni/). |
| 1421 | Jones, Anita K | not_found | Initial and Virginia-focused follow-up did not establish a supported Scholar author-profile ID for the systems researcher. |
| 1423 | Klawe, Maria | not_found | Found theory/education bibliography and scholarship-recipient references, not a supported Scholar author ID. [DBLP](https://dblp.org/pid/00/5675.html). |
| 1424 | Landweber, Lawrence H | not_found | Found computation bibliography and fellowship-recipient references, not a supported Scholar author ID. |
| 1425 | Larry Stockmeyer | not_found | Complexity bibliography found, not a supported Scholar author-profile ID. [DBLP](https://dblp.org/pid/40/805.html). |
| 1426 | Lesk, Michael E | not_found | Digital-library book references found, not a supported author-profile ID. [Book record](https://agris.fao.org/search/en/providers/122535/records/65ddd1f963b8185d9ca4cb02). |
| 1428 | Liskov, Barbara | not_found | Initial and exact-profile-URL follow-up found distributed-systems references, not a supported Scholar ID. [DBLP](https://dblp.org/pid/l/BarbaraLiskov.html). |
| 1430 | Nance, Richard E | not_found | Initial and Richard E. Nance follow-up found no supported ID; Buddhist-studies namesake excluded. [Simulation publication record](https://doi.org/10.1145/116890.116912). |
| 1432 | Preas, Bryan | not_found | EDA bibliography found, not a supported Scholar author-profile ID. [DBLP](https://dblp.org/pid/90/5052). |
| 1433 | Rao, TRN | not_found | The biography’s purported Scholar profile is actually the general query scholar?q=t.r.n.+rao, not an author profile. No exact author ID established. [Biography reference list](https://handwiki.org/wiki/Biography%3AT._R._N._Rao). |
| 1435 | Rice, John | not_found | Purdue mathematical-software references found. The [matching directory](https://research.com/u/john-r-rice), reached through Vernon’s coauthor list, has no Google Scholar link. No exact ID established; unrelated Rice namesakes excluded. |
| 1436 | Rosenberg, Arnold | not_found | Parallel/distributed-computing references found, but no supported author-profile ID. [Publication](https://research.google/pubs/a-tool-for-prioritizing-dagman-jobs-and-its-evaluation/). |
| 1439 | Savage, John E | not_found | No supported replacement established. Preserve the prior exclusion of genetic-association researcher JE Savage’s ASYT5QEAAAAJ. [Prior provenance](data_notes.md). |
| 1445 | Vernon, Mary K | not_found | Performance/streaming bibliography found. The [matching directory](https://research.com/u/mary-k-vernon), reached through Eager’s coauthor list, has no Google Scholar link. No exact ID established. |
| 1448 | Wasserman, Anthony I | inaccessible | [Scholar](https://scholar.google.com/citations?user=08Dlm8cAAAAJ). Initial and Tony Wasserman follow-up found no supported replacement. Preserve historical unavailable 08Dlm8cAAAAJ without a new direct Scholar fetch. A DBLP follow-up had a web-tool cache miss; this is not new Scholar availability evidence. [Prior provenance](data_notes.md). |
| 1450 | Weingarten, Fred W | not_found | Initial and Fred W. Weingarten follow-up found policy publications and award references, not a supported author-profile ID. |
| 1452 | Yovits, Marshall C | not_found | Computing bibliography and book records found, not a supported author-profile ID. [DBLP](https://dblp.org/pid/35/4097.html). |

## Queries

```text
"Anita Borg" "Google Scholar"
"B Chandrasekaran" "Google Scholar"
"George Dodd" "Google Scholar"
"Jose Encarnacao" "Google Scholar"
"Jeanne Ferrante" "Google Scholar"
"Michael J Fischer" "Google Scholar"
"Robert M Graham" "Google Scholar"
"Michael A Harrison" "Google Scholar"
"Jeffrey Jaffe" "Google Scholar"
"Anita K Jones" "Google Scholar"
"Maria Klawe" "Google Scholar"
"Lawrence Landweber" "Google Scholar"
"Larry Stockmeyer" "Google Scholar"
"Michael Lesk" "Google Scholar"
"Barbara Liskov" "Google Scholar"
"Richard Nance" "Google Scholar"
"Bryan Preas" "Google Scholar"
"TRN Rao" "Google Scholar"
"John Rice" Purdue "Google Scholar"
"Arnold Rosenberg" "Google Scholar"
"John E Savage" "Google Scholar"
"Mary Vernon" "Google Scholar"
"Anthony Wasserman" "Google Scholar"
"Fred Weingarten" "Google Scholar"
"Marshall Yovits" "Google Scholar"
"B Chandrasekaran" Ohio "scholar.google.com"
"George Dodd" "General Motors" scholar
"Robert M Graham" Multics scholar
"Michael A Harrison" Berkeley "scholar"
"Jeffrey Jaffe" W3C "scholar"
"Richard E Nance" "scholar.google.com"
"Anita Jones" Virginia "scholar.google.com"
"Fred W Weingarten" scholar
"Tony Wasserman" "Google Scholar"
"José Luis Encarnação" "Google Scholar"
"Michael J Fischer" Yale "citations?user"
"Barbara Liskov" "citations?user"
```

## Search-History Checkpoint

Appended 25 rows, preserving earlier searches and decisions byte for byte.
The ledger now contains 249 rows across 245 recipients, including 14 accepted associations.
Of 370 Fellows with blank Scholar links, 231 have search-history records and 139 do not.
These are CSV coverage counts; older Data Notes searches are not comprehensively backfilled.
All canonical data and the 18-task capture/import queue remain unchanged.
