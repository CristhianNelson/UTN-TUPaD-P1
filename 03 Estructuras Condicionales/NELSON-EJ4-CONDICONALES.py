"""
Programa que solicita edad al usuario y determina a qué categoría pertenece
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

# Solicita edad
edad = int(input("Ingrese su edad: "))

# Clasifica según la edad
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
