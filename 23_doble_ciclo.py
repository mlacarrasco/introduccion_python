
filas = int(input("Ingresa numero de filas: "))

for i in range(1,filas+1):
    for j in range(0,i):
        print(j+1, end=" ")
    print()