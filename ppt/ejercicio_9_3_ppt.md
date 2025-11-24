# Presentación Ejercicio 9.3 – Validar entrada entera

## Diapositiva 1 – Título y objetivo
- Título: Manejar errores de conversión.
- Objetivo: Practicar `try/except` con `ValueError`.

## Diapositiva 2 – Enunciado
- Pedir un número al usuario.
- Intentar convertirlo a entero.
- Si la conversión falla, mostrar un mensaje de error.

## Diapositiva 3 – Idea de la solución
- Leer la entrada como cadena.
- Dentro de `try`, convertir con `int()`.
- En `except ValueError`, imprimir un mensaje indicando el problema.

## Diapositiva 4 – Código clave
- `valor = input("Número: ")`
- `try:`
- `    numero = int(valor)`
- `    print(numero)`
- `except ValueError:`
- `    print("Entrada inválida")`

## Diapositiva 5 – Extensiones
- Volver a pedir el número hasta que sea válido.
- Permitir también números decimales con `float`.

