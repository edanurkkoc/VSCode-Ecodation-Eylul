#region string_metodları
""" 
upper() lower() title() capatilize()
count() replace() swapcase()
startswit() endswit()
strip() lstrip() rstrip()
isdigit() isalpa()
isalpanum() isspace() istitle() isidentifier()
split() index() find() format()
isinstance()
"""
#endregion

#tüm veri tipleri objeden türer
"""
ad="eda"
yas=21
pi=3.14

#upper() lower() title() capatilize()
ad="şakiRR"
result=ad.upper()#string ifadenin tüm arflerini büyütüp yazdırdı ekrana
result=ad.lower()#string ifadeyi tüm arflerini küçültüp yazdırdı ekrana 
#result=input("type q/Q to exit : ")
#if result=="q" or result=="Q":
#   print("Peki o zaman sizi özleyeceğiz")
#if result.lower()=="q":
#    print("Peki o zaman sizi özleyeceğiz")
#print(result)


ad="şakir kayadan"
result=ad.title()
result=ad.capitalize()
#count() replace() swapcase()
result=ad.count("a")#a arfinden kaç tane varsa ekrana basıyor
url="https://www.okan.com.tr"
print(url.replace("com.tr","edu.tr"))#com.tr yi edu.tr ile yer değiştir
url=url.replace("com.tr","edu.tr")
yorum="bu kelime sansürlenecek"
yorum=yorum.replace("sansürlenecek","...")
print(yorum)
"""
"""
#print(url)
###########################################
kotuKelimeler=["tüğ","kaka","serseri","kötü"]
yorum="Bu kötü kelimeler sansürlenecek"
for i in kotuKelimeler:
    if i in yorum:
        yorum=yorum.replace(i,"....")
print(yorum)
"""
"""
kurum="Tuzla Meslek Lisesi"
result=kurum.swapcase()#Büyük ve küçük arfler yer değiştiriyor

#startswit() ve endswit()
url="https://www.okan.com.tr"
result=url.startswith("www")#bununla mı başlıyo,öyleyse True,değilse Fale(boolean fonks)
result=url.endswith("com")#bununla mı bitiyo,öyleyse True,değilse Fale(boolean fonks)
print(result)
"""

"""
#strip() lstrip() rstrip()
kurum="         Tuzla Meslek Lisesi"
print(len(kurum))
result=kurum.strip()
result=kurum.ltrip()
result=kurum.rtrip()
print(result)
print(len(result))

#isdigit()->girilen değer sayı mı ve isalpha()->girilen değer arf mi
result="1"
result="106"
result="_22"
print(result.isdigit())#true/false
#sayi=input("Lütfen bir sayi giriniz:  ")
deger="birnci ders"
result=deger.isalpha()#a...z A..Z
#Alfanumerik
#a...z A..Z 0...9
deger="1.nci ders"
result=deger.isalnum()
#isalpanum() isspace() istitle() isidentifier()
#split() index() find() format()
#isinstance()

deger="     "
result=deger.isspace()
deger="TUMUBUYUKKARAKTER"
result=deger.isupper()
deger="Tuzla meslek"
result=deger.istitle()
result="ad".isidentifier()
result="1ad".isidentifier()
#print(result)

kurumAdi="Tuzla Mesleki ve Anadolu Lisesi"
result=kurumAdi.split()
#print(type(result)) ##Geriye list dönürür yani türü listedir
"""
#-----------------------ÖDEV--------------------------------------------------------
#splitten sonra captalize ile ilk arf büyük olsun
"""word, belgenizin profesyonelce üretilmiş görünmesini sağlamak için birbirini 
tamamlayan üst bilgi, alt bilgi, kapak sayfası ve metin kutusu tasarımları sağlar
"""

yorum= "word, belgenizin profesyonelce üretilmiş görünmesini sağlamak için birbirini tamamlayan üst bilgi, alt bilgi, kapak sayfası ve metin kutusu tasarımları sağlar. örneğin, birbiriyle uyumlu bir kapak sayfası, başlık ve kenar çubuğu ekleyebilir misiniz? ekle'ye tıklayın! ardından farklı galerilerden eklemek istediğiniz öğeleri seçin."
x=0
cumleler=[]
for i in range(len(yorum)):
    if yorum[i] in ".!?":
        cumleler.append(yorum[x:i])
        x=i+2
print(cumleler)
