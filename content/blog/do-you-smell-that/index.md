---
title: "Do You Smell That?"
date: "2006-11-24"
draft: false
categories:
  - "Unit Testing"
  - "OOP"
aliases:
  - "/WordPress/?p=89"
  - "/WordPress/index.php?p=89"
params:
  wayback_url: "https://web.archive.org/web/20070212182557/http://jayflowers.com:80/WordPress/?p=89"
  original_url: "http://jayflowers.com:80/WordPress/?p=89"
  archived_from: Wayback Machine

---

## Do You Smell That?

So there has been this enormous discussion on the Yahoo TDD Group about testability: it was kicked off by [Marcus](http://mawi.org/BenefitsOfTDDObviousHiddenOrJustByproducts.aspx).  I used this dialogue as an opportunity to explorer something my gut has been bothering me about.

My gut has been trying to warn me that TDD, as I understand it, provides inadequate direction, or maybe support is a better word, to newbies as far as testability is concerned.  Why is testability of concern when things are clearly testable?  It is TDD that we are talking about after all.  Well read the [Test Automation Manifesto](http://www.clrstream.com/index.php?option=com_docman&task=docclick&Itemid=68&bid=6&limitstart=0&limit=5) (TAM) first then finish reading this post.  You might also find the [preface](http://xunitpatterns.com/Preface.html) to xUnit Patterns relevant as well.  In my experience I have seen adoptions of TDD fail because the of the same things that Gerard is talking about in TAM and xUnit Patterns.  Gerard focuses on the test code, the fixtures and supporting class that test the product code.  This is where my gut comes in.  The test code is half the problem.  The test subjects, the product code, is the other half of the problem.  If a test subject is hard to test this will increase the effort to create and maintain the tests that exercise the test subject.  Such a test subject is testable, it has low testability.  This extra effort can jeopardize the success of the project and may precipitate the business need to drop the practice of TDD.  The chances of this happening are greatest on projects where the TDD is new to the team.  There are several things that can be done to reduce the risk of this happening for such a team.  I think an experienced coach is probably the best way to reduce the risk.  Unfortunately this is not an option for many teams.  If possible the team should add or exchange for experienced TDD developers and pair with them.  This new blood will need to play the role of a leader.  When these things aren’t possible what is a team to do?  Hope and pray?  I hope not.

The shared pool of knowledge that was create by the dialogue on the TDD group really helped me to find my way through the issue that my gut was pushing me to address.  The ah-ha moment for me was triggered by Joe Rainsberger.

> It might be worthwhile to introduce code smells first, then show how TDD   
> exposes code smells by making tests hard to write. Sprinkle the   
> necessary refactoring as you go. Up front, all I think I’d need to know   
> is “some designs suck in specific ways; TDD amplifies the suckiness; the   
> good news is that we have a bunch of recipes for removing specific kinds   
> of suckiness… we’ll learn ‘em as we go.”

As I read back through the thread I see that Keith Ray probably set up the ah-ha moment.  
> I’m on day three of writing a book on Code Smells, Refactoring, and  
> Design Principles. I want to link Code Smells, which are easy to  
> identify, to violations in Design Principles, which (it seems) are too  
> abstract for most people to really see in code (or see violated in  
> code).

I think that a possible solution, at the very least an improvement in the situation, is to provide newbies with a catalog of testability smells and refactorings.

*As I sit here writing this I wish I had brought home my copy of Design Patterns. ![:-(](http://jayflowers.com/WordPress/wp-includes/images/smilies/icon_sad.gif)* 

I have been asked several times if and how this catalog would differ from the existing catalog at [www.refactoring.com](http://www.refactoring.com).  I have not been able to verbalize an answer to that question yet.  In researching the matter I did notice that Joshua Kerievsky discovered 5 new smells when focusing on design patterns ([Refactoring to Patterns](http://www.amazon.com/Refactoring-Patterns-Addison-Wesley-Signature-Kerievsky/dp/0321213351)).  It seems to me that because motive will be focused to testability that there might be new smells discovered and existing smells might need to be tweaked to better relate back to testability.

[![](images/2006/10/WindowsLiveWriter/DoYouSmellThat_B2C1/SimpleUML_thumb1.png)](http://jayflowers.com/WordPress/wp-content/uploads/2006/10/WindowsLiveWriter/DoYouSmellThat_B2C1/SimpleUML3.png)

I think a small example would help to illustrate.  In this example our test subject class will be named MSMQChannel.  It inherits from an abstract class Channel.  The Template Method Pattern is at play in this example.  The class Channel performs all sorts of work specific to the host application.  In this example the MSMQChannel is expected to provide the ability to put messages in a queue.  It has a reference to the type MessageQueue.

*Timeout: I know right now that there are going to be testability issues.  What ever types the test subject has to work with the test will have to work with (in most cases).  So the reference to MessageQueue is going to be an issue.  I also know that MessageQueue works in an asynchronous way and this will cause complexity in tests.  There even more subtle issues at play in this design but lets stick to the obvious for now.*

This example is not contrived.  I have taken it from a project that I worked on a few years ago.  It is something that I wrote shortly after first reading about unit tests and TDD.  I was trying my best to create a well factored OO design.  I was trying hard to get those unit tests in place.  I thought that I did a good job and I was proud of the work I did.  Of course now I look at the code and sigh.  


```xml
<Test()> \_
```

Public Sub SendUnWrapped()

Me.Channel.SendMessage(Me.MsgSentWrapped)

Me.WaitForMsg()

Me.CheckExceptions()

    Assert.IsTrue( \_

Me.MsgRecievedUnWrapped.CompareTo( \_

DirectCast( \_

Me.MsgSentWrapped.Envelop.Body.Content, \_

String) \_

        ) = 0, \_

“Did not get the right message”)

End Sub

*Sorry for the VB.NET.  Like I said this is not a contrived example.*

Looking at this now I think I went to great lengths to make the test look simple, to cover up the complexity.  The test subject is in the property Channel.  It is created and prepared for execution in the test setup, adding to the look of simplicity of this test SendUnWrapped.  The very first line of the test is execution of the test subject method.  The next line is a call to a test helper method that will block until the message sent is retrieved, remember that SendMessage is asynchronous.  The next call is to another helper method.  The test subject is not allowed to throw exceptions, it can publish them to a log.  So the call to CheckExceptions is to retrieve all exceptions published to the log during the test and if some are found to fail the test.  The last call is to assert that the message received is the message that was sent.

Not counting the test fixture itself there are three other classes (384 lines) it depends on for getting things set up, torn down, and helper classes.  The test fixture itself had just 4 test methods out of 18 total methods; 338 lines.  As well each of the tests in the fixture took over 2 seconds to execute.

It seems I was working very hard to hide the complexity.

So when I look at this now I know that the first thing that should be done is to insert a seam between MSMQChannel and MessageQueue.  I would do this by writing a wrapper around the MessageQueue class and extracting an interface from the wrapper.  MSMQChannel would then expose a property typed as IWrappedMessageQueue.  The properties getter could have lazy creation of WrappedMessageQueue.  The test fixture would call the setter passing a test double (e.g. mock).  This would allow the test to occur synchronously dramatically simplifying the test.  Moving to a synchronous mode eliminates one whole class and 1 method; 60+ lines of code.  This test double will also eliminate the need for the test fixture to manage the queue being used for the test, another 4 methods and 55+ lines.  So all told the addition of a means to inject a test double would reduce the infrastructure for this test significantly.  There are plenty more things that can be done to improve this situation but lets spend sometime looking at what just happened.

Lets try and identify a smell or two.  We know what a root cause is; tight coupling.  Many symptoms or smells can trace back to one root cause.  Gerard puts it well in xUnit Patterns:

> A smell is a symptom of a problem. A smell doesn’t necessarily tell us what is wrong because there may be several possible causes for a particular smell. Most of the smells in this book have several different named causes; some causes even appear under several smells. That’s because a root cause may reveal itself via several different symptoms (or smells.)

So what grabs you by the nose and leads to tight coupling?  I don’t know yet.  Maybe looking at motivations will help.  I was motivated to perform this refactoring because:

- State Based Testing was too expensive time wise (the test took 2+ seconds to execute).- State Based Testing was more complex than Interaction Based Testing would be.- The use of a test double would make the nature of the test subject synchronous.

Now we are getting somewhere.  I think we can pull these smells out:

- [Slow Tests](http://xunitpatterns.com/Slow%20Tests.html)- Lengthy SetUp- Lengthy TearDown- [Asynchronous Test](http://xunitpatterns.com/Slow%20Tests.html#Asynchronous%20Test)- Party Crasher

 Two of those smells have already been identified by Gerard and are documented in xUnit Patterns.  The Lengthy SetUp, Lengthy TearDown, and Party Crasher smells are new to my knowledge (please correct me if I am wrong).

---

  

### Smell: Lengthy SetUp/TearDown

#### Symptoms

A large amount of code (i.e. classes, methods, or simply lines of code) is needed to setup and or tear down a test.

#### Impact

Tests may take a long time to execute.  They may also take considerable maintenance resources.  As there is more to know understandability is decreased.

#### Causes

There are a number of reasons that setup and tear down can be lengthy operations.

##### Cause: [Highly Coupled Code](http://xunitpatterns.com/Hard%20to%20Test%20Code.html#Highly%20Coupled%20Code)

**Note:** Gerard has recorded this cause.  I will not repeat his documentation here.

---

  

### Smell: Party Crasher

#### Symptoms

A third party component is heavily used by the test fixture.

#### Impact

Tests may take a long time to execute.  The test subject can not be executed in isolation causing reduced localization of errors.  Depending on the purpose of the third party component the test may be coupled to external resources like a data base or email server.

#### Causes

I am only aware of one cause.

##### Cause: [Highly Coupled Code](http://xunitpatterns.com/Hard%20to%20Test%20Code.html#Highly%20Coupled%20Code)

**Note:** Gerard has recorded this cause.  I will not repeat his documentation here.

---

This is just a sketch and it has clearly demonstrated that more testability smells exist and more work can be done to flesh out this catalog.

I am glad to have found that Gerard’s book xUnit Patterns has more to do with testability than I first thought.  He has a smell [Hard to Test Code](http://xunitpatterns.com/Hard%20to%20Test%20Code.html) in which he says “This is a big enough topic that it warrants a whole chapter of its own”.  Though I have not been able to locate the chapter.

Gerard does not formally link the Causes to refactorings.  I would have like to seen that.  In this case the refactoring needed was Wrap Class(from Working Effectively with Legacy Code).

**It seems that I can smell that and it has grabbed me by the nose!**
