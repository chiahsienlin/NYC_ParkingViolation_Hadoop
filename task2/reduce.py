#!/usr/bin/env python                                                          
import sys
cnt = 0
curkey = 0
for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t', 1)
    val = int(val)
    key = int(key)
    if curkey == key:
        cnt = cnt + val
    else:
        if cnt:
            print('{0:s}\t{1:s}'.format(str(curkey), str(cnt)))
        curkey = key
        cnt = val
if cnt:
    print('{0:s}\t{1:s}'.format(str(curkey), str(cnt)))
