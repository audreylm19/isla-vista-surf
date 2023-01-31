import pandas as pd
from pathlib import Path
from datetime import timedelta
import numpy as np

from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, CustomJS, TapTool

#reading in data
root_folder = Path.cwd().parents[0]
df = pd.read_csv(root_folder/'data/processed'/'01-final.csv')
df['PSTdt'] = pd.to_datetime(df['PST'], utc=True)-timedelta(hours=8)

#creating month column
df['Month'] = df['PSTdt'].dt.month

#defining colors
colors = ["#1E90FF", "#32CD32", "#808080", "#FFA500", "#FF4500"]

#making a count column
ones = np.ones(df.shape[0], dtype=int)
df['count'] = ones

#booleans to filter by score
zero = df.Score == 0
one = df.Score == 1
two = df.Score == 2
three = df.Score == 3
four = df.Score == 4

#hour count for each score by year
bar0 = df[zero]['count'].groupby(df['PSTdt'].dt.year).sum()
bar1 = df[one]['count'].groupby(df['PSTdt'].dt.year).sum()
bar2 = df[two]['count'].groupby(df['PSTdt'].dt.year).sum()
bar3 = df[three]['count'].groupby(df['PSTdt'].dt.year).sum()
bar4 = df[four]['count'].groupby(df['PSTdt'].dt.year).sum()

#interaction
callback = CustomJS(code=
'''alert('!!!')''')
tap = TapTool(callback=callback)

#creating data source
data = {'0':bar0, '1':bar1, '2':bar2, '3':bar3, '4':bar4}
source = pd.DataFrame(data)

#plotting
TITLE = "Ideal Isla Vista Surf Conditions 2017-2021"
plot = figure(title=TITLE, toolbar_location=None, tools="hover", tooltips = "@$name hours with score $name", width=500, height=500)

plot.vbar_stack(['0','1','2','3','4'], 
    x='PSTdt', 
    width=0.9, 
    color=colors,
    line_color='white',
    legend_label=['0','1','2','3','4'],  
    source=source,
    # set visual properties for selected glyphs
    selection_color=colors,
    selection_line_color='white',

    # set visual properties for non-selected glyphs
    nonselection_fill_alpha=1.0,
    nonselection_fill_color=colors,
    nonselection_line_color='white',
    nonselection_line_alpha=1.0)

plot.title.text_font_size = '20px'

plot.legend.title = "Score"

plot.xaxis.major_label_text_font_style = 'bold'
plot.xaxis.major_label_text_font_size = '15px'

plot.yaxis.axis_label = "Total Daylight Hours"
plot.yaxis.axis_label_text_font_style = 'bold'
plot.yaxis.axis_label_text_font_size = '15px'

plot.xgrid.visible = False
plot.ygrid.visible = False

plot.y_range.range_padding = 0.02

show(plot)