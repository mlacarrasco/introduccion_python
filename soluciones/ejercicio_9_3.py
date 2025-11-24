valor = input("Ingrese un número: ")

try:
    numero = int(valor)
    print("Ingresó el número entero:", numero)
except ValueError:
    print("Error: debe ingresar un número entero válido.")

