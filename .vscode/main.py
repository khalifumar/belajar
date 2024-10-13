
# print("Halo Jokow*")
# print("Apa kabar broooo")

# a = 2
# b = 5
# print(a + b)
# print(a * b)
# c = "apa lu"
# print(c)

# integer = 1
# print("Isi dari integer :", integer, ", bertipe :", type(integer))

# #ngambil elemen di bahasa manapun
# from ctypes import c_double, c_char
# data_apapun = c_double(25.5)
# print("data : ", data_apapun)
# print("tipenya : ", type(data_apapun))



# # #input apapun
# # integer_a = int(input("Masukan integer : "))
# # print("integer : ", integer_a, "Tipe :", type(integer_a))

# # string_a = str(input("Masukan integer : "))
# # print("integer : ", string_a, "Tipe :", type(string_a))

# print("\nProgram Perhitungan Suhu\n")

# #celciius
# celcius = float(input("Masukan suhu dalam celcius :"))
# print("Suhu adalah :", celcius, "Celcius\n" )

# #remour
# remour = celcius * (4 / 5)
# print("Suhu 2 adalah :", remour, "Remour\n")

# #fahrenheit
# fahrenheit = celcius * (9 / 5) + 32
# print("Suhu 2 adalah :", fahrenheit, "Fahrenheit\n")

# #kelvin
# kelvin = celcius + 273
# print("Suhu 3 adalah :", kelvin, "Kelvin\n\n")

# Perhitungan dari fahrenheit ke kelvin
# fahrenheit = float(input("Masukan angka farenheit :"))
# kelvin = (((fahrenheit - 32) * (5 / 9)) + 273)
# print("Hasil dari kelvin adalah : ", kelvin, "Kelvin")



# Perhitungan Komparasi Logika
# a = float(input("Masukan angka :"))
# syarat1 = a > 0
# syarat2 = a < 5
# syarat3 = a > 8
# syarat4 = a < 11

# isCorrect = (syarat1 and syarat2) or (syarat3 and syarat4)
# print("Jadi angka tersebut apakah sesuai kriteria? :", isCorrect)



# Nyoba belajar binner
# a = 9
# b = 5
# c = a ^ b
# print("Nilai :", a, "binary", format(a, "08b"))
# print("Nilai :", b, "binary", format(b, "08b"))
# print("Nilai :", c, "binary", format(c, "08b"))



# String
# a = "Aku laku"
# print("index ke-2"+ a[0:4])

# salam = "Hello Orkay"
# print(salam.upper())
# print(salam.lower())

# nyari_lower = salam.isupper()
# print("apakah kecil semua ? ", str(nyari_lower))
# nyari_huruf = salam.isalpha()
# print("apakah semuanya huruf ? ", str(nyari_huruf))
# nyari_kapital = salam.istitle()
# print("nyari kapital ? ", str(nyari_kapital))

# nama = "andi", "nana", "mamank"
# gabung = " ".join(nama)
# print(gabung)
# print(gabung.split(" "))

# kiri = "kiri".ljust(15)
# print("" + kiri + "")
# kanan = "kanan".rjust(15)
# print("" + kanan + "")
# tengah = "tengah".center(20,":")
# print("'"+tengah+"'")
# tengah = tengah.strip(":")
# print("'"+tengah+"'")

# nama = "yalu"
# umur = 23
# berat = 78
# ribuan = 20000
# nilai = 34.583

# string = f" hallo {nama}, apa kabar"
# kalimat = f"si {nama}, berumur {umur}, dengan berat {berat}, memiliki uang sebanyaak {ribuan:,}"
# nilaidoang = f"nilai {nilai:.1f}"
# nilaiaja = "nilainya {nilai:06.2f}"

# print(string)
# print(kalimat)
# print(nilaidoang)
# print(nilaiaja)



# Bidth and Multiline

# data_nama = "Bambang"
# data_umur = 17
# data_tinggi = 150.67
# data_nomor_sepatu = 45

# # \n = enter
# string = f"""
# Nama    = {data_nama}
# Umur    = {data_umur}
# Tinggi  = {data_tinggi}

# Sepatu  = {data_nomor_sepatu}
# """
# print(string)

# #merapihkan format
# string = f"""
# Nama    = {data_nama:>10}
# Umur    = {data_umur:>10}
# Tinggi  = {data_tinggi:>10}
# Sepatu  = {data_nomor_sepatu:>10}
# """
# print(string)



# Date and Time

# import datetime as dt
# hari_ini = dt.date.today()
# print(hari_ini)

# tanggal = dt.date(2005,2,23)
# print(f"hari {tanggal:%A}")

