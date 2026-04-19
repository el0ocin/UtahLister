# UtahLister Official End-to-End Service Workflow Architecture

## Core findings

**1. Research Scope Summary**

**Focus (in-scope):** This research finalizes UtahLister’s **official end-to-end service workflow architecture** from intake through proof capture, for a marketplace listing service where the **customer posts through their own account** but UtahLister handles as much of the work as possible. It defines what each step means, the sub-steps inside each step, required decision gates, exception paths, and what is customer-facing vs internal-only.

**Key constraints (facts):**  
- **Account access:** Requesting/handling customer login credentials is a workflow risk because platform terms commonly prohibit password sharing and “giving access” to accounts. entity["company","Meta","social media company"] Terms explicitly say users must not share passwords or give account access to others without permission. citeturn2search0  
- **Platform-specific compliance matters:** Listings can be blocked/hidden/removed if they violate platform rules (e.g., prohibited items, duplicate listings, incorrect/mismatched listing details). citeturn0search30turn0search2turn0search1turn0search5  

**Prior project research used:** UtahLister’s internal “Marketplace Resale System” playbook emphasizes: (a) decide **speed vs profit** early; (b) “truth-first” photos; (c) default posting order (Facebook Marketplace + KSL) unless item-specific reasons change it; (d) a “listing polish checklist” (lead photo, title keywords, honest condition) and a “not selling” rescue pattern. fileciteturn1file0

**External sources used (high-trust, decision-useful):**  
- Platform rules + posting requirements for **entity["company","Facebook Marketplace","commerce feature"]** (required fields + prohibited items + safety tips). citeturn3search0turn3search17turn0search5turn1search24turn1search4  
- Platform rules + fraud-guidance for **entity["company","KSL Classifieds","classifieds site utah"]** (posting rules, why listings don’t show, fraud tips). citeturn0search2turn0search30turn1search1turn1search5  
- Workflow frontstage/backstage distinction via service blueprinting guidance from **entity["organization","Nielsen Norman Group","ux research firm"]**. citeturn2search3turn0search3  
- Documentation/proof capture practices aligned with dispute evidence guidance from **entity["company","Stripe","payments platform"]**. citeturn1search2turn1search14  
- Photo quality standards to operationalize “photo review” from **entity["company","eBay","online marketplace"]** photo tips (clear, non-pixelated, minimum resolution). citeturn1search7  
- Listing quality + transparency norms from **entity["company","OfferUp","local marketplace app"]** selling guidance (great photos, clear titles, accurate descriptions, fair prices; transparency about defects). citeturn3search3turn3search7  

**Out of scope (explicitly not finalized here):** detailed SOPs per sub-step, tool stack selection (CRM, automation, storage), marketing funnel and acquisition, staffing, and long-term tier expansions beyond what impacts workflow architecture.

---

**2. Executive Summary**

**Fact (platform + security reality):** UtahLister’s workflow must be designed around the assumption that the **customer posts listings through their own account** to avoid account-access violations (e.g., password sharing / giving account access). citeturn2search0turn2search2

**Recommendation (official architecture):** Adopt an **11-stage official workflow** that functions like a **state machine** (jobs move forward only when entry criteria are satisfied; otherwise they branch into exception paths). The biggest fixes vs the rough draft are:
- Add an explicit **Intake Validation + Eligibility** stage before any drafting (prevents wasted labor and platform-policy risks). citeturn0search1turn0search5turn0search2turn0search30  
- Split “review photos” into two distinct realities: **photo quality** (can we sell?) and **information completeness** (can we write accurately?). This aligns with platform guidance emphasizing clear photos + accurate, transparent descriptions. citeturn3search3turn1search7turn3search0  
- Make “post” a formal customer handoff stage with required outputs: **URL (preferred) or screenshots**, because KSL and similar platforms may block/hide listings if rules are triggered, and UtahLister needs verifiable proof of “live listing” completion. citeturn0search30turn1search2turn1search14  
- Reframe “capture proof” as a disciplined **evidence packet** (timeline, deliverables, client acknowledgment, and links), which is consistent with payment dispute best practices (chronology + documentation + proof of delivery/service + policies). citeturn1search2turn1search14  

**Strong opinion (because the business is lean):** The “secret sauce” isn’t more steps—it’s **crystal-clear definitions + gates** so the workflow doesn’t become a polite chaos-machine where every job stalls at “waiting on customer.”

**Most realistic workflow right now:** Use a **single default service lane** (one-item or one-batch at a time), require **payment before production**, include **one structured revision pass within the 48-hour window**, and treat anything else as an exception path with explicit rules. This matches UtahLister’s existing internal emphasis on low mental overhead and decisive strategy (quick sale vs profit). fileciteturn1file0

---

**3. Problems and Gaps in the Current Rough Draft Workflow**

Rough draft:  
Intake received → review photos → price lane selected → payment received → draft → QC → deliver → post → log URLs → 48-hour review → capture proof

**What is unclear (and why it matters):**
- **“Price lane selected” ambiguity:** It is unclear whether this means (a) the **UtahLister service tier/price** or (b) the **item pricing strategy** (quick sale vs max profit). UtahLister’s own prior research heavily uses “quick sale vs max profit” as a decision system for the *item*, not the service fee. fileciteturn1file0  
  **Recommendation:** Rename into two separate decisions: **Service Lane (tier/fee)** and **Item Pricing Strategy (quick-sale vs profit-preserving)** so you never mix them again.
