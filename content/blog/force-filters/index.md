---
title: Force Filters
date: "2007-10-01"
draft: false
categories:
  - "CI Factory"
aliases:
  - "/WordPress/?p=191"
  - "/WordPress/index.php?p=191"
params:
  wayback_url: "https://web.archive.org/web/20071021044604/http://jayflowers.com:80/WordPress/?p=191"
  original_url: "http://jayflowers.com:80/WordPress/?p=191"
  archived_from: Wayback Machine

---

## Force Filters

I added two new force filters to [CI Factory](http://www.cifactory.org) in the last release, 0.9.0.52.  The host filter will check the host name of the machine that the force request is coming from against a list of allowed hosts.  I did not find a good way to get the host name for a machine over the Internet so you might want to reserve the use of that filter to private network build servers.  I hope to find a suitable solution in the near future.  Here is a config example:

```csharp
<hostForceFilter>
```

```csharp
  <includedHosts>
```

```csharp
    <includedHost>Jay-PC</includedHost>
```

```csharp
    <includedHost>jflowers-lp</includedHost>
```

```csharp
  </includedHosts>
```

```csharp
</hostForceFilter>
```

The password filter lets you specify a password that must be supplied by the forcee.  Here is an example config and some screen shots:

```csharp
<passwordForceFilter password=“allthetime“ />
```

![CropperCapture[20]](images/2007/10/CropperCapture%5B20%5D1.png)

![CropperCapture[21]](images/2007/10/CropperCapture%5B21%5D1.png)

Both from the web and cctray you must supply a password.

There are other filters in CI Factory like the most popular user force filter that I blogged about [here](http://jayflowers.com/WordPress/?p=72).

Here is a config example with context, note I would not use both, one or the other is good:

```csharp
<cruisecontrol>
```

```csharp
  <project name=“CI Factory Build Scripts“>
```

```csharp
    <webURL>http://cifactorybuild.stelligent.com/CI Factory/default.aspx?_action_ViewFarmReport=true</webURL>
```

```csharp
    <state type=“state“ />
```

```csharp
    <triggers>
```

```csharp
      <projectTriggerFilter>
```

```csharp
        <trigger type=“intervalTrigger“ seconds=“90“ />
```

```csharp
        <projectFilters>
```

```csharp
          &DevBuilding;
```

```csharp
          &ReleaseBuilding;
```

```csharp
        </projectFilters>
```

```csharp
      </projectTriggerFilter>
```

```csharp
    </triggers>
```

```csharp
    <forceFilters>
```

```csharp
      <passwordForceFilter password=“allthetime“ />
```

```csharp
      <hostForceFilter>
```

```csharp
        <includedHosts>
```

```csharp
          <includedHost>Jay-PC</includedHost>
```

```csharp
          <includedHost>jflowers-lp</includedHost>
```

```csharp
        </includedHosts>
```

```csharp
      </hostForceFilter>
```

```csharp
      <projectForceFilter>
```

```csharp
        <projectFilters>
```

```csharp
          &DevBuilding;
```

```csharp
          &ReleaseBuilding;
```

```csharp
        </projectFilters>
```

```csharp
      </projectForceFilter>
```

```csharp
    </forceFilters>
```

```csharp
    <integrationFilter>
```

```csharp
      <triggeredIntegrationFilter>
```

```csharp
        <allowed>
```

```csharp
          <modificationsRequired condition=“true“ />
```

```csharp
        </allowed>
```

```csharp
      </triggeredIntegrationFilter>
```

```csharp
    </integrationFilter>
```

```csharp
    <sourcecontrol  type=“svn“ tagOnSuccess=“false“ autoGetSource=“true“ >
```

```csharp
      <trunkUrl>https://ci-factory.googlecode.com/svn/Current/Build</trunkUrl>
```

```csharp
      <workingDirectory>c:ProjectsCI FactoryCurrentBuild</workingDirectory>
```

```csharp
      <webUrlBuilder type=“websvn“>
```

```csharp
        <url>http://ci-factory.googlecode.com/svn{0}</url>
```

```csharp
      </webUrlBuilder>
```

```csharp
    </sourcecontrol>
```

```csharp
    &labeller;
```

```csharp
    <tasks>
```

```csharp
      <nullTask/>
```

```csharp
    </tasks>
```

```csharp
    <publishers>
```

```csharp
      <xmllogger />
```

```csharp
      &email;
```

```csharp
    </publishers>
```

```csharp
  </project>
```
