import cv2
import numpy as np
import os 

recognizer = cv2.face.LBPHFaceRecognizer_create() #OpenCv yüz tanıma fonksiyonu recognizer içinde çalıştırılır
recognizer.read('trainer/trainer.yml') #recognizer eğittiğimiz trainer.yml verisini okur
cascadePath = "Cascades\haarcascade_frontalcatface.xml" # Yüz tanıma sınıflandırıcısının dosya konumu
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX #id yi yazdırıcak yazı fontu 

#id sayacı 0'dan başlatılır
id = 0

#id'ile sıralı isim listesi, örneğin 1-Emre 2-Samet...
names = ['None', 'Emre','Samet','Ahmet'] 

# Görüntü yakalama tanımlanır ve başlatılır
cam = cv2.VideoCapture(0)
cam.set(3, 640) # görüntü genişliği
cam.set(4, 480) # görüntü yüksekliği


# yüz tanınmlaması için kullanılacak olan minumum pencere boyutu
minW = 0.1*cam.get(3) #genişlik
minH = 0.1*cam.get(4) #yükseklik

while True:
    
    ret, img =cam.read() 
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    
    #yüz algılama
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    
    #yüz üzerine dikdörtgen çizme ve bilgileri gösterme
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w]) #algılanan yüz, yüzün id'si ile eşleştirilir
        
        # 'confidence'(yüz benzerliği) 25 ten büyük ise yüz eşleşmiş olarak kabul edilir
        if (25<confidence):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "bilinmiyor"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2) #isim yazdırma
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1) #benzerlik oranı yazdırma
        
    
    cv2.imshow('Yüz Tanıma',img) 
    k = cv2.waitKey(10) & 0xff # ascii tablosunda tanımlı tuş bekleme
    if (k == 27): #beklenen tuş ESC ise programı kapatır
        break
#Ekran temizlenir
print("\n Kapatılıyor ve temizleniyor!")
cam.release()
cv2.destroyAllWindows()