# Presentación Ejercicio 6.1 – Diccionario de cursos

## Diapositiva 1 – Título y objetivo
- Título: Diccionarios básicos en Python.
- Objetivo: Practicar creación y recorrido de diccionarios.

## Diapositiva 2 – Enunciado
- Crear un diccionario que almacene el nombre de 3 cursos.
- Cada curso tiene asociado la cantidad de créditos.
- Mostrar todos los pares `curso -> créditos`.

## Diapositiva 3 – Idea de la solución
- Definir el diccionario con llaves de texto y valores enteros.
- Usar `for clave, valor in dicc.items()` para recorrerlo.

## Diapositiva 4 – Código clave
- `cursos = {"Matemáticas": 10, "Programación": 8, "Física": 9}`
- `for nombre, creditos in cursos.items():`
- `    print(nombre, "->", creditos)`

## Diapositiva 5 – Extensiones
- Permitir que el usuario agregue un curso nuevo.
- Calcular el total de créditos sumando los valores.

