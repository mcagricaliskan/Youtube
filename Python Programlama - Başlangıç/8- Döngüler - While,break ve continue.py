#
#
#
# while True:
#     print("*")
#     print(" *")
#     print("  *")
#     print(" *")
#     print("*")

i = 0
# DonguKontrol = True
# break döngüleri kırar ve bitirir.
# continue



# while True:
#     i = i + 1
#     print(i)
#     if i == 800000:
#         print("Yeter Artık")
#         break

#
# while True:
#     i += 1 # i += 1
#     if i % 2 == 1:
#         continue
#
#     print(i)


kullanici_Adi = "mehmet"
sifre = "12345"


while True:
    girilen_kullanici_adi = input("Lütfen bir kullanıcı adı giriniz. = ")
    continue
    girilen_sifre = input("Lütfen şifrenizi giriniz. = ")

    if kullanici_Adi == girilen_kullanici_adi and sifre == girilen_sifre:
        print("Giriş Başarılı")
        break
    elif kullanici_Adi == girilen_kullanici_adi and sifre != girilen_sifre:
        print("Girdiğiniz şifre yanlış.")
    else:
        print("Böyle bir kayıtlı kullanıcı bulunmamaktadır.")





