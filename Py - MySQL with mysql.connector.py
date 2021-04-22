# ### Mengkoneksikan MySQL dengan Python

# Package yang akan digunakan 
# mysql-connector-python

# - pyMysqp
# - SQLLite
# - SQLAlchemy



import mysql.connector

## Server --- Client

## Server


# - Definisikan Server
# - Definisiakan User Akses
# - Definisikan Database

myDB = {
    'user' : 'faizulwan',
    'password' : 'blokg9',
    'host' : 'localhost',
    'database' : 'sales'
}


#### Client

# Definisikan Client

conn = mysql.connector.connect(**myDB)

# print (200)


C = conn.cursor()   ##Digunakan untuk mengeksekusi query SQL


##### Query

# Describe tabel
# query = 'DESCRIBE Employee'

# C.execute(query)

# for i in C:
#     print (i[0], i[1])


# Membuat Table baru
# query = """ CREATE TABLE Departement
# (Dept_ID char(10), Dept_Name char(30))
# """

# C.execute(query)
# print (200)


# Memasukkan Data ke dalam Tabel
# query = "INSERT INTO Departement VALUES ('D01', 'Finance')"

# C.execute(query)

# conn.commit() #Dibutuhkan ketika melakukan Data Manipulation (Create-Update-Delete)
# print (200)

############# Alternatif 1 untuk memasukkan data
# sql = "INSERT INTO Departement VALUES (%s, %s)"
# val = ("D02", "Accounting")

# C.execute(sql,val)
# conn.commit()
# print (200)

# Memasukkan Employee yang ada valuenya
# sql = "INSERT INTO Employee (Nama, Kota, Gaji) VALUES (%s, %s, %s)"
# val = ("Bayu", "Malang", "26000000")

# C.execute(sql,val)
# conn.commit()

# print (200)


### Memasukkan Banyak Data
# sql = "INSERT INTO Departement VALUES (%s, %s)"
# val = [
#     ("A01", "HR"),
#     ("C02", "Marketing"),
#     ("E04", "Data")
# ]

# C.executemany(sql, val)
# conn.commit()
# print (200)



### Mengakses Data (READ)
# Alt 1
# query = "SELECT *FROM Departement"
# C.execute(query)

# for i in C:
#     print(i)


# Alt 2
# query = "SELECT * FROM Departement"
# C.execute(query)

# hasil = C.fetchall()

# for i in hasil:
#     print(i)

# # count = 2
# query = f"SELECT *FROM Departement LIMIT {count}"
# query = "SELECT *FROM Departement LIMIT 3"

# C.execute(query)

# for i in C:
#     print (i)



# # Mengupdate Data
# query = "UPDATE Employee SET Usia = '24' WHERE Nama = 'Bayu'"
# C.execute(query)

# conn.commit()


# Hapus Data
query = "DELETE FROM Employee WHERE Nama = 'Bayu'"
C.execute(query)

conn.commit()