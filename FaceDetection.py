import cv2
import numpy as np
import keyboard
from matplotlib import pyplot as plt
import pyrebase

#configuration
config = {
   "apiKey": "apikey",
   "authDomain": "ubihacks-com.firebaseapp.com",
  "databaseURL": "https://ubihacks-com.firebaseio.com/",
  "storageBucket": "ubihacks-com.appspot.com",
   #"serviceAccount": "ubihacks.json"
   }

#Inilize Firebse
firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()

#Cam
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, img = cap.read()
    gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces =face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        
    cv2.imshow('FaceDetection BY ubihacks',img)
    #capture Image on Pressing 'c'
    if keyboard.is_pressed('c'):
        print ("Image Capture")
        cv2.imwrite("NewImage.jpg", img)
        #to snd on firebase set Firebase and uncomment the lines below 
        #storage.child("python").child(+"NewImage.jpg").put(NewImage.jpg)
        #data = {"ImageUrl": storage.child("python").child(Date).child(image_name()+".jpg").get_url(1)}  #To get ImageURL
        
    cv2.imwrite("imgr.png", img)
    
    
    k = cv2.waitKey(27) & 0xff
    if k == 27:
        break


cap.release()
cv2.destoryAllwindows()
