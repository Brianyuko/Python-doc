#Sintaks dasar di python

# Statement (Pernyataan) di python
# Semua perintah yang bisa dieksekusi oleh Python disebut STATEMENT

# Statement 1 baris
panjang1 = 5
panjang2 = 3
panjang3 = 3
panjang4 = 4
#Statemen Multibaris
a = panjang1 + panjang2 + \
    panjang3 + \
        panjang4
print(a)

#Statement yang ada didalam tanda kurung [], {}, () tidak memerlukan tanda \
nama_bulan = ['Januari', 'Maret', 'Juni']
print(nama_bulan)


#Baris dan indentasi
# Python tidak menggunakan tanda {} untuk menandai blok/grup kode
# Blok kode di python menggunakan tanda indentasi (spasi)
# Jumlah spasi untuk setiap baris yang ada dalam satu blok kode harus sama
nilai = 20
if nilai <= 5:
    print('Nilai merah dan tidak lulus')
else:
    print('Nilai biru dan lulus')

#Contoh indentasi yang salah
if True:
    print('Jawab') 
#  print('Jawab') # Ini akan error, karena indentasi tidak sama
else:
    print('Jawab salah')

#Tanda kutip di Python
# Python menggunakan tanda kutip tunggal ('), ganda ("), maupun triple (''' atau """)
# Tanda kutip untuk menandai string, sepanjang awal sampai akhir tanda kutip
Kata = 'Kata'
kalimat = "ini adalah kalimat"
paragraf = """ini adalah paragraf. Yang terdiri
dari beberapa baris"""
print(paragraf)

#Komentar di python
# Tanda Pagar # digunakan untuk menandai komentar di python.
# Komentar tidak akan diproses oleh interpreter Python.
# Komentar hanya berfungsi untuk memudahkan programmer memahami maksud dari kode
