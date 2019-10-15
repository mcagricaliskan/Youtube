import numpy as np


Dizi1 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])


Dizi2 = np.array([10,11,12])

Dizi3 = np.array([[13,14,15,16],
                  [17,18,19,20],
                  [32,16,108,19],
                  [67,39,48,92]])


print(Dizi3.ndim) # Numpy Matrisinin Kaç boyutlu olduğunu gösterir

print(Dizi3.shape) # Numpy Matrisinin Şeklini Gösterir.

print(Dizi3.size) # Numpy Matrisinin Toplam Eleman sayısı 

print(Dizi1.dtype) # Numpy Matrisinin Tipini Döndürür.




Dizi4 = Dizi1.flatten() # Matrisi düz bir dizi haline getirir

Liste = [1,2,3,4,5]

Dizi5 = np.array(Liste) # Listeyi numpy dizisine çevirir

Liste1 = list(Dizi3) # Numpy dizisini listeye çevirir.

print(Dizi3[1][1])

Dizi6 = np.linspace(0,100,200) # 0 dan 100 e kadar 200 uzunlukta bir dizi yaratır
 
Dizi7 = np.arange(0,100,5)# 0 dan 100 e kadar 5 atlayarak o sayılardan bir dizi yaratır




Dizi8 = Dizi3[1:3,1:3] # : hepsi anlamına gelir, Soluna gelen değerden başlar, sağına gelen değere KADAR gider.



Dizi9 = np.zeros((100,100)) # 0 lardan oluşan 100,100 bir matris oluşturur.
Dizi10 = np.ones((100,100)) # 1 lerden oluşan 100,100 lük bir matris oluşturur.
Dizi11 = np.random.random((100,100)) # 0,1 arasında random değerlerden 100,100 bir matris oluşturur.

Dizi12 = np.sort(Dizi11, axis = 0)# Diziyi sıralar, axis = None Tüm elemanları sıralar, Axis = 1 Satır satır sıralar, Axis = 0 Sütun sütun kendi aralarında sıralar.

