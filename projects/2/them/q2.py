import folium
import pandas as pd

waterfalls = pd.read_csv("waterfalls.txt")
# print(waterfalls)
lat = list(waterfalls["Latitude"])
lon = list(waterfalls["Longitude"])

map = folium.Map(location=[32,53], zoom_start=5)

fg = folium.FeatureGroup("Waterfalls")

for lt,ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt,ln]))

map.add_child(fg)

map.save("q2.html")