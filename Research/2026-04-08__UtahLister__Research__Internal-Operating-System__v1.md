Internal Operating System — Trackers, Fields, Templates, and Logs

# UtahLister Internal Operating System — Trackers, Fields, Templates, and Logs

## 1. Document Purpose and Scope

This document defines the minimum viable internal operating system UtahLister should use to run jobs consistently, reduce confusion, support QC, capture proof, and build reusable business data without overbuilding too early.

It converts UtahLister’s approved workflow, offer structure, production logic, QC rules, post-delivery tracking, exception handling, and SOP architecture into a practical operating system for a solo founder. It is based primarily on prior project research and internal UtahLister operating documents, including the approved workflow architecture, post-delivery tracking logic, SOP set, offer/pricing research, intake/readiness research, QC framework, and founder ops materials.    

This document is intentionally built for **simple first, scalable later**. It assumes:

* customer posts from their own account
* UtahLister does not collect passwords
* seller keeps the item, buyer handoff, and payout
* payment clears before production
* one item equals one Listing Pack unless a bundle is explicitly defined
* proof capture is a real evidence packet, not a random screenshot folder   

---

## 2. Minimum Viable Internal Operating System for UtahLister

UtahLister should use one lean system, not scattered tools.

### Recommended minimum stack

1. **Primary working database:** Notion
   Reason: prior UtahLister materials already treat Notion as the working surface and specifically call for URLs and proof to be saved there.  

2. **File storage:** Google Drive
   Reason: separate durable file storage keeps screenshots, delivered packages, and evidence packets organized outside the database while preserving a simple operating model. Current UtahLister systems already include Google Drive. 

3. **Payments:** Stripe
   Reason: payment should clear before production; use the processor rather than storing card data directly.  

4. **Email / communications:** Gmail templates or canned responses
   Reason: UtahLister needs repeatable client communication without adding a separate CRM too early. 

### Minimum internal system objects

UtahLister should run on:

* one **Master Jobs Database**
* one **Intake Form**
* one **Template Library**
* one **File Storage Tree**
* linked logs for URL tracking, 48-hour review, proof capture, case studies, and exceptions
* one controlled set of statuses, reason codes, and naming rules  

### Recommended system design principle

The database should be the **single source of truth**. Files live in Drive. Links to files live in the database. Statuses are controlled. Every stage saves a record. Nothing important should live only in email, text, or memory.  

### Minimum viable database objects

UtahLister should create these database objects now:

* Customers
* Jobs
* Items
* Pricing-Lane Records
* QC Records
* Delivery Records
* URL Logs
* 48-Hour Reviews
* Proof Capture Records
* Case Study Records
* Exception Register
* Template Library  

### Security baseline

Do not store raw passwords, IDs, exact home addresses, or unrelated personal files in the working database. Treat imported screenshots and listings as untrusted input.  

---

## 3. Main Trackers and Logs UtahLister Should Have

UtahLister does **not** need ten separate apps. It needs one strong relational structure.

### Core trackers and logs

1. **Intake Form**
   Captures the submission and creates the job.

2. **Job Tracker**
   Master record for each service engagement.

3. **Stage / Status Tracker**
   Controls workflow movement, customer-facing status, timestamps, and blocked states.

4. **Pricing-Lane Record**
   Stores service lane, listing strategy, quote, scope, turnaround, and revision boundary.

5. **QC Checklist**
   Stores pass/fail review before delivery.

6. **Delivery Record**
   Confirms what was delivered, when, and what the client must do next.

7. **URL Log**
   Stores the live listing record per platform.

8. **48-Hour Review Log**
   Stores early performance metrics and the one recommended change.

9. **Proof Capture Log**
   Stores the evidence packet and proof assets.

10. **Case Study Tracker**
    Stores reusable, permissioned proof for marketing and proof library use.

11. **Exception Register**
    Stores every non-standard problem, trigger, action, and resolution.  

### Recommended structure rule

Use **one master job record**, then attach the other logs as linked records. Do not create a separate disconnected sheet for each job. That gets sloppy fast. 

---

## 4. Intake Form Field Structure

System Name:
Intake Form

Purpose:
Capture only the information UtahLister actually needs to determine fit, start a job record, screen for readiness, and reduce back-and-forth before quote and production. 

Required Fields:
**Confirmed:**

* Customer full name
* Email
* Phone
* Item title or basic identity
* Item category
* Condition
* Seller goal: quick sale / max profit / not sure
* City or pickup area
* Photos upload
* Included-item notes
* Basic defect notes if defects exist   