# Tugas membuat pencarian hari lahir
# print("Masukan tanggal, bulan, dan tahun lahir anda :")
# tanggal = int(input("Tanggal : "))
# bulan = int(input("Bulan : "))
# Tahun = int(input("Tahun : "))

# import datetime as dt
# lahir = dt.date(Tahun,bulan,tanggal)
# print(f"lahir pada hari : {lahir:%A}")

# hari_ini = dt.date.today()
# umur_hari = hari_ini - lahir
# umur_tahun = umur_hari.days // 365
# print(f"Umur sekarang : {umur_hari}")
# print(f"Usia sekarang : {umur_tahun} tahun, pada hari {lahir:%A}")



# IF and ELSE
# nama = str(input("Masukan Nama : "))
# if nama == "menk" :
#     print("Cakep banget dehh")
# elif nama == "bayu" :
#     print("Kurang cakep")
# else :
#     print("Kamu culun")
# print("Berakhir program")



# Contoh program kalkulator

# print(20*"=")
# print("Kalkulator Sederhana")
# print(20*"=")

# bilangan1 = int(input("Masukan Bilangan pertama :"))
# operator = str(input("Masukan operator (+, -, x, :) :"))
# bilangan2 = int(input("Masukan bilangan kedua :"))

# if operator == "+" :
#     hasil = bilangan1 + bilangan2
#     print("Hasilnya adalah :", hasil)
# elif operator == "-" :
#     hasil = bilangan1 - bilangan2
#     print("Hasilnya adalah :", hasil)
# elif operator == "x" or operator == "*" :
#     hasil = bilangan1 * bilangan2
#     print("Hasilnya adalah :", hasil)
# elif operator == ":" or operator == "/":
#     hasil = bilangan1 / bilangan2
# else : print("Incorrect")



# Perulangan (Loop) : for and while

# angka = "*"
# kalimat = {"Anak Orang"}
# jumlah = range(1,int(input("Masukan jumlah :")))

# for kumpulan_angka in jumlah:
#     print(f"{angka}")

# print(f"{kumpulan_angka}")

# i = 1
# while i <= 10:
#     while i % 2 == 0:
#         print("Genap")
#         i+=1
#     print(i)
#     i+=1



# Pass and Continue

# i = 2
# while i < 10:
#     print(i)
#     while i % 2 == 0:
#         i+=1
#         continue
#     i+=1



# Break
# i = 2
# while i < 10:
#     print(i)
#     i+=1
#     if i == 7:
#         break

# print("Progam Selesai")



# Program Bintang piramid
# i = 0
# j = 0
# k = 0
# l = 0
# jumlah = 10

# while i < jumlah:
#     while j <= jumlah:
#         bintang = print(j*"*")
#         j += 1
#     i += 1
# hasil
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

# while jumlah > k:
#     while jumlah > l:
#         bintang = print(jumlah*"*")
#         jumlah -= 1
#     jumlah -= 1
# hasil
# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *

# Sama seperti diatas
# while True:
#     print("*"*i)
#     i += 1
#     if i > jumlah:
#         break

# angka = 1
# while True:
#     angka += 1

#     if (angka % 2):
#         print("*"*angka)
#         angka+=1
#     else:
#         angka+=1
#         continue

#     if angka > jumlah:
#         break

# Ganjil Genap
# while True:
#     print("*"*angka)
#     angka+=1
#     if angka % 2:
#         print("Ganjil")

#     if angka > jumlah:
#         break

# Buat Piramid
# spasi = int(jumlah / 2)
# while True:
#     if i % 2:
#         print(" "*spasi + "*"*i + " "*spasi)
#         spasi-=1

#     i+=1
#     if i > jumlah:
#         break
# Hasil
#     *
#    ***
#   *****
#  *******
# *********



# List
# data = ["ini string", 2, True, False, 4,5]
# print(data)

# data[1] = 5
# print(data)

# data_range = range(0,11,2) #range(start, stop, steel)
# print(data_range)

# data_list = list(data_range)
# print(data_list)

# Membuat list dengan For Loop
# list_for_loop = [i**2 for i in range(0,10)]
# print(list_for_loop)

# Membuat list dengan if (Perbandingan)
# list_if = [i for i in range(0,5) if i % 2 == 0]
# print(list_if)


# Manipulasi List
# data = ["Adi", "Satria", "Bambang"]
# data_angka = [1,3,6,8,5,2,4,5,7,5,3,9,1,0]
# print(data[1])
# print(data[-2])

# jumlah_data_barang = data_angka.count(3)
# print(f"Jumlah data 3 adalah : {jumlah_data_barang}")

# mencari_index = data.index("Adi")
# print(f"Mencari data Adi pada index : {mencari_index}")

