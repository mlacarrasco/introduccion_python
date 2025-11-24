# Presentación Ejercicio 4.1 – Suma de números hasta 0

## Diapositiva 1 – Título y objetivo
- Título: Acumulador con ciclo `while`.
- Objetivo: Practicar lectura repetitiva y condición de término.

## Diapositiva 2 – Enunciado
- Leer números enteros desde teclado.
- Acumular la suma de todos ellos.
- Detener la lectura cuando el usuario ingrese 0 y mostrar el total.

## Diapositiva 3 – Idea de la solución
- Usar un `while True` para pedir números indefinidamente.
- Si el número ingresado es 0, usar `break`.
- Ir sumando cada número válido en una variable `suma`.

## Diapositiva 4 – Código clave
- `suma = 0`
- `while True:`
- `    n = int(input("Número: "))`
- `    if n == 0: break`
- `    suma = suma + n`

## Diapositiva 5 – Extensiones
- Contar cuántos números se ingresaron.
- Calcular también el promedio de los números leídos.

