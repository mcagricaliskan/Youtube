import numpy as np


Dizi1 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

Dizi98 = np.array([10,11,12])

Dizi99 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

Dizi2 = np.array([[13,14,15,16],
                  [17,18,19,20],
                  [32,16,108,19],
                  [67,39,48,92]])


Dizi3 = Dizi1+99 # Matrisin her elemanın 99 ekler.
Dizi4 = Dizi1-99 # Matrisin her elemanın 99 çıkartır.
Dizi5 = Dizi1*99 # Matrisin her elemanın 99 ile çarpar.
Dizi6 = Dizi1**2 # Matrisin her elemanın karesini alır.

Dizi7 = Dizi2.sum() # Dizi elemanlarınn toplamı
Dizi8 = Dizi2.max() # Dizi elemanlarından en büyük olanı bulur
Dizi9 = Dizi2.min() # Dizi elemanlarından en küçük olanı bulur


Dizi10 = Dizi2.T # Matrisin Transpozunu alır.

Dizi11 = Dizi1+ Dizi99 # Diziyi üst üste ekler
Dizi12 = np.add(Dizi1,Dizi99) # Diziyi üst üte ekler

Dizi13 = np.square(Dizi1) # Dizi elemanlarının karesini alır

Dizi14 = np.vstack((Dizi1,Dizi99)) # Yeni satır olarak iki diziyi birleştirir. 2. diziyi satır olarak ekler.
Dizi15 = np.hstack((Dizi1,Dizi99)) # Yeni sütun olarak iki diziyi birleştirir. 2. diziyi sütun olarak ekler.

Dizi16 = np.column_stack((Dizi1,Dizi98))  # 3,1 bir diziyi 3,3 bir diziye sütun olarak ekler. 3,4 bir dizi elde etmemizi sağlar
Dizi17 = np.row_stack((Dizi1,Dizi98)) # 3,1 bir diziyi 3,3 bir diziye satır olarak ekler. 4,3 bir dizi elde etmemizi sağlar

Dizi18 = np.vsplit(Dizi2,4) # Dizinin satırlarını 4 e böler # Vertical
Dizi19 = np.hsplit(Dizi2,2) # Dizinin sütunlarını 2 e böler # Horizontal

Dizi20 = np.copy(Dizi2) # Diziyi kopyalar

Dizi21 = Dizi2.reshape(16,1) # Diziyi yeniden şekillendirmenize olanak sağlar

Dizi22 = Dizi1 * Dizi98 # MAtris elemanlarını bir biri ile çarpar
Dizi23 = np.dot(Dizi1,Dizi98) # Matris Çarpımı
