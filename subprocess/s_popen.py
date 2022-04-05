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

if not error:
    date = dt.datetime.now()
    for_write = f"{date}: the command: {command}, it ran correctly"
    file_write = open(log_file, "a")
    file_write.write(for_write)
    file_write.write("\n")
    file_write.close() 
    
else:
    date = dt.datetime.now()
    for_write = f"{date}: >> {error}"
    file_write = open(log_file, "a")
    file_write.write(for_write)
    file_write.write("\n")
    file_write.close()
    
output_file.writelines("\n")
output_file.close()
