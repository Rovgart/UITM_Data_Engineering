from folium import Icon, Map, Marker, FeatureGroup
from pandas import read_csv

map= Map(location=[-6.64157,46.01030],zoom_start=17, tiles="CartoDB Positron")
fg= FeatureGroup(name="My map")
dane=read_csv("Volcanoes.txt")
lat=list(dane["LAT"])
ln=list(dane["LON"])
print(dane);
for lt, ln in zip(lat, ln):
    fg.add_child(Marker(location=[lat,ln], popup="This is a marker", icon=Icon(color="green")))
    
map.add_child(fg)
map.save("Map3BC.html")