**Recommended:**

* Preferred platform(s)
* Best contact method
* Pickup constraints
* Urgency / target timeline
* Short free-text notes

Optional Fields:

* Brand
* Model
* Size / dimensions
* Color
* Serial / identifier if relevant
* Optional private floor or seller minimum
* Bundle notes
* Anything buyer should know
* Safety preferences for meetup guidance  

Status/Type Fields:

* Submission status: New / In Review / Needs Info / Rejected / Converted to Job
* Readiness status: Ready / Needs Clarification / Declined
* Intake source: Form / Email / DM / Referral
* Risk flag: Low / Medium / High

Who Updates It:
Customer submits it; UtahLister Founder/Operator validates and finalizes the internal intake status.

When It Gets Updated:
At submission, during intake review, and whenever missing info or additional photos are received.

What Decision It Supports:

* Is this job workable?
* Is this item allowed and in scope?
* Is there enough information to quote accurately?
* Does the job move to asset review or pause?  

Notes:
Keep the form lean. Too much friction lowers completion, but missing required fields causes rework. UtahLister should enforce required fields and use accept / clarify / decline logic. **DECISION NEEDED:** final mandatory-vs-optional line on private floor, platform preference, and advanced item details.  

---

## 5. Job Tracker Field Structure

System Name:
Job Tracker

Purpose:
Serve as the master operating record for each UtahLister service engagement from intake through closeout. This is the central tracker UtahLister should check first every day. 

Required Fields:
**Confirmed:**

* Job ID
* Customer ID or customer name
* Item ID or item short name
* Created timestamp
* Current internal stage
* Current customer-facing status
* Service lane
* Listing strategy
* Payment status
* Due date / turnaround promise
* Owner
* Exception flag
* Completion status  

**Recommended:**

* Priority
* Intake source
* Add-ons purchased
* Proof eligibility flag
* Case-study eligibility flag
* Repeat customer flag
* Founder time spent (minutes)
* Gross margin estimate later

Optional Fields:

* Notes
* Internal warnings
* Segment tag
* Category wedge tag
* Partner/referral source
* Satisfaction score
* Refund flag

Status/Type Fields:

* Internal stage
* Customer-facing status
* Payment status
* Fulfillment status
* Proof status
* Closure status
* Exception status

Who Updates It:
UtahLister Founder/Operator

When It Gets Updated:
At every stage change, payment event, delivery event, posting verification, review, closeout, and exception event.

What Decision It Supports:

* What needs attention now?
* Which jobs are blocked?
* Which jobs are overdue?
* Which jobs are ready for the next step?
* Which jobs are complete but missing proof?  

Notes:
This should be the single source of truth. Every other log should link back to Job ID. Founder-owned until delegation exists. 

---

## 6. Stage / Status Tracker Structure

System Name:
Stage / Status Tracker

Purpose:
Control workflow movement, allowed transitions, timestamps, blocked states, and the simplified customer-facing status view. UtahLister should run a detailed internal workflow and a simpler external status set at the same time. 

Required Fields:
**Confirmed:**

* Job ID
* Internal stage
* Stage entered timestamp
* Previous stage
* Next allowed stage
* Customer-facing status
* Blocked reason if any
* Next action date
* Owner  

**Recommended:**

* SLA due date for stage
* Reminder date
* Escalation flag
* Closeout reason code
* Pause date and resume date

Optional Fields:

* Notes to self
* Linked exception record
* Automation trigger status

Status/Type Fields:
**Recommended internal stages:**

* Intake, Validation & Eligibility
* Asset Review & Clarifications
* Service Lane & Quote Confirmation
* Payment Confirmation & Scheduling
* Listing Package Drafting
* QC & Policy Compliance
* Delivery & Posting Handoff
* Live Posting Verification
* URL Logging & 48-Hour Review
* Proof Capture & Closeout 

**Recommended customer-facing statuses:**

* Received
* Needs Info
* Quote Sent
* Awaiting Payment
* In Production
* Delivered
* Awaiting Posting
* Live Verified
* 48-Hour Review
* Complete 

Who Updates It:
UtahLister Founder/Operator; stage changes can later be automated from payment and review events.

When It Gets Updated:
Any time the job changes stage, pauses, reopens, closes, or triggers an exception.

What Decision It Supports:

* Can the job move forward?
* Is the job blocked?
* Has the client been told the right thing?
* Should a reminder or closeout rule fire now?

