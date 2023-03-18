"""
s1=30
s2=10
print("
       Lütfen cevaplamak istediğiniz soruyu giriniz
       [1-4]
")
soru=int(input())
if soru==1:
    cevap=int(input(f"{s1}+{s2}= "))
    if cevap==40:
        print("Doğru")
    else:
        print("Yanlış")
elif soru==2:
    cevap=int(input(f"{s1}-{s2}= "))
    if cevap==20:
        print("Doğru")
    else:
        print("Yanlış")
elif soru==3:
    cevap=int(input(f"{s1}*{s2}= "))
    if cevap==300:
        print("Doğru")
    else:
        print("Yanlış")
elif soru==4:
    cevap=int(input(f"{s1}/{s2}= "))
    if cevap==3:
        print("Doğru")
    else:
        print("Yanlış")
else:
    print("Yanlış seçim")
"""

"""
A kenarını giriniz=10
B kenarını giriniz:20
Dikdörtgenin alanı=200

A kenarını giriniz=10
B kenarını giriniz:10
Karenin alanı=100
"""
"""
aKenari=int(input("A kenarını giriniz= "))
bKenari=int(input("B kenarını giriniz= "))
alan=aKenari*bKenari
if aKenari==bKenari:
    print(f"karenin alanı= {alan} ")
else:
    print(f"dikdörtgenin alanı = {alan}  ")
"""

"""
Lütfen kısa kenarı giriniz=
Lütfen uzun kenarı giriniz=
Uzun kenar kısa kenardan küçük girilemez
"""
"""
kKenar=int(input("Lütfen kısa kenarı giriniz= "))
uKenar=int(input("Lütfen uzun kenarı giriniz= "))
if kKenar<uKenar:
    print("Dikdörtgendir")
elif kKenar==uKenar:
    print("Karedir")
else:
    print("Uzun kenar kısa kenardan küçük girilemez")
"""


"""
Ekrana iki tane sayı girilir ve
birbirlerine bölünüp/bölünmediğine bakılır
"""
s1=int(input("1.sayiyi giriniz= "))
s2=int(input("2.sayiyi giriniz= "))

if s2==0:
    print("Payda 0 olamaz")
else :
   if s1%s2==0:
        print(f"{s1} sayısı {s2} sayısına bölünür")
   else:
        print(f"{s1} sayısı {s2} sayısına bölünmez")
    
