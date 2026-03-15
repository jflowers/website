---
title: Reflector 5.0
date: "2007-02-20"
draft: false
categories:
  - "Doubler"
  - "Tools"
aliases:
  - "/WordPress/?p=136"
  - "/WordPress/index.php?p=136"
params:
  wayback_url: "https://web.archive.org/web/20070302064606/http://jayflowers.com:80/WordPress/?p=136"
  original_url: "http://jayflowers.com:80/WordPress/?p=136"
  archived_from: Wayback Machine

---

## Reflector 5.0

So there is a new version of Reflector out. As always you can get Reflector at Lutz’s site: [http://www.aisto.com/roeder/dotnet/](http://www.aisto.com/roeder/dotnet/ "http://www.aisto.com/roeder/dotnet/"). You can get add-ins for Reflector from [http://www.codeplex.com/reflectoraddins](http://www.codeplex.com/reflectoraddins "http://www.codeplex.com/reflectoraddins"). Lutz has a slidedeck of the new features [here](http://www.aisto.com/roeder/paper/reflector5.ppt).

Doubler has been recompiled against this new version of Reflector. There are no new features in the release of Doubler. Please find Doubler [0.5.6.2](http://code.google.com/p/doubler/) at the new Google Code project site.

There are some new features of Reflector that you should know about. The first thing that you should do is run the register commandline switch. Go to the command prompt that execute **Reflector.exe /register**. This will make dlls open with Reflector, you can double click them ![Shell Context Menu](images/2007/02/WindowsLiveWriter/Reflactor5.0_132A8/ShellContextMenu%5B4%5D.gif) and they open in Reflector. I think this was in the previous version. He has added some more integration into the shell with a **code** URI. I can see how this will be used in blogging and I bet there will be a Reflector add-in for that in the near future.

[code://mscorlib/System.IO.Directory](code://mscorlib/System.IO.Directory "code://mscorlib/System.IO.Directory")

You are supposed to be able to copy the current item to the clipboard with Ctrl+Alt+C but I was never able to get it to work.

The next thing that I suggest you do is set a few new configuration options. Make sure that the Show PDB symbols is checked, this is not a new setting for this version but is still kind of new. I would make sure that you set the Optimization to the version of .Net that you are interested in (none, 1.0, 2.0, and 3.5). A nice new feature is on the Browser tab, automatically resolve assemblies. I have been wait a while for this one. No more prompting for assemblies it can find on it’s own.

One of the best new features is the ability to show multiple windows in the right pane. I would really like to search and view a result without losing the search result state. You can Analyze and view an item from Analyzer window in the Disassembler window without loosing state in the Analyzer window. You can even add more Analyzed items into the Analyzer window.

![Analyzer](images/2007/02/WindowsLiveWriter/Reflactor5.0_132A8/Analyzer%5B3%5D.gif)

There are three new types of Analyzer results: Exposed By, Instantiated By, and Assigned By. I don’t know about you but I have really need the Exposed By result. I always seem to find what I need and then have to spend time finding how to get it. This will help me save a bunch of time on those types of tasks. I have been shying away from using NDepend 2.0 for this type of thing.

The last big thing for me has been the Expand Methods functionality in the Disassembler window. You can now view the entire type on one page.

![Expand Methods](images/2007/02/WindowsLiveWriter/Reflactor5.0_132A8/ExpandMethods%5B3%5D.gif)

I have not jumped into the LINQ thing yet but for those of you that have Reflector now supports it.




|

|
