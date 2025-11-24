# Presentación Ejercicio 5.2 – Lista ordenada

## Diapositiva 1 – Título y objetivo
- Título: Ordenar listas numéricas.
- Objetivo: Practicar creación de listas y método `.sort()`.

## Diapositiva 2 – Enunciado
- Pedir cuántos números se van a ingresar.
- Leer todos los números y guardarlos en una lista.
- Ordenar la lista de menor a mayor y mostrarla.

## Diapositiva 3 – Idea de la solución
- Leer `n` como entero.
- Usar un `for` para llenar la lista con `float` o `int`.
- Llamar a `lista.sort()` y luego imprimir la lista.

## Diapositiva 4 – Código clave
- `numeros = []`
- `for i in range(n):`
- `    num = float(input("Número: "))`
- `    numeros.append(num)`
- `numeros.sort()`
- `print(numeros)`

## Diapositiva 5 – Extensiones
- Ordenar de mayor a menor usando `reverse=True`.
- Mostrar también la posición original de cada número.

