---
title: TestDriven.Net FitNesse Runner
date: "2007-06-15"
draft: false
categories:
  - "Tools"
aliases:
  - "/WordPress/?p=157"
  - "/WordPress/index.php?p=157"
params:
  wayback_url: "https://web.archive.org/web/20080213202608/http://jayflowers.com:80/WordPress/?p=157"
  original_url: "http://jayflowers.com:80/WordPress/?p=157"
  archived_from: Wayback Machine

---

## TestDriven.Net FitNesse Runner

I would like to introduce a new plugin to [TestDriven.NET](http://www.testdriven.net).  This test runner executes [FitNesse](http://www.fitnesse.org) tests.

![fitrunner](images/2007/06/fitrunner.png)

Notice the attribute FitNesseUrl above.  This specifies what page the runner should execute.

![CropperCapture[8]](images/2007/06/CropperCapture%5B8%5D.png)

The output of the test is a little different than what you get with a unit test: the metrics are page based.  I have included a link to the live FitNesse url as well as a static html report of the test run.  Of course the Test With menu items work with this so you can Debug and get code coverage.

There is no installer yet.  Heck the TestDriven.NET FitNesse Runner has no home.  Until it gets a home here is the [binary](http://jayflowers.com/Misc%20Downloads/Fit.TestRunner-Binary.zip) and here is the [source](http://jayflowers.com/Misc%20Downloads/Fit.TestRunner-Source.zip).  To use it just reference it (and Program Files\TestDriven.NET 2.0\TestDriven.Framework.dll) from your fit fixture project and include this assembly level attribute:

[assembly: CustomTestRunner(GetType(TestRunner.FitTestRunner))]

This attribute clues TestDriven.NET into what runner to use.  Once we get an installer we can create the registry entries that are normally used to clue TestDriven.NET into what runner to use.

Where do you think the FitNesse plugin’s home should be?
