#!/usr/bin/env python
import sys
import os
from csv import reader
def isINT(value):
    try:
        int(value)
        return True
    except:
        return False

for s in reader(sys.stdin):
    filepath = os.environ.get("mapreduce_map_input_file")
    #if "park" in filepath:
    if len(s) == 22:
        #if(isINT(s[0]) == False or isINT(s[6]) == False or isINT(s[2]) == False):
        #    continue
        print ("{0:s}\t{1:s},{2:s},{3:s},{4:s},{5:s}".format(s[0],"1park",s[14],s[6],s[2],s[1]))
    #elif "open" in filepath:
    else:
        print ("{0:s}\t{1:s},{2:s},{3:s},{4:s},{5:s}".format(s[0],"2open","value","value","value","value"))
