# Programación Tradicional (Procedural)

def ingresar_temperaturas_diarias():
    temperaturas = []
    for _ in range(7):
        temperatura = float(input("Ingrese la temperatura diaria: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Uso de funciones
temperaturas_diarias = ingresar_temperaturas_diarias()
promedio_semanal = calcular_promedio_semanal(temperaturas_diarias)

print(f"Temperaturas diarias: {temperaturas_diarias}")
print(f"Promedio semanal: {promedio_semanal}")

#VENTAJAS DE PROGRAMACION TRADICIONAL
#1.Sencillez y Claridad: La programación tradicional tiende a ser más simple y directa. Para problemas pequeños o tareas simples.
#2.Menor Curva de Aprendizaje: Para programadores principiantes, el paradigma procedural a menudo presenta una curva de aprendizaje más suave. Comprender y adoptar conceptos de programación orientada a objetos (POO) puede llevar tiempo.
#3.Proyectos Pequeños o Scripts: Para scripts pequeños o proyectos muy simples, el enfoque procedural puede ser más directo y rápido de implementar.

#Como conclucion: Es importante tener en cuenta que la elección entre programación tradicional y orientada a objetos depende del contexto y los requisitos específicos del proyecto. Además, en muchos casos, se pueden aplicar principios de ambos paradigmas según sea necesario, y la elección puede depender del problema específico que se esté abordando y de las preferencias del equipo de desarrollo.