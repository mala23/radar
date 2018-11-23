import numpy as numpy
import pandas as pandas

# import data csv, rename and rearrange headers
data = pandas.read_csv('./datasets/wind_tidy.csv')
data.columns = ['Site', 'Startup', 'Production', 'Location', 'Canton', 'ZE-Coordinates']
data = data[['Location','Production','Startup']]

print(data)

# import coordinates csv
coordinates = pandas.read_csv('./coordinates/coordinates_wind.csv')

print(coordinates)

# merge
merged = pandas.merge(data, coordinates, how='outer', right_on='Location', left_on='Location')
#merged = merged[['Location','Production','Startup','Lat','Lng']]
merged.drop(merged.columns[[5]], axis=1, inplace=True)
merged.drop_duplicates(inplace=True)
print(merged)
