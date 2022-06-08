import os, sys, time, codecs,  multiprocessing as mp


def hijo1(pipe_s, q, stdin):
    sys.stdin = os.fdopen(stdin)
    for input in sys.stdin:
        if input[:3] == "adios":
            pipe_s.send("adios")
            pipe_s.close()
            break
  
        else:
            pipe_s.send(input)
            print("Primer hijo leyendo la cola:")
            time.sleep(0.3)
            print(q.get())

def hijo2(pipe_r, q):
    condicion = True
    while condicion == True:
        time.sleep(1)
        print("Segundo hijo leyendo el pipe:")
        mensaje = str(pipe_r.recv())
        if mensaje == "bye":
            condicion = False
            print("Hijos saliendo...")
        else:
            q.put(codecs.encode(mensaje,'rot_13'))
    
    pipe_r.close()

if __name__ == "__main__":
    fd = sys.stdin.fileno
    pipe_s, pipe_r = mp.Pipe()
    q = mp.Queue()
    proceso1 = mp.Process(target = hijo1, args = (pipe_s, q, fd))
    proceso2 = mp.Process(target = hijo2, args = (pipe_r, q))
    proceso1.start()
    proceso2.start()
    proceso1.join()
    proceso2.join()