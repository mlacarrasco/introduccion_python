def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

try:
    x = float(input("Ingrese el primer número: "))
    y = float(input("Ingrese el segundo número: "))

    print("Suma:", sumar(x, y))
    print("Producto:", multiplicar(x, y))
except ValueError:
    print("Debe ingresar números válidos.")

