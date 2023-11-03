import os
from threading import Thread


def fun1():
    pid = os.getpid()
    print("Hilo Hijo", pid)

if __name__ == "__main__":
    pid = os.getpid()
    print("Soy el proceso Padre", pid)
    #fun1()
    Thread = Thread(target=fun1)
    Thread.start()
    Thread.join()