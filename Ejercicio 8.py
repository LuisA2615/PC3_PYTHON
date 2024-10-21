import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

def validar_numero(numero):
    try:
        num = float(numero)
        if num <= 0:
            print("Error: Debe ser un número positivo.")
            return None
        return num
    except ValueError:
        print("Error: Tipo de dato no válido.")
        return None

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            radio = validar_numero(input("Ingrese el radio del círculo: "))
            if radio is not None:
                circulo = Circulo(radio)
                print(f"Área del círculo: {circulo.area():.2f}")

        elif opcion == '2':
            largo = validar_numero(input("Ingrese el largo del rectángulo: "))
            ancho = validar_numero(input("Ingrese el ancho del rectángulo: "))
            if largo is not None and ancho is not None:
                rectangulo = Rectangulo(largo, ancho)
                print(f"Área del rectángulo: {rectangulo.area():.2f}")

        elif opcion == '3':
            lado = validar_numero(input("Ingrese el lado del cuadrado: "))
            if lado is not None:
                cuadrado = Cuadrado(lado)
                print(f"Área del cuadrado: {cuadrado.area():.2f}")

        elif opcion == '4':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()
