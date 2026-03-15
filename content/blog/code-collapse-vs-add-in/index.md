---
title: "Code Collapse VS Add-in"
date: "2007-02-19"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=134"
  - "/WordPress/index.php?p=134"
params:
  wayback_url: "https://web.archive.org/web/20070307194554/http://jayflowers.com:80/WordPress/?p=134"
  original_url: "http://jayflowers.com:80/WordPress/?p=134"
  archived_from: Wayback Machine

---

## Code Collapse VS Add-in

I have always wanted an add-in for Visual Studio that collapses if, for, foreach, try, etc statements.  There is an add-in for VB.Net [Classify](http://visualstudiohacks.com/classify), I want one for C# and VB.Net.  There is [SmartOutline](http://submain.com/default.aspx?nav=products.smartoutline) too.  It, IMHO, requires too many actions to create a region (see the screen shots on their site).

I just could not find the one I wanted.  So I got up off my ass and set to work on writing one that did what I wanted.  It is by no means finished, it is good enough for now.  I had a LOT of help from Dustin Campbell.  He is one of the DevExpress developers.  Of course the easiest thing to do was create it as a DXCore plugin.  For now it is implemented as a command named “CreateHiddenRegion”.  So after you download the plugin, see the download link at the bottom, and place it in the DXCore plugin directory you need to add a shortcut to the command.  Creating a region is already Ctrl+3 so I mapped mine to Ctrl+Shift+3 as what is really going on is the create of a hidden region.  If you have no text selected the language element from beginning to end will be regionized.  If you have text selected the selection will be regionized.  If you execute the command on something already regionized it will unregionize it.

Update:  I changed things a little.  The banner for the region is no longer set so it appears as “…”.  As well the region begins at the end of the start line.  This way when the text of the first tine is changed the banner is not out of sync, not to metion that this seems to be the standard.

![CollapseElement](images/2007/02/CollapseElement.gif)

![CollapseSelection](images/2007/02/CollapseSelection.gif)

[Binary CR\_CodeFold.dll (24 KB)](images/2007/02/CR_CodeFold.dll)

[Source CR\_CodeFold.zip (12 KB)](images/2007/02/CR_CodeFold.zip)
