#Consulta de precio.

precio_producto = (input("Introduce el precio del producto:"))
precio_parte = precio_producto.split(",")
euros = precio_parte [0]
centimos = precio_parte [1]
long=len(centimos)
centimos=float(centimos)
centimos=centimos/10**long

print ("Euros:", euros)
print ("Centimos:", round (centimos,2))