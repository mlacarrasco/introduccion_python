n_str = input("Ingrese un número entero para ver su tabla de multiplicar: ")

try:
    n = int(n_str)
    print("Tabla de multiplicar del", n)
    for i in range(1, 11):
        resultado = n * i
        print(n, "x", i, "=", resultado)
except ValueError:
    print("Debe ingresar un número entero.")

