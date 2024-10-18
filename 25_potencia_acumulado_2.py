N = int(input("Ingresa el valor de N: "))
i = 1
acum = 0

while i<=N:
  j = 1        #inicializacion ciclo interno
  while j<=i:  #desde aca ciclo internno
    acum+= i**j
    j+= 1
  i+= 1 #esto es del ciclo externo

print(acum)
