# Presentación Ejercicio 9.5 – Juego de adivinar palabra

## Diapositiva 1 – Título y objetivo
- Título: Juego con intentos limitados.
- Objetivo: Practicar ciclos con contador de intentos.

## Diapositiva 2 – Enunciado
- Definir una palabra secreta.
- Dar al usuario 3 intentos para adivinarla.
- Si adivina, mostrar mensaje de éxito; si no, mostrar la palabra correcta.

## Diapositiva 3 – Idea de la solución
- Guardar la palabra secreta en una variable.
- Usar un `while` con un contador de intentos.
- Comparar el intento con la palabra secreta en cada vuelta.

## Diapositiva 4 – Código clave
- `palabra_secreta = "python"`
- `intentos = 3`
- `while intentos > 0:`
- `    intento = input("Palabra: ")`
- `    # comparar y decrementar intentos`

## Diapositiva 5 – Extensiones
- Usar una lista de palabras posibles al azar.
- Dar pistas (por ejemplo, longitud de la palabra).

