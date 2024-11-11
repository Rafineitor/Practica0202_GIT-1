#FraseInvertida.

frase = input("Introduce una frase: ")
#frase=str() 
longitud = -len(frase)-1
#longitud = longitud de caracteres de frase
frase_inversa = frase[-1:longitud:-1]
print (frase_inversa)