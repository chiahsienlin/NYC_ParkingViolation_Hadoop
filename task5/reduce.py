#!/usr/bin/env python
import sys
maxcnt = 0
curcnt = 1
curkey = None
maxkey = None
for line in sys.stdin:
    line = line.strip()
    key, cnt = line.split("\t", 1)
    if key == curkey:
        curcnt += 1
        if curcnt > maxcnt:
            maxcnt = curcnt
            maxkey = key
    else:
        curcnt = 1
        curkey = key
pid, state = maxkey.split(",", 1)
print("{0:s}, {1:s}\t{2:s}".format(pid, state, str(maxcnt)))
