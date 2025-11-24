# Presentación Ejercicio 10.1 – Leer y describir un CSV

## Diapositiva 1 – Título y objetivo
- Título: Primeros pasos con pandas.
- Objetivo: Practicar lectura de datos desde un archivo CSV.

## Diapositiva 2 – Enunciado
- Pedir al usuario la ruta de un archivo CSV.
- Leerlo en un `DataFrame`.
- Mostrar las primeras 5 filas.
- Mostrar un resumen estadístico de las columnas numéricas.

## Diapositiva 3 – Idea de la solución
- Importar `pandas` como `pd`.
- Usar `pd.read_csv(ruta)` para cargar los datos.
- Mostrar `df.head()` y `df.describe()`.

## Diapositiva 4 – Código clave
- `import pandas as pd`
- `df = pd.read_csv(ruta)`
- `print(df.head())`
- `print(df.describe())`

## Diapositiva 5 – Extensiones
- Probar con diferentes archivos CSV.
- Guardar el resumen en un archivo de texto.

