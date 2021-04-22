import requests


#urlresto = "https://developers.zomato.com/api/v2.1/location_details?entity_id=74&entity_type=city"  ##URL yang akan dipakai
# entity_id = country_id

key = "953a7c1382d94a98c504ebe56665b0d2"

kota = str(input("Please input a city name :")).lower()
jumlah = int(input("How many results do you want to show? "))

urlkota = f'https://developers.zomato.com/api/v2.1/cities?q={kota}&count=1'
webkota = requests.get(urlkota, headers = {'user-key': key})
output = webkota.json()

# print (output)
cityid = output['location_suggestions'][0]['id']




urlresto = f'https://developers.zomato.com/api/v2.1/search?entity_id={cityid}&entity_type=city&count={jumlah}'  #API Locations
webresto = requests.get(urlresto, headers = {'user-key': key})
output_1 = webresto.json()

print (output_1['restaurants'][2]['restaurant']['name'])                # Name
print (output_1['restaurants'][2]['restaurant']['establishment'][0])    # Establishment
print (output_1['restaurants'][2]['restaurant']['cuisines'])            # Cuisine
print (output_1['restaurants'][2]['restaurant']['location']['address']) # Address
print (output_1['restaurants'][2]['restaurant']['phone_numbers'])       # Phone
print (output_1['restaurants'][2]['restaurant']['user_rating']['aggregate_rating']) #Rating
print (output_1['restaurants'][2]['restaurant']['all_reviews_count'])   # Total review



