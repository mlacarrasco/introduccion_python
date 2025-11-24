# Presentación Ejercicio 3.4 – Año bisiesto

## Diapositiva 1 – Título y objetivo
- Título: Condiciones anidadas para bisiestos.
- Objetivo: Implementar la regla completa de años bisiestos.

## Diapositiva 2 – Enunciado
- Pedir un año (entero).
- Determinar si es bisiesto siguiendo las reglas:
  - divisible por 4,
  - si es divisible por 100 también debe serlo por 400.

## Diapositiva 3 – Idea de la solución
- Usar operadores módulo `%` para comprobar divisibilidad.
- Anidar `if` para representar la regla.
- Imprimir si el año es o no bisiesto.

## Diapositiva 4 – Código clave
- `anio = int(input("Año: "))`
- `if anio % 4 == 0:`
- `    if anio % 100 == 0:`
- `        if anio % 400 == 0:`
- `            print("Bisiesto")`
- `        else:`
- `            print("No bisiesto")`
- `    else:`
- `        print("Bisiesto")`
- `else:`
- `    print("No bisiesto")`

## Diapositiva 5 – Extensiones
- Refactorizar la condición en una sola expresión lógica.
- Probar con años conocidos (2000, 1900, 2020, etc.).

