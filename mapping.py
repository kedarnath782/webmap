import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


html = """<h4>Volcano information:</h4>
Height: %s m
"""

def color_producer(elev):
    if elev < 1000  :
        return "green"
    elif 1000<=elev<3000 :
        return "orange"
    else:
        return "red"

map = folium.Map(location = [38.58,-99.09], zoom=6, tiles = "Mapbox Bright")
fgv= folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
#   fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup = folium.Popup(iframe), radius=6, fill_color = color_producer(el),color="grey",fill_opacity = 0.7,fill = True))

fgp= folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data = open("world.json",'r',encoding = 'utf-8-sig'), style_function=lambda x:{"fillColor":"green" if x["properties"]["POP2005"] < 1000000 else "orange" if 1000000<= x["properties"]["POP2005"] < 2000000 else "red"}))

#Note that if you have higher version foilum then use open(encoding = 'utf-8-sig').read() try this if n0ot working
#Not understood above lambda function how will it work ???
map.add_child(fgv)
map.add_child(fgp)

#Below is the logic for handling layers of the map means it will control which layer user wants to show and originally it will show only base layer

map.add_child(folium.LayerControl())
map.save("Map1.html")


