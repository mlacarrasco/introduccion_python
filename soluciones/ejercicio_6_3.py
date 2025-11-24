estudiantes = {}

while True:
    print("\nMenú:")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Ver lista de estudiantes")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        rut = input("Ingrese RUT: ")
        nombre = input("Ingrese nombre: ")
        estudiantes[rut] = nombre
        print("Estudiante agregado.")
    elif opcion == "2":
        rut = input("Ingrese RUT a eliminar: ")
        if rut in estudiantes:
            del estudiantes[rut]
            print("Estudiante eliminado.")
        else:
            print("RUT no encontrado.")
    elif opcion == "3":
        print("Listado de estudiantes:")
        for rut, nombre in estudiantes.items():
            print(rut, "->", nombre)
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.")

