from geopy.distance import geodesic
from geopy import Point
import base64
import datetime

from LibRoad2Cary.utility import constants

# ==================================================================================================
#
#   ...
#
# ==================================================================================================

CUMULATIVE_DISTANCES = [0]
for i in range(len(constants.ROUTE) - 1):
    dist = geodesic(constants.ROUTE[i][1], constants.ROUTE[i+1][1]).km
    CUMULATIVE_DISTANCES.append(CUMULATIVE_DISTANCES[-1] + dist)

# --- Interpolation ---
def initial_bearing(start, end):
    import math
    lat1 = math.radians(start.latitude)
    lat2 = math.radians(end.latitude)
    delta_lon = math.radians(end.longitude - start.longitude)

    x = math.sin(delta_lon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    bearing = math.atan2(x, y)
    bearing_deg = (math.degrees(bearing) + 360) % 360
    return bearing_deg

def interpolate_position(dist_km):
    for i in range(len(CUMULATIVE_DISTANCES) - 1):
        d_start = CUMULATIVE_DISTANCES[i]
        d_end = CUMULATIVE_DISTANCES[i + 1]
        if d_start <= dist_km <= d_end:
            frac = (dist_km - d_start) / (d_end - d_start)
            start = Point(constants.ROUTE[i][1])
            end = Point(constants.ROUTE[i + 1][1])
            bearing = initial_bearing(start, end)
            segment_length_km = geodesic(start, end).km
            distance_along_segment = frac * segment_length_km
            point = geodesic(kilometers=distance_along_segment).destination(start, bearing)
            return point.latitude, point.longitude
    return constants.ROUTE[-1][1]

# ==================================================================================================
#
#   ...
#
# ==================================================================================================

# Read and encode image
with open(constants.ROAD2CARY_LOGO_PATH, "rb") as f:
    encoded_image = base64.b64encode(f.read()).decode()

# Create the data URI
IMAGE_URI = "data:image/png;base64," + encoded_image

# Get current time as a string
CURRENT_DATETIME = datetime.datetime.now().strftime("Last updated: %Y-%m-%d %H:%M:%S")