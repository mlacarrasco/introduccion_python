import pandas as pd
df = pd.read_csv('data/african_crises.csv')

#pregunta 1
group_1 = df.groupby('country')
stats_1 = group_1['inflation_annual_cpi'].agg(['std', 'mean'])
print(stats_1)

#pregunta 2
group_2 = df[df['banking_crisis']=='no_crisis'].groupby('country')
stats_2 = group_2['inflation_annual_cpi'].agg(['std', 'mean'])
print(stats_2)
