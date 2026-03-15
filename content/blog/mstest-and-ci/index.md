---
title: MSTest and CI
date: "2006-08-19"
draft: false
categories:
  - "Continuous Integration"
  - "Unit Testing"
aliases:
  - "/WordPress/?p=67"
  - "/WordPress/index.php?p=67"
params:
  wayback_url: "https://web.archive.org/web/20090223193804/http://jayflowers.com:80/WordPress/?p=67"
  original_url: "http://jayflowers.com:80/WordPress/?p=67"
  archived_from: Wayback Machine

---

## MSTest and CI

The team I am working with at the moment has decided to use MSTest as their xUnit framework.  Part of  my job has been to help get a build server up and running.  CIFactory is the solution we are using for our build server; this includes CCNET and NAnt.  In creating a CIFactory package for MSTest I tryed to use the commandline to control mstest.exe first.  I found that there are two ways to provide mstest with a list of test assemblies: through a metadata file or commandline switch testcontainer.  I know that th project I was working on was big and would have more test assemblies than the commandline would allow (space wise) so I immediately looked into how to control the metadata file.  Unfortunately a Testers or Architects license of VSTS is needed to save a list of tests to be executed and the file format is complex.  Next I thought what is mstest.exe sub main doing and opened it up in Reflector.  It did not look that complicated so I decided to build a NAnt task to drive MSTest.  This would relieve the commandline size restriction.


```xml
<mstest resultsfile=“${UnitTest.ReportFolder}\${UnitTest.ReportFile}“ runconfig=“${UnitTest.RunConfig}“ >  
    <testcontainers>  
        <include name=“${UnitTest.TestPath}\\*\*\bin\Test.\*.dll“ />  
    </testcontainers>  
</mstest>
```

Notice how as long as the dev team places all test projects in the unit test directory, specified in the property UnitTest.TestPath, and follows the naming convetion Test.\*.dll that script will not need alteration.  This makes for light maintenance.

So lets take a look at mstest.exe sub main to get an idea of what the NAnt task is going to need to do.

```
[STAThread]
private static int Main(string[] args)
{
      Runner.SetUICulture();
      using (Executor executor1 = new Executor())
      {
            Parser parser1 = new Parser(args);
            if (!CommandFactory.InterpretCommandLineSwitches(executor1, parser1, CommandFactory.SupportedCommandInfoForCommandLine, Runner.ApplicationLabel))
            {
                  HelpCommand command1 = new HelpCommand();
                  command1.HelpType = HelpCommand.HelpCommandType.ShortHelp;
                  command1.Execute(null);
                  return 1;
            }
            new ControlC(executor1);
            NativeMethods.ControlCHandlerDelegate delegate1 = new NativeMethods.ControlCHandlerDelegate(ControlC.Handler);
            NativeMethods.SetConsoleCtrlHandler(delegate1, true);
            bool flag1 = executor1.Execute();
            NativeMethods.SetConsoleCtrlHandler(delegate1, false);
            if (flag1)
            {
                  return 0;
            }
            return 1;
      }
}
```

Looks like Executor is the main class we will be working with so lets take a look at it.

```
internal class Executor : IDisposable
{
      public Executor();
      public Executor(Task task);
      public void AbortExecution();
      public void Add(Command command);
      public static bool CommandExists(ArrayList allCommands, Type commandType);
      public void Dispose();
      public bool Execute();
      private void Init();
      public bool IsCommandExist(Type commandType);
      public static bool TestSupplierCommandExists(ArrayList commandsList);
      public void ValidateCommands();

      public ExecutorStructure Commands { get; }
      public static string CustomResultFileName { get; set; }
      public static Output Output { get; set; }
      public static ResultManager ResultManagerInstance { get; }
      public TmiAdapter TmiAdapter { get; }

      private ExecutorStructure m_commands;
      private bool m_executionAborted;
      private static string m_fileName;
      private static Output m_output;
      private static ResultManager m_resultManager;
      private TmiAdapter m_tmiAdapter;
}
```

Ouch it’s internal.  At this point I knew that I was backed into a corner.  I knew that I could use reflection to create and drive these objects so I kept reading the code to figure out which classses I was going to need to work with.  I found that these were the classes that I was going to need to work with:

- Microsoft.VisualStudio.TestTools.CommandLine.Executor
- Microsoft.VisualStudio.TestTools.CommandLine.ResultsOutputCommand
- Microsoft.VisualStudio.TestTools.CommandLine.RunConfigCommand
- Microsoft.VisualStudio.TestTools.CommandLine.NoIsolationCommand

After some experimentation with reflection I decided that I should write reflection wrappers around these classes.  Idea being to encapsulate the reflection offering up an interface that looked normal to the consumer.  Take for example the Executor wrapper class.

