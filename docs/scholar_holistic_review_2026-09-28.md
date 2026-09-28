# Scholar Holistic Review — September 28, 2026

**Disposition update:** The [final user decisions](scholar_recalibration_2026-09-28.md#resolved-user-decisions) are applied: Gao, Morris, Cohen and Scott are N; Wilks is Y.
The other initial flags were accepted under the lenient recalibration, and no quality decision remains pending from this audit.
This report and its original CSVs preserve the initial evidence and proposals; consult the [current status](profile_review_status.md) for present totals and remaining work.

**Complete within retained-evidence limits: 1,264 of 1,264 distinct linked profiles individually inspected.**
This is a read-only audit using retained September 24–28 Scholar captures and retained ACM/DBLP evidence.
No additional crawling, live searches, canonical data edits, metric imports or visualization regeneration were performed.
The [row ledger](scholar_holistic_review_2026-09-28.csv) retains all 1719 award rows, including 425 rows without a stored link.
The [historical proposal queue](scholar_holistic_review_queue_2026-09-28.csv) records the initial 43 distinct profiles (46 award rows): 35 proposed N findings and eight borderline cases.
Its pending flags are historical; the [final disposition ledger](scholar_recalibration_2026-09-28.csv) supersedes them.

## Evidence and Method

Each linked profile is assessed against the ACM recipient/citation, captured name and affiliation, central works, career-spanning publication samples, authors and coauthors.
The baseline inspects the top three entries, entries near one-third and two-thirds, the final captured entry, and the two earliest and two latest dated entries (deduplicated).
Suspicious samples are expanded to all retained entries or to every title absent from the retained DBLP bibliography, with the exact inspected entry numbers recorded in the ledger.
Exact title overlap with previously reviewed DBLP captures is corroboration of works, not a stand-alone identity or quality test.
Small sets of isolated attribution errors do not warrant a downgrade; repeated unrelated clusters are flagged, while plausible interdisciplinary collaborations remain distinct from proved contamination.
Explicit prior user decisions are preserved.

The captures are most-cited first pages: usually 100 entries, sometimes exhausted shorter lists.
Raw entries include duplicate citations, patents, books and malformed dates, and do not equal unique publications.
The evidence supports judgments about identity and substantial core representation within sampled content; it cannot certify complete career coverage, all recent work, or current availability.
A missing stored link does not establish that no public profile exists, and no new discovery was attempted.
The retained run is `../bigcows-crawler/.cache/scholar-safari-refresh-2026-09-24-074715/`.
Input snapshots, judgments, DBLP title matches and resumable progress are retained in `../bigcows-crawler/.cache/scholar-holistic-review-2026-09-28/`.
At the original audit, Paulson's user-confirmed destination was assessed using only its 20-entry redirected page, limiting the quality finding.
The subsequent [authorized Paulson-only refresh](paulson_scholar_import_2026-09-28.md#latest-accepted-capture-100-entries) supersedes that limitation: all 100 fresh entries were inspected, identity and substantial core coverage were supported, and no apparent unrelated cluster was found.
The prior canonical link correction is separate from this audit; the subsequent [Paulson import](paulson_scholar_import_2026-09-28.md) accepted the retained page and imported its statistics and capture date.
The original CSV ledger preserves its historical 20-entry scope; the linked targeted report records the later 100-entry review and accepted capture.

## Initial Audit Outcomes

| Outcome | ACM Fellows | Turing Winners | Award Rows | Unique Recipients |
| --- | ---: | ---: | ---: | ---: |
| Supported within inspected scope / accepted Y preserved | 1,202 | 36 | 1,238 | 1,212 |
| New user-review flags | 43 | 3 | 46 | 43 |
| Existing linked N preserved | 9 | 1 | 10 | 9 |
| No stored Scholar link | 384 | 41 | 425 | 392 |
| Total | 1,638 | 81 | 1,719 | 1,656 |

All 1,264 distinct linked profiles received an individual judgment; the 425 blank-link rows received missing-link outcomes, not content verification.
All linked profiles have supported recipient identity anchors; the new flags primarily concern mixed ownership within those profiles, not proved wholly wrong-person links.
The 43 flags include 35 proposed N decisions for substantial contamination and eight borderline cluster/aggregation cases with quality preserved pending review.
The existing nine N profiles are Arindam Banerjee, Feifei Li, Sudipta Sengupta, Carlos Lucena, Ramesh Jain, Tetsuo Asano, James H. Morris, Edwin Catmull and David S. Johnson.
Catmull is a coverage case; his exhausted list contains mostly repeated leadership-book material and little seminal graphics research.
Aravind Srinivasan's explicit accepted Y is preserved despite additional conflicting namesake entries; it is recorded informationally rather than reopening the resolved decision.
Other explicit accepted ratings, rejected candidates and removed links remain preserved.

There are 63 recipients present in both award rosters, verified by nonempty normalized ACM recipient IDs: 30 share linked Scholar evidence and 33 share blank-link outcomes.
These reused judgments retain both award rows; profile URLs were not used alone to infer shared identity.
Eleven documented historical Fellow rows lack an ACM URL and remain distinct records rather than being merged by name; Chris S. Wallace is the only linked Scholar profile in that group.
His retained Monash affiliation and distinctive multiplier/MML body provide corroboration, with the unavailable ACM-profile evidence noted as a limitation.
The 69 heuristic name-mismatch flags from the capture run are covered by this full sweep; spelling or current affiliation alone was not treated as a failed identity.
No new invalid, disappeared or withdrawn profile finding is established by these retained pages; historical removed candidates remain separate resolved cases in the status index.

The 1,263 successful captures comprise 1,246 pages of 100 entries and 17 exhausted pages of 34–99 entries; Paulson's redirected page adds 20 entries.
Together these provide 125,695 raw entries captured from 2026-09-24 11:47:29 UTC through 2026-09-28 17:43:01 UTC.
Retained September 17/19 DBLP evidence supplies title corroboration for 1,259 linked profiles; Victor Miller, Sung Mo Kang, Jim Gray, David Patterson and James Wilkinson were inspected across their entire retained Scholar lists without that corroboration.
Neither a retained DBLP match nor a sampled Scholar acceptance certifies every paper, unique-publication count, full career coverage or recent work.
Malformed years and publication reprints remain labelled as raw metadata rather than asserted career dates.

## Validation

All 1,719 award rows are retained in source order and all 1,264 profile judgments are present.
Canonical input-file hashes are checked against the pre-audit snapshots; the preexisting Paulson correction is preserved.
All 1,264 raw Scholar capture hashes and 1,259 supporting DBLP hashes passed local verification, as did shared-recipient consistency and ledger/queue coverage.
All 40 canonical-data tests passed, including source-field manifest checks; visualization synchronization was deliberately not run while regeneration is deferred.
The exact entry ledger records 18,092 inspected entries: 1,107 baseline samples, 137 expanded samples and 20 complete retained lists, counted per distinct profile.
No data or visualization files were changed by this audit, and no network request was made.
Validation details are retained in `../bigcows-crawler/.cache/scholar-holistic-review-2026-09-28/validation.json`.

## Profiles Flagged for Review

These are historical inspection notes, including superseded recommendations.
All 43 cases have final dispositions in the recalibration ledger; do not treat the original recommendations below as an open queue.

- [Goel, Ashish](https://scholar.google.com/citations?user=B_rKfusAAAAJ): Expanded all 100 entries: Stanford affiliation and algorithms/social-choice/PageRank work establish intended Ashish Goel.
  Multiple clinical entries (44 zinc/hepatotoxicity,45 organophosphate poisoning,87 gallbladder ultrasound,94 cutaneous histoplasmosis), plus 86 anti-beggary law and74 spacecraft reentry suggest recurring namesake contamination.
  Recommend user review of whether this materially contaminated profile should be N; preserve Y pending decision.
  No replacement search under no-crawl scope.
- [Leonardi, Stefano](https://scholar.google.com/citations?user=p5LCHHEAAAAJ): All 100 captured entries inspected: Sapienza affiliation and algorithms/auctions core identify the intended Stefano Leonardi.
  Repeated forestry/genetics entries16,30,44,79,90,96 and dairy/milking entries88,93,99 form persistent unrelated clusters, not isolated errors.
  Recommend N for contamination subject to user review; preserve canonical Y.
  Thyroid prediction85 shares Siciliano with computing work and is not counted merely for its medical topic.
- [Backes, Michael](https://scholar.google.com/citations?user=ZVS3KOEAAAAJ): CISPA affiliation, cryptographic libraries, privacy and AI security identify Michael Backes.
  Expanded all12 titles without exact retained-DBLP matches: nine recurring ATLAS/HESS/MAGIC particle/astrophysics entries32,42,49,53,73,86,90,93,94 form a distinct cluster.
  Recommend N for material contamination for user review; preserve Y.
  Security entry67 lacking Backes is not the main concern.
- [Chen, Yingying](https://scholar.google.com/citations?user=jCZaWOEAAAAJ): Rutgers affiliation and wireless spoofing/mobile sensing establish intended Yingying Chen.
  Expanded all13 titles without exact retained-DBLP matches: a repeated power-grid/wind/energy cluster8,52,54,67,90,96,99 plus yeast/biocatalysis42,45,77 and rat-aorta65 have distinct coauthor groups.
  Recommend N for recurring mixed-domain contamination for user review; preserve Y.
  This is more than one isolated application paper.
- [Du, Wenliang](https://scholar.google.com/citations?user=1aMkcasAAAAJ): All100 captured entries inspected: Syracuse affiliation, SEED, secure multiparty computation and Android security firmly identify intended Wenliang Du.
  Repeated remote-sensing/image-matching entries35,64,67,73,75,76,81,91,92,94,95 use WL Du with a separate Zhao/Zhou/Yao group, absent from the retained DBLP page; distinguish a legitimate collaboration from a merged namesake before accepting quality.
  Additional fusion66 and waveguide99 are isolated conflicts.
  Preserve Y; user review of cluster authorship and possible N recommended.
- [Chandra, Ranveer](https://scholar.google.com/citations?user=Zq4ioqu5yb8C): MAUI, SSCH, FarmBeats and consistent Bahl/Moscibroda collaborators establish Ranveer Chandra.
  Expanded all46 titles without exact DBLP matches: antidiabetic plant extracts11, nanocrystals28, polyaniline29, composite damping46, Cu2O films84 and pulp-effluent microbiology86 form recurring unrelated R Chandra attributions.
  Recommend user review for N; preserve current Y.
  Patents and agricultural AI alone are not counted as conflicts.
- [Zheng, Haitao](https://scholar.google.com/citations?user=XrIr0nYAAAAJ): Chicago affiliation, wireless spectrum and AI security with BY Zhao identify Haitao Zheng.
  Expanded all31 titles without exact DBLP matches reveals recurring different-domain attributions: cooked-ham preservation71, steel coatings76, magnetic ordering83, petroleum84, soil carbon87, structural acoustics92 and tamoxifen96.
  Recommend N for user review due to persistent mixed-author concerns; preserve Y.
  Networking patents and neural watermarks remain relevant.
- [Zhu, Wenwu](https://scholar.google.com/citations?user=7t2jzpgAAAAJ): Tsinghua affiliation, multimedia networking and graph representation establish Wenwu Zhu.
  Expanded all19 nonmatching DBLP titles finds a recurring stem-cell/exosome cardiology cluster56,68,83 with shared Sun/Hong/Zhang coauthors, alongside quadrotor-control20/73 and optical imaging52.
  Flag whether these represent material namesake contamination versus supported collaborations; retain Y pending review, do not reject simply for cross-domain subject matter.
- [Balakrishnan, Meenakshi](https://scholar.google.com/citations?user=e_749FUAAAAJ): IIT Delhi affiliation, scratchpad/ASIP design and assistive Braille/cane systems establish Meenakshi Balakrishnan.
  Expanded all40 nonmatching DBLP titles: persistent coffee-pest/entomology cluster23,42,53,60,74,86,90 with MM Balakrishnan, plus distributed-cloud/logging11,25,27,28,34,38,61,83 with Birman/Malkhi/Aguilera appear to mix other authors.
  Sepsis12 and pharmaceutical87 add concerns.
  Recommend N for contamination; preserve Y for user review.
  Biomedical FPGA/assistive work with existing core collaborators is not counted as unrelated.
- [Das, Gautam](https://scholar.google.com/citations?user=oleB9xIAAAAJ): UT Arlington affiliation and DBXplorer, database ranking/time-series work establish Gautam Das.
  Expanded all24 nonmatching DBLP titles: chemistry41/61, materials/failure45/84/90, electrochemistry79/96, fiber optics98 and clinical/veterinary78/99 form multiple persistent unrelated clusters; sequencing1 is the highest listed entry and also needs authorship verification.
  Recommend N for user review; preserve Y.
  The anomalously early1977 scheduling entry58 is not used as positive career evidence.
- [Banerjee, Suman](https://scholar.google.com/citations?user=cLb-v7gAAAAJ): Correct UW-Madison wireless and network-systems identity, but expanded inspection of all 25 titles absent from retained DBLP reveals a recurring clinical S K Banerjee cluster: adenosine lung/asthma papers 23,32,44,77; rheumatoid troponin 47; mouse tobramycin 73; and 1958 radiosodium knee study 88.
  Materials books 79,97 and fish pesticide study 42 add unrelated records.
  Review for N due to substantial mixed-author contamination; preserve current Y pending user decision.
- [Gonzalez, Antonio](https://scholar.google.com/citations?user=DRP_OcMAAAAJ): Correct UPC architecture identity and substantial energy-efficient processor work, but all 25 nonmatching DBLP entries include repeated unrelated records: agricultural policy 37, marketing dictionary 55, avian bronchitis 63, APA citation guide by Gonzalez Bonorino 79, atomism pedagogy 89, at-risk minors intervention 95 and elderly disability 100.
  Review mixed-author contamination for possible N; preserve current Y.
- [Gribble, Steven](https://scholar.google.com/citations?user=7CohtIMAAAAJ): Correct systems/virtualization identity anchored by Denali, peer-to-peer studies and cluster services.
  Expanded all 33 nonmatching DBLP titles reveals a separate recurring Statistics Canada/health microsimulation group with Wolfson, Rowe and Hicks: breast-cancer risk 76, LifePaths 83/96, cervical/lung cancer 90/91, income rounding 98 and health inequality 99.
  Review for N due to coherent mixed-identity cluster; preserve Y.
- [Thompson, Kenneth Lane](https://scholar.google.com/citations?user=FsHMg9AAAAAJ): Correct Ken Thompson identity is anchored by UNIX, regular expressions, Plan 9, Go and chess.
  Expanded all 70 nonmatching DBLP entries reveals recurring sociology namesake works: Emile Durkheim 8, Jurgen Habermas 71 and Deconstructing Durkheim 77, plus Karen Thompson interview 43, school leadership 47, Home from Home 49 and bovine anaesthesia 59.
  Several malformed/spurious records compound the mixed bibliography.
  Review quality for possible N while preserving Y and URL; do not mistake duplicate UNIX records for distinct coverage.
- [Wang, Wei](https://scholar.google.com/citations?user=08CVzE8AAAAJ): Correct UCLA data-mining identity is supported by STING and relevant computational genetics, but expanded all 68 nonmatching DBLP titles reveals extensive materials/plant/environmental clusters: soft actuators 58/67, perovskites 59, plant proteomics 57/99, wheat stress 75/87, membranes 76, grassland/wetland studies 79/84, nitrate catalysis 89 and nanocrystals 98.
  Numerous database entries with Lin/Yu may also require namesake separation.
  Recommend reviewing for N based on substantial mixed bibliography, without treating legitimate genetics collaborations as contamination; preserve Y.
- [Aaronson, Scott J](https://scholar.google.com/citations?user=EYv2BNQAAAAJ): Correct UT Austin quantum-computing identity is anchored by stabilizer simulation and linear-optics complexity, but expanded all 42 nonmatching DBLP titles shows a large persistent S T Aaronson clinical psychiatry cluster: psilocybin 3/43/95, vagus stimulation 11/52/88/98, TMS 27/42/51/58/75/87/90 and depression roadmap 44.
  Strong case for N due to substantial mixed-author contamination; preserve Y for user review.
- [Xie, Yuan](https://scholar.google.com/citations?user=dK2ZuDcAAAAJ): Correct HKUST architecture identity is anchored by PRIME, NVSim and Tianjic.
  Expanded all 27 nonmatching DBLP entries reveals a large separate vision cluster with Y Qu/L Lin/C Li: 17,23,35,42,43,45,47,51,60,63,64,81,83,84,88,100.
  This may mix a computer-vision namesake with the chip researcher and needs review beyond topic adjacency; finance 39 and liver-disease 57/99 add conflicts.
  Preserve Y pending decision on the substantial cluster.
- [Gupta, Aarti](https://scholar.google.com/citations?user=S_jYB2sAAAAJ): Correct Princeton formal-verification identity is anchored by F-Soft, hardware verification and ILAng, but expanded all 19 nonmatching DBLP titles finds a persistent heterogeneous namesake mixture: silicon infiltration 24, LEP physics 43/91, kidney surgery 53/73, lithosphere 55, CT/MRI 58/78, astronomy 63, dengue 87 and gingival health 93.
  Review for N due to substantial contamination; preserve Y.
- [Rodriguez, Pablo](https://scholar.google.com/citations?user=yetbFCsAAAAJ): Correct networking identity is anchored by content distribution, YouTube analysis and Biersack/Gkantsidis collaborations.
  Expanded all 40 nonmatching DBLP entries shows recurring power-inverter patents 72/83/87/89 plus unrelated ventilation trial 5, conformal-symmetry physics 73, ovarian-cancer trial 86, ethics text 90 and pre-Hispanic childhood history 98.
  Review for substantial mixed-author contamination; contact-tracing 34 and brain-network modeling 84 can be legitimate network applications and are not counted merely for topic difference.
  Preserve Y.
- [Morris, Robert](https://scholar.google.com/citations?user=in6eBIwAAAAJ): Correct MIT systems identity is anchored by Chord, Click and Kaashoek collaborations, but expanded all 45 nonmatching DBLP titles reveals extensive separate cancer/proteomics work 25,33,51,59,61,66,69,71,75,76,87,91 and combinatorics/percolation with Balogh/Bollobas 32,50,63,80,89,94,97,98,100.
  Older R H Morris/Cherry UNIX work 57/84 and 1959 pregnancy study 41 add distinct-identity evidence.
  Strong case for N due to substantial mixed identities; preserve Y pending review.
- [Anderson, James H](https://scholar.google.com/citations?user=mIZu9oQAAAAJ): UNC real-time-systems identity and substantial EDF/LITMUS/lock-free core are supported, but expanded inspection exposes a recurring unrelated cluster: atmospheric climate/chlorine/aerosol entries 9/23/37/87, HST astrometry 13, wheat genetics 30, neonatal transfusion 34 and blood utilization 91.
  These exceed isolated errors; propose N for review while retaining the URL.
  Malformed mathematical entry 12 and early graph paper 92 add attribution uncertainty, not independent proof of the recipient's chronology.
- [Haas, Peter](https://scholar.google.com/citations?user=PeCI8KcAAAAJ): UMass Peter J. Haas identity and online aggregation, histograms, stochastic simulation and substantial patent/methodology core are supported.
  Expanded inspection finds numerous entries visibly by other authors: malware GAN 47, emergency department 60, business digital twin 81, blockchain supply chain 83, electric vehicles 88, population movement 97 and kidney transplantation 100, plus Gemulla thesis 93.
  Repeated 2019 simulation papers suggest proceedings/editor attribution spillover; propose N for this material aggregate contamination rather than claiming a wrong-person page.
- [Shim, Kyuseok](https://scholar.google.com/citations?user=3Y254i4AAAAJ): Seoul National University identity and CURE/ROCK/outlier mining with Guha/Rastogi establish Shim, but expanded inspection finds recurring atmospheric PM2.5/lidar/black-carbon papers 61/71/90/95 and a separate KS Shim quantum-network/protocol cluster 75/76/86/88/94 with W Lee and others.
  Together with unrelated LDA entry 66, this is material mixed attribution; propose N for review, retaining URL.
  Database patents are legitimate distinct evidence, not contamination.
- [Gao, Lixin](https://scholar.google.com/citations?user=bOKmjf8AAAAJ): UMass identity and AS relationships/routing with Rexford/Towsley support Lixin Gao, but expanded scope reveals extensive recurring corrosion/battery chemistry with D Zhang (28/31–37/45/51/54/58–60/62/65/84–90/92/96/97), PTP1B/natural products (63/69/73/78/83/88/93/94), biomedical and mechanical-fault work.
  These materially mix identities despite a strong networking core; propose N retaining URL.
- [Gupta, Manish](https://scholar.google.com/citations?user=fHISoWoAAAAJ): Google DeepMind identity and substantial Banerjee/Choi/Midkiff/Moreira compiler and BlueGene core are supported.
  Expanded unmatched works reveal repeated clinical attribution: cardiac resynchronization 11/13/80 (including duplicate versions), thyroid 71, pressure injury 72, meningitis 91 and rectal-cancer trial 97, plus welding 61.
  Material aggregate contamination warrants proposed N for review; adjacent HPC/AI papers and patents are not treated as contamination solely by topic.
- [Chen, Peter](https://scholar.google.com/citations?user=dVZNQqUAAAAJ): Michigan identity, RAID, ReVirt and King/Dunlap storage/security work establish Peter M. Chen.
  Expanded inspection finds repeated neonatal/cesarean work with RL Williams (14/37/50), massage mattress/chair patents 73/89, atmospheric/nuclear transport 48/99 and accelerator 77, plus different PMC Chen multimedia records 91/100.
  This substantial mixed-attribution set warrants proposed N while retaining the correct-person URL.
- [Erickson, Thomas D](https://scholar.google.com/citations?user=e5yN9ewAAAAJ): Erickson's social-translucence/Kellogg and interface-design core supports the correct HCI recipient.
  Expanded scope finds recurring 1974–1980 glass/fiber/manufacturing patents with WW Wolf (62/73/85/88/94/97), with duplicate versions, plus toxicology 48 and wastewater 92.
  These could be namesake patent contamination; retained evidence does not establish an early glass-engineering career.
  Flag this cluster for a holistic user decision while preserving Y; modern drone/interface patents with Pickover/Farrell are coherent IBM collaborations.
- [Wilks, Yorick](https://scholar.google.com/citations?user=NsHFYDcAAAAJ): IHMC identity and preference semantics, Electric Words, GATE collaborations and machine translation establish Yorick Wilks.
  Expanded inspection shows many highly placed whole books/handbooks or articles with other editor/author bylines (1/3/4/5/7/8/18/20/30/31/32/33/39/46/51/62/67/73/79/84/87/97).
  Some may represent his contributed chapters merged into book-level records, but retained metadata cannot distinguish this from substantial attribution spillover.
  Flag the aggregation issue for user review; preserve Y pending assessment rather than asserting these are all unrelated works.
- [Cohen, Michael F.](https://scholar.google.com/citations?user=YAtwLpwAAAAJ): Facebook identity and lumigraph, bilateral upsampling, Szeliski/Hoppe graphics establish Michael F. Cohen.
  Expanded scope reveals major astronomy (35/48/69), organizational psychology (5/27/63), schooling (56/68/78), cellular biology (13/32/34), and clinical/public-health clusters (18/33/60/64/73/74/83/87/91), plus urban policy 100.
  This is substantial mixed attribution; propose N retaining URL.
  Graphics patents are legitimate, and Gemini 1 remains individually unverified rather than assumed wrong.
- [Moore, J Strother](https://scholar.google.com/citations?user=91fyr68AAAAJ): UT Austin identity and Boyer-Moore/ACL2 theorem proving are clear, but expanded scope reveals many unrelated records: clinical cancer/asthma 8/19/26/37/78, aerospace 24/66/72, poultry 82/95, infection/microbiology 83/92/98, educational dialogue 42/81 and repeated neuroscience books 18/63/73/76.
  Material mixed attribution warrants proposed N retaining the correct-person URL; duplicate versions are not counted as distinct independent works.
- [kumar, vipin](https://scholar.google.com/citations?user=BnxU9TEAAAAJ): Minnesota identity, Karypis parallel partitioning, Tan/Steinbach data mining and Chandola anomaly detection establish Vipin Kumar.
  Expanded unmatched scope reveals a persistent marketing/customer-value cluster with Reinartz/Venkatesan/Ravishanker (12/19/25/37/59/63/87/92), plus electronic-structure 75, supercapacitors 86 and meat fibers 95.
  Propose N for material mixed attribution.
  Climate/lake models and sepsis work with known data-mining collaborators are plausible legitimate interdisciplinary research and are not counted as contamination.
- [Zhang, Hui](https://scholar.google.com/citations?user=UMll0FcAAAAJ): CMU/Conviva identity and WF2Q, service disciplines and Stoica multicast core support Hui Zhang.
  Expanded scope contains two peptidase papers 88/97 and cotton materials 92, plus a persistent adjacent networking cluster with Goel/Govindan (45/64/71/94/96) and NYU mesh 59 that may belong to a namesake rather than this recipient.
  Flag the ambiguous networking cluster for identity review, preserve Y; do not infer ownership merely because the topics are networking or count duplicate 45/94 twice.
- [Peyton-Jones, Simon L](https://scholar.google.com/citations?user=QsX7G-cAAAAJ): Epic identity and Haskell/GHC, strictness and spineless-machine core establish Simon Peyton Jones.
  Expanded scope exposes clinical kidney trials 58/66, Pompe disease 81, recurring dendron/DNA chemistry 83/86/97 and knee surgery 100, plus performance studies 50, beaver ecology 62 and aircraft drilling 84.
  This is material mixed attribution; propose N retaining URL, distinguishing legitimate spreadsheet patents and computing education from unrelated S/SP Jones work.
- [Carroll, John Millar](https://scholar.google.com/citations?user=7Mg8JZMAAAAJ): Penn State identity, Carroll/Rosson scenario design, minimalist instruction and HCI establish John M. Carroll.
  Expanded scope finds LHCb 11, cardiac gene transfer 35, surgical outcomes 65, oocyte biology 91 and twin ultrasound 97, plus the 1964 Richardson letters 74 and words/concepts 27.
  The aggregate spans distinct namesakes and merits N review despite the substantial correct HCI core.
  Preserve URL; do not treat legitimate psychology/cinema/design work as contamination merely by topic.
- [Freeman, Peter A](https://scholar.google.com/citations?user=1kW15d8AAAAJ): Georgia Tech/Irvine software identity is supported by Prieto-Diaz reuse, Leite requirements, Newell design and Aspray workforce work.
  Expanded 67 unmatched entries reveal persistent PJ Freeman genetics (VariantValidator 5; methylation 17; genome amplification 18; HGVS 25; DNA analysis 36; germline insertions 43; nomenclature 100) alongside PR Freeman community-health (33/40), fisheries (11), photography (45) and law (51).
  Proposed N for mixed publication ownership, retaining linked URL pending user review.
- [Brachman, Ronald J.](https://scholar.google.com/citations?user=zMnT8BsAAAAJ): Cornell Brachman identity and substantial KL-ONE/CLASSIC/Levesque knowledge-representation core are clear.
  Expanded 64 unmatched entries expose recurring Methods of Information in Medicine articles with complete other-author bylines: Rector clinical terminology (18), Zweigenbaum ontology (31), de Vries expert systems (65), Oliver/Shahar terminology changes (67), Degoulet decision support (74), Smart/Roux pathology (80), Scherrer (92), Flier classifications (97), plus NJ Rachman insect physiology (68).
  Topical adjacency does not establish authorship; persistent attribution contamination merits review/proposed N while retaining URL.
- [Pradhan, Dhiraj](https://scholar.google.com/citations?user=OETOceoAAAAJ): Bristol fault-tolerance identity strongly supported by textbooks, Vaidya routing, Koren redundancy and Kunz testing.
  Expanded 23 unmatched entries reveal prominent recurring neurobiology (GABA with DA Pradhan 4, autism 10, FEZ1/DISC1 neuronal development 25), yeast transcription with DA Pradhan (14), monsoon forecasting (35), bacteria (58) and fruit sensing (100).
  Some electrical/IoT topics may be legitimate; recurring distinct-initial biological authorship merits user review before deciding material contamination, preserving Y pending resolution.
- [Li, Kai](https://scholar.google.com/citations?user=9MSpWOUAAAAJ): Princeton systems identity supported by IVY/shared memory, Appel primitives, PARSEC and ImageNet.
  Expanded 36 unmatched entries show a persistent distinct proteogenomics cluster: lung/renal/glioblastoma/endometrial/head-neck cancer (11/13/14/22/28/31), MSBooster with Nesvizhskii (41), neoantigens (70), PDV (80), splicing proteome (97), alongside Y Zhang/K Li/K Li super-resolution (2/9).
  Princeton computational-neuroscience/connectomics work (26/43/69/94) is not automatically contamination; repeated proteomics authorship supports proposed N pending user review.
- [Taylor, Richard N](https://scholar.google.com/citations?user=h9t7KCcAAAAJ): Irvine software identity clear from Fielding web architecture, Medvidovic languages, Oreizy adaptation and Young analysis.
  Expanded 32 unmatched entries show recurring RS Taylor cardiac rehabilitation (5/33/44/46/93), Coulson graphite/molecular physics from 1951-52 (25/71/89), forestry (7/78/85), meteorite (66), gear pumps (84) and aircraft patent (100).
  Strong mixed-identity/chronology evidence merits proposed N, retaining URL for user disposition.
- [Jones, Cliff B](https://scholar.google.com/citations?user=W9m9SwwAAAAJ): Newcastle VDM identity supported by Bjorner specifications, Henhapl semantics, Hayes rely-guarantee and Romanovsky dependable systems.
  Expanded 46 unmatched entries show unrelated chromosome mapping (67), cervix (72), uranium chemistry (83), Texas mammals (84), gallstones (92), turtle conservation (99), Acacia propagation (100), plus recurring climate projections/CO2 (80/88/94).
  Infrastructure modelling may be legitimate and is not required for finding; persistent disparate namesakes merit proposed N pending user review.
- [Denning, Peter J](https://scholar.google.com/citations?user=-W3wvGkAAAAJ): Naval Postgraduate Peter identity supported by working sets, Coffman OS, Dorothy Denning information flow and Tedre computational thinking.
  Expanded 46 unmatched entries reveal repeated full other-author books/articles (5/8/12/33/34/37/38/45/56/58/65/83/88/94/96/98), plus JT Denning education economics (41/57) and HCV clinical consortium (73).
  Some entries may represent editor/foreword/reprinted contributions; publication aggregation and namesake mixture merit user review rather than assuming all are unrelated, preserving Y pending judgment.
- [Patterson, David](https://scholar.google.com/citations?user=Wj4ZBFIAAAAJ): Inspected all 100 without DBLP capture: Berkeley identity and Hennessy architecture, Katz/Gibson RAID, Asanovic RISC-V and Jouppi TPU are strong.
  Recurring PA David economics is unrelated (QWERTY 3/29, path dependence 48, growth 50, savings 60), with homelessness (56), petroleum flooding (93), agriculture (86), and Gene Ontology (9) additional concerns.
  Biomedical computing with Nothaft/Zaharia is not rejected by topic; persistent economics plus namesake mixture merits proposed N pending user review.
- [Scott, Dana S](https://scholar.google.com/citations?user=oaja5KYAAAAJ): Dana Scott identity supported by Rabin automata, Strachey semantics, continuous lattices and Suppes/Tarski logic.
  Expanded 81 unmatched entries show major recurring Evans chromosome/radiation cluster (26/34/43/53/74/79/85/96), DG Scott clinical/rheumatology (9/27/33/47/54/59/69), sea-lion carcinoma (42), schistosomiasis (55), grassland (76), and pandemic labour economics (65/77).
  Substantial mixed identities merit proposed N, retaining linked profile pending user review.
