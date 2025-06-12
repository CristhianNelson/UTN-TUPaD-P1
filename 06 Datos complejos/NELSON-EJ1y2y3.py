# Ejercicio 1: Crear diccionario con precios de frutas
precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print("Ejercicio 1:", precios_frutas)

# Ejercicio 2: Actualizar precios
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print("Ejercicio 2:", precios_frutas)

# Ejercicio 3: Lista con los nombres de las frutas
frutas = list(precios_frutas.keys())
print("Ejercicio 3:", frutas)
