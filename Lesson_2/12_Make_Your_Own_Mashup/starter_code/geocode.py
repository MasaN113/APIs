import httplib2
import json

def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    #google_api_key = "PASTE_YOUR_KEY_HERE"
    locationString = inputString.replace(" ", "+")
    url = ('https://nominatim.openstreetmap.org/search?q=%s&format=geojson'%(locationString))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result=json.loads(content)
    #result = json.loads(h.request(url,'GET')[1])
    #latitude = result['results'][0]['geometry']['location']['lat']
    #longitude = result['results'][0]['geometry']['location']['lng']
    return (result)
