import pandas as pd

ruta = input("Ingrese la ruta del archivo CSV: ")

try:
    df = pd.read_csv(ruta)
    print("Columnas disponibles:", df.columns.tolist())

    col_fila = input("Ingrese el nombre de la columna para las filas (por ejemplo, género): ")
    col_columna = input("Ingrese el nombre de la columna para las columnas (por ejemplo, tipo de curso): ")

    if col_fila in df.columns and col_columna in df.columns:
        tabla = pd.crosstab(df[col_fila], df[col_columna])
        print("Tabla de contingencia:")
        print(tabla)
    else:
        print("Las columnas ingresadas no existen en el DataFrame.")
except FileNotFoundError:
    print("No se encontró el archivo indicado.")
except Exception as e:
    print("Ocurrió un error:", e)

