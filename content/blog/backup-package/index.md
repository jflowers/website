---
title: Backup Package
date: "2006-12-29"
draft: false
categories:
  - "Continuous Integration"
  - "CI Factory News"
  - "CI Factory"
aliases:
  - "/WordPress/?p=111"
  - "/WordPress/index.php?p=111"
params:
  wayback_url: "https://web.archive.org/web/20070307194752/http://jayflowers.com:80/WordPress/?p=111"
  original_url: "http://jayflowers.com:80/WordPress/?p=111"
  archived_from: Wayback Machine

---

## Backup Package

Well I am finally getting around to publishing the Backup Package that I have been using on my current day job project.  Back in September we had a build server die on us.  It was not difficult to get a replacement up and running though we did lose the history of the build project.  That is to say that the CCNet build logs and state file were lost.  I was able to rebuild the state file by hand but the log files were just plain lost.  I created this simple Backup Package to keep us out of this kind of trouble in the future.  One of the main reasons that I remembered to sit down and release this Package was that same projects build server died again this week and this time recovery was complete.  Anyway I have uploaded the [Package zip](http://code.google.com/p/ci-factory/downloads/detail?name=Backup-Package.zip&can=2&q=) to the Google Project Hosting service and created [documentation](http://groups-beta.google.com/group/CI-Factory/web/backup-package?hl=en) for it as well.

Enjoy!

P.S. Hidden in there is the [Post Build extension](http://groups-beta.google.com/group/CI-Factory/web/Post%20Build?hl=en).
