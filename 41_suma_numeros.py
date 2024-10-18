
numero = int(input("Ingresa un numero: "))
esPar(numero)


def esPar(var):
  if var%2==0:
    print(var,"es par")
    return
  else:
    print(var,"es impar")
    return