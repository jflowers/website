---
title: Breaking with old ways
date: "2006-12-03"
draft: false
categories:
  - "Unit Testing"
  - "Testability"
aliases:
  - "/WordPress/?p=99"
  - "/WordPress/index.php?p=99"
params:
  wayback_url: "https://web.archive.org/web/20070212182733/http://jayflowers.com:80/WordPress/?p=99"
  original_url: "http://jayflowers.com:80/WordPress/?p=99"
  archived_from: Wayback Machine

---

## Breaking with old ways

I read Eli’s posts [Firing Events Made Easy](http://www.elilopian.com/2006/11/19/firing-events-made-easy/) and [How To Isolate Future Instances](http://www.elilopian.com/2006/11/19/how-to-isolate-future-instances/) last week and it hit me that this was ground breaking.  The capability that he demonstrates in these posts open doors that were previously shut without refactoring.  That is to say that your tightly coupled winform can now be programmatically tested with in frameworks like Fit and xUnit.  This has got to be the sharpest mocking tool available for .NET.

You maybe a little confused at this point.  My pals at work were when I excitedly explained this break through to them.  They thought that I did not like TypeMock.NET.  I clarified for them that TypeMock is an extremely sharp tool.  I like what Jeremy D. Miller says about sharp tools in his [Programming Manifesto](http://codebetter.com/blogs/jeremy.miller/archive/2006/10/30/My-Programming-Manifesto.aspx):

> My point being that just like a sharp knife or power tools, “sharp tool” techniques are safe when combined with some proper precautions (TDD).  Of course I’ve got a little scar on my bicep from shooting myself with a pneumatic nail gun, so what do I know about safety?

I think that I am also inline with [Ron Jeffries](http://tech.groups.yahoo.com/group/testdrivendevelopment/message/18844) view:

> I’m told that in the olden days, when one was working to become a  
> machinist, the first project you were given a chunk of metal and a  
> file and told to make two pieces, one with a square hole in it, the  
> other with a square peg coming out of it, that fit perfectly  
> together. Later, you got to play with the machines.

I explained to my buddies that it is not the wisest thing to do: hand out sharp tools and not educate people on how to use them.

Getting a laceration aside the only real argument that I could see against it is:  The effort one would put into controlling TypeMock could be better spent on refactoring the test subject into a more naturally testable subject.  A code generator to produce the blocks of code to control TypeMock integrated into the IDE you could easily defeat this concern.  I talked to Eli about this and he said “We have plans to create a GUI pack and a Recorder pack…”.

It seems to me that tool side of things are shaping up very well.  Take MbUnit, FitNesse, TypeMock.NET, ReSharper and CodeRush.  This toolset will let you do some amazing things if you take the time to learn.   It is nice not to need so much courage.
