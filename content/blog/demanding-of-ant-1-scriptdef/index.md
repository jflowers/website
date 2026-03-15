---
title: "Demanding of Ant: 1 scriptdef"
date: "2010-05-01"
draft: false
categories:
  - "Continuous Integration"
  - "Ant"
aliases:
  - "/WordPress/?p=213"
  - "/WordPress/index.php?p=213"
params:
  wayback_url: "https://web.archive.org/web/20100903133929/http://jayflowers.com:80/WordPress/?p=213"
  original_url: "http://jayflowers.com:80/WordPress/?p=213"
  archived_from: Wayback Machine

---

## Demanding of Ant: 1 scriptdef

I hate Ant. I like NAnt better, and I hate NAnt too.  The intent of this series is to share how I have demanded more out of Ant.

Did you know that you can mess with the Java objects of Ant in Ant script?  You can create tasks on the fly. You can even create a logger on the fly.  I have used the following example to insure that a log file is written to without having to count on a user supplying the needed command line arguments.

If you are not familiar with the scriptdef task in Ant you should read the help for the task [here](http://ant.apache.org/manual/OptionalTasks/scriptdef.html).  It is part of the optional Ant tasks, so you will need to have gotten your Ant install [setup correctly](http://ant.apache.org/manual/install.html#optionalTasks) for the optional tasks.  The scriptdef task supports several languages, here I will be using [JavaScript](http://www.mozilla.org/rhino/).


```xml
<?xml version=“1.0“ encoding=“UTF-8“?>

<project name=“scratch“ default=“play“ basedir=“.“ >

  <target name=“play“>

    <say.hello/>

  </target>

  <scriptdef name=“say.hello“ language=“javascript“>

    <![CDATA[

      self.log(”hello”);

    ]]>

  </scriptdef>

</project>
```

Executing this script will output:

> Buildfile: scratch.build.xml
>
> play:  
> [say.hello] hello
>
> BUILD SUCCESSFUL  
> Total time: 0 seconds

You can import Java classes into the JavaScript with the importClass method: importClass(Package.[Java Full Class Name]);.  When you combined this with your access back into the Ant object graph through self you can do some interesting things.  To explore what is available to me I used this trick to iterate over what self provides:


```xml
<scriptdef name=“explore.self“ language=“javascript“>

  <![CDATA[
```

  for (member in self)

  {

    self.log(member);

  }

  ]]>


```xml
</scriptdef>
```

> [explore.self] project  
> [explore.self] getText  
> [explore.self] createDynamicElement  
> [explore.self] toString  
> [explore.self] getTaskType  
> [explore.self] wait  
> [explore.self] bindToOwner  
> [explore.self] log  
> [explore.self] getClass  
> [explore.self] getLocation  
> [explore.self] taskType  
> [explore.self] hashCode  
> [explore.self] fail  
> [explore.self] reconfigure  
> [explore.self] class  
> [explore.self] notify  
> [explore.self] description  
> [explore.self] maybeConfigure  
> [explore.self] location  
> [explore.self] setTaskType  
> [explore.self] dynamicAttribute  
> [explore.self] getTaskName  
> [explore.self] clone  
> [explore.self] getOwningTarget  
> [explore.self] getProject  
> [explore.self] setLocation  
> [explore.self] setDescription  
> [explore.self] getRuntimeConfigurableWrapper  
> [explore.self] taskName  
> [explore.self] text  
> [explore.self] equals  
> [explore.self] setRuntimeConfigurableWrapper  
> [explore.self] setTaskName  
> [explore.self] setDynamicAttribute  
> [explore.self] owningTarget  
> [explore.self] getDescription  
> [explore.self] execute  
> [explore.self] setOwningTarget  
> [explore.self] perform  
> [explore.self] notifyAll  
> [explore.self] init  
> [explore.self] addText  
> [explore.self] setProject  
> [explore.self] runtimeConfigurableWrapper

Self provides a reference to the Ant object project; pretty much the root of the object graph.  You can use this same trick on other objects you need to get more information on.  Sometimes I need to understand the inner workings so I use a decompiler or read the Ant source.  The last critical piece of information you need to unlock the door to productivity is the method project.createTask(String taskName).  The argument taskName is the friendly name not the class name of the task to be created. For example project.createTask(“mkdir”) will create an instance of the mkdir task.  Armed with this knowledge you can experiment and learn to apply it in many helpful and time saving ways.  Here is an example that will use the default logger to output to the console and to a dynamically named log file.


```xml
<?xml version=“1.0“ encoding=“UTF-8“?>

<project name=“scratch“ default=“play“ basedir=“.“ >

  <taskdef resource=“net/sf/antcontrib/antcontrib.properties“ />

  <target name=“play“>

    <var name=“Log.Directory.Path“ value=“C:\Temp\Play“/>

    <start.logger/>

    <echo>T minus</echo>

    <echo>3</echo>

    <echo>2</echo>

    <echo>1</echo>

    <echo>blast off…</echo>

  </target>

  <scriptdef name=“start.logger“ language=“javascript“>

    <![CDATA[

        importClass(Packages.org.apache.tools.ant.DefaultLogger);

        importClass(Packages.java.io.File);

        importClass(Packages.java.io.FileOutputStream);

        importClass(Packages.java.io.PrintStream);

        importClass(Packages.org.apache.tools.ant.BuildEvent);

        importClass(Packages.org.apache.tools.ant.Target);

        mkdir = project.createTask(”mkdir”);

        mkdir.setDir(new File(project.getProperty(”Log.Directory.Path”)));

        mkdir.execute();

        tstamp = project.createTask(”tstamp”);

        format = tstamp.createFormat();

        format.setProperty(”now”);

        format.setPattern(”MM.dd.yyyy-HH.mm.ss-zz”);

        tstamp.execute();

        var logger = new DefaultLogger();

        var out = new PrintStream(new FileOutputStream(project.getProperty(”Log.Directory.Path”) + “/” + project.getProperty(”ant.project.name”) + “-” + project.getProperty(”now”) + “.log”));

        logger.setOutputPrintStream(out);

        logger.setMessageOutputLevel(2);

        project.setProjectReference(logger);

        project.addBuildListener(logger);

        logger.buildStarted(new BuildEvent(project));

        logger.targetStarted(new BuildEvent(self.getOwningTarget()));

        logger.taskStarted(new BuildEvent(self))

    ]]>

  </scriptdef>

</project>
```

This is the console output:

> c:\>ant -f scratch.build.xml play  
> Buildfile: scratch.build.xml
>
> play:  
> [echo] T minus  
> [echo] 3  
> [echo] 2  
> [echo] 1  
> [echo] blast off…
>
> BUILD SUCCESSFUL  
> Total time: 0 seconds

And here is the output to the logfile:

C:\Temp\play\scratch05.01.2010-10.00.33-EDT.log

> play:  
> [echo] T minus  
> [echo] 3  
> [echo] 2  
> [echo] 1  
> [echo] blast off…
>
> BUILD SUCCESSFUL  
> Total time: 0 seconds
