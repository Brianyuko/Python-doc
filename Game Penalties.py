from random import randint
class Player():
    jumlah = 0
    def __init__(self, Name, Number, Height, Weight, Position, shotPower, Curve, Penalties, gkReflexes):
        self.name = Name
        self.number = Number
        self.height = Height
        self.weight = Weight
        self.position = Position
        self.shotpower = shotPower
        self.curve = Curve
        self.penalties = Penalties
        self.gkreflexes = gkReflexes
        Player.jumlah += 1

    @property
    def info(self):
            return '''
            Name : {} \t Number : {} \t Height : {} \t Weight : {} \t Position : {} \t Shot Power : {} \t Curve : {} \t Penalties : {} \t Gk Reflexes : {} \t '''.format(self.name, self.number, self.height, self.weight, self.position, self.shotpower, self.curve, self.penalties, self.gkreflexes)
#Create Team
team1 = str(input("Masukan nama team ke 1: "))
team2 = str(input("Masukan nama team ke 2: "))
print('Team 1 adalah {} dan team 2 adalah {}'.format(team1,team2))
# Create Player
listteam1 = []
print('Create Player Fromm Team {}'.format(team1))
for i in range (0,2): #Bisa memilih sampai index ke berapa saja, saya menggunakan index kecil karena untuk mencoba dahulu supaya inputnya sedikit. Jika index kecil bisa, pasti index besar juga bisa
    listteam1.append( Player(str(input('Masukan Nama: ')), int(input('Masukan Number: ')),int(input('Masukan Height: ')),int(input('Masukan Weight: ')),str(input('Masukan Position: ')), int(input('Masukan Shot Power: ')), int(input('Masukan Curve: ')),int(input('Masukan Penalties: ')), int(input('Masukan gkReflexes: '))))
listteam2 = []
print('Create Player Fromm Team {}'.format(team2))
for i in range (0,2):
    listteam2.append( Player(str(input('Masukan Nama: ')), int(input('Masukan Number: ')),int(input('Masukan Height: ')),int(input('Masukan Weight: ')),str(input('Masukan Position: ')), int(input('Masukan Shot Power: ')), int(input('Masukan Curve: ')),int(input('Masukan Penalties: ')), int(input('Masukan gkReflexes: '))))
#print(pemain_madrid[1].__dict__) cek class
list1 = len(listteam1)
list2 = len(listteam2)
# Start Rules goals
def matchUser1(user): #function untuk input user team 1
    rules = randint(1,9)
    if user == rules:
        print('user {} dan rules {} sama'.format(user, rules))
        print('Lakukan pengecekan')
        print('shot power {}, curve {}, penalties {}'.format(listteam1[i].shotpower, listteam1[i].curve, listteam1[i].penalties))
        print('Gk refleks dari {} adalah {}'.format(listteam1[2].name, listteam1[2].gkreflexes))
        hitung = ((listteam1[i].shotpower + listteam1[i].curve + listteam1[i].penalties)/3) - listteam1[2].gkreflexes
        if hitung <= 10:
            print('Goall')
        else:
            print('Sayang sekali tidak Goal')
    else:
        print('Arah tendangan {}'.format(user))
        print('Arah gooalkeeper {}'.format(rules))
        print('GOALLL!!!')
    return matchUser1
def matchUser2(user): #function untuk input user team 2
    rules = randint(1,9)
    if user == rules:
        print('user {} dan rules {} sama'.format(user, rules))
        print('Lakukan pengecekan')
        print('shot power {}, curve {}, penalties {}'.format(listteam2[i].shotpower, listteam2[i].curve, listteam2[i].penalties))
        print('Gk refleks dari {} adalah {}'.format(listteam2[2].name, listteam2[2].gkreflexes))
        hitung = ((listteam2[i].shotpower + listteam2[i].curve + listteam2[i].penalties)/3) - listteam2[2].gkreflexes
        if hitung <= 10:
            print('Goall')
        else:
            print('Sayang sekali tidak Goal')
    else:
        print('Arah tendangan {}'.format(user))
        print('Arah gooalkeeper {}'.format(rules))
        print('GOALLL!!!')
    return matchUser2
# End Rules Goals
# Start Pilih Pemain
def matchPlayer1(find):
    for i in range(list1):
        if find == listteam1[i].name:
            print('Pemain {} ditemukan'.format(listteam1[i].name))
            break
        else:
            print('Pemain {} tidak ditemukan'.format(find))
    if find == listteam1[i].name:
        matchUser1(int(input('Masukan Arah 1-9: ')))
    elif find != listteam1[i].name:
        print('Pemain TIdak Ketemu')
    return matchPlayer1
def matchPlayer2(find):
    for i in range(list1):
        if find == listteam2[i].name:
            print('Pemain {} ditemukan'.format(listteam2[i].name))
            break
        else:
            print('Pemain {} tidak ditemukan'.format(find))
    if find == listteam2[i].name:
        matchUser2(int(input('Masukan Arah 1-9: ')))
    elif find != listteam2[i].name:
        print('Pemain TIdak Ketemu')
    return matchPlayer2
print('Jumlah Pemain dari kedua tim {}'.format(Player.jumlah))
# End Pilih Pemain
# Main Program
def matchStart(team):
    if team == team1:
        print('\t\t\t\t\t\t\t\t\t\t List Pemain {}'.format(team1))
        for i in range(list1):
            print(listteam1[i].info)
            i += 1
        matchPlayer1(input('Masukan Nama pemain: '))
    elif team != team1:
        print('\t\t\t\t\t\t\t\t\t\t List pemain {}'.format(team2))
        for i in range(list2):
            print(listteam2[i].info)
            i += 1
        matchPlayer2(input('Masukan Nama pemain: '))
matchStart(input('Pilih Team Mana:\n1.{}\n2.{}\nTulis nama team: '.format(team1, team2)))