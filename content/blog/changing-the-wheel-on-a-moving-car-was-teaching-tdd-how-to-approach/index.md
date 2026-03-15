---
title: "Changing the wheel on a moving car: Was Teaching TDD: How to approach?"
date: "2006-06-29"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=63"
  - "/WordPress/index.php?p=63"
params:
  wayback_url: "https://web.archive.org/web/20060830165011/http://jayflowers.com:80/WordPress/?p=63"
  original_url: "http://jayflowers.com:80/WordPress/?p=63"
  archived_from: Wayback Machine

---

## Changing the wheel on a moving car: Was Teaching TDD: How to approach?

I had started a thread on the TDD user group about how to teach TDD.  It grew and grew and I got a lot of good feed back.  I emailed [Jeremy Miller](http://codebetter.com/blogs/jeremy.miller/default.aspx) asking for him to weigh in on the issues and he responded on his blog with: [So How do You Introduce TDD into an Organization or Team?](http://codebetter.com/blogs/jeremy.miller/archive/2006/06/27/146899.aspx)  Which gained a bunch of comments.

To try and keep the blog sphere in the loop with the TDD user group discussion here is where I have ended up.

So in my original [post](http://groups.yahoo.com/group/testdrivendevelopment/message/17385?threaded=1&var=1) I mentioned a bunch of forces that would have  
to be resolved in teaching TDD (e.g. lack of OO skills).  There are  
other forces that should be mentioned: schedule, schedule, and  
schedule.  They were given to me in the order of priority.  This is a  
maintenance project (there are plenty of new features as well).  There  
is little OOish design and a lot of complexity.  Areas of the  
application were owned top to bottom by individuals, though anyone can  
mess with anything.  This has recently changed to team based  
ownership.  This ownership model has had an effect on the evolved  
design of the solution.  It has become common practice to use late  
binding and the type object, creating runtime circular references, to  
get the job done (remember schedule schedule schedule).  There are  
three different codelines, two are sand-boxes.  So it is very time  
consuming to keep your workspace up to date.  I am not going to list  
all the issues that are being worked.  There are a lot of issues that  
are being worked on.  The hardest part about all of these changes is  
finding a way that has a net effect of buying back time.  If we are  
not buying back time then management will not back the change (that is  
a necessary thing).  I say all this because I have come to think that  
the best way to implement TDD is not at an organisation level, nor at  
a project level, but at the individual level.  The risk that TDD  
imposes on schedule is determined by individual developers.  Some will  
pick it up quickly, they will have a short period of reduced  
productivity and hopefully a higher productivity afterward.  Others  
will have a difficult time picking it up.  Only after enough, critical  
mass, developers on a project have picked up TDD should it be adopted  
by the project.  This is the part where unit tests are executed in the  
build (at a minimum they would become first class citizens in the  
build, they can cause it to fail, graduating from build to CI).  
Becoming a mandatory process on the project.  So this changes the  
focus from how do we implement TDD on this project of 80 developers to  
hey guys who wants to learn TDD.  I have been approaching this from  
the standpoint of TDD has been blessed as a process improvement by  
management (I don’t mean to make that sound optional).  Hey guys  
management says we are going to start doing TDD.  Here’s how you do  
this…  I think I will explore the idea of a management blessed  
grassroots effort.  Instead of acting as a consultant to management I  
should act as a consultant to the developers (I am not, nor have I  
ever been, a developer on this project, causes me a lot of problems).  
I had started doing this with the build and workspace improvements,  
just not consciously.  It has all clicked for me now.

Grassroots Management Blessed Effort

I have been having great success with getting a plan together to  
improve the build and workspace issues.  I created a Build Improvement  
Team and am acting as a consultant to the developers on the team.  The  
improvement effort is blessed by management.

Have I explained this shift well?  Do you understand?  Do you agree?  
What pitfalls do you see…


|
