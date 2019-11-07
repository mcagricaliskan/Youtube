import cv2
from PIL import ImageGrab
import numpy as np


Resim = cv2.imread("RGB.jpg")
Ekran = ImageGrab.grab()

EkranGor = np.array(Ekran.getdata(), dtype='uint8').reshape((Ekran.size[1],Ekran.size[0],3))
EkranGor = cv2.cvtColor(EkranGor, cv2.COLOR_BGR2RGB)
EkranGor = cv2.resize(EkranGor, (1024,768))
cv2.imwrite("Kayıt.jpg", EkranGor)



while True:
    cv2.imshow("Pencere", EkranGor)

    key = cv2.waitKey(0)
    if key == ord("s"):
        cv2.destroyAllWindows()
        break