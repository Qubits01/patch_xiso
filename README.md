# patch_xiso
Patches XBOX360 isos to match Redump.org entries

This little python script basically does the same thing as "Xbox 360 Redump Patcher" by Starshadow.

In Detail, it has the following features:
* Does not rely on external tools
* Checks for overdump/underdump of the iso and trims/pads the file accordingly
* Fills the L0 Video padding with zeros
* Overwrites the stealth sectors with zeros

## Prerequisites
Python 3

## General usage
```
patch_xiso <isofile>
```
