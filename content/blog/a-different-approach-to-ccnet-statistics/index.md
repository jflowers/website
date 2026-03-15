---
title: A Different Approach to CCNET Statistics
date: "2006-11-10"
draft: false
categories:
  - "Uncategorized"
  - "Continuous Integration"
aliases:
  - "/WordPress/?p=95"
  - "/WordPress/index.php?p=95"
params:
  wayback_url: "https://web.archive.org/web/20070904033803/http://jayflowers.com:80/WordPress/?p=95"
  original_url: "http://jayflowers.com:80/WordPress/?p=95"
  archived_from: Wayback Machine

---

## A Different Approach to CCNET Statistics

At work on my current project there is some question as to how well the current build process is working? Some people are saying that there is contention for the build. We have a one person at a time, serialized, synchronous build system. The build times have been as high as 15+ minutes. If there is a contention issue this would be a real productivity problem. How can we know this is the case? The perception that this is happening and it actually happening can be different issues. So we need some hard impartial data to tell the story.

I have known that Ashish Kumar has had a Statistics Plugin for CCNET for sometime. I have wanted to get it ported back to CCNET 1.0 so that we could use it on our project. Then Grant Drake posted [CCStatistics for CruiseControl.Net 1.1](http://www.kiwidude.com/blog/2006/10/ccstatistics-for-cruisecontrolnet-11.html). So now it should be easy to get stats for all our old builds. Things were looking good.

I quickly finished the port of the stats plugin to CCNET 1.0 and set Grant’s CCStatistics tool to work. It bombed with an out of memory exception. This is not Grant’s fault. I was trying to process 1000+ log files. This would have produced a 1.4 MB file. For each log file the stats plugin will add a node to the report.xml file that looks like:


```xml
<integration build-label=“Team1-1.0.0.647“ status=“Success“ day=“03“ month=“Nov“ year=“2006“>

<statistic name=“BuildErrorType“>

</statistic>

<statistic name=“BuildErrorMessage“>

</statistic>

<statistic name=“StartTime“>11/3/2006 2:36:25 PM</statistic>

<statistic name=“Duration“>00:11:16</statistic>

<statistic name=“ProjectName“>dod.ahlta team1</statistic>

<statistic name=“mainsubmitter“>Jdegraffenried</statistic>

<statistic name=“submittercount“>1</statistic>

<statistic name=“buildcondition“>IfModificationExists</statistic>

<statistic name=“forcedby“>

</statistic>

<statistic name=“modificationcount“>8</statistic>

<statistic name=“trackercount“>1</statistic>

</integration>
```

Adding just this little node becomes an increasingly expensive operation as the file grows in size. The operation got too expensive and I received an out of memory exception. This combined with the limited extensibility of the stats plugin prompted me to roll my own solution.

I knew I wanted to append. This was the key. Appending to the end of a file was a scalable approach. You can not append to an Xml document, you can append to an Xml fragment. I learned from the CCNET project about defining your own DTD entities. Their example for [multiple projects](http://confluence.public.thoughtworks.org/display/CCNET/Multiple+Projects) shows how to reference a separate file when defining an entity. The separate file must contain an Xml fragment not a document. So I replaced report.xml with:


```xml
<?xml version=“1.0“?>

<!DOCTYPE statistics [

<!ENTITY content SYSTEM “..\..\Installs\MainAnalyticsReportContent.xml“>
```

]>


```xml
<statistics>
```

&content


```xml
</statistics>
```

The file name has been changed as well to MainAnalyticsReport.xml. Now we have a file that we can append to: MainAnalyticsReportContent.xml.

I mentioned earlier that I would like the solution to be wildly extensible. Well maybe not in such strong words. I would like to be able to add whole new files/categories as well as charts and graphs. I have been using a post build nant script to back up/archive the build artifacts. I setup the nant script the same way Main.Build.xml is in CI Factory. The archive functionality was implemented as a CI Factory Package (yeah I should release it). It seemed the right thing to do is implement this as a post build package and that is what I did. I created an xsl script that would process the build log creating the node, integration, shown above. The Analytics.Target.xml file contained a target that would apply the xsl against the log file just produced by CCNET. Note that the nant task comes after the log publisher task. I have also customized CCNET to include the log file name in the properties that it passes to nant. The output of the xsl is appended on the MainAnalyticsReportContent.xml file. So at this point we are equivalent to the functionality of the CCNET server plugin. I added another target that iterated over all the build log files and called the target that processed the log file. With this we had similar functionality to Grant’s CCStatistics tool. I ran it and it worked like a champ, no out of memory exceptions.

I decided to work on a chart next. I wanted to use [maani.us’s XML/SWF Charts](http://www.maani.us/xml_charts/index.php). Scott Hanselman turned me on to them in his post [Ohloh? Oo la la - Open Source Project Analysis](http://www.hanselman.com/blog/OhlohOoLaLaOpenSourceProjectAnalysis.aspx). The gist of how XML/SWF Chart works is you past their swf file your xml data like so:

```csharp
<HTML>
<BODY bgcolor="#FFFFFF">

<OBJECT classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0"
WIDTH="400"
HEIGHT="250"
id="charts"
ALIGN="">
<PARAM NAME=movie VALUE="charts.swf?library_path=charts_library&xml_source=sample.xml”> <PARAM NAME=quality VALUE=high> <PARAM NAME=bgcolor VALUE=#666666>  <EMBED xsrc=”charts.swf?library_path=charts_library&xml_source=sample.xml”        quality=high        bgcolor=#666666        WIDTH=”400″        HEIGHT=”250″        NAME=”charts”        ALIGN=”"        swLiveConnect=”true”        TYPE=”application/x-shockwave-flash”        PLUGINSPAGE=”http://www.macromedia.com/go/getflashplayer”> </EMBED> </OBJECT>  </BODY> </HTML>
```

The chart data format proved to be another issue to be overcome. The format is not something that can easily be created with xsl.


```xml
<chart>

<chart\_data>

<row>

<null/>

<string>2001</string>

<string>2002</string>

<string>2003</string>

<string>2004</string>

</row>

<row>

<string>Region A</string>

<number>5</number>

<number>10</number>

<number>30</number>

<number>63</number>

</row>

<row>

<string>Region B</string>

<number>100</number>

<number>20</number>

<number>65</number>

<number>55</number>

</row>

<row>

<string>Region C</string>

<number>56</number>

<number>21</number>

<number>5</number>

<number>90</number>

</row>

</chart\_data>

</chart>
```

Again this situation looks to be solved best with DTD entities and appending. I created a chart data file that looked like:


```xml
<?xml version=“1.0“ encoding=“utf-8“?>

<!DOCTYPE chart [

<!ENTITY XAxis SYSTEM “..\..\Installs\SuccessProgressXAxis.xml“>

<!ENTITY Success SYSTEM “..\..\Installs\SuccessProgressSuccessful.xml“>

<!ENTITY Fail SYSTEM “..\..\Installs\SuccessProgressFailed.xml“>

<!ENTITY Exception SYSTEM “..\..\Installs\SuccessProgressException.xml“>
```

]>


```xml
<chart>

<chart\_data>

<row>

<null/>
```

&XAxis;


```xml
</row>

<row>

<string>Success</string>
```

&Success


```xml
</row>

<row>

<string>Fail</string>
```

&Fail


```xml
</row>

<row>

<string>Exception</string>
```

&Exception


```xml
</row>

</chart\_data>

<chart\_type>line</chart\_type>

<axis\_category skip=‘100‘ />

</chart>
```

This should produce a line graph that shows the cumulative counts for successful, failed, and exception builds. There is one last problem to solve to create an xsl to produce the 4 files referenced by the chart data file. To produce each file I have to create 4 separate xsl files executing each one separately. That sounds to consume more time than I want to in the build. I looked around and found that exsl defines an element to output to multiple files: [<exsl:document>](http://www.exslt.org/exsl/elements/document/index.html).


```xml
<exsl:document
```

href = { “uri-reference“ }

method = { “xml“ | “html“ | “text“ | qname-but-not-ncname=“” }

version = { “nmtoken“ }

encoding = { “string“ }

omit-xml-declaration = { “yes“ | “no“ }

standalone = { “yes“ | “no“ }

doctype-public = { “string“ }

doctype-system = { “string“ }

cdata-section-elements = { “qnames“ }

indent = { “yes“ | “no“ }

media-type = { “string“ }>


```xml
<–Content:template–>

</exsl:document>
```

This got me part of the way there. I still needed to append to them. After some more looking around I found an MSDN article, [Producing Multiple Outputs from an XSL Transformation](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnexxml/html/xml06162003.asp), with code for an implementation of exsl:document. This gave me an easy in to add append to the implementation. I remembered seeing a post by Scott a long time ago about an Xml fragment writer: [XmlFragmentWriter - Omiting the Xml Declaration and the XSD and XSI namespaces](http://www.hanselman.com/blog/XmlFragmentWriterOmitingTheXmlDeclarationAndTheXSDAndXSINamespaces.aspx). I added the fragment writer to the msdn code plus some of my own. I found that the fragment writer was only good for one type of fragment. The kind with one root node. I had to add one more override to allow for multinode fragments. I added this to the mix as a nant task replacing the nant core task style in the script. Then I created the xsl script to create all the files.


```xml
<?xml version=“1.0“?>

<xsl:stylesheet version=“1.0“
```

xmlns:xsl=“http://www.w3.org/1999/XSL/Transform“

xmlns:exsl=“http://exslt.org/common“ exclude-result-prefixes=“exsl“>


```xml
<xsl:output method=“html“/>

<xsl:variable name=“BuildAttemptCount“ select=“count(/statistics/integration)“/>

<xsl:variable name=“SuccessfulBuildCount“ select=“count(/statistics/integration[@status=’Success’])“/>

<xsl:variable name=“FailedBuildCount“ select=“count(/statistics/integration[@status=’Failure’])“/>

<xsl:variable name=“ExceptionBuildCount“ select=“count(/statistics/integration[@status=’Exception’])“/>

<xsl:template match=“/“>

<number>

<xsl:value-of select=“$BuildAttemptCount“/>

</number>

<exsl:document href=“..\..\Installs\SuccessProgressSuccessful.xml“ fragment=“yes“ append=“yes“ >

<number>

<xsl:value-of select=“$SuccessfulBuildCount“/>

</number>

</exsl:document>

<exsl:document href=“..\..\Installs\SuccessProgressFailed.xml“ fragment=“yes“ append=“yes“ >

<number>

<xsl:value-of select=“$FailedBuildCount“/>

</number>

</exsl:document>

<exsl:document href=“..\..\Installs\SuccessProgressException.xml“ fragment=“yes“ append=“yes“ >

<number>

<xsl:value-of select=“$ExceptionBuildCount“/>

</number>

</exsl:document>

</xsl:template>

</xsl:stylesheet>
```

I refactored the main processing target to be more parameterized so that I could have it drive both the creation of the main statistics data and the chart data. This would leave it in a position to be use in the same way by me or anyone else in the future to add new charts and or statistics. I ran the script and was delighted to see the results. I had all sorts of xml files ready to be turned into html and flash charts. I really wanted to see the sharp looking chart so I skipped ahead and created a quick html file to view one. I was disappointed to find that it would not show. After some experimenting I found that XML/SWF Charts has no concept of a DTD entity in the chart data, bummer. It becomes important to know that I was copying off all the xml data files into an artifact directory for each build. I planned on having a build level plugin for the CCNET dashboard not a project level plugin like the Statistics plugin. This is important to know because if I am copying we could copy the xml document after expanding the entities. This shouldn’t be much more expensive than a regular file copy. I replaced the regular copy in the script with the xml copy, re-ran the script, and presto I had working graphs. Something interesting to note; the chart data xsl is passed the file MainAnalyticsReport.xml not the build log file.

To create an html report I will need an xsl and to show it I will need a new CCNET dashboard plugin. The xsl is mostly done as I have been stealing plenty from Ashish Kumar’s Statistics plugin. I made a few adjustments to the xsl that comes with the Statistics plugin most notably the addition of the chart. To get it to show on the dashboard I wrote a new build level plugin. It let you specify where to find the artifacts directory, what the name of the xml file is, and where the xsl file is located. Just like the xsl file has to be accessible through an http uri so does the artifacts directory and in turn the xml file. The artifacts directory is not something native to CCNET. This is a directory that the nant scripts create. In the life of CI Factory it was created to store installers and zips created in the build. It was named the installs directory, this might help to understand why installs is part of the paths in the examples above. This directory is exposed as an IIS virtual directory. The nant scripts create a directory for each build named with the datetime of the build. The plugin figures out which build artifact directory to use. It applies the xsl file specified to the xml specified and returns the html fragment. This gets the html report shown. At this point we have very similar functionality to Ashish Kumar’s Statistics plugin.

The package is still a little rough but I expect to have it polished in a the next 5 to 7 days. I will release the BackUp package at the same time.




|

|
