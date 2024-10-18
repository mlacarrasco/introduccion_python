from sys import int_info
import numpy 
import random

def mosca(num,pos):   
  """ es una funcion de mosca"""
  arreglo=numpy.zeros(num)   

  while (pos>=0) and (pos<len(arreglo)): 
    arreglo[pos]=arreglo[pos]+1
    temp=random.random()

    if temp<0.33:
      pos=pos-1
    else:
      if temp>0.66:
       pos=pos+1

  print(arreglo)
  print("el numero de movimientos es ", arreglo.sum())
  return (arreglo.sum())

mosca(50,25)

# podemos imprimir informacion 
# adicional sobre la función
print(mosca.__doc__)
