primero = input("Ingrese el primer número: ")
segundo = input("Ingrese el segundo número: ")

try:
    a = float(primero)
    b = float(segundo)

    try:
        resultado = a / b
        print("Resultado de la división:", resultado)
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero.")
except ValueError:
    print("Error: debe ingresar números válidos.")

