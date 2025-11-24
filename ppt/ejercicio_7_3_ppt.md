# Presentación Ejercicio 7.3 – Fecha y hora actuales

## Diapositiva 1 – Título y objetivo
- Título: Trabajar con `datetime`.
- Objetivo: Practicar obtención de la fecha y hora del sistema.

## Diapositiva 2 – Enunciado
- Obtener la fecha y hora actuales.
- Imprimirlas completas.
- Imprimir sólo el año actual.

## Diapositiva 3 – Idea de la solución
- Importar `datetime` desde la biblioteca estándar.
- Usar `datetime.now()` para capturar el momento actual.
- Acceder a atributos como `.year`.

## Diapositiva 4 – Código clave
- `from datetime import datetime`
- `ahora = datetime.now()`
- `print("Fecha y hora:", ahora)`
- `print("Año:", ahora.year)`

## Diapositiva 5 – Extensiones
- Mostrar también mes y día por separado.
- Dar formato a la fecha con `strftime`.

