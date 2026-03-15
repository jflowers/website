---
title: NCover/NCoverExplorer CI Factory Package Release
date: "2006-09-03"
draft: false
categories:
  - "Continuous Integration"
  - "Unit Testing"
aliases:
  - "/WordPress/?p=70"
  - "/WordPress/index.php?p=70"
params:
  wayback_url: "https://web.archive.org/web/20061122001225/http://jayflowers.com:80/WordPress/?p=70"
  original_url: "http://jayflowers.com:80/WordPress/?p=70"
  archived_from: Wayback Machine

---

## NCover/NCoverExplorer CI Factory Package Release

So with the release of NCover ([1.5.5](http://ncover.org/SITE/blogs/ncover_blog/archive/2006/09/01/550.aspx)) I feel that I can release the NCover package for CI Factory.  It includes a copy of NCoverExplorer and uses NCoverExplorer Extras.  I got a lot of help from [Grant Drake](http://www.kiwidude.com/blog/) to create to this package.  He mentioned this in a [post](http://www.kiwidude.com/blog/2006/07/nant-and-msbuild-tasks-for-ncover.html) in July.  The project that I made this package for is using .NET 2.0 /w Generics so I had to what for the 1.5.5 release for Generics support.  I will be on vacation for the next two weeks so I doubt that it will be applied to the build servers at work until I get back.  Point being that the package has not really been through prime time (currently works on my box ![;-)](http://jayflowers.com/WordPress/wp-includes/images/smilies/icon_wink.gif) ).

The project I am helping with CI and automated unit testing might be interesting for some folks.  It is the, as in the only, Electronic Medical Record (EMR) for the US DoD.  They have decided to use MSTest and are working to include more features of VSTS.  Currently VSTS server is not in the mix.  So we are using CI Factory (CCNET and NAnt) to do the builds.  I have looked at the build functionality in VSTS and feel that it is less than CCNET.  The MSBuild vs NAnt does seem to be a worth while discussion any more, it is a personal preference thing now.  CCNET is far easier to extend than VSTS.  VSTS has hard and fast extension points were as if the extension point does not exist in CCNET you can create it.  For instance I am close to finishing a custom release of CCNET 1.0 that includes Force Filters and Integration Filters.  More on that in a future post.  Any way I found that NCover was a better choice for code coverage in the build process than MSTest’s built in coverage capability.  This is because MSTest uses instrumentation to collect coverage information.  The instrumentation takes time that NCover does not need.  Time in a build is a precious thing so I did not see the need to waste it when I had a superior product NCover/NCoverExplorer at hand.

In the properties file of the package you need to choose which unit testing package you will be using (MSTest or MbUnit/NUnit).  The options are listed in the files (unless you are going to write your own package).  You might need to customise the assemblies NCover will include; the default is ${ProjectName}.\*.dll.  In the Main.build.xml you just need to substitute the include of the unit test package with the NCover package.  That might seem a little weird.  The coverage packages impersonate the unit test package.  The coverage package will execute the unit test package in a separate process.  That is the only way coverage can be gathered, from a separate process.  It seemed the easiest thing to do was impersonate the unit test package so that the Main.build.xml would be impacted very little.  As well the unit test package has no clue that it is not being run by Main.build.xml, so it is not impacted at all.  All unit test packages, existing and future, that comply with the unit test package interface will work with both the NCover and CoverageEye packages.  Pretty cool if I do say so; it is kinda OOish.  To be clear, if you get into a situation where you need to do some trouble shooting, NCover is executing NAnt.  Nant is executing the unit test package’s UnitTest.Target.xml’s target UnitTest.Run.  This works because the unit tests are being executed in the NAnt process.  For the MSTest unit test package I created a NAnt task that drives the VSTS class that execute the MSTests.  For the other unit test package MbUnit’s NAnt task will run MBunit tests as well as NUnit tests.  Neither task is shelling out to another process.

**You will need to install NCover, you don’t need to install NCoverExplorer.**  Maybe in the future I will work out how to use a .manifest file so that the NCover COM component does not need to be registered.

**If you are already using CI Factory:**

**1.** Unzip to the packages dir

**2.** Set the two properties mentioned above in the properties file

**3.** Switch to unit test package include for the NCover package in the Main.build.xml

**4.** Edit the dashboard.config and maybe the ccnet.exe.config (are you using the email publisher?) to include the xsls NCoverExplorer.xsl and NCoverExplorerSummary.xsl


```xml
<buildPlugins>  
  <buildReportBuildPlugin>  
    <xslFileNames>  
      <xslFile>xsl\header.xsl</xslFile>  
      <xslFile>xsl\modifications.xsl</xslFile>  
      <xslFile>Packages\VisualSourceSafe\ShowAllChanges.xsl</xslFile>  
      <xslFile>Packages\Deployment\deployment.xsl</xslFile>  
      <xslFile>Packages\Tracker\Tracker.xsl</xslFile>  
      <xslFile>xsl\compile.xsl</xslFile>  
      <xslFile>Packages\NCover\NCoverExplorerSummary.xsl</xslFile>  
      <xslFile>Packages\MSTest\MsTestSummary.xsl</xslFile>  
    </xslFileNames>  
  </buildReportBuildPlugin>  
  <buildLogBuildPlugin />  
  <xslReportBuildPlugin description=“NAnt Output“ actionName=“NAntOutputBuildReport“ xslFileName=“xsl\Nant.xsl“ />  
  <xslReportBuildPlugin description=“NAnt Timings“ actionName=“NAntTimingsBuildReport“ xslFileName=“xsl\NantTiming.xsl“ />  
  <xslReportBuildPlugin description=“.NET Compile Details“ actionName=“DevEnvCompileDetails“ xslFileName=“Packages\VS.NETCompile\DevEnvCompileDetails.xsl“ />  
  <xslReportBuildPlugin description=“NCover Report“ actionName=“NCoverBuildReport“ xslFileName=“Packages\NCover\NCoverExplorer.xsl“ />  
</buildPlugins>
```

**5.** Edit the ccnetproject.xml to merge <your projects location>\Build\CoverageReports\CoverageReport.xml


```xml
<publishers>  
  <merge>  
    <files>  
      <file>c:\Projects\dod.ahlta\Current\Build\Tracker Reports\\*.xml</file>  
      <file>c:\Projects\dod.ahlta\Current\Build\CompileLogs\\*.xml</file>  
      <file>c:\Projects\dod.ahlta\Current\Build\VSS\ThirdPartyChanges.xml</file>  
      <file>c:\Projects\dod.ahlta\Current\Build\VSS\ProductChanges.xml</file>  
      <file>c:\Projects\dod.ahlta\Current\Build\Unit Test Reports\\*.xml</file>  
      <file>c:\Projects\dod.ahlta\Current\Build\CoverageReports\CoverageReport.xml</file>  
    </files>  
  </merge>  
  <xmllogger />  
```

  &email;  

```xml
</publishers>
```

[**Download**](http://jayflowers.com/joomla/index.php?option=com_remository&Itemid=33&func=select&id=12)




|

|
