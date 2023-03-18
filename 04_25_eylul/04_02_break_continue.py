# region break-continue nedir ve  neden kullanılır?
"""
break    ->döngüyü sonlandırır
continue ->tepeye geri döndürecek
"""
# endregion
"""
i=1
while i<11:
    if i==5:
        break
    print(f"{i}.döngü")
    i+=1

"""
"""
#Break burda içteki döngüyü kırıyo ve kod ala devam ediyor
i,j=0,0
while i <5:
    while j<5:
        if j==3:
            break
        print(f"{i}-{j}",end="")
        j+=1
    i+=1
    print()
    j=0
#continue
i=1
while i<11:
    if i==5:
        i+=1
        continue
    print(f"{i}.döngü")
    i+=1

i=1
print("a")
    while i<=5:
        if i==3:
            i+=1
        continue
    print("b")
    i+=1
print("c")

i=1
print("a")
while i<100:
    if i%7==0:
        i+=1
        continue
    elif i%15==0:
        break
    print(f"{i}")
    i+=1
print("c")
"""
"""
#Girilen 5 sayıdan en büyüğünü ekrana basar
eb=-9999999999999
say=0
while True:
    sayi=int(input("Lütfen sayı giriniz,çıkmak için -1 sayısını giriniz:"))
    if sayi==-1:
        break
    say+=1
    if sayi>eb:
        eb=sayi
if say==0:
    print("Hiçbir sayı girmediniz")
else:
    print(f"En büyük sayi {eb}")
"""

"""
45-50
44-40

sayi=33
birler=sayi%10
onlar=sayi//10
if birler>4:
        onlar+=1
        print(f"{onlar}0")
else:
    print(f"{onlar}0")
#print(onlar,birler)
"""

"""
Lütfen tek sayı giriniz,çıkmak için -1:5
Lütfen tek sayı giriniz,çıkmak için -1:7
Lütfen tek sayı giriniz,çıkmak için -1:6
Sadece tek sayı girilmeli
Lütfen tek sayı giriniz,çıkmak için -1:11
Lütfen tek sayı giriniz,çıkmak için -1:-1
Girilen 3 adet tek sayının toplamı:23
"""
"""
tekAdet=0
tekToplam=0
while True:
    sayi=int(input("Lütfen tek sayi giriniz,çıkmak için -1 giriniz: "))
    if(sayi==-1):
        break
    elif(sayi%2==1):
        tekAdet+=1
        tekToplam+=sayi
        
    else:
        print("Sadece tek sayı girilmeli")
print(f"Girilen tek sayı adeti={tekAdet} ve tek sayıların toplamı={tekToplam}")

"""
"""
[1] km->mil
[2] mil->km
[3] çık
"""
#menu 

while True:

    secim=input("Lütfen seçim yapınız: ")
    if secim=="1":
        km=int(input("Lütfen km bilgisini giriniz: "))
        mil=km*0.62137
        print(mil)
    elif secim=="2":
        mil=int(input("Lütfen mil bilgisini giriniz: "))
        km=km/0.62137
        print(round(km, 2))
    elif secim=="3":
        print("Çıkış yapıldı")
    else:
        print("Hatalı tuşlama yaptınız")