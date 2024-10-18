from plotly.offline import plot
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/athlete_events.csv')

mujeres_2016 = df[(df['Sex']=='F') & (df['Year'] == 2016)]

fig = px.histogram(mujeres_2016, x="Age", y="Height")

plot(fig, auto_open=True)


