# UtahLister Productization Roadmap

## Short answer

This is not wishful thinking.

UtahLister can become a real internal app and eventually a customer-facing product.
The right first version is not a fragile "bot that posts everywhere automatically."
The right first version is a guided operator system that automates the repetitive work,
keeps a human in the approval loop, and only automates publishing where the platform
surface is officially supported and low-risk.

## What the first real app should do

1. Intake
- Customer submits item details, sale goal, optional private floor, and photo folder.
   - System validates required fields and file access.

2. Image pipeline
   - Pull images into controlled storage.
   - Strip EXIF and resize for safe internal use.
   - Flag blurry or weak cover-photo candidates.

3. Listing engine
   - Generate title, description, category suggestion, pricing lane, and buyer replies.
   - Force a human review before anything customer-facing is treated as final.

4. Policy and risk checks
   - Flag prohibited or restricted items.
   - Flag unsupported claims, missing condition disclosures, and risky wording.
   - Flag likely policy conflicts by marketplace.

5. Operator workspace
   - Show the item, images, selected lane, draft listing, and recommended next action.
   - Track status from intake to live listing to sold proof.

6. Posting support
   - Start with guided posting, not blind autoposting.
   - Give the operator a clean, final listing package and posting checklist.

7. Proof and learning loop
   - Capture clicks, messages, sale timing, and final sale price.
   - Feed outcomes back into pricing and copy rules.

## What should stay human-in-the-loop at first

- Final factual review
- Prohibited-item judgment
- Final pricing approval
- Final post/publish step
- Buyer negotiation edge cases

These are the highest-risk areas for false claims, policy issues, and account damage.

## Realistic phases

### Phase 1: Operator cockpit

Build a lightweight internal web app that replaces the current scattered workflow.

Core modules:
- intake dashboard
- item workspace
- image review
- pricing lane engine
- listing draft generator
- reply-script generator
- proof tracker

Success condition:
- one operator can run multiple items quickly without relying on memory or loose notes

### Phase 2: Controlled automation

Add automation around the safe middle of the workflow.

Examples:
- intake ingestion
- image cleanup
- draft generation
- rules-based QC
- research capture
- reporting and proof logging

Success condition:
- UtahLister gets faster and more consistent without increasing account or policy risk

### Phase 3: Selective integrations

Only automate live platform actions where official support, policy safety, and
operational reliability are acceptable.

Until that is verified, guided posting is the correct default.

## Recommended shape

### Front end
- Customer landing page and intake form
- Internal operator dashboard

### Back end
- API for items, drafts, pricing lanes, proof, and research
- image processing worker
- audit log and event tracking

### Storage
- private item/image storage
- relational data store for items, customers, drafts, and outcomes

### AI layer
- guarded prompt templates
- explicit structured outputs
- policy/risk checks before any draft is marked ready

## Why not jump straight to full autoposting

- Marketplace policy risk
- account-lock and trust risk
- unsupported claims risk
- fragile browser automation risk
- unreliable selectors and replay failures
- higher blast radius when something goes wrong

KSL's current public help still centers standard account-and-listing flows rather
than a production seller API workflow, which supports keeping manual publishing
in the loop for now:
- https://classifieds.ksl.com/resources/helpful-tips/welcome-getting-started-with-ksl-classifieds

For Facebook Marketplace, the current help surface I reviewed still points to
manual listing creation, editing, limits, and policy review. I did not verify a
clean public seller posting API in this pass, so direct autoposting should be
treated as unverified and higher risk until proven otherwise.

## Recommended next build after the website

Build Phase 1 only:
- operator dashboard
- intake record
- image ingest
- pricing lane output
- listing draft output
- reply output
- proof logging

That is the version most likely to save time, improve quality, and avoid creating
a policy or account problem.
