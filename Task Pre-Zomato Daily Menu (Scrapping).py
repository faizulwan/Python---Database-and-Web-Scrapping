import requests



key = "953a7c1382d94a98c504ebe56665b0d2"

kota = str(input("Please input a city name :")).lower()
resto = str(input("Please input a restaurant name :")).lower()
jumlah = int(input("How many results do you want to show? "))

urlkota = f'https://developers.zomato.com/api/v2.1/cities?q={kota}&count=1'
webkota = requests.get(urlkota, headers = {'user-key': key})
output_kota = webkota.json()

# print (output)
cityid = output_kota['location_suggestions'][0]['id']



urlsearch = f'https://developers.zomato.com/api/v2.1/search?entity_id={cityid}&entity_type=city&q={resto}'
websearch = requests.get(urlsearch, headers = {'user-key': key})
output_search = websearch.json()

res_id = output_search['restaurants'][0]['restaurant']['id']



urlmenu = f'https://developers.zomato.com/api/v2.1/dailymenu?res_id=1'
webmenu = requests.get(urlmenu, headers = {'user-key': key})
output_menu = webmenu.json()
# jumlah_menu = len(output_menu['daily_menus'][0]['daily_menu']['dishes'])
# print (jumlah_menu)
print (output_menu['message'])
print (output_menu)

if output_menu['message']=='No Daily Menu Available':
    print ('No Daily Menu Available')