# data_angka.sort()
# print(f"Mengurutkan data menjadi : {data_angka}")

# data_angka.reverse()
# print(f"Mengurutkan dari belakang : {data_angka}")


# Menduplikat list
# data_list = ["Faris", "Yahya", "Daffa", "Riady"]
# jumlah = len(data_list)
# print(jumlah)

# data_list2 = data_list
# print(f"Data 1 menjadi : {data_list}")
# print(f"Data 2 menjadi : {data_list2}")

# #Mengcopy data
# data_list3 = data_list2.copy()
# data_list[1] = "Zaira"
# print(f"Data 1 menjadi : {data_list}")
# print(f"Data 2 menjadi : {data_list2}")
# print(f"Data 3 menjadi : {data_list3}")

# #Address
# print(f"Address 1 menjadi : {hex(id(data_list))}")
# print(f"Address 2 menjadi : {hex(id(data_list2))}")
# print(f"Address 3 menjadi : {hex(id(data_list3))}")

# data_list3.sort()
# print(f"Data 1 menjadi : {data_list}")
# print(f"Data 2 menjadi : {data_list2}")
# print(f"Data 3 menjadi : {data_list3}")

# Nested List
# peserta1 = ["Al", 15, "SMA 20"]
# peserta2 = ["Hilmi", 16, "SMA Muhammadiyah"]
# peserta3 = ["Huzaif", 17, "MAN Insan"]

# list_peserta = [peserta1, peserta2, peserta3]
# print(f"Berikut list peserta : {list_peserta}")

# i = 0
# Dirapihkan menggunakan for
# print("Data dirapihkan")
# for peserta in list_peserta[i]:
#     print(f"Peserta ke {i} adalah {list_peserta[i]}")
#     i+=1

# print("\nLebih rapiih lagi")
# for peserta in list_peserta:
#     print(f"Nama\t : {list_peserta[i][0]}")
#     print(f"Umur\t : {list_peserta[i][1]}")
#     print(f"Sekolah\t : {list_peserta[i][2]} \n")
#     i+=1


# Deep Copy
# data1 = [1,2]
# data2 = [3,4]

# all_data = [data1, data2, 10]
# print("Tampilkan semua data")
# print(all_data, "\n")

# all_data_copy = all_data.copy()
# print(f"Data asli : {all_data}")
# print(f"Data copy : {all_data_copy}")

# all_data[0][1] = 5
# print("\nGanti data 1")
# print(f"Data asli : {all_data}")
# print(f"Data copy : {all_data_copy}")

# from copy import deepcopy
# all_data_deepcopy = deepcopy(all_data)
# print("\nTambah data deep copy ")
# print(f"Data asli\t : {all_data}")
# print(f"Data copy\t : {all_data_copy}")
# print(f"Data deepcopy\t : {all_data_deepcopy}")

# print("\nAdress ")
# print(f"Address asli menjadi\t : {hex(id(all_data))}")
# print(f"Address copy menjadi\t : {hex(id(all_data_copy))}")
# print(f"Address deepcopy menjadi : {hex(id(all_data_deepcopy))}")

# print("\nData ke 0 ")
# print(f"Data asli\t : {all_data[0]}")
# print(f"Data copy\t : {all_data_copy[0]}")
# print(f"Data deepcopy\t : {all_data_deepcopy[0]}")

# print("\n Address index ke 0")
# print(f"Address asli menjadi\t : {hex(id(all_data[0]))}")
# print(f"Address copy menjadi\t : {hex(id(all_data_copy[0]))}")
# print(f"Address deepcopy menjadi : {hex(id(all_data_deepcopy[0]))}")

# all_data[0][0] = 9
# print("\nData ke 0 diganti 9 menjadi ")
# print(f"Data asli\t : {all_data[0]}")
# print(f"Data copy\t : {all_data_copy[0]}")
# print(f"Data deepcopy\t : {all_data_deepcopy[0]}")
# print("Data deepcopy tidak berubah semudah itu")


# list Comprehension (Looping mudah)
# print("List Comprehension")
# data = ["ading", 1, 2, 3, "lolly"]
# [print(f"Data : {i}") for i in data]

# #Enumerate
# print("\nEnumerate")
# for index, data in enumerate(data):
#     print(f"Index : {index}, data = {data}")



# Program Sederhana List Buku
# list_buku = []

# while True:
#     judul_buku = input("Masukan judul buku \t:")
#     penerbit = input("Masukan Nama Penerbit \t:")
#     buku = [judul_buku, penerbit]
#     list_buku.append(buku)


#     print("\n", 20*"=")
#     for index, buku in enumerate(list_buku):
#         print(f"|{index+1} \t{buku[0]} \t{buku[1]}")
#         i+=1

