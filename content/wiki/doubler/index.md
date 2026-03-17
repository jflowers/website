---
title: doubler
date: "2006-05-04"
draft: false
categories:
  - "Wiki"
aliases:
  - "/wiki/doubler/"
params:
  wayback_url: "https://web.archive.org/web/20060629125321//wiki/doubler/"
  original_url: "/wiki/doubler/"
  archived_from: Wayback Machine

---

[[[doubler](/wiki/doubler/)]]



# This page has moved and you will be redirected.



---

|  |  |  |
| --- | --- | --- |
| **[Install](/wiki/doulberinstall/ "doulberinstall")** | **[Usage](/wiki/doublerusage/ "doublerusage")** | **[Support](/wiki/doublersupport/ "doublersupport")** |

  


---

| Description |
| --- |
| Doubler is a code generator that makes unit testing easier. It is especially useful when working with legacy code. It is a [Reflector](http://aisto.com/roeder/dotnet/ "http://aisto.com/roeder/dotnet/") add-in, a tool already woven into your workflow. It will help you cleave dependencies apart, create test doubles, and write unit tests with little effort and less coding. |

  

| Features |
| --- |
| Doubler is a [Reflector](http://www.aisto.com/roeder/dotnet/ "http://www.aisto.com/roeder/dotnet/") add-in that helps with creating unit tests. It offers four code generators:   - **Recording Generator** – Use against an abstract type. It will create a [Recording Test Stub](http://tap.testautomationpatterns.com:8080/Recording%20Test%20Stub.html "http://tap.testautomationpatterns.com:8080/Recording%20Test%20Stub.html"). Recorders generated have the following features for each method on the subject type:    - Property named **Called** of type **Boolean** that records if the method was called.   - Properties for each parameter passed named in the following format **Passed<ParameterTypeName><ParameterName>** of the same type as the parameter.   - Property named **ReturnValue** of the same type as return type of the subject method. If subject method is void this property is not created. When the method is called the this value is returned.   - Property named **ExceptionToThrow** of type **Exception**. When the method is called if this property is not null the property value is thrown. - **Wrapper/Interface Generator** – Use against a concrete type. It will create a mirror interface of the subject type and an implementation of the interface that passes all calls to a private instance of the subject type. This can be used to help control dependencies, allowing unit tests to insert a test double in place of the subject (run the Recording Generator on the mirror interface). - **Fake Generator** - Use against an abstract type. It will create a [Fake Object](http://tap.testautomationpatterns.com:8080/Fake%20Object.html "http://tap.testautomationpatterns.com:8080/Fake%20Object.html"). - **Test Generator** – Use against a concrete type. It will generate a unit test fixture and test methods for each public method on the test subject. The test methods will contain a start on the unit test. |

  

| Download |
| --- |
| Version 0.5.5.12  0.5.5.12-doubler.zip *[Link removed: content not recovered during site restoration]*  0.5.5.12   - Fixed Wrapper/Interface: creates interface again, no duplicate members - Fixed Recorder: no duplicate members - Minor changes   0.5.5 Changes:   - Added logging tab. - Unit Test generator can now tracks calls to named parameters, writting test code for how each parameter is used. - No longer locks assemblies.   0.5 Changes:   - Added drag file control. - Wrapper class members are all final. - Recorder method names that are shared wiht Object are marked with override or overload. - Wrapper class internals are marked as private and not part of the wrapper interface.   Example: unit\_test\_patterns.zip *[Link removed: content not recovered during site restoration]* |

doubler.txt · Last modified: 2006/05/04 14:51 by jflowers
