import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Pedro", "Juan", "Ana"],
    "Carrera": ["Ing. Civil", "Ing. Civil", "Ing. Informática", "Ing. Informática", "Ing. Civil"],
    "Nota": [5.0, 4.5, 6.0, 5.5, 6.5]
}

df = pd.DataFrame(datos)

print("DataFrame de estudiantes:")
print(df)

print("\nCarreras únicas:")
print(df["Carrera"].unique())

print("\nPromedio de nota por carrera:")
print(df.groupby("Carrera")["Nota"].mean())

