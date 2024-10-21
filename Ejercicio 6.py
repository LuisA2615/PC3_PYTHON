class Producto:
    def __init__(self, nombre, precio, año, categoria):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Año: {self.año} - Categoría: {self.categoria}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        return [producto for producto in self.productos if producto.año == año]

    def filtrar_por_categoria(self, categoria):
        return [producto for producto in self.productos if producto.categoria == categoria]

# Ejemplo de uso
catalogo = Catalogo()

# Creando productos
producto1 = Producto("Batería", 150, 2022, "Electrico")
producto2 = Producto("Frenos", 80, 2021, "Seguridad")
producto3 = Producto("Aceite Motor", 25, 2022, "Mantenimiento")

# Agregando productos al catálogo
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

# Mostrando todos los productos
print("Todos los productos en el catálogo:")
catalogo.mostrar_productos()

# Filtrando productos por año
año_filtrado = 2022
print(f"\nProductos del año {año_filtrado}:")
productos_por_año = catalogo.filtrar_por_año(año_filtrado)
for producto in productos_por_año:
    print(producto)

# Filtrando productos por categoría
categoria_filtrada = "Electrico"
print(f"\nProductos en la categoría '{categoria_filtrada}':")
productos_por_categoria = catalogo.filtrar_por_categoria(categoria_filtrada)
for producto in productos_por_categoria:
    print(producto)