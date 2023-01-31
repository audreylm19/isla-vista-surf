import pandas as pd
import numpy as np

from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Range1d

def chooseYear(year: int, df):
    data = df[df.PSTdt.dt.year == year]
    data = data.sort_values(by=['Month','Score', 'PSTdt'], axis=0).reset_index(drop=True)
    #for x values later
    data['nth hour'] = data.index.to_list()
    data['nth hour'] = data['nth hour'].apply(lambda x: float(x))+1
    return data 

def makeCounts(df):
    #creating culmulative hour column for use in normalizing y values later
    counts = df.groupby('Month').count()
    counts['count']=counts['PST']
    counts = counts.reset_index()[['Month','count']]
    row = {'Month': 0, 'count':0}
    row = pd.DataFrame(data=row, index=[0])
    counts = pd.concat([counts,row], ignore_index=True)

    n=0
    for i in range(13): 
        n += counts.loc[i,'count']
        counts.loc[i,'count'] = n
    counts.loc[12, 'count'] = 0

    counts = counts.shift(2).fillna(0)
    counts.Month = counts.index.to_list()

    #merging with original df
    df = df.merge(counts, on = "Month")

    #counting total hours by score and month
    score_counts = df.groupby(['Month', 'Score']).count()
    score_counts['totals'] = score_counts['PST']
    score_counts = score_counts['totals'].reset_index()
    df = df.merge(score_counts, left_on=['Month', 'Score'], right_on=['Month','Score'])

    return df

def makeXY(width: int, space: int, df):
    #define width of bar and space between bars

    #create x-y positions
    df['x'] = (df['nth hour'] % width)
    df['x'] += 1+(df['Month']-1)*width + (df['Month']-1)*space
    df['y'] = np.ceil((df['nth hour']-df['count'])/width)

    return df

def makePlot(width: int, space: int, df):
    source = ColumnDataSource(data=df)

    TITLE = 'Hourly Wave Quality in Isla Vista ' + str(df.PSTdt[0].year)
    TOOLS = "hover,wheel_zoom,box_zoom,reset,save"

    plot = figure(tools=TOOLS, toolbar_location='above',
        title=TITLE, width=1000, height=500,
        min_border=0,
        #x_range = Range1d(0, 20),
        #y_range = Range1d(0,5000)
        )
    #plot.title.align = 'center'
    plot.title.text_font_size = '20px'

    plot.hover.tooltips = [
        ("time", "@PSTdt{%m/%d at %H:00}"),
        ("score", "@Score"),
        ("total hours with this score", "@totals"),
        ("tide (ft)", "@Tide"),
        ("swell height (m)", "@Height"),
        ("swell direction", "@Deg"),
        ("swell period (s)", "@Period"),
        ("wind speed (mph)", "@{Wind Speed}"),
        ("wind direction", "@{Wind Direction}")
    ]

    plot.hover.formatters = {'@PSTdt': 'datetime'}

    plot.scatter(x="x", y="y", size=10, source=source, color="color", line_color="white", marker='square')

    #creating month ticks

    #defining locations
    ticks = []
    for i in range(12):
        ticks.append((width+2)/2 + i*(space+width))
    plot.xaxis.ticker = ticks

    #writing labels
    month_labels = ['Jan', 'Feb', 'Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
    x_labels = dict(zip(ticks, month_labels))
    plot.xaxis.major_label_overrides = x_labels
    # plot.xaxis.axis_label = "Month"
    # plot.xaxis.axis_label_text_font_style = 'bold'
    # plot.xaxis.axis_label_text_font_size = '15px'
    plot.xaxis.major_label_text_font_style = 'bold'
    plot.xaxis.major_label_text_font_size = '15px'

    #hiding grid and y-axis
    plot.yaxis.visible = False
    plot.xgrid.visible = False
    plot.ygrid.visible = False

    plot.y_range.range_padding = 0.02
    show(plot)
    return

def makeScatterBar(year: int, width: int, space: int, df):
    df = chooseYear(year, df)
    df = makeCounts(df)
    df = makeXY(width, space, df)
    makePlot(width, space, df)
    return








