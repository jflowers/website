---
title: Converting VB.Net to CSharp
date: "2007-02-20"
draft: false
categories:
  - "Continuous Integration"
  - "CI Factory"
aliases:
  - "/WordPress/?p=135"
  - "/WordPress/index.php?p=135"
params:
  wayback_url: "https://web.archive.org/web/20070313095108/http://jayflowers.com:80/WordPress/?p=135"
  original_url: "http://jayflowers.com:80/WordPress/?p=135"
  archived_from: Wayback Machine

---

## Converting VB.Net to CSharp

It has been so long I can’t remember why I started the project off in VB.Net to begin with.  I have had my fill and converted the Common.Tasks project from CI Factory to C#.  One of the reasons that I felt I could do this with out too much difficulty was the project NRefactory from [#develop](http://www.icsharpcode.net/OpenSource/SD/Default.aspx).  I was introduced to NRefactory from the Checkin Policy project located at CodePlex.  It is a code parser and generator.  Something that Microsoft should have released with the first version of .Net.  I have never understood why they haven’t rectified this egregious omission.

It took very little work to create a Filter for NAnt to convert from one language to the other.  Here is the script that I ended up with:

```
<target name=“ConvertVBToCSharp“>
  <copy todir=“C:Temp“ overwrite=“true“ newext=“.cs“>
    <fileset basedir=“C:ProjectsCI FactoryCurrentProductProductionNant“>
      <include name=“Common.Tasks***.vb“/>
    </fileset>
    <filterchain>
      <codeconvert to=“CSharp“ from=“VBNet“ />
    </filterchain>
  </copy>
</target>
```

The source for the Filter is [here](http://ci-factory.googlecode.com/svn/Current/Product/Production/Nant/CIFactory.NAnt.Tasks/Filters/CodeConvertFilter.cs).  The gist of it is:

```
public string Convert()
{
    TextReader Reader = this.GetReader();
    IParser Parser = ParserFactory.CreateParser(this.From, Reader);
    Parser.Parse();
    if (Parser.Errors.Count > 0)
    {
        Log(Level.Error, Parser.Errors.ErrorOutput);
        throw new BuildException(“Errors parsing code.”, this.Location);
    }
    CompilationUnit Tree = Parser.CompilationUnit;

    IOutputAstVisitor OutputVisitor = null;
    switch (this.To)
    {
        case SupportedLanguage.CSharp:
            OutputVisitor = new CSharpOutputVisitor();
            break;
        case SupportedLanguage.VBNet:
            OutputVisitor = new VBNetOutputVisitor();
            break;
    }
    Tree.AcceptVisitor(OutputVisitor, null);

    return OutputVisitor.Text;
}
```

The NRefactory lib is very easy to use.  I learned how from this [video](http://laputa.sharpdevelop.net/content/binary/NRefactory.wmv).

You might have some trouble with Creating a new NAnt Filter as the visibility of some the necessary parts of what comes with a Filter in NAnt.Core exclude it from being extended in external assemblies.  I corrected these visibility issues and recompiled NAnt on my own machine to overcome this issue.

It was not a flawless conversion from VB.Net to C#.  There were several minor issue that I cleared up in five minutes to so.

VB.Net:


```batch
If Not Something = SomethingElse Then
```

Converted to:


```batch
If (!Something == SomethingElse)
```

Should have been:


```batch
If (Something != SomethingElse)
```

VB.Net:


```csharp
var = hashtable(”key”)
```

Converted to:


```csharp
var = hashtable(”key”);
```

Should have been:


```csharp
var = hashtable[”key”];
```

VB.Net

reference.methodcall

Converted to:

reference.methodcall;

Should have been:

reference.methodcall();

There were a few more, you get the picture.
