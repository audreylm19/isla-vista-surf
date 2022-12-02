import gzip
import io
from pathlib import Path
import pandas as pd
import numpy as np

#gz = gzip file path name, a string
#txt = text file path name, a string
def clean_buoy(gz, txt):
    '''Write gzip file to text file, then clean data'''
    #unzipping
    file = gz
    with gzip.open(file, 'rb') as ip:
            with io.TextIOWrapper(ip, encoding='utf-8') as decoder:
                # Let's read the content using read()
                content = decoder.read()
    with open(txt, 'w') as f:
        f.write(content)
        
    #reading as space delimited file
    df = pd.read_csv(txt, sep='\s+', header=None)

    #all the cleaning
    df = df.iloc[:, 0:8].drop(index=1, columns=6)
    df.columns = df.iloc[0]
    df = df.drop([0], axis=0).rename(columns={"Hs": "Height", "Dp": "Deg"}).reset_index(drop='True')
    
    #getting rid of 30 minute data bc only need hour granularity
    df = df.iloc[::2].drop(columns=['MN'])
    
    return df 

def dt_swell(df):
    '''Make UTC column appropriate for datetime conversion'''
    #making columns in question strings
    df[['YEAR','MO','DY','HR']] = df[['YEAR','MO','DY','HR']].astype(str)
    
    #month formatting
    for i in range(len(df)):
        if len(df['MO'][i])<2:
            df['MO'][i]='0'+df['MO'][i]

    #day formatting
    for i in range(len(df)):
        if len(df['DY'][i])<2:
            df['DY'][i]='0'+df['DY'][i]

    #hour formatting
    for i in range(len(df)):
        if len(df['HR'][i])<2:
            df['HR'][i]='0'+df['HR'][i]
    
    #making a string that the to_datetime function will recognize
    df['UTC'] = df['YEAR']+df['MO']+df['DY']+df['HR']+'00'
    
    #dropping now useless columns
    df.drop(columns=['YEAR','MO','DY','HR'])
    
    return

root_folder = Path.cwd().parents[1]

s17 = clean_buoy(root_folder/'data/raw/cdip2017.gz', root_folder/'data/interim/swell2017.txt')
s18 = clean_buoy(root_folder/'data/raw/cdip2018.gz', root_folder/'data/interim/swell2018.txt')
s19 = clean_buoy(root_folder/'data/raw/cdip2019.gz', root_folder/'data/interim/swell2019.txt')
s20 = clean_buoy(root_folder/'data/raw/cdip2020.gz', root_folder/'data/interim/swell2020.txt')
s21 = clean_buoy(root_folder/'data/raw/cdip2021.gz', root_folder/'data/interim/swell2021.txt')