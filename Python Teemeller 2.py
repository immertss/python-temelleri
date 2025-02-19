faiz=1.59
vade=36
krediAdi= "İhtiyaç kredisi"


print(type(faiz))
print(type(vade))
print(type(krediAdi))
print(int(vade +12)) #string deeğer int yazılarak int olabilir eğer ki sayısal değerse 
faiz=str(faiz)
print(type(faiz)) #str yazılarak string olabilir
vade=int(input("Kaç yıllık vade olsunb istersiniz ?"))
print(vade) #input fonksiyonu kullanıcıdan veri alır
print(type(vade)) # kullanıcıdan alınan veri str dir print(int(vade+12)) yaparak str işlem yaptırasbiliriz ya da
# vade=int(input("VADE3Yİ GİR : ")) şeklinde de int yapabiliriz kullanıcının girişini

vade=int(vade+12)
#string interpolaiton
#seçttiğiniz vade sonucu ortaya çıkan vade : 
# print("seçtiğiniz vade sonucu ortaya çıkan vade :" + str(vade))
# print("seçtiğiniz vade sonucu ortaya çıkan vade : {vadesayisi}".format(vadesayisi=vade))
print(f"seçtğiniz vade sonucun ortaya çıkan vade : {vade}")

isim= input("İSMİNİZİ GİRİNİŞZ :")
metin="Merhaba {name}".format(name=isim)
print(metin) #string interpolaiton

## f-string
metin=f"Hoşgeldiniz {isim}"
print(metin)

#listeler
#listeler bir dizi değerden oluşur
#listeler parantez içinde değerleri virgül ile ayırarak yazılır
#listeler değişken olabilir
#listeler index ile tüm işlemler yapılabilir
krediler=["ihtiyaç kredisi", "taşıt kredisi", "konut kredisi" ]
print(type(krediler))
print(krediler)
print(krediler[0]) #,indexler 0 dan başlar listenin ilk elemanı 0. indextir
print(len(krediler)) #lenght uzunluk liste uzunluğunu 

# dizia=["ihtiyaç kredisi", 5 ,7.9, "taşıt kredisi", True]
# print(type(dizia))

krediler.append("özel kredi")
print(krediler) #append eklemek için kullanılır

krediler.append("okulş kredisi")
print(krediler)

krediler.pop(0)
#pop silmek için kullanılır default verilersee -1 olaraak alır -1 son elemanı ifade eder 

krediler.remove("özel kredi")
#remove silmek için kullanılır fakat remove değer ile kullanılır. 
krediler.extend("Y kredisi", "Z kredisi")
#extend eklemek için kullanılır default olarak listeye ekler

#döngüler
#for döngüsü 
# i=0 i<10 döngü devam 
x=23
for i in range(x):
    print("xxx")
    print(i)
print("***************************************")
for i in range(1,10):
    print(i)
print("***************************************")

for i in range(0,51,10): # range içindeki ilk eleman başlangıç ikinci bitiş üçüüncü artış sayısı  
    print(i)

kredier=["ihtiyaç kredisi", "taşıt kredisi", "konut kredisi" ]
for kredi in kredier:
    print(kredi)

print("********************************************")
for i in range(len(kredier)):
    print(kredier[i])
print("**************************************************************")


#sonsuz döngü
# while True:
#     print("y")
# print("u")
c=1
while c<=7:
    print("y")
    c+=1

while True:
    print("x")
    break
#break döngüden çıkarmak için kullanılır.
print("******************************")
p=0
while p<len(kredier):
    p+=1
    print(p)
    print(kredier[i])
    if kredier[p]=="taşıt kredisi":
        break

#fonksiyonlar 
fiyat =100
indirim=60
def kdv_hesapla(fiyat,indirim): #fiyat ve indirim paraametre olmuş olur. parametre kullanmak için fonksiyondaki parantez içini doldurmalıyız.
    print(fiyat+indirim)
kdv_hesapla(40,20)
kdv_hesapla(70,60)

def sayhello(name):
    print(f"Merhaba {name}")
sayhello("MERT")


def calculate():
    print(100-30)
calculate()

def calculateandreturn(price,discount):
    return price-discount
yenifiyat=calculateandreturn(200,50)
print(yenifiyat)

def calculateprice( price, discount):
    print(price-discount)

def calculatepriceandreturn(price, discount):
    return price-discount

print("*************************************")
fonk1= calculateprice(100,25)
fonk2= calculatepriceandreturn(100,12)
print(f"138. satyır {fonk1}")
print(f"139. satyır {fonk2}")
