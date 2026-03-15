---
title: using_junctions_to_manage_a_development_environment
date: "2006-10-14"
draft: false
categories:
  - "Wiki"
aliases:
  - "/doku/doku.php?id=using_junctions_to_manage_a_development_environment"
params:
  wayback_url: "https://web.archive.org/web/20190823134728/http://jayflowers.com/doku/doku.php?id=using_junctions_to_manage_a_development_environment"
  original_url: "http://jayflowers.com/doku/doku.php?id=using_junctions_to_manage_a_development_environment"
  archived_from: Wayback Machine

---

[[[using\_junctions\_to\_manage\_a\_development\_environment](/doku/doku.php?id=using_junctions_to_manage_a_development_environment&do=backlink)]]

[JayFlowers](/doku/doku.php?id= "[ALT+H]")

Trace: » [using\_junctions\_to\_manage\_a\_development\_environment](/doku/doku.php?id=using_junctions_to_manage_a_development_environment "using_junctions_to_manage_a_development_environment")

Junctions are symbolic links and have been supported since Win2k in NTFS. The OS provides no ways to manage junctions. There is a tool in the Win2K resource and there is a tool provided by Sysinternals. Below is a screen shot of part of a development environment structure.

[![targetjunction.jpeg](/doku/lib/exe/fetch.php?w=&h=&cache=cache&media=targetjunction.jpeg "targetjunction.jpeg")](/doku/lib/exe/detail.php?id=using_junctions_to_manage_a_development_environment&cache=cache&media=targetjunction.jpeg "targetjunction.jpeg")

Notice the icon overlays of the chain links. This functionality is provided by Travis Illig’s Junction Shell Extensions. With out this you will not be able to see a difference between a regular folder and a junction. Below is are screen shots of how to use the Sysinternals tool to display junction points and the properties of a junction with Junction Shell Extensions.

[![targetjuntionproperties.jpeg](/doku/lib/exe/fetch.php?w=&h=&cache=cache&media=targetjuntionproperties.jpeg "targetjuntionproperties.jpeg")](/doku/lib/exe/detail.php?id=using_junctions_to_manage_a_development_environment&cache=cache&media=targetjuntionproperties.jpeg "targetjuntionproperties.jpeg")

[![displayjunction.jpeg](/doku/lib/exe/fetch.php?w=&h=&cache=cache&media=displayjunction.jpeg "displayjunction.jpeg")](/doku/lib/exe/detail.php?id=using_junctions_to_manage_a_development_environment&cache=cache&media=displayjunction.jpeg "displayjunction.jpeg")

This functionality shows it’s usefulness when you are dealing with third party dependencies. The component suite VistaDB is a good example. There are two dlls of interest in VistaDB, one is in the GAC and the other is not. The directory path to the unregistered assembly can cause problems if just one developer installs VistaDB to a different directory than the rest of the team. I you follow the principle that the third party directory should contain all dependencies, junctions can greatly there as well. Developers will not be forced into installing Component suites into the third party directories of the projects they are working on. Developers can use the junction console to map a junction point from where they have installed the component suite to the projects third party directory. Below is screen shot of mapping the component suite Northwoods Software from the installation directory “C:\Projects\RegisteredThirdParty\Northwoods Software” to the project EFPlugins’s third party directory.

[![createjunction.jpeg](/doku/lib/exe/fetch.php?w=&h=&cache=cache&media=createjunction.jpeg "createjunction.jpeg")](/doku/lib/exe/detail.php?id=using_junctions_to_manage_a_development_environment&cache=cache&media=createjunction.jpeg "createjunction.jpeg")

[http://www.paraesthesia.com/blog/comments.php?id=801\_0\_1\_0\_C](http://www.paraesthesia.com/blog/comments.php?id=801_0_1_0_C "http://www.paraesthesia.com/blog/comments.php?id=801_0_1_0_C")

[http://www.sysinternals.com/utilities/junction.html](http://www.sysinternals.com/utilities/junction.html "http://www.sysinternals.com/utilities/junction.html")

using\_junctions\_to\_manage\_a\_development\_environment.txt · Last modified: 2006/10/14 21:09 by jflowers
