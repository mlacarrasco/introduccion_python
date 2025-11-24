# Presentación Ejercicio 5.3 – Nombres hasta “FIN”

## Diapositiva 1 – Título y objetivo
- Título: Listas con condición de término.
- Objetivo: Practicar ciclos con palabra clave de parada.

## Diapositiva 2 – Enunciado
- Leer nombres de estudiantes uno a uno.
- Detener la lectura cuando el usuario escriba “FIN”.
- Mostrar cuántos nombres se ingresaron en total.

## Diapositiva 3 – Idea de la solución
- Usar un `while True` para pedir nombres.
- Si el nombre es `"FIN"`, usar `break`.
- Agregar cada nombre válido a una lista y al final usar `len()`.

## Diapositiva 4 – Código clave
- `nombres = []`
- `while True:`
- `    nombre = input("Nombre: ")`
- `    if nombre == "FIN": break`
- `    nombres.append(nombre)`
- `print(len(nombres))`

## Diapositiva 5 – Extensiones
- Mostrar también la lista de nombres ingresados.
- Evitar que se agreguen cadenas vacías.

