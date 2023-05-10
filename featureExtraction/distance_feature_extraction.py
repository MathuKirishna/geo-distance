from geopy.geocoders import Nominatim
import pandas as pd
import math

df = pd.read_csv("../data/concat/geo_coded_feature_extracted_all.csv", header=0, sep=",")

print(df.columns)

source_latitude = df['source_latitude']
source_longitude = df['source_longitude']
target_latitude = df['DecimalLatitude']
target_longitude = df['DecimalLongitude']

# print(last_place_name.head)

def getDistance(source_lat, source_lon, target_lat, target_lon):
    R = 6371  # Earth's radius in kilometers

    source_lat, source_lon, target_lat, target_lon = map(math.radians, [source_lat, source_lon, target_lat, target_lon])

    dlat = target_lat - source_lat
    dlon = target_lon - source_lon

    a = math.sin(dlat / 2) ** 2 + math.cos(source_lat) * math.cos(target_lat) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c

    return d


df['distance']=0
for index, place_name in enumerate(target_latitude):
    distance = getDistance(source_latitude[index], source_longitude[index],target_latitude[index], target_longitude[index])
    df.at[index,'distance']=distance

print(df.head())

df.to_csv('../data/distance_added_feature_extracted_1500.csv', header=True, sep=',', index=False)
    