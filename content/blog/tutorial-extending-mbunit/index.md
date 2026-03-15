---
title: "Tutorial: Extending MbUnit"
date: "2006-10-02"
draft: false
categories:
  - "Unit Testing"
aliases:
  - "/WordPress/?p=88"
  - "/WordPress/index.php?p=88"
params:
  wayback_url: "https://web.archive.org/web/20070301053845/http://jayflowers.com:80/WordPress/?p=88"
  original_url: "http://jayflowers.com:80/WordPress/?p=88"
  archived_from: Wayback Machine

---

## Tutorial: Extending MbUnit

[MbUnit](http://mbunit.com/), my favorite xUnit Framework, is easy to extend.  This tutorial will cover creating a new type of test fixture attribute and test method attribute.  There are basically two reasons for creating extensions: to solve a general need and solve a specific need.  The need to create an extension for a specific context happens far more often so we will focus on it.  Marc Stober’s [comment](http://www.hanselman.com/blog/CommentView.aspx?guid=C7DF62F7-688C-49C9-8977-9A0E481D9BC0) puts it well “…some of what makes MbUnit popular is that you can use the same framework for integration testing…A lot of us like MbUnit because it just gives us a way to test whatever we think needs testing”.  The example I will use in this tutorial will be for an integration test, not a unit test.

First lets get you introduced to the participant types:

- TestFixturePatternAttribute- IRun- TestPatternAttribute- MethodRunInvoker

The first two are for a fixture and the second two are for a method.  Test fixture attributes need to inherit from TestFixturePatternAttribute.  This subtyping is how MbUnit finds test fixtures, it looks for methods that are decorated with all attributes deriving from TestFixturePatternAttribute.  The secondary function of the type is to provide the type of IRun to be used, a factory method.  It is important to understand that IRun is a decorator, as in the [Decorator Pattern](http://www.dofactory.com/Patterns/PatternDecorator.aspx).  This is how setup and teardown are added to chain of execution.

Our subtype of IRun’s main responsibility is to populate the execution tree with IRunInvokers, in our case MethodRunInvokers.  It will add to the name of each test being reported as well through the readonly property Name.

The TestPatternAttribute is the base type of the familiar TestAttribute, the one your are used to decorating most if not all your test methods with.  This attribute is important, reflection will be used our IRun locating each method decorated with this attribute.  For each decoration a MethodRunInvoker will be created.  This is the glue between our IRun and MethodRunInvoker.

Our subtype of MethodRunInvoker’s main responsibility is to execute the test method.  This is were you will tie it all together.  You can add behavior before, after, and during.  One of the other important responsibilities of this type is to provide a name for the test.  This can be as simple as the name of the decorated method or more complex.

Now that you have some idea about the players lets get into the problem we will solve.  We are going to create a commandline utility that takes the path of an xHtml file or a directory path and operates on all the xHtml files in the directory.  It will validate the format complies with the dtd referenced by the file.  It will produce an html report and display it in a browser.

Lets start with the custom fixture attribute:


```csharp
[AttributeUsage(AttributeTargets.Class, AllowMultiple = false, Inherited = true)]

public class XHtmlFixtureAtttribute : TestFixturePatternAttribute

{

public XHtmlFixtureAtttribute()

    {

    }

public override MbUnit.Core.Runs.IRun GetRun()

    {

SequenceRun Sequence = new SequenceRun();

OptionalMethodRun SetUpRun;

        SetUpRun = new OptionalMethodRun(typeof(SetUpAttribute), false);

        Sequence.Runs.Add(SetUpRun);

XHtmlFixtureRun TestRun = new XHtmlFixtureRun();

        Sequence.Runs.Add(TestRun);

OptionalMethodRun TearDownRun;

        TearDownRun = new OptionalMethodRun(typeof(TearDownAttribute), false);

        Sequence.Runs.Add(TearDownRun);

return Sequence;

    }

}
```

Besides the normal attribute stuff notice the override GetRun.  This is were the sequence of functions that will make up the test is created: SetUp, Test, TearDown.  Instead of the normal test an XHTMLFixtureRun is created.


```csharp
public class XHtmlFixtureRun : IRun

{
```

    #region IRun Members


```csharp
public bool IsTest

    {
```

get { return false; }


```csharp
    }

public string Name

    {
```

get


```csharp
        {

return “XHtmlFixture”;

        }

    }

public void Reflect(
```

        MbUnit.Core.Invokers.RunInvokerTree tree,

        MbUnit.Core.Invokers.RunInvokerVertex parent,

Type subjectType)


```csharp
    {

FileInfo[] Files = null;

if (XHtmlFileTester.File != null)

        {
```

            Files = new FileInfo[1]

                { new FileInfo(XHtmlFileTester.File) };


```csharp
        }

else if (XHtmlFileTester.Directory != null)

        {
```

            Files = new DirectoryInfo(XHtmlFileTester.Directory)

                .GetFiles(“\*.html”);


```csharp
        }

MethodInfo ValidateTest = TypeHelper.GetAttributedMethod(

            subjectType, typeof(XHtmlFileAttribute));

foreach (FileInfo XHtmlFile in Files)

        {

Object[] Args = new Object[1] { XHtmlFile };

String TestName = String.Format(“File {0}”,

                XHtmlFile.Name);

IRunInvoker TestInvoker = new MultiParameterRunInvoker(

this, ValidateTest, Args, TestName);
```

            TestInvoker = DecoratorPatternAttribute.DecoreInvoker(

                ValidateTest, TestInvoker);

            tree.AddChild(parent, TestInvoker);


```csharp
        }

    }
```

    #endregion


```csharp
}
```

This guys main responsibility is expressed in the Reflect method, as mentioned earlier.  We are only going to place one test method attribute on our test fixture so we only look for one.  You could search for more than one and add to the tree for each that you find.  Call GetAttributeMethods, plural, for such a situation.  Here thou we will be add to the tree for each file that we find.  Note that the name of the test will include the name of the file.  We also want to pass that file to the test method when it is being executed.  That is were the MultiParameterRunInvoker comes in.


```csharp
public class MultiParameterRunInvoker : MethodRunInvoker

{

private String \_Name;

private Object[] \_Args;

public Object[] Args

    {
```

get


```csharp
        {

return \_Args;

        }
```

set


```csharp
        {

            \_Args = value;

        }

    }

public override string Name

    {
```

get


```csharp
        {

return this.\_Name;

        }

    }

public MultiParameterRunInvoker(
```

IRun generator,

MethodInfo methodInformation,

Object[] args, String testName)


