import os
import argparse, string, time

parser = argparse.ArgumentParser()

parser.add_argument('-n', type=int, help="Generamos un n° de procesos dependiendo el número ingresado")

parser.add_argument('-r', type=int, help="Almacena en el archivo su letra según el número ingresado")

parser.add_argument('-f', help="Path del archivo con el cual vamos a trabajar")

parser.add_argument('-v', action="store_true", help="Ingresa en modo verboso")

args = parser.parse_args()


archivo = open(args.f, 'w+')
abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

for i in range(args.n):
    if os.fork() == 0:
        if args.v:
            print(f"Proceso{os.getpid()} escribiendoletra '{abecedario[i]}'")
        for r in range(args.r):
            archivo.write(abecedario[i])
            archivo.flush()
        time.sleep(1)
        os._exit(0)

for i in range(args.n):
    os.wait()
archivo2 = open(args.f, 'r')
print(archivo2.readlines()) 