print("kodlama")
baslik="Taşıt Kredisi"
print(baslik)
baslik= "ihtiyac kredisi"
print(baslik)
##int integer -> sayısal değer
##float float -> ondalık değer
##str string -> metin
vade= 36
ekvade=12
vade2= "36"
vade +=2
vade+=2
aylikodeme=200.58
#bool, boolean -> true ya da false değeri
yukselisteMi =False
#matematiksel operatörler 
print(5+5)
print(vade+6)
print(vade+ekvade)

print(5-5)
print(vade-6)
print(vade-ekvade)

print(5*5)
print(vade*6)
print(vade*ekvade)

print(5/5)
print(vade/6)
print(vade/ekvade)
# mod alma
print(5%5)
print(vade%6)
print(vade%ekvade)

yenivade= vade/2
fiyat=100
indirimlifiyatt= fiyat-43
print(yenivade)
print(indirimlifiyatt)

#mantıklsal operatörler
# CTRL K, CTRL C
# print(2==2)
# print(3<1)
# print(3>=2)
# print(1!=7
# and
# or
# not
print(1 > 2 or 2 < 5 )
print(1!=2 and 2>= 9 or 3<5)
print(1<0 and 2>3 and 0<9)

#karar yapıları 
# if 
# elif
# else
s1= 10
s2= 15
#condition

#indent 
if s1 > s2:
    print("s1 daha büyük")
#eğer if false ise 
elif s1==s2:
    print("s1 ve s2 eşit")
# eğer elif bloğu false olursa çalışsın
else:
    print("s2 daha büyük")
print(" if den çıktın ")

# if s1==s2:
#     print("s1 ve s2 eşit")
# if s1>=s2:
#     print("s1 daha büyük")
# else: 
#     print("s2 daha büyük") iflerin bağlantısı kesiliyor ard arda iki if eklersek 