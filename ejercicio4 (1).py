#Número de teléfono sin prefijo ni extensión.

tlf = input ("Introduce un número de teléfono con prefijo y extensión:  ")
grupos = tlf.split("-")
if grupos[0] == "+1":
    print (grupos [2])
else:
    print (grupos [1])