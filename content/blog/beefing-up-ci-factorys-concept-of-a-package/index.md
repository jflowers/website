---
title: Beefing up CI Factory’s concept of a Package
date: "2009-08-16"
draft: false
categories:
  - "CI Factory"
aliases:
  - "/WordPress/?p=211"
  - "/WordPress/index.php?p=211"
params:
  wayback_url: "https://web.archive.org/web/20091006175821/http://jayflowers.com:80/WordPress/?p=211"
  original_url: "http://jayflowers.com:80/WordPress/?p=211"
  archived_from: Wayback Machine

---

## Beefing up CI Factory’s concept of a Package

For a long time now CI Factory has had the concept of a Package: a set of NAnt targets, properties, tasks, and functions that can be loaded by the Main.Build.xml or the Post.Build.xml and later call targets on them.

```csharp
<include buildfile="${PackagesDirectory}MSBuildCompile.Target.xml" />
```

……

```csharp
<include buildfile="${PackagesDirectory}MSBuildCompile.Target.xml" />
```

Most packages include:

![image](images/2009/08/image.png "image") Properties file to tweak the package to your specific needs.

Targets file provides.. well targets that you can call from the main build file or from custom build files.

Xsl files to provide web page reports by transforming xml output from the build process.

And sometimes a bin folder containing NAnt task dlls and or console applications.

By convention the target file would include the properties file.  There was no thought to how one could safely customize a Package beyond changing the values of properties in the properties file.  This has cause some issues when trying to upgrade to a new version of CI Factory.  I think the new version of CI Factory has over come this issue and generally created a more powerful concept of Package.

To load packages there is a new task:

```csharp
<loadpackages>
```

```csharp
  <package name="Publish" />
```

```csharp
  <package name="Subversion" type="SourceControl" />
```

```csharp
  <package name="SourceModificationReport" />
```

```csharp
  <package name="TargetProcess" />
```

```csharp
  <package name="Simian" />
```

```csharp
  <package name="Ant" />
```

```csharp
  <package name="Selenium" />
```

```csharp
  <package name="FitNesse" />
```

```csharp
  <package name="JUnit" type="UnitTest" />
```

```csharp
  <package name="IntegrationTest" />
```

```csharp
  <package name="Corbertura" type="Coverage" />
```

```csharp
  <package name="Workspace" />
```

```csharp
  <package name="GlassFish" />
```

```csharp
  <package name="SoapUI" />
```

```csharp
</loadpackages>
```

When a Package is loaded these types of property are set, for example the Ant Package:

> Package.Ant.Custom.File.Loaded=False  
>   
> Package.Ant.Custom.File.Path=c:\Projects\Chapter33\Trunk\Build\Packages\Ant\Ant.Custom.xml
>
> Package.Ant.Directory.Path=c:\Projects\Chapter33\Trunk\Build\Packages\Ant
>
> Package.Ant.MacroDefs.File.Loaded=True
>
> Package.Ant.MacroDefs.File.Path=c:\Projects\Chapter33\Trunk\Build\Packages\Ant\Ant.MacroDefs.xml
>
> Package.Ant.Name=Ant
>
> Package.Ant.Properties.File.Loaded=True
>
> Package.Ant.Properties.File.Path=c:\Projects\Chapter33\Trunk\Build\Packages\Ant\Ant.Properties.xml
>
> Package.Ant.Targets.File.Loaded=True
>
> Package.Ant.Targets.File.Path=c:\Projects\Chapter33\Trunk\Build\Packages\Ant\Ant.Targets.xml

Notice there is the optional attribute type.  Type is something similar to an interface, it says that I offer these common pieces of functionality for you to make use of. This will likely become something that is enforced in a future version.  At the moment how much of that interface is implemented is up to the creator/maintainer.  The concept of a type of Package allows us to do things like:

```csharp
<loadpackages>
```

```csharp
  <package name="${package::find-name-by-type(’SourceControl’)}" type="SourceControl" />
```

```csharp
</loadpackages>
```

The loadpackages task knows of a Packages directory from the property Common.Directory.Packages.Path; this property is set by a core CI Factory script.  It will try and load these files in this order:

1. [PackageName/PackageType].Properties.xml
2. [PackageName/PackageType].MacroDefs.xml
3. [PackageName/PackageType].Targets.xml
4. [PackageName/PackageType].Custom.xml

The old convention was to name the file containing the targets [PackageName].Target.xml, singular; this has change to plural [ProjectName].Targets.xml.

There are two new files that can optional be included in a Package: [PackageName].MacroDefs.xml and [PackageName].Custom.xml.  The fork of NAnt included with CI Factory now includes the NAnt task macrodef; used for creating new tasks from nant script.  The [PackageName].MacroDefs.xml is where you can create new tasks.  The [PackageName].Custom.xml is where you can customize an existing Package.  Customization is really made possible with the new NAnt features that allow you to override an existing target and call a target by full name.

Here is an example to illustrate the override and call by full name.  Let say the following target was defined in the package Example targets file Example.Targets.xml:

```csharp
<?xml version="1.0" encoding="utf-8"?>
```

