---
title: "State Based UnitTesting, or Not?"
date: "2005-10-01"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=39"
  - "/WordPress/index.php?p=39"
params:
  wayback_url: "https://web.archive.org/web/20070307194825/http://jayflowers.com:80/WordPress/?p=39"
  original_url: "http://jayflowers.com:80/WordPress/?p=39"
  archived_from: Wayback Machine

---

## State Based UnitTesting, or Not?

I have been doing a lot of research lately on how to teach unit testing.  There seem to be to basic forms: State and Interaction.  In my last post I define what a unit test is in a very strict way.  By that definition I can not see how state based testing is unit testing.  I wanted to refer to my own examples here but gotdotnet user samples take 72 hours or so to be published so I will refer to Martin Fowler’s [Mocks Aren’t Stubs](http://www.martinfowler.com/articles/mocksArentStubs.html).  At the beginning of this article he illustrates the two approaches.  For state based testing to be performed a portion of the system, more than the test subject, was needed.  It was needed for the test subject simply to be used.  Sniff Sniff Sniff.  Do you smell that.  Smells like tight coupling to me.  Bugs in the warehouse class can easily cause the order unit test to fail.  This fail to express much of the potential value of a unit test.  Indicating were the problem is.  Now we can only know that when a unit test fails that it’s a problem in either the order or warehouse classes.  So why would I write a separate unit test for the warehouse class, I don’t really even feel like adding asserts to the order test to verify that the warehouse object is in the expected state.  All this leads me to believe that state based testing is not a unit testing style at all.  It promotes bad practices.  This is not to say that it isn’t a great style for other forms of testing, just unit testing.  Interaction testing on the other hand is dependent on loose coupling; same as the definition in the previous post depends on it.




|

|
