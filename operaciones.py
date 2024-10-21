import operaciones

# Ejemplos de uso de las funciones
a = 10
b = 2
c = 0
d = "texto"

print("Suma:", operaciones.suma(a, b))           # 10 + 2 = 12
print("Resta:", operaciones.resta(a, b))         # 10 - 2 = 8
print("Producto:", operaciones.producto(a, b))   # 10 * 2 = 20
print("División:", operaciones.division(a, b))    # 10 / 2 = 5.0

# Pruebas de errores
print("División por cero:", operaciones.division(a, c))  # Error
print("Suma con texto:", operaciones.suma(a, d))        # Error
