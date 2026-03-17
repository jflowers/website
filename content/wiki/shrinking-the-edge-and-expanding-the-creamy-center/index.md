---
title: shrinking_the_edge_and_expanding_the_creamy_center
date: "2006-10-14"
draft: false
categories:
  - "Wiki"
aliases:
  - "/wiki/shrinking-the-edge-and-expanding-the-creamy-center/"
params:
  wayback_url: "https://web.archive.org/web/20190823134932//wiki/shrinking-the-edge-and-expanding-the-creamy-center/"
  original_url: "/wiki/shrinking-the-edge-and-expanding-the-creamy-center/"
  archived_from: Wayback Machine

---

[[[shrinking\_the\_edge\_and\_expanding\_the\_creamy\_center](/wiki/shrinking-the-edge-and-expanding-the-creamy-center/)]]



Trace: » [shrinking\_the\_edge\_and\_expanding\_the\_creamy\_center](/wiki/shrinking-the-edge-and-expanding-the-creamy-center/ "shrinking_the_edge_and_expanding_the_creamy_center")

## Introduction

In the article [Introduction to Unit Testing](/wiki/shrinking-the-edge-and-expanding-the-creamy-center/ "/wiki/shrinking-the-edge-and-expanding-the-creamy-center/") a recipe was identified that could test any class in a system except for the edge. The recipe depends on the test subject knowing of other types through abstractions. The abstraction allows for indirection to be used to insert a test double. This methodology of testing is known as interaction based testing.

**Interaction Based Recipe:**

1. Does the test subject interact through abstractions? If not perform safe refactorings till compliant.
2. Write doubles for each abstract type the test subject interacts with. Ignore if using nMock or the like.
3. Create Test Method.

   1. Create any parameters need for creation of the test subject.
   2. Create instance of test subject.
   3. Create all doubles the test subject method will interact with that were not passed in the creation of the test subject.
   4. Set return values for expected interactions.
   5. If interactions occur through the test subjects public properties and or fields populate with the correct doubles.
   6. Call the test subject method passing doubles and or other values.
   7. Assert on expected interactions with doubles and or test subject public properties and fields.

The edge of a system has external dependencies and most types exposed in third party libraries are not abstract. This prevents test double substitution. The Warehouse class in the previous article was dependent on a database. This tight coupling to a database means that we can not isolate Warehouse. Remember that a unit test exercises just one class. This article will explore the use of the Adaptor Pattern and code generation to shrink the edge of your system and expand the creamy center. The creamy center being the sweet spot where types are easily isolated for unit testing.

|  |
| --- |
| Figure 1 |

## Test Subject

To keep the examples simple and easy for you to get working on your machine the file system will be used instead of a database. The test subject is going to be *very* simple in the article: I want the focus to stay on how to apply indirection. It uses a FileInfo object to create a text file and write one line, “Hello World!”.

```
public void UseIt(FileInfo file)

{

    using (StreamWriter Writer = file.CreateText())

    {

        Writer.WriteLine("Hello World!");

    }

}
```

  
Think about what this test subject will be like to test. You should be listing the responsibilities of the test subject in your head.   
**Responsibilities:**

1. Create a File specified by the file parameter.
2. Write one line of the text “Hello World!\n”.
3. Close the File.


```batch
If the file exists then #1 must have been satisfied. If we can open the file to read the contents then #3 must have been satisfied. We would need to compare the contents to what we expect for #2, “Hello Word!\n”.
```

## Testing With the Real Deal

Below is a simple test using the file system.

```
[Test]

public void TestUseItWithTheFileSystem()

{

    FileConsumer TestSubject = new FileConsumer();


    if (!Directory.Exists(@"C:\Temp"))

        Directory.CreateDirectory(@"C:\Temp");

    if (File.Exists(@"C:\Temp\TestFile.txt"))

        File.Delete(@"C:\Temp\TestFile.txt");


    FileInfo TestFile = new FileInfo(@"C:\Temp\TestFile.txt");


    TestSubject.UseIt(TestFile);


    String FileName = @"C:\Temp\TestFile.txt";

    Assert.IsTrue(File.Exists(FileName));

    String Contents;

    using (TextReader Reader = File.OpenText(FileName))

        Contents = Reader.ReadToEnd();

    Assert.AreEqual(string.Format("Hello World!{0}", System.Environment.NewLine), Contents);

}
```

  
First we make an instance of the test subject. The test subject will be creating a file in the C:\Temp directory. We can’t count on that directory existing so the test must check to see if it exists and if not create it. If the file that the test subject creates exists it needs to be deleted. We don’t want a previously successful test run to mask a problem. I don’t want to get crazy with making my test code super robust but there are already potiential problems with concurrency. We are hoping that there is no other process on the system vieing for these resources. Next we create the FileInfo object and pass it to the test subject’s method UseIt. The first assertion is on the existence of the file. The second implied assertion is in opening the file to read. To assert on the contents we read the file into a string variable and compare. Don’t forget the new line character.

