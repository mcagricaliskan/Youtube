"""
# Araba
# Hız, Modeli, Markası, Koltuk Sayısı


class BizimSınıfımız:
    def __init__(self,Marka,Model,Hız,KoltukSayısı):
        self.ArabaHız = Hız
        self.ArabaModel = Model
        self.ArabaMarka = Marka
        self.ArabaKoltuk = KoltukSayısı

    def ArabaYazdır(self):
        print(self.ArabaHız)
        print(self.ArabaMarka)
        print(self.ArabaModel)
        print(self.ArabaKoltuk)



BMW5 = BizimSınıfımız("BMW","5","200","4")
TeslaM1 = BizimSınıfımız("Tesla","M1","250","2")


#BMW5.ArabaYazdır()
#BMW5.ArabaHız = 300
#BMW5.ArabaYazdır()

TeslaM1.ArabaYazdır()
TeslaM1.ArabaKoltuk = 3
print("########################")
TeslaM1.ArabaYazdır()"""


class İnsan:
    def __init__(self,Adı,Soyadı,Boyu,Kilosu,Yaşı,Memleketi):
        self.Ad = Adı
        self.Soyad = Soyadı
        self.Boy = Boyu
        self.Kilo = Kilosu
        self.Memleket = Memleketi

    def Yazdir(self):
        print(self.Ad)
        print(self.Soyad)
        print(self.Boy)
        print(self.Kilo)
        print(self.Memleket)

    def VücutKitleİndeksi(self):
        self.Kitleİndeksi = self.Kilo / ((self.Boy/100)**2)
        print(self.Ad + " Kişisinin Vücut Kitle İndeksi = " + str(self.Kitleİndeksi))


Ahmet = İnsan("Ahmet","Mert",180,80,25,"İzmir")
Ayşe = İnsan("Ayşe","Mert",160,70,20,"Aydın")


Ahmet.VücutKitleİndeksi()
##############
Ayşe.VücutKitleİndeksi()

Ayşe.Soyad = "Doğan"
Ayşe.Yazdir()