#     selesai = input("Ingin tambah buku? (y/n) :")
#     if selesai == "n":
#         break



# Tuples
# Merupakan data tetap dengan ciri khas "()"
# data_tuple = ("Koko", "Kiki", "Kaka")
# data_tuple[1] = "kunyuk"
# print(data_tuple[1])



# Set
# Merupakan data yang tidak memiliki index
# data_tuple = {"Koko", "Kiki", "Kaka"}
# print(data_tuple)



# Dictionary
# data = ["yaya", "yiyi", "yuyu"]
# data_dictionary = {
#     'key' : 'value',
#     'ahm' : 'Ahmad',
#     'ss' : 'Susi',
#     'll' : data
# }

# print(data_dictionary["ahm"])
# print(data_dictionary["ss"])
# print(data_dictionary["ll"])



# Operasi Dictionary
# data_dictionary = {
#     'sai' : 'Saiful',
#     'ahm' : 'Ahmad',
#     'ss' : 'Susi',
# }

# LENDICT = len(data_dictionary)
# print(f"Panjang dictionary : {LENDICT}")

# KEY = "sai"
# CHECKKEY = KEY in data_dictionary
# print(f"Apakah {KEY} ada di data : {CHECKKEY}")

# print("Penggunaan get pada data dictionary")
# print(data_dictionary["sai"])
# print(data_dictionary.get("sai"))
# print(data_dictionary.get("loy", "ora ono"))

# #Update
# data_dictionary.update({"lol" : "lolly pop"})
# print(f"Data biasa :{data_dictionary}")
# data_dictionary.update({"gih" : "galih"})
# print(f"Data update :{data_dictionary}")

# Delete
# del data_dictionary["gih"]
# print(f"Setelah dihapus :{data_dictionary}")

# Mengecek isi dari Dictionary
# data_dictionary = {
#     'sai' : 'Saiful',
#     'ahm' : 'Ahmad',
#     'ss' : 'Susi',
# }

# for mhw in data_dictionary:
#     print(mhw)

# cara = data_dictionary.keys()
# print(cara)

# for mhw in data_dictionary.keys():
#     print(data_dictionary.get(mhw))

# #atau
# for value in data_dictionary.values():
#     print(value)

# #Items
# for item in data_dictionary.items():
#     print(item)

# #Gabungan
# for mhw, value in data_dictionary.items():
#     print(f"Key : {mhw}, Value : {value}")

# #Pop
# print("POP")
# data_dictionary["ahm"] = "aham"
# print(data_dictionary)

# friends = data_dictionary.pop("ahm")
# print(f"Data : {data_dictionary}")
# print(f"Data Pop : {friends}")

# #Popitem
# print("POP ITEM")
# data_dictionary["ahm"] = "aham"
# print(data_dictionary)

# friends = data_dictionary.popitem()
# print(f"Data : {data_dictionary}")
# print(f"Data Pop : {friends}")



# Multi keys dan Nesting Dictionary
# Program Database Mahasiswa
# import datetime

# print("PROGRAM NGEDATA MAHASISWA")
# print(30*"=", "\n")

# mahasiswa1 = {
#     'nama' : 'Khalif',
#     'masuk' : 27,
#     'beasiswa' : True,
#     'lahir' : datetime.datetime(2005, 2, 23)
# }

# mahasiswa2 = {
#     'nama' : 'yahya',
#     'masuk' : 23,
#     'beasiswa' : False,
#     'lahir' : datetime.datetime(2001, 5, 13)
# }

# data_mahasiswa = {
#     'mhw01' : mahasiswa1,
#     'mhw02' : mahasiswa2
# }

# print(f"{'KEY':<6} {'NAMA':<15} {'MASUK':<6} {'BEASISWA':<10} {'LAHIR':<6}")
# print(50*"-")

# for mahasiswa in data_mahasiswa:
#     KEY = mahasiswa

#     NAMA = data_mahasiswa[KEY]['nama']
#     JOIN = data_mahasiswa[KEY]['masuk']
#     BEASISWA = "Beasiswa" if data_mahasiswa[KEY]['beasiswa'] else "None"
#     LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
     
#     print(f"{KEY:<6} {NAMA:<15} {JOIN:^6} {BEASISWA:^8} {LAHIR:^15}")



# Fromkeys
# Latihan Dictionary 1
# import datetime
# import os

# os.system("cls")

# tamplate_mahasiswa = {
#     'nama' : 'none',
#     'nim' : 'none',
#     'sks_lulus' : 'none',
#     'lahir' : datetime.datetime(1111, 1, 11)
# }

# data_mahasiswa = {}
# print(f"BERIKUT DATA MAHASISWA")
# print(30*"-")

