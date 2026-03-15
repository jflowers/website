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

```
public class Conditional

{

    public String ComplexeMethod(String name)

    {

        if (name == null)

            throw new ArgumentNullException("name");

        if (name == String.Empty)

            throw new ArgumentException("Name can not be blank.");

        return String.Format("Hello {0}.", name);

    }

}
```

  
This is a very simple example. I trust you to see how this will apply to your own highly cyclomatic methods. There are three branches in this test subject. We will need to account for all of them. Again this is a simple example and I will trust you to keep in mind what each test solution would be like if this were a real life example(i.e. setups, teardowns, ...).

## The Usual Fixture

Normally one would try to write a separate test method for each test case like so:

```
[Test]

public void NullName()

{

    TestSubject.Conditional TestSubject = new TestSubject.Conditional();

    Exception CaughtException = null;

    try

    {

        TestSubject.ComplexeMethod(null);

    }

    catch (Exception ex)

    {

        CaughtException = ex;

    }

    Type ExpectedExceptionType = typeof(ArgumentNullException);

    String ExpectedExceptionMessage = String.Format("Value cannot be null.{0}Parameter name: name", Environment.NewLine);

    Assert.IsNotNull(CaughtException);

    Assert.AreEqual(

        ExpectedExceptionType,

        CaughtException.GetType(),

        "Expected an exception of type {0} but got one of type {1}.",

            ExpectedExceptionType.Name,

            CaughtException.GetType().Name);

    Assert.AreEqual(

        ExpectedExceptionMessage,

        CaughtException.Message,

        "Expected exception message '{0}' but got '{1}'.",

            ExpectedExceptionMessage,

            CaughtException.Message);

}


[Test]

public void EmptyName()

{

    TestSubject.Conditional TestSubject = new TestSubject.Conditional();

    Exception CaughtException = null;

    try

    {

        TestSubject.ComplexeMethod(String.Empty);

    }

    catch (Exception ex)

    {

        CaughtException = ex;

    }

    Type ExpectedExceptionType = typeof(ArgumentException);

    String ExpectedExceptionMessage = "Name can not be blank.";

    Assert.IsNotNull(CaughtException);

    Assert.AreEqual(

        ExpectedExceptionType,

        CaughtException.GetType(),

        "Expected an exception of type {0} but got one of type {1}.",

            ExpectedExceptionType.Name,

            CaughtException.GetType().Name);

    Assert.AreEqual(

        ExpectedExceptionMessage,

        CaughtException.Message,

        "Expected exception message '{0}' but got '{1}'.",

            ExpectedExceptionMessage,

            CaughtException.Message);

}


[Test]

public void GoodName()

{

    TestSubject.Conditional TestSubject = new TestSubject.Conditional();


    String ReturnValue = null;


    ReturnValue = TestSubject.ComplexeMethod("Bob");


    String ExpectedReturnValue = "Hello Bob.";

    Assert.AreEqual(ExpectedReturnValue, ReturnValue, String.Format("Expected {0} but got {1} as a return value.", ExpectedReturnValue, ReturnValue));

}
```

  
For a very simple example that is a lot of code. There is a lot duplicate code. We need to refactor it to share the duplicate code. In the confines of the traditional testfixture this would reduce readability: an attribute of quality unit tests that we wish to retain. So how can we re-organize the code to maintain readability and share code?

## A New Fixture

