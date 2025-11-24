anio_str = input("Ingrese un año (entero): ")

try:
    anio = int(anio_str)

    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                print("El año es bisiesto.")
            else:
                print("El año NO es bisiesto.")
        else:
            print("El año es bisiesto.")
    else:
        print("El año NO es bisiesto.")
except ValueError:
    print("Debe ingresar un número entero.")

