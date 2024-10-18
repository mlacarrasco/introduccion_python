import random
import time

#como generar numeros aleatorios
numero1= random.randint(1,10)
numero2= random.randint(1,10)

#tiempo inicial
ini = time.time() 

real = numero1*numero2

print("el numero 1 es:", numero1)
print("el numero 2 es:", numero2)

guess= int(input("cual es el resultado?:"))

#tiempo final
fin = time.time()
dff = fin-ini

if dff<10:
  if(guess == real):
    print("felicitaciones, aprobaste el curso!")
  else:
    print("debes regresar al colegio :-(")

else:
  print("eres muy lento!!!!")
