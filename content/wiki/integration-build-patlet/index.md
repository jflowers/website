---
title: integration_build_patlet
date: "2005-10-31"
draft: false
categories:
  - "Wiki"
aliases:
  - "/wiki/integration-build-patlet/"
params:
  wayback_url: "https://web.archive.org/web/20190922023230//wiki/integration-build-patlet/"
  original_url: "/wiki/integration-build-patlet/"
  archived_from: Wayback Machine

---

[[[integration\_build\_patlet](/wiki/integration-build-patlet/)]]



Trace: » [integration\_build\_patlet](/wiki/integration-build-patlet/ "integration_build_patlet")

## Context

All developers work in their own Private Workspace so that they can control when they see other changes. This helps individual developers make progress, but in many workspaces people are making independent changes that must integrate together, and the whole system must build reliably. This pattern addresses mechanisms for helping ensure that the code for a system always builds.

## Problem

How do you make sure that the code base always builds reliably?

## Solution

Be sure that all changes (and their dependencies) are built using a central integration build process.

integration\_build\_patlet.txt · Last modified: 2005/10/31 12:59 by jflowers
