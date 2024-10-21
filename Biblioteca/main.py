from gestion import GestionBiblioteca
from libro import Libro

def menu():
    gestion = GestionBiblioteca()
    while True:
        print("\nMenú de Gestión de Biblioteca")
        print("1. Agregar un libro")
        print("2. Listar libros")
        print("3. Buscar libro por título")
        print("4. Buscar libro por autor")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(libro)
            print("Libro agregado exitosamente.")

        elif opcion == '2':
            print("\nLista de libros en la biblioteca:")
            gestion.listar_libros()

        elif opcion == '3':
            titulo = input("Ingrese el título a buscar: ")
            resultados = gestion.buscar_por_titulo(titulo)
            if resultados:
                print("\nLibros encontrados:")
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros con ese título.")

        elif opcion == '4':
            autor = input("Ingrese el autor a buscar: ")
            resultados = gestion.buscar_por_autor(autor)
            if resultados:
                print("\nLibros encontrados:")
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros de ese autor.")

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
