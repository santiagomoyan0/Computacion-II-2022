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
        else:
            print(f'{os.getpid()} - {os.getppid()}: {pares}')
            os._exit(0)

