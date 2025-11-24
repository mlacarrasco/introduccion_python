# Presentación Ejercicio 3.3 – Puede votar según país

## Diapositiva 1 – Título y objetivo
- Título: Condicionales con texto y números.
- Objetivo: Combinar comparaciones de cadenas e enteros.

## Diapositiva 2 – Enunciado
- Pedir la edad de una persona.
- Pedir el país (por ejemplo “Chile” u “Otro”).
- Determinar si puede votar:
  - En Chile, desde los 18 años;
  - En otros países, desde los 21 años (regla simplificada).

## Diapositiva 3 – Idea de la solución
- Convertir edad a `int`.
- Pasar el país a minúsculas con `.lower()`.
- Usar `if` para decidir el umbral de edad.

## Diapositiva 4 – Código clave
- `edad = int(input("Edad: "))`
- `pais = input("País: ").lower()`
- `if pais == "chile":`
- `    puede = edad >= 18`
- `else:`
- `    puede = edad >= 21`

## Diapositiva 5 – Extensiones
- Manejar más países con diferentes edades mínimas.
- Mostrar en cuántos años más podría votar si aún no puede.

