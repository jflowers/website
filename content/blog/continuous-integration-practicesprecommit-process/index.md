---
title: Continuous Integration Practices–Precommit Process
date: "2012-03-12"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=232"
  - "/WordPress/index.php?p=232"
params:
  wayback_url: "https://web.archive.org/web/20120510071755/http://jayflowers.com:80/WordPress/?p=232"
  original_url: "http://jayflowers.com:80/WordPress/?p=232"
  archived_from: Wayback Machine

---

## Continuous Integration Practices–Precommit Process

Often what gets all the attention in Continuous Integration is what happens on a continuous integration server.  There is more to CI than what happens on the server.  What happens on a developer workspace is part of CI as well.  An easy example of this is the precommit process.  It describes what a developer does before committing changes to source control.

![](images/2012/03/clipboard.jpg "clipboard.jpg")

On a simple and small project this would entail:

1. Update to the latest source
2. Recompile (a clean compile)
3. Run all the tests (may require a local deployment)

The larger and more complex the project gets the less tenable this procedure becomes.  When you end up with thousands of unit tests, thousands of integration tests, and hundreds of user acceptance tests, functional tests, etc… it becomes unreasonable to run all of them every time before you commit.  To run all these tests would take a long time.  So how long is acceptable you say?  You need to decide that for yourself.  The project I am working on as I write this has decided that the whole precommit process should take about 30 minutes.  That doesn’t mean that we throw away tests until we can complete the process in the allotted time.  We need to take educated guesses as to which tests we should run, which tests are most relevant to the changes that are being tested.  For example if I was making changes to how the system processes orders there would be no value in running tests on product comparison.

In the book “Software Configuration Management Patterns: Effective Teamwork, Practical Integration” the pattern Private Build System is basically the same thing:

> #### Context
>
> A Private Workspace allows you, as a developer, to insulate yourself from external changes to your environment. But your changes need to work with the rest of the system too. To verify this, you need to build the system consistently, including building with your changes. This pattern explains how you can check whether your code will still be consistent with the latest published code base when you submit your changes.
>
> #### Problem
>
> How do you verify that your changes do not break the build or the system before you check them in?
>
> #### Solution
>
> Before making a submission to source control, build the system using a Private System Build similar to the nightly build.

This patlet raises the why of it: **why do we need a precommit process?**  And just like it says to make sure that we do not break the codeline (i.e. trunk or a branch).

**Why don’t we want to break the codeline(build)?** So that we don’t negatively affect the rest of the team.

**How would breaking the codeline(build) negatively affect the rest of the team?**  In two ways; first it would prevent anyone else from committing to the build as we follow the rule of not committing on top of a broken build, two if anyone updates from source control their local build will be broken too.

**Why is blocking the build a bad thing?**  It is not so bad if you fix the build quickly.  It really only becomes a bad thing when it is broken for an extended period of time.  This prevents others from committing to the build and so they continue to work, increasing the size of their changeset.  Large change sets are more likely to break the build, and when they do break the build they usually take a long time to fix.  This can easily lead to a situation where the build is often broken for extended periods of time.

**Why is having the build broken for extended periods of time or all the time a bad thing?**  The build then looses it usefulness.  It is clearly no longer keeping the codeline stable, which is its purpose.

Those 5 whys get us to the root of it.  We need a precommit process to support a centralized build process.  They also paint a picture that many feel is a slippery slope, causing great fear of breaking the build.  The danger is in how long you let any given broken build remain broken.  As long as you fix the build quickly, or rollback the offending changes to last good build quickly there is no danger.

## Fear of Broken Builds

Fear of breaking the build has caused some people to adopt measures to keep the build green at all costs.  There are several commercial CI Servers that play into this fear with features that provide precommit isolated private builds.  These are builds that occur outside of the developer’s workspace, they are private in the sense that the results are only shown to the developer who submitted the changes and the changes don’t make there way into source control unless the build passes.  Another common measure is to insist that all tests are run as a part of the precommit process.  Both of these have the side effect of increasing the average size of a changeset committed to the build.  Granted that these large changesets will pass the build…they will not necessarily be easy to integration into each developer’s workspace.  The larger the changeset the greater the chance it will impact changes in a developer’s workspace, especially if the local changes are large as well.  Gradual changes over time are easier to integration into a developer’s workspace than big bang changes.  A significant compounding factor with big bang changes is that they tend to be committed at the end of an iteration.  This means you would likely have multiple developers competing to commit large changesets at the end of an iteration.  When the competition gets rough developers often rationalize breaking the build in favor of being able to commit their changes hoping to differ testing to the next iteration. We finished the story, except for the testing, we’ll test it next iteration.

![](images/2012/03/iStock_000007510607XSmall.jpg "three gear")  

## Working in Small Changes

If the team works by decomposing stories into small tasks, tasks that can be completed in less than a day, preferably a couple of hours, things can work very smoothly.  Imagine that every hour or two the developers are committing changes as they complete tasks.  Their precommit process would involve integration of a small number of changes from a source control update and executing a small number of tests to exercise their changes.  I am sure you can see how this would result in a short precommit process with little chance that the updates from source control would impact local changes.




|

|
