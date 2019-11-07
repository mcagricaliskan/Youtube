import cv2


Resim = cv2.imread("Test.jpg")

ResimB,ResimG,ResimR = cv2.split(Resim)

# ResimB = Resim[:,:,0]
# ResimG = Resim[:,:,1]
# ResimR = Resim[:,:,2]

Birlesim = cv2.merge((ResimB,ResimG,ResimR))

while True:
    cv2.imshow("Pencere", Resim)
    cv2.imshow("PencereB", ResimB)
    cv2.imshow("PencereG", ResimG)
    cv2.imshow("PencereR", ResimR)
    cv2.imshow("Birlesim", Birlesim)

    key = cv2.waitKey(0)
    if key == ord("s"):
        cv2.destroyAllWindows()
        break