import math

numero_str = input("Ingrese un número: ")

try:
    numero = float(numero_str)
    raiz = math.sqrt(numero)
    seno = math.sin(numero)
    print("Raíz cuadrada:", raiz)
    print("Seno:", seno)
except ValueError:
    print("Debe ingresar un número válido.")

