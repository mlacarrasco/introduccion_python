n_str = input("¿Cuántos números desea ingresar?: ")

try:
    n = int(n_str)
    numeros = []

    for i in range(n):
        num_str = input("Número " + str(i + 1) + ": ")
        try:
            num = float(num_str)
            numeros.append(num)
        except ValueError:
            print("Entrada inválida, se registra 0.")
            numeros.append(0.0)

    numeros.sort()
    print("Lista ordenada de menor a mayor:")
    print(numeros)
except ValueError:
    print("Debe ingresar un número entero para la cantidad.")

