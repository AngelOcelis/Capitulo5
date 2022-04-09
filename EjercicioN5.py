Pal= str(input("Digite Una Texto: "))          
Pal= Pal.upper()
listPal= Pal.split(" ")
listUno=list(set(listPal))

print(listUno)