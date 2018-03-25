#!/usr/bin/env python
import sys
from csv import reader
for s in reader(sys.stdin):
    if(s[16] == "NY"):
        print("{0:s}\t{1:s}".format(s[16], "1"))
    else:
        print("{0:s}\t{1:s}".format("Other", "1"))

