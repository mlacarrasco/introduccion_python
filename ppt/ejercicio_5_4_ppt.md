# Presentación Ejercicio 5.4 – Números mayores que el promedio

## Diapositiva 1 – Título y objetivo
- Título: Filtrado de listas según una condición.
- Objetivo: Practicar cálculo de promedio y selección de elementos.

## Diapositiva 2 – Enunciado
- Leer números enteros hasta que el usuario ingrese 0.
- Calcular el promedio de los números ingresados.
- Mostrar solamente los números mayores que el promedio.

## Diapositiva 3 – Idea de la solución
- Guardar los números en una lista.
- Usar `sum(lista) / len(lista)` para el promedio.
- Recorrer la lista y mostrar solo los valores que superen el promedio.

## Diapositiva 4 – Código clave
- `numeros = []`
- `while True:`
- `    n = int(input("Número: "))`
- `    if n == 0: break`
- `    numeros.append(n)`
- `prom = sum(numeros) / len(numeros)`

## Diapositiva 5 – Extensiones
- Construir una nueva lista con los números filtrados.
- Mostrar cuántos números son mayores y cuántos menores o iguales al promedio.

