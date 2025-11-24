# Presentación Ejercicio 3.2 – Clasificación de notas

## Diapositiva 1 – Título y objetivo
- Título: Clasificar notas con rangos.
- Objetivo: Practicar condiciones encadenadas con `elif`.

## Diapositiva 2 – Enunciado
- Pedir una nota entre 1 y 7.
- Clasificarla como:
  - “insuficiente” si es menor a 4,
  - “suficiente” si está entre 4 y 5.5,
  - “sobresaliente” si es mayor o igual a 5.5.

## Diapositiva 3 – Idea de la solución
- Leer la nota como `float`.
- Validar que esté en el rango 1–7.
- Usar `if/elif/else` para asignar la categoría.

## Diapositiva 4 – Código clave
- `nota = float(input("Nota: "))`
- `if nota < 4:`
- `    print("Insuficiente")`
- `elif nota < 5.5:`
- `    print("Suficiente")`
- `else:`
- `    print("Sobresaliente")`

## Diapositiva 5 – Extensiones
- Pedir varias notas y mostrar la clasificación de cada una.
- Calcular el porcentaje de notas en cada categoría.

