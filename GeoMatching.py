#Matching adresses with coordinates
import geopy
from geopy.geocoders import Nominatim #для парсинга геокоординат по адресу и наоборот
geopy.geocoders.options.default_timeout = 60

'''
geolocator = Nominatim()
for i in range(300):
#for i in range(len(ptz_final)):
    if i == 0:
        location = geolocator.geocode(ptz_final.loc[i, 'address'])
        if location != None:
            ptz_final.loc[i, 'longitude'] = location.longitude
            ptz_final.loc[i, 'latitude'] = location.latitude
    else:
        if ptz_final.loc[i, 'address'] == ptz_final.loc[i-1, 'address']:
            ptz_final.loc[i, 'longitude'] = ptz_final.loc[i-1, 'longitude']
            ptz_final.loc[i, 'latitude'] = ptz_final.loc[i-1, 'latitude']
        else:
            location = geolocator.geocode(ptz_final.loc[i, 'address'])
            if location != None:
                ptz_final.loc[i, 'longitude'] = location.longitude
                ptz_final.loc[i, 'latitude'] = location.latitude
    if i % 100 == 0:
            print(i) #counter
'''
geolocator = Nominatim()
#for i in range(300):
for i in range(len(ptz_final)):
    if i == 0:
        location = geolocator.geocode(ptz_final.loc[i, 'address'])
        ptz_final.loc[i, 'longitude'] = location.longitude
        ptz_final.loc[i, 'latitude'] = location.latitude
    else:
        if ptz_final.loc[i, 'address'] == ptz_final.loc[i-1, 'address']:
            ptz_final.loc[i, 'longitude'] = ptz_final.loc[i-1, 'longitude']
            ptz_final.loc[i, 'latitude'] = ptz_final.loc[i-1, 'latitude']
        else:
            location = geolocator.geocode(ptz_final.loc[i, 'address'])
            if location != None:
                ptz_final.loc[i, 'longitude'] = location.longitude
                ptz_final.loc[i, 'latitude'] = location.latitude
            else:
                ptz_final.loc[i, 'longitude'] = "G-rypga"
                ptz_final.loc[i, 'latitude'] = "Джигурдинская"
    if i % 100 == 0:
            print(i)
