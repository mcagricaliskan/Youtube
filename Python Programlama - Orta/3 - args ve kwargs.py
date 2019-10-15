"""
def main(*args):
    print(type(args))
    #print(args)
    for arg in args:
        print(arg)


main("Merhaba","Bu","Benim","Youtube","Kanalım",5,6,7)


def main(Başlık, **kwargs):
    print(Başlık)
    #print(type(kwargs))
    #print(kwargs)
    for key,deger in kwargs.items():
        print("Anahtar Kelime = {} ve Değer = {}".format(key,deger))


main("Argümanlar Listesi = ", Yazı1 = "Merhaba", Yazı2 = "Selamlar", Sayı1 = 10)"""


class İnsan:
    def __init__(self,Boy,Kilo,İsim):
        self.Boy = Boy
        self.Kilo = Kilo
        self.İsim = İsim
    def Yazdir(self):
        print(self.Boy)
        print(self.Kilo)
        print(self.İsim)


class Cocuk(İnsan):
    def __init__(self,*args):
        super().__init__(*args)


Mehmet = Cocuk(180,80,"Mehmet")
Mehmet.Yazdir()