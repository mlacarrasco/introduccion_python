capitales = {}

pais = input("Ingrese el nombre de un país: ")
capital = input("Ingrese la capital de ese país: ")

capitales[pais] = capital

print("Diccionario de capitales:", capitales)

consulta = input("Ingrese el nombre de un país para consultar su capital: ")

if consulta in capitales:
    print("La capital de", consulta, "es", capitales[consulta])
else:
    print("No se tiene registrada la capital de ese país.")

