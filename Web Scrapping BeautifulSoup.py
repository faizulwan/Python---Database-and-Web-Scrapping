### Data Collection - Acquisition
'''
Database ====> Front Page ==> Coding Python ==> Statis ==> Web Scrapping


==> Data Dinamis
Database ===== API =====> Front Page
                ||
          Coding Python

### API
API ==> Application Programming Interface
Aplikasi A === API === Aplikasi B
                       Aplikasi D
                       Aplikasi C


### Rest API
Rest API ==> Representation State Transfer API

Database ==== REST API ==== Front Page => Via Web Scrapping
               ||
               Coding Python ==> Via REST API

- Data Dinamis => Contoh Cuaca, Mata uang (Konversi)
- Terkoneksi dengan internet
- API itu dibuat oleh developer
- Hanya dapat digunakan untuk web-webb tertentu yang memang memiliki API
- Format API berbeda untuk masing=masing web, tergantung developernya
- Limited access => Terbatas tergantung developer
- Format data umumnya berbentuk JSON

Request ==> Get
Response ==> Respon dari Server


## Langkah Collect Data via API
- Pastikan data yang dibutuhkan
- Tentukan web yang menyediakan data tersebut
- Pastikan WEB memiliki API
- Pastikan Data dapat disediakan melalui API
- Ketahui Format akses API
- Coding


Package ==> Requests

'''

'''
from bs4 import BeautifulSoup
import requests
import json


url = "https://jsonplaceholder.typicode.com/users"

web = requests.get(url)

out = web.json()

# print (out[2])

for i in range (10):
    print (f"Name - {out[i]['name']}; Email - {out[i]['email']}; City - {out[i]['address']['city']}")

'''


# ==================================================================================================================================================

#!/usr/bin/env python3
# importing the requests library
# API ENDPOINT

# UNWXLXmQM8Uxo3heTycJit8PIApGQy0LBlGSZ5ry
# https://kurs.web.id/

# import requests


# url = "https://api.kurs.web.id/api/v1?token=UNWXLXmQM8Uxo3heTycJit8PIApGQy0LBlGSZ5ry&bank=bca&matauang=usd"
# web = requests.get(url)
# output = web.json()

# print (output)

'''

# ====================================================================================================================================

# api.openweathermap.org/data/2.5/weather?q=London&appid={API Key}

import requests

key =  '188e6e77eb0608e60b4fea0f7d6b2eb7'
host = "api.openweathermap.org"
kota = input("Masukkan nama kota : ").lower()

url = f"https://{host}/data/2.5/weather?q={kota}&appid={key}"
data = requests.get(url)
cuaca = data.json()

print (cuaca)
'''



####################################### Zomato

# https://developers.zomato.com/documentation

import requests

key = "953a7c1382d94a98c504ebe56665b0d2"
cat = "/categories"
city = "/cities"
host = "https://developers.zomato.com/api/v2.1"
head = {"user-key" : key}


url = host + cat
url2 = host + city

data = requests.get(url, headers = head)
data2 = requests.get(url2, headers = {"user - key" : "953a7c1382d94a98c504ebe56665b0d2"})

output = data.json()
print (output['categories'])

isi = len(output['categories'])
kategori = output['categories']

List_Cat = []

for i in range (isi):
    List_Cat.append(kategori[i]['categories']['name'])

print (List_Cat)


############################# Latihan - Tugas
# Gunakan API dari Zomato