Notes:
Keep customer-facing statuses simple even if internal stages stay more detailed. **DECISION NEEDED:** final external status naming and exact allowed transitions. 

---

## 7. Pricing-Lane Record Structure

System Name:
Pricing-Lane Record

Purpose:
Store the quote decision, service scope, listing strategy, turnaround, revision boundary, and any custom pricing logic in a way that prevents future confusion.

Required Fields:
**Confirmed:**

* Job ID
* Service lane
* Listing strategy: quick sale / max profit / not sure
* Quote amount
* Included deliverables
* Excluded deliverables
* Turnaround promised
* Revision policy included
* Quote sent date
* Acceptance status  

**Recommended:**

* Complexity classification: simple / complex / custom
* Reason for lane selection
* Add-ons offered
* Add-ons accepted
* Expiration date for quote
* Bundle flag
* Rush flag
* Lane notes for future benchmarking

Optional Fields:

* Discount reason
* Referral adjustment
* Manual override reason
* Competitor comparison notes

Status/Type Fields:

* Draft Quote / Sent / Accepted / Declined / Expired / Custom Review Needed
* Listing strategy type
* Complexity type

Who Updates It:
UtahLister Founder/Operator

When It Gets Updated:
After asset review, when quote is sent, when the customer accepts, and if the scope changes.

What Decision It Supports:

* What exactly is being sold?
* What is included?
* What is not included?
* What gets invoiced?
* Does the job move to payment? 

Notes:
Service lane and listing strategy must stay separate. This is a core operating rule. **DECISION NEEDED:** final lane names, thresholds, pricing, turnaround promise, and revision boundary. 

---

## 8. QC Checklist Structure

System Name:
QC Checklist

Purpose:
Apply UtahLister’s pass/fail quality rules before delivery so no weak or incomplete package gets sent.

Required Fields:
**Confirmed:**

* Job ID
* Draft version reviewed
* QC reviewer
* QC date/time
* Title check result
* Description check result
* Pricing check result
* Category/platform check result
* Photo order check result
* Buyer reply scripts check result
* Posting instructions check result
* Policy/risk check result
* Overall pass/fail
* Approval timestamp or rework required flag   

**Recommended:**

* Defect codes
* Rework count
* Comments on weak spots
* Claims check passed checkbox
* Content rights confirmed checkbox
* Final package version approved

Optional Fields:

* Style notes
* Coaching note for future drafts
* Link to corrected version

Status/Type Fields:

* Pass / Fail / Needs Rework
* Defect vs Revision distinction
* Risk level: Low / Medium / High

Who Updates It:
UtahLister Founder/Operator

When It Gets Updated:
Immediately after drafting and before delivery; again if rework occurs.

What Decision It Supports:

* Is the package ready to send?
* What must be fixed before delivery?
* Is a failure a true defect or merely a preference revision?

Notes:
UtahLister research is explicit that defects and revisions are not the same. QC failures are objective defects and should trigger rework before delivery. **DECISION NEEDED:** final numeric QC thresholds for title length, photo minimums, and any hard pass/fail numbers UtahLister wants to enforce.  

---

## 9. Delivery Record Structure

System Name:
Delivery Record

Purpose:
Create a formal record of what UtahLister delivered, when it was sent, what instructions were included, and what the customer must do next.

Required Fields:
**Confirmed:**

* Job ID
* Final package version
* Delivery timestamp
* Delivery channel
* Included assets checklist
* Posting checklist version
* Delivery message sent
* URL request included
* Awaiting posting flag 

**Recommended:**

* Delivery acknowledgment received
* Posting Assist offered
* Posting Assist included or upsold
* Reminder due date if no post occurs
* Link to delivered package file

Optional Fields:

* Extra screenshots
* Live help booking link
* Client response notes

Status/Type Fields:

* Delivered / Awaiting Acknowledgment / Awaiting Posting / Delivery Issue / Completed
* Posting support type: None / Included / Upsell / Purchased

Who Updates It:
UtahLister Founder/Operator

When It Gets Updated:
At delivery, when client acknowledges, when posting support is offered, and when the post reminder window is reached.

What Decision It Supports:

* Has the handoff actually happened?
* Did the client get all needed instructions?
* Should the posting reminder fire now?
* Is optional support within scope?  

Notes:
The delivery stage is not complete when the file is merely sent. It is complete when the client has the package and clear next-step instructions. **DECISION NEEDED:** whether Posting Assist is included by default, upsold, or off by default. 

