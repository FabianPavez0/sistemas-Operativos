# 1) iniciar partida -> Introducir Nickname: macia, La partida ha empezado, elige un numero, has fallado, vuelve a intentarlo, partida finalizada
# 2) ver Ranking [Nombres y tiradas]-> macia 1º (lo ha resuelto en x tiradas) juano 2º javier 3º
# 3) Salir

import sys
import os
from random import randint
import time

class Menu:
    def __init__(self):
        self.opcion_elegida = None

    def mostrar_menu(self):
        print("1) Iniciar partida")
        print("2) Ver Ranking")
        print("3) Salir")

    def seleccionar(self):
        self.opcion_elegida = input("Seleccione su opcion: ")

class Partida:
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero
        self.nombre_jugador = None
        self.intentos = 0

    def iniciar_partida(self):
        os.system("clear")
        print(" ######    ####    #######  ##   ##  ##   ##  #######  ##   ##   ####    #####     #####")
        print("  ##  ##    ##      ##   #  ###  ##  ##   ##   ##   #  ###  ##    ##      ## ##   ##   ##")
        print("  ##  ##    ##      ## #    #### ##   ## ##    ## #    #### ##    ##      ##  ##  ##   ##")
        print("  #####     ##      ####    ## ####   ## ##    ####    ## ####    ##      ##  ##  ##   ##")
        print("  ##  ##    ##      ## #    ##  ###    ###     ## #    ##  ###    ##      ##  ##  ##   ##")
        print("  ##  ##    ##      ##   #  ##   ##    ###     ##   #  ##   ##    ##      ## ##   ##   ##")
        print(" ######    ####    #######  ##   ##     #     #######  ##   ##   ####    #####     #####")
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
        self.nombre_jugador = input(" ")
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

    def intento_incorrecto(self):
        self.intentos += 1

    def finalizar_partida(self, respuesta):
        os.system("clear")
        if respuesta == numero:
            print("Correcto")
            time.sleep(1)
            os.system("clear")
            print("Felicidades..")
        else:
            print("Incorrecto")
            self.intento_incorrecto()

    def registrar_intentos(self):
        if self.nombre_jugador is not None and self.intentos is not None:
            with open(self.nombre_fichero, "a") as f:
                f.write(f"{self.nombre_jugador}: {self.intentos} intentos\n")

    def leer_ranking(self):
        try:
            with open(self.nombre_fichero, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("Aún no hay registros en el ranking.")

if __name__ == "__main__":
    mi_menu = Menu()
    nueva_partida = Partida("ranking.txt")

    while True:
        mi_menu.mostrar_menu()
        mi_menu.seleccionar()

        if mi_menu.opcion_elegida == "1":
            os.system("clear")
            nueva_partida.iniciar_partida()
            numero = randint(0, 10)
            while True:
                respuesta = int(input("= "))
                nueva_partida.finalizar_partida(respuesta)
                if respuesta == numero:
                    nueva_partida.registrar_intentos()
                    break
        elif mi_menu.opcion_elegida == "2":
            os.system("clear")
            nueva_partida.leer_ranking()
            volver_al_menu = input("Presiona Enter para volver al menú.")
        elif mi_menu.opcion_elegida == "3":
            os.system("clear")
            print("Vuelve a intentarlo pronto...")
            sys.exit()
        else:
            print("Esa opción no está en mis posibilidades...tonto...")
            print("")