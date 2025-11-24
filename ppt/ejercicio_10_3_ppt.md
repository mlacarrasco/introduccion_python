# Presentación Ejercicio 10.3 – Tabla pivote por categoría

## Diapositiva 1 – Título y objetivo
- Título: Uso de `pivot_table` en pandas.
- Objetivo: Practicar agregación de datos por categorías.

## Diapositiva 2 – Enunciado
- Leer un CSV con al menos una columna categórica y otra numérica.
- Crear una tabla pivote que muestre la suma de los valores por categoría.

## Diapositiva 3 – Idea de la solución
- Leer el CSV en `df`.
- Pedir al usuario qué columna será la categoría y cuál el valor.
- Usar `df.pivot_table(index=col_categoria, values=col_valor, aggfunc="sum")`.

## Diapositiva 4 – Código clave
- `tabla = df.pivot_table(index=col_categoria,`
- `                       values=col_valor,`
- `                       aggfunc="sum")`
- `print(tabla)`

## Diapositiva 5 – Extensiones
- Probar otras funciones de agregación: `mean`, `max`, `min`.
- Exportar la tabla pivote a un nuevo CSV.

