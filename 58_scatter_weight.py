import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/athlete_events.csv')

print(df.columns)
print(df.dtypes)

grupos = df.groupby('Year')
bit = df['Year']==1996

datos = grupos[['Weight', 'Height']].agg(['min', 'max', 'mean'])

plt.scatter(datos.index, datos ['Weight']['mean'])
plt.title ('peso promedio por año')
plt.xlabel('años')
plt.ylabel('Peso promedio (kg)')
plt.show()
