
lista=[]
for i in range(5):
    numero = input("Ingresa un numero: ")
    while not numero.isdigit():
        print("error:ingresa un numero")
        numero = input("Ingresa un numero: ")
    lista.append(int(numero))

#forma 1
print(sorted(lista))

#forma 2
lista.sort()
print(list(lista))