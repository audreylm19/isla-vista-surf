import pandas as pd
from pathlib import Path
from datetime import timedelta
import numpy as np

from bokeh.io import show
# from bokeh.plotting import figure
# from bokeh.models import ColumnDataSource, Range1d
from bokeh.resources import CDN
from bokeh.embed import file_html

import sys
sys.path.insert(1, 'C:\\Users\\audre\\Documents\\Data Science Portfolio\\Surf\\src\\data_prep')
from scatter_bar_functions import makeScatterBar

#reading in data
root_folder = Path.cwd().parents[1]
df = pd.read_csv(root_folder/'data/processed'/'01-final.csv')
df['PSTdt'] = pd.to_datetime(df['PST'], utc=True)-timedelta(hours=8)

#creating month column
df['Month'] = df['PSTdt'].dt.month

#defining colors
df['color'] = ''
df.loc[df['Score']==-1, 'color'] = "#DDDD00"
df.loc[df['Score']==1, 'color'] = "#1E90FF"
df.loc[df['Score']==2, 'color'] = "#32CD32"
df.loc[df['Score']==0, 'color'] = "#808080"
df.loc[df['Score']==3, 'color'] = "#FFA500"
df.loc[df['Score']==4, 'color'] = "#FF4500"


# p15 = makeScatterBar(2015, 5, 5, df)
# p16 = makeScatterBar(2016, 5, 5, df)
# p17 = makeScatterBar(2017, 5, 5, df)
# p18 = makeScatterBar(2018, 5, 5, df)
# p19 = makeScatterBar(2019, 5, 5, df)
# p20 = makeScatterBar(2020, 5, 5, df)
p21 = makeScatterBar(2021, 5, 5, df)

html = file_html(p21, CDN, "scatter_bar_2021")

# Creating an HTML file
file = open("scatter_bar_2021.html","w")
   
# Adding input data to the HTML file
file.write(html)
              
# Saving the data into the HTML file
file.close()

show(p21)