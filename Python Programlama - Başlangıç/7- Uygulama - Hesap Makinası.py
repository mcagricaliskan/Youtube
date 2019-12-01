# kullanıcıdan 2 tane sayı alınacak #input()

# kullanıcıdan bir işlem girmesi istenecek #if ile kontrol

# bu işlem sonucu çıkan değer ekrana bastırılacak  # print()


sayi1 = int(input("Lütfen 1. sayıyı giriniz = "))
sayi2 = int(input("Lütfen 2. Sayıyı Giriniz = "))

işlem = input("Lütfen yapmak istediğiniz işlemi giriniz. (Toplama, Çıkartma, Çarpma, Bölme, ÜstAl) Lütfen yapmak istediğiniz işlemi seçiniz.")


if işlem == "Toplama":
    print(sayi1+sayi2)
elif işlem == "Çıkartma":
    print(sayi1-sayi2)
elif işlem == "Çarpma":
    print(sayi1*sayi2)
elif işlem == "Bölme":
    print(sayi1/sayi2)
elif işlem == "ÜstAl":
    print(sayi1**sayi2)