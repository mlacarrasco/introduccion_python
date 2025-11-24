# Presentación Ejercicio 5.5 – Lista de cuadrados

## Diapositiva 1 – Título y objetivo
- Título: Transformar listas con un segundo recorrido.
- Objetivo: Practicar la generación de una lista a partir de otra.

## Diapositiva 2 – Enunciado
- Leer 10 números enteros.
- Guardarlos en una lista original.
- Crear otra lista con el cuadrado de cada número.

## Diapositiva 3 – Idea de la solución
- Usar un ciclo `for` para leer y almacenar los valores.
- Crear una lista vacía para los cuadrados.
- Recorrer la lista original, elevar cada elemento al cuadrado y agregarlo.

## Diapositiva 4 – Código clave
- `enteros = []`
- `for i in range(10):`
- `    n = int(input("Número: "))`
- `    enteros.append(n)`
- `cuadrados = []`
- `for n in enteros:`
- `    cuadrados.append(n ** 2)`

## Diapositiva 5 – Extensiones
- Usar una *list comprehension* para generar la lista de cuadrados.
- Mostrar también la raíz cuadrada de cada número (si aplica).