- **“Review photos” is underspecified:** Photo review must cover at least three distinct checks:
  1) photo clarity/coverage (sellability), 2) correctness for item identification, 3) policy risk (prohibited/restricted categories). Platform guidance consistently links good listings to clear photos + accurate details, and policies constrain what can be listed. citeturn3search3turn1search7turn0search1turn0search5  
- **No explicit intake completeness gate:** Without a “Definition of Ready,” solo-operator time gets eaten by back-and-forth (missing measurements, missing brand/model, missing damage shots). This is a predictable bottleneck for a listing service because the listing fields themselves require structured details (title/price/category and often condition/description). citeturn3search0turn3search1turn3search7  
- **No explicit eligibility/policy gate before drafting:** Facebook Marketplace requires compliance with commerce policies; KSL has posting rules and can suppress listings for prohibited products, mismatched details, duplicates, etc. If UtahLister drafts first and discovers a policy issue later, it burns time and increases customer friction. citeturn3search17turn0search5turn0search2turn0search30  
- **“Post” is not defined as a customer handoff:** Since customers post through their account, “post” cannot be an internal action. It must be defined as: (a) customer publishes, (b) UtahLister verifies correct posting, (c) UtahLister logs link. Otherwise you cannot reliably reach “log URLs” or do a 48-hour review.
- **Proof capture is vague:** Proof should not be “a screenshot somewhere.” For dispute defense and operational clarity, it should be a standard evidence packet organized chronologically (deliverables sent, listing URL, client acknowledgment, revision notes). Stripe’s dispute guidance explicitly emphasizes chronological organization and proof of service/delivery plus policies (refund/terms). citeturn1search2turn1search14  

**What is missing (high-impact gaps):**
- **Client account safety policy:** Because terms prohibit password sharing / giving access, UtahLister should explicitly avoid collecting credentials and instead design workflow around customer posting. citeturn2search0turn2search2  
- **Customer-facing status updates:** Customers should see a small set of understandable stages (Submitted → Needs Info → Paid/Queued → Draft Delivered → Awaiting Posting → Live Verified → 48-hour Check → Complete). This reduces confusion and “where are we?” messages (a major solo-operator drain).  
- **Exception paths and pause rules:** The rough workflow has no “Needs Info,” “On Hold,” “Cancelled,” “Refunded,” or “Rejected (policy)” states—so the real workflow will leak time and create disputes.

## Official workflow architecture

**4. Recommended Official End-to-End Workflow for UtahLister**

**Fact (posting mechanics):** Marketplace platforms structure listings around standard fields (photos + title/price/category and often condition/description/location), so UtahLister’s workflow must produce a “listing package” that maps directly onto those fields. Facebook Marketplace’s own “Sell something” flow includes title, price, category, adding photos, and publishing. citeturn3search0  
Similarly, Facebook’s group-selling flow enumerates listing boxes such as Title, Price, Category, Condition, Description. citeturn3search1  
OfferUp’s posting guidance also reflects the reality of structured listing fields and photo limits. citeturn3search7  

**Fact (policy constraints):** Items listed on Facebook Marketplace must comply with Meta’s Commerce Policies, and there are categories that can’t be listed. citeturn3search17turn0search5turn0search1  
KSL posting rules restrict certain categories (e.g., firearms prohibited per their posting rules page) and require listings to follow platform rules; violations can suppress a listing. citeturn0search2turn0search30  

**Recommendation (architecture):** UtahLister should operate a workflow with:
- **Frontstage (customer-facing) milestones** that are simple and confidence-building.
- **Backstage (internal-only) stages** that protect quality, compliance, and time.
This is exactly the purpose of separating visible vs invisible service actions (line of visibility) in service blueprinting. citeturn2search3  

**Recommended end-to-end architecture (high-level):**
- Treat each job as a **single record** that moves through states with entry/exit criteria.
- Maintain two parallel “lanes” throughout:  
  - **Service Lane:** what the customer bought (tier/fee/deliverables)  
  - **Listing Strategy:** quick-sale vs profit-preserving pricing approach and platform plan (drives the draft)
This avoids the “price lane” ambiguity problem found in the rough draft and aligns with UtahLister’s internal strategy language around quick sale vs max profit. fileciteturn1file0  

---

**5. Recommended Primary Stages**

Below are the **official primary stages** UtahLister should use as the canonical workflow. Each stage is written so it can be implemented as a Kanban column and as a customer status (where appropriate).

1) **Intake Received & Job Created**  
2) **Intake Validated & Eligibility Screened**  
3) **Asset Review & Clarifications**  
4) **Service Lane Selected & Quote Confirmed**  
5) **Payment Confirmed & Scheduled**  
6) **Listing Package Drafted**  
7) **Quality Control & Policy Compliance Check**  
8) **Delivered to Customer**  
9) **Customer Posts & UtahLister Verifies Live Listing**  
10) **Link Logging & 48-Hour Performance Review**  
11) **Proof Capture & Closeout**

**Why these stages (recommendation anchored in facts):**
- They explicitly incorporate platform-policy gates (Facebook and KSL have prohibited categories and enforcement patterns). citeturn3search17turn0search5turn0search2turn0search30  
- They formalize “customer posts” as a required customer action, consistent with account-security constraints in platform terms. citeturn2search0turn2search2  
- They make proof capture a structured “evidence packet,” aligned with dispute evidence best practices. citeturn1search2turn1search14  

