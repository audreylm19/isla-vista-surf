from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, CustomJS, TapTool
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.layouts import row

#interaction
callback = CustomJS(code=
'''alert('!!!')''')
tap = TapTool(callback=callback)

# Create the bar chart
bar_source = ColumnDataSource(data=dict(x=[1, 2, 3, 4, 5], y=[4, 5, 6, 2, 8]))
bar = figure(title="Bar Chart", x_range=(0, 6), y_range=(0, 10), tools=[tap])
bar.vbar(x='x', top='y', width=0.9, source=bar_source)

show(bar)