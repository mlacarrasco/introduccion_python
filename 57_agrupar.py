import pandas as pd
df = pd.read_csv('data/simple_data.csv')

grupos = df.groupby('Edad')


print('\n\ndatos separados por grupos: \n')
for key, item in grupos:
   print(grupos.get_group(key), "\n")
