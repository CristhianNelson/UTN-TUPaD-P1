# Ejercicio 5: Verificar si una palabra es palíndromo de forma recursiva
def es_palindromo(palabra):
    # Caso base: si tiene 0 o 1 letras, es palíndromo
    if len(palabra) <= 1:
        return True
    # Comparamos primera y última letra, y llamamos recursivamente al resto
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

# Prueba de la función
palabra = input("Ingresá una palabra sin espacios ni tildes: ")
if es_palindromo(palabra):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