---

## 10. URL Log Structure

System Name:
URL Log

Purpose:
Store the live listing record per platform so UtahLister can verify posting, start the 48-hour timer, and preserve baseline proof.

Required Fields:
**Confirmed:**

* Job ID
* Platform
* Listing URL
* Screenshot fallback if no URL
* Post timestamp
* Listing title posted
* Category/subcategory posted
* Price posted
* Number of photos posted
* Live verification flag
* Verification timestamp
* Listing status  

**Recommended:**

* Listing ID if visible
* Cover photo used
* Initial views
* Initial saves/favorites
* Initial inquiries/messages
* Wrong-post / not-showing notes
* Repeat platform flag

Optional Fields:

* Campaign tag
* KSL service listing note
* Edit history notes
* Crosspost sequence note

Status/Type Fields:

* Pending URL / Verified Live / Needs Correction / Not Showing / Removed / Sold / Closed
* Proof type: URL / Screenshot Fallback

Who Updates It:
UtahLister Founder/Operator after the client posts.

When It Gets Updated:
Immediately when the client sends the live URL or screenshot; again if the listing changes materially or is removed.

What Decision It Supports:

* Did the client actually post?
* Is the listing live and trackable?
* Can the 48-hour review start?
* Is the listing usable as proof? 

Notes:
Use one row per live listing per platform. A single job may have multiple URL log entries if the item is posted on both Facebook Marketplace and KSL. Screenshot fallback is acceptable when URL is unavailable, but URL remains preferred. 

---

## 11. 48-Hour Review Log Structure

System Name:
48-Hour Review Log

Purpose:
Capture early performance, verify that the listing is still live and accurate, and document the one primary optimization recommendation if needed.

Required Fields:
**Confirmed:**

* Job ID
* URL Log link
* Platform
* Review due date/time
* Review completed date/time
* Views count
* Saves/favorites count
* Inquiries/messages count
* Live status confirmed
* Screenshot captured
* Issues found
* One recommended change
* Customer response to recommendation  

**Recommended:**

* First inquiry timestamp
* Clicks or shares if visible
* Customer-reported feedback
* Whether client changed the listing
* Whether the item sold before review
* Follow-up needed date

Optional Fields:

* 7-day check note if included in lane
* Benchmark comparison note
* Spam / scam contact note

Status/Type Fields:

* Due / Complete / Skipped / No URL / Sold Before Review
* Performance flag: Strong / Neutral / Weak
* Optimization type: Price / Photo / Copy / Category / No Change

Who Updates It:
UtahLister Founder/Operator

When It Gets Updated:
At the 48-hour mark, and again if the customer implements the recommendation or reports a sale.

What Decision It Supports:

* Is performance weak enough to justify intervention?
* What one change should UtahLister recommend?
* Can the job move to closeout or should it stay open? 

Notes:
UtahLister research recommends one decisive change rather than scattershot rewrites. One-week follow-up stays optional unless explicitly included in the lane. **DECISION NEEDED:** whether UtahLister tracks only views/inquiries or also saves, shares, and clicks by default.  

---

## 12. Proof Capture Log Structure

System Name:
Proof Capture Log

Purpose:
Store the evidence packet and all proof assets needed for dispute defense, internal learning, and future case-study selection.

Required Fields:
**Confirmed:**

* Job ID
* Evidence packet link
* Final URL(s) or screenshot fallback
* Live listing screenshot
* 48-hour review screenshot
* Key metrics summary
* Completion status
* Completion timestamp
* Proof completeness status  

**Recommended:**

* Before screenshot
* After screenshot
* Time to first inquiry
* Time to sale
* Sale outcome
* Testimonial received
* Testimonial permission status
* Completion acknowledgment message
* Lessons learned note

Optional Fields:

* Offer timeline
* Negotiation summary
* Final net payout if voluntarily provided
* Additional screenshots

Status/Type Fields:

* Complete / Partial / Proof Missing / Closed
* Reusable proof: Yes / No
* Permission status: None / Internal Only / Public Approved

Who Updates It:
UtahLister Founder/Operator

When It Gets Updated:
After the 48-hour review, at sale, and at final closeout.

What Decision It Supports:

* Is the job truly complete?
* Is there enough evidence for proof, disputes, or case study use?
* Does this job belong in the proof library? 

Notes:
Proof equals URL plus visuals plus data plus story. Capture proof that can vanish early, especially screenshots and live post evidence.  

