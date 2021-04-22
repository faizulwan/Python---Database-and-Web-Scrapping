MySQL 

- Server sudah auto run 
- Perlu mengaktifkan Client 
Ada 3 metode 
- Melalui Workbench 
- Melalui MySQL Command Line Client
- Melalui cmd - Command Prompt Windows / Terminal - Mac/Linux 

### Melalui Command Prompt Windows
 Masuk ke Path Server 
 C:\Program Files\MySQL\MySQL Server 8.0\bin
 Kemudian masukkan user dan password 
 mysql -u (namauser) -p (kemudian enter)
 - Masukkan Password 

 mysql -u kal -p 
 password : *****

 Jika keluar 
 mysql>
 berarti Client sudah Siap 

- SQL menganut sistem snake case (Sehingga tidak case sensitive)
============================================
####################

# Untuk melihat database di dalam server
show databases;

# untuk membuat Database
create Database (Nama database);

create database Sales;
create database contoh;
create database toko_online;

# Untuk menghapus database
drop database (nama database);

drop database contoh;

# Untuk memilih/menggunakan/mengaktifkan database
use (nama database);

use Sales;

# Membuat Tabel - dan struktur nya
create Table (Nama tabel) (Kolom/Field Atribut/tipe data)

create table Aset (noAset tinyInt, Nama char(25), stok smallInt);

create table contoh (noUrut Int);

# Melihat daftar tabel dalam database
show tables;

# Untuk menghapus tabel
drop table (nama tabel);

drop table contoh;

# Untuk Melihat STruktur Tabel
desc (nama tabel);
describe (nama tabel);

desc Aset;
describe Aset;

## Untuk memasukkan data ke dalam Tabel

#Alt 1
INSERT INTO namaTabel VALUES (Masukkan values/data yg akan diinput);
Values/data yg akan dimasukkan, harus Berurutan sesuai struktur tabel 

insert into aset values (12, "Pensil", 55);

# Alt 2
INSERT INTO namaTabel (Field1, Field2) values (Values/data yg akan diinput)

INSERT INTO Aset (stok, noAset) Values (89, 16)

## Untuk memasukkan banyak data sekaligus

INSERT INTO namaTabel (Field1, Field2) values 
(Values/data yg akan diinput),
(Values/data yg akan diinput),
(Values/data yg akan diinput) ....dst 


INSERT INTO Aset (Nama) Values 
("Pulpen"),
("Whiteboard");
- Kolom yg tidak diisi, akan bernilai NULL atau DEFAULT (Sesuai atribut kolom) == noAset dan Stok

## Primary Key & FOreign Key 
- Kolom/Field yg memiliki Data Unik 
- Kolom ini bisa digunakan sebagai Representasi Baris data    
- Primary Key tidak bisa NULL (Harus ada Isinya)
- Primary Key tidak menerima data Duplikat (Harus Unik dan berbeda di setiap Baris data)
- Jika ada Field/Kolom yg memiliki atribut Auto_Increment biasany menjadi Primary Key 
- Primary Key yg digunakan di Table lain, namanya berubah menjadi Foreign Key 
- Primary Key - Foreign Key digunakan sebagai penghubung antar Tabel (Relasi)

# Update Data 

# Kode_Mahasiswa - Kode_Matakuliah - Nilai
UPDATE nama_tabel SET field = Value_baru WHERE Kondisi;

UPDATE Aset SET stok = 100 WHERE Nama = "Pulpen"; ==> Update 1 Field/Kolom

UPDATE Aset SET stok = 250, Nama = "PC Gaming" WHERE Nama = "PC"; ==> Update beberapa Field/Kolom 

# Hapus Kolom/Field
DELETE From nama_tabel WHERE Kondisi;

DELETE From Aset Where Nama = "Lemari";

# Membaca Seluruh Data
SELECT * From NamaTabel;

SELECT * From Aset;

Create - Read - Update - Delete

############################# Update Struktur Tabel

