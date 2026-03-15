---
title: creating_a_loop_diagram_for_ci
date: "2007-06-01"
draft: false
categories:
  - "Wiki"
aliases:
  - "/doku/doku.php?id=creating_a_loop_diagram_for_ci"
params:
  wayback_url: "https://web.archive.org/web/20190823140851/http://jayflowers.com/doku/doku.php?id=creating_a_loop_diagram_for_ci"
  original_url: "http://jayflowers.com/doku/doku.php?id=creating_a_loop_diagram_for_ci"
  archived_from: Wayback Machine

---

[[[creating\_a\_loop\_diagram\_for\_ci](/doku/doku.php?id=creating_a_loop_diagram_for_ci&do=backlink)]]

[JayFlowers](/doku/doku.php?id= "[ALT+H]")

Trace: » [creating\_a\_loop\_diagram\_for\_ci](/doku/doku.php?id=creating_a_loop_diagram_for_ci "creating_a_loop_diagram_for_ci")

### Some Resources:

First you need to understand how to draw loop diagrams:  
  
Guidelines for Drawing Loop Diagrams  
[http://www.thesystemsthinker.com/tstgdlines2.html](http://www.thesystemsthinker.com/tstgdlines2.html "http://www.thesystemsthinker.com/tstgdlines2.html")  
[http://www.systemsprimer.com/making\_loops\_intro.htm](http://www.systemsprimer.com/making_loops_intro.htm "http://www.systemsprimer.com/making_loops_intro.htm")  
  
Tool for Drawing Loop Diagrams: MapSys [http://www.simtegra.com](http://www.simtegra.com "http://www.simtegra.com")  
  
Later you will need to read the diagram as it will be more complex than the simple diagrams used to illustrate how to draw loop diagrams.  
  
Systems Thinking Archetypes:  
[http://www.systems-thinking.org/arch/arch.htm](http://www.systems-thinking.org/arch/arch.htm "http://www.systems-thinking.org/arch/arch.htm")  
[http://www.exponentialimprovement.com/cms/uploads/ArchetypesGeneric02.pdf](http://www.exponentialimprovement.com/cms/uploads/ArchetypesGeneric02.pdf "http://www.exponentialimprovement.com/cms/uploads/ArchetypesGeneric02.pdf")  
[http://www.exponentialimprovement.com/cms/uploads/Archetypes%20Gang%20Up7.pdf](http://www.exponentialimprovement.com/cms/uploads/Archetypes%20Gang%20Up7.pdf "http://www.exponentialimprovement.com/cms/uploads/Archetypes%20Gang%20Up7.pdf")

### Fodder for the story

The fodder below has been taken from:  
[http://www.martinfowler.com/articles/continuousIntegration.html](http://www.martinfowler.com/articles/continuousIntegration.html "http://www.martinfowler.com/articles/continuousIntegration.html")  
[Software Configuration Management Patterns: Effective Teamwork, Practical Integration](http://www.amazon.com/Software-Configuration-Management-Patterns-Integration/dp/0201741172/ref=sr_1_1/102-1023087-7897755?ie=UTF8&s=books&qid=1180609369&sr=8-1 "http://www.amazon.com/Software-Configuration-Management-Patterns-Integration/dp/0201741172/ref=sr_1_1/102-1023087-7897755?ie=UTF8&s=books&qid=1180609369&sr=8-1")

Active Development Line You have an evolving codeline that has code intended to work with a future product release. You are doing most of your work on a Mainline. When you are working in a dynamic development environment, many people are changing the code. Team members are working toward making the system better, but any change can break the system, and changes can conflict. This pattern helps you balance stability and progress in an active development effort.

Integration Build All developers work in their own Private Workspace so that they can control when they see other changes. This helps individual developers make progress, but in many workspaces people are making independent changes that must integrate together, and the whole system must build reliably. This pattern addresses mechanisms for helping ensure that the code for a system always builds.

Private Workspace In Active Development Line, you and other developers make frequent changes to the code base, both to the modules you are working on and to modules you depend on. You want to be sure you are working with the latest code, but because people don’t deal well with uncontrolled change, you want to be in control when you start working with other developers’ changes. This pattern describes how you can reconcile the tension between always developing with a current code base and the reality that people cannot work effectively when their environment is in constant flux.

Development workspace All developers and the Integration Build work in their own Private Workspaces yet there needs to be consistency between them. This pattern is a means to define the structure of the Private Workspace.

private build A Private Workspace allows you, as a developer, to insulate yourself from external changes to your environment. But your changes need to work with the rest of the system too. To verify this, you need to build the system consistently, including building with your changes. This pattern explains how you can check whether your code will still be consistent with the latest published code base when you submit your changes.

Unit Test Sometimes a Smoke Test is not enough to test a change in detail when you are working on a module, especially when you are working on new code. This pattern shows you how to test detailed changes so that you can ensure the quality of your codeline.

Task level commit An Integration Build is easier to debug if you know what went into it. This pattern discusses how to balance the needs for stability, speed, and atomicity.

Every Commit Should Build the Mainline on an Integration Machine

By doing this frequently, developers quickly find out if there’s a conflict between two developers. The key to fixing problems quickly is finding them quickly. With developers committing every few hours a conflict can be detected within a few hours of it occurring, at that point not much has happened and it’s easy to resolve. Conflicts that stay undetected for weeks can be very hard to resolve.

Keep the Build Fast: The whole point of Continuous Integration is to provide rapid feedback. Nothing sucks the blood of a CI activity more than a build that takes a long time.

Test in a Clone of the Production Environment

Make it Easy for Anyone to Get the Latest Executable

Continuous Integration is all about communication, so you want to ensure that everyone can easily see the state of the system and the changes that have been made to it.

### Variables

- Commit/Build Frequency
- Changeset Size
- Speed of the Build
- Stability of the Codeline
- Size of the Team
- Effectiveness of Tests
- Availability of Product
- Information Radiation
- Risk of Break
- Time to find and fix bugs
- Rate of Change to Codeline
- Size of Team
- Avg Time to Fix a Broken Build
- Frequency of Broken Builds
- Build Availability
- Workspace tractability
- Task Size

### Diagrams

[![](/doku/lib/exe/fetch.php?w=&h=&cache=cache&media=ci-loop-diagram-1.png)](/doku/lib/exe/detail.php?id=creating_a_loop_diagram_for_ci&cache=cache&media=ci-loop-diagram-1.png "ci-loop-diagram-1.png")  
[ci.msys](/doku/lib/exe/fetch.php?id=creating_a_loop_diagram_for_ci&cache=cache&media=ci.msys "ci.msys")

creating\_a\_loop\_diagram\_for\_ci.txt · Last modified: 2007/06/01 07:17 by jflowers
