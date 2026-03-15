---
title: CI Factory Beta 0.9.0.14
date: "2007-09-12"
draft: false
categories:
  - "Continuous Integration"
  - "CI Factory News"
  - "CI Factory"
aliases:
  - "/WordPress/?p=186"
  - "/WordPress/index.php?p=186"
params:
  wayback_url: "https://web.archive.org/web/20071030174352/http://jayflowers.com:80/WordPress/?p=186"
  original_url: "http://jayflowers.com:80/WordPress/?p=186"
  archived_from: Wayback Machine

---

## CI Factory Beta 0.9.0.14

This is the first release of the 0.9 series, build 14.  You can read the [release notes here](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=44&Itemid=1) and [download from here](http://ci-factory.googlecode.com/files/CI-Factory-Beta-0.9.0.14.rar).

There is already a significant amount of change in this early release.  First off there is a NUnit Package now!  I am sure that a lot of people are saying about time.  There have been several performance improvements to CCNet, in particular the web dashboard.  One of the improvements that will make my life a lot easier in the NAnt scripting department is with xmlpeek.  I have improved the eval capabilities of the xpath expressions.  It should now work for any xpath expression, so things like sum(@testsrun) will work.  Lastly there have been some new CCNet NAnt functions added, allowing you to do things like write NAnt scripts to help testers get a test env setup for a build of their choosing.  Hopefully I will blog about these changes and more in the coming weeks.  Here are all the changes:

#### Beta 0.9.0.14

##### New

Added task to delete tfs subscriptions  
Added nant function to get date of last ccnet build  
Added ccnet nant function to get a list of build file names  
Added Setup Scripts to Power Tools  
Added NUnit Package and Tests  
Added CCNet NAnt function to get latest build file name  

##### Improvements

Added FreeText Mode to Ask task  
Added Add mode to XmlPoke task, named existing functionality replace mode  
Improved xpath eval of xmlpeek, now includes eval of functions like count()  
Added OuterXml property to xmlpeek  
Asyncexec/WaitForExit - Remove TaskNames from list after having waited on them  
Asyncexec/WaitForExit - Check to see if the Task exists before waiting on it  
Add interactive option to get in Subversion Package, uses Tortoise  
Added control over svn install location, no need to have in the path any more  
Added condition where when the build log files are on the same host as the dashboard the build logs are retrieved directly from the hard drive.  
SetupIIS.xml - Set to Classic ASP.Net for Vista.  
Performance improvements to CCNet core  
CCNet Server Aggregator - Implement more of the interface, allowing the aggregator to service dashboards  
Upgrade MbUnit to 2.4.1  
CCNet mod writer will now create the output dir if needed  

##### Fixes

Fix VersionFixup target, was deleting xml nodes that were not of the type compile, for example resources  
Issue 51 - Include exe project output for unit test execution  
Fix Ask, don’t look for more options than can be displayed  
Fix TextElement xml value for multiroot node fragements  
Alerts UnitTests - Fix missing ${ in unless  
TFS Source Control Block - Add fix for XmlDictionaryReaderQuotas and Notification size  
Fix username and Password issue with CCNet subversion source control block, it was a bad merge job, oops  
Fix largeproperty issue where when xml is true the outerxml is set as the value instead of the innerxml  
Fix message size issue for CCNet TFS source control block  
Fix issue with vdproj files and versioning  
VSTSVersionControl - Oops the or was not working as I thought Needed a ${} around the property




|

|
