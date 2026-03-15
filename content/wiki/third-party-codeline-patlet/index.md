---
title: third_party_codeline_patlet
date: "2005-10-31"
draft: false
categories:
  - "Wiki"
aliases:
  - "/doku/doku.php?id=third_party_codeline_patlet"
params:
  wayback_url: "https://web.archive.org/web/20190922023628/http://jayflowers.com/doku/doku.php?id=third_party_codeline_patlet"
  original_url: "http://jayflowers.com/doku/doku.php?id=third_party_codeline_patlet"
  archived_from: Wayback Machine

---

[[[third\_party\_codeline\_patlet](/doku/doku.php?id=third_party_codeline_patlet&do=backlink)]]

[JayFlowers](/doku/doku.php?id= "[ALT+H]")

Trace: » [third\_party\_codeline\_patlet](/doku/doku.php?id=third_party_codeline_patlet "third_party_codeline_patlet")

## Context

You want to focus on building the components for which you can add the most value, not on basic functionality that you can easily buy. Your codeline is associated with a set of external components that you will ship with your product. You may customize some of these to fit your needs. You need to associate versions of these components with your product. When you create your Private Workspace (6) or when you build a release for distribution, you need to associate these components with the version you are checking out. You also want your Repository (7) to contain the complete set of components that make up your system. This pattern shows how to track the third-party components in the same way you track your own code.

## Problem

What is the most effective strategy to coordinate versions of vendor code with versions of product code?

## Solution

Create a codeline for third-party code. Build workspaces and installation kits from this codeline.

third\_party\_codeline\_patlet.txt · Last modified: 2005/10/31 13:07 by jflowers
