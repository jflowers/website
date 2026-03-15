---
title: CI Factory RC4 1.0
date: "2008-01-17"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=202"
  - "/WordPress/index.php?p=202"
params:
  wayback_url: "https://web.archive.org/web/20090223193716/http://jayflowers.com:80/WordPress/?p=202"
  original_url: "http://jayflowers.com:80/WordPress/?p=202"
  archived_from: Wayback Machine

---

## CI Factory RC4 1.0

Announcing the forth release candidate for version 1.0 of CI Factory!

|  |  |  |
| --- | --- | --- |
| |  |  | | --- | --- | |  | [**Download CI Factory**](http://ci-factory.googlecode.com/files/CI-Factory-RC4-1.0.0.70.exe "CI-Factory-RC4-1.0.0.70.exe")  [*Version RC4 1.0*](http://ci-factory.googlecode.com/files/CI-Factory-RC4-1.0.0.70.exe "CI-Factory-RC4-1.0.0.70.exe") | |

The list is getting pretty short, here it is in total:

##### New/Improvements

Added After and ReplaceOuter modes to XmlPokeTask.   
Install XmlDiff for Simian Alert.   
Added kludge to Arguments.xml Post.Install to correct order of operations in Main.Build.xml.   
Make 2005 default VS for VS.NETDeploy   
Add Collapsible warnings   
Add license files

##### Fixes

Fix: correct NCover version to 2.0.3.0.   
Fix: SetupIIS.xml fails when virtual dirs already exist.   
Fix: MSBuild and DotNetUnit show report for Personal.Build.xml.   
Fix: correct install generation output for SetUp and TearDown target calls in Main.Build.xml.   
Fix: Switch all instances of hard coding installed files with Program Files to use of env var, these had been set as env var only in the install script.   
Fix: DotNetUnitTest check file report exists before copy   
Fix: Delete CCNet Remote dll   
Fix: preserve CCNet user emails   
Fix: Simian Alert, only install if the Simian Package is set to install.   
Fix: Give web apps an opportunity to end sessions and what not while coverage is still on.   
Fix: VS.NETDeploy ref’n a property before it was set.   
Fix: Simian Alert img paths and conditional show of removed blocks.   
Fix: Simian Alert compare counts, use int::parse to compare.   
Fix: Try to preserve email users for ccnet project config. This works for the default config.   
Fix: Aggregator remoting