```csharp
<project name="Example" xmlns="http://nant.sf.net/schemas/nant.xsd">
```

```csharp
  <target name="Hello">
```

```csharp
    <echo message="Hello World"/>
```

```csharp
  </target>
```

```csharp
</project>
```

We could then override that target in the Example.Custom.xml file of the package like so:

```csharp
<?xml version="1.0" encoding="utf-8"?>
```

```csharp
<project name="Example.Custom" xmlns="http://nant.sf.net/schemas/nant.xsd">
```

```csharp
  <target name="Hello" override="true">
```

```csharp
    <call target="Example::Hello"/>
```

```csharp
    <echo message="Bend to my will"/>
```

```csharp
  </target>
```

```csharp
</project>
```

If you were to call the target Hello the output would be:

> [echo] Hello World  
>   
> [echo] Bend to my will

Notice in the example of the original target I included the entire file.  The project tag requires a name, in this case Example.  So when calling a target you now have two options for the name of the target to call:  the short name (e.g. Hello) and the full name (e.g. Example::Hello and Example.Custom::Hello).

The MacroDefs file opens the door for sharing not just targets between Packages, now you can share tasks.  The Ant package defines the following macro:

```csharp
<?xml version="1.0" encoding="utf-8"?>
```

```csharp
<project xmlns="http://nant.sf.net/schemas/nant.xsd" name="Ant.MacroDefs">
```

```csharp
 
```

```csharp
  <macrodef name="ant">
```

```csharp
    <attributes>
```

```csharp
      <attribute name="antbat" default="${Ant.Bat}" type="string"/>
```

```csharp
      <attribute name="logfile" type="string"/>
```

```csharp
      <attribute name="target" type="string" require="true"/>
```

```csharp
      <attribute name="buildfile" type="string" require="true"/>
```

```csharp
    </attributes>
```

```csharp
    <elementgroups>
```

```csharp
      <elementgroup name="args" type="NAnt.Core.Types.Argument" elementname="arg"/>
```

```csharp
    </elementgroups>
```

```csharp
    <elements>
```

```csharp
      <element name="environment" type="NAnt.Core.Types.EnvironmentSet"/>
```

```csharp
    </elements>
```

```csharp
    <sequential>
```

```csharp
      <ifthenelse test="${property::exists(’logfile’)}">
```

```csharp
        <then>
```

```csharp
          <property name="Ant.LogParams" value=‘-logger com.agilex.ant.GoodXmlLogger -logfile "${logfile}"‘ overwrite="true"/>
```

```csharp
          <ifnot test="${directory::exists(path::get-directory-name(logfile))}">
```

```csharp
            <mkdir dir="${path::get-directory-name(logfile)}"/>
```

```csharp
          </ifnot>
```

```csharp
        </then>
```

```csharp
        <else>
```

```csharp
          <property name="Ant.LogParams" value=‘’ overwrite="true"/>
```

```csharp
        </else>
```

```csharp
      </ifthenelse>
```

```csharp
 
```

```csharp
      <exec program="${antbat}" failonerror="true" verbose="true">
```

```csharp
        <element name="environment"/>
```

```csharp
 
```

```csharp
        <arg line=‘${target} -buildfile "${buildfile}"‘ />
```

```csharp
        <arg line=‘${Ant.LogParams}‘ />
```

```csharp
        <arg line=‘-Dprogress-filepath="${CCNetListenerFile}"‘ />
```

```csharp
        <arg line=‘-DProductVersion="${CCNetLabel}"‘ />
```

```csharp
        <arg line=‘-Ddebug="${Ant.Debug}"‘ />
```

```csharp
 
```

```csharp
        <elementgroup name="args"/>
```

```csharp
      </exec>
```

```csharp
    </sequential>
```

```csharp
  </macrodef>
```

```csharp
 
```

```csharp
</project>
```

The ant macro is used by the JUnit Package as well as several others.  See how easy it is to call ant now:

```csharp
<ant
```

```csharp
  target="unittest.run"
```

```csharp
  buildfile="${Ant.Build.File.Path}"
```

```csharp
  logfile="${Ant.Log.Directory.Path}unittest_log.xml"
```

```csharp
>
```

```csharp
  <environment refid="${Common.EnvironmentVariables.RefId}"/>
```

```csharp
  <args>
```

```csharp
    <arg line="-Dcompile.debug=${Compile.Debug}"/>
```

```csharp
  </args>
```

```csharp
</ant>
```

The macrodef task in CI Factory is improved over the [original](https://please.peelmeagrape.net/svn/public/nant/macrodef/build/doc/tasks/macrodef.html) created by [Eoin Curran](http://peelmeagrape.net/).  It will allow you to set an existing property in the macro and have the new value persist after the macro has completed.  Normally all property values are returned to the same value before the macro was executed.  You can create an element group as well as just one element.  Lastly elements are referenced in a way that does not prevent the use of the same task/type name in the macro itself.

All these improvements to the concept of a Package in CI Factory should make it easier to do great things.  If you see something else that can be done to make it easier I am all ears…



Comments Closed
