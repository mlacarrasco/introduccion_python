primero_str = input("Ingrese el primer entero: ")
segundo_str = input("Ingrese el segundo entero: ")

try:
    primero = int(primero_str)
    segundo = int(segundo_str)

    print("Suma:", primero + segundo)
    print("Diferencia (primero - segundo):", primero - segundo)
    print("Producto:", primero * segundo)

    if segundo != 0:
        print("Cociente (primero / segundo):", primero / segundo)
    else:
        print("No se puede dividir por cero.")
except ValueError:
    print("Debe ingresar valores enteros.")

