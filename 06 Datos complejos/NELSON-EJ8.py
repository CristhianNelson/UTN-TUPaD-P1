# Ejercicio 8: Diccionario con stock
stock = {}

producto = input("Producto a consultar: ")
if producto in stock:
    print("Stock disponible:", stock[producto])
    agregar = int(input("Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no encontrado. Ingresá stock inicial: "))
    stock[producto] = nuevo_stock

print("Estado actual del stock:", stock)
