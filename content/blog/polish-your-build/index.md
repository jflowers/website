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

C:\Projects\<project name>\Current\Build\dashboard\templatesFarmSideBar.vm

```csharp
<table width=“100%“>
```

```csharp
  #foreach ($link in $links)
```

```csharp
  <tr><td><a href=“$link.Url“ class=“$link.LinkClass“>$link.Text</a></td></tr>
```

```csharp
  #end
```

```csharp
  <tr>
```

```csharp
    <td>
```

```csharp
      <a href=“WorkspaceSetup/CreateWorkspace.bat.txt“ >
```

```csharp
        Workspace Setup Script
```

```csharp
        <br/>Save As .bat
```

```csharp
      </a>
```

```csharp
    </td>
```

```csharp
  </tr>
```

```csharp
</table>
```

Here is an example of some NAnt script added to the personal build that checks for VS 2005 SP1:

```csharp
<property name=“VisualStudioServicePack“ value=“”/>
```

```csharp
<readregistry hive=“LocalMachine“                 
```

```csharp
              key=“SOFTWAREMicrosoftDevDivVSServicing8.0SP“
```

```csharp
              property=“VisualStudioServicePack“ failonerror=“false“/>
```

```csharp
 
```

```csharp
<ifnot test=“${VisualStudioServicePack == ‘1′}“>
```

```csharp
  <ask answer=“Answer“
```

```csharp
      question=“It looks like Visual Studio 2005 SP1 is not installed.  Do you wish to continue?“
```

```csharp
      caption=“Proceed Without Required Software?“
```

```csharp
      showdialog=“true“ >
```

```csharp
    <options>
```

```csharp
      <string value=“Continue“/>
```

```csharp
      <string value=“Stop and Install SP1“/>
```

```csharp
      <string value=“Exit“/>
```

```csharp
    </options>
```

```csharp
  </ask>
```

```csharp
  <ifthenelse test=“${Answer == ‘Stop and Install SP1′}“>
```

```csharp
    <then>
```

```csharp
      <asyncexec program=“cmd“
```

```csharp
      commandline=‘/C ” explorer http://msdn2.microsoft.com/en-us/vstudio/bb265237.aspx”‘
```

```csharp
          createnowindow=“true“
```

```csharp
          redirectoutput=“false“
```

```csharp
          useshellexecute=“true“
```

```csharp
          waitforexit=“false“ />
```

```csharp
      <fail message=“Installing VS 2005 SP1!“ />
```

```csharp
    </then>
```

```csharp
    <elseif if=“${Answer == ‘Exit’}“>
```

```csharp
      <fail message=“Please install VS 2005 SP1!“ />
```

```csharp
    </elseif>
```

```csharp
  </ifthenelse>
```

```csharp
</ifnot>
```

The batch file for creating the workspace is a little clunky compared to NAnt script.  I have been mulling around the idea of including NAnt in a self extracting zip and executing a script instead of this batch file fun:

echo off  
set ProjectName=CI Factory  
set ProjectCodeLineName=Current  
set ProjectCodeLineDirectory=C:\Projects\%ProjectName%\%ProjectCodeLineName%  
set ProductDirectory=%ProjectCodeLineDirectory%\Product  
set SVN.URL=<https://ci-factory.googlecode.com/svn/%ProjectCodeLineName%>

mkdir “%ProjectCodeLineDirectory%”

SET /P Anonymous=”Do you wish to do an anonymous checkout of the source? Yes for patch creators, No for submitters:(y,n)”

IF %Anonymous%==y set SVN.URL=<http://ci-factory.googlecode.com/svn/%ProjectCodeLineName%>

IF EXIST “%ProgramFiles%\TortoiseSVN\bin\TortoiseProc.exe” GOTO UseTortoise

svn –version  
IF NOT %ERRORLEVEL%==0 (set PATH=%PATH%;%ProgramFiles%\Subversion\bin) ELSE GOTO UseSubversion

svn –version  
IF NOT %ERRORLEVEL%==0 (set PATH=%PATH%;%ProgramFiles%\CollabNet Subversion Server\bin) ELSE GOTO UseSubversion

svn –version  
IF %ERRORLEVEL%==0 (GOTO UseSubversion) ELSE GOTO NoSubversion

:UseSubversion  
IF %Anonymous%==n SET /P SvnUserName=”What is the user name you wish to use to checkout the source?”

set Credentials=  
IF DEFINED SvnUserName set Credentials=–username “%SvnUserName%”

svn checkout %Credentials% “%SVN.URL%” “%ProjectCodeLineDirectory%”

IF %ERRORLEVEL%==0 (GOTO OpenFolder) ELSE GOTO END

:NoSubversion  
echo I can’t find where you have Subversion installed!  
GOTO END

:UseTortoise  
“%ProgramFiles%\TortoiseSVN\bin\TortoiseProc.exe” /command:checkout /url:”%SVN.URL%” /path:”%ProjectCodeLineDirectory%”

IF %ERRORLEVEL%==0 (GOTO OpenFolder) ELSE GOTO END

:OpenFolder  
explorer “%ProductDirectory%”

:END
