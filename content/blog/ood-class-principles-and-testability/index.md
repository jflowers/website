---
title: OOD Class Principles and Testability
date: "2006-10-10"
draft: false
categories:
  - "Unit Testing"
  - "OOP"
aliases:
  - "/WordPress/?p=93"
  - "/WordPress/index.php?p=93"
params:
  wayback_url: "https://web.archive.org/web/20070212150157/http://jayflowers.com:80/WordPress/?p=93"
  original_url: "http://jayflowers.com:80/WordPress/?p=93"
  archived_from: Wayback Machine

---

## OOD Class Principles and Testability

This is the final post in my series on OOD class principles and testability. It has included:

- #### [Single Responsibility Principle and Testability](http://jayflowers.com/WordPress/?p=92)
- #### [The Interface Segregation Principle and Testability](http://jayflowers.com/WordPress/?p=91)
- #### [Dependency Inversion Principle and Testability](http://jayflowers.com/WordPress/?p=86)
- #### [Open Closed Principle and Testability](http://jayflowers.com/WordPress/?p=85)
- #### [Liskov Substitution Principle and Testability](http://jayflowers.com/WordPress/?p=79)
- #### [The Law of Demeter and Testability](http://jayflowers.com/WordPress/?p=78)

There was a pit stop at [YAGNI and Testability](http://jayflowers.com/WordPress/?p=81) as it had some bearing on the OCP. It was all kicked of by [Benefits of Testability](http://jayflowers.com/WordPress/?p=77). Which was inspired by Dr. Stefan Jungmayr’s dissertation [Improving testability of object oriented system](http://www.dissertation.de/FDP/sj929.pdf).

BTW Stefan’s site [http://www.testability.de/](http://www.testability.de/ "http://www.testability.de/") is a great resource ([English Translation](http://translate.google.com/translate?u=http%3A%2F%2Fwww.testability.de%2F&langpair=de%7Cen&hl=en&newwindow=1&ie=UTF-8&oe=UTF-8&prev=%2Flanguage_tools)).

Here is a table that I think quickly summarizes how, when followed, the principles relate to the three aspects of testability.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Observability | Controllability | Understandability |
| Single Responsibility Principle | Yes-less | Yes-less | Yes-less |
| Interface Segregation Principle | Yes-less /w doubles | Yes-less /w doubles | Yes-less /w doubles |
| Dependency Inversion Principle | Yes-less /w doubles | Yes-less /w doubles | Yes-less /w doubles |
| Open Closed Principle | Yes-less /w doubles | Yes-less /w doubles | Yes-less /w doubles |
| Liskov Substitution Principle | No | No | Yes-reuse |
| Law of Demeter | Yes-less | Yes-less | Yes-less |

**Yes-less** = Because the surface area and or type population of the test subject has been reduced, there is less to: observe, control, or understand.

**Yes-less /w doubles** = The benefits of Yes-less are gain only by using test doubles (e.g. mock) and interaction based testing.

**Yes-reuse** = Because test fixtures can be reused to test all subtypes.

After studying the table I noticed two things. It pays to have less to work with in a test. That is to say that when there are very few types and members involved in a test it will be easier to understand. It is easier to observer and control less than more. When you can’t have less it pays to have a test double.

It seems there two general fulcrums that you have to control testability. They are decreasing the surface area and type population or introducing test doubles. As well, they help in increasing the effectiveness of unit tests by eliminating failure points other than the test subject.




|

|
