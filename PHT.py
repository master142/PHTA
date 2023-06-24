import phonenumbers
from my-number import number
from phonenumbers import geocoder
from opencage.geocoder import openCageGeocode
from phonenumbers import carrier

key = "your api key"

NO = phonenumbers.parse(number)

YL = geocoder.description_for_number(NO, "en")
print(YL)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

geocoder = openCageGeocode(key)
query  = str(YL)

result = geocoder.geocode(query)
print(reslut)

lat = result[0]['geormetry']['lat']
lng = result[0]['geormetry']['lng']

print(lat,lng)

MM = folium,map(loacation=[lat,lng], zoom_start = 9)

folium.Marker([lat, lng], popup= YL).add_to(MM)

MM.save('PHL.html')
