import cv2, os
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'
sub_data = 'ragul alvin'

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) = (130,100)


face_cascade = cv2.CascadeClassifier(haar_file)

webcam = cv2.VideoCapture(0)

count = 1
while count < 51:
    print(count)
    (_,im) = webcam.read()

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x,y,w,h) in face:
        cv2.rectangle(im, (x,y) ,(x+w,y+h), (255,0,0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path,count), face_resize)
    count += 1

    cv2.imshow('opencv', im)
    key =cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()

