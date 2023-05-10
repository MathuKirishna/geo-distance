from geopy.geocoders import Nominatim
import pandas as pd
import time


df = pd.read_csv("../data/ner_feature_extracted_all.csv", header=0, sep=",")
# print(df.columns)
start=900
end=1500
df=df[start:end]
print(df.head)
last_place_name= df['last_place_name']
# print(last_place_name.head)

def getGeoCoding(location:str, index):
    ZELAND = "Zealand"
    name_place=""
    if location.lower() in ZELAND.lower():
        name_place = location
    else:
        name_place= location + ", New Zealand"
    user_agent = "test-application_"+str(index)
    # Initialize the Nominatim geocoder
    geolocator = Nominatim(user_agent=user_agent, timeout=None)

    # Geocode the place
    geoCode = geolocator.geocode(name_place)
    return geoCode

null_data_count = 0
null_data_indices = []
df['source_latitude']=0
df['source_longitude']=0
for index, place_name in enumerate(last_place_name):
    time.sleep(1)
    geoCode = getGeoCoding(place_name,index)
    print(index)
    if geoCode !=None:
        df.at[index,'source_latitude']=geoCode.latitude
        df.at[index,'source_longitude']=geoCode.longitude
        print("null data count: ", null_data_count)
    else:
        null_data_count+=1
        null_data_indices.append(index)

print(null_data_count)
for index in null_data_indices:
    df=df.drop(start+index)

df.to_csv('../data/geo_coded_feature_extracted_all_1500.csv', header=False, sep=',', index=False)
    