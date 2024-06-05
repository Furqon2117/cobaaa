from abc import ABC, abstractmethod

class Car(ABC):
    def fasilitas(self):
        pass
    def kecepatan(self):
        pass
    def harga(self):
        pass
    def kekuatan(self):
        pass

class BMW(Car):
    def fasilitas(self):
        return "Kursi nyaman"
    def kecepatan(self):
        return "200km/jam"
    def harga(self):
        return "10.000 dollar"
    def kekuatan(self):
        return "Anti-Penyok"
    
class Avanza(Car):
    def fasilitas(self):
        return "Kapasitas muat banyak orang"
    def kecepatan(self):
        return "150km/jam"
    def harga(self):
        return "1.000 dollar"
    def kekuatan(self):
        return "Suspensi Empuk"

class Ferrari(Car):
    def fasilitas(self):
        return "Transmisi automatic"
    def kecepatan(self):
        return "300km/jam"
    def harga(self):
        return "20.000 dollar"
    def kekuatan(self):
        return "Melebihi Kecepatan cahaya"
    
def jenis_mobil(car: Car):
        print("-----------------------------------------------------")
        print(f"Mobil ini memiliki fasilitas: {car.fasilitas()} ")
        print(f"Mobil ini memiliki Kecepatan: {car.kecepatan()} ")
        print(f"Mobil ini harganya : {car.harga()}")
        print(f"Kekuatan mobil ini adalah: {car.kekuatan()}")
        print()


mobil1 = BMW();
mobil2 = Avanza();
mobil3 = Ferrari();

jenis_mobil(mobil1);
jenis_mobil(mobil2);
jenis_mobil(mobil3);

        