---

**6. Recommended Sub-Stages Within Each Primary Stage**

**Stage 1 — Intake Received & Job Created**  
Sub-stages (recommendation):
- Capture intake via form/DM/email with minimum required fields aligned to listing platforms (photos + item basics + location/pickup constraints). citeturn3search0turn3search7  
- Auto/standard confirmation message: “Received, reviewing for completeness + eligibility.”  
- Create Job ID + internal record (timestamped).

**Stage 2 — Intake Validated & Eligibility Screened**  
Sub-stages (fact + recommendation):
- **Completeness check:** do you have enough info to create an accurate listing (title-worthy identity + condition + what’s included)? OfferUp explicitly notes listings sell fastest with great photos + clear titles + accurate descriptions + fair prices, and transparency about defects. citeturn3search3  
- **Policy screen:** check prohibited/restricted types. Facebook Marketplace enforces Commerce Policies and disallows certain items. citeturn0search5turn0search1turn3search17  
  For KSL, confirm the item category isn’t prohibited under their posting rules and that the listing won’t trigger suppression reasons (e.g., prohibited items, duplicates). citeturn0search2turn0search30  
- If not eligible: decline + recommend alternative (exception path).

**Stage 3 — Asset Review & Clarifications**  
Sub-stages (fact + recommendation):
- Photo quality audit: apply objective checks (sharp/non-pixelated, uncluttered, sufficient angles). eBay’s guidance emphasizes avoiding blurry/pixelated images and meeting minimum resolutions. citeturn1search7  
- Coverage audit: ensure photos support truthful description (defects, labels, model numbers). OfferUp stresses transparency about defects. citeturn3search3  
- Clarification request package: 1 message with a checklist of missing details + specific extra shots requested (loop until satisfied or customer stops responding).

**Stage 4 — Service Lane Selected & Quote Confirmed**  
Sub-stages (recommendation):
- Decide service tier deliverables (e.g., “FBMP + KSL copy + pricing + photo order + buyer scripts”).  
- Confirm turnaround window and number of revision passes included.

**Stage 5 — Payment Confirmed & Scheduled**  
Sub-stages (fact + recommendation):
- Collect payment; confirm it cleared; schedule into production queue.
- **Proof-friendly record:** store invoice and service terms/refund policy because dispute best practices emphasize including terms/refund policy and proof of service/delivery. citeturn1search14turn1search2  

**Stage 6 — Listing Package Drafted**  
Sub-stages (recommendation anchored in platform field reality):
- Produce platform-mappable deliverables:  
  - Titles, prices, categories, condition, description blocks (Facebook listing fields explicitly include title/price/category and often condition/description). citeturn3search0turn3search1  
  - Photo order guidance (cover photo recommendation + sequence)  
  - Buyer message scripts (from UtahLister’s internal playbook emphasis) fileciteturn1file0  
  - Safety + fraud reminders (platform-specific) citeturn1search24turn1search1  

**Stage 7 — Quality Control & Policy Compliance Check**  
Sub-stages (fact + recommendation):
- Accuracy check: no overclaims; condition honest; included items correct. (Transparency reduces downstream conflict; platform guidance stresses honesty.) citeturn3search3  
- Policy check: no prohibited goods (Facebook Commerce Policies; KSL posting rules). citeturn0search5turn0search2  
- Posting-risk check: ensure no triggers like “incorrect descriptions or prices that do not match the item” (KSL suppression reason). citeturn0search30  

**Stage 8 — Delivered to Customer**  
Sub-stages (recommendation):
- Deliver a single “Listing Packet” containing:  
  - Copy/paste blocks per platform  
  - A “Post Exactly Like This” checklist (fields + order)  
  - A “Send me the URL” instruction  
- Capture delivery timestamp.

**Stage 9 — Customer Posts & UtahLister Verifies Live Listing**  
Sub-stages (fact + recommendation):
- Customer posts via their own account (consistent with account-security constraints; don’t share passwords / don’t give access). citeturn2search0turn2search2  
- Customer sends URL (preferred) or screenshot proof (fallback).  
- UtahLister verifies:
  - Listing is visible/live  
  - Key fields match the packet  
  - Not rejected/hidden for rule violations (KSL provides reasons listings may not show). citeturn0search30  

**Stage 10 — Link Logging & 48-Hour Performance Review**  
Sub-stages (fact + recommendation):
- Log URLs and timestamps.
- Perform 48-hour review focusing on first levers: photo order, title clarity, description tightness, price alignment (mirrors UtahLister’s internal “meaningful change” approach). fileciteturn1file0  
- If weak performance: propose one decisive change (don’t panic-edit 10 things). This also aligns with OfferUp guidance to update listings (add photos/details/reconsider price) when not selling. citeturn3search3  

**Stage 11 — Proof Capture & Closeout**  
Sub-stages (fact + recommendation):
- Build and store an evidence packet: intake, payment record, delivered listing packet, listing URL/screenshot, 48-hour review message, customer acknowledgment. Stripe’s guidance emphasizes organizing evidence chronologically and including proof of service/delivery and policies. citeturn1search2turn1search14  
- Close job with a completion message + what to do next (e.g., “mark as sold” guidance if relevant).

---

