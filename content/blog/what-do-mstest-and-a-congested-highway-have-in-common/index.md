---
title: "What do MSTest and a congested highway have in common?"
date: "2007-06-07"
draft: false
categories:
  - "Unit Testing"
aliases:
  - "/WordPress/?p=163"
  - "/WordPress/index.php?p=163"
params:
  wayback_url: "https://web.archive.org/web/20071211044211/http://jayflowers.com:80/WordPress/?p=163"
  original_url: "http://jayflowers.com:80/WordPress/?p=163"
  archived_from: Wayback Machine

---

## What do MSTest and a congested highway have in common?

By the time they have been upgraded they are out of date again.

[Naysawn Naderi](http://blogs.msdn.com/nnaderi/default.aspx), the PM for MSTest, [posted about improvements](http://blogs.msdn.com/nnaderi/archive/2007/05/11/new-unit-testing-features-in-orcas-part-1.aspx) that they are making to MSTest to bring it more inline with TDD usage.  He details 6 enhancements:

1. Better execution times- Run Tests context menu item- Short cut keys to run tests- Disable deployment- Inheritance of test attributes- Hot stack traces in the failure report

Where does this put MSTest?  On par with an older version of NUnit and TestDriven.NET.  Don’t get me wrong I commend the MSTest team for making these changes and heading in the right direction.  Will these changes get me to use MSTest?  Not willingly.  TestDriven.NET and MbUnit are far superior.  I want to use the best tools available to me.  The biggest difference to me is that TD.NET and MbUnit are extremely extensible.  There easy to extent as well.  I have written several extension for MbUnit including an [object provider fixture](http://jayflowers.com/WordPress/?p=46) and with Jamie’s help a [FitNesse runner](http://jayflowers.com/WordPress/?p=157) for TD.NET.  Being able to write extensions is critical to MSTest, I believe more so than it is for MbUnit or NUnit.  Microsoft releases software on a much large time scale than the Open Source community.  Both MbUnit and NUnit have made several releases since the last release, only release, of MSTest.  Oddly for free MbUnit/cheap TD.NET I get more value on a more frequent basis.  One would think that for the money that MSTest costs you would get everything that TD.NET and MbUnit had to offer and more.

I want to be clear about the spirit in which I say all this.  I think that MSTest could, COULD, be a great product.  The MSTest team has a big challenge in front of them and there is no good reason why they can’t rise to it.

The most important capability missing is extensibility,

The most important feature missing is light weight parameterized unit testing.  Please don’t confuse this with what Pex is.  Pex is a great solution for the limitations of what MSTest is right now.  This needs to be baked in, be a first class citizen of the grand design.  I want to use attributes to define parameters.  I want each set of parameters to be reported on as a separate test result.  I also want the option to use a factory to provide the parameters.  I want elegant solutions.


```batch
If I did not think that the MSTest team was competent I would not have written this post.
```

Don’t forget that you have to innovate on top of everything that I have asked for.  MbUnit, NUnit, and TD.NET are not going to wait for you to catch up.
