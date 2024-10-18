
filas = int(input("Ingresa potencia n: "))

cont = 1 
acum = 0
for i in range(1,filas+1):
    for j in range(1,i+1):
        acum+= i**j
    
print(acum)