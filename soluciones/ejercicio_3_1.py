numero_str = input("Ingrese un número entero: ")

try:
    numero = int(numero_str)
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
except ValueError:
    print("Debe ingresar un número entero.")

