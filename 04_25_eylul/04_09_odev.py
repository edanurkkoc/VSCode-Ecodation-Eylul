"""
Ödev 
Lütfen Sayı Giriniz, Çıkmak İçin 0 : 5 
Lütfen Sayı Giriniz, Çıkmak İçin 0 : 148 
Lütfen Sayı Giriniz, Çıkmak İçin 0 : 7 
Lütfen Sayı Giriniz, Çıkmak İçin 0 : 0 
Output 
2 Adet TEK HANELİ sayı girdiniz 
0 Adet İKİ HANELİ sayı girdiniz 
1 Adet ÜÇ HANELİ sayı girdiniz 
"""
tek_basamak=0
iki_basamak=0
uc_basamak=0
sayi=int(input("Lütfen Sayı Giriniz, Çıkmak İçin 0 :\t"))
while sayi!=0:
    if sayi>0 and sayi<10:
        tek_basamak+=1
        sayi=int(input("Lütfen Sayı Giriniz, Çıkmak İçin 0 :\t"))
        
    elif sayi>=10 and sayi<100:
        iki_basamak+=1
        sayi=int(input("Lütfen Sayı Giriniz, Çıkmak İçin 0 :\t"))
        
    elif sayi>=100 and sayi<1000:
        uc_basamak+=1
        sayi=int(input("Lütfen Sayı Giriniz, Çıkmak İçin 0 :\t"))
print(f"0 ariç {tek_basamak} adet tek basamak, {iki_basamak} adet iki basamak,{uc_basamak} adet üç basamak sayı vardır")

    