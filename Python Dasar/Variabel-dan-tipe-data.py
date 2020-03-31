# Variabel adalah lokasi di memori yang digunakan untuk menyimpan nilai
# Pada saat kita membuat variabel, kita 'memesan', tempat didalam memori.
# Tempat tersebut bisa diisi dengan data atau objek.

# Di python variabel tidak perlu di deklarasikan secara eksplisit
# Deklarasi terjadi secara otomatis pada saat kita memberi (menugaskan) suatu nilai ke variabel
# Tanda = digunakan untuk memberikan nilai ke variabel

# Memberikan nilai variabel
panjang = 100 # Tipe data integer
lebar = 21.5 # Tipe data float
nama = 'Brian' # Tipe data string
print('Nama saya {} panjang saya {} dan lebar {} wkwk'.format(nama, panjang, lebar))

# Multi Penugasan
x = y = z = 3
# Pada contoh diatas, kita menugaskan ketiga variabel untuk menunjuk ke lokasi yang sama yang berisi 3

# Kita juga bisa menugaskan beberapa variabel dan objek, dalam sebaris perintah
a, b, c = 1, 3.4, "Brian"
print('Variabel a {}\nVariabel b {}\nVariabel c {}'.format(a, b, c))

# Tipe Data Python
# Python Memiliki 6 tipe data standar atau paling sering digunakan, yaitu
# Bilangan (number)
# String
# List
# Tuple
# Set
# Dictionary

# Bilangan (number)
# Tipe data bilangan yang umum ada 2 yaitu, integer dan float
# Integer adalah bilangan bulat, dan float adalah bilangan pecahan
# Selain itu ada tipe bilangan lain, yaitu bilangan kompleks, yang memiliki bilangan real dan imajiner.
x = 5
print(x, "tipenya adalah ",type(x)) # Tipe data integer
x = 2.0
print(x, "tipenya adalah ",type(x)) # Tipe data float
x = 1+2j
print(x, "tipenya adalah ",type(x)) # Tipe data complex

# Tipe data integer panjangnya bisa berapa saja, hanya dibatasi oleh besar memori yang tersedia
# Tipe data float akurat sampai 17 angka di belakang koma.

# String
# String adalah tipe data yang anggotanya berurut dan memiliki indeks
# Indeks dimulai dari angka 0 bila mulai depan, dan -1 bila dari belakang
kalimat = "Nama saya Brian"
print(kalimat)      # print string lengkap
print(kalimat[0])   # print karakter pertama
print(kalimat[-1])  # print karakter terakhir
print(kalimat[4:7]) # print dari indeks 4 - 6
print(kalimat[:4])  # print dari indeks 0 - 3
print(kalimat[0:])  # print dari indeks 0 sampai indeks terakhir