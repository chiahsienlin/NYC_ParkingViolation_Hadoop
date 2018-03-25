#!/usr/bin/env python
import sys
from csv import reader
for s in reader(sys.stdin):
    print("{0:s}\t{1:s},{2:s}".format(s[2], s[12], "1"))
