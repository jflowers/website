---
title: CI Factory Beta 0.9.0.52
date: "2007-10-01"
draft: false
categories:
  - "CI Factory News"
  - "CI Factory"
aliases:
  - "/WordPress/?p=190"
  - "/WordPress/index.php?p=190"
params:
  wayback_url: "https://web.archive.org/web/20071028164212/http://jayflowers.com:80/WordPress/?p=190"
  original_url: "http://jayflowers.com:80/WordPress/?p=190"
  archived_from: Wayback Machine

---

## CI Factory Beta 0.9.0.52

This is the second release of the 0.9 series, build 52.  You can read the release notes here *[Link removed: content not recovered during site restoration]* and [download from here](http://ci-factory.googlecode.com/files/CI-Factory-Beta-0.9.0.52.rar).

This release includes and update for NCover 2.0.1!  Note the NCover package only supports 2.0.1.  There are two new force filters: Host and Password.  The host force filter will let you specify host names of clients that can force a build.  The password filter lets you specify a password that must be supplied to force a build.  The CI Factory live build server uses a password filter, see [here](http://cifactorybuild.stelligent.com/CI%20Factory/default.aspx?_action_ViewFarmReport=true).  Thanks to Nicolás Maldonado for a patch to use the program files env var instead of hard coding "C:\Program Files".

Most notable and easily apparent are the changes to web dashboard.  This release shows a significant start on a face lift. Thanks to [Scott Dorman](http://geekswithblogs.net/sdorman/Default.aspx) for some of these improvements.

![CropperCapture[1]](images/2007/09/CropperCapture%5B1%5D.png)

![CropperCapture[3]](images/2007/09/CropperCapture%5B3%5D.png)
