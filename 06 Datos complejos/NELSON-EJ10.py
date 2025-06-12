# Ejercicio 10: Invertir diccionario de países y capitales
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Japón": "Tokio"
}

capitales = {}
for pais, capital in paises.items():
    capitales[capital] = pais

print("Diccionario original:", paises)
print("Diccionario invertido:", capitales)