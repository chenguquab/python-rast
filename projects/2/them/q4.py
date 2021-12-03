import folium
import pandas as pd

waterfalls = pd.read_csv("waterfalls.txt")
# print(waterfalls)
lat = list(waterfalls["Latitude"])
lon = list(waterfalls["Longitude"])
height = list(waterfalls["Height"])

map = folium.Map(location=[32,53], zoom_start=5)

fg = folium.FeatureGroup("Waterfalls")

def color_producer(height):
    if height <= 20:
        color = "green"
    elif height <= 50:
        color = "orange"
    else:
        color = "red"
    return color

for lt,ln,hg in zip(lat, lon, height):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, fill_color=color_producer(hg), color="gray"))

map.add_child(fg)

map.save("q4.html")