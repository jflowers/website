---
title: "AsyncExec and WaitForExit: Speeding Up The Build To Do More"
date: "2006-12-03"
draft: false
categories:
  - "Continuous Integration"
aliases:
  - "/WordPress/?p=101"
  - "/WordPress/index.php?p=101"
params:
  wayback_url: "https://web.archive.org/web/20070903202329/http://jayflowers.com:80/WordPress/?p=101"
  original_url: "http://jayflowers.com:80/WordPress/?p=101"
  archived_from: Wayback Machine

---

## AsyncExec and WaitForExit: Speeding Up The Build To Do More

I have been working to bring the build time for our developer facing build to something less than 5 minutes.  I recently got it to less than 5.  Currently it does none of the nice fancy stuff like run Simian, NDepend, or FXCop.  I have been experimenting with an extended exec task: asynexec.  It wraps the core exec task starting base.ExecuteTask in a new thread.  It has one additional attribute that must be set: taskname.  Taskname is used to track the thread.  This enables the other task that I created: waitforexit.  These two tasks can be used in concert like so:


```xml
<asyncexec taskname=“UnitTests“
```


      program=“${NantProcess}“

      failonerror=“False“

      resultproperty=“UnitTestsResult“>


```xml
  <arg line=“-buildfile:.\Packages\MSTest\UnitTest.Target.xml“/>
```



```xml
  <arg line=‘@”${Common.PropertiesFile}”‘ />
```



```xml
  <arg line=“UnitTest.RunTests“/>
```



```xml
  <arg line=“-logger:NAnt.Core.XmlLogger“/>
```



```xml
  <arg line=‘-logfile:”${Common.ReportDirectory}\UnitTests.xml”‘ />
```



```xml
</asyncexec>
```



```xml
<waitforexit>
```



```xml
  <tasknames>
```



```xml
    <string value=“UnitTests“/>
```



```xml
  </tasknames>
```



```xml
</waitforexit>
```



```xml
<if test=“${int::parse(UnitTestsResult) != 0}“>
```



```xml
  <fail message=“Atleast one unit test failed!“/>
```



```xml
</if>
```


Functionally this will behave the same as simply calling that task exec.  Things get interesting when you start doing more:


```xml
<asyncexec taskname=“UnitTests“ program=“${NantProcess}“ failonerror=“False“ resultproperty=“UnitTestsResult“>
```



```xml
  <arg line=“-buildfile:.\Packages\MSTest\UnitTest.Target.xml“/>
```



```xml
  <arg line=‘@”${Common.PropertiesFile}”‘ />
```



```xml
  <arg line=“UnitTest.RunTests“/>
```



```xml
  <arg line=“-logger:NAnt.Core.XmlLogger“/>
```



```xml
  <arg line=‘-logfile:”${Common.ReportDirectory}\UnitTests.xml”‘ />
```



```xml
</asyncexec>
```



```xml
<asyncexec taskname=“Simian“ program=“${NantProcess}“ failonerror=“False“>
```



```xml
  <arg line=“-buildfile:.\Packages\Simian\Simian.Target.xml“/>
```



```xml
  <arg line=‘@”${Common.PropertiesFile}”‘ />
```



```xml
  <arg line=“Simian.Run“/>
```



```xml
  <arg line=“-logger:NAnt.Core.XmlLogger“/>
```



```xml
  <arg line=‘-logfile:”${Common.ReportDirectory}\Simian.xml”‘ />
```



```xml
</asyncexec>
```



```xml
<asyncexec taskname=“NDepend“ program=“${NantProcess}“ failonerror=“False“>
```



```xml
  <arg line=“-buildfile:.\Packages\NDepend\NDepend.Target.xml“/>
```



```xml
  <arg line=‘@”${Common.PropertiesFile}”‘ />
```



```xml
  <arg line=“nDepend.Calculate“/>
```



```xml
  <arg line=“-logger:NAnt.Core.XmlLogger“/>
```



```xml
  <arg line=‘-logfile:”${Common.ReportDirectory}\NDepend.xml”‘ />
```



```xml
</asyncexec>
```



```xml
<waitforexit>
```



```xml
  <tasknames>
```



```xml
    <string value=“Simian“/>
```



```xml
    <string value=“UnitTests“/>
```



```xml
    <string value=“NDepend“/>
```



```xml
  </tasknames>
```



```xml
</waitforexit>
```



```xml
<if test=“${int::parse(UnitTestsResult) != 0}“>
```



```xml
  <fail message=“Atleast one unit test failed!“/>
```



```xml
</if>
```


 This saved about 35 seconds on our build server from the old way:


```xml
<call target=“UnitTest.RunTests“/>
```



```xml
<call target=“Simian.Run“/>
```



