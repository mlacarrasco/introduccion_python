
filas = int(input("Ingresa numero de filas: "))

cont =1 
for i in range(1,filas+1):
    for j in range(0,i):
        print(cont, end=" ")
        cont+=1
    print()