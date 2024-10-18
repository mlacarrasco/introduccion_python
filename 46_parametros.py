def holaMundo(nombre):
    return "Hola: " + nombre + " desde la función"

nombre_usuario = input("Ingresa tu nombre: ")
saludo = holaMundo(nombre_usuario)
print(saludo)
