#OBEB problemi,iki sayının ortak bölenini ekrana bassın
"""
sayi1=int(input("Bir sayı giriniz= "))
sayi2=int(input("Bir sayı giriniz= "))
ek,obeb=0,0
if sayi1<sayi2:
    ek=sayi1
else:
    ek=sayi2
    for i in range(1,ek+1):
        if sayi1%i==0:
            if sayi2%i==0:
                obeb=i
    print(f"{obeb}")

"""
"""
#Girilen sayı TAU sayısı mı değil mi bul
sayi=int(input("Bir sayi giriniz: "))
adet=0
for i in range(1,sayi+1):
    if sayi%i==0:
        adet+=1
if sayi%adet==0:
        print("TAU sayısıdır")
else:
    print(f"TAU sayısı değildir çünkü {sayi} sayısı {adet} adetine bölünmez")
"""
#Mükkemmel sayı
toplam=0
sayi=int(input("Bir sayi giriniz: "))
for i in range(1,sayi):
    if sayi%i==0:
        toplam+=i
if sayi==toplam:
    print("Mükemmel sayısıdır")
else:
    print(f"Mükemmel sayısı değildir çünkü {sayi} sayısı={toplam} toplamına eşit değildir")

