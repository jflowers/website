---
title: "CI Factory, Where are you?"
date: "2009-08-03"
draft: false
categories:
  - "CI Factory News"
  - "CI Factory"
aliases:
  - "/WordPress/?p=210"
  - "/WordPress/index.php?p=210"
params:
  wayback_url: "https://web.archive.org/web/20090831002728/http://jayflowers.com:80/WordPress/?p=210"
  original_url: "http://jayflowers.com:80/WordPress/?p=210"
  archived_from: Wayback Machine

---

## CI Factory, Where are you?

CI Factory and I have been stuck in the Java world for over a year now.  I have not had much reason to keep up with the Dot Net packages.  I ![iStock_000000778473XSmall](images/2009/08/iStock_000000778473XSmall.jpg "iStock_000000778473XSmall")know there are new versions of most of the Dot Net tools CI Factory offers packages for.  I have let this keep me from releasing a new version of CI Factory.  There have been many new features in the core of CI Factory and several new packages around Java tools.  I will not sacrifice my personal life to maintain all of CI Factory.  As well I see no good reason for delaying a release of a new version of CI Factory for out-of-date Dot Net packages.  I welcome anyone’s help in updating the Dot Net packages.

That said I hope to finish a release version of 1.2 in August.

Here are some of the features in the new version:

Core

- Default CCNet projects are now Build Scripts, Dev, Heavy, Release, Deploy, and Test.
- Improved directory structure, cleaner, more intuitive.
- Ground work for 64 bit support.
- Improved property names.
- Better support for environment variables.

CCNet

- Real time log messages on the dashboard.
- Improved how CCNet kills a process tree when a timeout occurs.
- Improved dashboard layout.
- Add WCF REST interface to CCNet server.
- Added sounds to CCTray installer.

NAnt

- Added task deleteregistry.
- Added task macrodef (credit to [Eoin Curran](http://peelmeagrape.net/)).
- Improved xsd intellisense to include properties, target names, functions, and more.
- Added task propertystructure and property structure iterator for loopthrough task.
- Added task stringadd to add values to a string list.
- Added task stringsplit to convert a delaminated string into a string list.
- Added process functions: get-current-pid, get-parent-pid, and get-command-line.
- Improved code to allow overriding a target and calling a target by full name: full name format = [project name]::[target name].
- Added task loadpackages to load CI Factory packages, packages are now a baked in part of NAnt.
- Improved saveproperties task to accept property structure iterators.
- Added package functions: find-name-by-type.
- Added TargetProcess tasks.
- Added property functions: destroy and value.
- Added scriptfile functions: exists, loaded, get-file-Path, get-directory-Path, get-name, get-current-name, get-current-file-path, and get-current-directory.

Packages

- Added TargetProcess Package, mine commit/checkin log message/comment for TargetProcess Story/Task/Bug id to display title and description on summary build report.
- Upgrade to new version of Subversion 1.6.
- Improved Ant package, includes Ant scripts for Compile, Coverage Instrumentation with Corbertura, JUnit, and Packaging.
- Added FitNesse Package.
- Added Selenium Package.
- Added JUnit Package.
- Added Corbertura Package.
- Added JUnit Integration Test Package.
- Added Personal Tracking Package.
- Added Eclipse Package.
- Added support for VS 2008.
- Analytics: general improvements plus new graphs and measures for FitNesse, individual developers, Code Coverage.



Comments Closed