**7. Entry and Exit Criteria for Each Stage**

Below are execution-ready criteria (recommendation), mapped to platform realities (facts cited).

**Stage 1 — Intake Received & Job Created**  
- **Entry:** customer submits request + at least 1 photo + contact channel.  
- **Exit:** Job record created; acknowledgment sent; queued for validation.

**Stage 2 — Intake Validated & Eligibility Screened**  
- **Entry:** Stage 1 complete.  
- **Exit (pass):** intake is “workable” (enough info to draft) AND item is allowed under target platforms’ policies/rules. citeturn3search17turn0search5turn0search2  
- **Exit (fail):** move to “Needs Info” (missing) or “Rejected (policy)” (not allowed), because platforms enforce prohibited categories. citeturn0search1turn0search2  

**Stage 3 — Asset Review & Clarifications**  
- **Entry:** Stage 2 pass OR Stage 2 “Needs Info” with new assets received.  
- **Exit:** photos/info meet minimum quality + coverage; clarification list resolved (or job paused).

**Stage 4 — Service Lane Selected & Quote Confirmed**  
- **Entry:** Stage 3 complete enough to size effort.  
- **Exit:** service tier + deliverables + turnaround confirmed in writing.

**Stage 5 — Payment Confirmed & Scheduled**  
- **Entry:** Stage 4 confirmed.  
- **Exit:** payment received/cleared; production start time assigned; evidence-friendly records stored (invoice + terms). citeturn1search14  

**Stage 6 — Listing Package Drafted**  
- **Entry:** Stage 5 complete.  
- **Exit:** draft packet includes all fields needed for posting (title/price/category + other required fields) consistent with platform flows. citeturn3search0turn3search1  

**Stage 7 — Quality Control & Policy Compliance Check**  
- **Entry:** Stage 6 complete.  
- **Exit:** accuracy verified + policy risks cleared (no prohibited items; avoids suppression triggers like mismatched description/price). citeturn0search5turn0search30  

**Stage 8 — Delivered to Customer**  
- **Entry:** Stage 7 complete.  
- **Exit:** customer has packet + posting checklist + “send URL” instruction; delivery timestamp captured.

**Stage 9 — Customer Posts & UtahLister Verifies Live Listing**  
- **Entry:** Stage 8 delivered.  
- **Exit (pass):** listing live + verified; URL/screenshot received; no obvious rule suppression. citeturn0search30  
- **Exit (fail):** exception path: “Posting Error,” “Listing Not Showing,” or “No URL Provided.”

**Stage 10 — Link Logging & 48-Hour Performance Review**  
- **Entry:** Stage 9 pass.  
- **Exit:** 48-hour review delivered; optimization actions proposed or applied; logged.

**Stage 11 — Proof Capture & Closeout**  
- **Entry:** Stage 10 complete OR customer declines optimization after review.  
- **Exit:** evidence packet stored; job marked complete; completion message sent (and any dispute-defense documentation organized chronologically). citeturn1search2turn1search14  

## Controls and exceptions

**8. Internal-Only Steps vs Customer-Facing Steps**

**Fact (service blueprinting):** A service blueprint distinguishes customer actions vs frontstage/backstage activities using lines of interaction/visibility; this is a practical way to separate what the customer sees from internal operations. citeturn2search3

**Customer-facing (what the customer should see):**
- Intake received (confirmation)
- Needs more info (if applicable)
- Quote/tier confirmed + payment link
- In production
- Delivered (listing packet)
- Awaiting posting (customer action required)
- Live verified (UtahLister confirms)
- 48-hour review delivered
- Complete

**Internal-only (backstage, customer doesn’t need to see):**
- Eligibility screen against platform policies/rules (Facebook Commerce Policies; KSL posting rules). citeturn0search5turn0search2  
- QC checklist completion (accuracy + policy + formatting)  
- Evidence packet assembly (for operational clarity + dispute defense). citeturn1search2turn1search14  

**Recommendation (make it explicit in UX):** In customer communications, only expose **~7 statuses** even though you run **11 internal stages**, because customers don’t benefit from backstage complexity—and a solo operator absolutely does not benefit from explaining it repeatedly.

---

**9. Required Decision Gates**

These are the “you shall not pass” gates (recommendation) that prevent wasted work, policy trouble, and disputes (facts cited).

**Gate A — Intake Completeness (Definition of Ready)**  
- **Decision:** Can UtahLister draft an accurate listing without guessing?  
- **Pass criteria:** photos + item identity + basic condition + what’s included + pickup/location constraints.  
- **Why:** Platforms and selling guidance emphasize accurate descriptions and transparency; missing info creates misrepresentation risk and rework. citeturn3search3turn0search30  

**Gate B — Eligibility / Policy Screen**  
- **Decision:** Is the item allowed on target platforms?  
- **Pass criteria:** no prohibited categories under Facebook policies and KSL posting rules. citeturn0search5turn0search1turn0search2  
- **Fail action:** decline or reroute platform strategy.

**Gate C — Service Lane Confirmation**  
- **Decision:** What deliverables are being purchased?  
- **Pass criteria:** tier chosen + included revision policy + turnaround set.

**Gate D — Payment Cleared**  
- **Decision:** Start production?  
- **Pass criteria:** payment confirmed + invoice/receipt stored.  
- **Why:** dispute-handling best practices emphasize documentation, proof of service, and policies; payment-first reduces exposure to unpaid labor. citeturn1search14turn1search2  

