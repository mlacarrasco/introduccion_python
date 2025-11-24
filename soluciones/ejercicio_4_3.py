n_str = input("Ingrese un número entero para calcular su factorial: ")

try:
    n = int(n_str)
    if n < 0:
        print("El factorial no está definido para números negativos.")
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial * i
        print("El factorial de", n, "es", factorial)
except ValueError:
    print("Debe ingresar un número entero.")

