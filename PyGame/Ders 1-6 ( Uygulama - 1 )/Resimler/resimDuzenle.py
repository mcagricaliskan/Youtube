import cv2


copkovasi = cv2.imread("CopKovasi.png")
kagit = cv2.imread("kagit.jpg")
sehir = cv2.imread("sehirTemasi.jpg")


yeniCopKovasi = cv2.resize(copkovasi,(100,100))
yeniKagit = cv2.resize(kagit,(20,20))
yeniSehir = cv2.resize(sehir,(1280,1000))



cv2.imwrite("yeniCopkovasi.jpg",yeniCopKovasi )
cv2.imwrite("yeniKagit.jpg",yeniKagit )
cv2.imwrite("yeniSehir.jpg",yeniSehir )






"""
while True:
    cv2.imshow("Pencere", yeniSehir)
    if cv2.waitKey(25) and 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
"""