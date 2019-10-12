import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascade/haarcascade_eye.xml')



cam = cv2.VideoCapture(0)
i=0
k=0
while (True):

    ret, frame = cam.read()



    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
       if(i==20):
           i=0

       cv2.rectangle(frame, (x, y), (x + w, y + h), (60, 20, 220), 2) #BGR
       print("Rosto: ",x,y,w,h)
       arquivo="Rostos/rosto - ("+str(i)+").png"

       i = i + 1


       gray_rosto = gray[y:y + h, x:x + w]
       color_rosto = frame[y:y + h, x:x + w]
       cv2.imwrite(arquivo,color_rosto)

       rostoarm = cv2.imread(arquivo,0)

       eyes = eye_cascade.detectMultiScale(gray_rosto)

       for (ex, ey, ew, eh) in eyes:
          cv2.rectangle(color_rosto, (ex, ey), (ex + ew, ey + eh), (112, 25, 25), 2)
          print("Olhos: ",ex,ey,ew,eh)

          file = "Rostos/olhos - (" + str(k) + ").png"

          k = k + 1
          img_item_olho = file
          k = k + 1

          color_olho = frame[y:y + h, x:x + w]


          ##olho_gray = cv2.imread(file, 0)


    cv2.imshow('Deteccao', frame)
    #cv2.imshow('Rosto Capturado',rostoarm)
    #cv2.imshow('Olho',color_olho)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Saindo do Reconhecimento")
        break

cam.release()
cv2.destroyAllWindows()