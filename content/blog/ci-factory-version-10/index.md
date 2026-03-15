---
title: CI Factory Version 1.0
date: "2008-02-12"
draft: false
categories:
  - "Continuous Integration"
  - "CI Factory News"
  - "CI Factory"
  - "Tools"
aliases:
  - "/WordPress/?p=208"
  - "/WordPress/index.php?p=208"
params:
  wayback_url: "https://web.archive.org/web/20080219020905/http://jayflowers.com:80/WordPress/?p=208"
  original_url: "http://jayflowers.com:80/WordPress/?p=208"
  archived_from: Wayback Machine

---

## CI Factory Version 1.0

Well it has been a long time coming, version 1.0 is here ([release notes](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=44&Itemid=1)).

|  |  |  |
| --- | --- | --- |
| |  |  | | --- | --- | |  | [**Download CI Factory**](http://ci-factory.googlecode.com/files/CI-Factory-1.0.0.76.exe "CI-Factory-1.0.0.76.exe")  [*Version 1.0*](http://ci-factory.googlecode.com/files/CI-Factory-1.0.0.76.exe "CI-Factory-1.0.0.76.exe") | |

I am very happy with the improvements made in this release and feel confident in it’s quality and stability.  I think that CI Factory is pushing into an new frontier, I don’t see other products trying to solve some of the problems that CI Factory addresses: for instance automated branching.  Another good example is the developer workspace installer.  If I had to label this new frontier I would call it workspace management.  I look forward to fortifying CI Factory with capabilities in this new frontier.  I can’t imagine having been able to write these features if CI Factory did not have such [strong opinions](http://gettingreal.37signals.com/ch04_Make_Opinionated_Software.php).

In 5 months there were 271 builds that went into this major release with 9 intermediate releases (one silent):

- ### [CI Factory Beta 0.9.0.14](http://jayflowers.com/WordPress/?p=186)

There is already a significant amount of change in this early release.  First off there is a NUnit Package now!  I am sure that a lot of people are saying about time.  There have been several performance improvements to CCNet, in particular the web dashboard.  One of the improvements that will make my life a lot easier in the NAnt scripting department is with xmlpeek.  I have improved the eval capabilities of the xpath expressions.  It should now work for any xpath expression, so things like sum(@testsrun) will work.  Lastly there have been some new CCNet NAnt functions added, allowing you to do things like write NAnt scripts to help testers get a test env setup for a build of their choosing.

- ### [CI Factory Beta 0.9.0.52](http://jayflowers.com/WordPress/?p=190)

This release includes and update for NCover 2.0.1!  Note the NCover package only supports 2.0.1.  There are two new force filters: Host and Password.  The host force filter will let you specify host names of clients that can force a build.  The password filter lets you specify a password that must be supplied to force a build.  The CI Factory live build server uses a password filter, see [here](http://cifactorybuild.stelligent.com/CI%20Factory/default.aspx?_action_ViewFarmReport=true).  Thanks to Nicolás Maldonado for a patch to use the program files env var instead of hard coding "C:\Program Files".

Most notable and easily apparent are the changes to web dashboard.  This release shows a significant start on a face lift. Thanks to [Scott Dorman](http://geekswithblogs.net/sdorman/Default.aspx) for some of these improvements.

- ### [CI Factory Beta 0.9.0.90](http://jayflowers.com/WordPress/?p=197)

There is a new source control Package: Perforce!

There are more improvements to the dashboard, for examples see the screen shots in the [release announcement](http://jayflowers.com/WordPress/?p=197).

Also the ground work for automated branching has been laid.  The changes to enable this are small and important.  The ccnet project names now include the branch name, so by default a new CI Factory project named CoolBeans would have a ccnet project name of CoolBeans-Current.  The virtual directory structure in IIS has change as well.  The root dir name format is <projectname-codelinename> and the Artifacts dir has moved under the root dir.  These two simple changes will enable automated branching, so look for a create branch script in the next week or so.

There is another new Package named Workspace.  This Package defines the workspace needed to develop and build the product.  It has targets that check for required software, assist in installing missing software, and configure your system.  This Package also gets wrapped up in an Sfx archive and offered through a link on the web dashboard.  This setup exe can be downloaded by anyone and executed to help them get a development environment setup.  All that is needed to execute the setup exe is the .Net framework, other wise it is self contained.  In future version of CI Factory the Package will be called from the Personal.Build.xml and Main.Build.xml scripts to unsure that your personal env and the build server env is up to date.

The cctray zip file has been replaced with a Sfx archive.  This setup exe will install cctray and includes a settings file preconfigured to the server that you downloaded from.  In future versions the installer will merge settings if it finds and existing settings file.

CI Factory itself is now distributed in a Sfx.

- ### [CI Factory Beta 0.9.0.111](http://jayflowers.com/WordPress/?p=198)

Archive Package and Diskspace Alert script to help manage the space on your build server.  It’s always a bummer when the build breaks because the build server ran out of hard drive space.

An upgrade script, this may be the most important part of this release.  That’s right!  There is now a script to help you upgrade to a new version of CI Factory.  It doesn’t do it all yet but it does a lot of the work for you.  Please find the new file upgrade.bat in the CI Factory root folder, next to run.bat.  Simply execute this, there is no need to configure anything first.  Well if you have changed ProjectsDirectory to something other than c:\Projects then you need to adjust that property in …\CI Factory\Install Scripts\Upgrade.xml.  The script will walk you trough the upgrade asking questions and doing the work.

Stephen Bohlen contributed a patch to the Vault package that allows for shared repositores.

There were a bunch of lower level improvements as well, so of the more notable ones:

Added labelPrefix to the Perforce source control block for CCNet.

Moved all common variables to a dtd file Entities.xml.

- ### [CI Factory Beta 0.9.0.159](http://jayflowers.com/WordPress/?p=199)

Added [FxCop](http://www.gotdotnet.com/Team/FxCop/) Package, donated by [Steve Bohlen](http://unhandledexceptions.spaces.live.com/).  Steve has a nice blog post on it [here](http://unhandledexceptions.spaces.live.com/blog/cns%21FC56A7CB585DF52F%21247.entry).  Thanks Steve!

Added links from summary report sections to detailed reports for many Packages.

Allow initial version to be set in the Arguments.xml at install time.

Add the creation of a branching script: CreateBranch.xml.  It is located in the build directory.  Currently Subversion is the only Package that supports the necessary targets.  I am still working on Perforce, it has proven a little tricky.

- ### [CI Factory RC1 1.0](http://jayflowers.com/WordPress/?p=200)

So let’s look at what’s changed since the last version, 0.8. In my opinion the major changes are: the web dashboard has had a facelift, a Perforce, FxCop, Archive, Workspace, and NUnit Package have been added, and automated branch creation. There are numerous other changes.

##### New Web Dashboard

Here is an animated gif of the project grid showing a build in progress (sorry about the stuttering):

![ProjectGrid](images/2007/12/CropperCapture%5B5%5D.gif)

You now know much more about a build in progress. I love the elapsed time counter and the auto refresh. You can also see if your changes are in the current build.

![Build Report](images/2007/12/CropperCapture%5B10%5D.jpg)

The build report is significantly different as well. The section headers in the main report are hyperlinks to the corollary detail report page. You can get a feel for the new dashboard at the [live build dashboard for CI Factory](http://cifactorybuild.stelligent.com/CI%20Factory-Current/default.aspx?_action_ViewFarmReport=true).

##### Automated Branch Creation

There is a new NAnt script in the build folder: CreateBranch.xml. Run this script when you wish to create a branch. It will ask you some questions like what do you want to call the new branch, maybe 1.0, and what version to you want the parent branch to be, maybe 1.1. It will create a new code line directory tree as a sibling to the parent branch (probably Current or trunk). Something like this:

![Branch](images/2007/12/CropperCapture%5B11%5D.jpg)

It is possible to supply the answers to the script as input parameters so the script can be run silently. The script produces a ready to go branch and edits the parent branch so that it is ready to go as well. This is branch creation made easy!

##### Packages

###### Perforce

Simply a package that supports the use of Perforce as your source control repository.

###### FxCop

The [FxCop](http://www.gotdotnet.com/Team/FxCop/) Package was donated by [Steve Bohlen](http://unhandledexceptions.spaces.live.com/). Steve has a nice blog post on it [here](http://unhandledexceptions.spaces.live.com/blog/cns%21FC56A7CB585DF52F%21247.entry).

###### Archive

This Package copies off artifact folders to a network share maintaining a date window of artifact folders on the build server. This helps to keep the build server from running out of space. There is a companion Alert script that will email you when the space on the build server drops below a configurable point. This way you can be proactive as apposed to reactive.

###### Workspace

This Package’s purpose is to make creating and managing Workspaces easy. With it you can codify your Workspace using existing scripts and adding your own. It will bundle these scripts into a setup exe that is downloadable from the web dashboard. This makes it exceedingly easy for a new developer to get up and running. The scripts are also run as a part of the personal build scripts. So you can use them to keep your workspace up to date.

###### NUnit

Simply a Package to execute NUnit tests.

- ### [CI Factory RC3 1.0](http://jayflowers.com/WordPress/?p=201)

CI Factory’s NAnt now supports .NET 3.5.  Next there is a new Package VS.NETDeploy, it was split out of the VS.NETCompile Package.  You should use this package when you are using Visual Studio to create MSIs with deployment projects.  Lastly I was able to get NCover to collect coverage in IIS for tests like WatiN.  There is an new property that you can set in the NCover Package to turn on IIS coverage.

There were some notable fixes too:  The Subversion Package will now recognize \_svn admin folders.  The VSTSVersionControl Package now fully supports automated setup/install of a new CI Factory instance.  Improved intellisense for NAnt, the xsd creation was fixed, all task containers now show the correct intellisense.

- ### [CI Factory RC4 1.0](http://jayflowers.com/WordPress/?p=202)

### 

Various small fixes and improvements.




|

|