# Menambahkan Kolom Baru
ALTER TABLE nama_tabel ADD COLUMN nama_kolom tipe data opt Atribut;

ALTER TABLE employee ADD COLUMN Umur TinyInt; ==> akan menambahkan Kolom Umur pada Tabel Employee 
==> secara default, kolom baru yg ditambahkan akan diletakkan pada posisi paling kanan dari tabel
==> Setelah ditambahkan Kolom baru, isi kolom untuk Data lama sesuai dg Atribut yg digunakan
==> Akan bernilai DEFAULT (jika nilai default kita tentukan) dan akan bernilai NULL jika tidak ada nilai Default 
==> Query di atas akan membuat nilai kolom umur untuk data lama bernilai NULL 

ALTER TABLE employee ADD COLUMN Umur TinyInt DEFAULT 24;
==> Akan membuat nilai kolom umur untuk data lama bernilai 24

# Menghapus Kolom yg sudah ada

ALTER TABLE nama_tabel DROP COLUMN nama_kolom;

ALTER TABLE employee DROP COLUMN Umur; => akan menghapus kolom Umur dari tabel Employee 

# Menambahkan Kolom pada posisi Tertentu
- Query sama dengan ketika menambahkan Kolom, hanya ada sedikit tambahan Atribut untuk Posisi 

ALTER TABLE nama_tabel ADD COLUMN nama_kolom tipe_data AFTER nama_kolom;

ALTER TABLE employee ADD COLUMN Umur TinyInt DEFAULT 24 AFTER Kota;
=> Akan menambahkan kolom Umur disebelah kanan kolom Kota 
=> Nilai untuk data sebelumnya/lama 24 (Nilai DEFAULT)

# Mengubah Posisi Kolom yg sudah ada
ALTER TABLE nama_tabel MODIFY COLUMN nama_kolom tipe_data AFTER nama_kolom;

ALTER TABLE employee MODIFY COLUMN Kota char(50) AFTER Nama;
=> Akan mengubah posisi Kolom Kota menjadi di sebelah kanan kolom Nama

# Mengganti nama kolom
ALTER TABLE nama_tabel RENAME COLUMN nama_kolom_lama TO nama_kolom_baru;

ALTER TABLE employee RENAME COLUMN Umur TO Usia;
=> Akan mengubah nama kolom Umur menjadi Usia 

# Mengganti Tipe Data Kolom 
ALTER TABLE nama_tabel MODIFY COLUMN nama_kolom tipe_data_baru;

ALTER TABLE employee MODIFY COLUMN Nama Varchar(60);
=> Akan mengubah Tipe data dari kolom Nama menjadi Varchar(60)

#################################### Read Data

# Menampilkan Kolom tertentu dari Tabel
SELECT kolom_1, kolom_2, Kolom_3 FROM nama_tabel;

SELECT Nama, Kota, Gaji FROM employee;
=> Akan menampilkan Kolom Nama, Kota dan Gaji dari Tabel Employee
=> Tabel yg dihasilkan disebut Result table/Result set 
=> Urutan kolom yg ditampilkan bisa disesuaikan Tidak harus berurut sesuai Tabel Original 
=> Untuk mengganti nama kolom ketika ditampilkan pada Result Table, gunakan alias
=> as .... 

SELECT Nama as Nama Karyawan, Kota as Lokasi, Gaji as Gaji Pokok FROM employee;

Result Tabel akan menghasilkan
Nama Karyawan | Lokasi | Gaji Pokok 

=> Perubahan nama kolom pada Result tabel, bersifat Read Only dan Tidak Mengupdate/Mengubah Kolom pada tabel Original

## Membuat Kolom-Field Sintetis hasil Operasi Math

SELECT Nama, Kota, 0.2 * gaji as KenaikanGaji from employee;
=> Akan Menghasilkan-menampilkan Kolom Nama, Kota dan Kalkulasi dari Gaji * 0.2 untuk setiap baris data  
=> Kolom hasil Kalkulasi (KenaikanGaji) Tidak ditambahkan di Tabel Original 

