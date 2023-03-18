"""rakam=int(input("lütfen 0-9 arası bir rakam giriniz="))
print("Girdiğiniz rakamın 1 fazlası=" +str((rakam+1)))"""


"""Format Kullanımı"""
"""
rakam=int(input("lütfen 0-9 arası bir rakam giriniz="))
print("Girdiğiniz rakamın 1 fazlası= {}".format(rakam+1))
"""

"""
a=5
b=10
c=a+b
print("grilen {} ve {} değerlerinin toplamı {}".format(a,b,c))
"""
"""
a=5
b=10
c=a+b
print(f"girilen {a} ve {b} değerlerinin toplamı {c}")"""


"""
Lütfen 1.sayıyı giriniz->5
Lütfen 1.sayıyı giriniz->10
Lütfen 1.sayıyı giriniz->45
Girilen 5,10,45 sayılarının ortalaması 20.0
"""
"""
sayi1=int(input("Lütfen 1.sayıyı giriniz="))
sayi2=int(input("Lütfen 2.sayıyı giriniz="))
sayi3=int(input("Lütfen 3.sayıyı giriniz="))
ort=(sayi1+sayi2+sayi3)/3
print(f"Girilen {sayi1},{sayi2},{sayi3} sayılarının ortalaması->",ort)"""

"""
boy=int(input("Lütfen boy bilgisi giriniz->"))
m=boy//100
cm=boy%100
print(f"Boyunuz {m} metre ve {cm} santimetredir")"""

"""
sehir=input("yaşadığınız sehir->")
#Girdiğiniz ankara şehrinin uzunluğu 6
print(f"girdiğiniz{sehir} serinin uzunluğu ",{len(sehir)})"""

"""
Yarıçap bilgisini giriniz->10
10 cm yarıçap bilgisine sahip dairenin alanı .... cm kare,çevresi ... cm dir
"""
"""
yaricap=int(input("Yarıçap bilgisini giriniz->"))
alan=3.14*(yaricap**2)
cevre=2*3.14*yaricap
print(f"{yaricap} cm yarıçap bilgisine sahip dairenin alanı {alan} cm kare,çevresi",round(cevre,3),"cm dir")
"""


"""
saat=2
ekrandaki 2 saaat değerinin saniye karşılığı 7200 saniyedir
"""

saat=int(input("Saat bilgisini giriniz->"))
saniye=(saat*60) *60
print(f"Ekrandaki {saat} saat değerinin saniye karşılığı {saniye} saniyedir")



























