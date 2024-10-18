print("ingrese la base")
a = int(input())

print("ingrese el exponente")
n = int(input())

base = 1
i    = 0

while i<n:
    base = a*base
    print("valor:",base)
    i = i+1

print("valor final", base)