## Mengurutkan Data 
SELECT kolom_1, kolom_2, kolom_3 FROM nama_tabel ORDER BY nama_kolom;

SELECT * FROM nama_tabel ORDER BY nama_kolom;

- Sebaiknya nama kolom yg digunakan sebagai dasar pengurutan, ditampilkan di Result set

SELECT nama, kota, gaji FROM employee ORDER BY Gaji;
=> Akan menampilkan kolom nama, kota dan gaji, dan diurutkan berdasarkan kolom Gaji, dg metode Ascending (Terkecil ke Terbesar)
=> Secara DEfault, metide pengurutan menggunakan Ascending 

SELECT nama, kota, gaji FROM employee ORDER BY Gaji Desc;
=> Akan diurutkan berdasarkan gaji, dg metode Descending (Terbesar ke terkecil)

SELECT nama, kota, gaji FROM employee ORDER BY Kota, Gaji Desc;
=> Data Akan diurutkan berdasarkan Kota terlebih dahulu (Metode Ascending) Kemudian diurutkan lagi berdasarkan Gaji
dg metode Descendig (Terbesar ke terkecil)

### Menampilkan Data dengan Kondisi Tertentu
# Kondisi Berdasarkan Kolom yg ada pada Tabel Original

SELECT kolom_1, kolom_2, kolom_3 FROM nama_tabel WHERE Kondisi (Menggunakan Kolom dari Tabel Original);

SELECT nama, kota, gaji FROM employee WHERE kota = 'jakarta';
=> Akan menampilkan Data dg value Kota = 'Jakarta'

SELECT nama, kota, gaji From employee WHERE kota = 'jakarta' ORDER BY Gaji;

SELECT nama, kota, gaji From Employee WHERE kota != 'jakarta';
=> akan menampilkan data yg kotanya bukan jakarta

# Jika kondisi yg diinginkan SAMA PERSIS dengan data di kolom tertentu gunakan operator "="
# Jika kondisi yg dinginkan TIDAK SAMA dengan data di kolom tertentu gunakan operator "!="
# Gunakan Operator lain sesuai kebutuhan ">" untuk lebih besar dari atau "<" untuk kurang dari, dll

##### Menampilkan data dengan Kondisi Lebih dari 1

# Menampilkan data dg kondisi lebih dari 1 value (Kolom yg sama)

SELECT kolom_1, kolom_2, kolom_3 FROM nama_tabel WHERE nama_kolom IN (Kondisi);


SELECT nama, kota, gaji from employee WHERE Kota IN ('jakarta', 'bandung');
=> Akan menampilkan data yg kotanya Bandung atau Jakarta

SELECT kolom_1, kolom_2, kolom_3 FROM nama_tabel WHERE nama_kolom NOT IN (Kondisi);

SELECT nama, kota, gaji from employee WHERE Kota NOT IN ('jakarta', 'bandung');
=> Akan menampilkan data yg kotanya Bukan Bandung atau Jakarta

### Jika Kondisi dari Kolom yg Berbeda, dan SEMUA KONDISI HARUS TERPENUHI
SELECT kolom_1, kolom_2, kolom_3 FROM nama_tabel WHERE kondisi_1 AND kondisi_2 AND kondisi_3 AND kondisi_4 dst;

SELECT nama, kota, gaji From Employee WHERE Kota = 'Jakarta' AND gaji > 20000000;
=> Akan menampilkan data yg kotaya jakarta DAN gajinya diatas 20juta.

### Jika Kondisi dari Kolom yg berbeda dan SALAH SATU Kondisi Terpenuhi.
SELECT kolom_1, kolom_2, kolom_3 FROM nama_tabel WHERE kondisi_1 OR kondisi_2 OR kondisi_3 OR kondisi_4 dst;

SELECT nama, kota, gaji From Employee WHERE Kota = 'Jakarta' OR gaji > 20000000;
=> Akan menampilkan data yg kotaya jakarta ATAU gajinya diatas 20juta.

