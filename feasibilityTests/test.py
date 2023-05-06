import geoCoding
import NER
import distance

data = ["1 mile S. of Okari River, between Charleston and Westport, Westland",-41.845,171.556]
location = NER.find_last_name(data[0])
print(location)
coordinates = geoCoding.getGeoCoding(location)
print(coordinates)
distance = distance.distance(float(coordinates[0]), float(coordinates[1]), float(data[1]), float(data[2]))
print(distance)