```batch
        : base(generator, methodInformation)

    {

this.\_Name = testName;

this.Args = args;

    }

public override object Execute(object o, IList args)

    {

foreach (Object Arg in this.Args)

        {

            args.Add(Arg);

        }

return base.Execute(o, args);

    }

}
```

There is not much to this one.  We store the MethodInfo and the arguments to pass to it and execute it when Execute is called.

Before we get to far away from the XHtmlFixtureRun.Reflect: the one test method attribute that we looked for.  It is very simple:


```csharp
[AttributeUsage(
```

AttributeTargets.Method,

    AllowMultiple = false,

    Inherited = true)

]


```csharp
public class XHtmlFileAttribute : Attribute

{

}
```

It is just a method attribute type and that is it.  So we have all our extension pieces, lets use them.  Here is the test fixture:

[XHtmlFixtureAtttribute()]


```csharp
public class XHtmlFileTester

{

private static string \_Directory;

private static string \_File;

private bool \_IsValid = true;

private XmlSchemaException \_ValidationException;

public XmlSchemaException ValidationException

    {
```

get


```csharp
        {

return \_ValidationException;

        }
```

set


```csharp
        {

            \_ValidationException = value;

        }

    }

public bool IsValid

    {
```

get


```csharp
        {

return \_IsValid;

        }
```

set


```csharp
        {

            \_IsValid = value;

        }

    }

public static string File

    {
```

get


```csharp
        {

return \_File;

        }
```

set


```csharp
        {

            \_File = value;

        }

    }

public static string Directory

    {
```

get


```csharp
        {

return \_Directory;

        }
```

set


```csharp
        {

            \_Directory = value;

        }

    }
```

    [XHtmlFile]


