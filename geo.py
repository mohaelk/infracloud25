#VERY SHORT EXAMPLE SCRIPT
#pip install datetime
#pip install geopy
#pip install folium
from geopy.geocoders import Nominatim
import folium
geolocator = Nominatim(user_agent="http://biasc.be")
city_country = "Charles Malisstraat Sint-Jans Molenbeek, Belgium"
location = geolocator.geocode(city_country)
devnet_lat = location.latitude
devnet_lon = location.longitude
devnet_alt = location.altitude
#print"Altitude: ",devnet_alt)
coordinates = [devnet_lat,devnet_alt]
coordinates = [devnet_lat,devnet_lon]
map = folium.Map(location=coordinates, tiles='OpenStreetMap', zoom_start=16)
map
map.save("geopy_location.html")