# Site Launch Checklist

Use this before you actively send people to `utahlister.com`.

## What is already done
- the site copy is updated to the Trek Marlin 5 proof story
- the intake form fields now match the real UtahLister intake
- the site has a fallback intake checklist at `site/intake-checklist.txt`
- the site reads its launch settings from `site/config.js`

## Final manual setup
1. Open `site/config.js`.
2. Add a real `formAction` for the intake destination you choose.
3. Keep `formMethod` as `POST` unless your provider requires something else.
4. Update the `readyMessage` if you want a different response-time promise.
5. If your provider supports redirects, use `site/thanks.html` as the success page.
6. Re-upload the full `site` bundle to Porkbun static hosting.
7. Verify both `utahlister.com` and `www.utahlister.com` stay on HTTPS without any redirect downgrade.
8. Verify the live site is serving the updated CSP/referrer metadata after upload.

## What still needs your personal input
- the final intake destination
- the actual contact or routing method behind the form
- whether you want to use a hosted form service, a published form page, or another endpoint

## Safe rule
Do not publicly promote the site until `formAction` is set.

Until then, the site will clearly tell visitors that the form destination is not connected yet and point them to the intake checklist instead.
