import pandas as pd

import geopandas as gpd
from shapely.geometry import Point

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Latitude': [40.7128, 34.0522, 41.8781],
    'Longitude': [-74.0060, -118.2437, -87.6298]
})
gdf['geometry'] = gdf.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)

print(gdf)