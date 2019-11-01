import numpy as np


Dizi1 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

Dizi10 = np.array([[30,31,32],
                   [33,34,35],
                   [36,37,38]])

Dizi2 = np.array([10,11,12])

Dizi3 = np.array([[13,14,15,16],
                  [17,18,19,20],
                  [32,16,108,19],
                  [67,39,48,92]])



Dizi4 = Dizi1+99 # Her bir elemana bir sayı ekler.
Dizi5 = Dizi1-1 # her bir elemandan bir sayı çıkartır
Dizi6 = Dizi1*100 # Her bir elemanı bir sayı ile çarpar
Dizi7 = Dizi1**2 # Her bir elemanın kare alır.

Dizi1Toplam = Dizi1.sum() # Dizi elemanlarının toplamını verir
Dizi1Maksimum = Dizi3.max() # Maksimum değere ulaşır
Dizi1Min = Dizi3.min() # Minimum değere ulaşır



Dizi8 = Dizi3.T # Matrisin Transpozunu alır.

Dizi9 = Dizi1 + Dizi10 # Diziyi üst üste ekler
Dizi11 = np.add(Dizi1,Dizi10) # Diziyi üst üte ekler

Dizi12 = np.square(Dizi3) # Dizi elemanlarının karesini alır


Dizi13 = np.vstack((Dizi1,Dizi10)) # SAtır olarak ekler # Vertical
Dizi14 = np.hstack((Dizi1,Dizi10)) # Sütun olarak ekler # Horizontal

Dizi15 = np.column_stack((Dizi1,Dizi2)) # 3,1 bir diziyi 3,3 bir diziye sütun olarak ekler. 3,4 bir dizi elde etmemizi sağlar

Dizi16 = np.vsplit(Dizi3,2) # Dizinin satırlarını 2 ye böyler # Vertical
Dizi18 = np.hsplit(Dizi3,2) # Dizinin Sütunlerini 2 ye böler # Horizontal

Dizi19 = np.copy(Dizi10) # Diziyi kopyalar


Dizi20 = Dizi3.reshape(8,2) # Diziyi yeniden şekillendirmenize olanak sağlar

Dizi21 = Dizi1*Dizi10 # MAtris elemanlarını bir biri ile çarpar

Dizi22 = np.dot(Dizi1,Dizi2) # Matris Çarpımı
