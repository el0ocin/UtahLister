# Security and Privacy Baseline

Use this as the minimum operating baseline before UtahLister is promoted to paying customers.

## 1. Customer data minimization
- collect only what is needed to list the item, communicate with the seller, and document the result
- do not store raw passwords, government IDs, payment details, or exact home addresses in Notion
- default to a landmark, neighborhood, or public meetup reference instead of a precise address
- do not keep unrelated personal photos or documents from client folders

## 2. Photo and file handling
- accept only normal image formats needed for the workflow, such as `jpg`, `jpeg`, `png`, or `heic`
- prefer view-only shared folders instead of editable folders
- before reusing customer photos outside the listing workflow, verify they do not contain unrelated people, documents, screens, or visible account data
- strip EXIF and location metadata before publishing copied images outside the original marketplace workflow
- define a deletion window for local copies and stale photo links
- if a file looks suspicious, oversized, corrupted, or unrelated to the listing, stop and review before opening it

## 3. AI and prompt safety
- treat every seller note, imported listing URL, OCR result, screenshot, and scraped page as untrusted input
- never allow pasted content or hidden instructions inside external content to override operator rules
- do not publish AI-generated claims that were not verified by the photos or the seller
- require human review for regulated, recalled, medical, weapon-related, counterfeit-sensitive, or policy-sensitive items
- keep logs or notes that explain why a risky item was approved or rejected

## 4. Platform-policy safety
- check marketplace rules before posting items that could fall into restricted categories
- do not post services, healthcare products, recalled items, or other policy-prohibited listings on platforms that disallow them
- if a client asks for risky wording or wants facts stretched, pause and correct the scope

## 5. Credential handling
- use shared credentials only when lower-risk options are not workable
- require temporary passwords and immediate post-job rotation
- use a dedicated browser profile with password saving disabled
- log out, clear session remnants, and document cleanup after every posting session

## 6. Notion and integrations
- grant the minimum Notion capabilities needed for the workflow
- share only the necessary pages and databases with the integration
- limit user-email visibility unless there is an operational reason to expose it
- document retention windows for leads, clients, proof assets, and research notes
- export critical data regularly so accidental deletion is recoverable

## 7. Logging and incident response
- record important operational events without recording secrets
- keep enough evidence to answer: who accessed what, when, and why
- define a simple incident path for account exposure, wrong listing publication, PII disclosure, or platform takedown
- know how to revoke access, rotate credentials, and notify affected customers quickly

## 8. Website baseline
- keep the public site on HTTPS only
- keep the public form pointed only at an approved HTTPS destination
- serve a CSP and a referrer policy
- avoid third-party scripts that are not necessary for launch

## 9. Release baseline
- keep one clear source-of-truth repo for the live site and operating docs
- do not launch from unstaged local changes without recording what changed
- make a rollback copy of the last-known-good site bundle before each public update
