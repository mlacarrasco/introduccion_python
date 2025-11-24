cantidad_str = input("¿Cuántas notas desea ingresar?: ")

try:
    cantidad = int(cantidad_str)
    notas = []

    for i in range(cantidad):
        nota_str = input("Ingrese la nota " + str(i + 1) + ": ")
        try:
            nota = float(nota_str)
            notas.append(nota)
        except ValueError:
            print("Entrada inválida, se registra 0.")
            notas.append(0.0)

    if len(notas) > 0:
        promedio = sum(notas) / len(notas)
        print("El promedio de las notas es:", promedio)
    else:
        print("No se ingresaron notas.")
except ValueError:
    print("Debe ingresar un número entero para la cantidad.")