**Gate E — Draft QC Pass**  
- **Decision:** Is the listing packet safe and accurate to deliver?  
- **Pass criteria:** no prohibited content; accuracy validated; avoids known suppression triggers (e.g., incorrect description/price mismatch on KSL). citeturn0search30turn0search2turn0search5  

**Gate F — Live Listing Verified**  
- **Decision:** Can the job move to 48-hour review?  
- **Pass criteria:** URL/screenshot received; listing viewable.  
- **Why:** KSL explicitly lists reasons a listing might not show; you need verification before “48-hour review” becomes meaningful. citeturn0search30  

**Gate G — Proof Packet Complete**  
- **Decision:** Close the job?  
- **Pass criteria:** evidence packet assembled chronologically (deliverables, communications, URLs/screenshots). citeturn1search2turn1search14  

---

**10. Required Exception Paths**

Below are the required exception paths requested, written as execution rules (recommendation) anchored to known platform/workflow realities (facts cited).

**Incomplete intake**  
- **Detect:** missing required fields/photos (Gate A fails).  
- **Route:** Stage 2 → “Needs Info” → return to Stage 3 upon receipt.  
- **Rule:** single consolidated request message; job pauses after X days no response (timebox is a business policy decision).  
- **Why:** Listing creation requires structured details. citeturn3search0turn3search7  

**Weak photos**  
- **Detect:** blurry/pixelated, insufficient angles/coverage.  
- **Route:** Stage 3 → “Photo Retake Required.”  
- **Photo standard:** align to objective clarity guidance (avoid blurry/pixelated; meet minimum resolution). citeturn1search7  
- **Customer output:** resend required shots checklist.

**Unclear item identification**  
- **Detect:** brand/model/size uncertain; cannot write truthful title.  
- **Route:** Stage 3 clarification checklist (ask for label/serial/model photo, measurement shot, included accessories).  
- **Why:** OfferUp emphasizes accurate descriptions and transparency about defects; accuracy is non-negotiable. citeturn3search3  

**Pricing uncertainty**  
- **Detect:** comps conflict; item niche; condition unclear.  
- **Route:** Stage 6 draft includes two prices (quick-sale vs profit-preserving) + stated assumptions; escalate to customer decision.  
- **Why:** UtahLister’s internal OS relies on early “quick sale vs max profit” classification to prevent emotional discounting and chaos. fileciteturn1file0  

**Missing info (non-photo)**  
- **Detect:** missing dimensions, missing included parts, missing pickup constraints.  
- **Route:** Stage 3 clarification request; job pauses until resolved.

**Delayed payment**  
- **Detect:** Gate D fails.  
- **Route:** Stage 4 → “Awaiting Payment” with timebox; auto-cancel after policy-defined window.  
- **Why:** payment disputes are handled with documentation; starting work without payment increases risk. citeturn1search14  

**Customer delay (after delivery)**  
- **Detect:** customer hasn’t posted; no URL.  
- **Route:** Stage 8 → Stage 9 “Awaiting Posting.”  
- **Rule:** job can be “Delivery Complete / Posting Pending” after N days; mark “Complete (Delivered)” vs “Complete (Live Verified)” depending on tier.

**Incorrect posting**  
- **Detect:** customer posted wrong price/category/title; or forgot photos; or listing not visible.  
- **Route:** Stage 9 “Posting Fix Required” → provide a 1-page correction checklist.  
- **Fact anchor:** KSL lists “incorrect descriptions or prices that do not match the item being sold” and other issues as reasons listings may not show. citeturn0search30  

**No URL provided**  
- **Detect:** customer cannot send link.  
- **Route:** Stage 9 fallback: accept screenshot proof + listing title + timestamp; log as “No URL (Screenshot Only).”  
- **Why:** you still need verifiable proof for your own records (and dispute evidence best practice favors organized records). citeturn1search2  

**Weak early listing performance**  
- **Detect (48-hour review):** low views/messages/saves.  
- **Route:** Stage 10 optimization: change one primary lever first (lead photo/title/price) instead of random edits; this matches UtahLister’s internal “one meaningful change” approach. fileciteturn1file0  
- **Platform nuance (fact):** KSL suppression can be triggered by duplicate listings within 14 days; optimization might need to prefer edits over delete/repost during that window. citeturn0search30  

**Safety/scam concern (bonus, but operationally mandatory):**  
- **Detect:** customer asks about deposits, payments off-platform, or suspicious buyer behavior.  
- **Route:** provide platform-aligned safety guidance: Facebook recommends being wary of scams, verifying items, and related safety behaviors; KSL provides fraud-avoidance guidance (meet in safe place, secure payments, don’t accept overpayments). citeturn1search24turn1search4turn1search1turn1search5  

---

**11. Workflow Risks and Failure Points**

