# Presentación Ejercicio 5.1 – Promedio de notas en una lista

## Diapositiva 1 – Título y objetivo
- Título: Listas y promedio de valores.
- Objetivo: Practicar listas, bucles y función `sum()`.

## Diapositiva 2 – Enunciado
- Pedir cuántas notas se ingresarán.
- Leer cada nota y guardarla en una lista.
- Calcular y mostrar el promedio de las notas.

## Diapositiva 3 – Idea de la solución
- Convertir la cantidad a `int`.
- En un `for`, leer cada nota y añadirla a la lista.
- Usar `sum(lista) / len(lista)` para el promedio.

## Diapositiva 4 – Código clave
- `notas = []`
- `for i in range(cantidad):`
- `    nota = float(input("Nota: "))`
- `    notas.append(nota)`
- `prom = sum(notas) / len(notas)`

## Diapositiva 5 – Extensiones
- Contar cuántas notas son mayores o iguales a 4.0.
- Mostrar la nota máxima y la mínima.

