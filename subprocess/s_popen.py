import subprocess as sp 
import sys
import getopt
import datetime as dt

opt,arg = getopt.getopt(sys.argv[:1], 'c:f:l:')

log_file = ''
command = ''
output_file = ''

for (op,ar) in opt:
    if op == '-c':
        command = ar
    elif op == '-f':
        output_file = open(ar, "a")
    elif op == '-l':
        log_file = ar

process = sp.Popen([command], stdout=output_file, stderr=sp.PIPE, shell=True, universal_newlines=True)
error = process.communicate()[1]