**Highest-probability friction points (inference grounded in platform + workflow facts):**
- **Waiting on customer** (missing info, reshoot photos, not posting, not sending URL). Because customers must post themselves (per account-security constraints), Stage 9 is the highest stall risk. citeturn2search0turn2search2  
- **Policy violations leading to removal/suppression:** Facebook Marketplace listings must comply with Commerce Policies; KSL may suppress listings for prohibited products, duplicates within 14 days, mismatched details, or inappropriate content. citeturn0search5turn3search17turn0search30turn0search2  
- **Weak photos:** If photos are blurry or don’t show key details, performance suffers and misrepresentation risk rises. eBay’s photo tips emphasize avoiding blurry/pixelated images and meeting minimum resolution. citeturn1search7  
- **Fraud/scam risk creating customer anxiety:** KSL and Facebook both publish safety/fraud guidance because scams exist in marketplace contexts. For a listing service, this means customers may ask for help interpreting suspicious messages, even if that isn’t officially part of the service. citeturn1search1turn1search24turn1news37  
- **Payment disputes / “I didn’t get the service” claims:** Without proof capture (deliverables + timestamps + acknowledgment), dispute response is harder. Stripe dispute evidence guidance emphasizes chronological organization and proof of service/delivery plus policies. citeturn1search2turn1search14  

**Risk controls (recommendation):**
- Enforce **Gate A (Definition of Ready)** and **Gate D (Payment cleared)** before production starts. citeturn1search14turn3search0  
- Make Stage 9 outputs non-negotiable: URL or screenshot proof.  
- Keep customer-facing workflow short and deterministic; keep exceptions codified with timeboxes.

## Implementation outputs

**12. Recommended Official Workflow UtahLister Should Use Right Now**

**Recommendation (official v1):** Adopt the 11-stage model above as the internal “truth,” but implement it operationally as **10 trackable statuses** plus **3 universal exception statuses**:

**Core statuses (run every job through these):**
1) Intake Received  
2) Needs Info (if required)  
3) Eligible / Quote Ready  
4) Awaiting Payment  
5) Paid / Queued  
6) In Production  
7) QC  
8) Delivered  
9) Awaiting Posting / Live Verification  
10) 48-Hour Review → Complete

**Universal exception statuses (usable from any stage):**
- On Hold (Customer Delay)  
- Rejected (Policy / Not a Fit)  
- Cancelled / Refunded (Policy-defined)

**Why this is the most realistic right now (inference):** It preserves the full architecture (quality + compliance + proof) while keeping the tracking board simple enough for a solo operator to run without turning into a spreadsheet goblin.

---

**13. Recommended Actions for UtahLister Right Now**

**Recommendation (in strict priority order):**
1) **Create the “Definition of Ready” intake form** that directly maps to listing fields and truth-first requirements (photos + title-worthy identity + condition + what’s included). citeturn3search0turn3search3turn1search7  
2) **Write and publish a “No Account Access” policy**: customer posts from their account; UtahLister never requests passwords. (This is aligned to terms that prohibit password sharing / giving account access.) citeturn2search0turn2search2  
3) **Create a standardized Listing Packet template** (deliverable format): FBMP + KSL sections, photo order, price strategy, posting steps, buyer scripts, safety notes. fileciteturn1file0  
4) **Create a QC checklist** that includes platform policy checks (Facebook prohibited items; KSL posting rules; KSL “listing not showing” triggers). citeturn0search5turn0search2turn0search30  
5) **Implement proof capture as a required closeout action** with an evidence packet template (chronology + proof of service + policies), consistent with dispute evidence best practices. citeturn1search2turn1search14  
6) **Define your exception timeboxes** (e.g., how long you wait for missing info, posting, payment) and make them part of the written service terms.

---

**14. What Should Be Saved to UtahLister’s Internal Database**

**Fact (dispute/record-keeping logic):** Dispute evidence best practices emphasize maintaining organized, chronological documentation, including proof of service/delivery and policies. citeturn1search2turn1search14  

**Recommendation (database objects + fields):**

**Customer (per buyer of the service):**
- Customer ID, name, preferred contact channel
- Platforms customer intends to use (FBMP/KSL/etc.)
- Consent flags (e.g., permission to store photos and listing drafts)
- Safety preferences (public meetups, cash-only, etc.)

**Job (one service engagement):**
- Job ID, created timestamp, current stage, stage timestamps (audit trail)
- Service lane (tier), price paid, payment method, invoice/receipt ID
- SLA/turnaround promise and actual turnaround measured
- Exception codes encountered (for analytics)

**Item (one listing target; may be one per job or multiple per job):**
- Item ID, category, brand/model (if known), condition notes, included items
- Photo set references (links/file IDs), “missing shots requested” log
- Pricing strategy (quick-sale vs profit-preserving) + recommended ask + floor + rationale summary (brief)

**Deliverables (what UtahLister produced):**
- Listing copy versions (v1, v2), platform-specific blocks
- Photo order recommendation
- Posting checklist version delivered
- Buyer scripts + safety notes

**Posting & verification:**
- Listing URLs (per platform) + timestamps  
- Screenshot proof if URL missing  
- “Verified live” flag + verification timestamp  
- If suppressed/removed: reason notes (if known) + action taken (KSL provides common reasons listings may not show). citeturn0search30  

**48-hour review:**
- Metrics captured (customer-reported or screenshot evidence)
- Optimization advice delivered (what changed and why)
- Follow-up outcome (accepted, declined, no response)

**Evidence packet (closeout bundle):**
- Chronological timeline summary
- Copies of key messages/emails
- Payment record references
- Final URLs / screenshots
- Final “completion acknowledgment” (even a “thanks!” message counts)

---

**15. MANUAL WORK REQUIRED AFTER RESEARCH**

This research defines the architecture, but the following must be created/implemented manually:

