import random

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import offline


class Figure:
    def __init__(self):
        self.fig = go.Figure()

    def add(self, tar):
        self.fig.add_trace(tar)

    def draw2DScatterPlot(self, x, y, mov):
        if mov == 0:
            line = px.scatter(x=x, y=y, labels={'x': 'X Axis', 'y': 'Y Axis'}, title='2D Scatter Plot',
                              color_discrete_sequence=random.sample([
                                  'blue',
                                  'lightsteelblue',
                                  'lightgreen',
                                  'orange',
                                  'purple',
                                  'green',
                                  'cyan',
                                  'brown',
                                  'pink',
                                  'lightsalmon'], 1))
            self.add(line.data[0])
        elif mov == 1:
            line = px.scatter(x=x, y=y, labels={'x': 'X Axis', 'y': 'Y Axis'}, title='2D Scatter Plot',
                              color_continuous_scale='jet')
            self.add(line.data[0])

    def drawLinearFunction(self, k, b, dom):
        x = np.linspace(dom[0], dom[1], 100)
        y = k * x + b
        line = go.Scatter(x=x, y=y, name=f'{round(k, 4)}x+{round(b, 4)}', marker=dict(colorscale='Viridis'))
        self.add(line)

    def show(self):
        self.fig.show()

    def save(self, filename):
        offline.plot(self.fig, filename=f'{filename}', auto_open=False)
