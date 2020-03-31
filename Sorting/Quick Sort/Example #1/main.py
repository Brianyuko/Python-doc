from player import Player
from sorting import Sorting
from searching import Search

#data pemain Real Madrid
pemain1 = Player('Vinicus Jr.', 25, 176, 73, ['LW'], 73, 77, 65, 10)
pemain2 = Player('Segio Ramos', 4, 184, 82, ['CB'], 79, 74, 86, 11)
pemain3 = Player('Gareth Bale', 11, 185, 82, ['RW, ST, LW'], 92, 90, 76, 6)
pemain4 = Player('Eden Hazard', 7, 175, 74, ['LW, ST'], 82, 83, 88, 8)
pemain5 = Player('Karim Benzema', 9, 185, 81, ['CF'], 83, 81, 84, 7)
pemain6 = Player('Courtois',1, 199, 96, ['GK'], 56, 19, 27, 86)
pemain_madrid = [pemain1, pemain2, pemain3, pemain4, pemain5, pemain6]

#data pemain Barcelona
pemaina = Player('De Jong', 21, 180, 74, ['CM'], 68, 84, 45, 9)
pemainb = Player('Pique', 3, 194, 85, ['CB'], 62, 58, 69, 8)
pemainc = Player('Griezmann', 17, 176, 73, ['CF, ST, LW'], 82, 86, 86, 14)
pemaind = Player('Messi', 10, 170, 72, ['RW', 'ST', 'CF'], 86, 93, 75, 8)
pemaine = Player('Suarez', 9, 182, 86, ['ST'], 88, 86, 83, 37)
pemainf = Player('Ter Stegen', 1, 187, 85, ['GK'], 66, 18, 25, 90)
pemain_barca = [pemaina, pemainb, pemainc, pemaind, pemaine, pemainf]

daftar_pemain = Player.daftar_pemain

Tinggi = [[],[]]
Berat = [[],[]]

for players in daftar_pemain:
    Tinggi[1].append(players.get_height())
    Tinggi[0].append(players.get_name())
    Berat[1].append(players.get_weight())
    Berat[0].append(players.get_name())
    
Sorting.quick_sort(Tinggi,0,len(Tinggi[1])-1)
Sorting.quick_sort(Berat,0,len(Berat[1])-1)

print('\nMengurutkan Berdasarkan Tinggi')
for a,b in zip(Tinggi[0],Tinggi[1]):
    print("nama : {} \nTinggi : {}".format(a,b))

print('\nMengurutkan Berdasarkan Berat')
for a,b in zip(Berat[0],Berat[1]):
    print("nama : {} \nBerat : {}".format(a,b))

a = Search.cari_tinggi(180)
print("\nPemain dengan Tinggi diatas 180: ")
for i in a:
    print(i)