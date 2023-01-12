import pandas as pd
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Range1d

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

d = {'x': x, 'y': y}
df = pd.DataFrame(data=d)
df['Score'] = ''
df.loc[df.x < 5, 'Score'] = "#053061"
df.loc[df.x >5, 'Score'] = "#67001f"

source = ColumnDataSource(data=df)


plot = figure(
    title=None, width=300, height=300,
    min_border=0, toolbar_location=None,
    x_range = Range1d(0, 20),
    y_range = Range1d(0,20))

plot.scatter(x="x", y="y", size=20, source=source, color="Score", line_color="black")

show(plot)


