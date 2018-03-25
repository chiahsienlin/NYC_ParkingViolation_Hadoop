#!/usr/bin/env python
import sys
curkey = None
weekdaycnt = 0.0
weekendcnt = 0.0
for line in sys.stdin:
    line = line.strip()
    key, date = line.split("\t", 1)
    day = date.split("-")[-1]
    day = int(day)
    if key == curkey:
        if (day % 7 == 5) or (day % 7 == 6):
            weekendcnt += 1.0
        else:
            weekdaycnt += 1.0
    else:
        if curkey:
            print("{0:s}\t{1:.2f}, {2:.2f}".format(curkey, weekendcnt/8.0, weekdaycnt/23.0))
        if (day % 7 == 5) or (day % 7 == 6):
            weekendcnt = 1.0
            weekdaycnt = 0.0
        else:
            weekdaycnt = 1.0
            weekendcnt = 0.0
        curkey = key
if curkey == key:
    print("{0:s}\t{1:.2f}, {2:.2f}".format(curkey, weekendcnt/8.0, weekdaycnt/23.0))

