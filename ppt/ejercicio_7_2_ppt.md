# Presentación Ejercicio 7.2 – Lanzamiento de dado

## Diapositiva 1 – Título y objetivo
- Título: Aleatoriedad con la biblioteca `random`.
- Objetivo: Practicar generación de números aleatorios.

## Diapositiva 2 – Enunciado
- Simular el lanzamiento de un dado de 6 caras.
- Repetir la simulación 10 veces.
- Mostrar los resultados de cada lanzamiento.

## Diapositiva 3 – Idea de la solución
- Importar `random`.
- Usar `random.randint(1, 6)` dentro de un `for`.
- Imprimir el resultado en cada iteración.

## Diapositiva 4 – Código clave
- `import random`
- `for i in range(10):`
- `    lanzamiento = random.randint(1, 6)`
- `    print(lanzamiento)`

## Diapositiva 5 – Extensiones
- Contar cuántas veces salió cada cara.
- Representar los resultados en forma de histograma sencillo.