A new type of fixture can fulfill this need. A fixture that passes *a* test method *a* parameter from a provider. The fixture will iterate over a list of parameters passing each parameter to the test method on a separate call. Each parameter provided would be reported as a distinct test. The ObjectFixture, FactoryObjectProvider, FormattedObjectProvider, XmlObjectProvider, and TestWithEachObject are [MbUnit extensions](http://jayflowers.com/joomla/index.php?option=com_content&task=view&id=17&Itemid=45 "http://jayflowers.com/joomla/index.php?option=com_content&task=view&id=17&Itemid=45") that fulfill these needs.

```
[ObjectFixture()]

[FactoryObjectProvider(typeof(ConditionalFactory))]

public class TestConditional

{


    [TestWithEachObject()]

    public virtual void ComplexeMethod(NameTestCase testCase)

    {

        TestSubject.Conditional TestSubject = new TestSubject.Conditional();


        String ReturnValue = null;

        Exception CaughtException = null;

        try

        {

            ReturnValue = TestSubject.ComplexeMethod(testCase.Name);

        }

        catch (Exception ex)

        {

            CaughtException = ex;

        }


        testCase.Verify(ReturnValue, CaughtException);

    }

}
```

  
This test method will test every, *every*, test case we can think up for the test subject. It is easy to read and there is no duplication in the test fixture. No matter how complexe the test subject is the test fixture and test method will remain simple. The provider may be more complex. Here we are using a factory provider but the parameters could be provided by deserializing them from a file with either of the other two object providers. Notice how the argument testCase is used. It provides all data needed to prepare for the test, all the data to drive the test down the desired branch(s), and expected results. In this example a verify method is part of the testcase object much like a mock object. This is optional, the assertions could have been written in the test method. The parameter passed is the definition of the test case, hince the name of the parameter.

## Provide It Forward

The sole responsibility of an object provider is to provide a parameter for each call to the test method(s) decorated with the attribute TestWithEachObject. In the factory provider shown below the class ConditionalFactory implements IObjectProviderFactory. This interface defines only on member: `IContainer GetData()`. Remember that each parameter is all the data needed to drive a test case. There are three test cases defined here.

```
public class ConditionalFactory : IObjectProviderFactory

{

    #region IObjectProviderFactory Members

    public IContainer GetData()

    {

        ConditionalTestCaseContainer TestCases = new ConditionalTestCaseContainer();


        TestCases.NameTestCases.Add(this.NullNameCase());

        TestCases.NameTestCases.Add(this.EmptyNameCase());

        TestCases.NameTestCases.Add(this.GoodNameCase());


        return TestCases;

    }

    #endregion


    private NameTestCase NullNameCase()

    {

        NameTestCase TestCase = new NameTestCase();

        TestCase.TestCaseName = "Null Name";


        TestCase.Name = null;

        TestCase.ExpectedReturnValue = null;

        TestCase.ExpecteException = true;

        TestCase.ExpectedExceptionType = typeof(ArgumentNullException);

        TestCase.ExpectedExceptionMessage = String.Format("Value cannot be null.{0}Parameter name: name", Environment.NewLine);


        return TestCase;

    }

    private NameTestCase EmptyNameCase()

    {

        NameTestCase TestCase = new NameTestCase();

        TestCase.TestCaseName = "Empty Name";


        TestCase.Name = String.Empty;

        TestCase.ExpectedReturnValue = null;

        TestCase.ExpecteException = true;

        TestCase.ExpectedExceptionType = typeof(ArgumentException);

        TestCase.ExpectedExceptionMessage = "Name can not be blank.";


        return TestCase;

    }

    private NameTestCase GoodNameCase()

    {

        NameTestCase TestCase = new NameTestCase();

        TestCase.TestCaseName = "Good Name";


        TestCase.Name = "Bob";

        TestCase.ExpectedReturnValue = "Hello Bob.";

        TestCase.ExpecteException = false;


        return TestCase;

    }

}
```

  
Null Name is the first test case. It is designed to trace the first existing branch of the test subject. To enter the first conditional the parameter, name, to the test subject must be null.

```
public String ComplexeMethod(String name)

{

    if (name == null)

        throw new ArgumentNullException("name");

    if (name == String.Empty)

        throw new ArgumentException("Name can not be blank.");

    return String.Format("Hello {0}.", name);

}
```

  
So we set the property Name on the testcase to null. We also set the expected return value to null as the test subject will not have the opportunity to return. We set the expected exception type and message as well.

This procedure is repeated for each branch in the test subject.

## The Case of the Test Case

The test case, parameter, in this example is type NameTestCase. It could have been any type, it will probably correspond to the test fixture in a one to one relationship. At a bare minimum it is nothing more than a data structure. You should override the ToString method, the return value of ToString provides the name of the test run to the reporting framework. In this example it is also responsible for the assertions.

```
public void Verify(String returnValue, Exception exception)

{

    Assert.AreEqual(

        this.ExpectedReturnValue,

        returnValue,

        "Expected {0} but got {1} as a return value.", this.ExpectedReturnValue, returnValue);


    Assert.AreEqual(this.ExpecteException, exception != null, "An excpetion was expected.");


    if (this.ExpecteException)

    {

        Assert.AreEqual(

            this.ExpectedExceptionType,

            exception.GetType(),

            "Expected an exception of type {0} but got one of type {1}.",

                this.ExpectedExceptionType.Name,

                exception.GetType().Name);


        Assert.AreEqual(

            this.ExpectedExceptionMessage,

            exception.Message,

            "Expected exception message '{0}' but got '{1}'.",

                this.ExpectedExceptionMessage,

                exception.Message);

    }

}
```

## Basic Insight

The reason this works is there are a known set of controls and a known set of sensable effects. Not all controls may be used in a test case the same as not all effects maybe felt for every test case. The test case type needs to be written to hold data needed for the entire control set and data for describing expectations for the entire sensable effect set. The test method is responsible creating the test environment, the test subject, executing the test subject, and asserting the expectations were met. It uses the control set in the test case to create the environment and test subject as well as executing the test subject. It uses the expectation data to assert on the effects felt. A variation on this recipe is to have the test case provide the assertion on expectations.

## Resources

[MbUnit Extensions](http://jayflowers.com/joomla/index.php?option=com_content&task=view&id=17&Itemid=45 "http://jayflowers.com/joomla/index.php?option=com_content&task=view&id=17&Itemid=45")

[Solution Zip](http://jayflowers.com/joomla/index.php?option=com_remository&Itemid=33&func=fileinfo&id=7 "http://jayflowers.com/joomla/index.php?option=com_remository&Itemid=33&func=fileinfo&id=7")

[Conditional![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_1 "reveal")

```
public class Conditional

{

    public String ComplexeMethod(String name)

    {

        if (name == null)

            throw new ArgumentNullException("name");

        if (name == String.Empty)

            throw new ArgumentException("Name can not be blank.");

        return String.Format("Hello {0}.", name);

    }

}

[TestConditional![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_2 "reveal")

[TestFixture()]

[TestSubjectClassAttribute(TestSubject=typeof(TestSubject.Conditional))]

[ObjectFixture()]

[FactoryObjectProvider(typeof(ConditionalFactory))]

public class TestConditional

{


    [TestSubjectMemberAttribute(MemeberName="ComplexeMethod")]

    [TestWithEachObject()]

    public virtual void ComplexeMethod(NameTestCase testCase)

    {

        TestSubject.Conditional TestSubject = new TestSubject.Conditional();


        String ReturnValue = null;

        Exception CaughtException = null;

        try

        {

            ReturnValue = TestSubject.ComplexeMethod(testCase.Name);

        }

        catch (Exception ex)

        {

            CaughtException = ex;

        }


        testCase.Verify(ReturnValue, CaughtException);

    }


    [Test]

    public void NullName()

    {

        TestSubject.Conditional TestSubject = new TestSubject.Conditional();

        Exception CaughtException = null;

        try

        {

            TestSubject.ComplexeMethod(null);

        }

        catch (Exception ex)

        {

            CaughtException = ex;

        }

        Type ExpectedExceptionType = typeof(ArgumentNullException);

        String ExpectedExceptionMessage = String.Format("Value cannot be null.{0}Parameter name: name", Environment.NewLine);

        Assert.IsNotNull(CaughtException);

        Assert.AreEqual(

            ExpectedExceptionType,

            CaughtException.GetType(),

            "Expected an exception of type {0} but got one of type {1}.",

                ExpectedExceptionType.Name,

                CaughtException.GetType().Name);

        Assert.AreEqual(

            ExpectedExceptionMessage,

            CaughtException.Message,

            "Expected exception message '{0}' but got '{1}'.",

                ExpectedExceptionMessage,

                CaughtException.Message);

    }


    [Test]

    public void EmptyName()

    {

        TestSubject.Conditional TestSubject = new TestSubject.Conditional();

        Exception CaughtException = null;

        try

        {

            TestSubject.ComplexeMethod(String.Empty);

        }

        catch (Exception ex)

        {

            CaughtException = ex;

        }

        Type ExpectedExceptionType = typeof(ArgumentException);

        String ExpectedExceptionMessage = "Name can not be blank.";

        Assert.IsNotNull(CaughtException);

        Assert.AreEqual(

            ExpectedExceptionType,

            CaughtException.GetType(),

            "Expected an exception of type {0} but got one of type {1}.",

                ExpectedExceptionType.Name,

                CaughtException.GetType().Name);

        Assert.AreEqual(

            ExpectedExceptionMessage,

            CaughtException.Message,

            "Expected exception message '{0}' but got '{1}'.",

                ExpectedExceptionMessage,

                CaughtException.Message);

    }


    [Test]

    public void GoodName()

    {

        TestSubject.Conditional TestSubject = new TestSubject.Conditional();


        String ReturnValue = null;


        ReturnValue = TestSubject.ComplexeMethod("Bob");


        String ExpectedReturnValue = "Hello Bob.";

        Assert.AreEqual(

            ExpectedReturnValue,

            ReturnValue,

            "Expected {0} but got {1} as a return value.",

                ExpectedReturnValue,

                ReturnValue);

    }

}
```

[ConditionalFactory![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_3 "reveal")

```
public class ConditionalFactory : IObjectProviderFactory

{

    #region IObjectProviderFactory Members

    public IContainer GetData()

    {

        ConditionalTestCaseContainer TestCases = new ConditionalTestCaseContainer();


        TestCases.NameTestCases.Add(this.NullNameCase());

        TestCases.NameTestCases.Add(this.EmptyNameCase());

        TestCases.NameTestCases.Add(this.GoodNameCase());


        return TestCases;

    }

    #endregion


    private NameTestCase NullNameCase()

    {

        NameTestCase TestCase = new NameTestCase();

        TestCase.TestCaseName = "Null Name";


        TestCase.Name = null;

        TestCase.ExpectedReturnValue = null;

        TestCase.ExpecteException = true;

        TestCase.ExpectedExceptionType = typeof(ArgumentNullException);

        TestCase.ExpectedExceptionMessage = String.Format("Value cannot be null.{0}Parameter name: name", Environment.NewLine);


        return TestCase;

    }

    private NameTestCase EmptyNameCase()

    {

        NameTestCase TestCase = new NameTestCase();

        TestCase.TestCaseName = "Empty Name";


        TestCase.Name = String.Empty;

        TestCase.ExpectedReturnValue = null;

        TestCase.ExpecteException = true;

        TestCase.ExpectedExceptionType = typeof(ArgumentException);

        TestCase.ExpectedExceptionMessage = "Name can not be blank.";


        return TestCase;

    }

    private NameTestCase GoodNameCase()

    {

        NameTestCase TestCase = new NameTestCase();

        TestCase.TestCaseName = "Good Name";


        TestCase.Name = "Bob";

        TestCase.ExpectedReturnValue = "Hello Bob.";

        TestCase.ExpecteException = false;


        return TestCase;

    }

}
```

[ConditionalTestCaseContainer![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_4 "reveal")

```
public class ConditionalTestCaseContainer : IContainer

{


    private NameTestCaseCollection _Names;

    public NameTestCaseCollection NameTestCases

    {

        get

        {

            if (_Names == null)

                _Names = new NameTestCaseCollection();

            return _Names;

        }

        set

        {

            _Names = value;

        }

    }


    #region IContainer Members

    public System.Collections.ICollection ParameterCollection

    {

        get

        {

            if (_Names == null)

                _Names = new NameTestCaseCollection();

            return _Names;

        }

        set

        {

            _Names = (NameTestCaseCollection)value;

        }

    }

    #endregion

}
```

[NameTestCase![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_5 "reveal")

```
public class NameTestCase

{

    private String _TestCaseName;

    private String _Name;

    private String _ExpectedReturnValue;

    private Boolean _ExpecteException;

    private Type _ExpectedExceptionType;

    private String _ExpectedExceptionMessage;


    public String TestCaseName

    {

        get

        {

            return _TestCaseName;

        }

        set

        {

            _TestCaseName = value;

        }

    }

    public String Name

    {

        get

        {

            return _Name;

        }

        set

        {

            _Name = value;

        }

    }

    public String ExpectedReturnValue

    {

        get

        {

            return _ExpectedReturnValue;

        }

        set

        {

            _ExpectedReturnValue = value;

        }

    }

    public Boolean ExpecteException

    {

        get

        {

            return _ExpecteException;

        }

        set

        {

            _ExpecteException = value;

        }

    }

    public Type ExpectedExceptionType

    {

        get

        {

            return _ExpectedExceptionType;

        }

        set

        {

            _ExpectedExceptionType = value;

        }

    }

    public String ExpectedExceptionMessage

    {

        get

        {

            return _ExpectedExceptionMessage;

        }

        set

        {

            _ExpectedExceptionMessage = value;

        }

    }


    public void Verify(String returnValue, Exception exception)

    {

        Assert.AreEqual(

            this.ExpectedReturnValue,

            returnValue,

            "Expected {0} but got {1} as a return value.", this.ExpectedReturnValue, returnValue);


        Assert.AreEqual(this.ExpecteException, exception != null, "An excpetion was expected.");


        if (this.ExpecteException)

        {

            Assert.AreEqual(

                this.ExpectedExceptionType,

                exception.GetType(),

                "Expected an exception of type {0} but got one of type {1}.",

                    this.ExpectedExceptionType.Name,

                    exception.GetType().Name);


            Assert.AreEqual(

                this.ExpectedExceptionMessage,

                exception.Message,

                "Expected exception message '{0}' but got '{1}'.",

                    this.ExpectedExceptionMessage,

                    exception.Message);

        }

    }


    public override string ToString()

    {

        return this.TestCaseName;

    }


}
```

[NameTestCaseCollection![reveal hidden content](/doku/lib/plugins/folded/closed.gif)](#folded_6 "reveal")

```
public class NameTestCaseCollection:System.Collections.CollectionBase

{

    public NameTestCase this[int index]

    {

        get

        {

            return (NameTestCase) this.List[index];

        }

        set

        {

            this.List[index] = value;

        }

    }



    public void Add(NameTestCase item)

    {

        this.List.Add(item);

    }



    public bool Contains(NameTestCase item)

    {

        return this.List.Contains(item);

    }



    public void CopyTo(System.Array array, int index)

    {

        this.List.CopyTo(array, index);

    }



    public int IndexOf(NameTestCase item)

    {

        return this.List.IndexOf(item);

    }



    public void Insert(int index, NameTestCase item)

    {

        this.List.Insert(index, item);

    }



    public void Remove(NameTestCase item)

    {

        this.Remove(item);

    }


}
```

unit\_testing\_highly\_cyclomatic\_test\_subjects.txt · Last modified: 2006/10/14 21:11 by jflowers
