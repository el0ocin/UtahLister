# Private Build And Systems Summary

This document describes the UtahLister build work that exists privately without publishing code or sensitive implementation details.

## Why This Exists

The repo should still explain what has been built so far.

The right way to do that is to summarize the private systems at a business level while keeping the actual code, runtime, and operator setup outside the public repo.

## Private Systems That Exist Today

### Private operator tooling

UtahLister has private internal tooling to support the service workflow.

At a business level, that tooling currently covers:

- photo quality review
- light-touch photo enhancement
- mixed-item customer batch grouping
- hero-image selection and gallery ordering
- listing-copy generation
- human review before final output

### Private workflow support

There is also private workflow logic around:

- grouped customer photo batches
- item-by-item listing package preparation
- operator review checkpoints
- safer human-in-the-loop approval

### Private website and launch work

UtahLister also has private build work tied to:

- website implementation
- intake-path testing
- launch experiments
- runtime setup

## What These Systems Mean For The Business

The important business point is not the code. The important point is the capability.

UtahLister is no longer just a loose idea or a set of notes. It already has private operator systems that support:

- clearer listing preparation
- more structured intake handling
- more repeatable photo workflows
- more consistent listing-copy output

## What These Systems Are Not

These private systems are not:

- a public software product
- a customer-facing SaaS platform
- a fully autonomous autoposting engine

The service is still built around:

- human review
- seller-owned accounts
- controlled publishing
- trust-first operations

## How To Think About The Build

UtahLister currently has two layers:

### Public layer

- the documented business
- offer and workflow
- positioning and roadmap
- research and templates

### Private layer

- operator tooling
- runtime setup
- implementation code
- internal experiments

This repo is meant to document the public layer and summarize the private layer without exposing it.
