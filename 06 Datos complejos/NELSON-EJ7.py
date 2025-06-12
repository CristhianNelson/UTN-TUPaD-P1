# Ejercicio 7: Sets con estudiantes que aprobaron parciales
parcial1 = set(input("Ingresá los nombres de los que aprobaron el Parcial 1 (separados por coma): ").split(","))
parcial2 = set(input("Ingresá los nombres de los que aprobaron el Parcial 2 (separados por coma): ").split(","))

print("Aprobaron ambos parciales:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)