### Jika Kondisi dari Rentang (Range) tertentu
SELECT kolom_1, kolom_2, kolom_3 FROM nama_tabel WHERE nama_kolom BETWEEN kondisi AND kondisi;

SELECT nama, kota, gaji From employee WHERE Gaji BETWEEN 15000000 AND 25000000;
=> akan menampilkan data yg memiliki gaji antara 15juta sampai 25juta
=> bersifat Inclusive sehingga value antara Between tetap akan ditampilkan 

SELECT nama, kota, gaji From employee WHERE 15000000 <= gaji =< 25000000

# Format Tanggal - BETWEEN biasanya digunakan juga untuk data bertipe DATE 
Tahun Bulan Hari 
20210113
SELECT nama, kota, gaji, tgl_masuk WHERE tgl_masuk BETWEEN '20200301' AND '20201130';
=> akan menampilkan data yg memiliki Tanggal masuk antara 1 maret 2020 sampai 30 november 2020.

### HAVING
- Having kita gunakan jika, Kondisi berdasarkan Kolom Sintetis (Tidak ada di Tabel Original)

SELECT nama, kota, 0.2 * gaji as Kenaikan From employee HAVING Kenaikan > 3000000;
=> akan menampilkan data yg memiliki kenaikan diatas 3 juta
=> tidak menggunakan WHERE, karena Kenaikan merupakan Tabel sintetis (Tidak ada di Tabel Original)

### Menampilkan Data yg memiliki Unsur tertentu

SELECT kolom_1, kolom_2, kolom_3 FROM nama_tabel WHERE nama_kolom LIKE 'unsur';

SELECT nama, kota, gaji from employee where nama Like 'John';
=> Menampilkan data yg namanya John 

SELECT nama, kota, gaji from employee WHERE nama Like '%a';
=> Menampilkan data yg namanya berakhiran huruf A 

SELECT nama, kota, gaji from employee WHERE nama Like 'a%';
=> Menampilkan data yg namanya berawalan huruf A 

SELECT nama, kota, gaji from employee WHERE nama Like 's%a';
=> Menampilkan data yg namanya berawalan huruf S dan berakhiran huruf A 

SELECT nama, kota, gaji from employee WHERE nama Like '%a%';
=> Menampilkan data yg namanya memiliki huruf A

SELECT nama, kota, gaji from employee WHERE nama Like '%sa';
=> Menampilkan data yg namanya berakhiran SA 

Tabel A --> Tabel B --> Tabel C ---> Tabel D

Nama - Kota - Gaji - Kenaikan - Upd by - Latest Update (timestamp)


Tabel Master 
Tabel Transaksi



Create - Update - Delete 

Database ====> Aplikasi 

#### Mendapatkan Data Teratas
SELECT * FROM nama_tabel LIMIT nilai;

SELECT * FROM employee LIMIT 5;
menampilkan 5 data teratas - data pertama 


SELECT * FROM employee ORDER BY gaji LIMIT 3,5;
=> Menampilkan data yg telah diurutkan berdasarkan gaji dg metode Ascending 
=> Kemudian melewatkan(skip) 3 data pertama, kemudian tampilkan 5 data selanjutnya.

URUTAN SYNTAX SELECT :
1. select
2. from
3. where
4. like
5. group by
6. having
7. order by
8. limit


Database Administrator
Data Engineer

Data Analyst

Data Scientist




############################## Aggregation Data

# Menghitung Jumlah Data
SELECT COUNT(*) FROM nama_tabel;

SELECT COUNT(*) FROM Employee; => Akan menampilkan jumlah Employee


# Summary Data (Jumlah Total) = Data Numerik - Math
SELECT SUM(nama_kolom) FROM nama_tabel;

SELECT SUM(Gaji) FROM Employee;
=> Menampilkan total gaji Employee secara keseluruhan


# Rata-rata Data => Data Numeruk - Math
SELECT AVG(nama_kolom) FROM nama_tabel;

SELECT AVG(Gaji) FROM Employee;
