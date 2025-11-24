print("Ingrese tres números para calcular el promedio.")

try:
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    c = float(input("Número 3: "))

    promedio = (a + b + c) / 3

    print("Promedio:", promedio)
    print("¿El promedio es mayor que el primer número?", promedio > a)
    print("¿El promedio es mayor que el segundo número?", promedio > b)
    print("¿El promedio es mayor que el tercer número?", promedio > c)
except ValueError:
    print("Debe ingresar números válidos.")

