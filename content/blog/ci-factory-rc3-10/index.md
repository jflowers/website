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

This release, as you would expect, is mostly fixes and polish.  Before I share with you the most notable changes I would like to ask for your help.  Would you please help us with the CI Factory documentation?  We plan to release the final version 1.0 the first week of February.  There is not much time left and even just an hour or two of your time will make a difference.  To help please register an account at the CI Factory home page *[Link removed: content not recovered during site restoration]*.  I will grant you rights to edit and author pages.  We need help with these pages:

![DocPic](images/2008/01/DocPic.jpg)

- Getting Started for the Build Master *[Link removed: content not recovered during site restoration]*
- Getting Started for the Developer *[Link removed: content not recovered during site restoration]*
- Wix *[Link removed: content not recovered during site restoration]*
- VSTSVersionControl *[Link removed: content not recovered during site restoration]*
- VS.NETDeploy *[Link removed: content not recovered during site restoration]*
- VS.NETCompile *[Link removed: content not recovered during site restoration]*
- Versioning *[Link removed: content not recovered during site restoration]*
- Simian *[Link removed: content not recovered during site restoration]*
- Perforce *[Link removed: content not recovered during site restoration]*
- NUnit *[Link removed: content not recovered during site restoration]*
- NDepend *[Link removed: content not recovered during site restoration]*
- NCover *[Link removed: content not recovered during site restoration]*
- MSTest *[Link removed: content not recovered during site restoration]*
- MSBuild *[Link removed: content not recovered during site restoration]*
- FxCop *[Link removed: content not recovered during site restoration]*
- What is a Package? *[Link removed: content not recovered during site restoration]*
- DotNetUnitTest *[Link removed: content not recovered during site restoration]*
- Deployment *[Link removed: content not recovered during site restoration]*
- Backup *[Link removed: content not recovered during site restoration]*
- Archive *[Link removed: content not recovered during site restoration]*
- Vault *[Link removed: content not recovered during site restoration]*
- MSBuild *[Link removed: content not recovered during site restoration]*
- Alerts *[Link removed: content not recovered during site restoration]*
- Subversion *[Link removed: content not recovered during site restoration]*
- VisualSourceSafe *[Link removed: content not recovered during site restoration]*

Once you are logged in with editor rights you will see *[Image: image -- not recovered during site restoration]* buttons next to pages you can edit.  You can even add/edit items to/in the FAQ section *[Link removed: content not recovered during site restoration]*.  The FAQs and the Documentation are now included in the release exe with a nice [index](images/2008/01/Index.htm).

## What’s Changed That’s Notable?

First off CI Factory’s NAnt now supports .NET 3.5.  Next there is a new Package VS.NETDeploy, it was split out of the VS.NETCompile Package.  You should use this package when you are using Visual Studio to create MSIs with deployment projects.  Lastly I was able to get NCover to collect coverage in IIS for tests like WatiN.  There is an new property that you can set in the NCover Package to turn on IIS coverage.

There were some notable fixes too:  The Subversion Package will now recognize \_svn admin folders.  The VSTSVersionControl Package now fully supports automated setup/install of a new CI Factory instance.  Improved intellisense for NAnt, the xsd creation was fixed, all task containers now show the correct intellisense.

As always you can read the release notes *[Link removed: content not recovered during site restoration]* for a complete list of changes.
