---
title: "MSTest Died!"
date: "2007-03-09"
draft: false
categories:
  - "Continuous Integration"
  - "Unit Testing"
aliases:
  - "/WordPress/?p=140"
  - "/WordPress/index.php?p=140"
params:
  wayback_url: "https://web.archive.org/web/20091010163349/http://jayflowers.com:80/WordPress/?p=140"
  original_url: "http://jayflowers.com:80/WordPress/?p=140"
  archived_from: Wayback Machine

---

## MSTest Died!

We have been encountering this from MSTest intermitently:

[mstest] Passed Dod.Chcsii.DataLayer.DataAccessHelper.ReaderPlayerTest.GetCharInvalidIndexTest  
[mstest] Run has the following issue(s):  
[mstest] The connection to the controller was lost.  
[mstest] Final Test Results:  
[mstest] Results Top Level Tests  
[mstest] ——- —————  
[mstest] Passed (run aborted) Dod.Chcsii.BusinessLayer.BusinessEntities.AntibodyTest.ConstructorIdNegativeInvalidNcid2Test

…

[mstest] Not Executed Dod.Chcsii.Shared.ParametersTest.Clone2  
[mstest] 0/598 test(s) Passed, 292 Passed (run aborted), 306 Not Executed  
[mstest] Summary  
[mstest] ——-  
[mstest] Test Run Error.  
[mstest] Passed (run aborted) 292  
[mstest] Not Executed 306  
[mstest] ————————-  
[mstest] Total 598  
[mstest] Results file: c:\Projects\dod.ahlta\Current\Build\Unit Test Reports\dod.ahltaUnitTests.xml  
[mstest] Run Configuration: Local Test Run


```batch
If we rerun it will succeed.  To help the developer know that they did not do something to fail the build and that it is a bug in the tool I added this to the build report.
```

![](images/2007/03/WindowsLiveWriter/MSTestDied_F609/CropperCapture%5B8%5D%5B3%5D.gif)
