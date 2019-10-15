

"""

Ödev 

dairenin çevresini ve alanını hesaplayan fonksiyon yazın
10 tane daire için bu fonksiyonu for döngüsü ile kullanın
10 dairenin yarı çapları bir listede tutulsun

"""




def Hesapla(yariCap):
    pi = 3.14
    DC = 2*pi*yariCap
    DA = pi*(yariCap*yariCap)
    return DC,DA



Daireler = [5,10,15,20,25,30,35,40,45,50]

for i in Daireler:
    print(Hesapla(i))