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
Kübra = İnsan("Kübra","Mert",160,70,23,"Aydın")
Ahmet.VücutKitleİndeksi()

class Cocuk(İnsan):
    def __init__(self,Adı,Soyadı,Boyu,Kilosu,Yaşı,Memleketi,Oyuncak):
        super().__init__(Adı,Soyadı,Boyu,Kilosu,Yaşı,Memleketi)
        self.Oyuncak = Oyuncak

    def Yazdir(self):
        super().Yazdir()
        print(self.Oyuncak)


Burak = Cocuk("Burak","Mert",30,10,0.5,"İzmir","Araba")
Burak.Yazdir()
Burak.VücutKitleİndeksi()