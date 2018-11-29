import numpy as numpy
import pandas as pandas

# import data csv, rename and rearrange headers
data = pandas.read_csv('./datasets/water.csv')
#print(data)

# import coordinates csv
coordinates = pandas.read_csv('./coordinates/coordinates_water.csv')
#print(coordinates)

# merge
merged = pandas.merge(data, coordinates, how='outer', right_on='Location', left_on='Location')
merged.drop(merged.columns[[4]], axis=1, inplace=True)
merged.drop_duplicates(inplace=True)
#print(merged)

# save to csv
merged.to_csv(path_or_buf='./water_merged.csv', index=False)
