---
title: Automated Workspace Management
date: "2010-04-30"
draft: false
categories:
  - "Continuous Integration"
  - "CI Factory"
aliases:
  - "/WordPress/?p=212"
  - "/WordPress/index.php?p=212"
params:
  wayback_url: "https://web.archive.org/web/20100903133849/http://jayflowers.com:80/WordPress/?p=212"
  original_url: "http://jayflowers.com:80/WordPress/?p=212"
  archived_from: Wayback Machine

---

## Automated Workspace Management

Recently I was at [CITCON 2010](http://citconf.com/raleigh-durham2010/) (Continuous Integration and Testing Conference) in Raleigh-Durham. One of the sessions I participated in was on [automated workspace management](http://citconf.com/wiki/index.php?title=Automated_Workspace_Setup).  I thought I would share more on my related experiences here.![workbench](images/2010/04/iStock_000006864190XSmall.jpg "workbench")

First what is automated workspace management?  Think of a new person on your project.  How do they get a workspace created?  Most projects have a document or documents, maybe on the wiki, that is supposed to give instructions on how to get setup.  We all know that these are never up to date.  Often they lie and confuse.  In the end it always requires someone on the team to help them figure out how to get them up and running.   And I would put money on that most times, in the end, when it starts working no one is really sure why it finally starts working.  In essence private workspaces are works of art.  We are not in the business of making works of art.  Our workspaces should be easy to create, destroy, and recreate: they should be disposable.  A new person should be able to click a button to setup their workspace.  All team members should be able to click a button to update their workspaces’ to be in sync with the latest from source control.

In CI Factory there is a Package dedicated to this; it is named…you guessed it Workspace.  It is organized into to basic types of scripts software and configuration.  Here are a couple of simple examples of each:

Software – The Subversion script will check that you have at least a minimum version of TortoiseSVN installed and prompt you for permission to download and install it if you do not have it installed.

Configuration – The TimeSync script will check that your w32time service is configured to sync with the Navy time server Tock and if not prompt you for permission to adjust the configuration.

In the session at CITCON I discovered that in the Linux OPs world there are tools written around doing this very thing.  People have begun using them to manage not only operations centers but personal workspaces for developers and testers.  Some of the tools mentioned in the session were:

- [cfengine](http://www.cfengine.org/)
- [puppet](http://www.puppetlabs.com/)
- [chef](http://wiki.opscode.com/display/chef/Home)

I have not had a chance to look deeply into these tools yet…especially to see if they can better satisfy my need on a Windows platform.  I am most keen to see how they address the myriad of ways that software for the Windows platform is offered for download and the technologies used to install.  There is no [RPM](http://www.rpm.org/) or [YUM](http://yum.baseurl.org/) for Windows…

In CI Factory we have employed several techniques to over come the variations.

First you may not be able to reliably, or legally, script the download of an installer (take the JDK for example).  In this case we downloaded the JDK to a server(http or ftp) that everyone on the team has access to and script the download from there.


```xml
<property name=“Java.Installer.File.Name“ value=“jdk-6u13-windows-i586-p.exe“/>
```



```xml
<property name=“Java.Installer.File.Path“ value=“C:\Temp\${Java.Installer.File.Name}“/>
```



```xml
<property name=“Java.Installer.Download.URL“ value=“${Workspace.Ftp.Url}${Java.Installer.File.Name}“/>
```



```xml
<get
```


  src=“${Java.Installer.Download.URL}“

  dest=“${Java.Installer.File.Path}“

  unless=“${file::exists(Java.Installer.File.Path)}“

/>

Second you need to silently execute the installer.  Most installer technologies offer some form of silent install.  You just need to read up on how they work.


```xml
<property name=“Java.Install.Path“ value=“C:\Java\jdk1.6.0\_13“/>
```



```xml
<exec
```


  workingdir=“${path::get-directory-name(Java.Installer.File.Path)}“

  program=“${Java.Installer.File.Path}“

  commandline=‘/s /v “/qn INSTALLDIR=${Java.Install.Path}”‘

  verbose=“true“

/>

You will eventually run into a situation where you need to reverse engineer an installer.  I recommend that you keep it simple, create a zip.  I doubt that you would ever need anything fancier than a SFX (self-extracting zip); both 7Zip and WinRar are good tools for creating SFX installers.  Here is a simple NAnt script I have used to create SFX files with WinRar:


```xml
<largeproperty name=“SfxConfig.Content“>
```



```xml
  <value expand=“true“ xml=“false“>
```



```xml
    <![CDATA[;The comment below contains SFX script commands
```


Path=C:\FuzzyBunnies

Setup=echo Hippied Hop

Overwrite=1

Title=My Example Installer]]>


```xml
  </value>
```



```xml
</largeproperty>
```



```xml
<property name=“SfxConfig.FilePath“ value=“C:\Temp\SfxConfig.txt“/>
```



```xml
<echo message=“${SfxConfig.Content}“ file=“${SfxConfig.FilePath}“/>
```



```xml
<property name=“InstallerZip.FileName“ value=“Example-Installer.zip“/>
```



```xml
<property name=‘InstallerZip.FilePath‘ value=‘C:\Temp\${InstallerZip.FileName}‘/>
```



```xml
<zip zipfile=“${InstallerZip.FilePath}“ verbose=“True“ >
```



```xml
  <fileset>
```



```xml
    <include name=“some stuff“/>
```



```xml
  </fileset>
```



```xml
</zip>
```



```xml
<exec
```


  program=“${WinRarProgramPath}“

  commandline=‘s -ibck “${InstallerZip.FilePath}” c -z”${SfxConfig.FilePath}”‘

  workingdir=‘C:\Temp‘

  verbose=‘true‘

/>

The end result would be C:\Temp\Example-Installer.exe.  I would unzip to the directory C:\FuzzyBunnies and echo Hippied Hop in a command window.  The title of the install window would be My Example Installer.  You can read the help for WinRar or play with the GUI to see all the options.

![WinRar SFX](images/2010/04/CropperCapture2.jpg "WinRar SFX")

The Workspace Package in CI Factory creates a SFX that bundles up NAnt and all the scripts needed to bootstrap the process of creating a new workspace.

![Workspace Setup](images/2010/04/CropperCapture4.jpg "Workspace Setup")




|

|
