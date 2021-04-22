## Latihan - Tugas
'''
http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/
'''
'''
Lakukan Web Scrapping

Daftar Ultraman dan Daftar Monster
Nama Ultraman dan Nomornya, ==> 01. Ultraman
Nama Monster dan Nomornya, ==> 73. Judah Spectre

Export ke dalam File JSON

Format isi untuk File JSON:
[{"Ultraman" : {"01" : "Ultraman", "02" : "Ultra Seven"...}
"Monster" : {"01" : "alien Baltan". "02" : "Gomora"}}]
'''

from bs4 import BeautifulSoup
import requests
import json


url = "https://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/"

web = requests.get(url)

out = BeautifulSoup(web.content, "html.parser")


## Scrapping nama Ultraman dan Monster melalui tag 'strong'
strong = []
for i in out.find_all('strong'):
    strong.append(i.text)

# print (strong)

## Mengetahui index setiap ultraman dan monster yang terdapat
# ultraman = strong.index('01 Ultraman')
# monster1 = strong.index("01 Alien Baltan")
# monster2 = strong.index("73 Judah Spectre")

# print (ultraman)
# print (monster1)
# print (monster2)

## Slicing hasil scrapping sesuai dengan kebutuhan untuk nama ultraman dan monster
ultramannames = strong [2:36]
monsternames = strong [37:110]

print (ultramannames)

## Membuat dictionary ultraman berikut dengan nomor dan jenisnya
keyultraman = []
valueultraman = []
for i in ultramannames:
    keyultraman.append(i[:2])
    valueultraman.append(i[3:])
ultraman = dict(zip(keyultraman, valueultraman))

print ('=' * 50)
print (keyultraman)
print (ultraman)

## Membuat dictionary monster berikut dengan nomor dan jenisnya
keymonster = []
valuemonster = []
for j in monsternames:
    keymonster.append(j[:2])
    valuemonster.append(j[3:])
monster = dict(zip(keymonster, valuemonster))

# print (monster)

## Menulis file JSON
Scrapping_Ultraman = [dict(zip(['Ultraman','Monsters'],[ultraman, monster]))]
with open('Scrapping_Ultraman.json', 'w') as file:
    json.dump(Scrapping_Ultraman, file)

# print(Scrapping_Ultraman)