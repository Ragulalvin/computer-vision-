import cv2
img=cv2.imread("RRA2.jpg")
cv2.imshow('show',img)
cv2.imwrite('photo.png',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
