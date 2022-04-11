#!/usr/bin/python3
import os
import sys
import getopt
from os import getpid, fork, getppid

opt,arg = getopt.getopt(sys.argv[1:], 'n:hv')

def child():
    if os.fork():
        pares = sum([i for i in range(os.getpid()) if i % 2 == 0])
        if modo_verboso:
            print("Starting process")
            print(f'{os.getpid()} - {os.getppid()}: {pares}')
            print("Ending process")
            os._exit(0)
        else:
            print(f'{os.getpid()} - {os.getppid()}: {pares}')
            os._exit(0)
    os.wait()

modo_verboso = False
for (op,ar) in opt:
    if op == '-n':
        num_hjos = int(ar)
    elif op == '-h':
        print(" Modo verboso : -v , ayuda -h,")
    elif op == '-v':
        modo_verboso = True


for i in range(num_hjos):
        child()