#Correo electronico + dominio.

correo = input("Ingrese su correo electronico: ")
correo_parte = correo.split("@")
correo_final = correo_parte[0]+"@ceu.es"
print ("El nuevo correo electronico es:",correo_final)