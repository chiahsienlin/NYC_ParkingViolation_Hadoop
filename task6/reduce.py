#!/usr/bin/env python
import sys
curcnt = 1
curkey = None
buf = []
for line in sys.stdin:
    line = line.strip()
    key, cnt = line.split("\t", 1)
    if key == curkey:
        curcnt += 1
    else:
        if curkey:
            pid, state = curkey.split(",", 1)
            buf.append((pid, state, curcnt))
        curcnt = 1
        curkey = key
buf = sorted(buf, key=lambda b: b[2], reverse = True)
for i in range(0, 20):
    print("{0:s}, {1:s}\t{2:s}".format(buf[i][0], buf[i][1], str(buf[i][2])))
#for i in range(len(buf)-10, len(buf)):
#    print("{0:s}, {1:s}\t{2:s}".format(buf[i][0], buf[i][1], str(buf[i][2])))
