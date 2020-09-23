# face_recognation
Python ve OpenCv kullanarak yazdığım yüz algılama ve tanıma uygulamasıdır.

!! NASIL ÇALIŞIR !!
Yüz algılama ve tanıma sistemim 3 aşamadan oluşmaktadır:
1 ** Veri Toplama
2 ** Programı Eğitme
3 ** Tanımlayıcıyı Başlatma

--VERİ TOPLAMA--
Öncelikle yüz tanıma uygulamamızın çalışması için veri tabanına ihtiyacımız olacaktır.
Bunun için veritoplama.py adlı dosyamızı çalıştırarak database klasörümüze yüzümüzün fotoğrafları yüzümüz her algılandığında kaydedilecektir.
Daha sonra bu dosyayı tekrar çalıştırarak farklı kişilerin yüzlerini farklı id'ler ile databse'e ekleyebilirsiniz.

--PROGRAMI EĞİTME--
Eğer databse klasörümüze ilk defa fotoğraflar eklenmişse ya da tekrar kullanılarak database zenginleştirilmiş ise trainer klasöründe bulunan trainer.py çalıştırılmalıdır
Bu dosyanın çalıştırılması fotoğraflar kullanılarak bir sonraki aşama için eğitilmiş trainer.yml adlı bir model oluşturacak.

--Tanımlayıcıyı Başlatma--
Artık tanımlama.py adlı dosyayı çalıştırarak eğittiğiniz programınızın yüzleri tanımasına tanık olabilirsiniz...
