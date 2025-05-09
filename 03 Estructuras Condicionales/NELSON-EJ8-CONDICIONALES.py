"""
Programa que transforma un nombre según la opción seleccionada
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

# Solicita nombre y opción
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 para MAYÚSCULAS, 2 para minúsculas, 3 para Capitalizada: ")

# Aplica transformación según opción
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida")
