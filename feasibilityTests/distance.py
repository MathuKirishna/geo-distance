import math

def distance(source_lat, source_lon, target_lat, target_lon):
    R = 6371  # Earth's radius in kilometers

    source_lat, source_lon, target_lat, target_lon = map(math.radians, [source_lat, source_lon, target_lat, target_lon])

    dlat = target_lat - source_lat
    dlon = target_lon - source_lon

    a = math.sin(dlat / 2) ** 2 + math.cos(source_lat) * math.cos(target_lat) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c

    return d