---

## 13. Case Study Tracker Structure

System Name:
Case Study Tracker

Purpose:
Convert strong proof records into permissioned, reusable before/after proof for UtahLister’s website, proof library, referral trust, and future marketing.

Required Fields:
**Confirmed:**

* Job ID
* Proof Capture Log link
* Item category
* Platform
* Before state summary
* After state summary
* What changed
* Outcome metrics
* Permission status  

**Recommended:**

* Before screenshot link
* After screenshot link
* Quote/testimonial
* Publish-ready short narrative
* Redaction status
* Publish status
* Trust-signal tag: speed / price / clarity / proof

Optional Fields:

* Segment tag
* Locality tag
* Category wedge tag
* Video or carousel use notes

Status/Type Fields:

* Candidate / Awaiting Permission / Approved / Published / Archived
* Case type: Internal Learning / Public Proof / Referral Example

Who Updates It:
UtahLister Founder/Operator

When It Gets Updated:
When proof is strong enough, when permission is granted, and when a case is published or archived.

What Decision It Supports:

* Which jobs become proof cases?
* Which cases are publishable?
* What proof categories is UtahLister still missing? 

Notes:
UtahLister’s proof advantage comes from visible before/after transformation, pricing clarity, and measured outcomes. Public case studies must respect permission and truthful-results rules. 

---

## 14. Exception Register Structure

System Name:
Exception Register

Purpose:
Log every non-standard issue, the rule used, the action taken, and the final resolution so UtahLister stops improvising and starts learning from repeat problems.

Required Fields:
**Confirmed:**

* Exception ID
* Job ID
* Stage where it occurred
* Exception category
* Trigger
* Date opened
* Current status
* Pause / Continue / Close rule used
* Resolution
* Closure reason
* Closed date  

**Recommended:**

* Reminder count
* Customer message used
* Owner
* Root cause
* Lesson learned
* Repeat-pattern flag
* Escalation flag

Optional Fields:

* Refund amount
* Dispute reference
* Linked screenshot or email
* Policy citation note

Status/Type Fields:

* Open / Paused / Resolved / Closed / Escalated
* Categories:

  * Missing Info
  * Payment Pending
  * Quality Flag
  * Revision Requested
  * Wrong Post
  * No URL
  * Listing Not Showing
  * Client Delay
  * Out-of-Scope Request
  * Proof Missing
  * Refund Request 

Who Updates It:
UtahLister Founder/Operator

When It Gets Updated:
When an exception opens, when follow-ups happen, when status changes, and when the issue closes.

What Decision It Supports:

* Does the job pause, continue, or close?
* Which problems repeat most often?
* Which rules or templates need improvement next? 

Notes:
UtahLister research explicitly calls for exception flags, timeouts, and logging. **DECISION NEEDED:** final reminder windows and closeout timeboxes for missing info, missing payment, posting delay, and no-URL cases. 

---

## 15. Required Customer Communication Templates

Template Name:
Intake Confirmation

Purpose:
Acknowledge submission and set the expectation that UtahLister is reviewing fit and completeness.

Trigger:
New intake received.

Required Message Elements:

* Confirmation that the item was received
* Brief explanation that UtahLister is reviewing for fit and completeness
* Reminder not to send passwords or sensitive info
* Next expected step

Optional Elements:

* Estimated review window
* Link to photo standards

Notes:
This should be immediate and short. 

Template Name:
Clarification Request

Purpose:
Request missing details or better photos in one clean message.

Trigger:
Asset review finds gaps.

Required Message Elements:

* Exact missing details or photos needed
* Clear reason UtahLister needs them
* Action request
* Reply deadline or next follow-up timing

Optional Elements:

* Example photo references
* Reminder that turnaround pauses until missing items arrive

Notes:
Bundle requests into one message whenever possible. 

Template Name:
Payment Request

Purpose:
Move an accepted quote into paid production.

Trigger:
Customer accepts scope and quote.

Required Message Elements:

* Total due
* What is included
* Payment link or invoice
* Turnaround starts after payment clears
* No-work-before-payment reminder

Optional Elements:

* Quote expiration date
* Short scope recap

Notes:
Payment is the production gate.  

Template Name:
Delivery Message

Purpose:
Hand off the completed Listing Package and tell the client exactly what to do next.

Trigger:
QC passes and final package is ready.

Required Message Elements:

* Package is ready
* What is included
* Post from your own account
* Send live URL or screenshots after posting
* Reminder that UtahLister does not log into accounts

