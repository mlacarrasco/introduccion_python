print("Ingrese 10 números enteros.")

enteros = []

for i in range(10):
    valor_str = input("Número " + str(i + 1) + ": ")
    try:
        valor = int(valor_str)
    except ValueError:
        print("Entrada inválida, se registra 0.")
        valor = 0
    enteros.append(valor)

cuadrados = []
for num in enteros:
    cuadrados.append(num ** 2)

print("Lista original:", enteros)
print("Lista de cuadrados:", cuadrados)

