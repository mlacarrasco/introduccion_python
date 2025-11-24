print('Ingrese nombres de estudiantes. Para terminar escriba "FIN".')

nombres = []

while True:
    nombre = input("Nombre: ")
    if nombre == "FIN":
        break
    nombres.append(nombre)

print("Se ingresaron", len(nombres), "nombres.")