## Finding the Knobs and Dials

|  |
| --- |
| Sidebar |
| [It is Always Indirectionreveal hidden content](#folded_1 "reveal")  Well it’s all most always indirection. The answer that is to why is it hard to unit test this test subject. This is due to tight coupling, specifically interfaces knowing of non-abstract types. When implementations are tightly coupled you can not isolate one from the tightly coupled mass. When indirection isn’t the answer it is usually the case that you have a class that is trying to do too much and needs to be split into multiple classes. With all this encouragement to use abstractions there is a need to mention: you need to temper your application of this tool. Interfaces are more difficult to abuse than abstract classes. Please learn the appropriate use of each. One more hint. Testing of the Template Method Pattern is not simple, testing of aggregation is easier. |


```batch
If you knew of a way to test that was easier for you and was not brittle (e.g. resource contention issues) I bet you would use it. Well here is the key: indirection, same as last time. To make things better we need to introduce some indirection. But where and why? It is needed in front of the file system. Specificaly the FileInfo type, the StreamWriter type is abstract. It is needed to allow substitution of test doubles[1)](#fn__1). This is the control that we can exert to shrink the edge and expand the creamy center.
```

|  |
| --- |
| Figure 2 |

  

See the tight coupling to the FileInfo type, test subject is on the edge.

|  |
| --- |
| Figure 3 |

## Wrappers and Test Doubles

How can indirection be introduced when not all the file system classes are derivatives and I don’t own the file system code to refactor it. Use the Adapter Pattern[2)](#fn__2) to introduce the indirection. Create a new interface that mimics the public interface of the type in question, FileInfo for this example. Create a new class, a wrapper, that implements the mimicking interface. It will need to hold an instance of the wrappie and pass all calls to it.

|  |
| --- |
| Figure 4 |

  

Will this indirection the test subject will need to alter a bit. Notice only the type of the parameter file was changed from FileInfo to IWrapperFileInfo.

```
public void UseIt(IWrapperFileInfo file)

{

    using (StreamWriter Writer = file.CreateText())

    {

        Writer.WriteLine("Hello World!");

    }

}
```

  
Now the test can adjust to use Recording Test Stubs[3)](#fn__3).

```
[Test]

public void TestUseItWithRecorders()

{

    FileConsumer TestSubject = new FileConsumer();

    RecorderIWrapperFileInfo FileRecorder = new RecorderIWrapperFileInfo("A Bogas Bunch of Junk!");

    RecorderStreamWriter Streamrecorder = new RecorderStreamWriter(new MemoryStream());

    FileRecorder.Recordings.CreateTextRecording.ReturnValue = Streamrecorder;

    TestSubject.UseIt(FileRecorder);

    Assert.IsTrue(Streamrecorder.Recordings.WriteLineStringRecording.Called);

    Assert.AreEqual("Hello World!", Streamrecorder.Recordings.WriteLineStringRecording.PassedStringvalue);

    Assert.IsTrue(Streamrecorder.Recordings.CloseRecording.Called);

}
```

  
Notice that it is even a few lines shorter than the test against the file system types. This certainly introduces the needed indirection and will make writing the unit test easier but three new types were just created. Overall this does not look like an easier solution yet. This is nothing new. Michael C. Feathers documented this technique as **Skin and Wrap the API**[4)](#fn__4) giving the following advice:

Skin and Wrap the API is good in these circumstances:

- The API is relatively small.
- You want to completely separate out dependencies on a third-party library.
- You don’t have tests, and you can’t write them because you can’t test through the API.
