
lista=[]
for i in range(5):
    numero = input("Ingresa un numero: ")
    while not numero.isdigit():
        print("error:ingresa un numero")
        numero = input("Ingresa un numero: ")
    
    lista.append(int(numero))

acum = 0.0
for elemento in lista:
    acum= acum + elemento

promedio = acum/len(lista)

print("el promedio es: ", promedio)