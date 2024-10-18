import pandas as pd
df = pd.read_csv('data/simple_data.csv')

list1 = df['Edad']>15
list2 = df['Altura']<24

df1= df[list1 & list2]
grupos = df.groupby('Altura')

print(df1)

