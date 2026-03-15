---
title: "Shh, Keep it Quiet"
date: "2007-02-15"
draft: false
categories:
  - "Continuous Integration"
aliases:
  - "/WordPress/?p=133"
  - "/WordPress/index.php?p=133"
params:
  wayback_url: "https://web.archive.org/web/20070307194928/http://jayflowers.com:80/WordPress/?p=133"
  original_url: "http://jayflowers.com:80/WordPress/?p=133"
  archived_from: Wayback Machine

---

## Shh, Keep it Quiet

Sometimes you just wish there was a way to make it secret.  It was really simple.

```
<target name=“test“ >
  <exec program=“ping“ commandline=“localhost“ output=“c:tempping.log“ />
  <echo message=“before“/>
  <loglevel level=“None“>
    <do>
      <exec program=“ping“ commandline=“localhost“ output=“c:tempping.log“/>
    </do>
  </loglevel>
  <echo message=“after“/>
</target>

test:

     [exec] Starting ‘ping (localhost)’ in ‘C:\Projects\CI Factory\Current\Product\nAnt Scratch’  
     [exec]   
     [exec]   
     [exec] Pinging jflowersxp5.CHCSII.COM [::1] with 32 bytes of data:  
     [exec]   
     [exec]   
     [exec]   
     [exec] Reply from ::1: time<1ms   
     [exec]   
     [exec] Reply from ::1: time<1ms   
     [exec]   
     [exec] Reply from ::1: time<1ms   
     [exec]   
     [exec] Reply from ::1: time<1ms   
     [exec]   
     [exec]   
     [exec]   
     [exec] Ping statistics for ::1:  
     [exec]   
     [exec]     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),  
     [exec]   
     [exec] Approximate round trip times in milli-seconds:  
     [exec]   
     [exec]     Minimum = 0ms, Maximum = 0ms, Average = 0ms  
     [exec]   
     [echo] before  
     [echo] after

BUILD SUCCEEDED

Total time: 7.1 seconds.

[TaskName(“loglevel”)]
public class LogLevelTask : Task
{
    private Level _LogLevel;
    private TaskContainer _Tasks;

    [BuildElement(“do”, Required = true)]
    public TaskContainer Tasks
    {
        get
        {
            return _Tasks;
        }
        set
        {
            _Tasks = value;
        }
    }

    [TaskAttribute(“level”, Required = true)]
    public Level LogLevel
    {
        get
        {
            return _LogLevel;
        }
        set
        {
            _LogLevel = value;
        }
    }

    protected override void ExecuteTask()
    {
        Level OldLevel = this.Project.Threshold;
        this.Project.Threshold = this.LogLevel;
        this.Tasks.Execute();
        this.Project.Threshold = OldLevel;

    }
}
```
