import pandas as pd
import numpy as np

def ideal_wind(df, wind_direction: list, wind_speed: list):
    """Creates Ideal Wind column, 0 for bad wind, 1 for good wind"""

    zeros = np.zeros(df.shape[0],dtype=int)
    df['Ideal Wind']=zeros

    #low speed winds are ideal
    df.loc[df['Wind Speed'] <= wind_speed[0], 'Ideal Wind'] = 1

    #filter for direction
    wdints = pd.to_numeric(df['Wind Direction'],errors='coerce') #only care about integer values
    goodwind = (wind_direction[0] <= wdints) & (wdints <= wind_direction[1]) 
    df.loc[goodwind, 'Ideal Wind'] = 1

    #high speed winds bad
    df.loc[df['Wind Speed']>=wind_speed[1], 'Ideal Wind'] = 0

    return

def ideal_period(df, good_period: int):
    "Creates Ideal Period column, 0 for bad period, 1 for good period"
    
    zeros = np.zeros(df.shape[0],dtype=int)
    df['Ideal Period']=zeros

    #longer periods good
    df.loc[df['Period']>=good_period, 'Ideal Period'] = 1

    return

def ideal_tide(df, good_tide: list):
    """Creates Ideal Tide column, 0 for bad tide, 1 for good tide"""

    zeros = np.zeros(df.shape[0],dtype=int)
    df['Ideal Tide']=zeros

    #in good tide range
    good = (good_tide[0] <= df.Tide) & (df.Tide <= good_tide[1])
    df.loc[good, 'Ideal Tide'] = 1

    return

def ideal_swell(df, direction: list, height: list):
    """Creates Ideal Swell column, 0 for bad swell, 1 for good swell"""

    zeros = np.zeros(df.shape[0],dtype=int)
    df['Ideal Swell'] = zeros

    #want both direction and height
    good_direction = (direction[0] <= df.Deg) & (df.Deg <= direction[1])
    good_height = (height[0] <= df.Height) & (df.Height <= height[1])
    good = good_direction & good_height
    df.loc[good, 'Ideal Swell'] = 1

    return 

def make_ideals(df, Ideals: dict):
    
    ideal_wind(df, Ideals['wind_direction'], Ideals['wind_speed'])
    ideal_period(df, Ideals['period'])
    ideal_tide(df, Ideals['tide'])
    ideal_swell(df, Ideals['swell_direction'], Ideals['swell_height'])

    return