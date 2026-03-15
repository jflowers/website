---
title: common_nant_tasks
date: "2006-05-04"
draft: false
categories:
  - "Wiki"
aliases:
  - "/doku/doku.php?id=common_nant_tasks"
params:
  wayback_url: "https://web.archive.org/web/20060514160925/http://jayflowers.com:80/doku/doku.php?id=common_nant_tasks&amp;DokuWiki=2e807874e3c3eed68c9d7bab1c907781"
  original_url: "http://jayflowers.com:80/doku/doku.php?id=common_nant_tasks&amp;DokuWiki=2e807874e3c3eed68c9d7bab1c907781"
  archived_from: Wayback Machine

---

[[[common\_nant\_tasks](/doku/doku.php?id=common_nant_tasks&do=backlink&DokuWiki=76309d334572ff0c1c62e8625f7f41cd)]]

[JayFlowers](/doku/doku.php?id=&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "[ALT+H]")

### [Articles](/doku/doku.php?id=articles&DokuWiki=76309d334572ff0c1c62e8625f7f41cd) :: [Software Projects](/doku/doku.php?id=software_projects&DokuWiki=76309d334572ff0c1c62e8625f7f41cd) :: [Works in Progress](/doku/doku.php?id=works_in_progress&DokuWiki=76309d334572ff0c1c62e8625f7f41cd)

---

# This page has moved and you will be redirected.

![](/joomla/templates/mp_chinook/images/logo.jpg)

## Description

This is an assmebly of tasks, types, and functions that I found I could not live without.

**Tasks:**

- [LargeProperty](/doku/doku.php?id=nant.largeproperty&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.largeproperty")
- [LoopThrough](/doku/doku.php?id=nant.loopthrough&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.loopthrough")
- [Replace](/doku/doku.php?id=nant.replace&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.replace")
- [SaveProperties](/doku/doku.php?id=nant.saveproperties&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.saveproperties")
- [Strings](/doku/doku.php?id=nant.strings&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.strings")
- [Write](/doku/doku.php?id=nant.write&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.write")
- [IfThenElse](/doku/doku.php?id=nant.ifthenelse&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.ifthenelse")
- [Function](/doku/doku.php?id=nant.function&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.function")

**Functions:**

- [FileSet](/doku/doku.php?id=nant.filesetfunctions&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.filesetfunctions")
- [StringList](/doku/doku.php?id=nant.stringlistfunctions&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.stringlistfunctions")

**Type:**

- [SaveProperty](/doku/doku.php?id=nant.saveproperty&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.saveproperty")
- [StringItem](/doku/doku.php?id=nant.stringitem&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.stringitem")
- [TextElement](/doku/doku.php?id=nant.textelement&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "nant.textelement")

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

[common.tasks.zip](/doku/lib/exe/fetch.php?id=common_nant_tasks&cache=cache&media=common.tasks.zip&DokuWiki=76309d334572ff0c1c62e8625f7f41cd "common.tasks.zip")

common\_nant\_tasks.txt · Last modified: 2006/05/04 14:54 by jflowers
