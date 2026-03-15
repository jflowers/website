---
title: unit_testing_highly_cyclomatic_test_subjects
date: "2006-10-14"
draft: false
categories:
  - "Wiki"
aliases:
  - "/doku/doku.php?id=unit_testing_highly_cyclomatic_test_subjects"
params:
  wayback_url: "https://web.archive.org/web/20190823134507/http://jayflowers.com/doku/doku.php?id=unit_testing_highly_cyclomatic_test_subjects"
  original_url: "http://jayflowers.com/doku/doku.php?id=unit_testing_highly_cyclomatic_test_subjects"
  archived_from: Wayback Machine

---

[[[unit\_testing\_highly\_cyclomatic\_test\_subjects](/doku/doku.php?id=unit_testing_highly_cyclomatic_test_subjects&do=backlink)]]

[JayFlowers](/doku/doku.php?id= "[ALT+H]")

Trace: » [unit\_testing\_highly\_cyclomatic\_test\_subjects](/doku/doku.php?id=unit_testing_highly_cyclomatic_test_subjects "unit_testing_highly_cyclomatic_test_subjects")

## Introduction

Sometimes the simplest way to solve a problem is to write a method that has a lot of conditional logic in it. When it is, testing that method does not have to be difficult. This article will explore different ways of creating quality unit tests in the face of a highly cyclomatic test subject.

## Meet the Test Subject

```csharp
public class Conditional
```

```csharp
{
```

```csharp
    public String ComplexeMethod(String name)
```

```csharp
    {
```

```csharp
        if (name == null)
```

```csharp
            throw new ArgumentNullException("name");
```

```csharp
        if (name == String.Empty)
```

```csharp
            throw new ArgumentException("Name can not be blank.");
```

```csharp
        return String.Format("Hello {0}.", name);
```

```csharp
    }
```

```csharp
}
```

  
This is a very simple example. I trust you to see how this will apply to your own highly cyclomatic methods. There are three branches in this test subject. We will need to account for all of them. Again this is a simple example and I will trust you to keep in mind what each test solution would be like if this were a real life example(i.e. setups, teardowns, ...).

## The Usual Fixture

Normally one would try to write a separate test method for each test case like so:

```csharp
[Test]
```

```csharp
public void NullName()
```

```csharp
{
```

```csharp
    TestSubject.Conditional TestSubject = new TestSubject.Conditional();
```

```csharp
    Exception CaughtException = null;
```

```csharp
    try
```

```csharp
    {
```

```csharp
        TestSubject.ComplexeMethod(null);
```

```csharp
    }
```

```csharp
    catch (Exception ex)
```

```csharp
    {
```

```csharp
        CaughtException = ex;
```

```csharp
    }
```

```csharp
    Type ExpectedExceptionType = typeof(ArgumentNullException);
```

```csharp
    String ExpectedExceptionMessage = String.Format("Value cannot be null.{0}Parameter name: name", Environment.NewLine);
```

```csharp
    Assert.IsNotNull(CaughtException);
```

```csharp
    Assert.AreEqual(
```

```csharp
        ExpectedExceptionType,
```

```csharp
        CaughtException.GetType(),
```

```csharp
        "Expected an exception of type {0} but got one of type {1}.",
```

```csharp
            ExpectedExceptionType.Name,
```

```csharp
            CaughtException.GetType().Name);
```

```csharp
    Assert.AreEqual(
```

```csharp
        ExpectedExceptionMessage,
```

```csharp
        CaughtException.Message,
```

```csharp
        "Expected exception message '{0}' but got '{1}'.",
```

```csharp
            ExpectedExceptionMessage,
```

```csharp
            CaughtException.Message);
```

```csharp
}
```

```csharp
 
```

```csharp
[Test]
```

```csharp
public void EmptyName()
```

```csharp
{
```

```csharp
    TestSubject.Conditional TestSubject = new TestSubject.Conditional();
```

```csharp
    Exception CaughtException = null;
```

```csharp
    try
```

```csharp
    {
```

```csharp
        TestSubject.ComplexeMethod(String.Empty);
```

```csharp
    }
```

```csharp
    catch (Exception ex)
```

```csharp
    {
```

```csharp
        CaughtException = ex;
```

```csharp
    }
```

```csharp
    Type ExpectedExceptionType = typeof(ArgumentException);
```

```csharp
    String ExpectedExceptionMessage = "Name can not be blank.";
```

