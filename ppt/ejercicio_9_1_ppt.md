# Presentación Ejercicio 9.1 – Juego de adivinar número

## Diapositiva 1 – Título y objetivo
- Título: Juego simple con números aleatorios.
- Objetivo: Practicar `random`, entradas por teclado y condicionales.

## Diapositiva 2 – Enunciado
- Generar un número secreto entre 1 y 10.
- Pedir un intento al usuario.
- Indicar si adivinó, se quedó corto o se pasó.

## Diapositiva 3 – Idea de la solución
- Usar `random.randint(1, 10)` para el número secreto.
- Convertir el intento a `int`.
- Comparar intento y número secreto con `if/elif/else`.

## Diapositiva 4 – Código clave
- `numero_secreto = random.randint(1, 10)`
- `intento = int(input("Intento: "))`
- `if intento == numero_secreto: print("¡Adivinaste!")`
- `elif intento < numero_secreto: print("Te quedaste corto.")`

## Diapositiva 5 – Extensiones
- Permitir varios intentos dentro de un ciclo.
- Contar la cantidad de intentos usados.