Optional Elements:

* Offer of Posting Assist if included or purchased
* Copy/paste posting checklist

Notes:
The message should be usable on mobile. 

Template Name:
Posting Reminder

Purpose:
Prompt the client to post quickly so the job does not stall and proof can begin.

Trigger:
No live URL or screenshot received within the reminder window after delivery.

Required Message Elements:

* Friendly reminder to post
* Reminder to send URL or screenshot immediately after posting
* Brief note that early posting supports tracking and review

Optional Elements:

* Offer to help if they are stuck
* Deadline before next follow-up

Notes:
Research supports a short prompt, not nagging. 

Template Name:
48-Hour Follow-Up

Purpose:
Report early performance and recommend one primary change if needed.

Trigger:
48-hour review completed.

Required Message Elements:

* Confirmation listing has been reviewed
* Metrics observed
* Any issue found
* One recommended change
* Next step

Optional Elements:

* Positive reinforcement if traction is good
* Ask whether the client wants the change explained more fully

Notes:
Do not dump ten suggestions. One strong recommendation is the rule. 

Template Name:
Proof / Testimonial Request

Purpose:
Collect usable proof and an honest testimonial after measurable progress or sale.

Trigger:
Item sells, gets strong traction, or closeout begins with enough proof to request feedback.

Required Message Elements:

* Congratulate or acknowledge outcome
* Ask for an honest short quote
* Request permission level for use
* Specify what proof is helpful: screenshot, sale result, message count, etc.

Optional Elements:

* Link to review page
* Brief reminder that no incentives are offered

Notes:
Feedback collection must be compliant and non-incentivized. 

Template Name:
Rejection / Out-of-Scope Notice

Purpose:
Close bad-fit jobs without ambiguity.

Trigger:
Item is prohibited, too incomplete, or outside UtahLister’s current boundaries.

Required Message Elements:

* Clear statement that UtahLister cannot take the job as submitted
* Short reason
* Any safe alternative or next step if appropriate

Optional Elements:

* Invite resubmission if missing info is fixable
* Suggest a different lane if that is the issue

Notes:
Use plain language. No vague “policy” brush-off. 

Template Name:
Completion Message

Purpose:
Confirm the file is closed and the final record is saved.

Trigger:
Proof capture and closeout complete.

Required Message Elements:

* Job is complete
* Final status
* What was saved
* Any last requested proof or testimonial if still outstanding

Optional Elements:

* Referral ask
* Review link

Notes:
Useful for clean closeout and later dispute defense. 

---

## 16. Recommended File and Naming Structure

UtahLister should use a **single shared file structure** that mirrors the workflow and proof system.

### Recommended top-level folders

* `UtahLister/00_Internal-Systems`
* `UtahLister/01_Templates`
* `UtahLister/02_Active-Jobs`
* `UtahLister/03_Completed-Jobs`
* `UtahLister/04_Proof-Library`
* `UtahLister/05_Case-Studies`
* `UtahLister/06_Policies-and-Terms`
* `UtahLister/07_Pricing-and-Playbooks`
* `UtahLister/08_Archive`

### Recommended per-job folder format

`JL-YYYYMMDD-###__ClientLast__ItemShortName`

Example:
`JL-20260409-001__Smith__TrekMarlin5`

### Recommended file names inside each job folder

* `JL-20260409-001__Intake`
* `JL-20260409-001__AssetReview`
* `JL-20260409-001__Quote`
* `JL-20260409-001__Invoice`
* `JL-20260409-001__ListingPack_v1`
* `JL-20260409-001__QC`
* `JL-20260409-001__Delivery`
* `JL-20260409-001__URLLog`
* `JL-20260409-001__48hReview`
* `JL-20260409-001__EvidencePacket`
* `JL-20260409-001__CaseStudy`
* `JL-20260409-001__ExceptionLog`

### Naming rules

* Always start with Job ID
* Use double underscores between major parts
* Use short, human-readable item names
* Use version numbers on editable deliverables
* Never store files without Job ID unless they are shared templates
* Never use customer passwords, exact home addresses, or unrelated personal data in file names 

### Recommended database naming

* Master database: `UtahLister Master Jobs & Proof Database`
* Case study database: `UtahLister Proof Library`
* Template database: `UtahLister Template Library`

Notes:
Research consistently points to strict folder conventions, saved records at every stage, and proof organization as part of defensibility.  

---

## 17. DECISION NEEDED

