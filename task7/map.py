#!/usr/bin/env python
import sys
from csv import reader
for s in reader(sys.stdin):
    violationCode = s[2]
    issueDate = s[1]
    print("{0:s}\t{1:s}".format(violationCode, issueDate))
