# UtahLister — Cloudflare Pages Deployment Guide

## How to deploy (manual upload)

1. Go to [dash.cloudflare.com](https://dash.cloudflare.com) → **Pages** → your UtahLister project
2. Click **Upload assets** (the manual upload button, not the Git integration)
3. Drag the entire `site/` folder contents into the upload area — or zip the folder and upload the zip
4. Click **Deploy site**

**Files to upload every time:**
```
index.html
styles.css
script.js
config.js
favicon.svg
thanks.html
fonts/fonts.css
proof-trek-before.png
trek-bike-outdoor.jpg
trek-bike-proof.png
proof-nike-shorts-front.png
proof-nike-shorts-tag.png
proof-kalimba-front.png
proof-kalimba-kit.png
sample-listing-package.pdf
sample-listing-package.html
sample-listing-package-hero.png
sample-listing-package-preview.png
sample-listing-package-renders/page-01.png
sample-listing-package-renders/page-03.png
sample-listing-package-renders/page-05.png
intake-checklist.txt
```

## Important: do NOT let Manus overwrite these files

Manus built an earlier version of this site. **Any Manus-generated files will overwrite the redesign** if uploaded. Only upload from this local `site/` folder.

If you ever need to recover the current live version, download it from Cloudflare Pages → your project → latest deployment → **Download** before uploading new files.

## Fonts

Fonts load from Google Fonts CDN (`fonts.googleapis.com`). No local font files needed. The CSP in `index.html` and `thanks.html` already allows these domains.

## Form routing

Form submissions go to Formspree (`https://formspree.io/f/maqlnklb`) → forwarded to `youreachednicole@gmail.com`. Configured in `config.js`. No changes needed unless you move to a different form backend.

## Quick checklist before each deploy

- [ ] Tested the form flow locally (select a service path → fields appear → submit → redirects to thanks.html)
- [ ] Checked that images load (no broken img tags)
- [ ] Verified the Google Fonts import loads (requires internet connection)
- [ ] Ran through the site on mobile width (~375px) in browser devtools
