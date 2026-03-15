---
title: CI Factory RC1 1.0
date: "2007-12-06"
draft: false
categories:
  - "Continuous Integration"
  - "CI Factory News"
  - "CI Factory"
  - "Tools"
aliases:
  - "/WordPress/?p=200"
  - "/WordPress/index.php?p=200"
params:
  wayback_url: "https://web.archive.org/web/20071207183210/http://jayflowers.com:80/WordPress/?p=200"
  original_url: "http://jayflowers.com:80/WordPress/?p=200"
  archived_from: Wayback Machine

---

## CI Factory RC1 1.0

That’s right! You read correctly, it says 1.0. This is the first release candidate for version 1.0. There are no features left to add in this release. There is some cleanup, such as documentation updates. I expect the final version to be released sometime early next year.

|  |  |  |
| --- | --- | --- |
| |  |  | | --- | --- | |  | [**Download CI Factory**](http://ci-factory.googlecode.com/files/CI-Factory-RC1-1.0.0.2.exe "CI-Factory-RC1-1.0.0.2.exe")  [*Version RC1 1.0*](http://ci-factory.googlecode.com/files/CI-Factory-RC1-1.0.0.2.exe "CI-Factory-RC1-1.0.0.2.exe") | |

So let’s look at what’s changed since the last version, 0.8. In my opinion the major changes are: the web dashboard has had a facelift, a Perforce, FxCop, Archive, Workspace, and NUnit Package have been added, and automated branch creation. There are numerous other changes.

### New Web Dashboard

Here is an animated gif of the project grid showing a build in progress (sorry about the stuttering):

![ProjectGrid](images/2007/12/CropperCapture%5B5%5D.gif)

You now know much more about a build in progress. I love the elapsed time counter and the auto refresh. You can also see if your changes are in the current build.

![Build Report](images/2007/12/CropperCapture%5B10%5D.jpg)

The build report is significantly different as well. The section headers in the main report are hyperlinks to the corollary detail report page. You can get a feel for the new dashboard at the [live build dashboard for CI Factory](http://cifactorybuild.stelligent.com/CI%20Factory-Current/default.aspx?_action_ViewFarmReport=true).

### Automated Branch Creation

There is a new NAnt script in the build folder: CreateBranch.xml. Run this script when you wish to create a branch. It will ask you some questions like what do you want to call the new branch, maybe 1.0, and what version to you want the parent branch to be, maybe 1.1. It will create a new code line directory tree as a sibling to the parent branch (probably Current or trunk). Something like this:

![Branch](images/2007/12/CropperCapture%5B11%5D.jpg)

It is possible to supply the answers to the script as input parameters so the script can be run silently. The script produces a ready to go branch and edits the parent branch so that it is ready to go as well. This is branch creation made easy!

### Packages

#### Perforce

Simply a package that supports the use of Perforce as your source control repository.

#### FxCop

The [FxCop](http://www.gotdotnet.com/Team/FxCop/) Package was donated by [Steve Bohlen](http://unhandledexceptions.spaces.live.com/). Steve has a nice blog post on it [here](http://unhandledexceptions.spaces.live.com/blog/cns%21FC56A7CB585DF52F%21247.entry).

#### Archive

This Package copies off artifact folders to a network share maintaining a date window of artifact folders on the build server. This helps to keep the build server from running out of space. There is a companion Alert script that will email you when the space on the build server drops below a configurable point. This way you can be proactive as apposed to reactive.

#### Workspace

This Package’s purpose is to make creating and managing Workspaces easy. With it you can codify your Workspace using existing scripts and adding your own. It will bundle these scripts into a setup exe that is downloadable from the web dashboard. This makes it exceedingly easy for a new developer to get up and running. The scripts are also run as a part of the personal build scripts. So you can use them to keep your workspace up to date.

#### NUnit

Simply a Package to execute NUnit tests.

### Assorted Improvements

#### NAnt

Add stdin attribute to exec based tasks, it’s value will be fed to standard input.

Added NAnt function to replace a hint path for a binary ref.

Allow includes in nant to occure anywhere, look out for new and fun errors.

Add file::get-product-version nant function.

Change TryCatchTask to catch type Exception and not just BuildException

Added task to delete tfs subscriptions

Added nant function to get date of last ccnet build

Added ccnet nant function to get a list of build file names

Added CCNet NAnt function to get latest build file name

Added FreeText Mode to Ask task

Added Add mode to XmlPoke task, named existing functionality replace mode

Improved xpath eval of xmlpeek, now includes eval of functions like count()

Added OuterXml property to xmlpeek

Asyncexec/WaitForExit - Remove TaskNames from list after having waited on them

Asyncexec/WaitForExit - Check to see if the Task exists before waiting on it

#### Personal Build

Pass many args to NAnt from batch files, Build.bat and NoUpdateBuild.bat

Added CSS style sheet to personal build output.

#### Dashboard

Add icon to header

Change Dashboard title to be more informative

Add build time info to project grid

Improve FxCop, NDepend, Simian, Modifications, and Deployment reports

Added links from summary report sections to detailed reports

switch MbUnit package to new reporting style

switch NCover to new reporting style

Added mods and forcee to project grid

Add images for Deployment, File, SourceControl, CI Factory icon, and more

Collapsible modifications in dashboard

Better colors for errors and warning sections

Improved Header

Source Control and Deployment File Icons

Add better images for web dashboard

Add Status Images Improve layout

add confirm prompt to force build button

Consolidate Build state and activity into Availability

Add logos for Simian, NDepend, and MSBuild

#### Core CI Factory

Add NAnt.xsd to build project, attempting to have the xsd automatically picked up by the IDE for intellisense.

Add Force Filters to ccnet project file.

Add Personal.Build folder to build solution.

Make use of the DTD Entities instead of hard coded paths in all xml config files and xsl files.

Promote the Unit Test and Install directories to Properties.build.xml

Allow initial version to be set in the install.

Add script CreateBranch.xml to the build directory, supports basic creation of branches.

Move common variables to a new file Entities.xml

Move personal build stuff from Power Tools to full install.

Add Creation of Sfx installer for CCTray.

Added condition where when the build log files are on the same host as the dashboard the build logs are retrieved directly from the hard drive.

SetupIIS.xml - Set to Classic ASP.Net for Vista.

Performance improvements to CCNet core

CCNet Server Aggregator - Implement more of the interface, allowing the aggregator to service dashboards

CCNet mod writer will now create the output dir if needed

#### Packages

Upgrade NDepend to 2.5.0.1382

Upgrade Simian to 2.2.21

Upgrade NUnit to 2.4.5

VS.NETCompile: Add set of working dir exec of DevEnv, fixes some post build script issues that use relative paths

Added FxCop Package, donated by Steve Bohlen.

Add check for Subversion to Subversion Package, if not installed will download and install it.

Added Archive Package

Added Diskspace Alert script

Improvement on the Vault Package from Stephen Bohlen: a new property called ${Vault.Repository.BasePath} that points to the folder path in the repository that the CIFactory installer will use as the ‘root’ pathing of the project when its added to VAULT. The SourceControl.Targets.xml has been modified to use this setting to construct the needed pathing in the VAULT repository and to then set the working folder in the repos to this folder for the solution.

Added Perforce Package

Created a Workspace Package to define, create, and maintain workspaces, this includes a setup exe as a download from the dashboard.

Add trigger manipulation to VSTS package

Added NUnit Package and Tests

Add interactive option to get in Subversion Package, uses Tortoise

Added control over svn install location, no need to have in the path any more