1. Final service lane structure: names, thresholds, and pricing. 
2. Final turnaround promise: standard and rush windows. 
3. Final revision boundary: exactly what the included revision round covers. 
4. Exact timeboxes for:

   * info-needed follow-up
   * payment reminder / pause / close
   * posting reminder
   * no-URL closeout
   * proof request follow-up 
5. Whether Posting Assist is included, upsold, or off by default. 
6. Whether message coaching exists at all, and if so, the cap by time and volume. 
7. Final QC numeric thresholds for photo minimums, title rules, and any hard fail numbers. 
8. Final launch category boundaries: what UtahLister accepts now versus later. 
9. Final internal and customer-facing status names. 
10. Final refund / cancellation language. 
11. Whether the intake form requires private floor or keeps it optional.  
12. Whether 7-day review is included by default or only in certain lanes.  

---

## 18. Recommended Actions for UtahLister Right Now

1. Build the **Master Jobs Database** first.
2. Build the **Definition of Ready Intake Form** second.
3. Build the **Listing Package template** third.
4. Build the **QC checklist** fourth.
5. Build the **URL Log and 48-Hour Review log** fifth.
6. Build the **Evidence Packet / Proof Capture record** sixth.
7. Add **exception categories, reason codes, and closeout rules** before taking volume.
8. Publish the **No Account Access / No Passwords** rule everywhere relevant.
9. Lock the **file naming structure** and make it non-optional.
10. Run pilot jobs through this operating system and tighten it using time-per-item, revision rate, and proof quality.  

---

## 19. What Should Be Saved to UtahLister’s Internal Database

UtahLister’s internal database should store only what directly improves delivery, proof, pricing, compliance, or repeatability.

### Save these objects and fields

**Customer**

* Customer ID
* Name
* Contact info
* Preferred contact method
* Platforms intended
* Consent / permission flags
* Safety preferences
* Repeat customer status 

**Job**

* Job ID
* Current stage
* Stage timestamps
* Service lane
* Listing strategy
* Quote and payment status
* Turnaround promised vs actual
* Exception codes
* Owner
* Completion status 

**Item**

* Category
* Brand/model
* Condition notes
* Included items
* Photo references
* Missing-shots log
* Quick-sale / profit-preserving strategy
* Recommended ask
* Optional floor
* Rationale summary 

**Deliverables**

* Title versions
* Description versions
* Photo order recommendation
* Category/platform guidance
* Buyer reply scripts
* Posting checklist version
* Delivery version sent 

**QC**

* QC results
* Defect codes
* Rework count
* Approval timestamp
* Claims check passed
* Rights confirmed checkbox 

**Posting / Verification**

* Listing URL
* Platform
* Post timestamp
* Verification timestamp
* Screenshot fallback
* Listing status
* Wrong-post / not-showing notes 

**48-Hour Review**

* Views
* Saves/favorites
* Inquiries/messages
* Issues found
* Actions taken
* Customer response
* Optional 7-day note if included 

**Proof / Closeout**

* Evidence packet link
* Before/after screenshots
* Sale outcome
* Time to first inquiry
* Time to sale
* Testimonial
* Lessons learned 

**Exceptions**

* Exception category
* Trigger
* Rule used
* Resolution
* Closure reason
* Lesson learned 

**Reusable libraries**

* Pricing lane library
* Proof case studies
* Reply scripts
* Compliance / trust policies
* Template library 

### Do not save

* Raw passwords
* Verification codes
* Exact home addresses unless absolutely required for a specific reason outside the standard workflow
* Government ID copies
* Unrelated personal files
* Stored card data  

---

## 20. MANUAL WORK REQUIRED AFTER CHAT

* Create the Notion databases and linked relations
* Create the Google Drive folder tree
* Build the intake form with required field validation and file upload
* Turn the QC structure into a real checklist
* Turn the delivery, posting reminder, 48-hour follow-up, and proof request into saved templates
* Create the Evidence Packet template
* Add the status rules and allowed transitions
* Add exception categories and closeout rules
* Decide the founder approvals listed in Section 17
* Test one dummy job from intake through proof capture
* Then run pilot jobs and tighten based on real time and real friction  

---

## 21. Appendix A — Database-Ready Entries

### System names

* UtahLister Master Jobs & Proof Database
* UtahLister Template Library
* UtahLister Proof Library
* UtahLister Pricing Lane Library
* UtahLister Exception Register

### Tracker names

