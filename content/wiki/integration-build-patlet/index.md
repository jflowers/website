---
title: integration_build_patlet
date: "2005-10-31"
draft: false
categories:
  - "Wiki"
aliases:
  - "/doku/doku.php?id=integration_build_patlet"
params:
  wayback_url: "https://web.archive.org/web/20190922023230/http://jayflowers.com/doku/doku.php?id=integration_build_patlet"
  original_url: "http://jayflowers.com/doku/doku.php?id=integration_build_patlet"
  archived_from: Wayback Machine

---

[[[integration\_build\_patlet](/doku/doku.php?id=integration_build_patlet&do=backlink)]]

[JayFlowers](/doku/doku.php?id= "[ALT+H]")

Trace: » [integration\_build\_patlet](/doku/doku.php?id=integration_build_patlet "integration_build_patlet")

## Context

All developers work in their own Private Workspace so that they can control when they see other changes. This helps individual developers make progress, but in many workspaces people are making independent changes that must integrate together, and the whole system must build reliably. This pattern addresses mechanisms for helping ensure that the code for a system always builds.

## Problem

How do you make sure that the code base always builds reliably?

## Solution

Be sure that all changes (and their dependencies) are built using a central integration build process.

integration\_build\_patlet.txt · Last modified: 2005/10/31 12:59 by jflowers
