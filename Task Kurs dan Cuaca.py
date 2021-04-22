# ==================================================================================================================================================
########################## Konversi Mata Uang
'''
Buat Program untuk Konversi mata uang 

Menu :
1. IDR to Mata Uang Asing 
2. Mata Uang Asing to IDR 

Pilihan 1 :
- Masukkan Nama Bank 
- Masukkan Mata Uang Asing : USD/JPY/GBP dll 
- Masukkan Nilai Rupiah : 500000

Output :
Nilau uang anda ... Rupiah dalam ..(mata uang asing)... adalah .... (nilai konversi) 

Pilihan 2:

- Masukkan Nama Bank 
- Masukkan Mata Uang Asing : USD/JPY/GBP dll 
- Masukkan Nilai uang anda : 50

output:
Nilau uang anda .50 usd.. (Mata uang asing) dalam rupiah . adalah .... (nilai konversi)... 
'''


import requests

print ('===> KONVERSI MATA UANG 15 DEC 2020 <===')  # Pemberitahuan Aplikasi
print ('''Menu :
1. IDR to Mata Uang Asing 
2. Mata Uang Asing to IDR''')

menu = int(input('Pilih Menu (1/2) : '))  # Meminta user untuk memilih menu

if menu == 1:
    print ('==> Menu IDR to Mata Uang Asing <==')

    try:
        bank = str(input('Masukkan Kode Bank : ')).lower()                      # Meminta inputan kode bank 
        matauang = str(input('Masukkan Tujuan Mata Uang Asing : ')).lower()     # Meminta inputan kode mata uang 
        rupiah = int(input('Masukkan Nilai Mata Uang Rupiah Anda : '))          # Meminta inputan jumlah nominal uang

        banklist = list(bank)
        matauanglist = list(matauang)
        l_bank = len(banklist)
        l_matauang = len(matauanglist)

        url = f"https://api.kurs.web.id/api/v1?token=UNWXLXmQM8Uxo3heTycJit8PIApGQy0LBlGSZ5ry&bank={bank}&matauang={matauang}"
        web = requests.get(url)
        output = web.json()

        
        kursbeli = output['beli']
        konversi = float(rupiah/kursbeli)

        print (f"Nilau uang anda {rupiah} Rupiah dalam {matauang} adalah {konversi}")
                
    except:
        print ('''Invalid Input:
        1. Kode Bank salah
        2. Kode Mata Uang tidak ditemukkan
        3. Tidak menerima format nominal tersebut''')


elif menu == 2:
     print ('==> Menu Mata Uang Asing to IDR <=1=')

     try: 
        bank = str(input('Masukkan Kode Bank : ')).lower()
        matauang = str(input('Masukkan Asal Mata Uang Asing Anda : ')).lower()
        nominal = int(input('Masukkan Nilai Mata Uang Asing Anda : '))

        banklist = list(bank)
        matauanglist = list(matauang)
        l_bank = len(banklist)
        l_matauang = len(matauanglist)

        url = f"https://api.kurs.web.id/api/v1?token=UNWXLXmQM8Uxo3heTycJit8PIApGQy0LBlGSZ5ry&bank={bank}&matauang={matauang}"
        web = requests.get(url)
        output = web.json()
        kursjual = output['jual']
        konversi = float(nominal * kursjual)

        print (f"Nilau uang anda {nominal} {matauang} adalah {konversi} Rupiah")

     except:
        print ('''Invalid Input:
        1. Kode Bank salah
        2. Kode Mata Uang tidak ditemukkan
        3. Tidak menerima format nominal tersebut''')

else:
    print ("Menu tidak ditemukkan")


# ====================================================================================================================================
########################################## Open WeatherMap ## Prakiraan Cuaca
### https://openweathermap.org/
'''
# api.openweathermap.org/data/2.5/weather?q=London&appid={API key}

key = '3a18ccca6a337aa57302cc46a2907609'
host = "api.openweathermap.org"
kota = input("Masukkan Nama Kota : ")

url = f"https://{host}/data/2.5/weather?q={kota}&appid={key}"

data = requests.get(url)
cuaca = data.json()

print(cuaca)

#### Latihan Prakiraan Cuaca

Input : Masukkan Nama Kota : 

Output :

Kota yang anda pilih adalah : .....
Suhu : .... (Celcius)
Keadaan cuaca : ..... berawan ...
Koordinat Kota anda : Lat .... Long ...
Humidity Level : ....
Kecepatan Angin : .....

Kalau Kota tidak ada : 
Kota yang anda masukkan tidak terdaftar 

Format Kota yang anda masukkan salah 

## Gunakan API OpenweatherMap
'''

# api.openweathermap.org/data/2.5/weather?q=London&appid={API Key}

# import requests

# key =  '188e6e77eb0608e60b4fea0f7d6b2eb7'
# host = "api.openweathermap.org"
# kota = input("Masukkan nama kota : ").lower()

# url = f"https://{host}/data/2.5/weather?q={kota}&appid={key}"
# data = requests.get(url)
# cuaca = data.json()

# print (cuaca)
