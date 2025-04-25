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