# mahasiswa = dict.fromkeys(tamplate_mahasiswa)
# print(mahasiswa)

# mahasiswa["nama"] = input("Masukan Nama Mahasiswa :")
# mahasiswa["nim"] = input("Masukan NIM Mahasiswa :")
# mahasiswa["sks_lulus"] = input("Masukan SKS lulus Mahasiswa  :")
# TAHUN_LAHIR = int(input("Masukan Tahun lahir anda : "))
# BULAN_LAHIR = int(input("Masukan bulan lahir anda : "))
# HARI_LAHIR = int(input("Masukan hari lahir anda : "))
# mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR(1-12), HARI_LAHIR(1-30))

# print(mahasiswa)



# Latihan Dictionary 2
# import os
# import datetime
# import random
# import string

# data_mahasiswa = {}
# mahasiswa_template = {
#     "nama": "None",
#     "nim": "00000",
#     "sks": "None",
#     "ttl": datetime.datetime(1111,1,11) 
# }

# while True:
#     os.system("cls")

#     mahasiswa = dict.fromkeys(mahasiswa_template)
#     mahasiswa["nama"] = input("Masukan Nama Mahasiswa :")
#     mahasiswa["nim"] = input("Masukan NIM Mahasiswa :")
#     mahasiswa["sks"] = input("Masukan SKS Mahasiswa  :")
#     TAHUN_LAHIR = int(input("Masukan Tahun lahir anda : "))
#     BULAN_LAHIR = int(input("Masukan bulan lahir anda (1-12): "))
#     HARI_LAHIR = int(input("Masukan hari lahir anda (1-30): "))
#     mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, HARI_LAHIR)
    
#     KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
#     data_mahasiswa.update({KEY:mahasiswa})

#     print(f"{"KEY":<10} {"NAMA":<10} {"NIM":<10} {"SKS":<10} {"ttl":^10}")  
#     for mahasiswa in data_mahasiswa:
#         KEY = mahasiswa

#         NAMA = data_mahasiswa[KEY]['nama']
#         NIM = data_mahasiswa[KEY]['nim']
#         SKS = data_mahasiswa[KEY]['sks']
#         LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")      
#         print(f"{KEY:<10} {NAMA:<10} {NIM:<10} {SKS:<10} {LAHIR:<10}")

#     print("\n")
#     beres = input("Apa sudah beres? y/n :")
#     if beres == "y":
#         break

# print("\n\nSELESAI")




# FUNGSIIIII
# def hello_world():
#     print("Hello World!!!")

# hello_world()

# def coba_input(angka1, angka2):
#     hasil = angka1 +angka2
#     print(hasil)

# coba_input(1,3)

# def isi_list(list_peserta):
#     data_peserta = list_peserta.copy()
#     for peserta in data_peserta:
#         print(f"Nama : {peserta}")

# anggota = {"Umar", "Faris", "Yahya"}
# isi_list(anggota)

# Repeat / Return (Kembalian)
# def kuadrat(angka_kuadrat):
#     hasil = angka_kuadrat**2
#     return hasil

# y = kuadrat(5)
# print(y)

# hasil = int(input("Masukan Pangkat :"))
# akhir = kuadrat(hasil)
# print(akhir)

# Return banyak
# def coba_return_banyak(angka1, angka2):
#     tambah = angka1 + angka2
#     kurang = angka1 - angka2
#     kali = angka1 * angka2
#     bagi = angka1 / angka2
#     return tambah,kurang,kali,bagi

# angka1 = int(input())
# angka2 = int(input())
# t,k,l,b = coba_return_banyak(angka1, angka2)
# print(t)
# print(k)
# print(l)
# print(b)

# Mengganti inputan dan memprioritaskan
# def ubah_inputan(nama, pesan="Apss Kabss Brooo"):
#     print(f"haii {nama}, {pesan}")

# ubah_inputan("menk")
# ubah_inputan("Jai", "Kunaon sia?")

# def tambah(tambah1=1, tambah2=2, tambah3=3 , tambah4=4):
#     hasil = tambah1 + tambah2 + tambah3 + tambah4
#     return hasil

# print(tambah())
# print(tambah(tambah3=4))



# Latihan1
# import os

# def header():
#     os.system("cls")

#     print(f"{'PROGRAM MENGHOTUNG LUAS' :^40}")
#     print(f"{'DAN KELILING PERSEGI PANJANG' :^40}")
#     print("-"*40, "\n")

# def input_user():
#     panjang = int(input("Masukan panjang :"))
#     lebar = int(input("Masukan lebar :"))
#     return panjang, lebar

# def luas_persegi_panjang(panjang, lebar):
#     return panjang*lebar

# def keliling_persegi_panjang(panjang, lebar):
#     return 2*(panjang+lebar)

