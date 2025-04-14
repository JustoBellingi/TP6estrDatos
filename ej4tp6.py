class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def saludar(self):
        print(
            f" Hola, como estas? Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años."
        )
persona.saludar()
