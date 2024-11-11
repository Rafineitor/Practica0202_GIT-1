#Frase con vocal introducida en mayúscula.

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")
vocal_mayuscula = vocal.upper()
frase_mayuscula = frase.replace (vocal, vocal_mayuscula)
print (frase_mayuscula)