# def display(luas, keliling):
#     print(luas)
#     print(keliling)

# while True:

#     header()
#     option = int(input("Pilih salah satu :\n1. Hitung Luas \n2. Hitung Keliling \n3. Hitung Luas dan Keliling\nPilih nomer :"))
#     PANJANG, LEBAR = input_user()

#     if option == 1: 
#         LUAS = luas_persegi_panjang(PANJANG, LEBAR)
#         print(LUAS)
#     elif option == 2:
#         KELILING = keliling_persegi_panjang(PANJANG, LEBAR)
#         print(KELILING)
#     elif option == 3:
#         LUAS = luas_persegi_panjang(PANJANG, LEBAR)
#         KELILING = keliling_persegi_panjang(PANJANG, LEBAR)
#         display(LUAS, KELILING)    
#     else:
#         print("Terima kasih")
#         break

#     keluar = input("Lagi? y / n :")
#     if keluar == "n":
#         print("Terima kasih")
#         break


# Penggunaan Type hint
# import string

# def fungsi_dengan_hint(argument:int):
#     output = 10**argument
#     return output

# hasil = fungsi_dengan_hint(2)
# print(hasil)

# Penggunaan *args
# def data_orang(*args):
#     nama = args[0]
#     berat = args[1]
#     tinggi = args[2]
#     print(f"Si {nama} memiliki berat {berat} dan tinggi {tinggi}")

# data_orang("Yoyo",40,160)

# def data_berat(*data):
#     output = 0
#     for i in data:
#         output+=i
#     return output

# hasil = data_berat(1,2,3,4,5,6,7)
# print(hasil)




# #Penggunaan **kwargs
# def fungsi(nama, tinggi, berat):
#     print(f"Si {nama} memiliki berat {berat} dan tinggi {tinggi}")

# fungsi("Ucup", 50, 160)

# def fungsi_kwargs(**kwargs):
#     print(kwargs) #{'nama': 'Dadang', 'berat': 60, 'tinggi': 190}
#     print(kwargs["nama"]) #Dadang

# fungsi_kwargs(nama="Dadang", berat=60, tinggi=190)
# # bonus kwargs adalah memiliki keyword pada setiap elemennya, misal :

# def fungsi_kwargs(**kwargs):
#     nama = kwargs["nama"]
#     berat = kwargs["berat"]
#     tinggi = kwargs["tinggi"]
#     print(f"Si {nama} memiliki berat {berat} dan tinggi {tinggi}")
    
# fungsi_kwargs(nama="Dadang", berat=60, tinggi=190)

# Contoh lain
# def math(*args, **kwargs):
#     output=0
#     if kwargs["option"] == "Tambah":
#         for angka in args:
#             output+=angka
#     elif kwargs["option"] == "Kurang":
#         for angka in args:
#             output-=angka            
#     elif kwargs["option"] == "Kali":
#         output=1
#         for angka in args:
#             output*=angka
#     elif kwargs["option"] == "Bagi":
#         output=40
#         for angka in args:
#             output/=angka
#     else:
#         print("Tengkiyau")
#     return output

# hasil = math(1,2,3,4,5, option = "Tambah")
# print(hasil)
# hasil1 = math(40,2,3, option = "Kurang")
# print(hasil1)
# hasil2 = math(1,2,3, option = "Kali")
# print(hasil2)
# hasil3 = math(20,2,2, option = "Bagi")
# print(hasil3)




# Lambda
# kuadrat = lambda angka:angka**2
# print(f"Hasil kuadrat dari angka 5 adalah {kuadrat(5)}")

# inputan = int(input("Masukan angka kuadrat :"))
# print(f"Hasil kuadrat dari {inputan} adalah {kuadrat(inputan)}")

# number = int(input("Masukan angka :"))
# power = int(input("Masukan kuadrat :"))
# pangkat = lambda number,power : number**power
# print(f"Angka {number} pangkat {power} menghasilkan {pangkat(number,power)}")

# Lambda berguna untuk sorting pengganti fungsi
# data_list = ["umay", "aiss", "yahyuy"]
# data_list.sort(key=lambda nama:len(nama))
# print(f"Data list : {data_list}")



# Filter
# Memfilter angka kurang dari
# data_angka = [1,2,1,3,4,3,5,6,7,5]

# def kurang_dari_empat(angka):
#     return angka<4

# data_angka = list(filter(kurang_dari_empat, data_angka))
# print(data_angka)

# Atau menggunakan Lambda
# data_angka = list(filter(lambda x:x<4, data_angka))
# print(data_angka)

# Data genap
# data_genap = [1,2,3,4,5,6,7,8,9]
# data_genap = list(filter(lambda genap:genap%2 == 0, data_genap))
# print(data_genap)

