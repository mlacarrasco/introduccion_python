print("ingrese la base")
a = int(input())

print("ingrese el exponente")
n = int(input())
base= 1

for i in range(0,n):
    base = a*base
    print("valor:",base)

print("valor final", base)
