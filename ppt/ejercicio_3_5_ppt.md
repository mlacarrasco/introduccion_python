# Presentación Ejercicio 3.5 – Día de la semana

## Diapositiva 1 – Título y objetivo
- Título: Selección múltiple con `elif`.
- Objetivo: Asociar números a textos usando condicionales.

## Diapositiva 2 – Enunciado
- Pedir un número entre 1 y 7.
- Mostrar el día de la semana correspondiente:
  - 1 → lunes, 2 → martes, …, 7 → domingo.

## Diapositiva 3 – Idea de la solución
- Convertir la entrada a `int`.
- Usar una cadena de `if/elif` para cada día.
- Manejar el caso de número fuera de rango.

## Diapositiva 4 – Código clave
- `dia = int(input("Número (1-7): "))`
- `if dia == 1: print("Lunes")`
- `elif dia == 2: print("Martes")`
- `...`
- `else: print("Número inválido")`

## Diapositiva 5 – Extensiones
- Implementar la misma lógica con un diccionario.
- Soportar abreviaturas (“lun”, “mar”, etc.) como entrada.

