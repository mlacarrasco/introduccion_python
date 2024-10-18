import pandas as pd
import numpy as np
df = pd.read_csv('data/african_crises.csv')

#agrupamos por país
grp = df.groupby(['country'])

#determiamos aquellos valores por pais con crisis
tbl = grp['banking_crisis'].agg([('cont',lambda col:np.sum(col=='crisis'))])
print(f'Número de crisis por país {tbl}')

#buscamos el mayor de toda la tabla
id = pd.Series.argmax(tbl['cont'])
no_crisis = tbl.iloc[id].cont
print(f'{tbl.iloc[id].name} tiene un máximo de ({no_crisis} ) ')

