import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

root_folder = Path.cwd().parents[1]

#which file do you want to graph
filename = '01-final.csv'

#how to save graph
graphname = 'bar.png'

columns = ['PST','Score']
df = pd.read_csv(root_folder/'data/processed'/filename, usecols=columns)
df['UTC'] = pd.to_datetime(df['PST'], utc=True)

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
bar0 = df[zero]['count'].groupby(df['UTC'].dt.year).sum()
bar1 = df[one]['count'].groupby(df['UTC'].dt.year).sum()
bar2 = df[two]['count'].groupby(df['UTC'].dt.year).sum()
bar3 = df[three]['count'].groupby(df['UTC'].dt.year).sum()
bar4 = df[four]['count'].groupby(df['UTC'].dt.year).sum()


#ALL OF THE PLOTTING

#names of group and bar width and edgecolor
names = bar0.index.to_list()
bar_width = 1
edgecolor = 'white'

#position of bars on the x-axis
r = np.arange(len(names))

#bar heights
bar2_start = np.add(bar0,bar1).tolist()
bar3_start = np.add(bar2_start, bar2).tolist()
bar4_start = np.add(bar3_start, bar3).tolist()

#plot size
plt.figure(figsize=(6,8))

#create zero bars
plt.bar(r, bar0, color='gray', edgecolor = edgecolor, width=bar_width)

#create one bars
plt.bar(r, bar1, bottom=bar0, color='dodgerblue', edgecolor = edgecolor, width=bar_width)

#create two bars
plt.bar(r, bar2, bottom=bar2_start, color='limegreen', edgecolor = edgecolor, width=bar_width)

#create three bars
plt.bar(r, bar3, bottom=bar3_start, color='orange', edgecolor = edgecolor, width=bar_width)

#create four bars
plt.bar(r, bar4, bottom=bar4_start, color='orangered', edgecolor = edgecolor, width=bar_width)

#custom x axis
plt.xticks(r,names, fontweight='bold')
plt.xlabel('Year')

plt.ylabel('Surfable Hours')

# Add a legend
gray = mpatches.Patch(color='gray', label='0')
blue = mpatches.Patch(color='dodgerblue', label='1')
green = mpatches.Patch(color='limegreen', label='2')
orange = mpatches.Patch(color='orange', label='3')
red = mpatches.Patch(color='orangered', label='4')
plt.legend(handles = [red,orange,green,blue,gray],loc='upper left', bbox_to_anchor=(1,1), ncol=1)

plt.title('Number of Ideal Conditions Met', loc='center')

plt.savefig('plots/'+graphname, bbox_inches='tight')

plt.show()
