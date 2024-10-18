import pandas as pd

df = pd.read_csv('data/simple_data.csv')
print(df.describe(include='all'))
full_data   = df[['Nombre','Altura']]

columnas = df.columns

fillna_data = df['Altura'].fillna('nada')
id_nada   = df['Altura'].fillna('nada')=="nada"
print(df['Edad'].idxmin(axis=0))
df_seek_nada = df[df['Altura'].fillna('nada')!="nada"]

less_data = df.drop(columns=["Edad"])

nombres_unicos = full_data['Nombre'].unique()
print(nombres_unicos)
