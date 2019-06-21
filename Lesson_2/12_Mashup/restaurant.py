from nominatim import geoNominatim
import json
import httplib2

import sys
import codecs
""" sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)
 """
fsq_client_id = "UWI1ZIJEHRUKOSQCFNU3UEOZ03LMF0UNP25Q4Y3QXDIOX25K"
fsq_client_secret = "UZMNMYHGDWQRKQDJUUXI2HK0TXMHXME2HSE4RXGTQN1D4DQP"


def findARestaurant(mealType, location):
	lat,lng = geoNominatim(location)
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s'%(fsq_client_id, fsq_client_secret, lat, lng, mealType))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1].decode("utf-8"))
	
	if result['response']['venues']: #moramo pokriti verjetnost, da ne najde ničesar
		first = result['response']['venues'][0] #prva restavracija
		first_id = first['id'] #id prve restavracije, potrebujemo potem za sliko
		first_name = first['name'] #ime prve
		first_address = first['location']['formattedAddress'] #naslov prve - napisan v delih, ločenih z vejico, zato:
		address = "" #prazen string
		for i in first_address: #dele naslova bodo dzružili skupaj, ločeno le s presledkom
			address += i + " "
		first_address = address #naslov prve rest. nastavimo na preoblikovani naslov
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
		pic_url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % (first_id,fsq_client_id,fsq_client_secret))
		#v dokumentaciji Foursquara, kako se dobijo slike
		pic_result = json.loads(h.request(pic_url, 'GET')[1].decode("utf-8"))
		if pic_result['response']['photos']['items']: #najprej preverimo, ce sploh je kaksna slika
	#5. Grab the first image
			first_pic = pic_result['response']['photos']['items'][0]
			prefix = first_pic['prefix']
			suffix = first_pic['suffix']
			image_URL = prefix + "300x300" + suffix #sestaviš image url
		else:
	#6. If no image is available, insert default a image url
			image_URL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"
		#to sem skopirala iz solutiona
	#7. Return a dictionary containing the restaurant name, address, and image url	
		restaurant_dict = {'name': first_name, 'address': first_address, 'image URL': image_URL}
		print("Restaurant Name: %s" % restaurant_dict['name'])
		print ("Restaurant address: %s" % restaurant_dict['address'])
		print ("Image: %s" % restaurant_dict['image URL'])
		return restaurant_dict
	else:
		print ("No Restaurants Found for %s" % location)
		return "No Restaurants Found"

if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney, Australia")
