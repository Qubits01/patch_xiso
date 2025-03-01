#!/usr/bin/env python3

import sys
import os

def trimiso(iso, sizediff):
  with open(iso, 'r+b') as f:
    f.seek(sizediff, os.SEEK_END)
    data = f.read(-sizediff)
    if data.decode('utf-8').strip('\x00') != '':
      print('Error, truncate part contains data. Canceling.')
    f.seek(sizediff, os.SEEK_END)
    f.truncate()

def padiso(iso, sizediff):
  with open(iso, 'r+b') as f:
    f.seek(0, os.SEEK_END)
    padding = [0x0 for _ in range(sizediff)]
    f.write(bytearray(padding))  

def guesssize(isosize, valids):
  templist = []
  for v in valids:
    templist.append(abs(isosize-v))
  return valids[templist.index(min(templist))]


def zeropadl0_and_unstealth(iso, xgd3):
  video = 0xFD90000
  step = 0x1800
  ss = 16
  if xgd3:
    video = 0x2080000
    step = 0x9800
    ss = 32
  with open(iso, 'r+b') as f:
    f.seek(video - step)
    f.read(5)
    startoff = int.from_bytes(f.read(3), byteorder='big')
    f.read(5)
    endoff = int.from_bytes(f.read(3), byteorder='big')
    pfi_sectors = endoff - startoff + 1
    # print(hex(pfi_sectors))
    if pfi_sectors == 1:
      sys.exit('Error. No PFI info found. The ISO is probably already patched. If you are unsure, readd PFI info with abgx and rerun this script.')
    f.seek(pfi_sectors*0x800)
    padsize = video - pfi_sectors*0x800 #also zero stealth sectors
    #write chunks of 64 KB (32 sectors)
    chunk = [0x0 for _ in range(32 * 0x800)]
    while padsize >= len(chunk):
      f.write(bytearray(chunk))
      padsize -= len(chunk)
    if padsize > 0:
      f.write(bytearray(chunk[:padsize]))
      

def fixfilesize(iso):
  validsizes = [7834892288, 7835492352, 7838695424, 8738846720] # [wave 1, wave 2/3, wave 4+, xgd3]
  realsize = os.path.getsize(iso)
  if realsize in validsizes:
    print('OK')
    return
  else:
    goodsize = guesssize(realsize, validsizes)
    sizediff = goodsize-realsize
    if abs(sizediff) > 3803136:
      sys.exit('Size difference too big. Invalid file or the video partition is missing. Use abgx to add the video partition.')
      return
    if goodsize < realsize:
      print('\nOverdump. Trimming',-sizediff,'bytes...', end = '')
      trimiso(iso,goodsize-realsize)
      print('done')
    elif goodsize > realsize:
      print('\nUnderdump. Padding...',sizediff,'bytes...', end = '')
      padiso(iso, goodsize-realsize)
      print('done')


if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.exit("Usage: x360isopatch <isofile>")
  iso = sys.argv[1]
  if not os.path.isfile(iso):
    sys.exit('File not found:', iso)
  if os.path.getsize(iso) < 7000000000:
    sys.exit('Not a XBOX360 ISO file:', iso)
  print('Processing', iso)
  xgd3 = os.path.getsize(iso) > 8000000000
  print('Ckecking filesize...', end = '')
  fixfilesize(iso)
  print('Zeroing Sectors...', end = '')
  zeropadl0_and_unstealth(iso, xgd3)
  print('done\n')
