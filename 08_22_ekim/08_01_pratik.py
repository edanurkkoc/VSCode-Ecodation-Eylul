import random
rSayi = random.randint(1,100) #Bilgisayarın ürettiği random sayı
enKucukFark = 101;tahmin=0
for i in range(3):  #Kullanıcıdan istenen 3 sayı
    s = int(input("lütfen sayı tahmini yapın : "))
    fark = abs(rSayi-s)  #abs -> içeriyi pozitif yaptı
    if fark<enKucukFark:
        enKucukFark = fark
        tahmin = s
print(f" random sayımız ={rSayi}ve en yakın {tahmin}")