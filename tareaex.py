class Coche:
    def __init__(self, nombre_coche, caballos):
        self.nombre_coche = nombre_coche
        self.caballos = caballos


class Carrera:  
    def empieza_carrera():
        print("Ha empezado la carrera")

    def muestra_resultado():
        print("Los resultados han sido:")

if __name__ == '__main__':

    c1 = Coche("Mercedes", "120hp")
    c2 = Coche("ferrari", "200hp")
    c3 = Coche("adsfadsf", "asdf")

    coches= [c1, c2, c3]
    c = Carrera(coches)
    c.empieza_carrera()
    c.muestra_resultado()