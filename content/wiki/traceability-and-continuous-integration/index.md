---
title: traceability_and_continuous_integration
date: "2005-10-17"
draft: false
categories:
  - "Wiki"
aliases:
  - "/wiki/traceability-and-continuous-integration/"
params:
  wayback_url: "https://web.archive.org/web/20070903201747//wiki/traceability-and-continuous-integration/"
  original_url: "/wiki/traceability-and-continuous-integration/"
  archived_from: Wayback Machine

---

[[[traceability\_and\_continuous\_integration](/wiki/traceability-and-continuous-integration/)]]



Trace: » [traceability\_and\_continuous\_integration](/wiki/traceability-and-continuous-integration/ "traceability_and_continuous_integration")

## Introduction

I am a proponent of CI (Continuous Integration). I have read a great deal of material on Agile. Yet I have never seen anyone folding a ticket tracking system into a CI process. I have seen them spoken to separately. The industry standard CI servers and tools for scripting builds do not integrate with ticket tracking system either. I have found the synergy created when a ticket tracking system is integrated into CI to be invaluable. Normally you hear people expousing the virtues of CI they talk about rapid feedback, quick identification of bugs, reliability..., these are not things this article will discuss. Here I will discuss the value of the record results of the build. The value of traceability it adds to a project. It shows a historic list of changes to the project. Adding the context of why those changes were made to the history dramatically increases its value.

## Overview

It is always nice to start on the same page, I assume we share some common values.

> We would like to manage or be managed in an Agile manner.

Well that’s a very general statement you say?

> We value concise management. Does that help?

Some, but not enough.

> Okay, managment is needed but needs to allow for and be balanced with personal and team ownership.

Better. :)

One of the tricks to concise management is in knowing what to spend time managing, when the path is being strayed from. To know when and what to manage you need to have information or feedback. Luckily Continuous Integration can easily produce voluminous amounts of information. Having loads of information is not always helpful, having the right information is. This begs the question: What information do we need to successfully manage?

1. What tasks/issues/features are to be done?
2. Who is doing the work?
3. When was the work done?
4. What work was done to complete the task/issue/feature?
5. What quality was the work?

The answers to these questions will allow for better management of and by many different aspects and roles of/for a software project. Before we get into how more effective and efficant management can be achieved lets go over how to perform this integration.

## The Process

I always like to view things with a little context, so we will start before the build submission. A Developer is assigned a ticket. When they begin work on this ticket they change the status to \*In Progress\*. When they have completed the work they should update the ticket with a comment explaining the work they performed. Before they check in their source they need to update the status of the ticket from **In Progress** to **Pending Build**. Any tickets that are in a status of **Pending Build** when the build is run will be manipulated by the build script. The scripts can do several things to the ticket(s).

- It can add a comment to ticket listing the source modifications.
- It can add a comment that the ticket was successfully built.
- It can change the assignee and the status of the ticket as well.

Now I have omitted some of the steps in the above description of the process. The following steps will detail the process in full. I will start from the point of the developer has completed the work tasked in a ticket.

1. Add a comment to the ticket detailing the work performed.
2. Check the ticket tracking system query **All Pending Build**.

   1. If there are tickets in the query someone else has claimed the build. The developer must wait until that build is available.
   2. If there are no tickets in the query then the developer may proceed.
3. Flip the status of the ticket to \*Pending Build\*, now the build has been claimed.
4. Check in source (add a comment including the ticket number).
5. Wait for the build result.

   1. If the build result is successful then the developer is done.
   2. If the build result is failing then developer must fix the build.

There was one new item introduced in the steps above: the query **All Pending Build**. This query serves two purposes; allow developers to claim the build, and allow the build script to easily grab all the tickets submitted with the build.

## What Have You Bought?

There are three benefits to integrating the build process and the ticket tracking system. The least important benefit is the ability to claim a build, granted overlapping submissions rarely occur and this will only prevent an overlap if the process is followed. The main benefit is the ability to correlate the build page with a ticket and vise versa. The last benefit is being able to manipulate a ticket from the build script.

Here is a partial screenshot of a build report from a project that correlates tickets (SCRs) with builds.

*[Image: correlation.jpg -- not recovered during site restoration]*

Notice that the check in comments link to the ticket numbers (1596 and 1629). This means that source control, the build page, and the ticket tracking system are all correlated. From any one of them you can track to the others.

This correlation is useful to enable managers to quickly see what is going on in the project. It is easy to see on the build page what work was done, for what ticket, who did the work, and the quality metrics are there as well. When looking at a ticket the build script will have added a comment detailing any information from the build that is deemed necessary.

The build scripts can assume responsibility of moving the ticket to a new status, say **Pending Release**. Now the developer does not have to be responsible for flipping the status of the ticket. A query showing all the tickets \*Pending Release\* eases a manager search for the condition of a release.

## Improving Managment

This information can help better manage a project. Take the role of architect for example. An architect can review the results of a build and quickly identify if the source file modifications listed relate to the ticket submited to the build. If not the architect will know to investage further, posibly in the source control repository with diffs. If the architect expected the addition of new classes and the listing does not include them she can investigate further. If listing is what the architect expected she does not need to investiage further. The build page now holds enough information to inform the architect where to investigate if needed. This information can be used to perform root cause analysis as well. For example a bug is identified in the product. The source control repository is used to identify when the bug was introduced. The ticket associated to the change can be obtained by the check-in comment if the developer included the ticket number or tracing back to the build version through the build labels of the source. With the ticket associated to the offending change you can understand the context of the change that introduced the bug. This can go a long way in root cause analysis. In short order one can find the context in which the developer introduced the bug or failed to fix it.

## Let's Do It!

To adopt this process you would need to:

1. Add the statuses **Pending Build** and **Pending Release** as well as their related queries to your ticket tracking system.
2. Write custom code to allow your build script language to control a ticket in your ticket tracking system.
3. Add to your current build script the necessary section to interact with the ticket tracking system.
4. Update the CI server config to merge the ticket information reported from the build script.
5. CI server report web page to show the ticket information collected.
6. Last follow the process when submitting to the build.

## The Next Step

Something exciting that could be done from here is to take the data recorded for each build and enter it into a database. With a database of build log information numerous metrics of meaning become available. Relating bugs back to a source file is now possible. A report showing what are the top ten offending source files is possible. The possibilities are very interesting indeed.

traceability\_and\_continuous\_integration.txt · Last modified: 2005/10/17 15:35 by jflowers
