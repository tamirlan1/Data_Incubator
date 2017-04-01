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
    
data = pd.concat(dataframes)

# Q1: What is the median trip duration, in seconds?
print np.median(data['tripduration'])

# Q2: What fraction of rides start and end at the same station?

same_station = (data['start station id'] == data['end station id'])
print sum(same_station)
fraction = float(sum(same_station)) / len(same_station)
print fraction
same_station2 = (data['start station name'] == data['end station name'])
print sum(same_station2)
same_station3 = (data['start station latitude'] == data['end station latitude'])
print sum(same_station3)
same_station4 = (data['start station longitude'] == data['end station longitude'])
print sum(same_station4)
df_bike_station_start = data[['bikeid', 'start station id']]
df_bike_station_end = data[['bikeid', 'end station id']]

# What is the standard deviation of the number of stations visited by a bike?

df_bike_station_start.columns=['bike', 'station id']
df_bike_station_end.columns=['bike', 'station id']
df_bike_station = pd.concat([df_bike_station_start, df_bike_station_end])
df_bike_station_groupby = df_bike_station.groupby("bike").agg({"station id": pd.Series.nunique})
# print df_bike_station_groupby
print np.std(df_bike_station_groupby['station id'])

#What is the average length, in kilometers, of a trip?
df_not_same_station = data[same_station == False]

lat1 = np.radians(df_not_same_station['start station latitude'])
lon1 = np.radians(df_not_same_station['start station longitude'])
lat2 = np.radians(df_not_same_station['end station latitude'])
lon2 = np.radians(df_not_same_station['end station longitude'])
R = 6373
dlon = lon2 - lon1
dlat = lat2 - lat1
a = (np.sin(dlat/2))**2 + np.cos(lat1) * np.cos(lat2) * (np.sin(dlon/2))**2 
c = 2 * np.arctan2( np.sqrt(a), np.sqrt(1-a) ) 
df_not_same_station['trip length'] = R * c
print df_not_same_station

print np.mean(df_not_same_station['trip length'])

# Calculate the average duration of trips for each month in the year. (Consider a trip to occur in the month in which it starts.) What is the difference, in seconds, between the longest and shortest average durations?
#data['month'] = pd.DatetimeIndex(data['starttime']).month
data['month'] = data['starttime'].apply(lambda x: str(x).split('/')[0])
df = data.groupby("month").agg({"tripduration": np.mean})
print df
longest = max(df['tripduration'])
shortest = min(df['tripduration'])
print longest
print shortest
print longest - shortest

# Let us define the hourly usage fraction of a station to be the fraction of all rides starting at that station that leave during a specific hour. A station has surprising usage patterns if it has an hourly usage fraction for an hour significantly different from the corresponding hourly usage fraction of the system as a whole. What is the largest ratio of station hourly usage fraction to system hourly usage fraction (hence corresponding to the most "surprising" station-hour pair)?
# data['hour'] = pd.DatetimeIndex(data['starttime']).hour
data['hour'] = data['starttime'].apply(lambda x: str(x).split()[1].split(':')[0] if len(str(x).split()[1].split(':')[0])==2 else '0' + str(x).split()[1].split(':')[0])
slice_df2 = data.groupby("hour").agg({"tripduration": 'count'})
slice_df2.columns = ['system hourly fraction']
slice_df2['system hourly fraction'] = slice_df2['system hourly fraction'] / sum(slice_df2['system hourly fraction'])

print sum(slice_df2['system hourly fraction'])

slice_df3 = slice_df.groupby(['hour', 'start station id']).agg({'tripduration': 'count'}).reset_index()
slice_df3.columns = ['hour', 'start station id', 'count']
slice_df4 = slice_df3.groupby('hour').agg({'count': 'count'})
# print slice_df2
slice_df2['count by station'] = slice_df4['count']
slice_df2['max by station'] = slice_df3.groupby('hour').agg({'count': max})
slice_df2['fraction max by station'] = slice_df2['max by station'] / slice_df2['count by station']
slice_df2['golden ration'] = slice_df2['fraction max by station'] / slice_df2['system hourly fraction']
print 'Largest Ratio:', max(slice_df2['golden ration'])
print slice_df2

# There are two types of riders: "Customers" and "Subscribers." Customers buy a short-time pass which allows 30-minute rides. Subscribers buy yearly passes that allow 45-minute rides. What fraction of rides exceed their corresponding time limit?
exceed = (data['usertype'] == 'Subscriber') & (data['tripduration'] > 45*60) | (data['usertype'] == 'Customer') & (data['tripduration'] > 30*60)
print float(sum(exceed)) / len(exceed)

# Most of the time, a bike will begin a trip at the same station where its previous trip ended. Sometimes a bike will be moved by the program, either for maintenance or to rebalance the distribution of bikes. What is the average number of times a bike is moved during this period, as detected by seeing if it starts at a different station than where the previous ride ended?
df0 = data.groupby(['bikeid', 'starttime', 'start station id', 'end station id']).count().reset_index()#.agg({"station id": pd.Series.nunique})
print df0

#LAST question
dff = data.sort(['bikeid', 'starttime'])
dff['end station id'] = dff['end station id'].shift(1)
good = (dff['start station id'] == dff['end station id'])
goodsum = sum(good)
unique = len(dff.bikeid.unique())
# all = len(good)
print float(goodsum + unique)/unique

