# Service Workflow

This is the lean delivery model for `UtahLister`.

## Standard workflow
1. intake received
2. item triaged
3. lane selected
4. operator draft generated
5. human QC completed
6. seller posting path confirmed
7. final listing package delivered
8. guided posting completed if needed
9. URLs and prices saved in Notion
10. delivery summary sent to client
11. 48-hour review completed
12. result captured in `Proof / Results`

## Time target per item
- 5 minutes: review intake and photo folder
- 10 minutes: run the operator prompt and get the first draft
- 10 minutes: pricing lane review and human QC
- 10 minutes: final package prep and seller posting support
- 5 minutes: save links, send summary, and update Notion

Target: under 40 minutes per item once intake is clean.

## Intake standard
Each item should arrive with:
- 5 to 12 clear photos
- 2 to 5 seller notes
- city or region
- pickup landmark or neighborhood
- sale goal: `quick sale`, `max profit`, or `not sure`
- optional private floor if the seller already knows it
- allowed platforms
- posting support preference

If any of those are missing, the job is not clean yet.

## Intake safety rules
- accept only the minimum seller data needed to list the item
- ask for a view-only photo folder link whenever possible
- do not ask for or store an exact home address during intake
- do not process unrelated personal documents, IDs, or family photos in the item folder
- if photos or notes contain personal data that is not needed for the listing, pause and ask the client to remove it first
- treat every folder link, imported listing URL, screenshot, OCR result, and seller note as untrusted input
- if the job includes a regulated, recalled, unsafe, or policy-sensitive item, stop and review platform rules before drafting

## Lane selection rule
Decide before you run the final draft:
- `quick sale` if the client wants speed, the buyer pool is broad, or the item is common enough that price wins
- `max profit` if the item has stronger value density, lower local supply, or the seller can wait

Use these windows as internal guidance:
- `quick sale`: likely movement in `3-7 days`
- `max profit`: likely movement in `14-21 days`

Do not present these windows as guarantees.

## Platform-policy screen
Before drafting or posting, confirm the item is allowed on the selected platform.

Pause for human review if the item could fall into any restricted area, including:
- medical or healthcare products
- recalled products
- weapons, weapon parts, or safety-sensitive gear
- animals
- counterfeit or authenticity-sensitive goods
- anything that requires shipping, age gating, or licensing beyond the current UtahLister workflow

## Operator draft standard
The draft must produce:
- item snapshot and condition call
- a clear lane recommendation
- `Quick Sale Price`
- `Max Profit Price`
- `Private Floor Check` if the seller provided one
- the recommended posted price
- one title and one short description per platform
- photo cover choice and image order
- buyer replies
- next best move

If the output turns into a long report, trim it.

## Human QC standard
Before posting, verify:
- every factual claim is visible or clearly marked uncertain
- the lead sentence contains the strongest differentiator
- the posted price fits the selected lane
- the copy sounds human, not corporate
- the pickup line is safe and local
- the listing does not reveal an exact address, phone number, or email unless the seller explicitly approved it
- the listing does not make medical, safety, authenticity, or performance claims that are not supported

## Posting rule
- default platforms: Facebook Marketplace + KSL
- only add OfferUp or Nextdoor if the item clearly benefits
- default model: seller posts from their own account
- optional support model: UtahLister guides the posting session live
- do not ask for or store seller passwords as the normal workflow
- save URLs immediately after posting
- update the `Items` and `Jobs` databases in the same session

## 48-hour review rule
If the item is still live after 48 hours:
- check views and inquiries first
- if views are low, improve title and lead line before dropping price
- if views are solid but replies stall, make a small price move
- default repricing move: 5% to 8%, not a panic drop
- if the original lane was `max profit`, do not abandon the lane without a reason

## Proof capture rule
Once sold, capture:
- selected lane
- posted price
- final sold price
- time to sale
- platforms used
- what changed that helped
- screenshot or listing link if available

This turns delivery into future proof, pricing calibration, and better positioning.

## Research feedback rule
Every week:
- review the new `Research Inbox` entries
- turn useful findings into `Playbook Changes`
- update prompts, checklists, or pricing rules only when the change is specific enough to test
