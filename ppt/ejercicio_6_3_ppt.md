# Presentación Ejercicio 6.3 – Diccionario de estudiantes

## Diapositiva 1 – Título y objetivo
- Título: Menú de gestión con diccionarios.
- Objetivo: Practicar operaciones de agregar y eliminar elementos.

## Diapositiva 2 – Enunciado
- Crear un diccionario donde la clave sea el RUT y el valor el nombre.
- Permitir agregar estudiantes.
- Permitir eliminar estudiantes por RUT.
- Mostrar la lista de estudiantes.

## Diapositiva 3 – Idea de la solución
- Usar un ciclo `while` para mostrar un menú de opciones.
- Para agregar: `estudiantes[rut] = nombre`.
- Para eliminar: `del estudiantes[rut]` si la clave existe.

## Diapositiva 4 – Código clave
- `estudiantes = {}`
- `while True:`
- `    # mostrar menú y leer opción`
- `    # según opción, agregar/eliminar/mostrar/salir`

## Diapositiva 5 – Extensiones
- Validar que el RUT no se repita al agregar.
- Guardar y cargar el diccionario desde un archivo de texto.

