# Presentación Ejercicio 4.3 – Factorial con `for`

## Diapositiva 1 – Título y objetivo
- Título: Uso de acumulador multiplicativo.
- Objetivo: Implementar el factorial con un ciclo `for`.

## Diapositiva 2 – Enunciado
- Pedir un entero `n` ≥ 0.
- Calcular `n! = 1·2·3·...·n`.
- Mostrar el resultado en pantalla.

## Diapositiva 3 – Idea de la solución
- Inicializar `factorial = 1`.
- Recorrer desde 1 hasta `n` multiplicando en cada paso.
- Manejar el caso `n = 0` (factorial de 0 es 1).

## Diapositiva 4 – Código clave
- `n = int(input("n: "))`
- `factorial = 1`
- `for i in range(1, n + 1):`
- `    factorial = factorial * i`
- `print(factorial)`

## Diapositiva 5 – Extensiones
- Comparar con la versión usando `while`.
- Mostrar la “traza” del cálculo (producto parcial).

