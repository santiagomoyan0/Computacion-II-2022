#!/usr/bin/python3

import getopt
import sys

(opt,arg) = getopt.getopt(sys.argv[1:], 'o:n:p:')

for (op,ar) in opt:
    if op == '-o':
        operador = ar
    if op == '-n':
        numero1 = int(ar)
    if op == '-m':
        numero2 = int(ar)

def calculadora(operador,numero1,numero2):
    if operador == '+':
        print(numero1+numero2)
    elif operador == '-':
        print(numero1-numero2)
    elif operador == '*':
        print(numero1*numero2)
    elif operador == '/':
        print(numero1/numero2)

if operador in ["+","-","*",""]:
    calculadora(operador,numero1,numero2)
else:
    print ("El operador es incorrecto, usar +, -, *, /")
    