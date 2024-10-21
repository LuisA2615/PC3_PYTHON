def suma(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: Tipo de dato no válido.")

def resta(a, b):
    try:
        return a - b
    except TypeError:
        print("Error: Tipo de dato no válido.")

def producto(a, b):
    try:
        return a * b
    except TypeError:
        print("Error: Tipo de dato no válido.")

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        return a / b
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
    except TypeError:
        print("Error: Tipo de dato no válido.")
