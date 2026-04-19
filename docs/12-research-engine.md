# Research Engine

This is how `UtahLister` should get smarter without turning into a content-hoarding mess.

## Goal
Build a repeatable research loop that improves `UtahLister` results over time.

The output is not "more reading."

The output is:
- better pricing calls
- better titles and first lines
- better photo-order guidance
- better buyer replies
- better decision rules for when to hold or reprice

## Research stack
- `Knowledge Library`: durable source archive
- `Research Inbox`: extracted notes and actionable signals
- `Playbook Changes`: approved or rejected implementation decisions

The library stores the actual source material and long-form notes.

The inbox stores the useful extraction.

The change log stores what should actually affect delivery.

## Cadence
- daily scan: collect new signals
- weekly brief: summarize what matters and decide what to test

## Daily scan rules
Pull in only useful sources:
- official platform guidance from Facebook Marketplace, KSL, and adjacent resale platforms
- current articles about local resale pricing, listing conversion, and photo trust
- high-signal operator notes from completed jobs
- relevant examples of strong local listings and weak local listings
- durable books, reports, and podcast episodes when they teach principles that still map to local resale behavior

Reject:
- generic SEO filler
- broad e-commerce advice that does not fit local pickup
- content older than needed unless it still teaches a durable principle

## Knowledge Library rules
For each durable source, save:
- source title
- format
- publisher or author
- source URL
- published date
- platform relevance
- topics
- evidence strength
- currentness
- access type
- short summary
- why it matters
- the mechanism or principle that should change how UtahLister operates

Use the page body for:
- article notes
- chapter notes
- podcast notes
- implementation implications
- proof screenshots or internal observations

## What to capture in Research Inbox
For each entry, save:
- related knowledge source
- source
- platform
- topic
- published date
- URL
- short summary
- one concrete takeaway
- actionability level

## Weekly brief rules
Once a week, turn the inbox into a short implementation brief:
- what changed
- what still looks durable
- what should change in the operator prompt
- what should change in pricing
- what should change in QC or posting
- what should be ignored for now

## Playbook change rules
Only create a `Playbook Changes` item when the recommendation is specific enough to test.

Good example:

`For bulky furniture, call out stair access or easy loading in the first two lines when true.`

Bad example:

`Make listings more persuasive.`

Every playbook change should point back to:
- at least one `Knowledge Library` source
- at least one `Research Inbox` note or internal proof item

## Approval rule
Research can draft recommendations automatically.

Live changes to the offer, site, prompt, or SOPs should stay approval-gated until there is enough real proof data to compare before and after.

No future monetization change for buyer replies should go live unless:
- outside research still supports reply quality and question-led messaging as real conversion levers
- internal data shows people will actually pay for higher-touch buyer handling

## First automation shape
- daily scan automation: collect and summarize fresh sources into `Research Inbox`
- weekly brief automation: synthesize the week into approved or proposed `Playbook Changes`

## Seed priorities
Start the library with:
- official platform guidance from Meta, OfferUp, and eBay
- question-led conversation research
- response-time and trust signals
- negotiation and persuasion books with structured notes
- internal proof assets like before-and-after UtahLister listings

## Success metric
The research engine is working if it makes actual delivery faster, cleaner, and more effective than the average person using a generic AI prompt by themselves.
