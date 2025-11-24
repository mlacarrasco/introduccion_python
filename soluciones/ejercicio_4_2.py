n_str = input("Ingrese un número entero mayor o igual a 2: ")

try:
    n = int(n_str)
    if n < 2:
        print("El número debe ser al menos 2.")
    else:
        print("Números pares desde 2 hasta", n)
        for i in range(2, n + 1, 2):
            print(i)
except ValueError:
    print("Debe ingresar un número entero.")

