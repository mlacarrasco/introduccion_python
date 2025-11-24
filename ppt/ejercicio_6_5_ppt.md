# Presentación Ejercicio 6.5 – Filtrado de productos por precio

## Diapositiva 1 – Título y objetivo
- Título: Recorrer diccionarios y aplicar filtros.
- Objetivo: Practicar selección de elementos según su valor.

## Diapositiva 2 – Enunciado
- Crear un diccionario de productos con su precio.
- Pedir un precio mínimo al usuario.
- Mostrar sólo los productos cuyo precio sea mayor que ese mínimo.

## Diapositiva 3 – Idea de la solución
- Definir el diccionario con nombres como claves y precios enteros.
- Leer el límite y convertirlo a `int`.
- Recorrer el diccionario con `.items()` y aplicar la condición.

## Diapositiva 4 – Código clave
- `productos = {"Pan": 1000, ...}`
- `limite = int(input("Precio mínimo: "))`
- `for nombre, precio in productos.items():`
- `    if precio > limite:`
- `        print(nombre, "->", precio)`

## Diapositiva 5 – Extensiones
- Construir un diccionario nuevo sólo con los productos filtrados.
- Ordenar la salida por precio.

