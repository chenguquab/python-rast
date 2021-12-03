import folium
import pandas as pd

waterfalls = pd.read_csv("waterfalls.txt")
# print(waterfalls)
lat = list(waterfalls["Latitude"])
lon = list(waterfalls["Longitude"])
name = list(waterfalls["Name"])
height = list(waterfalls["Height"])
state = list(waterfalls["State"])

map = folium.Map(location=[32,53], zoom_start=5)

fg = folium.FeatureGroup("Waterfalls")

"""
for lt,ln,nm,hg,st in zip(lat, lon, name, height, state):
    popup_text = f"{nm} waterfall is located in the {st} state and it has about {hg} meters of height"
    fg.add_child(folium.Marker(location=[lt,ln], popup=popup_text))
"""

for lt,ln,nm,hg,st in zip(lat, lon, name, height, state):
    html = """
    <h1>Name: %s<h1/>
    <h4>Height: %s meters<h4/>
    <h4>State: %s<h4/>
    <a href="https://google.com/search?q=%s waterfall">Read More</a>
    """ % (nm,hg,st,nm)
    iframe = folium.IFrame(html=html , width=300, height=200)
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe)))



map.add_child(fg)

map.save("q2.html")