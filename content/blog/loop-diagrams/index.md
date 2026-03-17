---
title: Loop Diagrams
date: "2007-09-06"
draft: false
categories:
  - "Continuous Integration"
aliases:
  - "/WordPress/?p=184"
  - "/WordPress/index.php?p=184"
params:
  wayback_url: "https://web.archive.org/web/20071112060655/http://jayflowers.com:80/WordPress/?p=184"
  original_url: "http://jayflowers.com:80/WordPress/?p=184"
  archived_from: Wayback Machine

---

## Loop Diagrams

[Jeffery Fredrick](http://www.developertesting.com/) asked for some verbage around the loop diagrams that are in the slides from this [post](http://jayflowers.com/WordPress/?p=182).

The first slide with a loop diagram was about simply adding value:

![AddValueLoop](images/2007/08/AddValueLoop.png)

This is generally the situation in which a project is in before adding Continuous Integration.  Please know that the Ss and Os in the diagram stand for same and opposite (thanks again Jeff), meaning the two nodes connected by the line vary the same or in opposition.  So this diagram says that:  As desired value increases so does the gap in value.  As the gap in value increase so does the actions to add value.  When there is a delay in the system or when the perception is inadequate, increases in action to add value worsen the delay and or perception, which in turn increase the gap in value.  Alternatively when the system does not have a delay or issue with fidelity of perception, actual value increases as actions to add value increase, which decrease the gap in value.

I like the picture better than my words. ![:-)](http://jayflowers.com/WordPress/wp-includes/images/smilies/icon_smile.gif)

The next slide is on causality:

![CropperCapture[14]](images/2007/08/CropperCapture%5B14%5D.png)

I first blogged about this back in this [post](http://jayflowers.com/WordPress/?p=150).  I really like this example.  I think it does a spectacular job of taking what is normally very tacit knowledge and makes it accessible to your cerebral cortex.  This is a concrete example of the previous diagram and hopefully is an easy step from there to here.

The next slide is on the question: Did what we just change make things worse?

[![CropperCapture[2]](images/2007/08/CropperCapture%5B2%5D_thumb.png)](http://jayflowers.com/WordPress/wp-content/uploads/2007/08/CropperCapture%5B2%5D.png)

What is this stuff about mind you say?  I originally blog about this over [here](http://jayflowers.com/WordPress/?p=168).  Here is the excerpt:

> …Many new practitioners of meditation say that there minds are more chaotic and less calm than before they ever meditated.  Their instructor will point out that this is a perception.  That this is a good sign.  Their minds are not more chaotic, they are more aware of their minds.  They have reduced a delay in feedback as well as increased the quality of the feedback.
>
> This perception of things getting worse before they get better is common to any system in which there is:
>
> - A negative gap in reality and the perception of reality.- A significant delay in perception.- Poor quality of perception.
>
> Many Agile practices fall into this category.  They not only remove delays, they increase the fidelity of the feedback.
>
> Ignorance is bliss?  At least until the bill is due.

The last loop diagram slide is on specifically CI of course. ![:-P](http://jayflowers.com/WordPress/wp-includes/images/smilies/icon_razz.gif)

![CILoopDiagram](images/2007/08/CILoopDiagram.png)

This diagram is by no means complete.  It is meant to spark a dialogue on this subject.  I would like it to to be a resource for people who are evaluating possible changes to their environment or even just to understand what is going on in there existing environment.  For example, it will help to answer the question: What are the consequences of a long running build?

I have a page on my wiki about working with this loop diagram [here](/wiki/creating-a-loop-diagram-for-ci/).  It includes information on understanding loop diagrams, creating loop diagrams, software for creating loop diagrams, as well as fodder and variables for this loop diagram.  Lastly it includes a link to a download of the project file for this loop diagram.

I hope over the next year to be able to flesh this out at all the different conferences that I will be going to.  I truly believe that this will be a great asset to the CI community.
