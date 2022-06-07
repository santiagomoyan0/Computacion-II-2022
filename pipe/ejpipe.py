import getopt, sys, os

opt,arg = getopt.getopt(sys.argv[1:], 'f:')


lines = []

for (op,ar) in opt:
    if op == '-f':
        file_read = ar

def leer():
    texto = open(file_read, 'r')
    return texto.readlines()

def hijo(linea):
    if not os.fork():
        os.write(w, linea[::-1].encode('ascii'))
        os._exit(0)
    else:
        valor = os.read(r, 100)
        lines.append(valor.decode())


if __name__ == '__main__':
    lineas = leer()
    r, w = os.pipe()
    
    for linea in lineas:
        hijo(linea)
    
    for linea in lineas:
        os.wait()

    for linea in lines:
        print(linea)