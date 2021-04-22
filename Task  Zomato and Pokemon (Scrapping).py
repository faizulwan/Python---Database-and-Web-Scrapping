############################# Latihan - Tugas 1
'''
Gunakan API dari Zomato


Selamat datang di Zomato Apps:
Silahkan pilih opsi :
1. Cari resto
2. Daily Menu

Opsi 1 :
Mencari Restoran di kota tertentu
Input:
- Masukkan Nama Kota : (error handling)
- Masukkan Jumlah Restoran yang akan ditampilkan : contoh berapa jumlah restoran 1/5/10/all


Outputnya :
- Nama Restoran : .....
- Establishment Name : .....
- Cuisine Name : .....
- Alamat : .....
- No. Telfon : ....
- Rating : ...(angka)...
- Review : ...(angka)...
# 1x run bisa banyak url yang kita get, coba2 get yang sesuai

Opsi 2 :
Daily Menu - Menu Harian Restor
Input :
- Masukkan nama Kota : (error handling)
- Masukkan nama Resto : 
- Jumlah menu yang akan ditampilkan :

Outputnya :
Daily Menu di restoran xxxx adalah ....{Sesuai dengan jumlah menu yang ingin ditampilkan}
'''
# ==================================================================================================
import requests

# key = "953a7c1382d94a98c504ebe56665b0d2"
# cat = "/categories"
# city = "/cities"
# host = "https://developers.zomato.com/api/v2.1"
# head = {"user-key" : key}

# url = host + cat
# url2 = host + city

# data = requests.get(url, headers = head)
# data2 = requests.get(url2, headers = {"user-key" : "953a7c1382d94a98c504ebe56665b0d2"})

# output = data.json()
# print (output['categories'])


key = "953a7c1382d94a98c504ebe56665b0d2"

while True:
    
    print ("======>Welocome to Zomato Apps<======")
    print ('''What are you gonna do today ?
1. Find a Restaurant
2. Daily Menu
3. Exit''')
    menu = input("Choose your apps (1/2/3) :")

    if menu == '1':
        print ("====FIND A RESTAURANT====")

        while True:
            try:
                kota = str(input("Please input a city name :")).lower()  # Meminta nama kota
                jumlah = int(input("How many restaurants do you want to show : ")) # Meminta jumlah restoran yang akan dikeluarkan

            ### Find City
                urlkota = f'https://developers.zomato.com/api/v2.1/cities?q={kota}&count=1'  # API Cities
                webkota = requests.get(urlkota, headers = {'user-key': key})
                output_kota = webkota.json()
                # print (output)
                cityid = output_kota['location_suggestions'][0]['id'] # Get entity_id of city
                # print (cityid)



            ### Find Restaurant
                urlresto = f'https://developers.zomato.com/api/v2.1/search?entity_id={cityid}&entity_type=city&count={jumlah}'  #API Search
                webresto = requests.get(urlresto, headers = {'user-key': key})
                output_resto = webresto.json()
                jumlah_resto = len(output_resto['restaurants'])

                if jumlah <1:
                    print ('Invalid show number')

                else:    
                    for i in range(jumlah_resto):
                        print ('=' * 30)
                        print (f'Nama          :{output_resto["restaurants"][i]["restaurant"]["name"]}')                                # Name
                        print (f'Establishment :{output_resto["restaurants"][i]["restaurant"]["establishment"][0]}')                    # Establishment
                        print (f'Cuisine       :{output_resto["restaurants"][i]["restaurant"]["cuisines"]}')                            # Cuisine
                        print (f'Address       :{output_resto["restaurants"][i]["restaurant"]["location"]["address"]}')                 # Address
                        print (f'Phone         :{output_resto["restaurants"][i]["restaurant"]["phone_numbers"]}')                       # Phone
                        print (f'Rating        :{output_resto["restaurants"][i]["restaurant"]["user_rating"]["aggregate_rating"]}/5.0') # Rating
                        print (f'Total Review  :{output_resto["restaurants"][i]["restaurant"]["all_reviews_count"]}')                   # Total review
                        print ('=' * 30)
                        print ('')

                    break
                                    
            except:
                print("\nInvalid city name or show number\n")

        break


    elif menu == '2':
        print ("====DAILY MENU====")

        while True:
            try:
                kota = str(input("Please input a city name :")).lower()  # Meminta nama kota
                restaurant = str(input("Input a restaurant name : "))    # Meminta nama restoran yang akan dikeluarkan
                jumlah = int(input('How many menu do you want to show : ')) #Meminta banyaknya menu yang akan ditampilkan

            ### Find City
                urlkota = f'https://developers.zomato.com/api/v2.1/cities?q={kota}'  # API Cities
                webkota = requests.get(urlkota, headers = {'user-key': key})
                output_kota = webkota.json()
                # print (output)
                cityid = output_kota['location_suggestions'][0]['id'] # Get entity_id of city
                # print (cityid)

            ### Find a Restaurant
                urlsearch = f'https://developers.zomato.com/api/v2.1/search?entity_id={cityid}&entity_type=city&q={restaurant}' #API Search
                websearch = requests.get(urlsearch, headers = {'user-key': key})
                output_search = websearch.json()

                res_id = output_search['restaurants'][0]['restaurant']['id']  # Get Res_id of restaurant
                # print (res_id)

            ### Find Daily Menu
                urlmenu = f'https://developers.zomato.com/api/v2.1/dailymenu?res_id={res_id}&count={jumlah}'
                webmenu = requests.get(urlmenu, headers = {'user-key': key})
                output_menu = webmenu.json()
                # print (output_menu)
                no_menu = output_menu['message']
                # print (no_menu)
                jumlah_menu = len(output_menu['daily_menus'][0]['daily_menu']['dishes'])                
                

                if jumlah < 1:
                    print ('Invalid show number')

                else:
                    if output_menu['status'] == 'success':
                        for i in range(jumlah):
                            print(f"Menu {i+1}")
                            print(f"Dish name: {output_menu['daily_menus'][0]['daily_menu']['dishes'][i]['dish']['name']}")

                        break

                    else:
                        print ("No Daily Menu Available")

                        break

                


            except:
                print("\nInvalid city name or restaurant name\n")

        break


    elif menu == '3':
        print("====EXIT====")
        break

    
    else:
        print ("\nApp is not avalaible\n")










