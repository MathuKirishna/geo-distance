from geopy.geocoders import Nominatim

def getGeoCoding(location:str):
    ZELAND = "Zealand"
    name_place=""
    if location.lower() in ZELAND.lower():
        name_place = location
    else:
        name_place= location + ", New Zealand"

    # Initialize the Nominatim geocoder
    geolocator = Nominatim(user_agent="test-application")

    # Geocode the place
    geoCode = geolocator.geocode(name_place)
    return [geoCode.latitude, geoCode.longitude]
