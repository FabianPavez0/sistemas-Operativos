class partido:
    def __init__ (e1, e2, ocasiones):
        self.e1 = e1
        self.e2 = e2
        self.ocasiones = ocasiones
        self.goles_e1 = 0
        self.goles_e2 = 0

    def jugar_partido():
        for i in range(self.ocasiones):
            aleatorio = random(0,1)
            
            if aleatorio == 0:
                self.e1 = ocasion_gol()
                self.goles_e1 += 1
            else:
                self.e2 = ocasion_gol()
                self.goles_e2 += 1

class equipo:
    #def __init__ (jugador, nombre_equipo):
#        self

    def ocasion_gol():
        aleatorio = random(0,1)
        if aleatorio == 0:
            return 1
        else:
            return 0


# Main

equipo1 = equipo(["Manolo", "Juan"], "Betis")

equipo2 = equipo(["Gustavo", "Antonio"], "Barça")

partido = partido(equipo1, equipo2, 10)

partido.jugar_partido()