"""

ÖDEV !!!

Hesap Makinesi

kullanıcıdan işlem alacak
işlemi sorgulayacak
kullanıcıdan 2 sayı alacak
kullanıcın verdiği işlemi iki sayı üzerinde uygulayacak
sonucu ekrana yazdır

"""


sayi1 = int(input("1. Sayiyi Giriniz = "))
sayi2 = int(input("2. sayiyi Giriniz = "))

print("Lütfen bu işlemlerden birinizi seçiniz = Toplama,Çıkartma,Çarpma,Bölme")
islem = input("işlemi Giriniz = ")

if islem == "Toplama":
    sayi3 = sayi1 + sayi2
    print(sayi3)
elif islem == "Çıkartma":
    sayi3 = sayi1 - sayi2
    print(sayi3)
elif islem == "Çarpma":
    sayi3 = sayi1 * sayi2
    print(sayi3)
elif islem == "Bölme":
    sayi3 = sayi1 / sayi2
    print(sayi3)
else:
    print("Yanlış Bir İşlem Seçtiniz")
    
    

