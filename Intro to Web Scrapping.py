'''
Data Collection - Data Acquisition

---Data Sources

1. Internal ==> Data dari perusahaan (Bisa dari departemen sendiri ataupun lintas departemen)
    - ERP => Entreprise Resourcecs Planning ==> Sistem terintegrasi
    - Database => Back End



2. External
    - Data dari supplier
    - atau sumber data lain yang legal
    - 

Web Public ==> Website yang di open untuk Publik
- Front End --> Halaman yang bisa kita lihat as user  
    Database --> Front End (Front Page) -- HTML Page ==> Scrapped

==> Web Scrapping <==
   -Teknik mengekstrasi Data dari website yang akan kita simpan di local disk kita
    dapat berupa : Spreadsheet, csv, database, JSON, dll.
   -Suatu teknik automatisasi pengambilan data dari internet yang tidak atau semi terstruktur menjadi testruktur (Tabel)
   -Digunakan untuk halaman yang datanya statis 


==> Langkah
    1. Tentukan dulu Data yang akan diambil
    2. Tentukan URL-nya (websitenya)
    3. Lihat struktur website - Inspect element
    4. Coding ==> Scrap data termasuk simpan ke lokal

'''

'''
# Package ==> Beautifulsoup
# Package ==> Requests

py -m pip install beautifulsoup4
py -m pip install requests
'''







### File HTML Offline
# Beautifulsoup

from bs4 import BeautifulSoup

url = "contoh.html"

out = BeautifulSoup(open(url, 'r'), "html.parser")
# r = read (CRUD)

# tag html
# <.>Data yang kita cari</.>

# print (out)
# print (out.prettify)
# print (out.title)
# print (out.title.text)
# print (out.h3.text)
# print (out.h2.text)
# print (out.p.text)
# print (out.b.text)
# print (out.i.text)
# print (out.sub.text)
# print (out.strong.text)
# print (out.sup.text)
# print (out.ul.text)
# print (out.li)
# print (out.li.text)
 
# nama = []
# for i in out.find_all('li'):
#     nama.append(i.text)

# print (nama)

# tamu = []
# for i in out.find_all('li', class_= "Orang"):
#     tamu.append(i.text)

# print (tamu)

# karyawan = []
# for i in out.find_all('li', class_="Emp"):
#     karyawan.append(i.text)

# print (karyawan)


# - JSON ==> Format standar data yang ada di HTML (Secara mayoritas), JavaScript Object Notation

member = [{
    "nama" : "Rudi",
    "usia" : 20,
    "kota" : "Bandung"
}]

import json

## Menulis File JSON
# with open ("latihan.json", "w") as file:
#     json.dump(member, file)

# print("File Created")


## Membaca File JSON
# with open("latihan.json") as file:
#     Output = json.load(file)

# print ("Data Loaded")
# print (Output)

# w = write = nulis
# dump = fungsi untuk menulis file JSON
# r = read = baca
# load = fungsi untuk membaca file JSO








### File HTML Online
# Beautifulsoup
# Requests

from bs4 import BeautifulSoup
import requests
# --- GET and POST ==> Request

url = "http://127.0.0.1:5500/contoh.html"

web = requests.get(url)

out = BeautifulSoup(web.content, "html.parser")

print (out.h1.text)
print (out.p.text)
print (out.strong.text)

tamu = []
for i in out.find_all('li', class_ = "Orang"):
    tamu.append(i.text)
print (tamu)

karyawan = []
for i in out.find_all('li', id = "Person2"):
    karyawan.append(i.text)
print (karyawan)



