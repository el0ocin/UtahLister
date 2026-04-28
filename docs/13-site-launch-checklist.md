# Site Launch Checklist

Use this before actively sending people to `utahlister.com`.

## Current private build status

The latest private site build now includes:

- dual-offer messaging: `New Listing Build` and `Listing Rescue`
- sample deliverable support
- proof and reviews sections
- stronger safety and trust language
- an intake flow that can branch by service path

That does not mean the public launch step is complete. The live domain still needs a full production verification pass.

## Launch-critical checks

1. Verify the live domain is serving the latest homepage, proof, reviews, sample package, and thank-you page.
2. Submit a real test lead through the live intake and confirm it arrives in the actual operating system.
3. Verify the intake clearly supports both `New Listing Build` and `Listing Rescue`.
4. Verify the live site stays on HTTPS from both apex and `www` with no downgrade hops.
5. Verify the live site is serving the expected CSP and referrer-policy metadata.
6. Verify the sample package link works on mobile and desktop.
7. Verify no raw proof screenshots, profile photos, or private image folders are exposed publicly.
8. Verify the safety language is visible:
   - seller keeps the account and payout
   - no passwords or verification codes
   - founder proof is labeled clearly when used

## Manual setup still required before promotion

- confirm the live intake endpoint and notification routing
- confirm the thank-you flow after successful submission
- confirm the service-area and contact details on the live domain
- confirm the public proof blocks only use approved, sanitized assets

## Safe rule

Do not promote the site broadly until the live production domain passes an end-to-end submission test.
