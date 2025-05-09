"""
Programa que clasifica terremotos según la escala de Richter
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

# Solicita magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasifica según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (graves daños a gran escala)")
