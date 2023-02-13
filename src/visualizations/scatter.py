import pandas as pd
from pathlib import Path
from datetime import timedelta
import numpy as np

from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import Range1d, ColumnDataSource
#reading in data
root_folder = Path.cwd().parents[1]
df = pd.read_csv(root_folder/'data/processed'/'01-final.csv')
df['PSTdt'] = pd.to_datetime(df['PST'], utc=True)-timedelta(hours=8)

#making a count column
ones = np.ones(df.shape[0], dtype=int)
df['count'] = ones

#getting best hours
four = df.Score == 4
bar4 = df[four]['count'].groupby(df['PSTdt'].dt.year).sum().reset_index()

#plotting
source = ColumnDataSource(bar4)
plot = figure(width=400, height=400, tools="hover", tooltips = "@count", title="Total Daylight Hours with Score 4")

plot.scatter("PSTdt", "count", source=source, size=20, color="#FF4500")

plot.title.text_font_size = '20px'

plot.xaxis.major_label_text_font_style = 'bold'
plot.xaxis.major_label_text_font_size = '15px'
plot.xaxis.minor_tick_line_color = None

# plot.yaxis.axis_label = "Daylight Hours with Score 4"
# plot.yaxis.axis_label_text_font_style = 'bold'
# plot.yaxis.axis_label_text_font_size = '15px'
plot.y_range = Range1d(150, 300)



show(plot)
