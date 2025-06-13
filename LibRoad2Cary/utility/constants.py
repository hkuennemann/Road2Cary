'''
constants.py
------------

This module defines constants for file paths, formats, and values used throughout the project.

Paths:
    -

Formats:
    -

Values:
    -
'''

import pandas as pd
from io import StringIO

# ==================================================================================================
#
#   COLORS
#
# ==================================================================================================

TEAM_MARKER_COLOR = "Blue"  # TODO: SAS Blue / SAS Gray
COUNTRY_COLOR='#D9D9D9'
LAND_COLOR='#F2F2F2'
OCEAN_COLOR="#C4DEFD"
COATLINE_COLOR="darkgray"

# ==================================================================================================
#
#   PATHS
#
# ==================================================================================================

# Include Road2Cary Logo and last updated text
ROAD2CARY_LOGO_PATH = "C:\Users\hekunn\OneDrive - SAS\Documents\Road2Cary\Road2Cary\R2C_Logo.png"

# ==================================================================================================
#
#   Values
#
# ==================================================================================================

# Office locations with coordinates (latitude, longitude)
ROUTE = [
    ("Marlow", (51.5719, -0.7760)),
    ("Copenhagen", (55.6761, 12.5683)),
    ("Helsinki", (60.1695, 24.9354)),
    ("Stockholm", (59.3293, 18.0686)),
    ("Oslo", (59.9139, 10.7522)),
    ("Glasgow", (55.8642, -4.2518)),
    ("Dublin", (53.3498, -6.2603)),
    ("Cary", (35.7915, -78.7811))
]

# Directional offsets for city labels
CITY_LABEL_OFFSETS = {
    "Marlow": (2.5, -3.5),
    "Copenhagen": (0, -3.5),
    "Helsinki": (0, 5),
    "Stockholm": (0, 4),
    "Oslo": (-0.5, 2),
    "Glasgow": (0, 3),
    "Dublin": (-2, -3),
    "Cary": (-1.5, 3),
}

# Factor to shorten leader lines
LEADER_LINE_SHORTENING_FACTOR = 0.7

# Image positioning
IMAGE_POSITION_X = 0.905
IMAGE_POSITION_Y = 0.125

# DateTime text positioning
DATETIME_POSITION_X = 0.25
DATETIME_POSITION_Y = 0.05

# Map configurations
MAP_CONFIGS = {"scrollZoom": False,
               "doubleClick": False,
               "displayModeBar": False
               }
