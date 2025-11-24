import pandas as pd
import matplotlib.pyplot as plt

ruta = input("Ingrese la ruta del archivo CSV: ")

try:
    df = pd.read_csv(ruta)
    print("Columnas disponibles:", df.columns.tolist())

    x_col = input("Ingrese el nombre de la columna para el eje X: ")
    y_col = input("Ingrese el nombre de la columna para el eje Y: ")

    if x_col in df.columns and y_col in df.columns:
        plt.scatter(df[x_col], df[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title("Gráfico de dispersión")
        plt.show()
    else:
        print("Las columnas ingresadas no existen en el DataFrame.")
except FileNotFoundError:
    print("No se encontró el archivo indicado.")
except Exception as e:
    print("Ocurrió un error:", e)

