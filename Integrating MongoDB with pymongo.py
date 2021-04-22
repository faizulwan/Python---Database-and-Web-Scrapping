# Untuk mengkoneksikan database MongoDB dengan program Python
# dibutuhkan package
# pymongo

# # #Install Package
# py -m pip install pymongo

import pymongo
# print ("Install Success")

# Database (Server) === Client ==> Harus mengetahui Nama Server atau IP Server
# Harus tau Nama Server

# Jika MongoDB tidak di set sebagai Services (Autorun), maka server harus dinyalakan

# #Cara menyalakan - Mengaktifkan Server
# Buka Command prompt (Terminal)
# ketik cd
# Masuk ke Path Server: cd C:\Program Files\MongoDB\Server\4.4\bin
# Ketik mongod

# ### Definisikan Lokasi Server
# mongodb://Nama server:port/

dburl = 'mongodb://localhost:27017'  ## Mendefinisikan lokasi server (Lokal) dan Port (Default:27017)

# 27017 : Port default dari MongoDB
# Localhost : Karena DB diinstall di PC/Device Client (Lokal)

myMongo = pymongo.MongoClient(dburl) ### Mendefinisikan Client yang akan terkoneksi dengan server Database yang telah didefinisikan

# print ("Connection Success")


### Show Database ==> Untuk melihat isi database di dalam server
dbs = myMongo.list_database_names()
# print (dbs)

### untuk melihat collections ==>Kita harus masuk memilih database

myDB = myMongo['Purchasing']  ### Memilih Database

List_Col = myDB.list_collection_names() # Untuk melihat collections di dalam database Purchasing

# print (List_Col)


### Meilih / Menggunakan Collection
myEmployee = myDB['Employee'] ## Mengaktifkan/memilih Collection Employee
# myAset = myDB['Aset'] ## MEngaktifkan collection Aset

##### Melihat Data dalam Collections
## Hasil dari.find() berupa object, sama seperti map atau filter
## Sehingga perlu dikonversi agar bisa dibaca

All_Data = list(myEmployee.find())  ##Menampilkan Seluruh data didalam collections
# print (All_Data)

# ## Looping data yang telah dikonversi
# for i in All_Data:
#     print (i['Nama'])

newDB = myMongo['Marketing']
# ## Memiliki 2 fungsi
# # - Jika Database sudah ada di dalam server, maka DB tersebut akan dipilih dan diaktifkan (Contoh DB Purchasing) 
# # - Tapi, Jika database belum ada/tidak ada, maka DB tersebut akan dibutuhkan

# newCol =newDB['Karyawan'] ##Membuat collection Karyawan

# # print (dbs)
# ## Database baru tidak akan tampil, jika belum ada data di dalam collections 

# ### MEmasukkan Data ke dalam Collections (Create)

# data = {
#     "NIK" : "123AB",
#     "Nama" : "Ricky",
#     "Kota" : "Jakarta",
#     "Usia" : 24
# }

# # newCol.insert_one(data) ### Memasukkan data ke dalam collections (newCol)

# # print ("Data Submitted")

# # print (dbs)

# # for i in newCol.find():  # Melihat isi data di dalam collections
# #     print (i)

# data_1 = {
#     "NIK" : "123Ac",
#     "Nama" : "John",
#     "Kota" : "Bandung",
#     "Usia" : 26
# }

# x = newCol.insert_one(data_1)
# x.inserted_id ==> Memunculkan ID ketika data awal baru di masukkan
# print (f"Data Submitted, with ID: {x.inserted_id}")

# for i in newCol.find():  # Melihat isi data di dalam collections
#     print (i)




### Mengakses data dengan kondisi tertentu
### Isi Collections employee
# '_id': ObjectId('5fda1ef1ef0427b82461cd12'), 'Nama': 'Bram', 'Usia': '25', 'Kota': 'Jakarta', 'Gaji': 15000000.0, 'Divisi': 'Data Management'}
# {'_id': ObjectId('5fda1ef1ef0427b82461cd13'), 'Nama': 'Cia', 'Usia': '27', 'Kota': 'Bandung', 'Gaji': 20000000.0, 'Divisi': 'Data Management'}
# {'_id': ObjectId('5fda1ef1ef0427b82461cd14'), 'Nama': 'Fodenn', 'sia': '28', 'Kota': 'Jakarta', 'Gaji': 25000000.0, 'Divisi': 'Data Management'}
# {'_id': ObjectId('5fda1ef1ef0427b82461cd15'), 'Nama': 'Sho', 'Usia': 21.0, 'Kota': 'Amsterdam', 'Gaji': 50000000.0, 'Divisi': 'Data Management'}
# {'_id': ObjectId('5fda1ef1ef0427b82461cd16'), 'Nama': 'Albert', 'Usia': 26.0, 'Kota': 'Washington', 'Gaji': 70000000.0, 'Divisi': 'Data Management'}
# {'_id': ObjectId('5fda1ef1ef0427b82461cd17'), 'Nama': 'Shi', 'Usia': 22.0, 'Kota': 'Taipei', 'Gaji': 100000000.0, 'Divisi': 'Data Management'}
# {'_id': ObjectId('5fdb6188781e329365819e2e'), 'Nama': 'Mike', 'Kota': 'Balikpapan', 'Gaji': 17000000.0, 'Divisi': 'Data Management'}
# {'_id': ObjectId('5fdb6aea781e329365819e2f'), 'Nama': 'Cia', 'Usia': '27', 'Kota': 'Medan', 'Gaji': 15000000.0, 'Divisi': 'Data Management'}