```xml
<call target=“nDepend.Calculate“/>
```


I spent some time playing around with how best to use this.  We use CI Factory on this project.  I bring this up because it will give some background to how the build script is setup.  There is a target analogous to sub Main.  In this Main target targets from Packages are called.  The table below contains timing information about those targets:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Asynchronous | | Asynchronous | | Synchronous | |
| Target | Seconds | Minutes | Seconds | Minutes | Seconds | Minutes |
| nDepend.Calculate | 166.5 | 02:46 |
| Simian.Run | 118.17 | 01:58 | 53.81 | 00:53 |
| Compile.CompileSource | 95.89 | 01:35 | 81.47 | 01:21 | 84.98 | 01:24 |
| UnitTest.RunTests | 87.95 | 01:27 | 31.47 | 00:31 | 20.3 | 00:20 |
| SourceControl.GetOfProductDirectory | 14.47 | 00:14 | 15.78 | 00:15 | 15.11 | 00:15 |
| Tracker.Queries | 9.28 | 00:09 | 9.75 | 00:09 | 8.94 | 00:08 |
| Tracker.MoveTrackersTo | 8.67 | 00:08 | 5.39 | 00:05 | 5.95 | 00:05 |
| Tracker.Report | 2.89 | 00:02 | 3.83 | 00:03 | 3.97 | 00:03 |
| SourceControl.GetOfThirdPartyDirectory | 1.28 | 00:01 | 2.53 | 00:02 | 1.06 | 00:01 |
| SetUp | 1.59 | 00:01 | 1.64 | 00:01 | 0.89 | 00:00 |
| SourceModificationReport.ConsolidateReports | 0.97 | 00:00 | 1.16 | 00:01 | 0.95 | 00:00 |
| TearDown | 0.3 | 00:00 | 0.22 | 00:00 | 0.17 | 00:00 |
| Actual Total | 299.45 | 04:59 | 174.81 | 02:54 | 144.09 | 02:24 |
| Total If Synchronous | 507.96 | 08:27 | 207.05 | 03:27 |
| Time Saved | 208.51 | 03:28 | 32.24 | 00:32 |

Like colored targets are executed at the same time.  I ran the scripts many times to get a feel for any variance.  The data above are from mean runs.  Things looked pretty good until I added NDepend.  This could be because it is an expensive operation and or that I had the script executing the unit tests and Simian at the same time (it is only dual proc).

A few posts ago I talked about a post build nant script; one that CCNET ran after the log publisher task.  I have used the asyncexec task there too but in slightly different way.  It is not waiting for an exit.  There is no need to complete the work in the post build script before starting on a new build.  I think that NDepend could be moved to the post build script.  This would let us gain both NDepend and Simian for a sum total of 30+ seconds (note this is only accurate if another build does not start immediately).  Not a bad price.

Below is the nant script main target.  It has been color coded to match the table above.


```xml
<target name=“Triggered“ depends=“SetUps“ >
```


  <trycatch>

    <try>


```xml
      <description>Begin Main Build</description>
```



```xml
      <description>Begin Pre Build Actions</description>
```



```xml
      <call target=“SourceModificationReport.ConsolidateReports“ />
```



```xml
      <call target=“Tracker.Queries“ />
```



```xml
<asyncexec taskname=“TrackerReport“ program=“${NantProcess}“ failonerror=“False“>
```



```xml
        <arg line=“-buildfile:.\Packages\VisualSourceSafe\VSS.Target.xml“/>
```



```xml
        <arg line=‘@”${Common.PropertiesFile}”‘ />
```



```xml
        <arg line=“Tracker.Report“/>
```



```xml
        <arg line=“-D:Tracker.QueryScrList=${Tracker.QueryScrList}“ />
```



```xml
        <arg line=“-logger:NAnt.Core.XmlLogger“/>
```



```xml
        <arg line=‘-logfile:”${Common.ReportDirectory}\TrackerReport.xml”‘ />
```



```xml
      </asyncexec>
```



```xml
      <description>End Pre Build Actions</description>
```



```xml
      <description>Begin Clean Up Actions</description>
```



```xml
<asyncexec taskname=“GetOfThirdPartyDirectory“ program=“${NantProcess}“ failonerror=“False“
```


                resultproperty=“GetOfThirdPartyDirectoryResult“>


```xml
        <arg line=“-buildfile:.\Packages\VisualSourceSafe\VSS.Target.xml“/>
```



```xml
        <arg line=‘@”${Common.PropertiesFile}”‘ />
```



```xml
        <arg line=“SourceControl.GetOfThirdPartyDirectory“/>
```



```xml
        <arg line=“-logger:NAnt.Core.XmlLogger“/>
```



