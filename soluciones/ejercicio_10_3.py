import pandas as pd

ruta = input("Ingrese la ruta del archivo CSV: ")

try:
    df = pd.read_csv(ruta)
    print("Columnas disponibles:", df.columns.tolist())

    col_categoria = input("Ingrese el nombre de la columna categórica: ")
    col_valor = input("Ingrese el nombre de la columna de valores numéricos: ")

    if col_categoria in df.columns and col_valor in df.columns:
        tabla_pivote = df.pivot_table(index=col_categoria, values=col_valor, aggfunc="sum")
        print("Tabla pivote (suma por categoría):")
        print(tabla_pivote)
    else:
        print("Las columnas ingresadas no existen en el DataFrame.")
except FileNotFoundError:
    print("No se encontró el archivo indicado.")
except Exception as e:
    print("Ocurrió un error:", e)

