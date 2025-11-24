# Presentación Ejercicio 10.5 – Tabla de contingencia (`crosstab`)

## Diapositiva 1 – Título y objetivo
- Título: Tablas de frecuencia con pandas.
- Objetivo: Practicar `pd.crosstab` con variables categóricas.

## Diapositiva 2 – Enunciado
- Leer un CSV con dos columnas categóricas (por ejemplo, género y tipo de curso).
- Generar una tabla de contingencia que muestre la frecuencia de cada combinación.

## Diapositiva 3 – Idea de la solución
- Leer el CSV en un `DataFrame`.
- Elegir las columnas categóricas para filas y columnas.
- Usar `pd.crosstab(df[col_fila], df[col_columna])`.

## Diapositiva 4 – Código clave
- `tabla = pd.crosstab(df[col_fila], df[col_columna])`
- `print(tabla)`

## Diapositiva 5 – Extensiones
- Normalizar la tabla para obtener proporciones.
- Representar la tabla en un gráfico de barras o mapa de calor.

