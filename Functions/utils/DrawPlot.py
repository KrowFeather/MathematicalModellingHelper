import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import offline


class Figure:
    def __init__(self):
        self.fig = go.Figure()

    def add(self, tar):
        self.fig.add_trace(tar)

    def draw2DScatterPlot(self, x, y):
        line = px.scatter(x=x, y=y, labels={'x': 'X Axis', 'y': 'Y Axis'}, title='2D Scatter Plot')
        self.add(line.data[0])

    def drawLinearFunction(self, k, b, dom):
        x = np.linspace(dom[0], dom[1], 100)
        y = k * x + b
        line = go.Scatter(x=x, y=y)
        self.add(line)

    def show(self):
        self.fig.show()

    def save(self, filename):
        offline.plot(self.fig, filename=f'{filename}', auto_open=False)
