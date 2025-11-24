# Presentación Ejercicio 2.5 – Condición de aprobación

## Diapositiva 1 – Título y objetivo
- Título: Lógica compuesta para aprobar.
- Objetivo: Usar `and` con varias condiciones numéricas.

## Diapositiva 2 – Enunciado
- Pedir dos notas (entre 1.0 y 7.0).
- Calcular el promedio.
- El estudiante aprueba si el promedio ≥ 4.0 y ninguna nota es menor a 3.0.

## Diapositiva 3 – Idea de la solución
- Leer `nota1` y `nota2` como `float`.
- Calcular el promedio aritmético.
- Evaluar `promedio >= 4.0 and nota1 >= 3.0 and nota2 >= 3.0`.

## Diapositiva 4 – Código clave
- `nota1 = float(input("Nota 1: "))`
- `nota2 = float(input("Nota 2: "))`
- `prom = (nota1 + nota2) / 2`
- `aprueba = prom >= 4.0 and nota1 >= 3.0 and nota2 >= 3.0`
- `print("¿Aprueba?", aprueba)`

## Diapositiva 5 – Extensiones
- Clasificar el resultado en “reprobado”, “aprobado”, “destacado”.
- Permitir ingresar más de dos notas usando listas.

