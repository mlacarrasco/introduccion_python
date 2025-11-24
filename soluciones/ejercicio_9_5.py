palabra_secreta = "python"
intentos = 3

print("Juego de adivinar la palabra secreta.")

while intentos > 0:
    print("Te quedan", intentos, "intentos.")
    intento = input("Ingresa tu intento: ")
    if intento == palabra_secreta:
        print("¡Correcto! Adivinaste la palabra.")
        break
    else:
        print("Incorrecto.")
        intentos = intentos - 1

if intentos == 0:
    print("Has perdido. La palabra secreta era:", palabra_secreta)

