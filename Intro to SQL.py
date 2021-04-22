MySQL

Salah satu dari DBMS yang berbasis relasi
- Big Data --> 3v
    Volume
    Variety
    Velocity





RDBMS ===> Relational Database Management System
Contoh RDBMS :
- MySQL, Oracle, Postgres, MS. Access, Ms. SQL Server


Bahasa yang digunakan secara de facto ==> Structured Query Language (SQL)

DDL = Data Definition Language => Memanipulasi Struktur Database
DML => Data Manipulation Language =>

MongoDB => Camel Case
SQL => Snake Case

MongoDB ==> User akses terletak di masing-masing database

MySQL ==> User access terletak di server

CRUD => Create Read Update Delete

root => Akses paling tinggi ==> SuperAdmin

Kita dapat membuat user dengan privilage yang sama dengan root




##### Bekerja dengan SQL
- Server SQL berjalan secara auto run
- Create User  
- Login ke dalam server -sistem
- Create Database
- Use Database
- Create Table ==> Membuat Tabel sekaligus Struktur Tabel (Nama kolom dan tipe data untuk kolom tersebut)
- Insert Data sesuai dengan struktur Tabel
- Bisa melakukan DML


Data ==> Tuple (rows), Field (columns)

=======================================================================================================

Tipe Data di SQL
- Numerik
- String
- Date
- Text


========================================================================================================
NUMERIK :
- Integer
- Fixed Point
- Floating Point

INTEGER : Bilangan bulat (bukan pecahan/desimal)
- TinyInt ==> -128 s/d 127
- Smallint ==> -32.768 s/d 32.767
- MediumInt ==> 8,3 juta s/d 8,3 juta
- INT ==> 2,1 Milyar s/d 2,1 Milyar
- BigInt ==> -9,2 Quadrilion s/d 9,2 Quadralion

========================================================================================================
Jenis tipe data Fixed Point ==> Bilangan desimal/pecahan
yang angka dibelakang komanya, sudah diatur dari awal.
Define dengan 2 digit angka
- Digit pertama : Menunjukkan jumlah seluruh digit angka
- Digit kedua : Menunjukkan jumlah koma dibelakang angka

DECIMAL (4,2) ==> Total digit angka ada 4, Total digit angka dibelakang koma ada 2
-99,99 s/d 99,99

DECIMAL (4, 1) ===> -999.9 s/d 999,9
DECIMAL (3, 1) ===> -99,9 s/d 99,9
DECIMAL (3 .2) ===> 9,99 s/d 9,99

Angka pertama maksimal 65
Angka kedua maksimal 30
DECIMAL (65, 30)
======================================================================================================


FLOATING POINT
Bilangan desimal/pecahan tetapi angka dibelakang koma maupun total digit, bisa berbeda setiap berbasis
- Float
- Double ==> 2x float ==> Size 2x lipat




==========================================================================================================
STRING
1. Char ==> Max 255 Karatkter 
2. VarChar ==> 65.535 Karatkter

char(25)
varchar(25)


===> Binary & VarBinary ===> Metode penyimpanan char dengan  biner

=================================================================================================
TEXT

- Tiny Text ==> 255 Char
- Text ==> 65.535 Char
- MediumText ==> 16,7 jutaan Char
- LongText ==> 4,2 milyaran Char

=======================================================================================
DATE

- Date ==> Tanggal
- DateTime ==> Tanggal dan Jam
- Timestamp ==> Tanggal dan Jam ketika data diinput
- Year(2) ==> Format tahun 2 digit
- Year (4) ==> Format tahun 4 digit



========================================================================================
ENUM ==> Mirip dengan pilihan radio button/ Combo Box

User hanya dapat  memilih salah satu dari pilihan data yang sudah didefine sebelumnya
Contoh : Gender
- Male
- Female
Max opsi ==> 65.535 Pilihan


========================================================================================
SET

Mirip dengan checkbox
Mirip dengan ENUM, tetapi user dapat memilih lebih dari satu pilihan yang tersedia
Max hanya 64 pililhan


========================================================================================
Atribut Tipe Data

1. Auto Increment ==> Penambahan otomatis satu angka ==> 1 Kolom ==> Primary Key
2. Default (Jika tidak diisi) ==> NULL (Kosong)
    Nama Default (Anonim)
    Jika user tidak menginput/mengosongkan maka nama akan tersimpan sebagai anonim

    -Not NULL ==> Kolom menjadi mandatory (wajib diisi)
    -NULL ==> Data boleh dikosongkan ==> Secara default, semua kolom beratribut NULL
    -UNSIGNED ==> Untuk tioe data numerik, tidak bisa menerima nilai negatif
Range data akan lebih panjang
Contoh : 
    TinyINT ==> 0 s/d 255
    SmallInt ==> 0 s/d 65.535
    MediumInt ==> 0 s/d 16,7 juta
    Int ==> 0 s/d 4 milyaranBigInt ==> 0 s/d ....

-SIGNED ==> Menerima angka negatif

NIP - NIK
1
2

4
5
6



NIP - NIK

Tabel Mahasiswa ==> Independent Tabel
NIM - Nama - Jurusan - Tanggal Lahir - Alamat - Email - No Hp

Kolom Primary Key - Kolom unik yang merepresentasikan baris data - tidak boleh ada duplikat - tidak boleh kosong
Foreign Key ==> Primary Key yang digunakan di tabel lain

Tabel nilai ==> Dependent Tabel
Kode_MataKuliah - NIM - nilai

Tabel Mata Kode_MataKuliah ==> Independent Tabel
Kode_MataKuliah - MataKuliah - Dosen



=========>
Start MySQL

Server -- CLient
Server MySQL ==> Secara Default sudah Autorun


Client 
Ada 3 alternatif
1. Melalui Workbench ==> GUI (Graphic User Interface)
2. Melalui  MySQL Command Line Client
3. Melalui Command Prompt ===> 
    Masuk ke Parh Server MySQL -> C:\Program Files\MySQL\MySQL Server 8.0\bin
    Kemudian masukkan user dan password -? mysql -u (user) -p (kemudian enter) -> masukkan password
    Kalau cursor sudah menjadi mysql> (sudah masuk)

Memberi Nama Kolom atau Nama Tabel
Jika lebih dari satu kata gunakan CamelCase atau underscore (_)





