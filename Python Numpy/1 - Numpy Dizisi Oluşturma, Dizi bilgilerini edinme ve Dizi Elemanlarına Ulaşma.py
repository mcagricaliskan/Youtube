import numpy as np


Dizi1 = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]
])

print(Dizi1.ndim) # Numpy dizisinin kaç boyutlu olduğunu.
print(Dizi1.shape) # Numpy dizisinin şeklini gösterir.
print(Dizi1.size) # Numpy dizisinin toplam elaman sayısını verir.
print(Dizi1.dtype) # Numpy dizisinin tipini gösterir.

Dizi2 = Dizi1.flatten() # Numpy dizisinin düz bir hale gelmesini sağlar.


Liste = [1,2,3,4,5,6]
Dizi3 = np.array(Liste) # Listeyi Numpy Dizisine Çevirir
Liste2 = list(Dizi3) # Numpy Dizisini Listeye çevirir

print(Dizi1[2][0])

Dizi4 = np.linspace(0,100,200) # 0 dan 100 e kadar 200 tane veri olacak şekilde dizi oluştur.

Dizi5 = np.arange(0,100,5) # 0 dan 100 e kadar 5 er atlayarak bir dizi oluştur.

Dizi6 = Dizi1[1:3,1:3] # sadece ":" tüm hepsini almayı sağlar, "buradan başla: buraya kadar al"


Dizi7 = np.zeros((100,100)) # Tamamen 0 lardan oluşan 100e100 lük bir matris oluşturur.
Dizi8 = np.ones((100,100)) #Tamamen 1 lardan oluşan 100e100 lük bir matris oluşturur.
Dizi9 = np.random.random((100,100)) # 0 ile 1 arasında random 100e100 lük bir matris oluşturur.
Dizi10 = np.array([214,256346,8765,67,423,21345,23])
Dizi11 = np.sort(Dizi10, axis=None) # axis=None tüm numpy dizisini sılar, axis= 1 satır satır sıralma axis=0 sütun sütun sıralama yapar.
print(Dizi11)