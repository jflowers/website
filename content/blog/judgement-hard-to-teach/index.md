---
title: Judgement… hard to teach
date: "2006-05-29"
draft: false
categories:
  - "Uncategorized"
  - "Unit Testing"
  - "OOP"
aliases:
  - "/WordPress/?p=58"
  - "/WordPress/index.php?p=58"
params:
  wayback_url: "https://web.archive.org/web/20070206163406/http://jayflowers.com:80/WordPress/?p=58"
  original_url: "http://jayflowers.com:80/WordPress/?p=58"
  archived_from: Wayback Machine

---

## Judgement… hard to teach

ctodx posted a [blog entry](http://community.devexpress.com/blogs/ctodx/archive/2006/05/18/109.aspx) of a discussion on teaching a team about design, specifically interface inheritance over implementation inheritance. I have to comments.

I am sure that judgement can be easy to teach, maybe even in some cases objective not subjective. I think the key here is to bring unit testing into the discussion. If a criteria of good design is testability then things get a bit easier. Well almost, that statement assumes that you value unit testing and are practicing it. Well designed test subjects are much easier to test than poorly designed test subjects. To take the example of [Single Responsibility Principle (SRP)](http://www.objectmentor.com/resources/articles/srp), a test subject with many responsibilities is much harder to test than one with fewer. This is something that the developers with out much design experience or good design judgement can feel. If they are responsible for the testing then they are likely to be more interested in learning how to make things easier to test. Ahh motivation. Now you have instilled motivation and can use that as a fulcrum marinate your team in the design principles.

Interface inheritance is much easier to mock. The point of implementation inheritance is to share code. <sidenote>Every time I have used inheritance to share code I have wished later on that I had used aggregation and composition instead of implementation inheritance.</sidenote> There is no good reason not to always use interface inheritance with implementation inheritance. On your types public members always know a derivative by an interface not an implementation. This way mocking and extending are much easier.




|

|
