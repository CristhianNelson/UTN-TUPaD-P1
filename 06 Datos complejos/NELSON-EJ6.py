# Ejercicio 6: Notas de alumnos
alumnos = {}
for i in range(3):
    nombre = input("Nombre del alumno: ")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: promedio {promedio}")
