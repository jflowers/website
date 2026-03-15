---
title: Iteration One
date: "2008-01-26"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=207"
  - "/WordPress/index.php?p=207"
params:
  wayback_url: "https://web.archive.org/web/20090221100634/http://jayflowers.com:80/WordPress/?p=207"
  original_url: "http://jayflowers.com:80/WordPress/?p=207"
  archived_from: Wayback Machine

---

## Iteration One

We just finished iteration one!  We are doing 1 week iterations just in case you can’t count. ![;-)](http://jayflowers.com/WordPress/wp-includes/images/smilies/icon_wink.gif)

We really over committed on the first iteration, we forgot about the holiday.  Oops.  None of the stories were fully completed, and there was business value to show.  It’s a new team and we are still getting used to what we can get done in a week.  I am more than a little concerned about how we have utilized our tool stack.  My pair was lucky enough not to encounter any hindrance from how we were using the tools, though we were not using JBoss or Selenium for our story; this iteration we will.  It is going to be a pain in the butt jumping out of the IDE to manage JBoss, Selenium, and Maven.  Selenium RC needs to be running if you are going to run Selenium tests in the IDE and turned off if running them from Maven.  JBoss dies a painful death after several deployments, so we will have to keep and eye on this.  Hey, did the tests fail because we broke something or did JBoss die again?  Also we have what I expect to be just a bandaid on a build script issue where integration tests start to run before deployment to JBoss has completed, the bandaid being a sleep command in the Maven pom.xml.

I seem to have nothing good to say.  I was really hoping to report something that we liked better than the .Net world.  I even consulted with the team before writing this post.  So far it is hands down .Net and my team mates have no knowledge of things like LINQ, VS 2008, ASP.Net MVC, and most of the 3.5 technologies.

It looks like I will get some good exposure to Java Server Faces and EJB 3.0 next week.  Maybe that will bring about something cool…
