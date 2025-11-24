estudiante = {
    "nombre": "Ana",
    "notas": {
        "Matemáticas": [5.0, 6.0, 5.5],
        "Programación": [6.0, 6.5, 6.0],
        "Física": [4.5, 5.0, 5.5]
    }
}

print("Estudiante:", estudiante["nombre"])

for asignatura, lista_notas in estudiante["notas"].items():
    if len(lista_notas) > 0:
        promedio = sum(lista_notas) / len(lista_notas)
    else:
        promedio = 0
    print("Promedio en", asignatura, "=", promedio)