```csharp
public void FileTester(FileInfo file)

    {

XmlReader XHmlReader = null;

this.IsValid = true;

this.ValidationException = null;

XmlReaderSettings Settings = new XmlReaderSettings();

        Settings.ProhibitDtd = false;

        Settings.ValidationType = ValidationType.DTD;

        Settings.ValidationEventHandler += new ValidationEventHandler(TestValidationEventHandler);
```

        XHmlReader = XmlReader.Create(

            file.FullName,

            Settings);

try


```csharp
        {

while (XHmlReader.Read() && this.IsValid)

            {

            }

        }

catch (XmlException ex)

        {

Assert.Fail(“Xml Error: {0}”, ex.Message);

        }

        XHmlReader.Close();

        Settings.ValidationEventHandler -= new ValidationEventHandler(TestValidationEventHandler);

if (this.ValidationException != null
```

            && this.ValidationException.Message != null)


```csharp
        {

Assert.IsTrue(

this.IsValid,

this.ValidationException.Message);

        }

else

        {

Assert.IsTrue(this.IsValid);

        }

    }

public void TestValidationEventHandler(
```

object sender,

ValidationEventArgs args)


```csharp
    {

this.ValidationException = args.Exception;

this.IsValid = false;

    }

}
```

To begin notice that the class is decorated with the attribute XHtmlFixture.  Next skip on down to the FileTester method.  It to is decorated with one of our new custom methods: XHtmlFile.  It will create an xml reader, configure it for validation, and read the file.  The validator events when there is a violation exception.  This event is handled by the method TestValidationEventHandler.  It will set a flag and store the violation exception.  If a violation occurs the reading will stop.  After the reading has stop, for a violation or EOF the flag will be asserted on.  So if there are any errors the assertion will fail.  Now we just need to get files pumped into this rig.

I you look back at the method XHtmlFixtureRun.Reflect you will notice that it is calling on the static properties Directory and File of the XHtmlFileTester fixture that we just examined.  These static properties are how we are going to pump the files in, we need to get them from the commandline.  I like to use Param.NET and you can read about it on the Code Project if you like.  It will allow us to keep sub main nice and clean:


```csharp
static class Program

{

static int Main(string[] args)

    {

ParamCollection Parameters = ParamCollection.ApplicationParameters;

CommandLineOptions Options = new CommandLineOptions();

        Options.Directory = (string)Parameters[“Directory”].Value;

        Options.File = (string)Parameters[“File”].Value;

if (Options.File == null && Options.Directory == null)

        {

            System.Windows.Forms.MessageBox.Show(
```

“No file or directory specified!”,

“A little help please!”);


```csharp
return -1;

        }

XHtmlFileTester.Directory = Options.Directory;

XHtmlFileTester.File = Options.File;

using (AutoRunner runner = new AutoRunner())

        {

            runner.Load();

            runner.Run();

            runner.ReportToHtml();

return runner.ExitCode;

        }

    }

}
```

Notice how we populate the static properties XHtmlFileTester.Directory and XHtmlFileTester.File.  I am sure that you also see the AutoRunner.  That is a MbUnit class.  It will load the fixture XHtmlFileTester, execute it, create a report, and present it. Very easy!  All that is left is to compile and execute.  In the example project you will find an install.reg file.  Edit the paths to reflect the location where you compiled to.  This reg file will add a menu item to the context menu for directories in Windows Explorer.  Right click the web directory in example project and select Validate xHtml.  A web browser should open with a report showing one passing file and one failing file.  This is pretty cool and all but if you know the MbUnit fixture attributes I am sure you are thinking that this could have been more easily coded with the TestSuiteFixture.  Your right, but we aren’t done yet.

**But wait there’s more!**

It would be really nice to know how many violations there are in a non-compliant file.  Lets change it so that every validation reports as a failure.  To do this we will need to actually do the validation in the XHtmlFixtureRun.  Every time the validation event is fired we will add to the tree object a test method that does nothing but call Assert.Fail.  If we make it to the end of the file with out violation we will add a test method the does nothing, it will pass.  Here are altered XHtmlFixtureRun and XHtmlFileTester.

[XHtmlFixtureAtttribute()]


```csharp
public class XHtmlFileTester

{

private static string \_Directory;

private static string \_File;

public static string File

    {
```

get


```csharp
        {

return \_File;

        }
```

set


```csharp
        {

            \_File = value;

        }

    }

public static string Directory

    {
```