- Finalize workflow version naming (e.g., “Workflow v1.0”) and publish internally as the official standard.
- Turn each primary stage into an SOP (checklists, templates, timebox rules).
- Build the tracking board (Kanban columns + allowed transitions).
- Create the intake form (Definition of Ready) and the “missing info” auto-message template.
- Create the Listing Packet template and QC checklist template.
- Create the evidence packet template and storage conventions.
- Decide the official service lanes/tiers and revision policy (what’s included vs add-on).

---

**16. Metadata Block**

- Topic: UtahLister Official End-to-End Service Workflow Architecture (Customer Posts via Their Own Account)  
- Date: 2026-04-09 (America/Chicago)  
- Workflow Version: v1.0 (recommended)  
- Major Stages: Intake Received & Job Created; Intake Validated & Eligibility Screened; Asset Review & Clarifications; Service Lane Selected & Quote Confirmed; Payment Confirmed & Scheduled; Listing Package Drafted; Quality Control & Policy Compliance Check; Delivered to Customer; Customer Posts & UtahLister Verifies Live Listing; Link Logging & 48-Hour Performance Review; Proof Capture & Closeout  
- Key Decision Gates: Intake Completeness; Eligibility/Policy Screen; Service Lane Confirmation; Payment Cleared; QC Pass; Live Listing Verified; Proof Packet Complete  
- Key Exception Paths: Incomplete Intake; Weak Photos; Unclear Identification; Pricing Uncertainty; Missing Info; Delayed Payment; Customer Delay; Incorrect Posting; No URL Provided; Weak Early Performance  
- Source Types Used: Platform help/policy pages (Facebook/Meta, KSL, OfferUp, eBay); service design methodology (NN/g); payment dispute guidance (Stripe); internal project playbook  
- Confidence Level: High for workflow structure + gates; Medium for platform-specific optimization timing rules beyond what platforms explicitly state  
- Key Keywords: workflow architecture, service blueprint, intake validation, listing packet, QC, policy compliance, proof capture, 48-hour review, exception paths, solo operator  
- Suggested File Name: UtahLister_Workflow_v1_Official_End-to-End_Service_Architecture_2026-04-09.md  
- Suggested Notion Tags: Operations, Workflow, SOP-Prep, Service-Design, Marketplace-Listings, Quality-Control, Proof-Capture  

## End outputs

**A. OFFICIAL WORKFLOW DRAFT**

Intake Received & Job Created → Intake Validated & Eligibility Screened → Asset Review & Clarifications → Service Lane Selected & Quote Confirmed → Payment Confirmed & Scheduled → Listing Package Drafted → QC & Policy Compliance Check → Delivered to Customer → Customer Posts → UtahLister Verifies Live Listing → Log URLs → 48-Hour Performance Review/Optimization → Proof Capture → Closeout

---

**B. DATABASE-READY ENTRIES**

Copy-paste format (YAML). Adjust names to match your database schema.

