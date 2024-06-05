class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Tentara(Manusia):
    def peranan(self):
        print(f"Nama saya adalah: {self.nama}\nPekerjaan saya adalah: Tentara\nUmur saya adalah: {self.umur}")

class Dokter(Manusia):
    def peranan(self):
        print(f"Nama saya adalah: {self.nama}\nPekerjaan saya adalah: Dokter\nUmur saya adalah: {self.umur}")

class Petani(Manusia):
    def peranan(self):
        print(f"Nama saya adalah: {self.nama}\nPekerjaan saya adalah: Petani\nUmur saya adalah: {self.umur}")

tentara = Tentara("Andi", 35)
tentara.peranan()

dokter = Dokter("Citra", 40)
dokter.peranan()

petani = Petani("Dewi", 45)
petani.peranan()
