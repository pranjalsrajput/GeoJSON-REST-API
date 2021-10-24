from django_initialization import start_django

start_django()
import json
# Opening JSON file
from api.models.features import GeoFeature
import geopandas as gpd
file = open('/home/luo/Documents/Python Projects/Kaios/GeoJSON/geo_json_rest_api/api/data/municipalities_nl.geojson',)
geoFeature = json.load(file)
for feature in geoFeature['features']:
    GeoFeature.objects.update_or_create(features=feature)
# print(geoFeature)



# # We import the geoJSON file.
# url = ("/home/luo/Documents/Python Projects/Kaios/GeoJSON/geo_json_rest_api/api/data")
# state_geo = f"{url}/municipalities_nl.geojson"
#
# # We read the file and print it.
# geoJSON_df = gpd.read_file(state_geo)
# geoJSON_df.head()