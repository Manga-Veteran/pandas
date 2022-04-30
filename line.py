import pandas as pd

import plotly.express as px

#reading data from csv files
df = pd.read_csv("data.csv")
fig = px.line(df, x='Country', y='InternetUsers')
fig.show()
