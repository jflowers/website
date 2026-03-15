---
title: "CI Factory 0.8 Final Release!"
date: "2007-07-08"
draft: false
categories:
  - "Continuous Integration"
  - "CI Factory News"
  - "CI Factory"
  - "Tools"
aliases:
  - "/WordPress/?p=172"
  - "/WordPress/index.php?p=172"
params:
  wayback_url: "https://web.archive.org/web/20080606215710/http://jayflowers.com:80/WordPress/?p=172"
  original_url: "http://jayflowers.com:80/WordPress/?p=172"
  archived_from: Wayback Machine

---

## CI Factory 0.8 Final Release!

Announcing the final release for CI Factory 0.8.0.165. It can be downloaded [here](http://code.google.com/p/ci-factory/downloads/detail?name=CI-Factory-0.8.0.165.zip&can=2&q=) and the release notes can be viewed from [here](http://docs.google.com/Doc?id=dd6cv3jm_09r2s2h).

Update:  jeremyn11 and [Doug Seelinger](http://wss3.agileer.com/default.aspx) found an annoying bug in the installer.  Here is a [fixed version 0.8.0.166](http://code.google.com/p/ci-factory/downloads/detail?name=CI-Factory-0.8.0.166.zip&can=2&q=).

![iStock_000000152525XSmall](images/2007/07/iStock_000000152525XSmall.jpg) There have been a few surprises in getting the final out the door.  Due to a confluence of issues I did not complete the documentation.  I have said this before and it bears repeating.  Documentation for CI Factory is a nice to have.  There are enough examples of success not only in setting up new factories but creating new packages as well with what little documentation there is.  If you do find yourself in need of help just post to the user group.  I generally answer questions in less than 30 minutes.

That was the disappointing surprise, there were good ones too.  The one I am most excited about is dashboard linking.  This was a two line modification.  It was so simple I had a hard time not kicking myself for not seeing it sooner.  Normally when you click a link on the main dashboard, the project grid to be precise, you remain local to the machine hosting the dashboard.  This was due to the links not being fully qualified URLs.  I simply made the links fully qualified, with the base of the URL coming from the CCnet project’s webUrl property.  So, if the ccnet project A is hosted on machine A and you are clicking on the project A link on a dashboard hosted on machine B you will be sent to machine A’s build report for project A.  That is a mouth full.  I will do a detailed blog about it this weekend.  With a picture or two I am sure you will see how simple and flexible it is.  I am having a hard time coming up with a name.  It is a distributed/virtually consolidated dashboard.  Anyway…

Here is the complete list of improvements and fixes made since 0.8.0.153:

**Improvements**

Added echo of what change set is being gotten for getting from a change set  
Make multiTriggers available to use in ccnet config  
Concatenate base url derived from ccnet projects weburl property to the default.aspx link in the project grid  
Removed required attribute on tfs datatypes, no error lines when using refid  
Made Tfs Get reuse existing refid for fileset of gotten files  
Refactored TFS Package  
Added the option to overwrite in Tfs Package  
Added Success to email group notification type for ccnet email publication  
Integrated email publication with force user knowledge through check for integration property CCNetForcedBy

**Fixes**

Merge with CCNet Trunk to get fix for Claudio  
Fail in Tfs Get task if unable to get successfully  
Fix async part of Post Build Shim  
Fix - Account for distinction between blocked and filtered integrations  
Fix - remove the nant xmlns from the value when xml is set to true  
Fix lost build when a trigger filter blocks  
Fix unit test alert for broken builds  
Fix Current and other Path hard coding

There have been a lot of new features and improvements in the 0.8 series.  I can’t wait to see what the 0.9 series brings.
