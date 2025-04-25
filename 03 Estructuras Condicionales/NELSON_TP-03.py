"""
Programa que pide edad del usuario y si es mayor de 18 años imprime mayor de edad
Autor: Nelson, Cristhian
Fecha: 15/04/2025
"""

edad = int(input("Ingrese su edad: "))

if edad > 18: 
    print("Es mayor de edad")
    
"""
Programa que solicite una nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar el mensaje de "Aprobado".
Caso contrario, deberá mostrar "Desaprobado"
Autor: Nelson, Cristhian
Fecha: 15/04/2025
"""

nota = int(input("Ingrese su nota: "))

if nota >= 6 :
    print("Aprobado")
else : 
    print("Desaprobado")
    
"""
Programa que permita ingresar sólo números pares. Si el número ingresado es par, mostrar mensaje "Ha ingresado un número par".
Caso contrario, mostrar mensaje "Por favor, ingrese un número par"
Autor: Nelson, Cristhian
Fecha:15/04/2024    
"""

número = int(input("Ingrese un número: "))

if número % 2 == 0 :
    print("Ha ingresado un número par")
else :
    print("Por favor, ingrese un número par")
    
"""
Programa que solicita edad al usuario y determina a qué categoría pertenece
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Es niño/a")
elif 12 <= edad < 18:
    print("Es adolescente")
elif 18 <= edad < 30:
    print("Es adulto/a joven")
elif edad >= 30:
    print("Es adulto/a mayor")
    
"""
Programa que tome la lista de numeros aleatorios, calcule su moda, su mediana y su media y las compare
para determinar si hay sesgo positivo, negativo o no hay sesgo. 
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo aparente (distribución simétrica)"


print("Lista generada (primeros 10 elementos):", numeros_aleatorios[:10], "...")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media:.2f}")  # Mostramos con 2 decimales
print("\nAnálisis de sesgo:", sesgo)

"""
Programa un programa que solicite una frase o palabra al usuario. Si el string termina con vocal, 
colocar signo de exclamación al final e imprimir.  Caso contrario, imprimir en pantalla el string como está
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

entrada = input("Ingrese una frase o palabra: ")

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if entrada and entrada[-1] in vocales:
    print(entrada + "!")
else:
    print(entrada)
    
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

"""
Programa que clasifica terremotos según la escala de Richter
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

magnitud = float(input("Ingrese la magnitud del terremoto en escala Richter: "))

if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"

print(f"\nPara una magnitud de {magnitud} en la escala Richter:")
print(f"Clasificación: {categoria}")   
   