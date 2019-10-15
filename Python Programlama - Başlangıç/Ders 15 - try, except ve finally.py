"""
while True:
    try: # Dene
        sayı1 = int(input("Lütfen 1. sayıyı giriniz = "))
        sayı2 = int(input("Lütfen 2. sayıyı giriniz = "))

        sayı3 = sayı1 / sayı2
        print(sayı3)
    except ValueError as VE: # Yanlış değer girme hatası. int bekler str girme gibi
        continue
    except ZeroDivisionError as ZDE: # 0 a bölme hatası
        print("Girdiğiniz sayı2 değeri 0 olamaz. Aldığınız Hata Mesajı = " + str(ZDE))
    except: # Tüm hatalar için
        print("GİRDİĞİNİZ DEĞERLERDE BİR SORUN VAR LÜTFEN KONTROL EDİN !!")
    finally: # Her türlü çalışır
        break
"""


import tensorflow
