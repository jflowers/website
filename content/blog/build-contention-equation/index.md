---
title: Build Contention Equation
date: "2006-07-12"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=65"
  - "/WordPress/index.php?p=65"
params:
  wayback_url: "https://web.archive.org/web/20070307194637/http://jayflowers.com:80/WordPress/?p=65"
  original_url: "http://jayflowers.com:80/WordPress/?p=65"
  archived_from: Wayback Machine

---

## Build Contention Equation

We are exploring new ways to build our software at work.  I was trying to convey a thought on validating the feasibility of a build process today with the following equation.

**Number of Change Packages** = 8 Hours \* 60 Minutes / (**Build Time** + **Preparation Time** + **Buffer**)

Filling out the right side of the equation will show how many change packages can be process by the build on an average day.  The **Build Time** is how long it take the build to complete.  The **Preparation Time** is how long it takes a developer to get the build started.  This could represent claiming the build token, submitting to source control and waiting for the build process to begin.  In the proposed build process only one developer could submit at a time; the build is triggered by a submission to source control.  The **Buffer** is the tricky variable.  The buffer deals with contention or rather is a means to reduce contention.  It is desirable for developers to be able to submit to the build when they complete a task.  It is not desirable for them to have to wait to submit.  The buffer is the amount of time that will create a situation where when a developer goes to claim the build token chances are it is available.  Let me repeat that, chances are it is available.  I do not know how much this variable should be.  I just see that it is a fulcrum, a way to control, reduce the contention for the build.  It will not eliminate it will just reduce the chances of it occurring.  Lets say we make the Buffer 15 minutes.  This will yield a build that can process on average 20 change packages in 8 hours with a 65% chance that the build will be available when a developer goes to submit.

20 Change Packages = 8 Hours \* 60 Minutes/ (5 Minute Build Time + 3 Minute Preparation Time + 15 Minute Buffer)

65% Chance Availability = 15 Minute Buffer / (5 Minute Build Time + 3 Minute Preparation Time + 15 Minute Buffer)

So if you have 10 developers they can submit twice a day.  Does this fit your needs?  No?  Well can you live with a lower chance of availability risking that developers will start working in larger change packages?  If so then lets try reducing the buffer to provide a 50% chance of availability .  That will yield an average of 30 change packages in 8 hours for 2.5 submissions per developer for a 10 developer team.

So what is a team of 10 developers to do if there are no acceptable set of values to this equation?  The only solution that I can fathom out is to split the build into multiple builds (e.g. a build for the client and a build for the server).  Dividing the build should occur along two axis, package dependencies and number of contributing developers.  For example there is not much benefit to splitting the the server off into its own build if only 10% of the team works on it.
