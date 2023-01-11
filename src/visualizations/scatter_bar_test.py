import pandas as pd
import numpy as np
from bokeh.io import curdoc, show
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, Scatter, Range1d

#how to save graph
#graphname = 'scatter-bar-test.png'

#x values
l = [1,2,3]
x = l*5
l = [6,7,8]
x.extend(l*10)

#y values
y=[]
for i in range(5):
    l = [i,i,i]
    y.extend(l)
for i in range(10):
    l=[i,i,i]
    y.extend(l)

data = {'x_values':x,
        'y_values':y}

source = ColumnDataSource(data=data)

plot = Plot(
    title=None, width=300, height=300,
    min_border=0, toolbar_location=None,
    x_range = Range1d(0, 20),
    y_range = Range1d(0,20))

glyph = Scatter(x="x_values", y="y_values", size=20, fill_color="#74add1")

plot.add_glyph(source, glyph)

xaxis = LinearAxis()
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot.add_layout(yaxis, 'left')

plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

curdoc().add_root(plot)

show(plot)