# kondisi = {"Nama" : "Fodenn"}

# cari = myEmployee.find(kondisi)

# for i in cari:
#     print (i)

## query : db.employee.find({"Nama":"Fodenn"})


### Memasukkan data berdasarkan user input

# col_Baru = newDB['Barang']  ##Collection baru di dalam DB marketing

# kode = input("Masukkan Kode Barang : ")
# nama = input("Masukkan Nama Barang: ")
# harga = float(input("Masukkan Harga Barang: "))
# stok = int(input("Masukkan Stok Barang: "))


# new_data = {
#     "kode" : kode,
#     "Nama" : nama,
#     "Harga": harga,
#     "Stock": stok
# }

# x = col_Baru.insert_one(new_data)

# print (f"Data berhasil diinput denggan ID {x.inserted_id}")
# print ("="*50)

# print ("Keseluruhan Barang : ")
# for i in col_Baru.find():
#     print (i)


col_2 = newDB["Seragam"]  ## Memasukkan/membuat collection baru (Seragam) di dalam Database lama (Marketing)

# DATA = [
#     {"Jenis" : "Celana Panjang", "Stok" : 30},
#     {"Jenis" : "Kemeja", "Stok" : 25},
#     {"Jenis" : "Kaos", "Stok" : 15},
#     {"Jenis" : "Sepatu", "Stok" : 20}
# ]

# col_2.insert_many(DATA)

# print ("Data Saved")

# for i in col_2.find():
#     print (i)


### Mengakses Data Collectioons dengan kondisi tertentu
# for i in myEmployee.find():
#     print (i)

### Akses menggunakan syntax membership (IN)
# Kota = ["Jakarta", "Bandung"]
# kondisi = {"Kota" : {"$in" : Kota}}

# y = myEmployee.find(kondisi)

# for i in y:
#     print (i)


#### Conditional - Logical Condition

## Operator OR
## Menampilkan data yang memenuhi minimal salah satu kondisi yang ditentukkan

#Alt 1
# Kondisi = {"$or" : [{"Gaji" : 15000000}, {"Kota" : "Jakarta"}]}

# z = myEmployee.find(Kondisi)
# for i in z:
#     print (i)


# Alt 2
# operator = "$or"
# Kondisi1 = {"Gaji" : 10000000}
# Kondisi2 = {"Kota" : "Jakarta"}

# query = {operator : [Kondisi1, Kondisi2]}
# z = myEmployee.find(query)

# for i in z:
#     print (i)


## Operator And
## MEnampilkan Data yang memnuhi SELURUH kondisi yang ditentukan

# Alt 1
# Kondisi = {"$and" : [{"Gaji" : 15000000}, {"Kota" : "Jakarta"}]}

# z = myEmployee.find(Kondisi)
# for i in z:
#     print (i)


# Alt 2
# operator = "$and"
# Kondisi1 = {"Gaji" : 15000000}
# Kondisi2 = {"Kota" : "Jakarta"}

# query = {operator : [Kondisi1, Kondisi2]}
# z = myEmployee.find(query)

# for i in z:
#     print (i)




# query = {"Kota": {"$ne" : "Jakarta"}}
# z = myEmployee.find(query)

# for i in z:
#     print (i)

################################################### Mengupdate Data
#### Ketika yang akan diupdate adalah Value

# for i in col_2.find():
#     print(i)


# {'_id': ObjectId('5ff5ca1e6d7bd95a13afc5f3'), 'Jenis': 'Celana Panjang', 'Stok': 30}
# {'_id': ObjectId('5ff5ca1e6d7bd95a13afc5f4'), 'Jenis': 'Kemeja', 'Stok': 25}
# {'_id': ObjectId('5ff5ca1e6d7bd95a13afc5f5'), 'Jenis': 'Kaos', 'Stok': 15}
# {'_id': ObjectId('5ff5ca1e6d7bd95a13afc5f6'), 'Jenis': 'Sepatu', 'Stok': 20}


# Data = {"Jenis" : "Kemeja"}
# new_val = {"$set" :{"Stok" : 100}}

# # col_2.update_one(Data, new_val)

# # for i in col_2.find():
# #     print (i)


# Data = {}
# value_baru = {"$set" : {"Kondisi" : "BNIB"}}

# col_2.update_many(Data, value_baru)
# print ("Data Updated")

# for i in col_2.find():
#     print (i)


### Menghapus Property
# Data = {"Jenis" : "Kaos"}
# new_val = {"$unset" : {"Kondisi" : True}}
# col_2.update_one(Data, new_val)

# print ("Data Updated")

# for i in col_2.find():
#     print (i)


### Mengubah Property
# Data = {"Stok" : 30}
# new_val = {"$rename" : {"Jenis" : "Nama"}}

# col_2.update_one(Data, new_val)

# for i in col_2.find():
#     print (i)



# ### Hapus Data
# Kondisi = {"Jenis" : "Sepatu"}
# col_2.delete_one(Kondisi)

# for i in col_2.find():
#     print (i)

# col_2.delete_many({})