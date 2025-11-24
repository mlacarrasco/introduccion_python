import math
import random
from datetime import datetime

def opcion_math():
    numero_str = input("Ingrese un número para calcular su raíz: ")
    try:
        numero = float(numero_str)
        print("Raíz cuadrada:", math.sqrt(numero))
    except ValueError:
        print("Número inválido.")

def opcion_random():
    print("Número aleatorio entre 1 y 100:", random.randint(1, 100))

def opcion_datetime():
    ahora = datetime.now()
    print("Fecha y hora actual:", ahora)

while True:
    print("\nMenú de bibliotecas:")
    print("1. Usar math (raíz cuadrada)")
    print("2. Usar random (número aleatorio)")
    print("3. Usar datetime (fecha y hora actual)")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        opcion_math()
    elif opcion == "2":
        opcion_random()
    elif opcion == "3":
        opcion_datetime()
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.")

