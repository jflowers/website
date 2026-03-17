---
title: a_recipe_for_build_maintainability_and_reusability
date: "2006-10-14"
draft: false
categories:
  - "Wiki"
aliases:
  - "/wiki/a-recipe-for-build-maintainability-and-reusability/"
params:
  wayback_url: "https://web.archive.org/web/20160910022614//wiki/a-recipe-for-build-maintainability-and-reusability/"
  original_url: "/wiki/a-recipe-for-build-maintainability-and-reusability/"
  archived_from: Wayback Machine

---

[[[a\_recipe\_for\_build\_maintainability\_and\_reusability](/wiki/a-recipe-for-build-maintainability-and-reusability/)]]



Trace: » [traceability\_and\_continuous\_integration](/wiki/traceability-and-continuous-integration/ "traceability_and_continuous_integration") » [a\_recipe\_for\_build\_maintainability\_and\_reusability](/wiki/a-recipe-for-build-maintainability-and-reusability/ "a_recipe_for_build_maintainability_and_reusability")

## Continuous Integration

Definition: The practice of integrating (compiling and testing) changes produced by a task into the product’s code line before starting on another task.

There are many benefits to Continuous Integration(CI). It is helpful to understand that CI is not a practice performed in isolation. There are several other practices that support CI and still others that depend on it. The benefits of these supporting practices are magnified as they culminate into CI. A simple example is the practice of unit testing. A developer experiences many benefits when practicing unit testing in their own Private Workspace: rapid feedback, localization of errors, confidence to make change, and more. When unit tests are exercised in the practice of CI their meaning is subtly altered. The tests are being run on an independent machine after a clean build. This adds to the feedback: not only did it work on my machine it worked on the integration build server so it should work on any machine. The following list of benefits may seem familiar, that is because of CI’s supporting practices.

- Rapid Feedback.
- Decreased time in the debugger.
- Identification of bugs early.
- Localization of bugs.
- Decreases the need for or length of code freezes.
- The product is always in a stable/releasable state.
- It is easy to get a new developer’s system up and running and keep it up to date.

This paper will cover how to successfully implement CI in a repeatable way. I’m sure that you don’t work in a vacuum, there are many other projects going on where you work. If one project shows success with a new practice others become interested and would like to try. Maybe you are even a CI evangelist! First the supporting practices will be covered and the synergy they create to be come CI. Secondly a high level discussion on implementing a CI server. Then moving into how to take that success and pull the reusable parts out. Concluding in packaging up the reuse in a process for new projects to use.

## Pattern Language