```
public class Executor

{


    private Object _WrappedSubject;

    private MethodInfo _AddCommandMethod;

    private MethodInfo _ExecuteMethod;

    private MethodInfo _ValidateCommandsMethod;

    private PropertyInfo _OutputProperty;


    private PropertyInfo OutputProperty

    {

        get

        {

            if (_OutputProperty == null)

            {

                _OutputProperty = this.WrappedSubject.GetType().GetProperty(”Output”);

            }

            return _OutputProperty;

        }

    }


    private object Output

    {

        set

        {

            this.OutputProperty.SetValue(this.WrappedSubject, value, null);

        }

    }


    private MethodInfo ValidateCommandsMethod

    {

        get

        {

            if (_ValidateCommandsMethod == null)

            {

                _ValidateCommandsMethod = this.WrappedSubject.GetType().GetMethod(”ValidateCommands”);

            }

            return _ValidateCommandsMethod;

        }

    }


    public void ValidateCommands()

    {

        this.ValidateCommandsMethod.Invoke(this.WrappedSubject, null);

    }


    private MethodInfo ExecuteMethod

    {

        get

        {

            if (_ExecuteMethod == null)

            {

                _ExecuteMethod = this.WrappedSubject.GetType().GetMethod(”Execute”);

            }

            return _ExecuteMethod;

        }

    }


    public Boolean Execute()

    {

        return (Boolean)this.ExecuteMethod.Invoke(this.WrappedSubject, null);

    }


    private MethodInfo AddCommandMethod

    {

        get

        {

            if (_AddCommandMethod == null)

            {

                _AddCommandMethod = this.WrappedSubject.GetType().GetMethod(”Add”);

            }

            return _AddCommandMethod;

        }

    }


    public void Add(Command command)

    {

        this.AddCommandMethod.Invoke(this.WrappedSubject, new object[1] { command.UnWrapObject });

    }


    private Object WrappedSubject

    {

        get

        {

            if (_WrappedSubject == null)

            {

                foreach (Type Canidate in TestToolsHelper.CommandLineAssembly.GetTypes())

                {

                    if (Canidate.FullName == “Microsoft.VisualStudio.TestTools.CommandLine.Executor”)

                    {

                        _WrappedSubject = Activator.CreateInstance(Canidate, null);

                        break;

                    }

                }

            }

            return _WrappedSubject;

        }

    }


    public Executor()

    {


    }


    public Executor(Boolean verbose)

    {

        if (!verbose)

            this.Output = TestToolsHelper.CreateInstance(”Microsoft.VisualStudio.TestTools.CommandLine.EmptyOutput”);

    }

}
```

All the reflection is hiden allowing the NAnt task to easily drive the execution of mstest.  Here is the ExecuteTask override.

```
protected override void ExecuteTask()

{

    Boolean Result = false;

    this.SubvertConsoleOutput();

    try

    {

        Executor TestExecutor = new Executor(this.Verbose);


        foreach (String File in AssembliesFileNames)

        {

            TestExecutor.Add(new TestContainerCommand(File));

        }


        TestExecutor.Add(new ResultsOutputCommand(this.ResultsFile));

        if (!String.IsNullOrEmpty(this.RunConfig))

            TestExecutor.Add(new RunConfigCommand(this.RunConfig));


        TestExecutor.Add(new NoIsolationCommand());


        TestExecutor.ValidateCommands();


        Result = TestExecutor.Execute();

    }

    finally

    {

        this.RestorConsoleOutput();

        this.LogCapturedOutput();

    }

    if (!Result && this.FailOnTestFailure)

        throw new BuildException(”At least one test failed!”);

}
```

Because the reflection has been encapsulated this method is simple and easy to read.  There was one other interesting thing that I felt was needed.  Microsoft’s Executor class was outputing some information to the console.  I wanted this info to be logged when the verbose attribute was true.  After reading the code in Reflector I found that I had two options; figure out how to: inherit from the internally marked Output class or subvert the Console output during the use of the Executor object.  I went with the console subversion.  Notice the calls to SubvertConsoleOutput, RestorConsoleOutput, and LogCapturedOutput in the listing of ExecuteTask.


```csharp
private void SubvertConsoleOutput()  

{

    this.StandardOut = Console.Out;

    FieldInfo OutFieldInfo = typeof(Console).GetField(”_out”, BindingFlags.Static | BindingFlags.NonPublic);

    OutFieldInfo.SetValue(null, this.Captured);

}


private void RestorConsoleOutput()

{

    FieldInfo OutFieldInfo = typeof(Console).GetField(”_out”, BindingFlags.Static | BindingFlags.NonPublic);

    OutFieldInfo.SetValue(null, this.StandardOut);

}
```

I read the code in Reflector for Console and it seemed that the best thing to do was to replace the backing stream.  I save off the original stream so that it can be returned after the subversion is no longer needed.  The replacement stream is a StringWriter wich is dumped into the log when LogCapturedOutput is called.  I wondered if it was possible to inherit from an internally marked class in IL but I thought that was going overboard for the problem at hand.  I had never had good reason to use reflection is this was before.  This experience has shown me that when it is needed there is a pattern to how wrapper classes can be created.  It is repetative and could easily be turned into a Reflector plugin with Refly.

Here is a zip containing the [MSTest CIFactory Package](http://jayflowers.com/joomla/index.php?option=com_remository&Itemid=33&func=select&id=11).  It includes:

- MsTestSummary.xsl
- UnitTest.Properties.xml
- UnitTest.Target.xml
- VSTS.Tasks.dll
