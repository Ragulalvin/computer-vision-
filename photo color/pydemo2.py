import cv2
img=cv2.imread("RRA2.jpg")
grayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('orginal',img)
cv2.imshow('Gray',grayImage)
cv2.imwrite('graynew.jpg',grayImage)
