# Imports pandas library and gives it an alias 'pd'

import pandas as pd
 
# Imports geopandas library and gives it an alias 'gpd'                 

import geopandas as gpd

# Imports Point class from the shapely.geometry module

from shapely.geometry import Point

# Imports pyplot module from the matplotlib library and gives it an alias 'plt'

import matplotlib.pyplot as plt 

# SECTION ON FILE READING
# The line of code uses the pandas library (pd) to read the CSV file and create a DataFrame 'df'
# It also assigns 'df' to the result of reading the csv file ('GrowLocations.csv')

df = pd.read_csv('GrowLocations.csv')

# SECTION ON DATA CLEANING (FILTERING INVALID LATITUDE AND LONGITUDES AND DUPLICATES REMOVAL)
# The code line below filters the DataFrame 'df' based on acceptable latitude and longitude range of values

df = df[(df['Latitude'] >= -90) & (df['Latitude'] <= 90)
        & (df['Longitude'] >= -180) & (df['Longitude'] <= 180)]

# The code line below removes duplicate latitude and longitude values

growdata = df.drop_duplicates(subset=['Latitude', 'Longitude'])

# This filters the DataFrame 'growdata' and makes it include rows where latitude and longitude values fall within the specified boundaries.

growdata = growdata[(growdata['Latitude'] >= -10.592) & (growdata['Latitude'] <= 1.6848) &
                    (growdata['Longitude'] >= 50.681) & (growdata['Longitude'] <= 57.985)]

# This code line creates a GeoDataFrame 'gdf' from the 'growdata' DataFrame. 
# The 'geometry' variable is assumed as a list of Shapely Point objects. 
# 'crs='EPSG:4326'' sets the coordinate reference system (CRS) of the GeoDataFrame. 
# 'EPSG:4326' is widely used for latitude and longitude coordinates geographic data.

growdata_geometry = [Point(xy) for xy in zip(growdata['Latitude'], growdata['Longitude'])] 

gdf = gpd.GeoDataFrame(growdata, geometry=growdata_geometry, crs='EPSG:4326')

# The code line below reads and subsequently loads the map image 

map_image = plt.imread('map7.png')

# The line of code uses Matplotlib to create a subplot

fig, ax = plt.subplots(figsize=(15, 10))

# The code line uses Matplotlib's imshow function to display the map_image on the 'ax' subplot
# within the specified spatial boundaries on the subplot. 

ax.imshow(map_image, extent=[-10.592, 1.6848, 50.681, 57.985])

# This code line creates a scatter plot on subplot ('ax') using red circular markers ('o') with a size of 8.5 points.

gdf.plot(ax=ax, marker='o', color='red', markersize=8.5, label='GROW sensor locations')

# The code lines below give the plot a title and the axes their labels

plt.title('Locations Plot of the sensors on the provided UK map')
plt.xlabel('Latitude')  
plt.ylabel('Longitude')

# The code line below adds a legend to the plot

plt.legend()
plt.show()