```xml
        <arg line=‘-logfile:”${Common.ReportDirectory}\GetOfThirdPartyDirectory.xml”‘ />
```



```xml
      </asyncexec>
```



```xml
<call target=‘SourceControl.GetOfProductDirectory‘/>
```



```xml
      <waitforexit>
```



```xml
        <tasknames>
```



```xml
<string value=“GetOfThirdPartyDirectory“/>
```



```xml
        </tasknames>
```



```xml
      </waitforexit>
```



```xml
      <if test=“${int::parse(GetOfThirdPartyDirectoryResult) != 0}“>
```



```xml
        <fail message=“Get latest of the Third Party directory failed!“/>
```



```xml
      </if>
```



```xml
      <description>End Clean Up Actions</description>
```



```xml
      <description>Begin Compile Actions</description>
```



```xml
      <touch millis=“1“ verbose=“true“>
```



```xml
        <fileset>
```



```xml
          <include name=“${ProductDirectory}\ProjectInfo.\*“/>
```



```xml
          <include name=“${ProductDirectory}\\*\*\AssemblyInfo.\*“/>
```



```xml
        </fileset>
```



```xml
      </touch>
```



```xml
      <delete dir=“${Compile.Bin}“ if=“${directory::exists(Compile.Bin)}“ />
```



```xml
      <call target=“Compile.CompileSource“ />
```



```xml
      <description>End Compile Actions</description>
```



```xml
      <description>Begin Varification Actions</description>
```



```xml
<asyncexec taskname=“NDepend“ program=“${BuildDirectory}\nAnt\bin\nant.exe“ failonerror=“False“>
```



```xml
        <arg line=“-buildfile:.\Packages\NDepend\NDepend.Target.xml“/>
```



```xml
        <arg line=‘@”${Common.PropertiesFile}”‘ />
```



```xml
        <arg line=“nDepend.Calculate“/>
```



```xml
        <arg line=“-logger:NAnt.Core.XmlLogger“/>
```



```xml
        <arg line=‘-logfile:”${Common.ReportDirectory}\NDepend.xml”‘ />
```



```xml
      </asyncexec>
```



```xml
<asyncexec taskname=“UnitTests“ program=“${NantProcess}“ failonerror=“False“ resultproperty=“UnitTestsResult“>
```



```xml
        <arg line=“-buildfile:.\Packages\MSTest\UnitTest.Target.xml“/>
```



```xml
        <arg line=‘@”${Common.PropertiesFile}”‘ />
```



```xml
        <arg line=“UnitTest.RunTests“/>
```



```xml
        <arg line=“-logger:NAnt.Core.XmlLogger“/>
```



```xml
        <arg line=‘-logfile:”${Common.ReportDirectory}\UnitTests.xml”‘ />
```



```xml
      </asyncexec>
```



```xml
<asyncexec taskname=“Simian“ program=“${NantProcess}“ failonerror=“False“>
```



```xml
        <arg line=“-buildfile:.\Packages\Simian\Simian.Target.xml“/>
```



```xml
        <arg line=‘@”${Common.PropertiesFile}”‘ />
```



```xml
        <arg line=“Simian.Run“/>
```



```xml
        <arg line=“-logger:NAnt.Core.XmlLogger“/>
```



```xml
        <arg line=‘-logfile:”${Common.ReportDirectory}\Simian.xml”‘ />
```



```xml
      </asyncexec>
```



```xml
      <waitforexit>
```



```xml
        <tasknames>
```



```xml
<string value=“UnitTests“/>
```



```xml
        </tasknames>
```



```xml
      </waitforexit>
```



```xml
      <if test=“${int::parse(UnitTestsResult) != 0}“>
```



```xml
        <fail message=“Atleast one unit test failed!“/>
```



```xml
      </if>
```



```xml
      <description>End Varification Actions</description>
```



```xml
      <description>Begin Post Build Actions</description>
```



```xml
      <call target=“Tracker.MoveTrackersTo“/>
```



```xml
      <waitforexit>
```



```xml
        <tasknames>
```



```xml
<string value=“Simian“/>
```



```xml
          <string value=“NDepend“/>
```



```xml
<string value=“TrackerReport“/>
```



```xml
        </tasknames>
```



```xml
      </waitforexit>
```



```xml
      <description>End Post Build Actions</description>
```



```xml
      <description>End Main Build</description>
```



```xml
    </try>
```



```xml
    <finally>
```



```xml
      <call target=“TearDowns“/>
```



```xml
    </finally>
```



```xml
  </trycatch>
```



```xml
</target>
```


**Download these tasks and more in** [**NAnt Stuff**](http://jayflowers.com/joomla/index.php?option=com_remository&Itemid=33&func=select&id=2)**.**




|

|
