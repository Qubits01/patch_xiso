# patch_xiso
Patches XBOX360 isos to match Redump.org entries

This little python script does mostly the same thing as "Xbox 360 Redump Patcher" by Starshadow.

In Detail, it has the following features:
* Does not rely on external tools or packages
* Checks for overdump/underdump of the iso and trims/pads the file accordingly
* Fills the L0 Video padding with zeros (done by abgx360 in Starshadow's script)
* Overwrites the stealth sectors with zeros (done by ppf patchfile in Starshadow's script)


Missing features to be implemented (please use abgx for that)
* Add/fix Video Partitions
* readding pfi info to the iso


Planned feature that the latest abgx Version (1.0.6) does not support
* add support for adding/fixing video partitions of wave 14+ games

Unfixable Issues
* AnyDVD style corruption
* Tampered files (e.g. some Scene releases have modified xex files of Japanese titles)
* maybe more

## Prerequisites
Python 3

## General usage
```
patch_xiso.py <isofile>
```
