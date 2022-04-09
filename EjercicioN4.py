listUno=[]
i=0
while i <= 20:
    Uno=int(input("Digite Un Numero De La Lista: "))
    while Uno < 0:
        print("Por Favor Digite Numeros Postivos")
        break
    listUno.append(Uno)
    i+=1
    for j in listUno:
        if j < 0:     
            listUno.remove(Uno)
print(listUno)