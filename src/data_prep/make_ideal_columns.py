from ideal_filters import make_ideals
from ideal_dictionary import Ideals

import pandas as pd
import numpy as np
from pathlib import Path

root_folder = Path.cwd().parents[1]
df = pd.read_csv(root_folder/'data/processed/00-final.csv')

make_ideals(df, Ideals)

df['Score'] = df[['Ideal Wind', 'Ideal Tide', 'Ideal Swell', 'Ideal Period']].sum(axis=1)

df.to_csv(root_folder/'data/processed/01-final.csv', index=False)