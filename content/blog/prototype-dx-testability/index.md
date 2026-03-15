---
title: "Prototype: DX Testability"
date: "2006-09-05"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=76"
  - "/WordPress/index.php?p=76"
params:
  wayback_url: "https://web.archive.org/web/20061124112250/http://jayflowers.com:80/WordPress/?p=76"
  original_url: "http://jayflowers.com:80/WordPress/?p=76"
  archived_from: Wayback Machine

---

## Prototype: DX Testability

So I have been holding on to this DXCore plugin for a while now.  I would like to have it a little more polished but it is just a prototype so I guess I should release it.  It adds three new metrics to DXCore; Compound Cyclomatic Complexity, Efferent Coupling, and Compound Efferent Coupling.

[![](images/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/MetricDropDown_thumb1.jpg)](http://jayflowers.com/WordPress/wp-content/uploads/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/MetricDropDown2.jpg)

Just in case you are not familiar with DXCore’s metrics they will also show to the left or right of the member declaration (see images below).

These metrics are a first crack at giving realtime feedback to developers as to how difficult there design will be to unit test.  These new metrics provide information about the type population that the test subject member depends on.  Efferent Coupling is based of the member not the type, meaning the the starting point for gathering the metric is the member.  In this case what types does Fill depend on, not what types does Fills parent class depend on.  Remember the metrics are geared to provide information on the test subject member not the entire test subject class.  Compound Efferent Coupling gives you the size of the type population that you will be working with in a unit test.  The Compound Cyclomatic Complexity tells you the overall complexity of the type population.  The easier a test subject is to test the lower all these metrics will be.  In the examples below the test subject member is Fill.  Please notice there are two images for each metric, a bad and a good one.  The bad includes a dependency on Warehouse the Good only depends on IWarehouse.

**Bad Efferent Coupling (5)**

[![Bad Efferent Coupling (5)](images/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/EfferentCouplingBad_thumb1.jpg)](http://jayflowers.com/WordPress/wp-content/uploads/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/EfferentCouplingBad3.jpg)

**Good Efferent Coupling (2)**

[![Good Efferent Coupling (2)](images/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/EfferentCouplingGood_thumb1.jpg)](http://jayflowers.com/WordPress/wp-content/uploads/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/EfferentCouplingGood2.jpg)

**Bad Compound Efferent Coupling (7)**

[![Bad Compound Efferent Coupling (7)](images/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/CompundEfferentCouplingBad_thumb1.jpg)](http://jayflowers.com/WordPress/wp-content/uploads/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/CompundEfferentCouplingBad2.jpg)

**Good Compound Efferent Coupling (3)**

[![Good Compound Efferent Coupling (3)](images/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/CompundEfferentCouplingGood_thumb1.jpg)](http://jayflowers.com/WordPress/wp-content/uploads/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/CompundEfferentCouplingGood2.jpg)

**Bad Compound Cyclomatic Complexity (16)**

[![Bad Compound Cyclomatic Complexity (16)](images/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/CompoundCyclomaticComplexityBad_thum.jpg)](http://jayflowers.com/WordPress/wp-content/uploads/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/CompoundCyclomaticComplexityBad2.jpg)

**Good Compound Cyclomatic Complexity (11)**

[![Good Compound Cyclomatic Complexity (11)](images/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/CompoundCyclomaticComplexityGood_thu.jpg)](http://jayflowers.com/WordPress/wp-content/uploads/2006/09/WindowsLiveWriter/PrototypeDXTestability_B889/CompoundCyclomaticComplexityGood2.jpg)

**Warning!**

This is not production worthy.  It is not optimized, in fact it can be down right slow depending on the code being analyzed.  As well the algorithms that generate the metrics may have bugs.  This is a prototype.  It’s purpose is to help get more information and determine if there is a product in this idea.

[**Download**](http://jayflowers.com/joomla/index.php?option=com_remository&Itemid=33&func=fileinfo&id=17)

**Note:** You will need to have DXCore installed.  You can download it from [**here**](http://www.devexpress.com/Downloads/NET/IDETools/DXCore/).






|

|
