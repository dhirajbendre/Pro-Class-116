import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv("data_classification.csv")
hours_slept = df["Hours_Slept"].tolist()
hours_studied = df["Hours_studied"].tolist()

fig = px.scatter(df, x=hours_slept, y=hours_studied)
fig.show()

import plotly.graph_objects as go
hours_slept = df["Hours_Slept"].tolist()
hours_studied = df["Hours_studied"].tolist()

results = df["results"].tolist()
colors = []

for data in results:
    if data == 1:
        colors.append("green")
    else:
        colors.append("red")    

fig = go.Figure(data=go.Scatter(
    x=hours_studied,
    y=hours_slept,
    mode ='markers',
    marker = dict(color=colors) 
))  
fig.show()      