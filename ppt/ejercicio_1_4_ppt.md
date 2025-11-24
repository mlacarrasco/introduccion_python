# Presentación Ejercicio 1.4 – Repetición de nombre

## Diapositiva 1 – Título y objetivo
- Título: Repetir textos varias veces.
- Objetivo: Combinar `input()`, conversión a entero y ciclos.

## Diapositiva 2 – Enunciado
- Pedir al usuario su nombre.
- Pedir cuántas veces quiere ver su nombre.
- Imprimir el nombre repetido la cantidad de veces indicada.

## Diapositiva 3 – Idea de la solución
- Leer el nombre como cadena.
- Leer la cantidad como cadena y convertirla a `int`.
- Usar un ciclo `for` para imprimir el nombre varias veces.

## Diapositiva 4 – Código clave
- `nombre = input("Ingrese su nombre: ")`
- `veces = int(input("¿Cuántas veces?: "))`
- `for i in range(veces):`
- `    print(nombre)`

## Diapositiva 5 – Extensiones
- Manejar errores si la cantidad no es un número.
- Numerar cada línea: `print(i+1, nombre)`.

