import pandas as pd
import plotly.express as px
import plotly

plotly.io.renderers.default = 'colab'

import plotly.graph_objects as go

df = pd.read_csv('data/athlete_events.csv')

mujeres_2016 = df[(df['Sex']=='F') & (df['Year'] == 2016)]

fig = px.histogram(mujeres_2016, x="Age", y="Height")
fig.show()