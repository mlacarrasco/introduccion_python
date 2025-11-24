edad_str = input("Ingrese su edad: ")

try:
    edad = int(edad_str)
    es_mayor_de_edad = edad >= 18
    print(es_mayor_de_edad)
except ValueError:
    print("Debe ingresar un número entero para la edad.")

