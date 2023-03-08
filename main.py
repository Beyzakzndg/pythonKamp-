print("Hello World")
baslik="Taşıt Kredisi"
print(baslik)

vade=36
ekVade=6
vade2="36"
#float
aylikOdeme=200.60
#bool
yukselisteMi=True
#operatörler

#Toplama(+)
print("*******TOPLAMA*********")
print(5+5)
print(vade+12)
print(vade+ekVade)
print("*******ÇIKARMA*********")
#çıkarma(-)
print(5-5)
print(vade-12)
print(vade-ekVade)
print("*******ÇARPMA*********")
#Çarpma(*)
print(5*5)
print(vade*12)
print(vade*ekVade)
print("*******BÖLME*********")
#BÖLME(/)
print(5/5)
print(vade/12)
print(vade/ekVade)
print("**********************")
yeniVade=vade
fiyat=100
indirimliFiyat=fiyat-20
print(yeniVade)
print(indirimliFiyat)
#mod alma
print(10%2)
print(vade%5)
print(30%10)
#mantıksal operatörler
print(1==1)
print(1==2)

print(1>2)
print(3>1)
print(1>1)
print(1>=1)
print("*****küçükür******")
print(1<2)
print(3<1)
print(1<1)
print(1<=1)
print("******eşit değildir*******")
print(1!=1)
print(1!=2)

#or and keyword
print(1>2 or 5>2)
print(1>2 and 5>2)
print("***quiz***")
print(1>2 or 5>2 and 3>2)
print(1>2 and 5>2 and 3>2)
print(2>1 or 1>2 and 3>2)

#karar yapıları
#if elif else

sayi1=10
sayi2=15
if sayi1>sayi2:
    {
        print("Sayı1 Büyük")
    }
elif sayi1<sayi2:
    {
        print("Sayı2 büyük")
    }
else:
    {
        print("Sayı1=Sayı2")
    }