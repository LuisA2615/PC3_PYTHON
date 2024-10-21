class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

# Crear un objeto de tipo RECTANGULO
rectangulo = RECTANGULO(5, 3)
print("Área del rectángulo:", rectangulo.area())

# Crear un objeto de tipo CUADRADO
cuadrado = CUADRADO(4)
print("Área del cuadrado:", cuadrado.area())
