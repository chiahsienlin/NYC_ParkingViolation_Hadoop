#!/usr/bin/env python
import sys
curval = None
curkey = None
key = None
parkcnt = False
opencnt = False
for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t',1)
    filename  = val.split(",")[0]
    if curkey == key:
        if filename == "1park":
            parkcnt = True
        else:
            opencnt = True
    else:
        if curkey:
            cur_filename, plate_id, vio_precinct, vio_code, date = curval.split(',', 4)
            if parkcnt and opencnt == False and cur_filename == "1park":    
                print(curkey + "\t" + plate_id + ", " + vio_precinct + ", " + vio_code + ", " + date)
        if filename == "1park":
            parkcnt = True
            opencnt = False
        else:
            opencnt = True
            parkcnt = False
        curkey = key
        curval = val
if curkey == key:
    cur_filename, plate_id, vio_precinct, vio_code, date = curval.split(',', 4)
    if parkcnt and opencnt == False and cur_filename == "1park":
        print(curkey + "\t" + plate_id + ", " + vio_precinct + ", " + vio_code + ", " + date)
