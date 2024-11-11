#Fecha de nacimiento.

fecha = input("Ingrese su fecha de nacimiento con el formato dd/mm/aaaa: ")
fecha_parte = fecha.split("/")
dia = fecha_parte[0]
mes = fecha_parte[1]
año = fecha_parte[2]

print ("El día de nacimiento es el",dia)
print ("El mes de nacimiento es el",mes)
print ("El año de nacimiento es",año)