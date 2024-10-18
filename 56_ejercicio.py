
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/athlete_events.csv')

mujeres_2016 = df[(df['Sex']=='F') & (df['Year'] == 2016)]
alturas = mujeres_2016['Height'].dropna()

plt.hist(alturas, bins=20)
plt.grid(axis='y', alpha=0.15)      #crea una grilla con lineas
plt.xlabel('Valores de X')          # imprime el valor
plt.ylabel('Frecuencia')            #impriue la frecuencia
plt.title('Mi primer histograma')   # imprime el titulo
plt.savefig('histograma__.png')
plt.show()


