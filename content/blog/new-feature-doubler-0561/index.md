---
title: "New Feature - Doubler 0.5.6.1"
date: "2006-09-01"
draft: false
categories:
  - "Doubler"
  - "Unit Testing"
aliases:
  - "/WordPress/?p=69"
  - "/WordPress/index.php?p=69"
params:
  wayback_url: "https://web.archive.org/web/20070307194803/http://jayflowers.com:80/WordPress/?p=69"
  original_url: "http://jayflowers.com:80/WordPress/?p=69"
  archived_from: Wayback Machine

---

## New Feature - Doubler 0.5.6.1

I guess the talk about Doubler got me motivated: I added a new feature. You can now select an entire assembly to create test stub recorders for!

![ManyRecordingsGeneratorContextMenuItem](images/2006/09/BlogFiles/ManyRecordingsGeneratorContextMenuItem.png)

The options page looks much the same as for generating a single test stub recorder.

![ManyRecordingsGeneratorView](images/2006/09/BlogFiles/ManyRecordingsGeneratorView.png)

Notice the icon in the bottom right this is dragable like a folder is dragable from Windows Explorer. It is tied to the a folder named after the root namespace.

![LotsOfRecorders](images/2006/09/BlogFiles/LotsOfRecorders_small1.jpg)

In this example EF.

This feature can be useful to maintain a mirror assembly of recorders. If the abstracts types in the subject assembly change the doubles will no longer compile. This can be managed by hand, yuck!, regenerating each file individually, maybe okay?, and now regenerate the entire assembly. This will make it intuitive for developers to know where to look for a double as well. It is in the assembly name <SubjectAssemblyName>.TestDoubles.dll, in the namespace <SubjectNamespace>.TestDouble, with a class name… in the case of test stub recorders Recorder<SubjectTypeName>.

**I have not added a progress bar, please be sure that it is done generating recorders before you drag! I watch the task manager cpu to know. 50 classes takes about 3 secs on my old laptop.**

**Release Notes:**

Lots and lots of fixes, I lost track. There is a new feature too!

If you right click on an assembly in the tree view of Reflector you can select to make Recorders for all abstract types found in the assembly. The drag and drop icon is attached to the folder where they are all written too. Drag that to the project in solution explorer to add to a project.

Know issue: Events with params by ref need to be edited by hand to pass the arguments received on the Fire<eventName> method to the event invocation.

[Download](http://jayflowers.com/joomla/index.php?option=com_remository&Itemid=33&func=fileinfo&id=16)




|

|
