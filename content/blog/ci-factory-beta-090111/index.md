---
title: CI Factory Beta 0.9.0.111
date: "2007-11-04"
draft: false
categories:
  - "CI Factory News"
  - "CI Factory"
aliases:
  - "/WordPress/?p=198"
  - "/WordPress/index.php?p=198"
params:
  wayback_url: "https://web.archive.org/web/20071105101246/http://jayflowers.com:80/WordPress/?p=198"
  original_url: "http://jayflowers.com:80/WordPress/?p=198"
  archived_from: Wayback Machine

---

## CI Factory Beta 0.9.0.111

This is the fourth release of the 0.9 series, build 111.  You can read the [release notes here](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=44&Itemid=1) and [download from here](http://ci-factory.googlecode.com/files/CI-Factory-Beta-0.9.0.111.exe).

Notably new in this release:

Archive Package and Diskspace Alert script to help manage the space on your build server.  It’s always a bummer when the build breaks because the build server ran out of hard drive space.

An upgrade script, this may be the most important part of this release.  That’s right!  There is now a script to help you upgrade to a new version of CI Factory.  It doesn’t do it all yet but it does a lot of the work for you.  Please find the new file upgrade.bat in the CI Factory root folder, next to run.bat.  Simply execute this, there is no need to configure anything first.  Well if you have changed ProjectsDirectory to something other than c:\Projects then you need to adjust that property in …\CI Factory\Install Scripts\Upgrade.xml.  The script will walk you trough the upgrade asking questions and doing the work.  There are a few steps that it does not yet do that you will need to perform:

> 1) If files were added then they need to be added to source control.   
> A brute force approach is to diff the tree, to identify which if any files need to be added.
>
> 2) If this is not the build server then you need to update the build server by hand from source control after you have finished updating source control.
>
> 3) Turn the ccnet server back on.

Stephen Bohlen contributed a patch to the Vault package that allows for shared repositores.

There were a bunch of lower level improvements as well, so of the more notable ones:

Added labelPrefix to the Perforce source control block for CCNet.

Moved all common variables to a dtd file Entities.xml.

There was more, read it in the Release Notes. ![:-)](http://jayflowers.com/WordPress/wp-includes/images/smilies/icon_smile.gif)
