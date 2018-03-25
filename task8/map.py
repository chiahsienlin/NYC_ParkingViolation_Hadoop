#!/usr/bin/env python
import sys
from csv import reader
for s in reader(sys.stdin):
    make = s[20]
    color = s[19]
    if color and make:
        print("{0:s},{1:s}\t{2:d}".format("1make", make, 1))
        print("{0:s},{1:s}\t{2:d}".format("2color", color, 1))
    elif make:
        print("{0:s},{1:s}\t{2:d}".format("1make", make, 1))
        print("{0:s},{1:s}\t{2:d}".format("2color", "NONE", 1))
    elif color:
        print("{0:s},{1:s}\t{2:d}".format("1make", "NONE", 1))
        print("{0:s},{1:s}\t{2:d}".format("2color", color, 1))
    else:
        print("{0:s},{1:s}\t{2:d}".format("1make", "NONE", 1))
        print("{0:s},{1:s}\t{2:d}".format("2color","NONE", 1))
