import folium

map = folium.Map(location=[32,53], zoom_start=5)

fg_b = folium.FeatureGroup(name="Countries Borders")

world_data = open("world.json", encoding="utf-8-sig").read()
# Path("world.json", encoding="utf-8-sig").read_text()

folium.GeoJson(data=world_data).add_to(fg_b)

map.add_child(fg_b)
map.save("q5.html")