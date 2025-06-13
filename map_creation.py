import LibRoad2Cary as R2C

# Specify the date for which you want to have the map
date = '06_12_25'

# Create the map
R2C_map = R2C.Road2CaryMap(date)

# Save the figure
R2C_map.write_html()
