import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/athlete_events.csv')
grupos = df.groupby('Year')

datos = grupos['Weight', 'Height'].agg(['min', 'max', 'mean'])
plt.scatter(datos.index, datos ['Height']['mean'])
plt.show()

#ojo. Muy lento!!
#pd.plotting.radviz(df[['Weight', 'Height','Age','Year', 'Sex']],'Sex')
#plt.show()