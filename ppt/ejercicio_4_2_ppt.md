# Presentación Ejercicio 4.2 – Pares hasta n

## Diapositiva 1 – Título y objetivo
- Título: Recorrer rangos con paso fijo.
- Objetivo: Practicar `range(inicio, fin, paso)` y ciclos `for`.

## Diapositiva 2 – Enunciado
- Pedir un entero `n` mayor o igual a 2.
- Imprimir todos los números pares desde 2 hasta `n`.

## Diapositiva 3 – Idea de la solución
- Convertir `n` a entero y verificar que sea ≥ 2.
- Usar `range(2, n+1, 2)` para generar pares.
- Imprimir cada valor en el ciclo `for`.

## Diapositiva 4 – Código clave
- `n = int(input("n: "))`
- `for i in range(2, n + 1, 2):`
- `    print(i)`

## Diapositiva 5 – Extensiones
- Generar ahora los impares con paso 2.
- Contar cuántos números pares se imprimieron.

