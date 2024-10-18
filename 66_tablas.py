import pandas as pd
import numpy as np

data = np.random.randint(0,20,(30,2))

df = pd.DataFrame(data, columns=['esta es la primera', 'segunda'])

print(df.loc[:,'esta es la primera'])


