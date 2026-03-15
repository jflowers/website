---
title: Shifting the Focus
date: "2008-01-22"
draft: false
categories:
  - "Unit Testing"
aliases:
  - "/WordPress/?p=206"
  - "/WordPress/index.php?p=206"
params:
  wayback_url: "https://web.archive.org/web/20090223194138/http://jayflowers.com:80/WordPress/?p=206"
  original_url: "http://jayflowers.com:80/WordPress/?p=206"
  archived_from: Wayback Machine

---

## Shifting the Focus

Last week I was having fun pair programming and TDD’n.  This was my first time pairing with my new friend so we naturally had to work through our differences.  One in particular was about a difference in unit testing and doubling (mocking) has stuck me with through the weekend.  My partner wanted to test and double protected members.  I was concerned that this was testing implementation and would bite us in the butt later by increasing the level of effort to refactor.  Another member of the team has no experience with test doubles beyond home grown simple stubs.  Working to explain the situations in which you would and would not want to use mocks, stubs, spys, etc has stuck with me too.  Particularly the distinction between state based testing and interaction based testing.

I see TDD as a design activity and not a testing activity.  I find it unfortunate that the word test is in TDD.  So saying state based **testing** and interaction based **testing** is not helping the situation.  I am going to start saying state based design and interaction based design.

When I was [unguing](http://www.secretgeek.net/ungument.asp) that writing a test for a protected member was testing implementation I really wanted to say something like this is no longer a design activity.  Instead I resorted to calling on Gerard’s [Preface](http://xunitpatterns.com/Preface.html) to provide a better vision of the woes of unit testing.  At the time we were working on design, we were working oh the interaction between some of our classes.  Later when we where working with the interaction between one of our classes and an external class I felt something shift and could not put a name to it.  I have it now, the shift was from internal interactions and design to external interactions and implementation.  We ended up using mocks in both cases testing design for internal interactions and implementation for external interactions.  The external interaction we were mocking was simplistic, [this is not always the case](http://www.mockobjects.com/2007/04/test-smell-everything-is-mocked.html).  If the interaction had not been so simplistic we would have gone straight to integration tests.  To be clear we wrote integration tests as well.  I was attracted to the mocked unit tests for their speed of execution and reliability over the slow execution times and external service dependencies of the integration tests.  Not to mention how this would play an even bigger role if we start using a [pipeline build](http://www.testearly.com/2007/09/17/consequences-of-pipeline-structure/).  I want the most feedback I can get in a 5 minute build and mocked external dependencies gave it to me, this time.

I wonder if TypeMock can play a role in improving this situation.  To be clear mocking the external dependency will not normally drive the implementation.  In essence I have duplicated effort in testing the external interaction, once with mocks and once with the real thing.  It seems to me that with the technologies that TypeMock is using you could write an integration test, specify the types or namespaces to record, execute the integration test while recording, and save off the record for playback.  With the playback you could then run those same integration tests in mocked mode, everything that you had specified to be recorded now being mocked.  You would have the benefit of in memory, fast running, tests and full integration tests with only a little extra effort.




|

|
