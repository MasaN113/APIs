import httplib2
import json

def geoNominatim(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    #google_api_key = "PASTE_YOUR_KEY_HERE"
    locationString = inputString.replace(" ", "+")
    url = ('https://nominatim.openstreetmap.org/search?q=%s&format=geojson'%(locationString))
    h = httplib2.Http()
    #result=json.loads(content.decode("utf-8")) #dodan decode, ker mi je sicer vracal byte
    result = json.loads(h.request(url,'GET')[1].decode("utf-8"))
    [lng, lat]=result['features'][0]['geometry']['coordinates']
    #latitude = result['features'][0]['geometry']['location']['lat']
    #longitude = result['results'][0]['geometry']['location']['lng']
    return lat,lng
