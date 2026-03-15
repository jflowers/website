---
title: "Demanding of Ant: 2 Run Once"
date: "2010-05-02"
draft: false
categories:
  - "Continuous Integration"
  - "Ant"
aliases:
  - "/WordPress/?p=214"
  - "/WordPress/index.php?p=214"
params:
  wayback_url: "https://web.archive.org/web/20100903144810/http://jayflowers.com:80/WordPress/?p=214"
  original_url: "http://jayflowers.com:80/WordPress/?p=214"
  archived_from: Wayback Machine

---

## Demanding of Ant: 2 Run Once

The use of the depends attribute on targets is prevalent in many project Ant scripts.  I believe that depends is the bane of reuse.  Lets take the name of a simple target like deploy.  In the context of a developers environment deploy would likely depend on package, package on unittest, unittest on compile…  This is fine until you want to reuse deploy in a different context, say to a different environment like production.  In that context deploy has no business with such a dependency chain.

That is not a clear enough picture though.  Depends is not just for defining a dependency chain, it also includes the much desired feature of run once.  That is to say when I call the target deploy, compile will only been run once even though both recompile and unittest depend on it.


```xml
<?xml version=“1.0“ encoding=“UTF-8“?>

<project name=“scratch“ default=“deploy“ basedir=“.“ >

  <target name=“deploy“ depends=“recompile,package“>

    <echo>deploy the missile</echo>

  </target>

  <target name=“package“ depends=“unittest“>

    <echo>package the missile</echo>

  </target>

  <target name=“unittest“ depends=“compile“>

    <echo>test the missile</echo>

  </target>

  <target name=“compile“ >

    <echo>compile the missile</echo>

  </target>

  <target name=“clean“>

    <echo>clean missile</echo>

  </target>

  <target name=“recompile“ depends=“clean,compile“/>

</project>
```

The output from calling the target deploy would be:

> c:\>ant -f scratch.build.xml  
> Buildfile: scratch.build.xml
>
> clean:  
> [echo] clean missile
>
> compile:  
> [echo] compile the missile
>
> recompile:
>
> unittest:  
> [echo] test the missile
>
> package:  
> [echo] package the missile
>
> deploy:  
> [echo] deploy the missile
>
> BUILD SUCCESSFUL  
> Total time: 0 seconds

Sidenote: you should almost never use antcall.  It violates the principle of least astonishment.  You should think of it like you are ask for Ant to execute the target in isolation.  You should use runtarget from Ant contrib.

I have found the use of orchestration targets to be far more powerful when I can ask for a target to be executed and optionally specify that it only be run once.  The depends run once is not as robust as you might think.  If you call multiple targets from the command line run once does not always work:

> c:\>ant -f scratch.build.xml recompile unittest  
> Buildfile: scratch.build.xml
>
> clean:  
> [echo] clean missile
>
> compile:  
> [echo] compile the missile
>
> recompile:
>
> compile:  
> [echo] compile the missile
>
> unittest:  
> [echo] test the missile
>
> BUILD SUCCESSFUL  
> Total time: 0 seconds

What would be ideal would be the following.


```xml
<target name=“deploy“>

  <call target=“recompile“ once=“true“/>

  <call target=“package“ once=“true“/>

  <echo>deploy the missile</echo>

</target>

<target name=“package“>

  <call target=“unittest“ once=“true“/>

  <echo>package the missile</echo>

</target>

<target name=“unittest“>

  <call target=“compile“ once=“true“/>

  <echo>test the missile</echo>

</target>

<target name=“compile“ >

  <echo>compile the missile</echo>

</target>

<target name=“clean“>

  <echo>clean missile</echo>

</target>

<target name=“recompile“>

  <call target=“clean“ once=“true“/>

  <call target=“compile“ once=“true“/>

</target>
```

With the output:

> c:\>ant -f scratch.build.xml recompile unittest  
> Buildfile: scratch.build.xml
>
> recompile:
>
> clean:  
> [echo] clean missile
>
> compile:  
> [echo] compile the missile
>
> unittest:  
> [echo] test the missile
>
> BUILD SUCCESSFUL  
> Total time: 0 seconds

I implemented the call task with a macrodef that checks if the target has been run; this is tracked by checking the existence of a property.


```xml
<macrodef name=“call“>

  <attribute name=“target“/>

  <attribute name=“if“ default=“true“/>

  <attribute name=“unless“ default=“false“/>

  <attribute name=“once“ default=“false“/>

  <sequential>

    <if>

      <and>

        <istrue value=“@{if}“ />

        <isfalse value=“@{unless}“ />

        <or>

          <and>

            <istrue value=“@{once}“/>

            <not>

              <isset property=“${ant.project.name}.Target.@{target}.Executed“/>

            </not>

          </and>

          <isfalse value=“@{once}“/>

        </or>

      </and>
```

      <then>


```xml
        <runtarget target=“@{target}“/>

      </then>

    </if>

  </sequential>

</macrodef>
```

This macrodef depends on a property being set after the successful execution of every target.  To accomplish this I created a simple logger to set a property for each target called; source is at the end of the post.  I also made sure that the logger was loaded with the script task at the beginning of the Ant project file.


