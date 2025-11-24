nombre = input("Ingrese su nombre: ")
veces_str = input("¿Cuántas veces desea repetir el nombre?: ")

try:
    veces = int(veces_str)
    for i in range(veces):
        print(nombre)
except ValueError:
    print("Debe ingresar un número entero para la cantidad de repeticiones.")

