edad_str = input("Ingrese la edad: ")
pais = input("Ingrese el país (por ejemplo, Chile u Otro): ")

try:
    edad = int(edad_str)

    if pais.lower() == "chile":
        puede_votar = edad >= 18
    else:
        puede_votar = edad >= 21

    if puede_votar:
        print("La persona puede votar.")
    else:
        print("La persona NO puede votar.")
except ValueError:
    print("Debe ingresar un número entero para la edad.")