```csharp
    Assert.IsNotNull(CaughtException);
```

```csharp
    Assert.AreEqual(
```

```csharp
        ExpectedExceptionType,
```

```csharp
        CaughtException.GetType(),
```

```csharp
        "Expected an exception of type {0} but got one of type {1}.",
```

```csharp
            ExpectedExceptionType.Name,
```

```csharp
            CaughtException.GetType().Name);
```

```csharp
    Assert.AreEqual(
```

```csharp
        ExpectedExceptionMessage,
```

```csharp
        CaughtException.Message,
```

```csharp
        "Expected exception message '{0}' but got '{1}'.",
```

```csharp
            ExpectedExceptionMessage,
```

```csharp
            CaughtException.Message);
```

```csharp
}
```

```csharp
 
```

```csharp
[Test]
```

```csharp
public void GoodName()
```

```csharp
{
```

```csharp
    TestSubject.Conditional TestSubject = new TestSubject.Conditional();
```

```csharp
 
```

```csharp
    String ReturnValue = null;
```

```csharp
 
```

```csharp
    ReturnValue = TestSubject.ComplexeMethod("Bob");
```

```csharp
 
```

```csharp
    String ExpectedReturnValue = "Hello Bob.";
```

```csharp
    Assert.AreEqual(ExpectedReturnValue, ReturnValue, String.Format("Expected {0} but got {1} as a return value.", ExpectedReturnValue, ReturnValue));
```

```csharp
}
```

  
For a very simple example that is a lot of code. There is a lot duplicate code. We need to refactor it to share the duplicate code. In the confines of the traditional testfixture this would reduce readability: an attribute of quality unit tests that we wish to retain. So how can we re-organize the code to maintain readability and share code?

## A New Fixture

