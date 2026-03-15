---
title: Single Responsibility Principle and Testability
date: "2006-10-11"
draft: false
categories:
  - "Unit Testing"
  - "OOP"
aliases:
  - "/WordPress/?p=92"
  - "/WordPress/index.php?p=92"
params:
  wayback_url: "https://web.archive.org/web/20070307194708/http://jayflowers.com:80/WordPress/?p=92"
  original_url: "http://jayflowers.com:80/WordPress/?p=92"
  archived_from: Wayback Machine

---

## Single Responsibility Principle and Testability

Straight from the [source](http://www.objectmentor.com/omReports/articles/srp.pdf):

> THERE SHOULD NEVER BE MORE THAN ONE REASON FOR A  
> CLASS TO CHANGE.
>
> What is a Responsibility?  
> In the context of the Single Responsibility Principle (SRP) we define a responsibility to be “a reason for change.” If you can think of more than one motive for changing a class, then that class has more than one responsibility. This is sometimes hard to see. We are accustomed to thinking of responsibility in groups.
>
> The SRP is one of the simplest of the principle, and one of the hardest to get right. Conjoining responsibilities is something that we do naturally. Finding and separating those responsibilities from one another is much of what software design is really about.

SRP has the broadest relationship to testability out of all the OOD principles. It relates to all aspects of testability; Observability, Controllability, Understandability. To test something you must be able to observe or sense that it did what it was supposed to do. To test something you must be able to control or manipulate it. Control is needed at the very least to instigate it to do the thing that you desire to test. In the case of unit tests and some other testing the control will be used to isolate the test subject. To test something you must be able to know: What needs to be controlled and observed. How to control what needs to be controlled. Lastly what the out come should be.

The fewer the responsibilities of the test subject the less that needs to be; observed, controlled, and understood. Chances are the fewer the responsibilities the less surface area the test subject will have. As well the less need to have interactions with other types. This reduces coupling and the type population tied to the test subject. All this effects testability.




|

|
