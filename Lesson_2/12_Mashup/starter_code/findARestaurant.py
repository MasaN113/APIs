from nominatim import geoNominatim
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

fsq_client_id = "UWI1ZIJEHRUKOSQCFNU3UEOZ03LMF0UNP25Q4Y3QXDIOX25K"
fsq_client_secret = "UZMNMYHGDWQRKQDJUUXI2HK0TXMHXME2HSE4RXGTQN1D4DQP"


def findARestaurant(mealType,location):
	(lat,lng) = geoNominatim(location)
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s'%(fsq_client_id, fsq_client_secret, lat, lng, mealType))
	#h = httplib2.Http()
	#result = json.loads(h.request(url,'GET')[1])
	return url
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like 

	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url	
#if __name__ == '__main__':
	#findARestaurant("Pizza", "Tokyo, Japan")
	#findARestaurant("Tacos", "Jakarta, Indonesia")
	#findARestaurant("Tapas", "Maputo, Mozambique")
	#findARestaurant("Falafel", "Cairo, Egypt")
	#findARestaurant("Spaghetti", "New Delhi, India")
	#findARestaurant("Cappuccino", "Geneva, Switzerland")
	#findARestaurant("Sushi", "Los Angeles, California")
	#findARestaurant("Steak", "La Paz, Bolivia")
	#findARestaurant("Gyros", "Sydney, Australia")
