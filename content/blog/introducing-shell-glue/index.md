---
title: Introducing Shell Glue
date: "2007-08-31"
draft: false
categories:
  - "Tools"
aliases:
  - "/WordPress/?p=183"
  - "/WordPress/index.php?p=183"
params:
  wayback_url: "https://web.archive.org/web/20080529045307/http://jayflowers.com:80/WordPress/?p=183"
  original_url: "http://jayflowers.com:80/WordPress/?p=183"
  archived_from: Wayback Machine

---

## Introducing Shell Glue

Shell Glue is a![iStock_000001915932XSmall](images/2007/08/iStock_000001915932XSmall.jpg) Windows Explorer Shell Extension, more specifically to add context menu items to files and folders.  What menu items and sub items are added to the context menu is controlled through a configuration file.  For a simple example lets create a configuration that will give a menu item that will build solution and or project files with MSBuild when selected.

![SimpleBuild](images/2007/08/SimpleBuild.png)

```csharp
<?xml version=“1.0“ encoding=“utf-8“ ?>
```

```csharp
<Settings>
```

```csharp
  <Actions>
```

```csharp
    <ActionItem>
```

```csharp
      <Name>Build</Name>
```

```csharp
      <Verb>Build</Verb>
```

```csharp
      <Help>Build</Help>
```

```csharp
      <TargetListMode>File</TargetListMode>
```

```csharp
      <IconFilePath>C:Program FilesShell Glue.Netmsbuild.ico</IconFilePath>
```

```csharp
      <ExtentionFilter>
```

```csharp
        <string>^.*.sln$</string>
```

```csharp
        <string>^.*..*proj$</string>
```

```csharp
      </ExtentionFilter>
```

```csharp
      <ProgramPath>C:Program FilesShell Glue.NetBuild.bat</ProgramPath>
```

```csharp
    </ActionItem>
```

```csharp
  </Actions>
```

```csharp
</Settings>
```

Here is the batch file contents:

> @echo off  
> set PATH=%PATH%;%windir%\Microsoft.NET\Framework\v2.0.50727  
> @echo on
>
> FOR /F “tokens=1 delims=” %%i in (%~fs1) do msbuild “%%i”
>
> @echo off  
> SET /P variable=”Hit Enter to exit.”

And here is the result of selecting the menu item:

![CropperCapture[7]](images/2007/08/CropperCapture%5B7%5D.png)

So lets take a look at what config options there are and what they do.  Here is a bogas example of all the config options:

```csharp
<?xml version=“1.0“ encoding=“utf-16“?>
```

```csharp
<ActionItem>
```

```csharp
  <Name>Name</Name><!–Menu Item Caption–>
```

```csharp
  <Verb>Verb</Verb><!–Optional - Cruft–>
```

```csharp
  <Help>Help</Help><!–Optional - HelpString for the Menu Item–>
```

```csharp
  <IconFilePath>Path</IconFilePath><!–Optional - Full path to ico file 16×16–>
```

```csharp
  <Actions><!–Optional - List of sub menu items–>
```

```csharp
    <ActionItem>
```

```csharp
      <Name>Child</Name>
```

```csharp
      <TargetListMode>File</TargetListMode><!–Optional - Default is File–>
```

```csharp
      <ProgramPath>path</ProgramPath><!–Program to be executed–>
```

```csharp
      <ExtentionFilter><!–Optional–>
```

```csharp
        <string>Regex Pattern</string>
```

```csharp
        <string>^.*.txt$</string>
```

```csharp
      </ExtentionFilter>
```

```csharp
    </ActionItem>
```

```csharp
    <ActionItem>
```

```csharp
      <Name>Child2</Name>
```

```csharp
      <TargetListMode>CommandLine</TargetListMode>
```

```csharp
      <ArgumentsFormat>something {0} /something</ArgumentsFormat><!–Optional–>
```

```csharp
      <ProgramPath>path</ProgramPath>
```

```csharp
    </ActionItem>
```

```csharp
  </Actions>
```

```csharp
</ActionItem>
```

Each menu item is tracked with a key that is a combination of the Name, Verb, and Help strings.  So you can have multiple context menu items with the same Name/Caption.  Each menu item may have an icon, it looks best with a 16X16 icon.  The ProgramPath is the full path to file to be executed.  The TargetListMode controls how the selected items are passed to the program to be executed.  The File mode will write each target file and folder to a temp file and pass the temp file path to the program to be executed.  If you look back at the batch file used in the MSBuild example the FOR loop is iterating over the contents of the temp file.  The only other option for the TargetListMode is CommandLine.  This will pass each target file and folder as a separate argument.  This is a risky choice as you might exceed the length limit for the commandline; still it can be use full.  The ArgumentFormat gives you more control of what the commandline for the program to be executed is.  This is particularly useful if you want to call a console application directly.  The list of targets or the temp file are stored in {0}.  Lastly there are ExtensionFilters.  These allow you to provide regular expressions to narrow what files this menu item will be displayed for.

This config file is located: C:\Program Files\Shell Glue\Settings.xml.

I originally start on this to create a poor mans Tortoise for Team Foundation Server(TFS).  Here is an example entry for a menu item to add files and folders to TFS:

```csharp
<ActionItem>
```

```csharp
  <Name>Add</Name>
```

```csharp
  <TargetListMode>CommandLine</TargetListMode>
```

```csharp
  <ArgumentsFormat>add {0} /recursive</ArgumentsFormat>
```

```csharp
  <ProgramPath>C:Program FilesMicrosoft Visual Studio 8Common7IDETF.exe</ProgramPath>
```

```csharp
</ActionItem>
```

So as this is no where near as nice as Tortoise products are I went with a crab (the theme being shells..).

![TFSCrab](images/2007/08/TFSCrab.png)

I have been warned that managed extensions can be problematic. From [MSDN Magazine](http://msdn.microsoft.com/msdnmag/issues/04/01/WindowsShell/default.aspx):

> [ **Editor’s Update - 6/23/2006:** Because shell extensions are loaded into arbitrary processes and because managed code built against one version of the runtime may not run in a process running an earlier version of the runtime, Microsoft recommends against writing managed shell extensions and does not consider them a supported scenario.]

I really made this for myself.  It did not take long to write.  The Wix installer took significantly longer than the extension.  So I am not worried about the warning for myself, you will have to judged for yourself.

Here is the download link:

[**ShellGlue-1.0.msi**](http://shellglue.googlecode.com/files/ShellGlue-1.0.msi)

The project is hosted on Google Code so you can play with the code yourself:

[http://code.google.com/p/shellglue/source](http://code.google.com/p/shellglue/source "http://code.google.com/p/shellglue/source")

Please know that it is using a commercial product to make extending the shell easy.  So if you want to play with the code you will need to download [Sky Software’s EZShellExtension.Net](http://www.ssware.com/ezshell/ezshell.htm).




|

|
