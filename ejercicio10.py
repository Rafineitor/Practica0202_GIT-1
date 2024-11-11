#Productos de cesta de compra.

productos = input("Ingrese los productos de la cesta de compra: ")
productos_lista = productos.split(",")
for productos in productos_lista:
    print(productos)