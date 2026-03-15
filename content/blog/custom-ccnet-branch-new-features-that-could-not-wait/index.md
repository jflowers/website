---
title: "Custom CCNET Branch - New Features That Could Not Wait!"
date: "2006-09-05"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=72"
  - "/WordPress/index.php?p=72"
params:
  wayback_url: "https://web.archive.org/web/20100612094142/http://jayflowers.com:80/WordPress/?p=72"
  original_url: "http://jayflowers.com:80/WordPress/?p=72"
  archived_from: Wayback Machine

---

## Custom CCNET Branch - New Features That Could Not Wait!

So I have written in previous posts about a project that I am helping automate the build.  It is a rather large project, in terms of code, people, and process.  We are trying to become more agile but there are some forces that we can not change (eg medical software).  CCNET is close to handling all our build needs.  It has been lacking some crusal functionality.  The ability to create relationships between builds; this is partially implemented.  One build can trigger another or watch another.  This is good for no [traffic regulation situations](http://www.evolvingexcellence.com/blog/2006/06/thoughts_on_one.html), small teams.  We needed the ability to control when builds could not happen.  For example project experimental1 should not be forcible when experimental2 is building or checking modifications:


```xml
<projectForceFilter>

     <projectFilters>

       <projectFilter
```

            serverUri=“tcp://localhost:21247/CruiseManager.rem“

            project=“experimental2“>


```xml
         <exclusionFilters>

           <activities>

             <activity>Building</activity>

             <activity>CheckingModifications</activity>

           </activities>

         </exclusionFilters>

       </projectFilter>

     </projectFilters>

   </projectForceFilter>
```

Nor should 1 be triggerable when 2 is building, checking modifications, or failed.


```xml
<projectTriggerFilter>
```

     <trigger type=“intervalTrigger“ seconds=“60“ />


```xml
     <projectFilters>

       <projectFilter
```

            serverUri=“tcp://localhost:21247/CruiseManager.rem“

            project=“experimental2“>


```xml
         <exclusionFilters>

           <conditions>

             <condition>Failure</condition>

           </conditions>

           <activities>

             <activity>Building</activity>

             <activity>CheckingModifications</activity>

           </activities>

         </exclusionFilters>

       </projectFilter>

     </projectFilters>

   </projectTriggerFilter>
```

We had need for this type of relationship because we have multiple build servers building the same codeline concurrently.  Each build server its own list of users that can trigger a build by committing changes to source control.  Only one user can be building at a time on a build box.  There is a long discussion about this on the yahoo XP group entitled “Build Contention Equation” if you want more details.  The point I am trying to show is that if one build is broken they will all be broken so there is no point in building.  In fact it would be more informative to the team if all the build servers broke when one broke but I have not taken it that far yet.  At any rate you can now create blocking relationships between builds.  I bet a lot of you just cringed when you read “blocking”.  If that is what the process is then the tool needs to support it.  Tools should not drive/dictate process.  As I mentioned earlier they type of project this is for demands this type of process.  We don’t all get to work on small teams.

**But wait there’s more!**

The build servers that I mentions above are working in an incremental fashion, not something that you would wont to release but it was needed to bring the build times lower.  This means we now have a release build server.  It is not trigger based: it is force only.  This build is controlled by the build team.  It’s automation includes things that only a build team member has the authority to do.  So we needed a way to restrict who could force the build.  I have seen this feature asked for many times of that few years, I was one of those people.  Well here it is:


```xml
<userForceFilter
```

            domainName=“chcsii“

            userName=“build“

            password=“password“>


```xml
     <includedUsers>

       <includedUser>jflowers</includedUser>

     </includedUsers>

     <includedGroups>

       <includedGroup>Build-Masters</includedGroup>

     </includedGroups>

   </userForceFilter>
```

This force filter uses a Windows domain for managing who can and can not force a build.  There are included and excluded listings avalible (the example just uses the included).  To get the group info an account in needed to login to the AD.  This filter works for both cctray and the web dashboard.  For the web dashboard you will need to change the authentication of the virtual directory from anonymous to basic  You will also need to add <identity impersonate=“true“/> to the web.config file.

**Beware!**

Currently there is no negative feedback on cctray that a force did not occur.  This will be rectified in the near future.  The web dashboard will let you know that a force did not happen but it will not tell you why.  Again this will be fixed in soon.  Force filters must interact will all remoting clients, some might require the client to provide info (eg userForceFilter).  This means that both cctray and the web dashboard now need all the assemblies that contain the implementations of all the types serialised in the project config.  The entire project is serialised, sent to the remoting client, and deserialized.  It is the deserialization that causes the dependency on all implementing assemblies.  This is a first cut and I am sure that better designs will present them selves (fire away).

Eric Hexter is helping me with this.  We are trying to get these changes in to the trunk of the CCNET project.  I think this may take sometime and the project I am working on can’t wait that long.  Untill then I will maintain a branch of the 1.0 release of CCNET.  The source is avalible from <http://svn2.cvsdude.com/jflowers/CCNET>.

[**Download**](http://www.jayflowers.com/BlogFiles/CCNET-Custom-Branch-1.0.zip)

Here is a complete example:


```xml
<?xml version=“1.0“ encoding=“utf-8“?>

<!DOCTYPE cruisecontrol [

  <!ENTITY labeller ‘<labeller type=”defaultlabeller”>

      <prefix>1.0.0.</prefix>

    </labeller>‘>
```

]>


```xml
<cruisecontrol>

  <project name=“experimental1“>

    <state type=“state“ />
```

    <triggers>


```xml
      <projectTriggerFilter>
```

        <trigger type=“intervalTrigger“ seconds=“60“ />


```xml
        <projectFilters>

          <projectFilter
```

            serverUri=“tcp://localhost:21247/CruiseManager.rem“

            project=“experimental2“>


```xml
            <exclusionFilters>

              <conditions>

                <condition>Failure</condition>

              </conditions>

              <activities>

                <activity>Building</activity>

                <activity>CheckingModifications</activity>

              </activities>

            </exclusionFilters>

          </projectFilter>

        </projectFilters>

      </projectTriggerFilter>

    </triggers>

    <forceFilters>

      <projectForceFilter>

        <projectFilters>

          <projectFilter
```

            serverUri=“tcp://localhost:21247/CruiseManager.rem“

            project=“experimental2“>


```xml
            <exclusionFilters>

              <activities>

                <activity>Building</activity>

                <activity>CheckingModifications</activity>

              </activities>

            </exclusionFilters>

          </projectFilter>

        </projectFilters>

      </projectForceFilter>

      <userForceFilter
```

            domainName=“chcsii“

            userName=“build“

            password=“password“>


```xml
        <includedUsers>

          <includedUser>jflowers</includedUser>

        </includedUsers>

        <includedGroups>

          <includedGroup>Build-Masters</includedGroup>

        </includedGroups>

      </userForceFilter>

    </forceFilters>

    <integrationFilter>
```

      <triggeredIntegrationFilter>


```xml
        <allowed>

          <modificationsRequired condition=“true“ />

        </allowed>

      </triggeredIntegrationFilter>

      <forcedIntegrationFilter>

        <blocked>
```

          <trackerRequired condition=“false“>


```xml
            <connectionInformation
```

              username=“build“

              password=“xxx“

              dbmsserver=“jupiter“

              dbmstype=“Tracker SQL Server Sys“

              dbmsloginmode=“2“

              dbmsusername=“tracker“

              dbmspassword=“password“

              projectname=“CHCSII“

            />


```xml
            <query name=“For Me“/>

          </trackerRequired>

        </blocked>

      </forcedIntegrationFilter>

    </integrationFilter>

    &labeller;

    <tasks>

      <nant>

        <executable>C:\Temp\TestProjects\nAnt\bin\nant.exe</executable>

        <baseDirectory>C:\Temp\TestProjects</baseDirectory>

        <logger>NAnt.Core.XmlLogger </logger>

        <buildFile>scratch.build.xml</buildFile>

        <buildTimeoutSeconds>5400</buildTimeoutSeconds>

      </nant>

    </tasks>

    <publishers>

      <xmllogger />

    </publishers>

  </project>

  <project name=“experimental2“>

     <state type=“state“ />
```

    <triggers>


```xml
      <projectTriggerFilter>
```

        <trigger type=“intervalTrigger“ seconds=“60“ />


```xml
        <projectFilters>

          <projectFilter
```

            serverUri=“tcp://localhost:21247/CruiseManager.rem“

            project=“experimental1“>


```xml
            <exclusionFilters>

              <conditions>

                <condition>Failure</condition>

              </conditions>

              <activities>

                <activity>Building</activity>

                <activity>CheckingModifications</activity>

              </activities>

            </exclusionFilters>

          </projectFilter>

        </projectFilters>

      </projectTriggerFilter>

    </triggers>

    <forceFilters>

      <projectForceFilter>

        <projectFilters>

          <projectFilter
```

            serverUri=“tcp://localhost:21247/CruiseManager.rem“

            project=“experimental1“>


```xml
            <exclusionFilters>

              <activities>

                <activity>Building</activity>

                <activity>CheckingModifications</activity>

              </activities>

            </exclusionFilters>

          </projectFilter>

        </projectFilters>

      </projectForceFilter>

      <userForceFilter
```

            domainName=“chcsii“

            userName=“build“

            password=“password“>


```xml
        <includedUsers>

          <includedUser>joflowers</includedUser>

        </includedUsers>

      </userForceFilter>

    </forceFilters>

    <integrationFilter>
```

      <triggeredIntegrationFilter>


```xml
        <allowed>

          <modificationsRequired condition=“true“ />

        </allowed>

      </triggeredIntegrationFilter>

      <forcedIntegrationFilter>

        <allowed>

          <modificationsRequired condition=“false“ />

        </allowed>

      </forcedIntegrationFilter>

    </integrationFilter>

    &labeller;

    <tasks>

      <nant>

        <executable>C:\Temp\TestProjects\nAnt\bin\nant.exe</executable>

        <baseDirectory>C:\Temp\TestProjects</baseDirectory>

        <logger>NAnt.Core.XmlLogger </logger>

        <buildFile>scratch.build.xml</buildFile>

        <buildTimeoutSeconds>5400</buildTimeoutSeconds>

      </nant>

    </tasks>

    <publishers>

      <xmllogger />

    </publishers>

  </project>

</cruisecontrol>
```
