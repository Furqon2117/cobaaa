class Manusia :
    def __init__(self, nama,umur):
        self.nama = nama
        self.umur = umur

    def sapa(self):
        print(f"Halo, nama saya {self.nama} dan umur saya {self.umur}" )
        
Manusia1 = Manusia('Budi', 20)
Manusia2 = Manusia('Andi', 22) 

Manusia1.sapa()
Manusia2.sapa()
