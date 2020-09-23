import cv2
import numpy as np
from PIL import Image
import os
# data base klasörü path olarak tanımlanır
path = 'database'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("Cascades\haarcascade_frontalcatface.xml");
# database klasöründe oluşturulan resimleri ve isim etiketlerini alan fonksiyon
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # gri tonlamaya çevirme
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids
print ("\n Tüm yüzler taranıyor ... Lütfen bekleyiniz...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
# Öğrenme modelini trainer.yml olarak kaydeder
recognizer.write('trainer/trainer.yml')

print("\n{0} yüz algılandı. Program kapatılıyor...".format(len(np.unique(ids))))
