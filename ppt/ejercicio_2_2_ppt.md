# Presentación Ejercicio 2.2 – Operaciones entre dos enteros

## Diapositiva 1 – Título y objetivo
- Título: Suma, resta, producto y división.
- Objetivo: Practicar operadores básicos y manejo de división por cero.

## Diapositiva 2 – Enunciado
- Pedir dos números enteros al usuario.
- Calcular y mostrar suma, diferencia, producto y cociente.
- En caso de segundo número igual a 0, informar que no se puede dividir.

## Diapositiva 3 – Idea de la solución
- Convertir las entradas a `int`.
- Usar operadores `+`, `-`, `*`, `/`.
- Antes de dividir, comprobar que el divisor no sea cero.

## Diapositiva 4 – Código clave
- `a = int(input("Primero: "))`
- `b = int(input("Segundo: "))`
- `print("Suma:", a + b)`
- `if b != 0: print("Cociente:", a / b)`

## Diapositiva 5 – Extensiones
- Mostrar también la división entera `//` y el resto `%`.
- Manejar errores de conversión con `try/except`.

