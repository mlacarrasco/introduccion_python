def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista_numeros):
    primos = []
    for numero in lista_numeros:
        if es_primo(numero):
            primos.append(numero)
    return primos

entrada = input("Ingrese números enteros separados por espacio: ")
partes = entrada.split()

numeros = []
for p in partes:
    try:
        numeros.append(int(p))
    except ValueError:
        print("Valor inválido ignorado:", p)

resultado = filtrar_primos(numeros)
print("Números primos en la lista:", resultado)

