#!/usr/bin/python3

import argparse
import os

parser = argparse.ArgumentParser(description="textos")

parser.add_argument("-i", "--origen_archivo", type=str, required=True, help="nombre del origen")

parser.add_argument("-o", "--destino_archivo", type=str, default=1024, help="nombre del destino")

args = parser.parse_args()


if os.path.isfile(args.origen_archivo):
    archiv_origen = open(args.origen_archivo, "r")
    texto = archiv_origen.read()
    archiv_origen.close()
    archiv_destino = open(args.destino_archivo,"a+")
    archiv_destino.write(texto)
    archiv_destino.close()
    print ("Lo del origen ya se encuentra en el destino")