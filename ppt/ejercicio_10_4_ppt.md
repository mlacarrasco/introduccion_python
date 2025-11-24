# Presentación Ejercicio 10.4 – Gráfico de dispersión

## Diapositiva 1 – Título y objetivo
- Título: Visualización básica con matplotlib.
- Objetivo: Practicar gráficos de dispersión a partir de un CSV.

## Diapositiva 2 – Enunciado
- Leer un archivo CSV.
- Elegir dos columnas numéricas (para ejes X e Y).
- Dibujar un gráfico de dispersión (scatter) con esos datos.

## Diapositiva 3 – Idea de la solución
- Leer los datos en un `DataFrame`.
- Usar `plt.scatter(df[x_col], df[y_col])`.
- Etiquetar los ejes y mostrar el gráfico con `plt.show()`.

## Diapositiva 4 – Código clave
- `import matplotlib.pyplot as plt`
- `plt.scatter(df[x_col], df[y_col])`
- `plt.xlabel(x_col); plt.ylabel(y_col)`
- `plt.show()`

## Diapositiva 5 – Extensiones
- Cambiar color y tamaño de los puntos.
- Guardar el gráfico a un archivo de imagen.