```xml
<?xml version=“1.0“ encoding=“UTF-8“?>

<project name=“scratch“ default=“deploy“ basedir=“.“ >

  <taskdef resource=“net/sf/antcontrib/antcontrib.properties“ />

  <typedef resource=“AgilexAnt.properties“ />

  <script language=“javascript“>

    <![CDATA[

      importClass(Packages.com.agilex.ant.TargetListener);

      var targetListener = new TargetListener();

      project.setProjectReference(targetListener);

      project.addBuildListener(targetListener);
```

    ]]>


```xml
  </script>

  <target name=“deploy“>

    <call target=“recompile“ once=“true“/>

    <call target=“package“ once=“true“/>

    <echo>deploy the missile</echo>

  </target>
```

  …

Once you have this functionality you can begin to orchestrate in more robust ways.  With depends you can only string targets together, one after the other with no customization between the execution of each target.  Now you have the opportunity to wrap each and every target call with any customization you can write.  You can reuse in any way you want.  For this example we only want to compile and package on a developers machine (e.g. env.dev==true).


```xml
<property name=“env.dev“ value=“true“/>

<target name=“deploy“>

  <call target=“recompile“ once=“true“ if=“${env.dev}“/>

  <call target=“package“ once=“true“ if=“${env.dev}“/>

  <echo>deploy the missile</echo>

</target>
```

> c:\>ant -f scratch.build.xml -Denv.dev=false  
> Buildfile: scratch.build.xml
>
> deploy:  
> [echo] deploy the missile
>
> BUILD SUCCESSFUL  
> Total time: 0 seconds


```java
package com.agilex.ant;

import java.lang.reflect.Field;  
import java.util.Enumeration;  
import java.util.Hashtable;  
import java.util.Vector;

import org.apache.tools.ant.BuildEvent;  
import org.apache.tools.ant.BuildListener;  
import org.apache.tools.ant.Project;  
import org.apache.tools.ant.ProjectHelper;  
import org.apache.tools.ant.Target;

public class TargetListener implements BuildListener {

@Override  
public void buildFinished(BuildEvent arg0) {  
```

// TODO Auto-generated method stub  

```csharp
}

@Override  
public void buildStarted(BuildEvent arg0) {  
```

// TODO Auto-generated method stub  

```csharp
}

@Override  
public void messageLogged(BuildEvent arg0) {  
```

// TODO Auto-generated method stub  

```csharp
}

@Override  
public void targetFinished(BuildEvent event) {  
Target target = event.getTarget();  
if (event.getException() != null)  
this.forceProperty(event.getProject(), event.getProject().getName() + “.Target.” + target.getName() + “.State”, “Failed”);  
```

else  
this.forceProperty(event.getProject(), event.getProject().getName() + “.Target.” + target.getName() + “.State”, “Success”);  
this.forceProperty(event.getProject(), event.getProject().getName() + “.Target.” + target.getName() + “.Executed”, Boolean.toString(true));  

```csharp
}

@Override  
public void targetStarted(BuildEvent event) {  
Target target = event.getTarget();  
this.forceProperty(event.getProject(), “Target.” + target.getName() + “.State”, “Running”);  
}

@Override  
public void taskFinished(BuildEvent arg0) {  
```

// TODO Auto-generated method stub  

```csharp
}

@Override  
public void taskStarted(BuildEvent arg0) {  
```

// TODO Auto-generated method stub  

```csharp
}  
private Object getValue( Object instance, String fieldName ) throws IllegalAccessException, NoSuchFieldException {  
Field field = getField( instance.getClass(), fieldName );  
field.setAccessible( true );  
return field.get( instance );  
}  
private Field getField( Class thisClass, String fieldName ) throws NoSuchFieldException {  
if ( thisClass == null ) {  
throw new NoSuchFieldException( “Invalid field : ” + fieldName );  
}  
try {  
return thisClass.getDeclaredField( fieldName );  
}  
catch ( NoSuchFieldException e ) {  
return getField( thisClass.getSuperclass(), fieldName );  
}  
}

private void forceProperty(Project project, String name, String value) {  
try {  
Hashtable properties = (Hashtable) getValue(project, “properties”);  
if ( properties == null ) {  
project.setUserProperty(name, this.parseProperty(project, value));  
}  
else {  
project.setProperty(name, this.parseProperty(project, value));  
}  
}  
catch ( Exception e ) {  
project.setUserProperty(name, this.parseProperty(project, value));  
}  
}
```

@SuppressWarnings(”deprecation”)  

```csharp
private String parseProperty(Project project, String value){  
Vector fragments = new Vector();  
Vector propertyRefs = new Vector();  
ProjectHelper.parsePropertyString(value, fragments, propertyRefs);

if (propertyRefs.size() != 0) {  
StringBuffer sb = new StringBuffer();  
Enumeration i = fragments.elements();  
Enumeration j = propertyRefs.elements();  
while (i.hasMoreElements()) {  
String fragment = (String)i.nextElement();  
if (fragment == null) {  
String propertyName = (String)j.nextElement();  
fragment = project.getProperty(propertyName);  
}  
sb.append( fragment );  
}  
return sb.toString();  
}  
return value;  
}  
}
```
