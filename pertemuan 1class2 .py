class hewan:
    def __init__(self,nama):
        self.nama = nama

    def suara(self):
        pass

class kucing(hewan):
    def suara(self):
        return ('Meow')

class anjing(hewan):
    def suara(self):
        return ('Guk guk')
        
class ayam(hewan):
    def suara(self):
        return ('Kukuruyuk')
    
Kucing = kucing('wahyu')
Anjing = anjing('pandu')
Ayam   = ayam('jibral')

print(f'{Kucing.nama} bersuara {Kucing.suara()}')
print(f'{Anjing.nama} bersuara {Anjing.suara()}')
print(f'{Ayam.nama} bersuara {Ayam.suara()}')