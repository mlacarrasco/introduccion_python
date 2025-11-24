# Presentación Ejercicio 6.2 – Países y capitales

## Diapositiva 1 – Título y objetivo
- Título: Diccionario editable desde teclado.
- Objetivo: Practicar inserción y consulta en diccionarios.

## Diapositiva 2 – Enunciado
- Crear un diccionario de capitales.
- Pedir al usuario un país y su capital y agregarlos.
- Luego permitir consultar la capital de un país dado.

## Diapositiva 3 – Idea de la solución
- Iniciar el diccionario vacío o con algunos datos.
- Asignar `capitales[pais] = capital`.
- Verificar si un país está con `if pais in capitales`.

## Diapositiva 4 – Código clave
- `capitales = {}`
- `pais = input("País: ")`
- `capital = input("Capital: ")`
- `capitales[pais] = capital`
- `consulta = input("País a consultar: ")`

## Diapositiva 5 – Extensiones
- Cargar varias parejas país-capital en un ciclo.
- Mostrar todas las capitales guardadas al final.

