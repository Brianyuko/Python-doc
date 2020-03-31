from player import Player

class Search(Player):
      
    def cari_tinggi(height):
        nama = []
        
        for players in Player.daftar_pemain:
            if players.get_height() > height:
                nama.append(players)
                
        return nama