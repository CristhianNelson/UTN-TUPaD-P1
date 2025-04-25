"""
Programa que transforma un nombre según la opción seleccionada
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

nombre = input("Ingrese su nombre: ")
opcion = input("Seleccione una opción (1, 2 o 3):\n"
               "1. Nombre en MAYÚSCULAS\n"
               "2. nombre en minúsculas\n"
               "3. Nombre con primera letra mayúscula\n"
               "Opción: ")

if opcion == "1":
    resultado = nombre.upper()
elif opcion == "2":
    resultado = nombre.lower()
elif opcion == "3":
    resultado = nombre.title()  
else:
    resultado = "Opción no válida. Por favor ingrese 1, 2 o 3."

print("\nResultado:", resultado)