* Intake Form
* Job Tracker
* Stage / Status Tracker
* Pricing-Lane Record
* QC Checklist
* Delivery Record
* URL Log
* 48-Hour Review Log
* Proof Capture Log
* Case Study Tracker
* Exception Register

### Required fields by system

**Intake Form**

* Customer Name
* Email
* Phone
* Item Title / Identity
* Category
* Condition
* Seller Goal
* City / Pickup Area
* Photos
* Included Items
* Defect Notes

**Job Tracker**

* Job ID
* Customer
* Item
* Created Timestamp
* Internal Stage
* Customer Status
* Service Lane
* Listing Strategy
* Payment Status
* Due Date
* Owner
* Completion Status

**Stage / Status Tracker**

* Job ID
* Internal Stage
* Stage Entered Timestamp
* Customer Status
* Blocked Reason
* Next Action Date
* Owner

**Pricing-Lane Record**

* Job ID
* Service Lane
* Listing Strategy
* Quote Amount
* Included Deliverables
* Excluded Deliverables
* Turnaround
* Revision Policy
* Acceptance Status

**QC Checklist**

* Job ID
* Draft Version
* Reviewer
* QC Timestamp
* Title Check
* Description Check
* Pricing Check
* Category/Platform Check
* Photo Order Check
* Buyer Replies Check
* Posting Instructions Check
* Policy Check
* Overall Result

**Delivery Record**

* Job ID
* Final Package Version
* Delivery Timestamp
* Delivery Channel
* Included Assets Checklist
* Posting Checklist Version
* URL Request Included

**URL Log**

* Job ID
* Platform
* Listing URL
* Screenshot Fallback
* Post Timestamp
* Title Posted
* Category Posted
* Price Posted
* Photo Count
* Live Verification Flag
* Verification Timestamp
* Listing Status

**48-Hour Review Log**

* Job ID
* URL Log Link
* Platform
* Review Due Date
* Review Completed Date
* Views
* Saves/Favorites
* Inquiries/Messages
* Screenshot Captured
* Issues Found
* One Recommended Change
* Customer Response

**Proof Capture Log**

* Job ID
* Evidence Packet Link
* URL Proof
* Live Screenshot
* Review Screenshot
* Metrics Summary
* Completion Status
* Proof Completeness Status

**Case Study Tracker**

* Job ID
* Proof Log Link
* Category
* Platform
* Before Summary
* After Summary
* What Changed
* Outcome Metrics
* Permission Status

**Exception Register**

* Exception ID
* Job ID
* Stage
* Exception Category
* Trigger
* Date Opened
* Current Status
* Rule Used
* Resolution
* Closure Reason
* Date Closed

### Template names

* Intake Confirmation
* Clarification Request
* Payment Request
* Delivery Message
* Posting Reminder
* 48-Hour Follow-Up
* Proof / Testimonial Request
* Rejection / Out-of-Scope Notice
* Completion Message

### Template triggers

* New intake received
* Missing info found
* Quote accepted
* Package delivered
* No URL received in reminder window
* 48-hour review completed
* Sale or strong proof captured
* Job rejected or out of scope
* Closeout completed

### File categories

* Internal Systems
* Templates
* Active Jobs
* Completed Jobs
* Proof Library
* Case Studies
* Policies and Terms
* Pricing and Playbooks
* Archive

### Naming rules

* Use Job ID first on all job files
* Use `JL-YYYYMMDD-###` format
* Use double underscores between major parts
* Include short client and item identifiers
* Add version number to editable deliverables
* Never include sensitive data in file names

### Unresolved decisions

* Final service lanes
* Final turnaround windows
* Final revision boundary
* Exact reminder / pause / close timeboxes
* Posting Assist policy
* Message coaching policy
* QC numeric thresholds
* Launch category boundaries
* Final status names
* Refund / cancellation policy
* Private floor required vs optional
* 7-day review included vs optional

---

## 22. Appendix B — File and Storage Instructions

**Exact file name for this document:**
`UtahLister_Internal_Operating_System__Trackers-Fields-Templates-and-Logs__v1__2026-04-09.md`

**Exact folder/category to store it under:**
`UtahLister/00_Internal-Systems`

**Suggested database title/category for organizing it later:**
`UtahLister Master Jobs & Proof Database`

**Storage instruction:**
Save this document as the operating reference inside `00_Internal-Systems`, then build the database and templates to match it exactly. The database should link out to Drive folders rather than storing every artifact as an unstructured attachment dump. 
