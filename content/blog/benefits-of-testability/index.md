---
title: Benefits of Testability
date: "2006-09-18"
draft: false
categories:
  - "Unit Testing"
  - "OOP"
aliases:
  - "/WordPress/?p=77"
  - "/WordPress/index.php?p=77"
params:
  wayback_url: "https://web.archive.org/web/20100628072844/http://jayflowers.com:80/WordPress/?p=77"
  original_url: "http://jayflowers.com:80/WordPress/?p=77"
  archived_from: Wayback Machine

---

## Benefits of Testability

I have been having a hard sell of “testability is a good thing” at my work. I feel that unit testing leads to testability leads to good OO. The dynamic mocking application TypeMock.NET has not helped: nor has the article [Stop Designing for Testability](http://www.codeproject.com/useritems/StopDesign4Tests.asp). TypeMock is a powerful application but I think that it can be misused to allow poor design with ease of unit testing. The pain that unit testing creates when dealing with a low testability test subject is experienced close to when the test subject was created. This gives the developer rapid feedback that there is a design issue. The feedback is experience while the developer is still in flow and can make the needed changes with the lest impact to schedule. So unit testing and testability are like an alarm indicating early that there is a design problem. This sounds like a good thing to me, something that I would not want to circumvent or avoid. There are a lot of other characteristics of design that are related to testability. In particular the list below are benefits to testability.

- Understandability
- Modifiability
- Availability
- Flexibility
- Maintainability
- Reliability
- Usability
- Changeability
- Fault Tolerance

This list was gathered from Appendix D of Stefan Jungmayr’s thesis [**Improving testability of object-oriented systems**](http://www.google.com/url?sa=t&ct=res&cd=6&url=http%3A%2F%2Fwww.dissertation.de%2FFDP%2Fsj929.pdf&ei=yvz6RP6LG8rUwgG56bzOCw&sig=__GUdqOEqs-Ksp47vYIYfqzwvAx5Y=&sig2=ZyGYX67tAhwW5EfO1kSlvQ#search=%22stefan%20testability%20metric%22).


```batch
If some or all of the list is important to your project then testability will help you get it.
```
