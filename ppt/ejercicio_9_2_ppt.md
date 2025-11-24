# Presentación Ejercicio 9.2 – Manejo de división por cero

## Diapositiva 1 – Título y objetivo
- Título: Manejo de excepciones aritméticas.
- Objetivo: Practicar `try/except` con `ZeroDivisionError`.

## Diapositiva 2 – Enunciado
- Definir una función que intente dividir por cero.
- Capturar la excepción generada.
- Mostrar un mensaje amigable al usuario.

## Diapositiva 3 – Idea de la solución
- Escribir una función que haga `1 / 0`.
- Llamarla dentro de un bloque `try`.
- Capturar específicamente `ZeroDivisionError`.

## Diapositiva 4 – Código clave
- `def dividir_por_cero():`
- `    return 1 / 0`
- `try:`
- `    dividir_por_cero()`
- `except ZeroDivisionError:`
- `    print("No se puede dividir por cero.")`

## Diapositiva 5 – Extensiones
- Pedir al usuario dos números y manejar el error si el segundo es 0.
- Registrar el error en un archivo de log.

