#Precio producto.

producto = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio del producto: ")
cantidad = int(input("Ingrese la cantidad de unidades del producto: "))
precio = precio.replace(",",".")
precio = round(float(precio),2)
coste = precio * cantidad
precio_ent = "{:07.2f}".format(precio)
cantidad = "{:>03}".format(cantidad)
coste = "{:09.2f}".format(coste)
print ("El producto",producto,"cuesta",precio_ent,".",cantidad,"unidades costarían",coste)