# 1) iniciar partida -> Introducir Nickname: macia, La partida ha empezado, elige un numero, has fallado, vuelve a intentarlo, partida finalizada
# 2) ver Ranking [Nombres y tiradas]-> macia 1º (lo ha resuelto en x tiradas) juano 2º javier 3º
# 3) Salir

class menu():
    def __init__(self):
        self.opcion_elegida = None

    def mostrar_menu(self):
        print ("1) Iniciar partida")
        print ("2) Ver Ranking")
        print ("3) Salir")

    def seleccionar(self):
        self.opcion_elegida = input("Seleccione su opcion: ")
    
class Partida2:
    def __init__(self):
        pass

    def iniciar_partida(self):
        print("")

class Partida:

    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def leer_ranking(self):
        f = open(self.nombre_fichero, "r")
        print(f.read())
        f.close()

    def write_ranking(self):
        f = open(self.nombre_fichero, "a")
        f.write()
        f.write("\n")
        f.close()

    mi_menu = menu()

    import sys
    import os
    while True:
        mi_menu.mostrar_menu()
        mi_menu.seleccionar()

        if mi_menu.opcion_elegida == "1":
            os.system("clear")
            nueva_partida = Partida2()
            nueva_partida.iniciar_partida()
            break
        elif mi_menu.opcion_elegida == "2":
            os.system("clear")
            
            break
        elif mi_menu.opcion_elegida == "3":
            os.system("clear")
            print("Vuelve a intentarlo pronto...")
            sys.exit()
        else:
            print("Esa opción no está en mis posibilidades...tonto...")
            print("")
    intentos = 0

    print(" ######    ####    #######  ##   ##  ##   ##  #######  ##   ##   ####    #####     #####")
    print("  ##  ##    ##      ##   #  ###  ##  ##   ##   ##   #  ###  ##    ##      ## ##   ##   ##")
    print("  ##  ##    ##      ## #    #### ##   ## ##    ## #    #### ##    ##      ##  ##  ##   ##")
    print("  #####     ##      ####    ## ####   ## ##    ####    ## ####    ##      ##  ##  ##   ##")
    print("  ##  ##    ##      ## #    ##  ###    ###     ## #    ##  ###    ##      ##  ##  ##   ##")
    print("  ##  ##    ##      ##   #  ##   ##    ###     ##   #  ##   ##    ##      ## ##   ##   ##")
    print(" ######    ####    #######  ##   ##     #     #######  ##   ##   ####    #####     #####")
    import time
    time.sleep(2)
    os.system("clear")
    print(" #####     ####    ##   ##  #######           ######   ##   ##           ##   ##   #####   ##   ##  ######   ######   #######")
    print("  ## ##     ##     ### ###   ##   #           # ## #   ##   ##           ###  ##  ##   ##  ### ###   ##  ##   ##  ##   ##   #")
    print("  ##  ##    ##     #######   ## #               ##     ##   ##           #### ##  ##   ##  #######   ##  ##   ##  ##   ## #")
    print("  ##  ##    ##     #######   ####               ##     ##   ##           ## ####  ##   ##  #######   #####    #####    ####")
    print("  ##  ##    ##     ## # ##   ## #               ##     ##   ##           ##  ###  ##   ##  ## # ##   ##  ##   ## ##    ## #")
    print("  ## ##     ##     ##   ##   ##   #             ##     ##   ##           ##   ##  ##   ##  ##   ##   ##  ##   ##  ##   ##   #")
    print(" #####     ####    ##   ##  #######            ####     #####            ##   ##   #####   ##   ##  ######   #### ##  #######")
    print("")
    print("")
    nombre = input()
    time.sleep(1)
    os.system("clear")
    print(" ####      ####     #####   ######    #####             ####")
    print("  ##        ##     ##   ##  # ## #   ##   ##           ##  ##")
    print("  ##        ##     #          ##     ##   ##               ##")
    print("  ##        ##      #####     ##     ##   ##              ##")
    print("  ##   #    ##          ##    ##     ##   ##             ##")
    print("  ##  ##    ##     ##   ##    ##     ##   ##        ")
    print(" #######   ####     #####    ####     #####              ##")
    time.sleep(1)
    os.system("clear")
    print("Intenta adivinar el número que estoy pensando")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Si eres capaz...")

if __name__ == "__main__":
    menu()

from random import randint
import time
import os
numero = randint(0, 10)

while True:
    respuesta = int(input("= "))
    if respuesta == numero:
        print("Correcto")
        time.sleep(1)
        os.system("clear")
        print("Felicidades..")
        break
    else:
        print("Incorrecto")