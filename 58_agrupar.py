import pandas as pd
import numpy as np
df = pd.read_csv('data/simple_data.csv')

grupos = df.groupby('Edad')

result = grupos['Altura'].agg([sorted, ('desp',lambda x: np.std(x, ddof=0))])

print(result)
