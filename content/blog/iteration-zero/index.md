---
title: Iteration Zero
date: "2008-01-20"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=204"
  - "/WordPress/index.php?p=204"
params:
  wayback_url: "https://web.archive.org/web/20090223193723/http://jayflowers.com:80/WordPress/?p=204"
  original_url: "http://jayflowers.com:80/WordPress/?p=204"
  archived_from: Wayback Machine

---

## Iteration Zero

I just started on a new contract using Java!  I have mixed feeling about working on a Java project.  I have little experience with the language, yet I am not concerned about it, it is very similar to C#.  I am concerned about my fulfillment on this project.  I am hoping that exposure to new ideas, tools, and ways to tackling problems will provide fulfillment.

We just finished iteration zero, setting up the project infrastructure.  It has been nothing but frustration so far.  I have been surprised by the lack of opinion in the tools that we have tried; maybe another way of putting it is guidance.  Eclipse for example has no opinion about anything as compared to Visual Studio.  It looks like I have gotten spoiled by CI Factory as well.  We tried Hudson and Cruise Control and neither even got close to a working setup.  First we tried Hudson.  It is too simple in my opinion.  It was a great experience when everytihg worked, and frustrating when things were not working.  At some point we decided to proceed with Cruise Control.  I have the pleasure of working with StarTeam on this project, and that has complicated the environment.  Cruise Control had issues with integrating StarTeam into the fold. Thanks to Borland’s license we had to compile Cruise Control ourselves.  We finally got Cruise Control to load the StarTeam plugins only to find that the Cruise Control dashboard refused to work when Cruise Control was run as a windows service.  On and on it went until we I noticed that we were approaching 150% of our time allotment for setting up a CI Server.  We had to get a CI Server up and running and quick.  There was no end in sight on the current path, continuing would be neurotic.  I made the command decision to switch to Cruise Control .Net.  We had it all hooked up including Maven and JUnit reporting in about an hour.  That included messing with the Maven bat file to report failed builds (you need to remove the /B from the exit command).

For sure I am more familiar with CCNet than CC and I still think that CCNet is a more mature product.  CCNet is implemented in a much simpler fashion than CC.  It provides much more info about what is happening as well.  Don’t think everything just worked the first try with CCNet.  That is not to say that most of it did work out of the box.  We had some issues with StarTeam and Maven and all were solved quickly as a result of the quality of logging information in the server and build logs for CCNet.

So far my experience with the tools surrounding Java as compared those surrounding .Net is that of disappointment.  Many of the tools in the .Net arena came from Java, and I thought to find more mature, better implementations, that would be easier to use.  I miss Visual Studio 200\*, Subversion, MbUnit, TestDriven.Net, NCover, TypeMock, NAnt, CI Factory, TortoiseSvn, and VisualSvn.