# Atau menggunakan lambda dengan fungsi
# def pangkat(n):
#     return lambda angka:angka**n

# hasil = pangkat(2)
# print(hasil(3))
# print(pangkat(3)(4))




# Global dan Local Scope
# nama_global = "Komenk"

# def coba_global():
#     print(f"Ini variable global : {nama_global}")

# hasil = coba_global()
# print(hasil)

# coba_angka_global = 0
# def angka_global(input):
#     global coba_angka_global
#     hasil = input + coba_angka_global

# input = input(" masukan input :")
# print(input)

# print(coba_angka_global)

# angka = 0
# for i in range(0,5):
#     print(i)
#     angka += i
#     angka_dummy = 0

# if True:
#     angka = 10
#     angka_dummy = 10

# print(angka)
# print(angka_dummy)




# import
# import cobaPrint
# hasil = cobaPrint.matematika(6,4)
# print(hasil)




# Module sederhana
# import cobaPrint
# hasil_tambah = cobaPrint.tambah(1,2,3,4,5)
# hasil_kali = cobaPrint.kali(1,2,3,4,5)
# hasil_pangkat = cobaPrint.pangkat(5)

# print(hasil_tambah)
# print(hasil_kali)
# print(hasil_pangkat(2))

# #Atau
# from cobaPrint import tambah,kali,pangkat
# hasil_tambah = tambah(1,2,3,4,5)
# hasil_kali = kali(1,2,3,4,5)
# hasil_pangkat = pangkat(5)

# print(hasil_tambah)
# print(hasil_kali)
# print(hasil_pangkat(2))

# #Atau
# from cobaPrint import *
# hasil_tambah = tambah(1,2,3,4,5)
# hasil_kali = kali(1,2,3,4,5)
# hasil_pangkat = pangkat(5)

# print(hasil_tambah)
# print(hasil_kali)
# print(hasil_pangkat(2))



# Package
# from coba_package.package_baru import tambah, kali, pangkat

# hasil_tambah = tambah(1,2,3,4,5)
# hasil_kali = kali(5,1,2,3)
# hasil_pangkat = pangkat(2)

# print(hasil_tambah)
# print(hasil_kali)
# print(hasil_pangkat(3))


# Coba init
# import coba_package

# hasil = coba_package.package_baru.tambah(1,2,3,4)
# print(hasil)

# hasil2 = coba_package.kali(1,2,3,4)
# print(hasil2)




# Obrak abrik library
# import datetime

# data_waktu = datetime.datetime.now()
# print(data_waktu)
# print(data_waktu.day)
# print(data_waktu.year)

# print(data_waktu.strftime('%A'))
# print(data_waktu.strftime('%B'))
# print(data_waktu.strftime('%C'))
# print(data_waktu.strftime('%D'))

# from collections import Counter

# data = ["a", "b", "c", "d", "a", "a", "b"]

# data_count = Counter(data)
# print(data_count)
# print(data_count['a'])

# import io

# file = io.open("file_text.text", "r")
# print(file.read())




# GUI -> Graphical User Interface
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# window = tk.Tk()
# window.configure(bg="white")
# window.geometry("500x500")
# window.resizable(False,False)
# window.title("WOYYYYYYYY")

# #Membuat Garis dengan Frame
# NAMA_DEPAN = tk.StringVar()
# NAMA_BELAKANG = tk.StringVar()

# #5 Tombol
# def tombol_click():
#     #print(NAMA_BELAKANG.get())
#     pesan = f"Selamat {NAMA_DEPAN.get()} mendapatkan {NAMA_BELAKANG.get()}"
#     showinfo(title="Whazzup!!", message=pesan)

# input_frame = ttk.Frame(window)
# #Penempatan Grid, Pack, Place
# input_frame.pack(padx=15, pady=15, fill="x", expand=True)

# #Komponen-komponen
# #1. Label nama depan
# #nama_depan_label = ttk.Label(window, text="Umay")
# nama_depan_label = ttk.Label(input_frame, text="Nama depan")
# nama_depan_label.pack(padx=15, pady=15, fill="x", expand=True)


# #2. Entry nama depan
# nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
# nama_depan_entry.pack(padx=15, fill="x", expand=True)


# #3. Label nama Belakang
# #nama_belakang_label = ttk.Label(window, text="Umay")
# nama_belakang_label = ttk.Label(input_frame, text="Nama belakang")
# nama_belakang_label.pack(padx=15, fill="x", expand=True)


# #4. Entry nama belakang
# nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
# nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)

# nama_belakang_entry.pack(padx=15, pady=15, fill="x", expand=True)

