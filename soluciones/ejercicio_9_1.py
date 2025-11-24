import random

numero_secreto = random.randint(1, 10)

print("Adivina el número entre 1 y 10.")

intento_str = input("Ingresa tu intento: ")

try:
    intento = int(intento_str)
    if intento == numero_secreto:
        print("¡Adivinaste!")
    elif intento < numero_secreto:
        print("Te quedaste corto.")
    else:
        print("Te pasaste.")
    print("El número secreto era:", numero_secreto)
except ValueError:
    print("Debes ingresar un número entero.")

