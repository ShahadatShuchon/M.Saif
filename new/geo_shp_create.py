
import pandas as pd
import geopandas as gpd
from shapely.geometry import point

df=pd.read_excel(r"C:\Users\Shahadat Shuchon\Documents\new\gps_agegate_final.xlsx")
print(df.columns)

#df['coordinates'] = df.apply(lambda x: point(((x.Longitude), (x.Latitude))), axis=1)

gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
#print(df.Latitude.dtype)
#print(gdf.geometry)

gdf['Date'] = pd.to_datetime(gdf['Date'], format='%Y')

schema = gpd.io.file.infer_schema(gdf)
print(schema)
schema['properties']['year'] = 'datetime'

#schema = {
    #'geometry': 'Point',
    #'properties': {
       # 'npri_id': 'int',
        #'facility': 'str',
        #'year': 'datetime',
#}}
gdf.crs= "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"

gdf.to_file(r'C:\Users\Shahadat Shuchon\Documents\new\MyGeometries.shp', schema=schema)






