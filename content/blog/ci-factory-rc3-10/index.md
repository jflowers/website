---
title: CI Factory RC3 1.0
date: "2008-02-20"
draft: false
categories:
  - "CI Factory News"
  - "CI Factory"
aliases:
  - "/WordPress/?p=201"
  - "/WordPress/index.php?p=201"
params:
  wayback_url: "https://web.archive.org/web/20080805181925/http://jayflowers.com:80/WordPress/?p=201"
  original_url: "http://jayflowers.com:80/WordPress/?p=201"
  archived_from: Wayback Machine

---

## CI Factory RC3 1.0

Announcing the third release candidate for version 1.0 of CI Factory!

|  |  |  |
| --- | --- | --- |
| |  |  | | --- | --- | |  | [**Download CI Factory**](http://ci-factory.googlecode.com/files/CI-Factory-RC3-1.0.0.53.exe "CI-Factory-RC3-1.0.0.53.exe")  [*Version RC3 1.0*](http://ci-factory.googlecode.com/files/CI-Factory-RC3-1.0.0.53.exe "CI-Factory-RC3-1.0.0.53.exe") | |

This release, as you would expect, is mostly fixes and polish.  Before I share with you the most notable changes I would like to ask for your help.  Would you please help us with the CI Factory documentation?  We plan to release the final version 1.0 the first week of February.  There is not much time left and even just an hour or two of your time will make a difference.  To help please [register an account at the CI Factory home page](http://www.cifactory.org/joomla/index.php?option=com_registration&task=register).  I will grant you rights to edit and author pages.  We need help with these pages:

![DocPic](images/2008/01/DocPic.jpg)

- [Getting Started for the Build Master](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=50&Itemid=41)
- [Getting Started for the Developer](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=49&Itemid=41)
- [Wix](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=68&Itemid=41)
- [VSTSVersionControl](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=67&Itemid=41)
- [VS.NETDeploy](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=66&Itemid=41)
- [VS.NETCompile](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=65&Itemid=41)
- [Versioning](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=64&Itemid=41)
- [Simian](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=63&Itemid=41)
- [Perforce](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=62&Itemid=41)
- [NUnit](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=61&Itemid=41)
- [NDepend](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=60&Itemid=41)
- [NCover](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=59&Itemid=41)
- [MSTest](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=58&Itemid=41)
- [MSBuild](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=57&Itemid=41)
- [FxCop](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=56&Itemid=41)
- [What is a Package?](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=55&Itemid=41)
- [DotNetUnitTest](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=54&Itemid=41)
- [Deployment](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=53&Itemid=41)
- [Backup](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=52&Itemid=41)
- [Archive](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=51&Itemid=41)
- [Vault](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=42&Itemid=41)
- [MSBuild](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=41&Itemid=41)
- [Alerts](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=40&Itemid=41)
- [Subversion](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=33&Itemid=41)
- [VisualSourceSafe](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=32&Itemid=41)

Once you are logged in with editor rights you will see ![](http://www.cifactory.org/joomla/images/M_images/edit.png) buttons next to pages you can edit.  You can even add/edit items to/in the [FAQ section](http://www.cifactory.org/joomla/index.php?option=com_content&task=section&id=3&Itemid=32).  The FAQs and the Documentation are now included in the release exe with a nice [index](images/2008/01/Index.htm).

## What’s Changed That’s Notable?

First off CI Factory’s NAnt now supports .NET 3.5.  Next there is a new Package VS.NETDeploy, it was split out of the VS.NETCompile Package.  You should use this package when you are using Visual Studio to create MSIs with deployment projects.  Lastly I was able to get NCover to collect coverage in IIS for tests like WatiN.  There is an new property that you can set in the NCover Package to turn on IIS coverage.

There were some notable fixes too:  The Subversion Package will now recognize \_svn admin folders.  The VSTSVersionControl Package now fully supports automated setup/install of a new CI Factory instance.  Improved intellisense for NAnt, the xsd creation was fixed, all task containers now show the correct intellisense.

As always you can read the [release notes](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=44&Itemid=1) for a complete list of changes.
