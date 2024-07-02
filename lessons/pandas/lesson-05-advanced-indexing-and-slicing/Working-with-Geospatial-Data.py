import pandas as pd

import geopandas as gpd

# Load a sample dataset
gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot the data
gdf.plot()
plt.show()

