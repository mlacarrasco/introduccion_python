# Presentación Ejercicio 8.3 – Función `es_par`

## Diapositiva 1 – Título y objetivo
- Título: Funciones booleanas simples.
- Objetivo: Practicar funciones que devuelven `True` o `False`.

## Diapositiva 2 – Enunciado
- Definir una función `es_par(n)` que indique si un número es par.
- Usar la función para imprimir todos los pares entre 1 y 20.

## Diapositiva 3 – Idea de la solución
- Dentro de la función, devolver `n % 2 == 0`.
- En un `for` de 1 a 20, llamar a `es_par(i)` y si es `True`, imprimir `i`.

## Diapositiva 4 – Código clave
- `def es_par(n):`
- `    return n % 2 == 0`
- `for i in range(1, 21):`
- `    if es_par(i): print(i)`

## Diapositiva 5 – Extensiones
- Usar la función para filtrar pares en una lista.
- Escribir la función contraria `es_impar`.

