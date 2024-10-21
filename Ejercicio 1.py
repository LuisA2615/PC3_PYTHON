def solicitar_fraccion():  
    while True:  
        try:  
            entrada = input("Ingrese una fracción en formato X/Y: ")  
            x, y = map(int, entrada.split('/'))  

            if y == 0:  
                print("Error: Y no puede ser cero. Intente de nuevo.")  
                continue  
            if x < 0 or y < 0 or x > y:  
                print("Error: X debe ser menor o igual a Y y ambos deben ser números enteros no negativos. Intente de nuevo.")  
                continue  

            porcentaje = (x / y) * 100  
            
            if porcentaje < 1:  
                print("E")  
            elif porcentaje > 99:  
                print("F")  
            else:  
                print(f"{round(porcentaje)}%")  
            break  
            
        except ValueError:  
            print("Error: Entrada inválida. Asegúrese de ingresar dos números enteros en formato X/Y.")  
        except ZeroDivisionError:  
            print("Error: La división por cero no es permitida.")  

solicitar_fraccion()