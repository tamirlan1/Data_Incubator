import pandas as pd
import numpy as np
import os
from os.path import join
import math
base_dir = os.path.dirname(os.path.realpath(__name__))
csv_files = [f for f in os.listdir(join(base_dir, 'Q2_data')) if f.endswith('.csv')]
dataframes = []
for csv_file in csv_files:
    dataframes.append(pd.read_csv(join('Q2_data', csv_file)))
    
print len(dataframes)
data = pd.concat(dataframes)
print data.shape
data['month'] = pd.DatetimeIndex(data['starttime']).month
print 'grouping is done'
df = data.groupby("month").agg({"tripduration": np.mean})
print df
longest = max(data['tripduration'])
shortest = min(data['tripduration'])
print longest
print shortest
print longest - shortest