---
title: common_nant_tasks
date: "2006-05-04"
draft: false
categories:
  - "Wiki"
aliases:
  - "/wiki/common-nant-tasks/"
params:
  wayback_url: "https://web.archive.org/web/20060514160925//wiki/common-nant-tasks/"
  original_url: "/wiki/common-nant-tasks/"
  archived_from: Wayback Machine

---

[[[common\_nant\_tasks](/wiki/common-nant-tasks/)]]



### [Articles](/wiki/articles/) :: [Software Projects](/wiki/software-projects/) :: [Works in Progress](/wiki/works-in-progress/)

---

# This page has moved and you will be redirected.



## Description

This is an assmebly of tasks, types, and functions that I found I could not live without.

**Tasks:**

- LargeProperty *[Link removed: content not recovered during site restoration]*
- LoopThrough *[Link removed: content not recovered during site restoration]*
- Replace *[Link removed: content not recovered during site restoration]*
- SaveProperties *[Link removed: content not recovered during site restoration]*
- Strings *[Link removed: content not recovered during site restoration]*
- Write *[Link removed: content not recovered during site restoration]*
- IfThenElse *[Link removed: content not recovered during site restoration]*
- Function *[Link removed: content not recovered during site restoration]*

**Functions:**

- FileSet *[Link removed: content not recovered during site restoration]*
- StringList *[Link removed: content not recovered during site restoration]*

**Type:**

- SaveProperty *[Link removed: content not recovered during site restoration]*
- StringItem *[Link removed: content not recovered during site restoration]*
- TextElement *[Link removed: content not recovered during site restoration]*

## Quick Example

```
<strings id="Numbers">
  <string value="1"/>
  <string value="2"/>
  <string value="3"/>
  <string value="4"/>
</strings>
 
<function execute="${stringlist::add('Numbers', '5')}"/>
 
<ifthenelse test="${stringlist::contains('Numbers', '5')}">
  <then>
    <echo message="Added number 5 to StringList, count = ${stringlist::count('Numbers')}."/>
  </then>
  <elseif if="false" >
    <echo message="This won't happen."/>
  </elseif>
  <else>
    <echo message="Did not add number 5 to StringList, count = ${stringlist::count('Numbers')}."/>
  </else>
</ifthenelse>
 
<function execute="${stringlist::remove('Numbers', '2')}"/>
 
<loopthrough property="Number">
  <items>
    <strings refid="Numbers" />
  </items>
  <do>
    <echo message="Number ${Number}!"/>
  </do>
</loopthrough>

Copyright (C) 2001-2005 Gerry Shaw
http://nant.sourceforge.net

Buildfile: file:///C:/Projects/CI Factory/Current/Product/nAnt Scratch/Scratch.build.xml
Target framework: Microsoft .NET Framework 1.1
Target(s) specified: test 

[loadtasks] Scanning assembly "Common.Functions" for extensions.

test:

     [echo] Added number 5 to StringList, count = 5.
     [echo] Number 3!
     [echo] Number 1!
     [echo] Number 4!
     [echo] Number 5!

BUILD SUCCEEDED

Total time: 0.1 seconds.
```

## Download

common.tasks.zip *[Link removed: content not recovered during site restoration]*

common\_nant\_tasks.txt · Last modified: 2006/05/04 14:54 by jflowers
