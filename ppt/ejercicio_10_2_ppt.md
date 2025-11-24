# Presentación Ejercicio 10.2 – Promedio de nota por carrera

## Diapositiva 1 – Título y objetivo
- Título: Agrupar datos con pandas.
- Objetivo: Practicar `DataFrame`, valores únicos y `groupby`.

## Diapositiva 2 – Enunciado
- Crear un `DataFrame` de estudiantes con columnas:
  - nombre, carrera, nota.
- Mostrar las carreras únicas.
- Calcular el promedio de nota por carrera.

## Diapositiva 3 – Idea de la solución
- Construir el `DataFrame` a partir de un diccionario.
- Usar `df["Carrera"].unique()` para ver carreras distintas.
- Aplicar `df.groupby("Carrera")["Nota"].mean()`.

## Diapositiva 4 – Código clave
- `df = pd.DataFrame(datos)`
- `print(df["Carrera"].unique())`
- `print(df.groupby("Carrera")["Nota"].mean())`

## Diapositiva 5 – Extensiones
- Agregar más columnas (por ejemplo, semestre).
- Ordenar el resultado por promedio de nota.

