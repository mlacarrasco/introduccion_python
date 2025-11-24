# Presentación Ejercicio 6.4 – Diccionario anidado de notas

## Diapositiva 1 – Título y objetivo
- Título: Diccionarios de diccionarios y listas.
- Objetivo: Practicar estructuras de datos anidadas.

## Diapositiva 2 – Enunciado
- Crear un diccionario que represente a un estudiante.
- Incluir su nombre y notas en varias asignaturas.
- Calcular y mostrar el promedio de cada asignatura.

## Diapositiva 3 – Idea de la solución
- Estructura propuesta:
  - `{"nombre": "...", "notas": {"Matemáticas": [5.0, ...], ...}}`.
- Recorrer `estudiante["notas"].items()` para obtener cada lista de notas.
- Calcular el promedio de cada lista.

## Diapositiva 4 – Código clave
- `for asignatura, lista_notas in estudiante["notas"].items():`
- `    promedio = sum(lista_notas) / len(lista_notas)`
- `    print(asignatura, promedio)`

## Diapositiva 5 – Extensiones
- Agregar nuevas asignaturas dinámicamente.
- Calcular un promedio general del estudiante.

