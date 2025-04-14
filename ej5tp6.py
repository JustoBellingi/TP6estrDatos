import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return math.pi * self.radio**2

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio


# Ejemplo de uso:
circulo = Circulo(15)
print("Área:", circulo.calcularArea())
print("Perímetro:", circulo.calcularPerimetro())