get


```csharp
        {

return \_Directory;

        }
```

set


```csharp
        {

            \_Directory = value;

        }

    }
```

    [XHtmlFilePass]


```csharp
public void GoodFile()

    {

    }
```

    [XHtmlFileFail]


```csharp
public void Violation(String message)

    {

Assert.Fail(message);

    }

}

public class XHtmlFixtureRun : IRun

{

private bool \_IsValid = true;

private MethodInfo \_PassMethod;

private MethodInfo \_FailMethod;

private Type \_TestFixture;

private MbUnit.Core.Invokers.RunInvokerTree \_Tree;

private MbUnit.Core.Invokers.RunInvokerVertex \_Parent;

private FileInfo \_CurrentFile;

public FileInfo CurrentFile

    {
```

get


```csharp
        {

return \_CurrentFile;

        }
```

set


```csharp
        {

            \_CurrentFile = value;

        }

    }

public MbUnit.Core.Invokers.RunInvokerTree Tree

    {
```

get


```csharp
        {

return \_Tree;

        }
```

set


```csharp
        {

            \_Tree = value;

        }

    }

public MbUnit.Core.Invokers.RunInvokerVertex Parent

    {
```

get


```csharp
        {

return \_Parent;

        }
```

set


```csharp
        {

            \_Parent = value;

        }

    }

public Type TestFixture

    {
```

get


```csharp
        {

return \_TestFixture;

        }
```

set


```csharp
        {

            \_TestFixture = value;

        }

    }

public MethodInfo PassMethod

    {
```

get


```csharp
        {

if (\_PassMethod == null)
```

                \_PassMethod = TypeHelper.GetAttributedMethod(


```csharp
this.TestFixture, typeof(XHtmlFilePassAttribute));

return \_PassMethod;

        }

    }

public MethodInfo FailMethod

    {
```

get


```csharp
        {

if (\_FailMethod == null)
```

                \_FailMethod = TypeHelper.GetAttributedMethod(


```csharp
this.TestFixture, typeof(XHtmlFileFailAttribute));

return \_FailMethod;

        }

    }

public bool IsValid

    {
```

get


```csharp
        {

return \_IsValid;

        }
```

set


```csharp
        {

            \_IsValid = value;

        }

    }
```

    #region IRun Members


```csharp
public bool IsTest

    {
```

get { return false; }


```csharp
    }

public string Name

    {
```

get


```csharp
        {

return “XHtmlFixture”;

        }

    }

public void Reflect(
```

        MbUnit.Core.Invokers.RunInvokerTree tree,

        MbUnit.Core.Invokers.RunInvokerVertex parent,

Type subjectType)


```csharp
    {

this.Tree = tree;

this.Parent = parent;

this.TestFixture = subjectType;

FileInfo[] Files = null;

if (XHtmlFileTester.File != null)

        {
```

            Files = new FileInfo[1]

                { new FileInfo(XHtmlFileTester.File) };


```csharp
        }

else if (XHtmlFileTester.Directory != null)

        {
```

            Files = new DirectoryInfo(XHtmlFileTester.Directory)

                .GetFiles(“\*.html”);


```csharp
        }

foreach (FileInfo XHtmlFile in Files)

        {

this.CurrentFile = XHtmlFile;

this.FileTester();

        }

    }
```

    #endregion


```csharp
public void FileTester()

    {

XmlReader XHmlReader = null;

this.IsValid = true;

XmlReaderSettings Settings = new XmlReaderSettings();

        Settings.ProhibitDtd = false;

        Settings.ValidationType = ValidationType.DTD;

        Settings.ValidationEventHandler += new ValidationEventHandler(TestValidationEventHandler);
```

        XHmlReader = XmlReader.Create(


```csharp
this.CurrentFile.FullName,

            Settings);
```

try


```csharp
        {

while (XHmlReader.Read())

            {

            }

        }

catch (XmlException ex)

        {

this.AddFailure(

String.Format(“Xml Error: {0}”, ex.Message),

String.Format(“File {0}”, this.CurrentFile.Name));

        }

        XHmlReader.Close();

        Settings.ValidationEventHandler -= new ValidationEventHandler(TestValidationEventHandler);

if (this.IsValid)

        {

this.AddSuccess(

String.Format(“File {0}”, this.CurrentFile.Name));

        }

    }

public void TestValidationEventHandler(
```

object sender,

ValidationEventArgs args)


```csharp
    {

String TestName = String.Format(“File {0} Line {1} Position {2}”,

this.CurrentFile.Name,
```

            args.Exception.LineNumber,

            args.Exception.LinePosition);


