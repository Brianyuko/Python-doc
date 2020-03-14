text1 = 'Jalan - jalan di hari minggu'
text2 = 'Jalan - jalan di hari jum\'at' #Menggunakan \ untuk ' didalam petik 1
text3 = "Jalan - jalan di hari jum'at"
text4 = 'Arip berkata, "Kemarin kemana bro?"'
text5 = "Nani menjawab, \" ke Bioskop \""
text6 = 'Arip berkata, "Kemarin kemana bro?" \n Nani menjawab "Ke bioskop"'
text7 = """
Arip : "Kemarin kemana bro?"
Nani : "Ke bioskop"
"""
text8 = r'/home/lazyturtle' #raw string
print(text8)
print(5*"wk")
kueA = 'Bolu'
print('Kue' 'Bolu')
print('Kue ' +kueA)

#Slicing Text
text9 = 'Hero 57'
a = text9[0:4] # Mengambil char dari text, dari index 0 sampai index 4
b = text9[0:] # Mengambil char, dari index 0 sampai index terakhir
c = text9[-2] # Mengambil char, dari 2 index terakhir dari text
print(a)
print(b)
print(c)