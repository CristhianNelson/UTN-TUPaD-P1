# Ejercicio 3: Calcular una potencia usando recursividad
def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    else:
        # Paso recursivo: base * potencia(base, exponente - 1)
        return base * potencia(base, exponente - 1)

# Probamos la función
b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")
