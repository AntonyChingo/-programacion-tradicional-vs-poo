# Programación Orientada a Objetos (POO)

class RegistroClima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas_diarias(self):
        for _ in range(7):
            temperatura = float(input("Ingrese la temperatura diaria: "))
            self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio

# Uso de la clase
registro = RegistroClima()
registro.ingresar_temperaturas_diarias()
promedio_semanal = registro.calcular_promedio_semanal()

print(f"Temperaturas diarias: {registro.temperaturas}")
print(f"Promedio semanal: {promedio_semanal}")

#VENTAJAS DE POO
#1.Encapsulamiento: La información sobre las temperaturas se encapsula en un objeto RegistroClima, proporcionando una estructura más organizada y reduciendo la complejidad.
#2.Reutilización de código: Las funciones relacionadas con el clima se agrupan en métodos de la clase RegistroClima, lo que facilita la reutilización del código en diferentes partes del programa.
#3.Abstracción: El código orientado a objetos utiliza métodos (ingresar_temperaturas_diarias, calcular_promedio_semanal) que abstractan la lógica subyacente, lo que facilita la comprensión del código.
#4.Modularidad: La clase RegistroClima proporciona una unidad modular que puede ser fácilmente extendida y modificada sin afectar otras partes del código.

#Como conclucion:La POO proporciona una estructura más clara y organizada, especialmente en programas más grandes, y facilita la reutilización y mantenimiento del código.