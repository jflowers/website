---
title: The Law of Demeter and Testability
date: "2006-09-11"
draft: false
categories:
  - "Unit Testing"
  - "OOP"
aliases:
  - "/WordPress/?p=78"
  - "/WordPress/index.php?p=78"
params:
  wayback_url: "https://web.archive.org/web/20100906042048/http://jayflowers.com:80/WordPress/?p=78"
  original_url: "http://jayflowers.com:80/WordPress/?p=78"
  archived_from: Wayback Machine

---

## The Law of Demeter and Testability

The Law of Demeter, also know as the Principle of Least Knowledge, is important to controlling the type population of a test subject. Here is a fun explain from c2.com:

- You can play with yourself.
- You can play with your own toys (but you can’t take them apart),
- You can play with toys that were given to you.
- And you can play with toys you’ve made yourself.

---

Explanation in plain English:

- Your method can call other methods in its class directly
- Your method can call methods on its own fields directly (but not on the fields’ fields)
- When your method takes parameters, your method can call methods on those parameters directly.
- When your method creates local objects, that method can call method on the local objects.

---

The paper [Mock Roles, not Objects](http://www.jmock.org/oopsla2004.pdf#search=%22mock%20roles%20not%20objects%22) contains a good example:

dog.Body.Tail.Wag();

should really be:

dog.ExpressHappiness();

To be clear the example code above would be contained in the test subject. The bad example couples the test subject to DogAnimal, DogBody, and DogTail. Where as the good example couples only to DogAnimal. This smell has always reminded me of a violation of the Single Responsibility Principle. These symptoms indicate a violation of the Law of Demeter:

- To Many Mock Objects
- To Much Mock Setup
- Mock Object Chaining

“Compliance to the Law of Demeter reduces the number of interfaces, the number of stubs and drivers that may be needed, and the number of integration test interfaces.” - [Reviewing Software Artifacts for Testability](http://www.informatik.fernuni-hagen.de/pi3/PDFs/EuroSTAR99.pdf#search=%22Reviewing%20Software%20Artifacts%20for%20Testability%22) by Stefan Jungmayr

Interestingly [Endo-Testing Unit Testing with Mock Objects](http://www.ccs.neu.edu/research/demeter/related-work/extreme-programming/MockObjectsFinal.PDF) by Tim Mackinnon, Steve Freeman and, Philip Craig presents the view that “…code developed with Mock Objects tends to conform to the Law of Demeter, as an emergent property. The unit tests push us towards writing domain code that refers only to local objects and parameters, without an explicit policy to do so.” I am not so sure that use of mocks naturally leads to conformance to the Law of Demeter. Martin Fowler noticed that developers that perform interaction based testing tend to follow the Law of Demeter ([Mocks Aren’t Stubs](http://www.martinfowler.com/articles/mocksArentStubs.html)):

“Interaction-based testers do talk more about avoiding ‘train wrecks’ - method chains of style of `getThis().getThat().getTheOther()`. Avoiding method chains is also known as following the Law of Demeter. While method chains are a smell, the opposite problem of middle men objects bloated with forwarding methods is also a smell. (I’ve always felt I’d be more comfortable with the Law of Demeter if it were called the Suggestion of Demeter.) One of the hardest things for people to understand in OO design is the [“Tell Don’t Ask” principle](http://www.amazon.com/exec/obidos/ASIN/020161622X), which encourages you to tell an object to do something rather than rip data out of an object to do it in client code. Interaction testers say that using interaction testing helps promote this and avoid the getter confetti that pervades too much of code these days.”

[Mock Object Patterns](http://hillside.net/plop/plop2003/Papers/Brown-mock-objects.pdf#search=%22%22Law%20of%20Demeter%22%20testability%22) by Matthew A. Brown and Eli Tapolcsanyi includes the pattern Pass in Mock Collaborator. In the implementation section of the pattern they direct you to use “… the Law of Demeter, design your method calls to permit easy testing” of the test subject.

I think the basic underlining issue with violations of the Law of Demeter is misplaced responsibility. I suspect that this is why it is also called the Principle of Least Knowledge and why it reminds me of the Single Responsibility Principle. Part of correctly assigning responsibility is dependency management an testability is very sensitive to dependency issues.

Side Note:

Some people get concerned about interaction based testing coupling the unit test to the implementation of the test subject. It can if a test double is used in place of an object that the test subject uses as a helper (i.e. the interaction of the test subject with the helper is not a responsibility of the test subject). In general you should only ever use test doubles where it is the responsibility of the test subject to perform the interaction. Please notice I said responsibility of the test subject and not the system. A test subject plays a role in a system and that role has responsibilities which include interaction, maybe even entirely comprised of, with other objects in the system. When you refactor a class, or test subject, in a system it is still responsible for interacting with the same objects it did before the refactoring. When you change its interactions, or move the responsibility to an other class, you are refactoring the system. When refactoring the system unit tests should break. When refactoring a class unit tests should not break.




|

|
