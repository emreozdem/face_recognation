import cv2
import os

cam = cv2.VideoCapture(0) 
cam.set(3, 640) # video genişiliğini ayarlama
cam.set(4, 480) # video yükseklliğini ayarlama
face_detector = cv2.CascadeClassifier('Cascades\haarcascade_frontalcatface.xml') 

face_id = input('\n Kullanıcı için bir id(numara) belirleyiniz ve Enter''a basınız  ')
print("\n Yüz yakalama programı başlatılıyor! Kameraya bakınız...")

count = 0
while(True):
    ret, img = cam.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        # Yüz fotoğraflarını database klasörüne kaydeder
        cv2.imwrite("database/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        
        cv2.imshow('Veri Toplama', img)
    k = cv2.waitKey(100) & 0xff # ascii tablosunda tanımlı tuş bekleme
    if k == 27: #beklenen tuş ESC ise programı kapatır
        break
    elif count >= 50: # 50 FOTOĞRAF ÇEKER 
         break

print("\n Kapatılıyor ve temizleniyor!")
cam.release()
cv2.destroyAllWindows()