Before we move on lets make sure we understand the system, or pattern language, in which CI exists. The pattern Active Development Line[1)](#fn__1) describes some of the goals of CI. In figure 1 a dependence diagram of patterns shows how Active Development Line is supported.

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Figure 1 | | Patlets | | --- | | [Active Development Line Patlet](/wiki/active-development-line-patlet/ "active_development_line_patlet") | | [Integration Build Patlet](/wiki/integration-build-patlet/ "integration_build_patlet") | | Private Workspace Patlet *[Link removed: content not recovered during site restoration]* | | Private Build System Patlet *[Link removed: content not recovered during site restoration]* | | [Unit Test Patlet](/wiki/unit-test-patlet/ "unit_test_patlet") | | [Task Level Commit Patlet](/wiki/task-level-commit-patlet/ "task_level_commit_patlet") | | [Development Workspace Patlet](/wiki/development-workspace-patlet/ "development_workspace_patlet") | | [Communication Lines Patlet](/wiki/communication-lines-patlet/ "communication_lines_patlet") | | Repository Patlet *[Link removed: content not recovered during site restoration]* | | [Third Party Codeline Patlet](/wiki/third-party-codeline-patlet/ "third_party_codeline_patlet") | |

  

Above is a list of patlets you can review, Active Development Line is the most relevant to our task at hand, understanding what CI is supporting, and is displayed below:

| Active Development Line Patlet |
| --- |
| Context You have an evolving codeline that has code intended to work with a future product release. You are doing most of your work on a Mainline. When you are working in a dynamic development environment, many people are changing the code. Team members are working toward making the system better, but any change can break the system, and changes can conflict. This pattern helps you balance stability and progress in an active development effort. Problem How do you keep a rapidly evolving codeline stable enough to be useful? Solution Institute policies that are effective in making your main development line stable enough for the work it needs to do. Do not aim for a perfect active development line but for a mainline that is usable and active enough for your needs. |

  

The pattern Active Development Line describes forces seen from a particular perspective. I can think of some forces that I would like resolved that are visible from a different perspective (though they look to me like dependencies of stable).

I would like and environment in which change is easy to introduce. So I need to explain easy in this context. When I introduce the change I should be informed quickly if the change breaks anything and if it does what it broke so that I can fix it. So I need to explain quick and inform now. By quick I mean I don’t want to loose flow[2)](#fn__2) before I have to fix something. By inform I mean I want to know what method of what class is not behaving in the expected way or even what line is causing the error. These add up to make it easy to introduce change. A by product of such an environment is stability in the face of rapid change. So one could tie these together as dependency and dependant. Now we have common goals to evaluate the implementation of the pattern language in its ability to produce a system to attain our goals.

A Private Workspace is worth a little discussion. Notice in figure 1 how Private Workspace depends on Active Development. CI indirectly supports Private Workspace and it re-enforces the need for Development Workspace. It has a ripple effect on the entire system.

## Prerequisite Practices

The prerequisites of CI are often assumed and overlooked. Many of the prerequisites are common sense and you have always done them. There are those that do not follow these and it is worth listing them for those that do not practice them.

- Use of source control repository
- Perpetual synchronization with code line
- Automated unit tests
- Homogeneous development workspace structure
- Accretion development
- Lines of Communication

#### Source Control

The use of a source control repository should be a familiar to most[3)](#fn__3). There are many reasons to use a source control repository(repo). The only reason pertinent to CI is what we are interested in here: a single place to locate all resources that are needed to build the product. This will allow the build server to start fresh every build: simply by deleting the Development Workspace from the previous build and getting latest from the repo will recreate the Development Workspace.

#### Perpetual Synchronization

It is essential that developers keep there environments synchronized with the code line. The frequency of this synchronization can be an issue. If it is difficult to do this often then broken builds are likely to occur. In such a situation it the developer will likely have to get their Private Workspace upto date before they can even begin working on why the build broke. This can cause lengthy delays to the rest of the team wishing to submit to the build. The problem is why the developer did not synchronize, up date their Private Workspace, before submitting to the build. I would bet that in most cases the answer will be that synchronizing is a time consuming and possibly difficult process.

#### Automated Unit Tests

Automated unit testing is needed to verify that the code does what the developer intended it to. This insures that it is worth someone else’s time to work with. This could be a tester, another developer consuming the API, or a customer. Only working builds should be published[4)](#fn__4). Simply compiling the code does not inform as to the workability of the product. There needs to be some testing, automated testing with automated results verification, to determine the success for failure of the build. For those of you used to thinking of the word build as synonymous with compile those days are over. There are some very strict definitions of what and what isn’t a unit test out there. All that counts here is how it supports or inhibits CI. In that light some good qualities of unit tests are:

- They run fast.
- They help us localize problems.
- They do not require additional resources to be installed on the build server.
- They do not use external resources to the build server.
- They are self sufficient.

#### Homogeneous Development Workspace

A homogeneous development workspace structure is probably the most overlooked. There should be no variation between developer workspace structures, and the build server will use the developer workspace structure. This is implied in the Pattern Repository[5)](#fn__5). My experience is pushing me to extract [Development Workspace](/wiki/development-workspace/ "development_workspace") as an individual pattern.

| Development Workspace Patlet |
| --- |
| Context All developers and the Integration Build work in their own Private Workspaces yet there needs to be consistency between them. This pattern is a means to define the structure of the Private Workspace. Problem With many Private Workspaces how do you mitigate the chance that differences between them will cause bugs? Solution Define a structured workspace and location for it in private environments. Allow for variation in the content and not the structure. |

  

The more differences there are between a build’s private workspace and a developers private workspace the more chances there are for “works on my box”. When there are differences and a build attempt fails one must suspect the differences in workspaces as well as the changes submitted to the build. This significantly decreases one of the benefits of CI: error localization.

#### Accretion Development

Accretion development is the practice of growing a system through the application of small controlled changes. The Pattern Task Level Commit and Task Driven Development are good examples[6)](#fn__6). Much of the benefit of CI directly depends on the application of small controlled changes to the codeline. Some of these benefits are that when an integration fails there is only he small controlled change to suspect, as well as the fact the developer’s mind is full and focus on this change and not some other task. The idea here is not to loose flow. The cheapest time to identify bugs is during the developer’s initial flow. Being able to provide feed back without an interruption in flow is a wonderful goal, even better is achieving it.

#### Communication Lines

Team members need to have an established means to communicate that they are going to claim the build(only one person can integrate at a time). This can be as simple as a shout or as complex as setting the status of a ticket in a ticket system. There are many varieties to this, I am sure some are silly.

## Ingredients

Beyond the prerequisites success will depend on a few more ingredients.

- An adequately fast server (hardware)
- A CI server (software)
- A build script

#### Hardware

It is important that the build server be a independent machine: it can not be co-hosted on a developer’s machine. It will need to perform compilations, unit testing, and present build results from a web server. Please consider all the services that you will delegate to it. It is important that it have enough horse power to be responsive[7)](#fn__7).

#### Software

The are many continuous integration servers, these two seem most popular:

- [CruiseControl.NET](http://www.continuousintegration.net/ "http://www.continuousintegration.net/")
- [CruiseControl](http://cruisecontrol.sourceforge.net/ "http://cruisecontrol.sourceforge.net/")

A good comparison matrix can be found at [Codehaus](http://damagecontrol.codehaus.org/Continuous+Integration+Server+Feature+Matrix "http://damagecontrol.codehaus.org/Continuous+Integration+Server+Feature+Matrix"). The CI server has three main responsibilities: monitor for a trigger to perform the integration, execute the integration, and report on the integration. Triggers are normally a result of monitoring a SC repo for change. When a change occurs the trigger is set off (there is a bit more complication here to wait for you to get all your changes into the repo). One can also force the build, a manual trigger. The integration itself is farmed out to a build script. The results of the build script are gathered and published.

#### Script

The build script could be in any language you like. I suggest you select a scripting language that integrates well with the CI server you chose. The output of the script needs to be understandable by the publishing system of the CI server. The only other suggestion I have is to strongly consider committing to a language that will move with the industry and your needs. Ant and nAnt for example are likely to provide your future needs as it is their main charter to service builds. Additionally both CruiseControls anticipate it as their client scripting language.

## Technique

- Avoid sourdough, start by deleting the workspace used in the previous integration.
- When labeling after successful build label the everything not just the product code

  - Product Code
  - Build Scripts (yes they should be in SC too)
  - Test Code
  - Installer Code
  - What ever else you may be doing

## Build Responsibilities

There is one responsibility that I think is worth noting above all others: it must be **self sufficient**. This is an absolute must, with out it chances are the practice will fail. The responsibilities listed below aren’t necessarily in order, in some situation they may not be needed. View these as a list of possible responsibilities the build server will fulfill.

- Monitor for trigger

  - There are many reasons to trigger and these will depend on your objectives for you build server. The most common trigger is changes to source control.
- Cleanup and verify build enviroment
- Control version of product and artifacts
- Compile Debug configruation of product and test code
- Run tests
- Compile Release configuration of product code
- Compile installer
- Publish results and artifacts
- Trigger dependant builds
- Complete in about ten minutes[8)](#fn__8)

## Developer Responsibilities

The developer responsibilities listed below are in sequence of execution, order is important. This list starts off in the greater sequence of events where the developer has just completed the task at hand and is ready to be the build submission process.

1. Synchronize with the SC repo
2. Compile
3. Execute unit tests
4. Make fixes if needed
5. Claim the build (don’t forget to communicate if it’s a significant change)
6. Submit changes to the SC repo
7. Wait for the build result (do not start coding on somthing)
8. If the build result is success congratulations, if not fix it

## Make It Happen

This is the part were you run off and make the CI server and institute the practice, or at least pretend. When you’re done read the next part.

## Componentize

This is great, I have a instituted CI on a project. I have done this a few times and I have found that I am duplicating effort each time I go through the process of implementing CI on a project. Here we will isolate the commonality. More commonality can be identified by committing to a toolset. Here I have committed to the tools Visual Studio .NET, Visual Source Safe, CruiseControl.NET, nAnt, and MbUnit. Remember the following is not the only way. This has evolved into being and will continue to evolve.

### Development Workspace

What does not vary in a Development Workspace? No matter the problem domain the product exists in there is commonality in the Development Workspace (figure 2).

|  |
| --- |
| Figure 2 |

  

Other than the product name there need be no variation in this structure. All build related files, scripts, CI server software, will be placed in the Build directory. All installation code (i.e. InstallShield) will be placed in the Install directory. All product code will be placed in the Production directory. All unit testing code will be placed in the Unit Test directory. All third party code will be placed in the Third Party directory.

From here tool specifics will be added starting with the Build directory (figure 3).

|  |
| --- |
| Figure 3 |

  

As a result of having committed to a toolset we have parametrized scripts allowing for variation between products(the product you are building not the toolset products). Notice the file ProductName-Build.sln? This is a VS.NET solution file, it includes all the build scripts and configuration files. It is integrated with VSS as well. Remember to hold the build to the same standards as the product. The folder server contains the CCNET server software, dashboard contains the CCNET website. Each product and version have their own CCNET server/dashboard allowing for independent downtime and customization. All the scripts that do the compilation, unit testing, and everything else are organized into packages. The VS.NETCompile package is in focus in figure 4. The standardization that we are defining here will allow for scripts that need little to no customization. Preferably the target file(s) need not be altered, the properties files should be able to handle most customizations.

|  |
| --- |
| Figure 4 |

  

|  |
| --- |
| Figure 5 |

  

In figure 5 you can see another solution with the product name. This solution is for the product itself, containing the installer code, the unit test code, and yes of course the actual production code.

### CI Server Configuration

In the Cruise Control project configuration file. The only variation is the ProductName and the credintials for VSS. The resposiblities detailed in [Build Responsibilities](/wiki/a-recipe-for-build-maintainability-and-reusability/ "a_recipe_for_build_maintainability_and_reusability") handled by CCNET are listed below.

- Monitor for trigger
- Publish results and artifacts
- Trigger dependant builds

### Build Script

The resposiblities detailed in [Build Responsibilities](/wiki/a-recipe-for-build-maintainability-and-reusability/ "a_recipe_for_build_maintainability_and_reusability") handled by nAnt scripts are listed below.

- Cleanup and verify build enviroment
- Control version of product and artifacts
- Compile Debug configruation of product and test code
- Run tests
- Compile Release configuration of product code
- Compile installer

The script Main.build.xml handles order of execution of the other scripts. The package VisualSourceSafe handles cleanup and creation of the Development Workspace. Versioning handles versioning of the product and artifacts (the product version is maintained by CCNET and applied by the script). Compilation of production, unit test, and installer code is handled by the package VS.NETCompile. Unit tests are executed by the package DotNetUnitTest. I am sure that you get the picture. The open source project [CI Factory](http://www.mertner.com/confluence/display/CIF/CI+Factory+Home "http://www.mertner.com/confluence/display/CIF/CI+Factory+Home") put this into practice. You can take a look at it for a detailed example of how to implement this your self or you could just make use of CI Factory itself.

## Lather, Rinse, and Repeat

Now that we have some idea as to a repeatable process lets not loose it. Lets shared it. At the beginning of a new project the temptation is to start tinkering and producing code. There is very rarely focus on creating the environment needed to support CI. It would help if there were some general steps to help guide a new project. The first thing that needs to be determined is when the build server needs to be operational. The answer is just before you start any coding. Let this guide your determination of a due date for the build server. To get your environment prepared for CI follow these general steps.

1. Identify a Source Control Repository to be used.

   - This not only means the brand but includes the actual hardware, all the user accounts, everything needed for your team to access it.
2. Catalog the third part code that will be utilized by the project.
3. Create the Development Workspace structure in the Repository.
4. Identify or establish the Communication Lines needed.
5. Insure the work to be performed is sized for accretion development.
6. Create the integration or build server.

Note that there is no product code or unit tests when the integration build server is created. The Development Workspace defines where they will go and that should be all the build script needs(grant it the build won’t succeed). The project is primed and ready for development to begin. I could leave it at that but lets follow this a bit further. The developer creates a Private Workspace by importing the Development Workspace from the Repository. The developer goes on to create product code and unit test code all the while using Private Build System. When the developer has finished with a task they use the Communication Lines to inform of the impending integration build and then submits to the Repository triggering an Integration Build. Don’t forget this was a description of the very first submission of production and unit test code to the Repository. It is indistinguishable from any other Task Level Commit.

When a project does not begin in this fashion work must be stopped to implement CI. It is difficult to justify stopping progress.

## Appendix

[1)](#fnt__1)
Software Configuration Management Patterns: Effective Teamwork, Practical Integration

[2)](#fnt__2)
Peopleware : Productive Projects and Teams

[3)](#fnt__3)
[http://www.cmcrossroads.com/articles/mznov03.pdf](http://www.cmcrossroads.com/articles/mznov03.pdf "http://www.cmcrossroads.com/articles/mznov03.pdf")

[4)](#fnt__4)
[http://www.martinfowler.com/articles/continuousIntegration.html](http://www.martinfowler.com/articles/continuousIntegration.html "http://www.martinfowler.com/articles/continuousIntegration.html")

[5)](#fnt__5)
Software Configuration Management Patterns: Effective
Teamwork, Practical Integration

[6)](#fnt__6)
[http://www.cmcrossroads.com/ubbthreads/showflat.php?Cat=&Number=28269](http://www.cmcrossroads.com/ubbthreads/showflat.php?Cat=&Number=28269 "http://www.cmcrossroads.com/ubbthreads/showflat.php?Cat=&Number=28269")

[7)](#fnt__7)
, [8)](#fnt__8)
[http://www.thoughtworks.com/long-build-troubleshooting-guide.pdf](http://www.thoughtworks.com/long-build-troubleshooting-guide.pdf "http://www.thoughtworks.com/long-build-troubleshooting-guide.pdf")

a\_recipe\_for\_build\_maintainability\_and\_reusability.txt · Last modified: 2006/10/14 21:07 by jflowers
