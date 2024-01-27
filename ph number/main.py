import phonenumbers
from test import number
from phonenumbers import geocoder
import folium
key="fd31b0d9b54d44638889c108f0ea1be8"
print(input("enter your number:"))
ch_number=phonenumbers.parse(number,"CH")
number_location=geocoder.description_for_number(ch_number,"en")
print(number_location)
from phonenumbers import carrier
service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))
from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(key)
query=str(number_location)
result=geocoder.geocode(query)
lat=result[0]["geometry"]["lat"]
lng=result[0]["geometry"]["lng"]
print(lat,lng)
map_location=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(map_location)
map_location.save("mylocation.html")