A new type of fixture can fulfill this need. A fixture that passes *a* test method *a* parameter from a provider. The fixture will iterate over a list of parameters passing each parameter to the test method on a separate call. Each parameter provided would be reported as a distinct test. The ObjectFixture, FactoryObjectProvider, FormattedObjectProvider, XmlObjectProvider, and TestWithEachObject are [MbUnit extensions](http://jayflowers.com/joomla/index.php?option=com_content&task=view&id=17&Itemid=45 "http://jayflowers.com/joomla/index.php?option=com_content&task=view&id=17&Itemid=45") that fulfill these needs.

```csharp
[ObjectFixture()]
```

```csharp
[FactoryObjectProvider(typeof(ConditionalFactory))]
```

```csharp
public class TestConditional
```

```csharp
{
```

```csharp
 
```

```csharp
    [TestWithEachObject()]
```

```csharp
    public virtual void ComplexeMethod(NameTestCase testCase)
```

```csharp
    {
```

```csharp
        TestSubject.Conditional TestSubject = new TestSubject.Conditional();
```

```csharp
 
```

```csharp
        String ReturnValue = null;
```

```csharp
        Exception CaughtException = null;
```

```csharp
        try
```

```csharp
        {
```

```csharp
            ReturnValue = TestSubject.ComplexeMethod(testCase.Name);
```

```csharp
        }
```

```csharp
        catch (Exception ex)
```

```csharp
        {
```

```csharp
            CaughtException = ex;
```

```csharp
        }
```

```csharp
 
```

```csharp
        testCase.Verify(ReturnValue, CaughtException);
```

```csharp
    }
```

```csharp
}
```

  
This test method will test every, *every*, test case we can think up for the test subject. It is easy to read and there is no duplication in the test fixture. No matter how complexe the test subject is the test fixture and test method will remain simple. The provider may be more complex. Here we are using a factory provider but the parameters could be provided by deserializing them from a file with either of the other two object providers. Notice how the argument testCase is used. It provides all data needed to prepare for the test, all the data to drive the test down the desired branch(s), and expected results. In this example a verify method is part of the testcase object much like a mock object. This is optional, the assertions could have been written in the test method. The parameter passed is the definition of the test case, hince the name of the parameter.

## Provide It Forward

The sole responsibility of an object provider is to provide a parameter for each call to the test method(s) decorated with the attribute TestWithEachObject. In the factory provider shown below the class ConditionalFactory implements IObjectProviderFactory. This interface defines only on member: `IContainer GetData()`. Remember that each parameter is all the data needed to drive a test case. There are three test cases defined here.

```csharp
public class ConditionalFactory : IObjectProviderFactory
```

```csharp
{
```

```csharp
    #region IObjectProviderFactory Members
```

```csharp
    public IContainer GetData()
```

```csharp
    {
```

```csharp
        ConditionalTestCaseContainer TestCases = new ConditionalTestCaseContainer();
```

```csharp
 
```

```csharp
        TestCases.NameTestCases.Add(this.NullNameCase());
```

```csharp
        TestCases.NameTestCases.Add(this.EmptyNameCase());
```

```csharp
        TestCases.NameTestCases.Add(this.GoodNameCase());
```

```csharp
 
```

```csharp
        return TestCases;
```

```csharp
    }
```

```csharp
    #endregion
```

```csharp
 
```

```csharp
    private NameTestCase NullNameCase()
```

```csharp
    {
```

```csharp
        NameTestCase TestCase = new NameTestCase();
```

```csharp
        TestCase.TestCaseName = "Null Name";
```

```csharp
 
```

```csharp
        TestCase.Name = null;
```

```csharp
        TestCase.ExpectedReturnValue = null;
```

```csharp
        TestCase.ExpecteException = true;
```

```csharp
        TestCase.ExpectedExceptionType = typeof(ArgumentNullException);
```

```csharp
        TestCase.ExpectedExceptionMessage = String.Format("Value cannot be null.{0}Parameter name: name", Environment.NewLine);
```

```csharp
 
```

```csharp
        return TestCase;
```

```csharp
    }
```

```csharp
    private NameTestCase EmptyNameCase()
```

```csharp
    {
```

```csharp
        NameTestCase TestCase = new NameTestCase();
```

```csharp
        TestCase.TestCaseName = "Empty Name";
```

```csharp
 
```

```csharp
        TestCase.Name = String.Empty;
```

```csharp
        TestCase.ExpectedReturnValue = null;
```

```csharp
        TestCase.ExpecteException = true;
```

```csharp
        TestCase.ExpectedExceptionType = typeof(ArgumentException);
```

```csharp
        TestCase.ExpectedExceptionMessage = "Name can not be blank.";
```

```csharp
 
```

```csharp
        return TestCase;
```

```csharp
    }
```

```csharp
    private NameTestCase GoodNameCase()
```

```csharp
    {
```

```csharp
        NameTestCase TestCase = new NameTestCase();
```

```csharp
        TestCase.TestCaseName = "Good Name";
```

```csharp
 
```

```csharp
        TestCase.Name = "Bob";
```

```csharp
        TestCase.ExpectedReturnValue = "Hello Bob.";
```

```csharp
        TestCase.ExpecteException = false;
```

```csharp
 
```

```csharp
        return TestCase;
```

```csharp
    }
```

```csharp
}
```

  
Null Name is the first test case. It is designed to trace the first existing branch of the test subject. To enter the first conditional the parameter, name, to the test subject must be null.

```csharp
public String ComplexeMethod(String name)
```

```csharp
{
```

```csharp
    if (name == null)
```

```csharp
        throw new ArgumentNullException("name");
```

```csharp
    if (name == String.Empty)
```

```csharp
        throw new ArgumentException("Name can not be blank.");
```

```csharp
    return String.Format("Hello {0}.", name);
```

```csharp
}
```

  
So we set the property Name on the testcase to null. We also set the expected return value to null as the test subject will not have the opportunity to return. We set the expected exception type and message as well.

This procedure is repeated for each branch in the test subject.

## The Case of the Test Case

The test case, parameter, in this example is type NameTestCase. It could have been any type, it will probably correspond to the test fixture in a one to one relationship. At a bare minimum it is nothing more than a data structure. You should override the ToString method, the return value of ToString provides the name of the test run to the reporting framework. In this example it is also responsible for the assertions.

```csharp
public void Verify(String returnValue, Exception exception)
```

```csharp
{
```

```csharp
    Assert.AreEqual(
```

```csharp
        this.ExpectedReturnValue,
```

```csharp
        returnValue,
```

```csharp
        "Expected {0} but got {1} as a return value.", this.ExpectedReturnValue, returnValue);
```

```csharp
 
```

```csharp
    Assert.AreEqual(this.ExpecteException, exception != null, "An excpetion was expected.");
```

```csharp
 
```

```csharp
    if (this.ExpecteException)
```

```csharp
    {
```

```csharp
        Assert.AreEqual(
```

```csharp
            this.ExpectedExceptionType,
```

```csharp
            exception.GetType(),
```

```csharp
            "Expected an exception of type {0} but got one of type {1}.",
```

```csharp
                this.ExpectedExceptionType.Name,
```

```csharp
                exception.GetType().Name);
```

```csharp
 
```

```csharp
        Assert.AreEqual(
```

```csharp
            this.ExpectedExceptionMessage,
```

```csharp
            exception.Message,
```

```csharp
            "Expected exception message '{0}' but got '{1}'.",
```

```csharp
                this.ExpectedExceptionMessage,
```

```csharp
                exception.Message);
```

```csharp
    }
```

```csharp
}
```

## Basic Insight

The reason this works is there are a known set of controls and a known set of sensable effects. Not all controls may be used in a test case the same as not all effects maybe felt for every test case. The test case type needs to be written to hold data needed for the entire control set and data for describing expectations for the entire sensable effect set. The test method is responsible creating the test environment, the test subject, executing the test subject, and asserting the expectations were met. It uses the control set in the test case to create the environment and test subject as well as executing the test subject. It uses the expectation data to assert on the effects felt. A variation on this recipe is to have the test case provide the assertion on expectations.

## Resources

[MbUnit Extensions](http://jayflowers.com/joomla/index.php?option=com_content&task=view&id=17&Itemid=45 "http://jayflowers.com/joomla/index.php?option=com_content&task=view&id=17&Itemid=45")

[Solution Zip](http://jayflowers.com/joomla/index.php?option=com_remository&Itemid=33&func=fileinfo&id=7 "http://jayflowers.com/joomla/index.php?option=com_remository&Itemid=33&func=fileinfo&id=7")

[Conditional![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_1 "reveal")

```csharp
public class Conditional
```

```csharp
{
```

```csharp
    public String ComplexeMethod(String name)
```

```csharp
    {
```

```csharp
        if (name == null)
```

```csharp
            throw new ArgumentNullException("name");
```

```csharp
        if (name == String.Empty)
```

```csharp
            throw new ArgumentException("Name can not be blank.");
```

```csharp
        return String.Format("Hello {0}.", name);
```

```csharp
    }
```

```csharp
}
```

[TestConditional![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_2 "reveal")

```csharp
[TestFixture()]
```

```csharp
[TestSubjectClassAttribute(TestSubject=typeof(TestSubject.Conditional))]
```

```csharp
[ObjectFixture()]
```

```csharp
[FactoryObjectProvider(typeof(ConditionalFactory))]
```

```csharp
public class TestConditional
```

```csharp
{
```

```csharp
 
```

```csharp
    [TestSubjectMemberAttribute(MemeberName="ComplexeMethod")]
```

```csharp
    [TestWithEachObject()]
```

```csharp
    public virtual void ComplexeMethod(NameTestCase testCase)
```

```csharp
    {
```

```csharp
        TestSubject.Conditional TestSubject = new TestSubject.Conditional();
```

```csharp
 
```

```csharp
        String ReturnValue = null;
```

```csharp
        Exception CaughtException = null;
```

```csharp
        try
```

```csharp
        {
```

```csharp
            ReturnValue = TestSubject.ComplexeMethod(testCase.Name);
```

```csharp
        }
```

```csharp
        catch (Exception ex)
```

```csharp
        {
```

```csharp
            CaughtException = ex;
```

```csharp
        }
```

```csharp
 
```

```csharp
        testCase.Verify(ReturnValue, CaughtException);
```

```csharp
    }
```

```csharp
 
```

```csharp
    [Test]
```

```csharp
    public void NullName()
```

```csharp
    {
```

```csharp
        TestSubject.Conditional TestSubject = new TestSubject.Conditional();
```

```csharp
        Exception CaughtException = null;
```

```csharp
        try
```

```csharp
        {
```

```csharp
            TestSubject.ComplexeMethod(null);
```

```csharp
        }
```

```csharp
        catch (Exception ex)
```

```csharp
        {
```

```csharp
            CaughtException = ex;
```

```csharp
        }
```

```csharp
        Type ExpectedExceptionType = typeof(ArgumentNullException);
```

```csharp
        String ExpectedExceptionMessage = String.Format("Value cannot be null.{0}Parameter name: name", Environment.NewLine);
```

```csharp
        Assert.IsNotNull(CaughtException);
```

```csharp
        Assert.AreEqual(
```

```csharp
            ExpectedExceptionType,
```

```csharp
            CaughtException.GetType(),
```

```csharp
            "Expected an exception of type {0} but got one of type {1}.",
```

```csharp
                ExpectedExceptionType.Name,
```

```csharp
                CaughtException.GetType().Name);
```

```csharp
        Assert.AreEqual(
```

```csharp
            ExpectedExceptionMessage,
```

```csharp
            CaughtException.Message,
```

```csharp
            "Expected exception message '{0}' but got '{1}'.",
```

```csharp
                ExpectedExceptionMessage,
```

```csharp
                CaughtException.Message);
```

```csharp
    }
```

```csharp
 
```

```csharp
    [Test]
```

```csharp
    public void EmptyName()
```

```csharp
    {
```

```csharp
        TestSubject.Conditional TestSubject = new TestSubject.Conditional();
```

```csharp
        Exception CaughtException = null;
```

```csharp
        try
```

```csharp
        {
```

```csharp
            TestSubject.ComplexeMethod(String.Empty);
```

```csharp
        }
```

```csharp
        catch (Exception ex)
```

```csharp
        {
```

```csharp
            CaughtException = ex;
```

```csharp
        }
```

```csharp
        Type ExpectedExceptionType = typeof(ArgumentException);
```

```csharp
        String ExpectedExceptionMessage = "Name can not be blank.";
```

```csharp
        Assert.IsNotNull(CaughtException);
```

```csharp
        Assert.AreEqual(
```

```csharp
            ExpectedExceptionType,
```

```csharp
            CaughtException.GetType(),
```

```csharp
            "Expected an exception of type {0} but got one of type {1}.",
```

```csharp
                ExpectedExceptionType.Name,
```

```csharp
                CaughtException.GetType().Name);
```

```csharp
        Assert.AreEqual(
```

```csharp
            ExpectedExceptionMessage,
```

```csharp
            CaughtException.Message,
```

```csharp
            "Expected exception message '{0}' but got '{1}'.",
```

```csharp
                ExpectedExceptionMessage,
```

```csharp
                CaughtException.Message);
```

```csharp
    }
```

```csharp
 
```

```csharp
    [Test]
```

```csharp
    public void GoodName()
```

```csharp
    {
```

```csharp
        TestSubject.Conditional TestSubject = new TestSubject.Conditional();
```

```csharp
 
```

```csharp
        String ReturnValue = null;
```

```csharp
 
```

```csharp
        ReturnValue = TestSubject.ComplexeMethod("Bob");
```

```csharp
 
```

```csharp
        String ExpectedReturnValue = "Hello Bob.";
```

```csharp
        Assert.AreEqual(
```

```csharp
            ExpectedReturnValue,
```

```csharp
            ReturnValue,
```

```csharp
            "Expected {0} but got {1} as a return value.",
```

```csharp
                ExpectedReturnValue,
```

```csharp
                ReturnValue);
```

```csharp
    }
```

```csharp
}
```

[ConditionalFactory![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_3 "reveal")

```csharp
public class ConditionalFactory : IObjectProviderFactory
```

```csharp
{
```

```csharp
    #region IObjectProviderFactory Members
```

```csharp
    public IContainer GetData()
```

```csharp
    {
```

```csharp
        ConditionalTestCaseContainer TestCases = new ConditionalTestCaseContainer();
```

```csharp
 
```

```csharp
        TestCases.NameTestCases.Add(this.NullNameCase());
```

```csharp
        TestCases.NameTestCases.Add(this.EmptyNameCase());
```

```csharp
        TestCases.NameTestCases.Add(this.GoodNameCase());
```

```csharp
 
```

```csharp
        return TestCases;
```

```csharp
    }
```

```csharp
    #endregion
```

```csharp
 
```

```csharp
    private NameTestCase NullNameCase()
```

```csharp
    {
```

```csharp
        NameTestCase TestCase = new NameTestCase();
```

```csharp
        TestCase.TestCaseName = "Null Name";
```

```csharp
 
```

```csharp
        TestCase.Name = null;
```

```csharp
        TestCase.ExpectedReturnValue = null;
```

```csharp
        TestCase.ExpecteException = true;
```

```csharp
        TestCase.ExpectedExceptionType = typeof(ArgumentNullException);
```

```csharp
        TestCase.ExpectedExceptionMessage = String.Format("Value cannot be null.{0}Parameter name: name", Environment.NewLine);
```

```csharp
 
```

```csharp
        return TestCase;
```

```csharp
    }
```

```csharp
    private NameTestCase EmptyNameCase()
```

```csharp
    {
```

```csharp
        NameTestCase TestCase = new NameTestCase();
```

```csharp
        TestCase.TestCaseName = "Empty Name";
```

```csharp
 
```

```csharp
        TestCase.Name = String.Empty;
```

```csharp
        TestCase.ExpectedReturnValue = null;
```

```csharp
        TestCase.ExpecteException = true;
```

```csharp
        TestCase.ExpectedExceptionType = typeof(ArgumentException);
```

```csharp
        TestCase.ExpectedExceptionMessage = "Name can not be blank.";
```

```csharp
 
```

```csharp
        return TestCase;
```

```csharp
    }
```

```csharp
    private NameTestCase GoodNameCase()
```

```csharp
    {
```

```csharp
        NameTestCase TestCase = new NameTestCase();
```

```csharp
        TestCase.TestCaseName = "Good Name";
```

```csharp
 
```

```csharp
        TestCase.Name = "Bob";
```

```csharp
        TestCase.ExpectedReturnValue = "Hello Bob.";
```

```csharp
        TestCase.ExpecteException = false;
```

```csharp
 
```

```csharp
        return TestCase;
```

```csharp
    }
```

```csharp
}
```

[ConditionalTestCaseContainer![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_4 "reveal")

```csharp
public class ConditionalTestCaseContainer : IContainer
```

```csharp
{
```

```csharp
 
```

```csharp
    private NameTestCaseCollection _Names;
```

```csharp
    public NameTestCaseCollection NameTestCases
```

```csharp
    {
```

```csharp
        get
```

```csharp
        {
```

```csharp
            if (_Names == null)
```

```csharp
                _Names = new NameTestCaseCollection();
```

```csharp
            return _Names;
```

```csharp
        }
```

```csharp
        set
```

```csharp
        {
```

```csharp
            _Names = value;
```

```csharp
        }
```

```csharp
    }
```

```csharp
 
```

```csharp
    #region IContainer Members
```

```csharp
    public System.Collections.ICollection ParameterCollection
```

```csharp
    {
```

```csharp
        get
```

```csharp
        {
```

```csharp
            if (_Names == null)
```

```csharp
                _Names = new NameTestCaseCollection();
```

```csharp
            return _Names;
```

```csharp
        }
```

```csharp
        set
```

```csharp
        {
```

```csharp
            _Names = (NameTestCaseCollection)value;
```

```csharp
        }
```

```csharp
    }
```

```csharp
    #endregion
```

```csharp
}
```

[NameTestCase![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_5 "reveal")

```csharp
public class NameTestCase
```

```csharp
{
```

```csharp
    private String _TestCaseName;
```

```csharp
    private String _Name;
```

```csharp
    private String _ExpectedReturnValue;
```

```csharp
    private Boolean _ExpecteException;
```

```csharp
    private Type _ExpectedExceptionType;
```

```csharp
    private String _ExpectedExceptionMessage;
```

```csharp
 
```

```csharp
    public String TestCaseName
```

```csharp
    {
```

```csharp
        get
```

```csharp
        {
```

```csharp
            return _TestCaseName;
```

```csharp
        }
```

```csharp
        set
```

```csharp
        {
```

```csharp
            _TestCaseName = value;
```

```csharp
        }
```

```csharp
    }
```

```csharp
    public String Name
```

```csharp
    {
```

```csharp
        get
```

```csharp
        {
```

```csharp
            return _Name;
```

```csharp
        }
```

```csharp
        set
```

```csharp
        {
```

```csharp
            _Name = value;
```

```csharp
        }
```

```csharp
    }
```

```csharp
    public String ExpectedReturnValue
```

```csharp
    {
```

```csharp
        get
```

```csharp
        {
```

```csharp
            return _ExpectedReturnValue;
```

```csharp
        }
```

```csharp
        set
```

```csharp
        {
```

```csharp
            _ExpectedReturnValue = value;
```

```csharp
        }
```

```csharp
    }
```

```csharp
    public Boolean ExpecteException
```

```csharp
    {
```

```csharp
        get
```

```csharp
        {
```

```csharp
            return _ExpecteException;
```

```csharp
        }
```

```csharp
        set
```

```csharp
        {
```

```csharp
            _ExpecteException = value;
```

```csharp
        }
```

```csharp
    }
```

```csharp
    public Type ExpectedExceptionType
```

```csharp
    {
```

```csharp
        get
```

```csharp
        {
```

```csharp
            return _ExpectedExceptionType;
```

```csharp
        }
```

```csharp
        set
```

```csharp
        {
```

```csharp
            _ExpectedExceptionType = value;
```

```csharp
        }
```

```csharp
    }
```

```csharp
    public String ExpectedExceptionMessage
```

```csharp
    {
```

```csharp
        get
```

```csharp
        {
```

```csharp
            return _ExpectedExceptionMessage;
```

```csharp
        }
```

```csharp
        set
```

```csharp
        {
```

```csharp
            _ExpectedExceptionMessage = value;
```

```csharp
        }
```

```csharp
    }
```

```csharp
 
```

```csharp
    public void Verify(String returnValue, Exception exception)
```

```csharp
    {
```

```csharp
        Assert.AreEqual(
```

```csharp
            this.ExpectedReturnValue,
```

```csharp
            returnValue,
```

```csharp
            "Expected {0} but got {1} as a return value.", this.ExpectedReturnValue, returnValue);
```

```csharp
 
```

```csharp
        Assert.AreEqual(this.ExpecteException, exception != null, "An excpetion was expected.");
```

```csharp
 
```

```csharp
        if (this.ExpecteException)
```

```csharp
        {
```

```csharp
            Assert.AreEqual(
```

```csharp
                this.ExpectedExceptionType,
```

```csharp
                exception.GetType(),
```

```csharp
                "Expected an exception of type {0} but got one of type {1}.",
```

```csharp
                    this.ExpectedExceptionType.Name,
```

```csharp
                    exception.GetType().Name);
```

```csharp
 
```

```csharp
            Assert.AreEqual(
```

```csharp
                this.ExpectedExceptionMessage,
```

```csharp
                exception.Message,
```

```csharp
                "Expected exception message '{0}' but got '{1}'.",
```

```csharp
                    this.ExpectedExceptionMessage,
```

```csharp
                    exception.Message);
```

```csharp
        }
```

```csharp
    }
```

```csharp
 
```

```csharp
    public override string ToString()
```

```csharp
    {
```

```csharp
        return this.TestCaseName;
```

```csharp
    }
```

```csharp
 
```

```csharp
}
```

[NameTestCaseCollection![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_6 "reveal")

```csharp
public class NameTestCaseCollection:System.Collections.CollectionBase
```

```csharp
{
```

```csharp
    public NameTestCase this[int index]
```

```csharp
    {
```

```csharp
        get
```

```csharp
        {
```

```csharp
            return (NameTestCase) this.List[index];
```

```csharp
        }
```

```csharp
        set
```

```csharp
        {
```

```csharp
            this.List[index] = value;
```

```csharp
        }
```

```csharp
    }
```

```csharp
 
```

```csharp
 
```

```csharp
    public void Add(NameTestCase item)
```

```csharp
    {
```

```csharp
        this.List.Add(item);
```

```csharp
    }
```

```csharp
 
```

```csharp
 
```

```csharp
    public bool Contains(NameTestCase item)
```

```csharp
    {
```

```csharp
        return this.List.Contains(item);
```

```csharp
    }
```

```csharp
 
```

```csharp
 
```

```csharp
    public void CopyTo(System.Array array, int index)
```

```csharp
    {
```

```csharp
        this.List.CopyTo(array, index);
```

```csharp
    }
```

```csharp
 
```

```csharp
 
```

```csharp
    public int IndexOf(NameTestCase item)
```

```csharp
    {
```

```csharp
        return this.List.IndexOf(item);
```

```csharp
    }
```

```csharp
 
```

```csharp
 
```

```csharp
    public void Insert(int index, NameTestCase item)
```

```csharp
    {
```

```csharp
        this.List.Insert(index, item);
```

```csharp
    }
```

```csharp
 
```

```csharp
 
```

```csharp
    public void Remove(NameTestCase item)
```

```csharp
    {
```

```csharp
        this.Remove(item);
```

```csharp
    }
```

```csharp
 
```

```csharp
}
```

unit\_testing\_highly\_cyclomatic\_test\_subjects.txt · Last modified: 2006/10/14 21:11 by jflowers
