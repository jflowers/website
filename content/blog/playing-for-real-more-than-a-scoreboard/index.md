---
title: "Playing for Real, More Than a Scoreboard"
date: "2006-12-15"
draft: false
categories:
  - "Continuous Integration"
aliases:
  - "/WordPress/?p=105"
  - "/WordPress/index.php?p=105"
params:
  wayback_url: "https://web.archive.org/web/20070903202336/http://jayflowers.com:80/WordPress/?p=105"
  original_url: "http://jayflowers.com:80/WordPress/?p=105"
  archived_from: Wayback Machine

---

## Playing for Real, More Than a Scoreboard

For the umpteenth time I am working on getting my organization to adopt TDD.  We have been directed to figure out how to adopt unit testing.  So regardless of TDD or some other way we will be writing unit tests.  So we will have some kind of objective like increase the number of unit tests.  Point being there will be a measure.  This measure will need to be on a public scoreboard because if it ain’t we are just playing around.  A scoreboard communicates that you are serious.  So you need to have a scoreboard that exudes seriousness.  I have been [![](images/2006/12/WindowsLiveWriter/PlayingforRealMoreThanaScoreboard_11B23/CropperCapture%5B1%5D_thumb%5B2%5D.jpg)](http://jayflowers.com/WordPress/wp-content/uploads/2006/12/WindowsLiveWriter/PlayingforRealMoreThanaScoreboard_11B23/CropperCapture%5B1%5D%5B4%5D.jpg)working on a [Analytics Package](http://jayflowers.com/WordPress/?p=95) for CI Factory.  This package will add yet another plugin link to CCNET’s web page bringing our configuration to a grand total of 10 links on the build page.  There is an overwhelming amount of information on the build page.  To make matters worse we have more to add, MSTest has no detailed report page and we have not added FXCop into the mix yet.  The scoreboard is likely to be lost in this sea of information.

This week I have been piecing together the beginnings of a new package.  At the moment I am calling it the Threshold Package.  It has been suggested to me that the Big Brother Package might be more appropriate.  This package can monitor values generated in the build as well as differences between the current and previous builds.  Take unit testing for example.  At the moment it will send out a thank you email to anyone that adds a unit test, increases the unit test count.  As well it will send a warning email to anyone that reduces the unit test count.

---

Subject: 1.0.0.2: Thanks For Adding More Unit Tests

12/15/2006 09:48:21

1.0.0.2

jflowers,

Thank you for increasing the number of unit tests from 119 to 120.

Cheers,

Your pal the build server.

---

Subject: 1.0.0.3: Did You Mean to Remove Unit Tests?

12/15/2006 09:42:22

1.0.0.3

jflowers,

Please take note that you have reduced the number of unit tests from 120 to 119.

Cheers,

Your pal the build server.

---

So that little example shows some interesting possibilities for shaping developers.  Notice that there was positive feedback as well as negative and even the negative is not very direct.  I imagine that this could be used to help shape a culture.  Now please don’t think that I mean human interaction will not be needed.  I see this as a helpful tool for engaged leaders.  I don’t see this working out well for a leader of the command style.  I do see it working for the leadership styles: visionary, affiliative, and coaching.  The emails should go to more than just the developer, they should be sent to the leaders as well.  This will help the leaders to remember to engage.

I think this Threshold Package will raise the scoreboard up and keep it from being lost in the sea of data.  It will be the exuder as long as the leaders play their part.




|

|
