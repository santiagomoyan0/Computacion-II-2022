#!/usr/bin/python3

import getopt
import sys

(opt,arg) = getopt.getopt(sys.argv[1:], 'o:n:p:')
if len(opt) != 3:
    print("enter correctly the number of parameters")
    exit()

