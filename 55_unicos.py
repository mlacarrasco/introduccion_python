import pandas as pd

df = pd.read_csv('data/african_crises.csv')

print(df.shape[0])

unique_country = df['country'].unique()

print(list(unique_country))


n = df['country'].nunique()
print(f'Numero de paises: {n}')
