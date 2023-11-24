class Coche:
    def __init__(self, motor, ruedas, puertas, modelo, color, velocidad):
        self.motor = motor
        self.ruedas = ruedas
        self.puertas = puertas
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad

    def velocidad_normal(self):
        "80"

    def velocidad_punta(self):
        "230km/h"

    while velocidad_normal < velocidad_punta:
        velocidad_normal = +5

    def arrancar(self):
        print ("Arrancando el coche")


c1 = Coche("V6", "michelin", 4, "BMW", "azul", 80)
c1.arrancar()


print(c1.motor)
print(c1.ruedas)
print(c1.puertas)
print(c1.modelo)
print(c1.color)
print(c1.velocidad)
