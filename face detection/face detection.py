import cv2

alg = "haarcascade_frontalface_default.xml" #initialing path file

haar_cascade = cv2.CascadeClassifier(alg) #loading algorithm

cam = cv2.VideoCapture(0) #cam id initialization

while True:
    _,img = cam.read()

    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face = haar_cascade.detectMultiScale(grayImg,1.3,4) #getting coordinates

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 
    cv2.imshow("FaceDetection",img)
 
    key = cv2.waitKey(10)
    if key ==27:
        print(key)# 27 is escap key value
        break
cam.release()
cv2.destroyAllWindows()    



    
