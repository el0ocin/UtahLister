# Public Repo Boundary

This document defines what belongs in the UtahLister public-safe repo and what should stay private.

## The Rule

If a file helps someone understand the UtahLister business and is still safe to expose publicly, it belongs here.

If a file would expose code, customer data, runtime setup, or sensitive operating detail, it does not.

## Safe To Keep In The Repo

- business summaries
- offer and pricing docs
- workflow and operating-model docs
- brand and positioning guidance
- outreach scripts and public-safe marketing plans
- research summaries
- source registers
- sanitized templates
- business roadmap and current-state summaries
- high-level summaries of private build progress

## Keep Private

- source code
- prompt implementation details that expose private tooling behavior
- website source files and deployment configuration
- operator runtime setup
- customer photos and raw proof screenshots
- customer contact data
- credentials, 2FA flows, or account-access details
- raw security findings that reveal implementation specifics
- exact workspace structure, local paths, or internal service configuration

## Sanitization Rules

Before adding a doc, remove:

- local filesystem paths
- internal URLs
- raw screenshots with personal data
- exact workspace or integration configuration
- language that assumes shared customer credentials are part of the default model

## What To Do Instead Of Publishing Sensitive Material

- summarize the business lesson
- explain the operating decision
- capture the high-level status
- store the private implementation elsewhere

## Example Boundary

Good for the repo:

- "UtahLister has private operator tooling for photo QC, grouped batch review, and listing generation."

Not good for the repo:

- exact file paths
- application source code
- local runtime commands
- raw security findings tied to private implementation

## Commit Standard

Before anything is added to Git, check:

1. Is this a business document rather than private implementation?
2. Does it avoid code and runtime detail?
3. Does it avoid customer, proof, or credential exposure?
4. Would I still be comfortable with this on a public GitHub page?

If not, keep it out of the repo.
