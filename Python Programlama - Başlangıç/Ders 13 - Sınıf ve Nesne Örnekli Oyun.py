import random


class Savaşçı:
    def __init__(self,Ad, Gücü, Canı, Savunma, Exp):
        self.Ad = Ad
        self.Güc = Gücü
        self.Can = Canı
        self.Savunma = Savunma
        self.Exp = Exp

    def Yazdir(self):
        print(self.Ad)
        print(self.Güc)
        print(self.Can)
        print(self.Savunma)

    def LevelUp(self):
        self.Savunma+= 5
        self.Güc+= 10

Jack = Savaşçı("Jack", 10, 100, 3,0)
Burak = Savaşçı("Burak", 5 , 200,5,0)

sayac = 0
Saldırı1 = 0
Saldırı2 = 1
while True:
    # SAldırı1
    sayac+= 1
    SaldırıLİstesi = [Saldırı1,Saldırı2]
    Sonuc = random.choice(SaldırıLİstesi)

    if Sonuc == Saldırı1:
        Burak.Can = Burak.Can + Burak.Savunma - Jack.Güc
    elif Sonuc == Saldırı2:
        Jack.Can = Jack.Can + Jack.Savunma - Burak.Güc

    if sayac % 10 == 0:
        Burak.Yazdir()
        Jack.Yazdir()
        Burak.LevelUp()
        Jack.LevelUp()

    if Burak.Can <= 0:
        print("Burak Kaybetti Jack Kazandı")
        break
    elif Jack.Can <= 0:
        print("Jack Kaybetti Burak Kazandı")
        break

