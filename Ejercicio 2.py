def obtener_calificaciones():  
    calificaciones = input("Introduce una lista de calificaciones separadas por comas: ")  
    lista_calificaciones = calificaciones.split(",")  

    try:  
        lista_enteros = [int(calif.strip()) for calif in lista_calificaciones]  
        print("Las calificaciones son:", lista_enteros)  
    except ValueError:  
        print("Error: Asegúrate de introducir solo números enteros separados por comas.")  

obtener_calificaciones()