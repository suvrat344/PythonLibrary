# pip install geopy
# pip install geocoders

# We would use Nominatim API to scrap geocoding information of any open ended address text using Python.
from geopy.geocoders import Nominatim 

# Activate Nominatim Geocoder
locator = Nominatim(user_agent="suvratchauhan123@gmail.com")


# Type Any Address Code
location1 = locator.geocode("Champ de Mars, Paris, France")
location2 = locator.geocode("IIT Madras")

print("Location ID : ",location1.raw)
print("Point : ",location1.point)
print("Address : ",location1.address)
print("Altitude : ",location1.altitude)
print("Latitude : ",location1.latitude)
print("Longitude : ",location1.longitude)

print("*"*100)

print("Location ID : ",location2.raw)
print("Point : ",location2.point)
print("Address : ",location2.address)
print("Altitude : ",location2.altitude)
print("Latitude : ",location2.latitude)
print("Longitude : ",location2.longitude)