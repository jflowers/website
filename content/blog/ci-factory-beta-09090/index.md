---
title: CI Factory Beta 0.9.0.90
date: "2007-10-24"
draft: false
categories:
  - "CI Factory News"
  - "CI Factory"
aliases:
  - "/WordPress/?p=197"
  - "/WordPress/index.php?p=197"
params:
  wayback_url: "https://web.archive.org/web/20071028164217/http://jayflowers.com:80/WordPress/?p=197"
  original_url: "http://jayflowers.com:80/WordPress/?p=197"
  archived_from: Wayback Machine

---

## CI Factory Beta 0.9.0.90

This is the third release of the 0.9 series, build 90.  You can read the [release notes here](http://www.cifactory.org/joomla/index.php?option=com_content&task=view&id=44&Itemid=1) and [download from here](http://ci-factory.googlecode.com/files/CI-Factory-Beta-0.9.0.90.exe).

There is a new source control Package: Perforce!

There are more improvements to the dashboard, for examples see the screen shots below.

Also the ground work for automated branching has been laid.  The changes to enable this are small and important.  The ccnet project names now include the branch name, so by default a new CI Factory project named CoolBeans would have a ccnet project name of CoolBeans-Current.  The virtual directory structure in IIS has change as well.  The root dir name format is <projectname-codelinename> and the Artifacts dir has moved under the root dir.  These two simple changes will enable automated branching, so look for a create branch script in the next week or so.

There is another new Package named Workspace.  This Package defines the workspace needed to develop and build the product.  It has targets that check for required software, assist in installing missing software, and configure your system.  This Package also gets wrapped up in an Sfx archive and offered through a link on the web dashboard.  This setup exe can be downloaded by anyone and executed to help them get a development environment setup.  All that is needed to execute the setup exe is the .Net framework, other wise it is self contained.  In future version of CI Factory the Package will be called from the Personal.Build.xml and Main.Build.xml scripts to unsure that your personal env and the build server env is up to date.

The cctray zip file has been replaced with a Sfx archive.  This setup exe will install cctray and includes a settings file preconfigured to the server that you downloaded from.  In future versions the installer will merge settings if it finds and existing settings file.

CI Factory itself is now distributed in a Sfx.  I like Sfxs a lot.

There are more changes but that is what the release notes are for.

![CropperCapture[6]](images/2007/10/CropperCapture%5B6%5D.png)

![CropperCapture[24]1](images/2007/10/CropperCapture%5B24%5D11.png)
