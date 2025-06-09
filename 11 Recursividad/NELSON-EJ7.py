# Ejercicio 7: Contar la cantidad total de bloques para una pirámide
def contar_bloques(n):
    # Caso base: si hay un solo bloque, devolvemos 1
    if n == 1:
        return 1
    else:
        # Paso recursivo: sumamos los bloques de este nivel con los del siguiente
        return n + contar_bloques(n - 1)

# Prueba de la función
niveles = int(input("Cantidad de bloques en la base de la pirámide: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")