```yaml
stages:
  - name: "Intake Received & Job Created"
    purpose: "Capture request, create job record, acknowledge receipt."
    entry_criteria:
      - "Customer request received with at least 1 photo and a contact channel."
    exit_criteria:
      - "Job ID created and timestamped."
      - "Receipt confirmation sent to customer."
    handoff_rules:
      - "Auto-move to 'Intake Validated & Eligibility Screened' within the next business processing window."
    exception_paths:
      - code: "E-INCOMPLETE-INTAKE"
        trigger: "Missing photos or missing minimum contact info."
        action: "Request missing minimum inputs; set status to Needs Info."

  - name: "Intake Validated & Eligibility Screened"
    purpose: "Ensure the job is workable and the item is eligible to list on intended platforms."
    entry_criteria:
      - "Stage 1 exit criteria met."
    exit_criteria:
      - "Definition-of-Ready check passed OR job marked Needs Info."
      - "Eligibility/policy screen passed OR job marked Rejected (Policy)."
    handoff_rules:
      - "If Needs Info: send one consolidated request, pause until response."
      - "If Rejected (Policy): send decline + alternatives, close job."
      - "If passed: move to Asset Review & Clarifications."
    exception_paths:
      - code: "E-POLICY-REJECT"
        trigger: "Item category prohibited for intended platform(s)."
        action: "Decline or reroute to eligible platform strategy if available."
      - code: "E-NEEDS-INFO"
        trigger: "Missing required item details (identity, condition, included items)."
        action: "Send checklist; pause job."

  - name: "Asset Review & Clarifications"
    purpose: "Review photo quality and information completeness; resolve uncertainties before drafting."
    entry_criteria:
      - "Eligibility screen passed."
    exit_criteria:
      - "Photos meet minimum clarity/coverage."
      - "All critical questions resolved OR job paused for customer response."
    handoff_rules:
      - "If photo retake required: send exact shot list and examples."
      - "If resolved: move to Service Lane Selected & Quote Confirmed."
    exception_paths:
      - code: "E-WEAK-PHOTOS"
        trigger: "Blurry/pixelated or missing key angles/labels."
        action: "Request retake; pause."

  - name: "Service Lane Selected & Quote Confirmed"
    purpose: "Lock scope: deliverables, turnaround, revision policy, and service price."
    entry_criteria:
      - "Assets workable enough to estimate effort."
    exit_criteria:
      - "Service lane/tier confirmed in writing."
      - "Invoice/payment link sent."
    handoff_rules:
      - "Do not start drafting until payment confirmed."
    exception_paths:
      - code: "E-SCOPE-CHANGE"
        trigger: "Customer requests deliverables outside selected lane."
        action: "Issue updated quote or keep within lane."

  - name: "Payment Confirmed & Scheduled"
    purpose: "Confirm payment cleared and assign production slot."
    entry_criteria:
      - "Quote confirmed."
    exit_criteria:
      - "Payment confirmed/cleared."
      - "Production start timestamp assigned."
    handoff_rules:
      - "If unpaid after timebox: remind, then cancel per policy."
    exception_paths:
      - code: "E-DELAYED-PAYMENT"
        trigger: "Payment not received by defined deadline."
        action: "Send reminder; auto-cancel if still unpaid."

  - name: "Listing Package Drafted"
    purpose: "Produce the full listing deliverable set mapped to posting fields."
    entry_criteria:
      - "Payment confirmed."
    exit_criteria:
      - "Draft packet complete (platform-specific copy blocks, pricing strategy, photo order, posting checklist, buyer scripts)."
    handoff_rules:
      - "Move to QC & Policy Compliance Check."
    exception_paths:
      - code: "E-PRICING-UNCERTAIN"
        trigger: "Comps unclear or item identification incomplete."
        action: "Include assumptions + 2-price option; flag for customer decision."

  - name: "Quality Control & Policy Compliance Check"
    purpose: "Verify accuracy, clarity, and policy safety before delivery."
    entry_criteria:
      - "Draft packet complete."
    exit_criteria:
      - "QC checklist passed."
      - "No prohibited content detected for intended platforms."
    handoff_rules:
      - "If QC fails: return to Drafted stage with specific fixes."
    exception_paths:
      - code: "E-QC-FAIL"
        trigger: "Accuracy or policy issue detected."
        action: "Revise; re-check QC."

  - name: "Delivered to Customer"
    purpose: "Send the finalized listing packet with clear posting instructions."
    entry_criteria:
      - "QC passed."
    exit_criteria:
      - "Delivery sent and timestamped."
      - "Customer instructed to post via their own account."
    handoff_rules:
      - "Set status to Awaiting Posting / Live Verification."
    exception_paths:
      - code: "E-DELIVERY-BOUNCE"
        trigger: "Email/message undeliverable."
        action: "Request alternate contact method."

  - name: "Customer Posts & UtahLister Verifies Live Listing"
    purpose: "Customer publishes listing(s); UtahLister verifies and captures link evidence."
    entry_criteria:
      - "Listing packet delivered."
    exit_criteria:
      - "URL received (preferred) OR screenshot proof received (fallback)."
      - "Listing verified live/visible."
    handoff_rules:
      - "If incorrect posting: send correction checklist and re-verify."
    exception_paths:
      - code: "E-NO-URL"
        trigger: "Customer cannot provide link."
        action: "Accept screenshots + listing title + timestamp."
      - code: "E-INCORRECT-POSTING"
        trigger: "Wrong price/title/category or listing not visible."
        action: "Provide fix checklist; re-verify."
      - code: "E-CUSTOMER-DELAY"
        trigger: "No posting evidence after timebox."
        action: "Reminder; then mark Delivered/Posting Pending or close per lane policy."

  - name: "Link Logging & 48-Hour Performance Review"
    purpose: "Log URLs and run early performance check; propose one decisive optimization if needed."
    entry_criteria:
      - "Listing verified live."
    exit_criteria:
      - "URLs logged with timestamps."
      - "48-hour review delivered (and any included revision completed)."
    handoff_rules:
      - "Move to Proof Capture & Closeout."
    exception_paths:
      - code: "E-WEAK-EARLY-PERF"
        trigger: "Low engagement signals; customer reports weak inquiries."
        action: "Recommend one primary lever change; document."

  - name: "Proof Capture & Closeout"
    purpose: "Assemble evidence packet and mark job complete."
    entry_criteria:
      - "48-hour review complete OR customer declines."
    exit_criteria:
      - "Evidence packet stored (intake, payment, deliverables, URL/screenshots, review notes)."
      - "Job marked Complete."
    handoff_rules:
      - "Close with completion message and next guidance."
    exception_paths:
      - code: "E-DISPUTE-RISK"
        trigger: "Customer dissatisfaction signals or refund request."
        action: "Escalate to resolution policy; preserve all evidence."
```

---

**C. MANUAL WORK REQUIRED AFTER RESEARCH**

- Choose and lock the final workflow name/version (e.g., “Workflow v1.0”) as the official standard.
- Convert each stage into an SOP (checklist + templates + examples + timeboxes).
- Build a tracking board with the recommended statuses and allowed transitions.
- Build the intake form (Definition of Ready) and the “Needs Info” message template.
- Create the Listing Packet template (deliverable) + QC checklist.
- Create the evidence packet template and define storage conventions (folder structure, naming).
- Define service lanes/tiers + revision policy + cancellation/refund rules and publish them.

---

**D. FILE AND STORAGE INSTRUCTIONS**

- Exact file name: **UtahLister_Workflow_v1_Official_End-to-End_Service_Architecture_2026-04-09.md**  
- Folder/category to store under: **UtahLister Research OS → Operations → Workflow Architecture**  
- Suggested database title/category for organizing later: **“UtahLister Ops Standards” → “Workflow v1.0”**