


"""


Contine Devam
break kır


"""


"""


donguDurumu = True
sayaç = 0




while donguDurumu:
    print("Merhaba")
    sayaç+= 1  # sayaç = sayaç + 1 in kısaltılmış hali
    if sayaç == 100:
        print(sayaç)
        donguDurumu = False
    



kullanaciAdi = "Kemal"
şifre = "1234"





while True:
    
    girilenKA = input(" Kullanıcı Adını Giriniz = ")
    girilenS = input(" Şifreyi Giriniz = ")
    
    
    if (girilenKA == kullanaciAdi) and (girilenS == şifre): # and iki kuralı birden çalıştırmak için ve bağlacı , or 2 kuraldan birinin sağlanması yeterli
        print("Hoşgeldiniz.")
        break
    elif girilenKA == kullanaciAdi and girilenS != şifre: # != eşit olmama durumunu sorgular
        print("Şİfreniz yanlış. Lütfen Tekrar Deneyin")
    else:
        print(" Böyle bir üyelik bulunumaadı.")
    
    
"""







sayaç = 0

while True:
    sayaç+= 1
    
    if sayaç == 100:
        continue
    
    
    if sayaç % 2 == 0: # % mod almaya yarar.
        print(sayaç)
            
    if sayaç == 100:
        break
    










































