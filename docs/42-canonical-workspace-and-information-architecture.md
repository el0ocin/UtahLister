# Canonical Workspace And Information Architecture

This document defines where UtahLister information should live and which system is authoritative for each type of information.

## Canonical source by domain

### GitHub repo

Use the repo as the canonical source for:

- the public-safe business handbook
- stable strategy docs
- research synthesis packs
- sanitized templates
- roadmap and operating-model summaries

The repo should not be the dump for raw working files.

### Local UtahLister workspace

Use the local workspace as the canonical source for:

- private code
- private tooling
- active experiments
- raw proof assets
- working screenshots
- temporary synthesis work before it is cleaned up

### Flash drive

Use the flash drive as the canonical source for:

- the portable operator runtime
- guided test runs
- portable input and output folders
- beginner-facing app usage docs

The flash drive is an operations tool, not the long-term business handbook.

### Google Drive

Use Google Drive as the canonical source for:

- seller asset storage
- active photo folders
- working proof libraries
- research-doc storage
- review screenshots and similar visual sources

Do not use Drive as the canonical source for repo mirrors or code history.

## Current reconciliation conclusion

As of April 28, 2026, UtahLister information exists across four overlapping systems:

- the GitHub repo
- the local private workspace
- the flash drive runtime
- Google Drive

The main issue is not missing material. The main issue is duplicate storage and mixed purpose.

The working rule should be:

- `repo = handbook`
- `local = build and raw work`
- `flash drive = portable runtime`
- `Drive = asset library`

## Research handling rule

Raw research should not go straight into the handbook.

Use this sequence:

1. collect raw research in a private or working folder
2. write one clean decision pack in `Research/`
3. update the canonical handbook docs in `docs/`
4. leave the raw folder private or clearly marked as support material

This avoids turning the repo into a brainstorm archive.

## Drive organization rule

Drive should have one active UtahLister working structure, not multiple competing mirrors.

Based on the current audit:

- the active lightweight Drive folder is the better working model
- older repo-style mirror folders should be treated as legacy reference or archive candidates
- review screenshots, marketplace photos, and research docs should stay separated by purpose

## Flash-drive organization rule

The flash drive should stay optimized for use, not for storage sprawl.

That means:

- keep clear `Start Here` guidance
- keep the runtime and support files separated from seller input/output folders
- avoid storing old test clutter indefinitely
- treat the flash drive as a portable execution environment

## Local workspace rule

The local UtahLister folder can contain both public-safe and private material, but it should remain understandable.

The practical rule is:

- use `docs/` and `Research/` for durable business knowledge
- keep raw proof and raw marketplace assets out of those canonical folders
- do not rely on memory to know which folder is authoritative

## What to keep synchronized

These things should stay synchronized on purpose:

- handbook-level business decisions
- roadmap changes
- pricing and service-model changes
- research conclusions that change operations

These things do not need to stay synchronized everywhere:

- raw screenshots
- duplicate exports
- temporary working bundles
- private runtime state

## Operating benefit

If UtahLister follows this structure, the result is:

- a cleaner public handbook
- less duplicated strategy work
- fewer "which copy is the real one?" problems
- easier onboarding into both the business and the private operating system
