---
name: check-profiles
description: Verify ACM Fellows and Turing Award winners' linked Google Scholar, DBLP and CSRankings identities, publication coverage and profile quality in acm-bigcows. Use for individual checks or complete roster reviews.
---

# Check Profiles

Use in the `acm-bigcows` repository.
Unless the user specifies a subset, review populated links in every row of `data/acm_fellows.csv` and `data/turing_award_winners.csv`, including existing `N` ratings.
Evaluate Google Scholar, DBLP and CSRankings separately for each recipient, then reconcile the evidence across services.
Record blank Scholar/DBLP URLs and blank CSRankings name keys as missing and not searched in this audit.
Missing-link discovery is costly and requires a separate explicit user request; an audit or check does not authorize searching for absent associations, even when older searches or candidate evidence exist.
Creating or editing this skill does not initiate a profile review.

## Workflow Stage

This skill owns **review** in the [four-stage workflow](../../README_FOR_AGENTS.md#four-stage-workflow).
Use saved captures by default; parsing publications or metrics for inspection does not authorize canonical statistics imports.
Record acceptance against specific capture hashes/timestamps, separately from profile-link acceptance and quality ratings, so extraction can consume the reviewed evidence.
Crawling, canonical statistics extraction/import and visualization are separate stages and require their own authorization, which may already be included in the user's request.
Preserve the standing authorization below for profile-link, quality and dependent consistency corrections; it is not blanket permission to refresh statistics.
Report accepted captures awaiting extraction separately from unresolved review cases.

## Ground Truth and Scope

Read the repository's `AGENTS.md`, [publication quality criteria](../../README_FOR_AGENTS.md#publication-profile-quality), [CSRankings name-link guidance](../../README_FOR_AGENTS.md#csrankings-name-links), and the latest relevant [Data Notes](../../docs/data_notes.md), including cited reviews and explicit user decisions.
Read the [current review status](../../docs/profile_review_status.md) before resuming; update that index when inspection progress or open cases change, and distinguish inspected notes from applied CSV changes and completed audits.
The ACM directory name, recipient profile and award citation establish the recipient's identity and recognized work.
Preserve ACM names, award years, citations and profile links unless strong, cited evidence establishes an actual error; a different spelling on Scholar, DBLP or CSRankings alone is insufficient.
Preserve existing documented ACM corrections and historical recipients omitted from the current directory.
When an ACM profile is unavailable, use retained ACM evidence and corroborating institutional or recipient sources, and state the limitation.
Do not silently make another publication profile the ground truth.

The user has explicitly configured this skill to correct obvious publication-profile and CSRankings-link errors when they request its application, as recorded in [AGENTS.md](../../AGENTS.md#finalized-award-csvs).
For an explicit request to apply the skill, this standing authorization covers Scholar/DBLP URLs, their quality flags and capture dates, CSRankings name links and alignment dates, and dependent profile-table synchronization.
It does not authorize changing ACM identities, award fields or roster membership; those require a separate explicit request and the strong evidence described above.
Automatic skill discovery or a general verification/consistency request alone does not authorize finalized-roster edits; report proposed corrections unless the user has authorized them in the task.
A read-only review or dry run overrides the standing edit authorization.
Apply a correction when concrete, converging evidence supports a clear decision; record the previous value, new value and evidence.
For a proven wrong-person link, use an independently verified replacement if available; otherwise clear the incorrect association and its dependent date rather than inventing a replacement.
An unavailable, invalid or potentially withdrawn profile is a separate case: follow the flag-for-review policy below instead of automatically clearing, replacing or restoring it.
Rate a clearly contaminated or inadequately covered publication profile `N` even when the person matches; retain the URL unless a clearly supported better profile is found under the search workflow below.
Correct ACM data only with the separate explicit authorization and stronger ground-truth exception above, with strong cited evidence of an actual error.
For borderline identity, coverage or contamination findings, preserve the existing values and flag the case for user review with the competing evidence, proposed action and specific decision needed.
During every requested profile audit or check, reflag stored links or CSRankings associations that remain suspicious under these criteria, including previously reviewed or explicitly accepted cases.
Clear sparse-DBLP coverage findings follow the direct-resolution rule below instead of requiring repeated user review.
Profiles can change over time, so a previously accepted identity or quality decision is not permanent verification; assess the evidence available for the current audit and resurface concerns that warrant reconsideration.
When newer evidence is available, compare it with the earlier decision's evidence and describe any supported changes; retained evidence alone cannot establish that a profile has changed since that decision.
A prior decision does not suppress a current review item, and new evidence is not required to resurface a concern supported by the inspected evidence.
Include the exact link or key, concrete concern, evidence date and scope, prior user decision, and the decision now requested; identify reused evidence as retained rather than newly observed.
Preserve prior user decisions in the canonical data until the user changes them; reflagging is not permission to reverse them automatically.
An explicit request for a fresh audit authorizes and requires reassessment of all prior review decisions within the requested scope, including explicit user decisions, accepted exceptions, rejections and holds.
Treat those decisions as historical context rather than exemptions from inspection; report whether the available evidence supports retaining or revising each decision, and bring proposed reversals of explicit user decisions back to the user before applying them, except for clear sparse-DBLP coverage findings already authorized for direct resolution below.
“Fresh audit” means a new assessment, not automatic authorization for new crawls, statistics imports, missing-link discovery or visualization regeneration.
Reassess prior missing-link rejections from retained evidence when relevant, but do not search for or restore absent associations without the separately required authorization.
This applies to prior `Y` and `N` decisions: report evidence of deterioration or improvement, and distinguish a changed profile at the same URL from a different replacement candidate.
An old evidence date alone is a freshness limitation, not proof that a link is suspicious; identify the concrete concern and request an evidence refresh only under the existing authorization rules.
Keep a separate review queue; do not invent a third quality value or use `N` solely to signal uncertainty.
Do not ask again for permission already given in the current task.
Preserve unrelated fields and row order; preserve manually accepted canonical values pending the user's decision on any proposed reversal, without exempting them from fresh-audit reassessment.
Do not regenerate visualizations unless the user requests it.

## Evidence Collection

Snapshot the input rosters and profile tables and create a per-recipient review queue before editing.
Keep both award rows for shared recipients in the audit; reuse evidence for the same person/profile, then check that conclusions and any applied changes agree across rosters.
Use recipient IDs, award years and stored URLs to connect older evidence to current names; do not rely on historical spelling or row numbers alone.

Start with existing crawls, publication lists, review evidence and cached CSRankings source files.
Inventory their capture dates, completeness and gaps, then ask whether the user wants to update the evidence before starting any crawl or source refresh, unless that update is already authorized.
Explain that refreshing can be time-consuming and offer to use existing evidence, refresh selected gaps or refresh the full requested scope; provide an approximate effort estimate only when supported by crawl size and pacing information.
Continue useful inspection of existing evidence while awaiting the answer, but do not start the proposed refresh without approval.
If the user keeps the existing evidence, perform the review against those captures and label conclusions with the evidence dates; do not imply a live availability check or advance capture dates merely for re-reviewing them.
Existing captures can support identity and quality judgments as of their capture dates, but cannot prove that a profile remains available or unchanged today.
Assess the captured content rather than simply inheriting existing quality ratings; flag cases whose evidence is missing, incomplete or insufficient for a supported decision.
For an approved refresh, use a new run or explicit refresh that actually fetches upstream content; reparsing a cached success or changing its date is not a fresh crawl.
For future approved Scholar refreshes, collect a larger most-cited publication page and a recent-publications page before judging overall profile quality.
Record both ordering modes, actual retrieved counts and pagination limits; expand further when gaps or suspicious clusters require it.
An existing 20-entry most-cited capture can support identity and sampled-quality findings, but leave broader coverage and recent-work assessment explicitly unresolved when those portions are absent.
This collection policy does not authorize a refresh when the user has chosen existing evidence.
When resuming an approved crawl, reuse its successful captures and fetch unfinished profiles within the approved scope; record each capture's actual timestamp.
Follow the [crawler and reviewed import workflows](../../README_FOR_AGENTS.md#crawlers) before bulk fetching; store captures, hashes, timestamps, input snapshots and run state under `../bigcows-crawler/.cache/`.
Record whether evidence is newly fetched or retained and when it was captured.
Search for corroboration on the recipient's or institution's website, CV, publication list, award announcement or publisher pages as needed.
Search-result snippets can identify leads but do not establish complete publication coverage.

For each recipient, build an identity assessment using the ACM name and citation together with name variants, research areas, country, current and historical institutional affiliations, career chronology, coauthors and representative publications.
Compare the ACM award-time country and institution with the locations and affiliations in Scholar, DBLP, CSRankings, institutional biographies and publication metadata, recording the dates or periods each describes.
Account for moves between countries or institutions, joint and visiting appointments, renamed institutions and stale profile metadata before declaring a mismatch.
When the name, research and publication evidence otherwise converge, a location or affiliation difference alone is not an actionable issue or a reason to ask the user for a decision.
Consider relocation as a possible explanation without claiming a move occurred unless supported; escalate only when the combined evidence leaves a material identity conflict.
Use country and institution as corroborating or conflicting evidence, not as standalone proof of identity; shared institutions do not resolve namesakes, and different current countries do not by themselves disprove a match.
Keep affiliation country distinct from citizenship or nationality, and leave unknown locations unknown rather than inferring them from a person's name.
Treat name normalization, shared Scholar IDs, DBLP aliases and CSRankings identifiers as candidate evidence, not proof.
Inspect contradictory evidence explicitly: identical names and adjacent research areas can still describe different people, and institutional moves can explain different affiliations.
Do not let a copied or previously inferred cross-service association corroborate itself.

## Invalid, Unavailable or Withdrawn Profiles

Flag any previously linked profile that the inspected evidence shows as missing, invalid, private, redirected to an unrelated destination or explicitly withdrawn upstream, stating when that condition was observed.
Do not claim a new disappearance based solely on an old capture or the absence of a local cache file.
Record the original URL or CSRankings key, fetch time, response status, final URL, visible message and any evidence distinguishing a removal from an access failure.
Separate a confirmed removal or withdrawal from a suspected removal and from temporary failures such as timeouts, rate limits, CAPTCHA or login barriers.
A failed request, an empty crawler result or a missing CSRankings row alone does not prove that the author withdrew the profile.
Use the crawler's bounded retries and inspect the returned page before classifying the outcome; do not repeatedly retry or bypass a privacy or withdrawal decision.

Preserve stored values pending the user's review and report the availability finding with its evidence date; a previous `Y` must not be presented as proof of current availability.
Do not advance a successful-capture date on failure, infer a quality change solely from disappearance, or automatically replace or recreate a potentially withdrawn profile from cached, archived or mirrored copies.
Respect an explicit upstream withdrawal and flag the local link and dependent data for the user's disposition; historical evidence is provenance, not authorization to republish or restore withdrawn content.
For CSRankings, distinguish an already documented historical absence from a newly disappeared entry, and flag the latter without automatically dropping or relinking it.
Continue independent checks of the recipient's other services; one service's removal does not invalidate another service's profile or ACM award record.

## Google Scholar and DBLP

For each linked profile, record three separate findings: whether it represents the recipient, whether its publication coverage is substantial, and whether unrelated publications materially contaminate it.
An identity match alone does not establish a good-quality profile.

The user has chosen sampling across highly cited or otherwise central works, recent publications and older work across the recipient's career as the default inspection method.
Do not require inspection of every publication by default; record the sampled scope and expand it when concerns arise.
Check publication titles, authors/coauthors, venues, dates and topics against the ACM-recognized contributions and independent publication evidence.
Examine suspicious clusters beyond the initial sample; broaden inspection when names, topics, chronology or affiliations conflict.
A few matching papers do not establish that the rest of a profile belongs to the recipient.

Both Scholar and DBLP should contain substantial numbers of publications and represent a meaningful part of the recipient's established body of work.
Record the observed publication count or a clearly labeled lower bound, the years covered and how much of the list was inspected.
Distinguish a complete sparse bibliography from a short first page, pagination, an incomplete crawl, a filtered view or an access challenge.
Citation totals and h-index are not publication counts and do not establish identity or completeness.
The user has chosen contextual judgment rather than a numerical minimum: assess substantial coverage relative to the recipient's career and known bibliography, recording actual publication counts or clearly labeled lower bounds.
Do not use a fixed publication-count threshold as an automatic acceptance or rejection rule.
A genuinely sparse profile is evidence of a poor match or inadequate coverage even if some entries fit; a justified exception needs positive identity and coverage evidence recorded in the audit.
For DBLP, a genuinely sparse bibliography with clearly inadequate career coverage is a clear-cut quality `N`: retain the link, record the evidence and apply or retain `N` without requesting individual user confirmation.
The user explicitly authorized this treatment on September 29, 2026, including downgrading existing `Y` ratings when the sparse-coverage finding is clear; this later instruction supersedes earlier sparse-profile acceptance for that finding.
Reassess such profiles during fresh audits, but record resolved sparse-coverage findings in the audit rather than repeatedly placing them in the user-review queue.
Do not mistake truncated captures, pagination, filters or access failures for a genuinely sparse bibliography, and do not invent a numerical cutoff.
Continue to flag material identity conflicts, contamination thresholds and genuinely uncertain coverage; a sparse count alone does not authorize clearing a link.
All ACM Fellows and Turing Award winners are prominent researchers with an established body of work.
For both Google Scholar and DBLP, very few genuine profile entries are strong evidence of low quality even when the name, affiliation, research area and other identity information match.
Identity agreement and a handful of recognizable landmark publications do not establish substantial coverage or justify `Y`; assess representation of the expected body of work and rate clearly inadequate coverage `N`.
Do not weaken this coverage requirement merely because the recipient’s award recognizes historical, industrial, leadership or service contributions.
The user explicitly reconfirmed linked quality `N` for [Burton Smith’s 11-entry DBLP profile](https://dblp.org/pid/64/4805) and [Charles Thacker’s 12-entry DBLP profile](https://dblp.org/pid/58/4470): these contain too few entries for their prominent careers despite matching core contributions.
Treat these as specific coverage decisions, not a universal numerical cutoff; reassess them in fresh audits and resolve clear sparse-coverage findings directly under the rule above.
See the [September 29 disposition ledger](../../docs/holistic_profile_audit_2026-09-29_dispositions.csv) for the user decisions.

Apply the [quality criteria](../../README_FOR_AGENTS.md#publication-profile-quality) independently to each service:

| Finding | Quality Decision |
| --- | --- |
| Supported identity, substantial coverage, and mostly relevant or adjacent publications without substantial contamination | `Y`, allowing isolated attribution errors. |
| Wrong person | `N`, with the conflicting identity evidence. |
| Correct person but suspicious unrelated publications or mixed entries | Apply the rough 20% rule below; flag threshold or uncertain cases for the user. |
| Obviously incomplete or genuinely sparse coverage without a supported exception | `N`, with actual counts and the coverage concern; do not automatically call it a wrong-person match. |
| Missing stored link | `N`; record that service as missing rather than claiming no public profile exists. |
| Previously linked profile now invalid, unavailable or potentially withdrawn | Flag its availability status for user review; preserve stored values pending disposition and do not treat old evidence as fresh verification. |
| Fetch blocked or available evidence insufficient to assess identity, coverage or contamination | Mark the review unresolved and preserve the previous rating; do not call it verified or infer `N` from access failure alone. |

Apply the user's rough 20% suspicious-publication rule independently to Scholar and DBLP, subject to supported identity, substantial coverage and preserved explicit user decisions:

- Much less than 20% suspicious publications: rate `Y`.
- Much more than 20% suspicious publications: rate `N`.
- Around 20%, or uncertainty that could place the result near that threshold: preserve the existing rating, flag the case and ask the user to decide.

Do not invent precise numerical bands for “much less,” “much more” or “around.”
Exactly 20% is a threshold case for the user, not an automatic `Y` or `N`.
Record the suspicious-publication count, inspected denominator, sampling scope and attribution uncertainty; a sampled fraction is not a measured full-profile fraction or a citation-weighted fraction.
If the sample is too small, incomplete or biased to support a judgment, expand inspection within the available evidence or mark the assessment unresolved; do not treat zero suspicious entries in an inadequate sample as proof of `Y`.
Suspicious publications include apparently unrelated areas or topics, subject to the contextual checks below.
Consider legitimate interdisciplinary work, career changes and collaborations before calling publications unrelated.
Isolated questionable or misattributed publications are acceptable when the identity, coverage and overall bibliography otherwise support `Y`.
Do not downgrade or seek a replacement solely for such isolated entries; a brief informational audit note is sufficient when they leave no material concern about the link under the criteria above.
If inspection leaves a material identity, coverage or threshold concern, reflag it even when the existing rating is `Y` or the concern was previously reviewed.
Expand inspection when an isolated concern may indicate a larger cluster, and flag or reject substantial contamination under the criteria above.
Preserve explicit user ratings while reflagging suspicious links for reconsideration as instructed above; do not silently reverse those ratings.
Quality `N` does not itself authorize deleting a stored URL.

## Search for Missing or Better Profiles

Whenever a populated Scholar or DBLP profile is low quality, perform a general web search for a better profile on that service, including populated links that already had an `N` rating before the run.
The `N` required for a blank URL does not trigger this replacement-search rule.
Search for missing Scholar/DBLP links or CSRankings name links only when the user explicitly requests missing-link discovery as a separate step.
Without that request, leave blank associations out of discovery, do not backfill them from cached candidates, and do not create search-ledger entries or advance search dates for merely observing a blank field.
This boundary concerns absent stored associations; checks of populated links, corroborating identity searches, and searches for better alternatives to existing poor or wrong-person links remain in scope under this skill's other rules.
Search for the correct CSRankings entry when an existing populated association is a wrong-person match.
Do not limit discovery to the local tables, existing identifiers or a service's internal search.
Use name variants together with the service name, current and historical institutions, country, research area or distinctive publication titles to distinguish candidates.
Follow links from the recipient's own homepage, institutional biography or CV when available, and inspect the actual candidate profiles rather than accepting search-result snippets.

Apply the same holistic identity, publication-coverage and contamination checks to each plausible replacement, starting with any existing captures for that exact candidate.
General web searches and inspection of public candidate pages remain part of discovery; they do not imply authorization for a bulk crawl or source refresh.
If verifying candidates requires additional crawling or source downloads, include those in the user's refresh choice or ask for a targeted update, grouping candidates rather than asking once per profile.
A same-name result, larger publication count or higher citation count alone does not make a candidate better.
For Scholar and DBLP, accept a replacement only when both identity and quality are clearly supported; do not substitute one poor profile for another merely because it is less poor.
For CSRankings, verify the exact source key and affiliation history against the selected cached or newly refreshed source files and independent identity evidence, recording source dates.

During explicitly requested missing-link discovery, add clearly supported missing links; during an audit, replace low-quality populated links with clearly supported good alternatives within the existing correction authorization, updating quality flags, dependent dates and CSRankings table associations consistently.
Preserve the old URL, its quality finding and the evidence for replacement in the audit.
An explicit user decision about the old profile remains part of its history; it does not certify or determine the quality of a different candidate URL.
If multiple plausible profiles remain, available candidate evidence is insufficient, or the improvement is borderline, flag the alternatives for user review without changing the association.
When no good match is found, retain a correctly identified low-quality profile with `N`, or leave a missing link blank, and record the search outcome without claiming that no profile exists.

The withdrawal safeguards still apply: search may clarify a disappeared profile or reveal an author-published successor, but do not automatically restore or replace a potentially withdrawn profile or use archived copies as a substitute.
Flag any such successor candidate for the user's review alongside the disappearance evidence.
Record search queries, search dates, candidate URLs or exact name keys, reasons for acceptance or rejection, and any unresolved alternatives.

## CSRankings

For every recipient, verify the existing populated `csrankings_name`; record blank keys as missing and not searched unless missing-link discovery was explicitly requested.
For authorized discovery or replacement of an existing wrong-person association, search the selected cached faculty sources, documented historical profile records and available alias/name-change evidence for candidates, and perform general web searches.
Use name variants, country, current and historical affiliations, research areas, publications, Scholar IDs and independently verified DBLP identities together to evaluate candidates.
A missing or poor-quality Scholar or DBLP profile does not preclude a CSRankings link supported by other evidence.
Add a clearly supported match using the source's exact `name`, including punctuation, disambiguation numbers and campus tags, and set `csrankings_name_alignment_date` to the UTC date the association is accepted.
Keep the ACM name unchanged; store the CSRankings identity only in its dedicated field.
For ambiguous candidates, preserve an existing unresolved association or leave a missing name link blank, and flag the alternatives for review.
When an authorized missing-link search finds no supported match, leave the key blank and record the search; a proven wrong-person existing link follows the correction and prior-decision rules above.
If a candidate needs source files or captures not already available, follow the evidence-refresh approval policy rather than automatically downloading them.

Resolve every populated `csrankings_name` exactly once against `data/csrankings_profiles.csv`; investigate absent or duplicate keys.
Compare the row's original name, institutional affiliation and its country, homepage, `scholarid` and any `dblp_profile` with the recipient's independently supported identity and affiliation history.
Use the selected cached faculty sources or an approved refresh to check inclusion as of the source date, and retained historical records to establish historical provenance.
Do not describe inclusion in an older source snapshot as confirmed current inclusion.
Respect source disambiguation numbers and campus tags: stripping them for candidate generation must not erase evidence of a namesake.
Ignore blank identifiers and `NOSCHOLARPAGE` as matching evidence.
The current table's DBLP field reproduces CSRankings' name-generated link; follow the [generation and acquisition rules](../../README_FOR_AGENTS.md#csrankings-dblp-link-generation).
Earlier audits used roster-derived DBLP links and cannot independently corroborate those same roster associations.
For current links, inspect retained captures or an approved refresh, recording the original generated URL, final URL, evidence time and author identity.
Compare the resolved author with the award-roster profile; `/pers/hd/` and `/pid/` spelling differences alone are not evidence of different people.
Generation is not a successful capture and does not update profile-crawl or name-alignment dates.
An upstream Scholar identifier can also be wrong; investigate conflicts rather than deciding by identifier alone.
Preserve the original CSRankings source fields, including demonstrably incorrect upstream identifiers; ignore established source errors as matching evidence and do not try to repair them.
Once independent evidence supports the recipient’s name association, treat an obvious upstream error as non-actionable; record a brief audit note when useful without opening a user-review item or repeatedly asking whether to fix it.
This does not suppress reflagging when the evidence calls the recipient's name association itself into question; source-field preservation and association review are separate decisions.
Do not modify upstream sources or submit upstream correction requests as part of this skill.
Use the independently reviewed award-roster profile for the accepted association; do not overwrite source fields or add override columns without a separate user request.

Classify the link as supported, wrong person, unresolved or missing in the audit; do not invent a CSRankings quality column.
Documented historical profiles absent from the latest sources remain eligible when identity and provenance are supported.
When applying obvious link corrections, preserve exact accepted keys and synchronize the table to the union of populated keys across both rosters using the name-link guidance.
Include newly accepted links in that synchronization, copying the original CSRankings source fields and retaining provenance for historical exceptions.
Check that each key belongs to only one recipient within a roster and that shared Fellows/Turing recipients use the same accepted key.
For a key shared across rosters, require matching nonempty normalized ACM recipient IDs; flag conflicting or unavailable identity evidence instead of inferring ownership from a shared profile URL or name.
Do not run the legacy name-inference builder to regenerate the canonical table.
Always derive the lookup table's DBLP URL from the original CSRankings name; never copy a reviewed award URL or redirect destination into it, or clear it because upstream is wrong.
Keep independently reviewed DBLP links and quality decisions in the award rosters; preserve CSRankings-generated links and flag material conflicts in the audit.

## Update CSV Dates

Apply date changes together with the corresponding accepted data changes, using UTC `YYYY-MM-DD` values.
Keep capture dates, name-alignment decision dates and table-synchronization dates distinct.
For Scholar, the date rules below apply when extraction/import is authorized; review-only acceptance records the new capture in the audit while preserving dates attached to existing imported statistics.
Clear a rejected URL’s paired date when applying an authorized link correction, and leave a newly adopted Scholar URL’s date blank until its statistics are imported.
For DBLP, record acceptance in review and advance the canonical capture date when the extract stage applies the accepted capture.
The CSRankings lookup table has no date column; record synchronization time in Data Notes and retain source-download timestamps in the evidence audit.

| CSV Field | Required Update |
| --- | --- |
| `acm_fellow_profile_crawl_date`, `google_scholar_profile_crawl_date`, `dblp_profile_crawl_date` in both award rosters | Use the actual `fetched_at` UTC date of the accepted successful capture for the stored URL. Extraction of an accepted new capture updates the date even if the URL is unchanged. |
| Capture date when a profile URL is added or replaced | Clear any old URL's date; populate the new date during authorized extraction from accepted evidence, including existing crawls. Leave blank while extraction is pending; never substitute today's review date. |
| Capture date when a profile URL is cleared | Clear the paired date in the same edit, and set the applicable Scholar or DBLP quality flag to `N`. |
| Capture date during a quality-only review, failed fetch or pending withdrawal decision | Preserve the previous imported date unless an authorized extraction applies a different accepted capture. Record the review or failed-attempt timestamp in the audit instead. |
| `csrankings_name_alignment_date` in both award rosters | Set to the UTC decision date when adding, changing or explicitly revalidating a supported name link, even if using existing evidence. Clear it when removing the name link; preserve it for unresolved cases, unrelated edits or source refresh alone. |
| `crawl_date` in `data/google_scholar_extracted_data.json` | If importing a Scholar record, derive its date from the same accepted capture as its stored profile data and metrics. Do not restamp old metrics to the date of a newer identity check. |

Keep dates consistent across shared award recipients using the same accepted profile capture or name-alignment decision.
Preserve capture timestamps and source dates in the evidence audit so every changed CSV date has a traceable basis.
Validate that cleared URLs and name links have blank paired dates, populated dates parse correctly, and no date was advanced simply because the skill ran.
After changing profile links, capture dates or Scholar imports, rebuild the [capture/import queue](../../README_FOR_AGENTS.md#capture-and-import-backlog); queue generation reads local data only and does not authorize a refresh.

## Record and Validate the Review

Produce a dated row audit covering every requested recipient and all three services.
Record the roster, ACM recipient identity and year, reviewed URL or name key, evidence mode (existing captures or approved refresh), fetch outcome where applicable and availability status as of the evidence date, prior and proposed quality, identity finding, country and institutional evidence with relevant time periods, publication count and inspection scope, coverage finding, contamination finding, concrete rationale, evidence URLs/capture dates, unresolved questions and action taken.
For CSRankings, publication-count and quality fields are not applicable; record the identity and source-provenance findings instead.
Record representative relevant and conflicting publications where they determine the decision.
Write the review summary and a completion-time entry in Data Notes according to repository conventions; preserve older audits as historical evidence.

Validate changes against the input snapshots: only authorized fields changed, original award rows/order remain intact, shared-recipient decisions agree, and every populated CSRankings key resolves exactly once with no unreferenced table rows.
Apply only the stage-authorized CSV date updates above and the repository's [profile capture-date rules](../../README_FOR_AGENTS.md#profile-crawl-dates), checking old and new dates in the field-level audit.
Verify every CSRankings DBLP link matches upstream-compatible generation, including links with known upstream errors, and that generated visualizations remain unchanged.
Run the source-field manifest checks; after an authorized source update, rebuild that manifest only from the independently retained inputs described in the name-link guidance, never merely to bless a local mismatch.

Report per-roster and per-service totals for reviewed, supported, poor-quality, missing and unresolved cases, distinguishing award rows from unique people and identity problems from coverage or contamination.
Separate applied obvious corrections from borderline cases awaiting the user's decision, and present the latter with enough evidence for individual review.
Report invalid, disappeared and potentially withdrawn profiles separately from missing stored links and ordinary quality problems.
Complete a full sweep only when every requested row has a recorded outcome; blocked or uncertain profiles remain explicitly unresolved.
Missing associations recorded as “missing—not searched in this audit” are valid completed audit outcomes, not unfinished discovery tasks; keep prior search history intact and do not imply they were never searched.
For a long review, retain resumable progress and identify what remains rather than presenting a sample as a completed sweep.
