
filas = int(input("Ingresa potencia n: "))

acum = 0
for i in range(1,filas+1):
    tmp=1
    for j in range(1,i+1):
        tmp*=j
        
    acum+=tmp
    
print(acum)