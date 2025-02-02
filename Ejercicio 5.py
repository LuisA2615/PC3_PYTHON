class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print(f"Notas: {self.notas}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.notas.append(nota)

# Ejemplo de uso
alumno1 = Alumno("Juan Pérez", "123456")
alumno1.setAge(20)
alumno1.setNota(8.5)
alumno1.setNota(9.0)

# Mostrar la información del estudiante
alumno1.display()