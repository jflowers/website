---
title: Polish Your Build
date: "2007-10-01"
draft: false
categories:
  - "Continuous Integration"
  - "CI Factory"
aliases:
  - "/WordPress/?p=192"
  - "/WordPress/index.php?p=192"
params:
  wayback_url: "https://web.archive.org/web/20071021044624/http://jayflowers.com:80/WordPress/?p=192"
  original_url: "http://jayflowers.com:80/WordPress/?p=192"
  archived_from: Wayback Machine

---

## Polish Your Build

I think one of the reasons that I have had great success with [CI Factory](http://www.cifactory.org) when introducing teams to CI is polish, or ease of use.  Some of that polish comes with CI Factory out of the box, this post is about that extra that I have found myself adding of late.

I like to provide a script that will get developers all setup from the get go.  Recently I have found the best place to locate this script to be on the CCNet dashboard.

![CropperCapture[1]](images/2007/10/CropperCapture%5B1%5D1.png)

The workspace setup script should check for the needed source control client, create the directory structure needed, and get the latest from the source control repository.  Lastly it opens a Windows Explorer window to the Product directory:

![CropperCapture[22]](images/2007/10/CropperCapture%5B22%5D.png)

From here the developer can run a build by double clicking the Build.bat.  I have gotten to including a check for required software at the beginning of the personal build.  For example if Visual Studio 2005 SP1 is required I check for it and prompt the developer about it if missing.  Where possible I have the script install missing software with the developers permission.

![CropperCapture[23]](images/2007/10/CropperCapture%5B23%5D.png)

Once all the required software checks pass the rest of the build runs as normal.  The last bit to be polished is the cctray install.  In CI Factory the cctray download is a zip not a setup.exe.  I like to turn this into a self extracting zip and include a pre-configured settings.xml file.  This way when cctray starts up for the first time it is already configured.

In my experience these things leave developers the head room to focus on things that deserve their attention.  Communicating this through actions like polish go a long way to demonstrating how CI can have an affect on the quality of their lives.

To add download links to the main web dashboard edit the file:


```batch
C:\Projects\<project name>\Current\Build\dashboard\templatesFarmSideBar.vm

<table width=“100%“>

  #foreach ($link in $links)

  <tr><td><a href=“$link.Url“ class=“$link.LinkClass“>$link.Text</a></td></tr>

  #end

  <tr>

    <td>

      <a href=“WorkspaceSetup/CreateWorkspace.bat.txt“ >

        Workspace Setup Script

        <br/>Save As .bat

      </a>

    </td>

  </tr>

</table>
```

Here is an example of some NAnt script added to the personal build that checks for VS 2005 SP1:

```
<property name=“VisualStudioServicePack“ value=“”/>

<readregistry hive=“LocalMachine“                 

              key=“SOFTWAREMicrosoftDevDivVSServicing8.0SP“

              property=“VisualStudioServicePack“ failonerror=“false“/>


<ifnot test=“${VisualStudioServicePack == ‘1′}“>

  <ask answer=“Answer“

      question=“It looks like Visual Studio 2005 SP1 is not installed.  Do you wish to continue?“

      caption=“Proceed Without Required Software?“

      showdialog=“true“ >

    <options>

      <string value=“Continue“/>

      <string value=“Stop and Install SP1“/>

      <string value=“Exit“/>

    </options>

  </ask>

  <ifthenelse test=“${Answer == ‘Stop and Install SP1′}“>

    <then>

      <asyncexec program=“cmd“

      commandline=‘/C ” explorer http://msdn2.microsoft.com/en-us/vstudio/bb265237.aspx”‘

          createnowindow=“true“

          redirectoutput=“false“

          useshellexecute=“true“

          waitforexit=“false“ />

      <fail message=“Installing VS 2005 SP1!“ />

    </then>

    <elseif if=“${Answer == ‘Exit’}“>

      <fail message=“Please install VS 2005 SP1!“ />

    </elseif>

  </ifthenelse>

</ifnot>
```

The batch file for creating the workspace is a little clunky compared to NAnt script.  I have been mulling around the idea of including NAnt in a self extracting zip and executing a script instead of this batch file fun:


```batch
echo off  
set ProjectName=CI Factory  
set ProjectCodeLineName=Current  
set ProjectCodeLineDirectory=C:\Projects\%ProjectName%\%ProjectCodeLineName%  
set ProductDirectory=%ProjectCodeLineDirectory%\Product  
set SVN.URL=<https://ci-factory.googlecode.com/svn/%ProjectCodeLineName%>
```

mkdir “%ProjectCodeLineDirectory%”


```batch
SET /P Anonymous=”Do you wish to do an anonymous checkout of the source? Yes for patch creators, No for submitters:(y,n)”

IF %Anonymous%==y set SVN.URL=<http://ci-factory.googlecode.com/svn/%ProjectCodeLineName%>

IF EXIST “%ProgramFiles%\TortoiseSVN\bin\TortoiseProc.exe” GOTO UseTortoise
```

svn –version  

```batch
IF NOT %ERRORLEVEL%==0 (set PATH=%PATH%;%ProgramFiles%\Subversion\bin) ELSE GOTO UseSubversion
```

svn –version  

```batch
IF NOT %ERRORLEVEL%==0 (set PATH=%PATH%;%ProgramFiles%\CollabNet Subversion Server\bin) ELSE GOTO UseSubversion
```

svn –version  

```batch
IF %ERRORLEVEL%==0 (GOTO UseSubversion) ELSE GOTO NoSubversion

:UseSubversion  
IF %Anonymous%==n SET /P SvnUserName=”What is the user name you wish to use to checkout the source?”

set Credentials=  
IF DEFINED SvnUserName set Credentials=–username “%SvnUserName%”
```

svn checkout %Credentials% “%SVN.URL%” “%ProjectCodeLineDirectory%”


```batch
IF %ERRORLEVEL%==0 (GOTO OpenFolder) ELSE GOTO END

:NoSubversion  
echo I can’t find where you have Subversion installed!  
GOTO END

:UseTortoise  
```

“%ProgramFiles%\TortoiseSVN\bin\TortoiseProc.exe” /command:checkout /url:”%SVN.URL%” /path:”%ProjectCodeLineDirectory%”


```batch
IF %ERRORLEVEL%==0 (GOTO OpenFolder) ELSE GOTO END

:OpenFolder  
```

explorer “%ProductDirectory%”


```batch
:END
```
