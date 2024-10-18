import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('data/data_venta_verduras.xlsx',sheet_name='Sheet1')

print(df.columns)

ct = pd.crosstab(df['Country'], df['Product'],margins=True)


print(ct)

#seleccionamos por nombre de fila
print(ct.loc['All'])
