print("Ingrese números enteros. Para terminar, ingrese 0.")

suma = 0

while True:
    valor_str = input("Número: ")
    try:
        valor = int(valor_str)
        if valor == 0:
            break
        suma = suma + valor
    except ValueError:
        print("Debe ingresar un número entero.")

print("La suma total es:", suma)

