nota_str = input("Ingrese una nota entre 1 y 7: ")

try:
    nota = float(nota_str)
    if nota < 1 or nota > 7:
        print("La nota debe estar entre 1 y 7.")
    elif nota < 4:
        print("Insuficiente")
    elif nota < 5.5:
        print("Suficiente")
    else:
        print("Sobresaliente")
except ValueError:
    print("Debe ingresar un valor numérico.")

