from mountain_database import *
import folium

#Creates map of the country
map = folium.Map(
        location=[41.1529058, 20.1605717],
        zoom_start=10,
        tiles='Stamen Terrain'
)

#Fetches data from database
cur.execute("SELECT * FROM Albanian_mountains")
db=cur.fetchall()

#Imports data from database into map markers that will be displayed on a map
for name, latitude, longitude in db:
    folium.Marker([latitude, longitude], popup=name, icon=folium.Icon(color='red')).add_to(map)


#Launches map
print(map.save('albania.html'))
