import random

print("Lanzando un dado 10 veces:")

for i in range(10):
    lanzamiento = random.randint(1, 6)
    print("Lanzamiento", i + 1, ":", lanzamiento)

