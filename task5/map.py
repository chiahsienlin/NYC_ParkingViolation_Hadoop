#!/usr/bin/env python
import sys
from csv import reader
for s in reader(sys.stdin):
    print("{0:s},{1:s}\t{2:s}".format(s[14], s[16],"1"))
