---
title: nAnt Scratch
date: "2006-06-03"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=49"
  - "/WordPress/index.php?p=49"
params:
  wayback_url: "https://web.archive.org/web/20070307194616/http://jayflowers.com:80/WordPress/?p=49"
  original_url: "http://jayflowers.com:80/WordPress/?p=49"
  archived_from: Wayback Machine

---

## nAnt Scratch

I love nAnt.  It can do so many things for me and I can get it to do those things for me so very quickly.  I do not like to leave the IDE, I try to keep the list of reasons for my leaving it short.  To help me keep that list short while still getting nAnt to pull it weight I have integrated nAnt into the IDE through the external tools feature of VS.NET.  This not a brainy thing.  I bet plenty of people have done it.  But I don’t see many and more people should.  Take a look at how I use it.  First I keep a scratch file as a solution item: Scratch.build.xml.  I edit this file to do repetitive tasks for me.

![NAnt Menu Item](http://www.jayflowers.com/BlogFiles/nAnt_20Menu_20Item.png)

While I have the scratch file in focus I execute the nAnt external tool.

![NAnt Command Execution](http://www.jayflowers.com/BlogFiles/nAnt_20Command_20Execution.png)

To get nAnt to show up as an external tool configure a new external tool like so:

![NAnt Command Config](http://www.jayflowers.com/BlogFiles/nAnt_20Command_20Config.png)

Some shops have self contained projects, meaning that everything the project needs to build is contained in its directory structure.  I follow this practice so nAnt is located in the project environment not in my machine environment.  This is important to note if you follow this practice too.  How will VS.NET find the nAnt.exe.  You don’t want to configure a path to a specific projects copy of nAnt.  I use bat files to start my IDE.

![Scratch Dir](http://www.jayflowers.com/BlogFiles/Scratch_20Dir_small.jpg)

This OpenSolution batch file will set the PATH to include nAnt.exe.

```
set PATH=%SystemRoot%system32;%SystemRoot%;%SystemRoot%System32Wbem;C:Program FilesSubversionbin;..BuildnAntbincall "C:Program FilesMicrosoft Visual Studio8VCvcvarsall.bat"devenv "Doubler.sln"
```

You may have noticed the RunScratch batch file as well.  This for situations when you need to call devenv.exe from the nAnt script. For some reason it will not compile a lick from the commanline if the IDE is open.  I don’t know why.

Something more we can do to make this easier is map a control key sequence to execute the nAnt script.  All external tool entries have a VS.NET command.  Look in the registry to find the external tool number.  On my machine nAnt is 2.

![NAnt Command Reg Entry](http://www.jayflowers.com/BlogFiles/nAnt_20Command_20Reg_20Entry.png)

I mapped mine to Ctrl+Shift+N.

![NAnt Shortcut Keys](http://www.jayflowers.com/BlogFiles/nAnt_20Shortcut_20Keys.png)
