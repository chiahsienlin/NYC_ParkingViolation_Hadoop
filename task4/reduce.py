#!/usr/bin/env python
import sys
cntNY = 0
cntOther = 0
curkey = None
for line in sys.stdin:
    line = line.strip()
    key, cnt = line.split("\t", 1)
    if curkey == key:
        if curkey == "NY":
            cntNY += 1
        else:
            cntOther += 1
    else:
        if curkey:
            if curkey == "NY":
                print("{0:s}\t{1:s}".format("NY", str(cntNY)))
            else:
                print("{0:s}\t{1:s}".format("Other", str(cntOther)))
        if key == "NY":
            cntOther = 0
            cntNY += 1
        else:
            cntNY = 0
            cntOther += 1
        curkey = key
if curkey == "NY":
    print("{0:s}\t{1:s}".format("NY", str(cntNY)))
else:
    print("{0:s}\t{1:s}".format("Other", str(cntOther)))
