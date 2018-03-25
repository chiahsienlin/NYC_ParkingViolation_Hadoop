#!/usr/bin/env python
import sys
colorcnt = 0
makecnt = 0
curkey = None
for line in sys.stdin:
    line = line.strip()
    key, cnt = line.split("\t", 1)
    K_M, val = key.split(",", 1)
    if curkey == key:
        if K_M == "1make":
            makecnt += 1
        else:
            colorcnt += 1
    else:
        if curkey:
            cur_K_M, cur_val = curkey.split(",",1)
            if cur_K_M == "1make":
                print("{0:s}\t{1:s}, {2:d}".format("vehicle_make", cur_val, makecnt))
            else:
                print("{0:s}\t{1:s}, {2:d}".format("vehicle_color", cur_val, colorcnt))
        if K_M == "1make":
            makecnt = 1
            colorcnt = 0
        else:
            colorcnt = 1
            makecnt = 0
        curkey = key
if curkey == key:
    cur_K_M, cur_val = curkey.split(",",1)
    if cur_K_M == "1make":
        print("{0:s}\t{1:s}, {2:d}".format("vehicle_make", cur_val, makecnt))
    else:
        print("{0:s}\t{1:s}, {2:d}".format("vehicle_color", cur_val, colorcnt))
