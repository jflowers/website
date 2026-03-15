---
title: "Is Open Source More Agile Than Commercial Software?"
date: "2008-01-21"
draft: false
categories:
  - "Tools"
  - "ALT.Net"
aliases:
  - "/WordPress/?p=205"
  - "/WordPress/index.php?p=205"
params:
  wayback_url: "https://web.archive.org/web/20090223194131/http://jayflowers.com:80/WordPress/?p=205"
  original_url: "http://jayflowers.com:80/WordPress/?p=205"
  archived_from: Wayback Machine

---

## Is Open Source More Agile Than Commercial Software?

In general I think open source is better at enabling you to behave Agile then commercial software.  Lets start from the point when you realize that you have a need that is not being fulfilled.  I want to explore this in two slightly different directions.  First imagine that we have not finished defining our tool set and second imagine that we already have a tool set to integrate into.

Source control is something we all have had to deal with so I think it will serve us well here.  So we are at the beginning of a project and need to choose a source control system.  If you already have a source control system supported by your IT dept then you probably don’t even think this is something that deserves thought.  Think for a moment about how this tool will enable you or hinder you in your practice of Agile over the course of the project.  For example does it play nice with pair programing? Will it force you into some strange behavior just so that you can practice pair programming?  Will it support your simple work flow: update, commit, update, commit…?  Let’s pick on StarTeam for a moment.  To my knowledge StarTeam is a hindrance for both the examples.  It is not conducive to pair programming, it prefers to support one user per machine.  This pushes you to log into a machine as some anonymous user.  You end up creating a user per pair workstation.  I quickly imagine 6 months from now trying to understand why something is the way it is in the software we are developing and reading the commit/checkin comments for some clue.  In a normal world I would see that Billy had been working on this and go ask him.  Now all I know is that someone on pair station 2 was working on this the afternoon of Sept 16th.  Bummer!  As well StarTeam has no update or get latest functionality in the UI.  It has 3 categories of changes and at best you can update each category by selecting all changes in that category and selecting the appropriate action from the context menu.  Mind you it is not the same context menu item for all categories!  The point here is that this tool needlessly is requiring more of your brain power for you to get your job done.  Subversion for example, as the open source alternative, has none of these issues.  It is conducive to pair programming and supports "please just freaking update my sh\*t!".  Just in case, the latter is about KISS and StarTeam is in no way the embodiment of KISS.  We could pick on any number of other commercial source control systems and find that they too fail to naturally support pair programming, in most cases you must operate in a contrived manner.  To be fair there are some that don’t suffer from this affliction.

Lets move on to imagining that we are looking for a tool to meet a need and we already have an established tool suite.  As well lets continue to contrast StarTeam and Subversion.  There are many more tools that extend, enhance, and integrate with Subversion than StarTeam, both open source and commercial.  Even the open source tools that do surround StarTeam provide minimal integration as compared with those surrounding Subversion.  Take Cruise Control .Net (CCNet) for example, it is the only source control plugin to CCNet that does not support labeling, or tagging, on successful builds.  The original Cruise Control (CC), Java, requires that you build CC from scratch to gain support for the plugins (this is no small feat).  Both CCNet and CC provide first class integration to Subversion out of the box.

In either case once you have decided on a tool moving forward with open source is as simple as download and go where as commercial usually means some song and dance with you procurement dept.

Continuing to live with the product can be a very different experience between commercial and open source.  The release cycle in the open source world is far more frequent than in the commercial.

Some tools already have a large Agile user base and are a driving force in the evolution of that tool.  Subversion for example has a large Agile user base effecting the Subversion ecosystem.  I imagine if there was a larger Agile user base for StarTeam CC’s and CCNet’s support of StarTeam would be in a much better state.  When you take into account both the affect a large Agile user base has and more frequent releases of open source I am sure that you see how an open source project will respond much quicker to the needs of the Agile community than a commercial project on a slower release cycle.  Let me heap on a little more: in many cases the developers on these open source project are Agile practitioners themselves where as many of the Commercial tool vendors are not practicing Agile.




|

|
