#!/usr/bin/python3

import argparse


parser = argparse.ArgumentParser(description="ejemplo parser")

parser.add_argument("-i", "--origen_archivo", type=str, required=True, help="nombre del origen")

parser.add_argument("-o", "--destino_archivo", type=str, default=1024, help="nombre del destino")

args = parser.parse_args()


