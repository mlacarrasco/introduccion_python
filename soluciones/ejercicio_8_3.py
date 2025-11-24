def es_par(n):
    return n % 2 == 0

print("Números pares entre 1 y 20:")
for i in range(1, 21):
    if es_par(i):
        print(i)

