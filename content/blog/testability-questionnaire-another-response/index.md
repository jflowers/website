---
title: "Testability Questionnaire: Another Response"
date: "2006-09-26"
draft: false
categories:
  - "Unit Testing"
  - "OOP"
aliases:
  - "/WordPress/?p=87"
  - "/WordPress/index.php?p=87"
params:
  wayback_url: "https://web.archive.org/web/20070307194659/http://jayflowers.com:80/WordPress/?p=87"
  original_url: "http://jayflowers.com:80/WordPress/?p=87"
  archived_from: Wayback Machine

---

## Testability Questionnaire: Another Response

It seems that I misunderstood Kelly Anderson and he wished to be included in the [posting](http://jayflowers.com/WordPress/?p=84). Thanks again for straightening me out Kelly. ![:)](http://jayflowers.com/WordPress/wp-includes/images/smilies/icon_smile.gif) Here is his reply:

How do YAGNI and testability relate?

> If one subscribes to the point of view that the tests fulfill the role  
> of a live specification, YAGNI is a natural outcome. Writing code to  
> some purpose other than passing the test at hand becomes, with practice,  
> a rather irrelevant exercise. Thus, it doesn’t happen as much as when  
> you are not writing to a live spec.  
> >Is testability a first class citizen, or force, in design?  
> Yes. If you can’t test it, you shouldn’t write it. Someone once said,  
> “If you aren’t smart enough to write the test, what makes you think  
> you’re smart enough to write the code.” I thought that was really  
> logical.

What benefits if any do you see in testability beyond making testing easier?

> The primary benefits I see are the natural evolution of decoupled code.  
> On my team, if someone breaks the build, everyone else continues to work  
> on their little piece of the problem without incident. On the team down  
> the hall that doesn’t use TDD or decoupled code, when someone breaks the  
> build (frequently) everyone else suffers. They resolve this issue by  
> only doing a get of fresh code once every few days. When they do finally  
> succumb to the need to do a get, they often spend a long time getting  
> their code to compile again. Multiple checkout and complex merges  
> complicate matters even further. My team checks in every few minutes,  
> and do gets frequently with no ill effect on the portion of the project  
> they are working on.

Do you think that the software development industry has any thing to learn from the hardware industry’s dedication of 3-5% of circuits to testing and testability?

> Maybe. I’m not a huge fan of shipping the tests, but I don’t have a  
> really good reason for my stance on this.

What, if any, design characteristics and forces do you see in opposition with testability? Is the tension beneficial?

> I see emerging technology going in the direction of declarative design.  
> Vista’s UI model, for example is declarative. The current generation of  
> Unit testing frameworks does nothing to give the programmer confidence  
> about his declared components. I see this as a potentially damaging  
> development to the TDD movement.

How does testability effect design?

> Decoupling.

How does design effect testability?

> If the design is spaghetti code, and not already tested, it’s hard to  
> get started doing TDD.

What do you think is the best way to get testability into a product?

> I think it’s best approached as a matter of personal honor. Each  
> programmer has to make a personal commitment to quality. Doing TDD is  
> how I express that commitment.




|

|
