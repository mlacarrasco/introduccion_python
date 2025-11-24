# Presentación Ejercicio 1.1 – Nombre y apellido

## Diapositiva 1 – Título y objetivo
- Título: Formato “Apellido, Nombre” en Python.
- Objetivo: Practicar `input()` y `print()` para combinar cadenas.

## Diapositiva 2 – Enunciado
- Pedir al usuario su nombre y apellido por teclado.
- Imprimirlos en una sola línea con el formato “Apellido, Nombre”.
- Ejemplo: entrada “Ana Pérez” → salida “Pérez, Ana”.

## Diapositiva 3 – Idea de la solución
- Leer nombre y apellido en dos variables con `input()`.
- Unirlos con una cadena intermedia `", "`.
- Mostrar el resultado con `print()`.

## Diapositiva 4 – Código clave
- `nombre = input("Ingrese su nombre: ")`
- `apellido = input("Ingrese su apellido: ")`
- `formato = apellido + ", " + nombre`
- `print(formato)`

## Diapositiva 5 – Extensiones
- Validar que las entradas no estén vacías.
- Convertir la primera letra a mayúscula con `.title()`.

