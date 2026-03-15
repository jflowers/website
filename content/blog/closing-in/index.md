---
title: Closing In
date: "2007-02-02"
draft: false
categories:
  - "Continuous Integration"
  - "CI Factory"
aliases:
  - "/WordPress/?p=132"
  - "/WordPress/index.php?p=132"
params:
  wayback_url: "https://web.archive.org/web/20070904033621/http://jayflowers.com:80/WordPress/?p=132"
  original_url: "http://jayflowers.com:80/WordPress/?p=132"
  archived_from: Wayback Machine

---

## Closing In

I am closer than I have ever been. ![:)](http://jayflowers.com/WordPress/wp-includes/images/smilies/icon_smile.gif)

I have been focused on getting our build infrastructure working with Visual Studio Team Systems, Team Foundation Server.  ![](images/2007/02/WindowsLiveWriter/ClosingIn_14082/logo81.jpg) This means creating a VSTS Source Control Package for [CI Factory](http://www.cifactory.org), which includes NAnt tasks and CCNet plugins.  Blah Blah Blah, you have ![](images/2007/02/WindowsLiveWriter/ClosingIn_14082/cifactory91.gif)heard this before?  True.  I think I am just about done.  When I publish, it would be nice if it were actually useful to some other shops.  So I will try to do a quickly summary of the features here and you can let me know if I have missed something that you would like to see.

![](images/2007/02/WindowsLiveWriter/ClosingIn_14082/NAnt331.gif) I have added 9 tasks and 24 functions.  This is directly against the Team Foundation (TF) API not the TF.exe tool.  I did try to maintain, without restricting improvement, congruency with tf.exe.  So for the moment you should be able to get help from the tf.exe help doc.  There are of course some new things here.  There are filesets, which are generally localitems elements, which should be intuitive to NAnt user.  There is one task that is an experiment, tfsblock.  Notice the function call just before the tfsblock, it passes the string ‘tfs’, the id of the tfsserverconnection.  In the tfsblock the function calls do not require this information as it is specified in the block declaration.  So from one perspective there are only 12 functions, half only operate in a tfsblock.  BTW I plan to add a fileset option to the tfsget task, like the tfsadd already has.


```xml
<tfsserverconnection
```


  password=“”

  username=“”

  serverurl=“”

  domain=“”

  id=“tfs“/>


```xml
<versionspec
```


  type=“Changeset, Date, Label, Workspace, Latest, or Null“

  versionspec=“”

  id=“ver“/>


```xml
<tfsadd
```


  localitem=“”

  recursive=“”

  workspacename=“”>


```xml
  <localitems>
```



```xml
    <include name=“”/>
```



```xml
  </localitems>
```



```xml
  <tfsserverconnection refid=“tfs“/>
```



```xml
</tfsadd>
```



```xml
<echo message=“${tfs-vc::get-latest-changeset-id(’tfs‘)}“/>
```



```xml
<tfsblock
```


  clean=“true or false“

  workspacename=“”>


```xml
  <tfsserverconnection refid=“tfs“/>
```



```xml
  <do>
```


    <!–

    do some stuff in here without having to specify

    workspace and or connection info

    –>


```xml
    <echo message=“${tfs-vc::get-latest-changeset-id()}“/>
```



```xml
    <echo message=“${tfs-vc::get-latest-changeset-id-frompath(serverItem)}“/>
```



```xml
    <echo message=“${tfs-vc::label-exists(label, scope)}“/>
```



```xml
    <echo message=“${tfs-vc::workspace-exists(workspaceName)}“/>
```



```xml
    <echo message=“${tfs-vc::get-workspace-name(localItem)}“/>
```



```xml
    <echo message=“${tfs-vc::is-server-path-mapped(serverItem)}“/>
```



```xml
    <echo message=“${tfs-vc::is-local-path-mapped(localItem)}“/>
```



```xml
    <echo message=“${tfs-vc::get-localitem-for-serveritem(serverItem)}“/>
```



```xml
    <echo message=“${tfs-vc::get-serveritem-for-localitem(localItem)}“/>
```



```xml
    <echo message=“${tfs-vc::has-pending-changes()}“/>
```



```xml
    <echo message=“${tfs-vc::has-pending-changes(localItem)}“/>
```



```xml
    <echo message=“${tfs-vc::has-confilcts(pathfilter, recursive)}“/>
```



```xml
  </do>
```



```xml
</tfsblock>
```



```xml
<tfscheckin
```


  comment=“”

  localitem=“”

  recursive=“”

  workspacename=“”

  >


```xml
  <localitems>
```



```xml
    <include name=“”/>
```



```xml
  </localitems>
```



```xml
  <tfsserverconnection refid=“tfs“/>
```



```xml
</tfscheckin>
```



```xml
<tfscheckout
```


  localitem=“”

  recursive=“”

  workspacename=“”

  >


```xml
  <localitems>
```



```xml
    <include name=“”/>
```



```xml
  </localitems>
```



```xml
  <tfsserverconnection refid=“tfs“/>
```



```xml
</tfscheckout>
```



```xml
<tfsdeleteworkspace
```


  workspacename=“”

  >


```xml
  <tfsserverconnection refid=“tfs“/>
```



```xml
</tfsdeleteworkspace>
```



```xml
<tfsget
```


  all=“”

  localitem=“”

  overwrite=“”

  recursive=“”

  resultfilesetrefid=“”

  serveritem=“”

  workspacename=“”

  >


```xml
  <tfsserverconnection refid=“tfs“/>
```



```xml
  <versionspec refid=“ver“/>
```



```xml
</tfsget>
```



```xml
<tfshistory
```


  itemspec=“”

  recursive=“”

  reportfile=“”

  >


```xml
  <tfsserverconnection refid=“tfs“/>
```



```xml
  <fromversionspec refid=“ver“/>
```



```xml
  <toversionspec refid=“ver“/>
```



```xml
</tfshistory>
```



```xml
<tfslabel
```


  child=“”

  comment=“”

  delete=“”

  itemspec=“”

  labelname=“”

  recursive=“”

  scope=“”

  >


```xml
  <tfsserverconnection refid=“tfs“/>
```



```xml
  <versionspec refid=“ver“/>
```



```xml
</tfslabel>
```



```xml
<tfsmapworkspace
```


  comment=“”

  workspacename=“”

  >


```xml
  <tfsserverconnection refid=“tfs“/>
```



```xml
</tfsmapworkspace>
```


![](images/2007/02/WindowsLiveWriter/ClosingIn_14082/ccnet41.gif)I have added two plugins to CCNet and altered a third.  The two that I added, vstsbychangesetTrigger and vstsbychangesetSourceControl, subscribe to the checkin event, TFS will call a WCF soap service hosted in the CCNet process on the port specified.  This means that triggering a build is much more responsive and safe (as in concurrency).  As well each build will work with just one person’s changes.  The [third plugin](http://www.codeplex.com/TFSCCNetPlugin) is [Martin Woodward’s](http://www.woodwardweb.com/) with a few modifications.  The main one being that it remembers the latest changeset from when the build starts, during the get modification phase, and will use this in the get and label operations.  Again this is to prevent concurrency issues.


```xml
<vstsbychangesetTrigger
```


  port=“4567“

  project=“$/test.project/Current/Build“

  server=“http://vsts.chcsii.com:8080“

  statefilepath=“C:\Projects\test.project\Current\Build\server\vsts.state.xml“

  username=“false“

  password=“false“

  domain=“false“

  />


```xml
<vstsbychangesetSourceControl 
```


  applyLabel=“false“

  force=“false“

  cleancopy=“false“

  autoGetSource=“true“

  port=“4567“

  project=“$/test.project/Current/Build“

  server=“http://vsts.chcsii.com:8080“

  statefilepath=“C:\Projects\test.project\Current\Build\server\vsts.state.xml“

  workingDirectory=“C:\Projects\test.project\Current\Build“

  workspace=“BuildTest“

  deleteWorkspace=“false“

  username=“false“

  password=“false“

  domain=“false“

  />


```xml
<vsts 
```


  applyLabel=“true“

  force=“false“

  cleancopy=“false“

  autoGetSource=“false“

  project=“$/test.project/Current“

  server=“http://vsts.chcsii.com:8080“

  workingDirectory=“C:\Projects\test.project\Current\Build“

  workspace=“BuildTest“

  deleteWorkspace=“false“

  username=“false“

  password=“false“

  domain=“false“

  />

The project that I am doing this for would like to start with very few changes from the Source Safe environment that they now work in.  This means that we won’t go directly to vstsbychangesetSourceControl, one changeset per build.  We will start with Martin’s vsts plugin and a modification delay.  It is unclear if we will start with an interval trigger or move directly to vstsbychangesetTrigger.  Both are compatible with Martin’s vsts plugin and a modification delay.

The two new plugins use a listener behind the scenes, the subscription to TFS checkin event.  In the example above they share the same listener.  The current configuration schema is clunky.  Only the listener needs port and statefilepath.  It shares the need for project, server, username, password, and domain with vstsbychangesetSourceControl.  vstsbychangesetTrigger does not work with TFS directly so it does not need any of this info, save to pass to the listener.

There are a few new attributes force, cleancopy, and deleteWorkspace that bear some explanation.  Force will replace all files, it is like the all and overwrite switches for the tf.exe get command.  Cleancopy will delete the workingDirectory.  deleteWorkspace will delete the TF workspace and recreate it.  These three options are used during the get source phase of the build if the autoGetSource option is true.

![](images/2007/02/WindowsLiveWriter/ClosingIn_14082/cifactory%5B6%5D1.gif)

If you are just dyeing to get you hands on this you can find the source for the [NAnt tasks and functions](http://ci-factory.googlecode.com/svn/Current/Product/Production/Common/TF.Tasks/) and the [first two CCNet plugins](http://ci-factory.googlecode.com/svn/Current/Product/Production/Common/CCNET.TFS.Plugin/) in [CI Factory’s source control repo](http://ci-factory.googlecode.com/svn/Current/Product/) and [Martin’s is on CodePlex.](http://www.codeplex.com/TFSCCNetPlugin)  I have attached [my modifications to Martin’s stuff](images/2007/02/WindowsLiveWriter/ClosingIn_14082/Vsts.cs).




|

|
