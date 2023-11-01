import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium
import matplotlib.pyplot as plt
xy_table = pd.read_excel(r'C:\Users\Shahadat Shuchon\Documents\new\gps_agegate_final.xlsx')
print(xy_table.columns)
xy_table.drop('Date',axis=1,inplace= True)
xy_table['coordinates'] = xy_table[['Longitude', 'Latitude']].values.tolist()
xy_table['coordinates'] = xy_table['coordinates'].apply(Point)
stations = gpd.GeoDataFrame(xy_table, geometry = 'coordinates')
stations = stations.set_crs('epsg:4326')
stations_epsg3978 = stations.to_crs('EPSG:3978')
stations_epsg3978.to_file(filename='myshapefile.shp', driver='ESRI Shapefile')