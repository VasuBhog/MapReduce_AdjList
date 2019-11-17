#!/usr/bin/env python
"""mapper.py"""

import sys
import os

##LOCAL TEST
# with open('sample.txt','r') as f:
#         for line in f:
#             if line[0] == '#':
#                 pass
#             else:
#                 line = line.strip()
#                 x = line.split()
#                 if len(x) == 1:
#                     pass
#                 else:
#                     key = x[0]
#                     val = x[1]
#                     print(key,val)

# input comes from STDIN (standard input)
for line in sys.stdin:
    if line[0] == '#':
        pass
    else:
        line = line.strip()
        x = line.split()
        if len(x) == 1:
            pass
        else:
            key = x[0]
            val = x[1]
            print("%s\t%s" % (key,val))