```csharp
this.AddFailure(args.Exception.Message, TestName);

this.IsValid = false;

    }

public void AddFailure(String message, String testName)

    {

Object[] Args = new Object[1] { message };

IRunInvoker TestInvoker = new MultiParameterRunInvoker(

this, this.FailMethod, Args, testName);
```

        TestInvoker = DecoratorPatternAttribute.DecoreInvoker(


```csharp
this.FailMethod, TestInvoker);

this.Tree.AddChild(this.Parent, TestInvoker);

    }

public void AddSuccess(String testName)

    {

Object[] Args = new Object[0] {  };

IRunInvoker TestInvoker = new MultiParameterRunInvoker(

this, this.PassMethod, Args, testName);
```

        TestInvoker = DecoratorPatternAttribute.DecoreInvoker(


```csharp
this.PassMethod, TestInvoker);

this.Tree.AddChild(this.Parent, TestInvoker);

    }

}
```

This turns things around a bit.  The unit test execution normally happens in the test fixture but here the test fixture is used just to relay the results.  The design of MbUnit is very flexible.  I would say that using it in this way is beyond its intended use but it works well.  Now when we execute we get a report that shows more than just one failing test and one passing test.  We get one passing test and 5 failing tests: one failure for each violation.  One key thing to take not of is that the while loop reading the file no longer looks to see if the file has proven to be in valid and stop reading if so.  This allows the reading to continue to the end of the file collecting all the violations.  Below is the report out.  Notice the names of the tests.  The first test name is **XHtmlFileTester.File bad.html Line 10 Position 2**.  The first part of the name is contributed by XHtmlFixtureRun.Name.  The second part is made in XHtmlFixtureRun.Reflect but is provided to the MbUnit framework by MultiParameterRunInvoker.Name.  So the format for the name is **<XHtmlFixtureRun.Name>.<MultiParameterRunInvoker.Name>**.

![](images/2006/10/mbunitlogo.png)

# Test Summary

- **Date:**2006-10-01T12:58:37.359375-04:00- **Duration:** 0.02s

|  |  |
| --- | --- |
| Total | 6/1/5/0/0/0 |
| [XHtmlFileTester](#XHtmlFileTesterAssembly) | 6/1/5/0/0/0 |
| [XHtmlFileTester.XHtmlFileTester.XHtmlFileTester](#XHtmlFileTester.XHtmlFileTester) | 6/1/5/0/0/0 |

# Warnings


# Test result details

Expand AllCollapse All

## XHtmlFileTester

- **Full Name:**XHtmlFileTester, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null- **Results:**6 test, 1 success, 5 failures, 0 skipped, 0 ignored, 0 asserts- **Duration:** 0.02s

|  |
| --- |
| 6/1/5/0/0/0 |
| XHtmlFileTester.XHtmlFileTester.XHtmlFileTester (0.02s) |
| MbUnit.Cons.exe -filter-type:XHtmlFileTester.XHtmlFileTester “file:///C:/Projects/MbUnit Extension Tutorial/FileTester/bin/Debug/XHtmlFileTester.exe” |
| |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ||  |  |  |  |  | | --- | --- | --- | --- | --- | | |  |  | | --- | --- | | - | XHtmlFileTester.File bad.html Line 10 Position 2 | | 15.625ms | 0.82 Kb, 0 | | |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  | | --- | | **Type:**MbUnit.Core.Exceptions.AssertionException | | **Message:**The element ‘body’ has invalid child element ‘br’. List of possible elements expected: ‘p h1 h2 h3 h4 h5 h6 div ul ol dl pre hr blockquote address fieldset table form noscript ins del script’. | | **Source:**MbUnit.Framework | | TargetSite:Void Fail(System.String) | | HelpLink:null | | **StackTrace:**    ```    at MbUnit.Framework.Assert.Fail(String message)    at XHtmlFileTester.XHtmlFileTester.Violation(String message) in C:ProjectsMbUnit Extension TutorialFileTesterXHtmlFileTester.cs:line 47 ``` | | | | |  |  | | --- | --- | | - | XHtmlFileTester.File bad.html Line 10 Position 5 | | 0.000ms | 0.82 Kb, 0 | | |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  | | --- | | **Type:**MbUnit.Core.Exceptions.AssertionException | | **Message:**The element cannot contain white space. Content model is empty. | | **Source:**MbUnit.Framework | | TargetSite:Void Fail(System.String) | | HelpLink:null | | **StackTrace:**    ```    at MbUnit.Framework.Assert.Fail(String message)    at XHtmlFileTester.XHtmlFileTester.Violation(String message) in C:ProjectsMbUnit Extension TutorialFileTesterXHtmlFileTester.cs:line 47 ``` | | | | |  |  | | --- | --- | | - | XHtmlFileTester.File bad.html Line 11 Position 2 | | 0.000ms | 0.82 Kb, 0 | | |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  | | --- | | **Type:**MbUnit.Core.Exceptions.AssertionException | | **Message:**The element ‘br’ cannot contain child element ‘hr’ because the parent element’s content model is empty. | | **Source:**MbUnit.Framework | | TargetSite:Void Fail(System.String) | | HelpLink:null | | **StackTrace:**    ```    at MbUnit.Framework.Assert.Fail(String message)    at XHtmlFileTester.XHtmlFileTester.Violation(String message) in C:ProjectsMbUnit Extension TutorialFileTesterXHtmlFileTester.cs:line 47 ``` | | | | |  |  | | --- | --- | | - | XHtmlFileTester.File bad.html Line 11 Position 5 | | 0.000ms | 0.82 Kb, 0 | | |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  | | --- | | **Type:**MbUnit.Core.Exceptions.AssertionException | | **Message:**The element cannot contain text. Content model is empty. | | **Source:**MbUnit.Framework | | TargetSite:Void Fail(System.String) | | HelpLink:null | | **StackTrace:**    ```    at MbUnit.Framework.Assert.Fail(String message)    at XHtmlFileTester.XHtmlFileTester.Violation(String message) in C:ProjectsMbUnit Extension TutorialFileTesterXHtmlFileTester.cs:line 47 ``` | | | | |  |  | | --- | --- | | - | XHtmlFileTester.File bad.html | | 0.000ms | 0.82 Kb, 0 | | |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  | | --- | | **Type:**MbUnit.Core.Exceptions.AssertionException | | **Message:**Xml Error: The ‘hr’ start tag on line 11 does not match the end tag of ‘body’. Line 13, position 3. | | **Source:**MbUnit.Framework | | TargetSite:Void Fail(System.String) | | HelpLink:null | | **StackTrace:**    ```    at MbUnit.Framework.Assert.Fail(String message)    at XHtmlFileTester.XHtmlFileTester.Violation(String message) in C:ProjectsMbUnit Extension TutorialFileTesterXHtmlFileTester.cs:line 47 ``` | | | | |  |  | | --- | --- | | - | XHtmlFileTester.File good.html | | 0.000ms | 0.00 Kb, 0 | |  | |

![](images/2006/10/mbuniticon.gif) This report was generated using [MbUnit](http://www.mbunit.org/).

---

When I asked the [MbUnit Google Groups](http://groups.google.com/group/MbUnitUser) to review this tutorial Peli (the creator of MbUnit) suggested that I make the extension reusable.  This got me thinking that you, as in you the reader,  could take the code provided in this tutorial and alter it to test any xml against any dtd.

[XmlValidationFixtureAtttribute(

    XmlFile=@”path\document.xml”,

    DtdFile=@”path\document.dtd”)]


```csharp
public class MyXmlTester : XmlValidationFixture

{

}
```

You could then use this in any project that included xml files that must conform to a dtd specification.  You could also use it in projects that produce xml that must conform with a dtd.  I am sure that you get the idea, I will leave you to it. ![](images/2006/10/smile1.gif)

This tutorial was compiled aganst MbUnit 2.3 RC2.

[MbUnit Extension Tutorial.zip](images/2006/10/MbUnit_20Extension_20Tutorial.zip)
