---
title: CI Factory Beta 0.9.0.159
date: "2007-11-23"
draft: false
categories:
  - "CI Factory News"
  - "CI Factory"
aliases:
  - "/WordPress/?p=199"
  - "/WordPress/index.php?p=199"
params:
  wayback_url: "https://web.archive.org/web/20071207183205/http://jayflowers.com:80/WordPress/?p=199"
  original_url: "http://jayflowers.com:80/WordPress/?p=199"
  archived_from: Wayback Machine

---

## CI Factory Beta 0.9.0.159

This is the fifth release of the 0.9 series, build 159.  You can read the [release notes here](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=44&Itemid=1) and [download from here](http://ci-factory.googlecode.com/files/CI-Factory-Beta-0.9.0.159.exe).

Notably new in this release:

Added [FxCop](http://www.gotdotnet.com/Team/FxCop/) Package, donated by [Steve Bohlen](http://unhandledexceptions.spaces.live.com/).  Steve has a nice blog post on it [here](http://unhandledexceptions.spaces.live.com/blog/cns!FC56A7CB585DF52F!247.entry).  Thanks Steve!

Added links from summary report sections to detailed reports for many Packages.

Allow initial version to be set in the Arguments.xml at install time.

Add the creation of a branching script: CreateBranch.xml.  It is located in the build directory.  Currently Subversion is the only Package that supports the necessary targets.  I am still working on Perforce, it has proven a little tricky.  The rest of the source control packages will have the targets implemented soon.

If you tried to use the new upgrade script in the last release on a 0.8 CI Factory project I am sure that it bombed on you.  That has been fixed!

There was more, read it in the Release Notes.




|

|