'''
############################# Latihan - Tugas 2
Pokemon
pokeapi.co

Pokemon Database :

inputnya :
- Masukkan nama pokemon : (error handling)

outputnya :
- Nama Pokemon : ....
- HP : ....
- Attack : ....
- Deffense : ...
- Speed : ....
- Type : ....
- Image : url image foto pokemon
- Ability Name : ....
1.
2.
3.
'''

# ==================================================================================================
# import requests

# while True:
#     try:
#         pokemon = str(input("Input Pokemon name : ")).lower()
#         url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
#         web = requests.get(url)
#         output = web.json()

#         if pokemon.isdigit() == True:
#             print ('Number is not allowed')

#         else:
#             name = (output['name']).title()            # Nama
#             attack = output['stats'][1]['base_stat']   # Attack
#             defense = output['stats'][2]['base_stat']  # Defense
#             speed = output['stats'][5]['base_stat']    # Speed
#             image = output['sprites']['back_default']   # Image

#             tipe = output['types']
#             types= []
#             for i in range (len (output['types'])):
#                 types.append(tipe[i]['type']['name'])
#             # print (types)
#             types1 = ('-').join(types)
#             tipe_tipe =  types1                         # Type

#             abilities = output['abilities']
#             ability= []
#             for i in range (len (output['abilities'])):
#                 ability.append(abilities[i]['ability']['name'])
#             # print (ability)
#             ability1 = ('-').join(ability)
#             abilities_abilities = ability1               # Abilities

#             print(f'''===> POKEMON DATABASE <===
# Name        : {name}
# Attack      : {attack}
# Defense     : {defense}
# Speed       : {speed}
# Types       : {tipe_tipe}
# Image       : {image}
# Abilities   : {abilities_abilities}''')
#             break

#     except:
#         print ('''====Ivalid Pokemon name====
# Please input a valid pokemon name!''')
# ===================================================================================================