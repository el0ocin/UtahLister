# UtahLister Repository System

This repository is the durable, public-safe knowledge base for UtahLister.

Its job is to make the business understandable without exposing the private codebase, customer material, or sensitive operational details.

## What Belongs Here

- stable business docs
- offer and pricing rules
- public-safe workflow and operating model docs
- positioning, messaging, and outreach guidance
- research summaries and source maps
- sanitized templates
- brand guidance
- business-state, roadmap, and launch-readiness summaries

## What Does Not Belong Here

- application source code
- automation scripts
- website source files
- deployment configuration
- customer credentials or account-access workflows
- customer photos, proof screenshots, or raw working folders
- private internal URLs, exact workspace structure, or live runtime paths
- raw security reports with implementation-specific findings

## Source-Of-Truth Order

1. This repo for durable business understanding and approved documentation.
2. Private operational systems for code, tooling, runtime, and live execution.
3. Working systems such as Notion or Drive for active job handling and day-to-day operations.

## Canonical Repo Map

### Core business docs

- [../README.md](../README.md)
- [README.md](README.md)

### Research library

- [../Research](../Research)

### Templates

- [../templates/client](../templates/client)
- [../templates/notion](../templates/notion)

### Brand rules

- [../brand/README.md](../brand/README.md)

## Maintenance Rules

When UtahLister learns something important from research, delivery, or real customer work:

1. update the relevant business doc in `docs`
2. update any matching template or research summary if the change affects repeatability
3. keep the explanation public-safe and remove private implementation details
4. store code, customer proof, and sensitive runtime material outside this repo

## Public Repo Test

Before adding a file, ask:

1. Does this help someone understand the UtahLister business?
2. Would it still be safe if the repo were public?
3. Does it avoid exposing code, customer data, or sensitive internal setup?

If the answer to any of those is `no`, the file does not belong here.
