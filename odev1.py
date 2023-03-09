#string metinsel ifadeler için kullanılır
#int tam sayı değerler için kullanılır
#float ondalıklı sayılar için kullanılır 
#Mantıksal veri tipleri   Bool yapısı doğru veya yanlış (true/false) mantığı ile çalışır.
#Sequence (sıralama, dizi) veri tipleri  List birden fazla veri dizisini tek bir tipte birleştirmeyi sağlarken içinde string, int ve float değerler barındırabilir. Range bir fonksiyon olarak çalışmakla birlikte genellikle döngülerin içerisinde kullanılır. Tuple ise parantez ile çalışan, dizi oluşturan bir yapıdır ve sıralı bir biçimde oluşturulmaktadır.
#Mapping (haritalama, adresleme) veri tipleri Dict veri tipi sözlük oluşturmakta işe yarayan bir veri tipidir.
#Set (küme) veri tipleri  Kümeler birden çok öğeyi tek bir değişken içerisinde tutmak için kullanılır ve süslü parantez ile yazılır. Set ve Frozenset olarak ikiye ayrılır. 
#Binary veri tipleri  Bytes verilmiş olan boyutta ve girilen verilerle başlatılan değişmez bir bayt nesnesini kendi içerisinde döndürürken, Bytearray byte veri tipinde oluşturulan veriler üzerinde değişiklik için yapmakta kullanılır.  Memoryview ise Python’da bellek durumunu görüntülemek için kullanılır.

kursAdi="(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium"
yüzdeKacTamamladi=50
kurslar=["c# Yetiştirme Kampı","python","Java","JS"]
eğitmenler=["Engin Demiroğ","Halit Enes Kalaycı"]
for kurs in kurslar:
    print(kurslar[0]+" : "+eğitmenler[0])
    print(kurslar[1]+" : "+eğitmenler[1])
    print(kurslar[2]+" : "+eğitmenler[0])
girisYapmisMi=True
if girisYapmisMi==True:
    {
        print("ayarlar")
    }
else:
    {
        print("Giriş Yap Yada Kayıt Ol")
    }