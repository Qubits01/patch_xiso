# patch_xiso
Patches XBOX360 isos to match Redump.org entries

This little python script does mostly the same thing as "Xbox 360 Redump Patcher" by Starshadow.

In Detail, it has the following features:
* Does not rely on external tools or packages
* Checks for overdump/underdump of the iso and trims/pads the file accordingly (new feature)
* Fills the L0 Video padding with zeros (done by abgx360 at Starshadow's script)
* Overwrites the stealth sectors with zeros (done by ppf patchfile at Starshadow's script)

## Prerequisites
Python 3

## General usage
```
patch_xiso.py <isofile>
```
