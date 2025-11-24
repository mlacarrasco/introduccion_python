import pandas as pd

ruta = input("Ingrese la ruta del archivo CSV: ")

try:
    df = pd.read_csv(ruta)
    print("Primeras 5 filas:")
    print(df.head())
    print("\nDescripción estadística de columnas numéricas:")
    print(df.describe())
except FileNotFoundError:
    print("No se encontró el archivo indicado.")
except Exception as e:
    print("Ocurrió un error al leer el CSV:", e)

