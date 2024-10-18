print("ingrese el num. de elementos: ")
num = int(input())

lista = []
for i in range (num):
  print("ingrese numero",i+1)
  aux = input()
  while not aux.isdigit():
    print("ingresa un numero, no otra cosa")  
    aux = input()

  lista.append(aux)


print ("la lista es:")
for i in range (0,len(lista)):
  print(lista[i])