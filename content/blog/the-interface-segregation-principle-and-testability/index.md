---
title: The Interface Segregation Principle and Testability
date: "2006-10-11"
draft: false
categories:
  - "OOP"
  - "Unit Testing"
aliases:
  - "/WordPress/?p=91"
  - "/WordPress/index.php?p=91"
params:
  wayback_url: "https://web.archive.org/web/20120114190506/http://jayflowers.com:80/WordPress/?p=91"
  original_url: "http://jayflowers.com:80/WordPress/?p=91"
  archived_from: Wayback Machine

---

## The Interface Segregation Principle and Testability

So c2.com does not maintain a good page on ISP. I will lean on [David Hayden](http://davidhayden.com/blog/dave/archive/2005/06/15/1482.aspx) to round up a quick explanation of ISP:

> The Interface-Segregation Principle focuses on the cohesiveness of interfaces with respect to the clients that use them. Here are some other descriptions I found while Googling:
>
> - “Many client specific interfaces are better than one general purpose interface“- “The dependency of one class to another one should depend on the smallest possible interface“- “Make fine grained interfaces that are client specific.“- “Clients should not be forced to depend upon interfaces that they don’t use. This principle deals with the disadvantages of fat interfaces. Fat interfaces are not cohesive. In other words the interfaces of classes should be broken into groups of member functions.“

One of the first things that comes to my mind when exploring how ISP effects testability is surface area. ISP is aimed at reducing how much a client is exposed to, and a test is a client. Reducing surface area can have the affect of reducing the type population as well. This is only really helpful in the context of test doubles (e.g. mock). Using the class behind the slim interface in the test can increase the type population possibly negating all benefit to testability. This constructor to the backing class or it’s implementation can negate the benefit.