# tombol_done = ttk.Button(input_frame, text="Done", command=tombol_click)
# tombol_done.pack(padx=10, pady=10, fill='x', expand=True)



# window.mainloop()


# import numpy as np
# import numpy as np

# list_a = [1,2,3,4]
# vektor_a = np.array([1,2,3,4])

# print(f"Ini adalah list : {list_a}")
# print(f"Ini adalah np : {vektor_a}")

# print(f"Ini adalah list : {list_a}")
# print(f"Ini adalah np : {vektor_a**2}")

# matriks_a = ([(1,2),(3,4)])
# print(f"ini adalah matriks_a :\n {matriks_a}")

# matriks_b = ([(1,2,3),(4,5,6),(7,8,9)])
# print(f"ini adalah matriks_b :\n {matriks_b}")

# zeroes_c = np.zeros((3,3))
# print(zeroes_c)

# ones_d = np.ones((2,2))
# print(ones_d)

# jumlah_a= ones_d + matriks_a
# print(jumlah_a)

# jumlah_b = matriks_b - zeroes_c
# print(jumlah_b)

# import pygame

# initial
# pygame.init()

# Variable running game
# isRun = True

# #Membuat Display
# window_lebar = 500
# window_panjang = 500
# window = pygame.display.set_mode((window_lebar,window_panjang))

# #Object game
# #Koordinat
# x = 250
# y = 250

# #Ukuran
# panjang = 20
# lebar = 20

# #Kecepatan
# speed = 10

# while isRun:
#     pygame.time.delay(10)
#     #User Input
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             isRun = False

#     #ambil semua keyboard press
#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_LEFT] and x > 0:
#         x -= speed
#     if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
#         x += speed
#     if keys[pygame.K_DOWN] and y < window_panjang-panjang:
#         y += speed
#     if keys[pygame.K_UP] and y > 0:
#         y -= speed

#     window.fill((255,255,255))
#     pygame.draw.rect(window,(0,0,255), (x,y,panjang,lebar))
#     pygame.display.update()

# pygame.quit()




# Membaca File Txt dari data.txt

# file = open("data.txt",mode="r")

# Menanyakan apakah bisa dibaca atau ditulis
# print(f"Status read : {file.readable()}")
# print(f"Status write : {file.writable()}")

# Baca seluruh baris
# print(file.read())

# Baca satu baris
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")

# Baca sebagai list
# print(file.readlines())

# print(f"Apakah file sudah di close? {file.closed}")
# file.close()
# print(f"Apakah file sudah di close? {file.closed}")


# Salah  satu teknik membuka file dengan "With"
# with open("data.txt", mode="r") as file:
#     content = file.readline()
#     print(content, end="")
#     print(f"Apakah file sudah di close? {file.closed}")

# print(f"Apakah file sudah di close? {file.closed}")
    



# Write
# with open("data.txt", 'w', encoding="utf-8") as file:
#     file.write("Kunyuk\n")
    
# with open("data.txt", 'a', encoding="utf-8") as file:
#     file.write("Faris\n")
#     file.write("Lolly\n")

# with open("data.txt","r+", encoding="utf-8") as file:
#     file.write("Yahyuy yuyoy") #r+ untuk mennimpa isi sebelumnya dan mengabaikannya


# Nyoba mengganti data di baris ter tentu, namun masih error
# def update_line(file_path, line_number, new_content) :
#     with open (file_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()

#     if 0 <= line_number < len(lines):
#         lines(line_number) = new_content + '\n'
#     else:
#         print("Nomor baris tidak ada")

#     with open(file_path, 'w', encoding="utc-8") as file:
#         file.writelines(lines)

# file_path = "data.txt"
# line_number = 1
# new_content = "Kunci"
# update_line(file_path, line_number, new_content)



# Contoh menangkap exception
# from math import nan

# input_user = int(input("Masukan angka : "))
# hasil = nan

# try:
#     hasil = 10/input_user
# except:
#     print("input tidak boleh 0")

# print(f"Hasil : {hasil}")


# Contoh di aplikasi dengan try and except
# while True:
#     angka = int(input("Masukan angka :"))
#     try :
#         hasil = 10/angka
#         print(f"Hasil : {hasil}")
#         inputan = input("Apakah mau lanjut? y/n :")
#         if inputan == "n":
#             break
#     except :
#         print("Angka  tidak boleh 0")
# print("Terima kasih")

# while (True):
#     try:
#         with open("data.txt", "r") as file:
#             print(file.read())
#         break
#     except:
#         print("FIle tidak ditemukan, buat file baru")
#         with open("data.txt", "w", encoding="utc-8") as file:
#             file.write("file baru")
#         break
# print("Thanks")




# Project Database dan Read
