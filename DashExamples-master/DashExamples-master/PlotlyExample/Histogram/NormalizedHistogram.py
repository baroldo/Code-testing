import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df = pd.read_csv('../Data/salary.csv')

# Data
data = []
x = np.random.randn(500)
data.append(go.Histogram(x=x, histnorm='probability'))
# Layout
layout = {'title':{'text':'Distribution of 500 Random Numbers', 'x':0.5}}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='normalized_histogram.html')
