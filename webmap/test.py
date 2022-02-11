import folium
import pandas as pd

volcanos = pd.read_csv("../files/Volcanoes.txt", sep=",")
lat = list(volcanos['LAT'])
lon = list(volcanos['LON'])
myMap = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
for lt, ln in zip(lat, lon):
    folium.Marker(location=[lt,ln], popup="Hi this is a marker", icon=folium.Icon(color='red')).add_to(myMap)

myMap.save("Map1.html")