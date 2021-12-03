import folium
import pandas as pd

map = folium.Map(location=[32,53], zoom_start=5)
waterfalls = pd.read_csv("waterfalls.txt")
lat = list(waterfalls["Latitude"])
lon = list(waterfalls["Longitude"])

# Waterfalls
fg_w = folium.FeatureGroup("Waterfalls")
for lt,ln in zip(lat, lon):
    fg_w.add_child(folium.Marker(location=[lt,ln]))

# Countries Borders
fg_b = folium.FeatureGroup(name="Countries Borders")
world_data = open("world.json", encoding="utf-8-sig").read()
folium.GeoJson(data=world_data).add_to(fg_b)

map.add_child(fg_b)
map.add_child(fg_w)

# Add Layer Control To Map
map.add_child(folium.LayerControl())
map.save("q6.html")