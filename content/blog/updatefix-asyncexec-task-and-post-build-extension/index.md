---
title: Update/Fix AsyncExec Task and Post Build Extension
date: "2007-03-09"
draft: false
categories:
  - "Continuous Integration"
  - "CI Factory"
aliases:
  - "/WordPress/?p=117"
  - "/WordPress/index.php?p=117"
params:
  wayback_url: "https://web.archive.org/web/20070904121145/http://jayflowers.com:80/WordPress/?p=117"
  original_url: "http://jayflowers.com:80/WordPress/?p=117"
  archived_from: Wayback Machine

---

## Update/Fix AsyncExec Task and Post Build Extension

In a [previous post](http://jayflowers.com/WordPress/?p=101) I introduced the task [AsyncExec](http://ci-factory.googlecode.com/svn/Current/Product/Production/Common/Common.Tasks/AsyncExec.vb).  For the way I was using it in that post it worked great.  I hinted at using it to execute a process, letting the child process continue after the parent had exited.  The task was not in fact capable of this.  The ancestor task [ExternalProgramBase](http://nant.cvs.sourceforge.net/nant/nant/src/NAnt.Core/Tasks/ExternalProgramBase.cs?view=markup) spawned two threads for collecting the Standard Out and Error Out streams.  These threads as well as the one spawned for calling the base method ExecuteTask were not background threads.  These three threads plus the call to WaitForExit on the System.Diagnostics.Process object were causing the parent process to hang around.  So four things needed to be addressed to allow for the desired behavior.

I ended up replacing some of the ancestor functionality and spawning no new threads.  I manage the process and when or whether to wait for it to exit.  This uses much fewer resources and in turn is much faster.

One of the key things to note is that the output attribute does not work.  Take the example for the exec task in the NAnt docs, ping.  You could add the output attribute to this and quickly have a log of the command.  I decided not to try and figure out if this task was going to complete before or after the parent process so you will need a shim process to redirect output to a file.  This can easily be done with cmd and >.


```xml
<target name=“test“>

  <delete file=“C:\temp\ping.txt“ if=“${file::exists(’C:\temp\ping.txt’)}“ />

  <asyncexec program=“cmd.exe“

            commandline=“/C ping 192.168.1.3 > C:\temp\ping.txt“

            taskname=“ping“

            resultproperty=“ping“

            failonerror=“false“

            verbose=“true“ />

  <asyncexec program=“notepad.exe“ waitforexit=“false“ />

  <waitforexit>

    <tasknames>

      <string value=“ping“/>

    tasknames>
```

  waitforexit>


```xml
  <echo message=“The exit code for pinging 192.168.1.3 was ${ping}.“/>

  <loadfile file=“C:\temp\ping.txt“ property=“output“ />

  <echo message=“${output}“/>
```

target>

This script will begin executing the ping command and continue on to opening notepad before the ping command has finished.  The ping command is being piped to the file ‘c:\temp\ping.txt’.  Here is the example scripts output:

test:

[delete] Deleting file C:\temp\ping.txt.  
[asyncexec] Starting ‘cmd.exe (/C ping 192.168.1.3 > C:\temp\ping.txt)’ in ‘C:\Projects\CI Factory\Current\Product\nAnt Scratch’  
[asyncexec] Starting ‘notepad.exe ()’ in ‘C:\Projects\CI Factory\Current\Product\nAnt Scratch’  
[asyncexec] C:\Projects\CI Factory\Current\Product\nAnt Scratch\Scratch.build.xml(9,6):  
[asyncexec] External Program Failed: cmd.exe (return code was 1)  
[echo] The exit code for pinging 192.168.1.3 was 1.  
[echo]  
[echo] Pinging 192.168.1.3 with 32 bytes of data:  
[echo]  
[echo] Request timed out.  
[echo] Request timed out.  
[echo] Request timed out.  
[echo] Request timed out.  
[echo]  
[echo] Ping statistics for 192.168.1.3:  
[echo] Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),  
[echo]

BUILD SUCCEEDED - 1 non-fatal error(s), 0 warning(s)

Total time: 21.3 seconds.

I have been working a good bit with the Post Build extension for [CI Factory](http://cifactory.org); I mention this in my post about the [Backup Package](http://jayflowers.com/WordPress/?p=111).  While getting this fine tuned I noticed the Post Shim continued to execute until the Post Build completed.  This of course defeated at least half the purpose of the Post Build and even more of the Post Shim.  The improvements that I have made to the asyncexec task forced a small change to the Post Shim as you can see here:


```xml
<asyncexec taskname=“PostBuild“ waitforexit=“false“ program=“${NantExePath}“ failonerror=“false“>

  <arg line=“-buildfile:Post.Build.xml“/>

  <arg line=‘-logger:NAnt.Core.XmlLogger‘ />

  <arg line=‘-logfile:”${Common.ArtifactDirectoryPath}\postbuildlog.xml”‘ />

  <arg line=‘@”${Common.PropertiesFile}”‘ />

  <arg line=‘-D:CCNetLogFilePath=”${CCNetLogFilePath}”‘ />

  <arg line=“${CCNetForcedByArg}“ />

  <arg line=“PostBuild“/>
```

asyncexec>

The attribute taskname used to be required, but now is not, and there is a new attribute waitforexit. Waitforexit’s default is true, meaning that the parent process will not exit until the child process has exited. There is a relationship between waitforexit and taskname. Taskname is used to invoke the task waitforexit. Allowing you to determine when to wait in the script. So if you want to wait later in the script, as in the ping example, set the taskname to something and the waitforexit attribute of asyncexec to true. When the waitforexit is set to true, and the taskname is not set, the task will not act asynchronously, it will wait for the child process to exit before continuing. If you set the waitforexit attribute to false, and then do not set the taskname attribute, the process will be spawned with a completely independent life from the parent’s.  Basicaly you want to either set the attribute waitforexit to false or set the taskname and call the waitforexit task.

**Here are the bits:**

[**NAnt Stuff**](http://jayflowers.com/joomla/index.php?option=com_remository&Itemid=33&func=select&id=2)

**Post Build Extension** [**Zip**](http://code.google.com/p/ci-factory/downloads/detail?name=Post-Build-Extension-v2.zip&can=2&q=) **and** [**Doc**](http://groups-beta.google.com/group/CI-Factory/web/Post+Build?hl=en&_done=%2Fgroup%2FCI-Factory%2Fweb%2FPost%2BBuild%3Fmsg%3Dns%26hl%3Den)

**Source for asyncexec and waitforexit** [**Async.Tasks.zip**](http://www.jayflowers.com/Misc%20Downloads/Async.Tasks.zip)




|

|
