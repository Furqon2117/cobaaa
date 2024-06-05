class Kendaraan :
    def __init__(self, nama,warna,harga) :
        self.nama = nama
        self.warna = warna
        self.harga = harga
        
    def tampilkan(self):
        print("Rincian: ", self.nama, self.warna, self.harga)

    def kecepatanmaxpertama(self):
        print("Kecepatan maximum kendaraan: ", self.nama, "adalah 150km/jam")
        
    def gantigearpertama(self):
        print("Ganti gear maximum kendaraan sampi 6")


# CHILDREN CLASS
class Mobil(Kendaraan):
    def kecepatanmaxkedua(self):
        print("Kecepatan maximum kendaraan: ", self.nama, "adalah 200km/jam")

    def gantigearkedua(self):
        print("Ganti gear maximum kendaraan adalah sampai 7")

    # object mobil

# memanggil fungsi dari parent class kendaraan
Avanza = Mobil("Avanza", "Putih", 20000000) 
Avanza.tampilkan()
Avanza.kecepatanmaxpertama()
Avanza.gantigearpertama()

# memanggil fungsi dari parent class kendaraan dan children class mobil
Jeep = Mobil("Jeep","Coklat", 30000000)
Jeep.tampilkan()
Jeep.kecepatanmaxkedua()
Jeep.gantigearkedua()