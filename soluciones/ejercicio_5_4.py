print("Ingrese números enteros. Para terminar ingrese 0.")

numeros = []

while True:
    valor_str = input("Número: ")
    try:
        valor = int(valor_str)
        if valor == 0:
            break
        numeros.append(valor)
    except ValueError:
        print("Debe ingresar un número entero.")

if len(numeros) == 0:
    print("No se ingresaron números.")
else:
    promedio = sum(numeros) / len(numeros)
    print("Promedio:", promedio)
    print("Números mayores que el promedio:")
    for num in numeros:
        if num > promedio:
            print(num)

